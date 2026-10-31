# Génère bone-atlas-fr/data/muscles.json et la table de renommage des nœuds du modèle.
# Usage : python3 -I build_muscles.py <scratchpad> <dossier de sortie>
import json, re, sys, unicodedata, collections, importlib.util

S, OUT = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location('mfr', f'{S}/muscles_fr.py'); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
inv = json.load(open(f'{S}/za/inv/nq_muscular.json'))['list']
lex = json.load(open(f'{S}/za/lexicon.json'))

rows = {}
for line in M.ROWS.strip().splitlines():
    en, tech, usual, sec, kind, group = [x.strip() for x in line.split('|')]
    rows[en] = dict(tech=tech.replace("'", '’'), usual=usual.replace("'", '’'), sec=sec, kind=kind, group=group)

def slug(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '_', s).strip('_')

FEM = {'partie', 'parties', 'bourse', 'bourses', 'gaine', 'gaines', 'aponévrose', 'arcade', 'lame', 'trochlée', 'ligne'}
PLURAL = {'muscles', 'parties', 'bourses', 'gaines', 'tendons'}
def with_side(tech, side):
    """« Muscle grand pectoral gauche », mais « Muscle droit de l’abdomen, côté gauche » quand un complément suit."""
    if not side: return tech
    first = tech.split()[0].lower()
    if first in PLURAL or re.search(r"\b(du|de|des|d’)\b", tech) or re.search(r'\bdroit\b', tech, re.I):
        return f"{tech}, côté {'gauche' if side == 'L' else 'droit'}"
    adj = 'gauche' if side == 'L' else ('droite' if first in FEM else 'droit')
    return f'{tech} {adj}'

# camera zones (same keys as the bone regions) and views from behind
ZONE = {'face': 'head', 'mastic': 'head', 'eye': 'head', 'tongue': 'head', 'suprahy': 'head', 'infrahy': 'head', 'neckm': 'head', 'pharynx': 'head',
        'backsup': 'torso/spine', 'backmid': 'torso/spine', 'backdeep': 'torso/spine', 'subocc': 'head',
        'thorax': 'torso/ribcage', 'abdomen': 'torso/pelvis', 'pelvis': 'torso/pelvis',
        'shoulder': 'arm', 'armc': 'arm', 'fant': 'arm', 'fpost': 'arm', 'hand': 'hand',
        'glut': 'torso/pelvis', 'thant': 'leg', 'thmed': 'leg', 'thpost': 'leg', 'legant': 'leg', 'leglat': 'leg', 'legpost': 'leg', 'foot': 'foot'}
BACK_SUBS = {'backsup', 'backmid', 'backdeep', 'subocc', 'glut', 'thpost', 'legpost', 'fpost'}
BACK_IDS = {'Long head of triceps brachii', 'Lateral head of triceps brachii', 'Medial head of triceps brachii', 'Quadratus lumborum muscle'}

