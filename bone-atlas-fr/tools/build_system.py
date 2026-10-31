# Génère bone-atlas-fr/data/<système>.json, le tableau de relecture <système>-noms.csv et la table de
# renommage des nœuds du modèle, à partir de <système>_fr.py (table des noms et réglages du système).
# Usage : python3 -I build_system.py <système> <dossier de travail> <dossier de sortie>
import json, re, sys, csv, unicodedata, collections, importlib.util

SYSN, S, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
spec = importlib.util.spec_from_file_location('cfg', f'{S}/{SYSN}_fr.py'); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
inv = json.load(open(f'{S}/za/inv/{M.INVENTORY}.json'))['list']
lex = json.load(open(f'{S}/za/lexicon.json'))

rows = {}
for line in M.ROWS.strip().splitlines():
    en, tech, usual, sec, kind, group = [x.strip() for x in line.split('|')]
    assert en not in rows, en
    rows[en] = dict(tech=tech.replace("'", '’'), usual=usual.replace("'", '’'), sec=sec, kind=kind, group=group)

def slug(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '_', s).strip('_')

FEM = set(M.FEMININE)
PLURAL = set(M.PLURAL)
def with_side(tech, side):
    """« Muscle grand pectoral gauche », mais « Muscle droit de l’abdomen, côté gauche » quand un complément suit."""
    if not side: return tech
    first = tech.split()[0].lower()
    if first in PLURAL or re.search(r"\b(du|de|des|d’)\b", tech) or re.search(r'\bdroit\b', tech, re.I) or '(' in tech:
        return f"{tech}, côté {'gauche' if side == 'L' else 'droit'}"
    adj = 'gauche' if side == 'L' else ('droite' if first in FEM else 'droit')
    return f'{tech} {adj}'

base_of = lambda n: re.sub(r'\.(l|r)$', '', n)
items, groups, rename = [], collections.OrderedDict(), {}
missing_rows = set()
for m in inv:
    name = m['name']; en = base_of(name).strip()
    side = {'l': 'L', 'r': 'R'}.get(name[-1]) if re.search(r'\.(l|r)$', name) else ''
    if en in getattr(M, 'IGNORE', ()): continue   # unnamed pieces in the source: left out of the page and the model
    r = rows.get(en)
    if not r: missing_rows.add(en); continue
    reg, sub = r['sec'].split('/')
    center = [(m['min'][i] + m['max'][i]) / 2 for i in range(3)]
    zone, turn = M.camera(reg, sub, en, center)
    zr, _, zs = zone.partition('/')
    stem = M.PREFIX + slug(en.strip(' ()*\''))
    if en.endswith("'"): stem += '_2'   # « Central canal' » : second morceau d'une structure de même nom
    iid = stem + ('_' + side.lower() if side else '')
    assert iid not in {d['id'] for d in items}, iid
    rename[name] = iid
    tech = with_side(r['tech'], side)
    label = f"{tech} ({r['usual']})" if r['usual'] else tech
    lx = lex.get(en) or lex.get(f'({en.strip("()")})') or lex.get(en.strip('()')) or {}
    d = {'id': iid, 'name': label, 'tech': tech, 'region': reg, 'sub': sub, 'side': side, 'zr': zr, 'kind': r['kind'],
         'en': re.sub(r'\.l$', ' (left)', re.sub(r'\.r$', ' (right)', name))}
    if zs: d['zs'] = zs
    if lx.get('la'): d['la'] = lx['la']
    if turn: d['turn'] = turn
    gk = None if r['group'] == '-' else (r['group'] or slug(en.strip(' ()*\'')))
    if gk:
        if gk not in groups:
            gname = M.GROUPS.get(gk)
            if gname is None or gname[0] is None: gname = (f"{r['tech']} ({r['usual']})" if r['usual'] else r['tech'], r['tech'])
            groups[gk] = {'name': gname[0].replace("'", '’'), 'tech': gname[1].replace("'", '’'), 'region': reg, 'sub': sub, 'members': []}
        groups[gk]['members'].append(iid); d['group'] = gk
    items.append(d)

assert not missing_rows, missing_rows
unused = set(rows) - {base_of(m['name']).strip() for m in inv}
assert not unused, unused
# order: regions and subs as listed, then the model's own order; groups follow their first member
order = {}
for i, (k, l, subs) in enumerate(M.REGIONS):
    for j, (sk, sl) in enumerate(subs): order[(k, sk)] = (i, j)
for d in items: assert (d['region'], d['sub']) in order, (d['id'], d['region'], d['sub'])
items = [d for _, d in sorted(enumerate(items), key=lambda x: (order[(x[1]['region'], x[1]['sub'])], x[0]))]
first = {}
for i, d in enumerate(items):
    if d.get('group') and d['group'] not in first: first[d['group']] = i
groups = collections.OrderedDict(sorted(groups.items(), key=lambda kv: first[kv[0]]))
data = {
    'regions': [dict({'key': k, 'label': l, 'subs': [{'key': sk, 'label': sl} for sk, sl in subs]}, **({'separate': True} if k in M.SEPARATE else {})) for k, l, subs in M.REGIONS],
    'tips': M.TIPS, 'groups': groups, 'bones': items, 'context': {},
}
for key in ['all'] + [k for k, l, s in M.REGIONS] + [sk for k, l, s in M.REGIONS for sk, sl in s]:
    assert key in M.TIPS, f'astuce manquante : {key}'
json.dump(data, open(f'{OUT}/{SYSN}.json', 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(rename, open(f'{S}/za/{SYSN}_rename.json', 'w'), ensure_ascii=False)

SUBL = {sk: sl for k, l, subs in M.REGIONS for sk, sl in subs}; REGL = {k: l for k, l, subs in M.REGIONS}
with open(f'{OUT}/{SYSN}-noms.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f, delimiter=';')
    w.writerow(['identifiant', 'côté', 'nom officiel', 'nom affiché avec indices', 'latin', 'anglais (Z-Anatomy)', 'région', 'sous-région', 'type', 'groupe des essentiels'])
    for d in items:
        g = groups[d['group']]['tech'] if d.get('group') else ''
        w.writerow([d['id'], {'L': 'gauche', 'R': 'droit'}.get(d['side'], ''), d['tech'], d['name'], d.get('la', ''), d['en'], REGL[d['region']], SUBL[d['sub']], d['kind'], g])

ess = [g for g in groups.values() if g['region'] not in M.SEPARATE]
print('structures', len(items), '| groupes', len(groups), '| essentiels au corps entier', len(ess), '| toutes au corps entier', sum(1 for d in items if d['region'] not in M.SEPARATE))
print('types', dict(collections.Counter(d['kind'] for d in items)))
print('régions', dict(collections.Counter(d['region'] for d in items)))