items, groups, rename, context = [], collections.OrderedDict(), {}, {}
missing_rows = set()
for m in inv:
    name = m['name']; en = re.sub(r'\.(l|r)$', '', name)
    side = {'l': 'L', 'r': 'R'}.get(name[-1]) if re.search(r'\.(l|r)$', name) else ''
    r = rows.get(en)
    if not r: missing_rows.add(en); continue
    reg, sub = r['sec'].split('/')
    cy = (m['min'][1] + m['max'][1]) / 2; cz = (m['min'][2] + m['max'][2]) / 2
    if reg == 'annex':
        if sub == 'fhead': zone = 'head'
        elif sub == 'ftrunk': zone = 'torso/spine' if 'thoracolombaire' in r['tech'] else ('torso/ribcage' if cy > 1.2 else 'torso/pelvis')
        elif sub == 'ful': zone = 'hand' if cy < 0.83 else 'arm'
        else: zone = 'foot' if cy < 0.13 else ('torso/pelvis' if cy > 0.75 else 'leg')
        turn = 'back' if cz < -0.035 else ''
    else:
        zone = ZONE[sub]; turn = 'back' if (sub in BACK_SUBS or en in BACK_IDS) else ''
    zr, _, zs = zone.partition('/')
    iid = 'm_' + slug(en.strip('()')) + ('_' + side.lower() if side else '')
    rename[name] = iid
    tech = with_side(r['tech'], side)
    label = f"{tech} ({r['usual']})" if r['usual'] else tech
    lx = lex.get(en) or lex.get(f'({en.strip("()")})') or {}
    d = {'id': iid, 'name': label, 'tech': tech, 'region': reg, 'sub': sub, 'side': side, 'zr': zr, 'zs': zs or None, 'kind': r['kind'], 'en': name.replace('.l', ' (left)').replace('.r', ' (right)')}
    if lx.get('la'): d['la'] = lx['la']
    if turn: d['turn'] = turn
    gk = None if r['group'] == '-' else (r['group'] or slug(en.strip('()')))
    if gk:
        if gk not in groups:
            gname = M.GROUPS.get(gk, (None, None))
            if gname[0] is None:   # single-piece group: the piece's own name, without side
                gname = (f"{r['tech']} ({r['usual']})" if r['usual'] else r['tech'], r['tech'])
            groups[gk] = {'name': gname[0].replace("'", '’'), 'tech': gname[1].replace("'", '’'), 'region': reg, 'sub': sub, 'members': []}
        groups[gk]['members'].append(iid); d['group'] = gk
    if d['zs'] is None: del d['zs']
    items.append(d)

assert not missing_rows, missing_rows
# order: regions and subs as listed (head to foot), then the model's own order; groups follow their first member
order = {}
for i, (k, l, subs) in enumerate(M.REGIONS):
    for j, (sk, sl) in enumerate(subs): order[(k, sk)] = (i, j)
items = [d for _, d in sorted(enumerate(items), key=lambda x: (order[(x[1]['region'], x[1]['sub'])], x[0]))]
first = {}
for i, d in enumerate(items):
    if d.get('group') and d['group'] not in first: first[d['group']] = i
groups = collections.OrderedDict(sorted(groups.items(), key=lambda kv: first[kv[0]]))
unused = set(rows) - {re.sub(r'\.(l|r)$', '', m['name']) for m in inv}
assert not unused, unused
data = {
    'regions': [dict({'key': k, 'label': l, 'subs': [{'key': sk, 'label': sl} for sk, sl in subs]}, **({'separate': True} if k == 'annex' else {})) for k, l, subs in M.REGIONS],
    'tips': M.TIPS, 'groups': groups, 'bones': items, 'context': context,
}
json.dump(data, open(f'{OUT}/muscles.json', 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(rename, open(f'{S}/za/muscles_rename.json', 'w'), ensure_ascii=False)
# table to proofread the names (opens in a spreadsheet)
import csv
SUBL = {sk: sl for k, l, subs in M.REGIONS for sk, sl in subs}; REGL = {k: l for k, l, subs in M.REGIONS}
with open(f'{OUT}/muscles-noms.csv', 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f, delimiter=';')
    w.writerow(['identifiant', 'côté', 'nom officiel', 'nom affiché avec indices', 'latin', 'anglais (Z-Anatomy)', 'région', 'loge / sous-région', 'type', 'groupe des essentiels'])
    for d in items:
        g = groups.get(d.get('group'), {}).get('tech', '') if d.get('group') else ''
        w.writerow([d['id'], {'L': 'gauche', 'R': 'droit'}.get(d['side'], ''), d['tech'], d['name'], d.get('la', ''), d['en'], REGL[d['region']], SUBL[d['sub']], d['kind'], g])
kinds = collections.Counter(d['kind'] for d in items)
print('items', len(items), 'groups', len(groups), 'kinds', dict(kinds))
print('par région', dict(collections.Counter(d['region'] for d in items)))
for d in items[39:44] + items[150:152] + items[300:303]: print('  ', d['name'], '|', d['tech'], '|', d.get('group'), d['zr'], d.get('zs'), d.get('turn', ''))
