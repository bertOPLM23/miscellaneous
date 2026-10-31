# Rassemble, pour chaque structure (gauche et droite réunies), la définition française de Z-Anatomy si elle existe,
# sinon la description anglaise (d'après Wikipédia) à résumer en français.
# Usage : python3 -I desc_src.py <travail> <dossier data de la page>  ->  <travail>/desc/<système>.src.json
import json, re, os, sys
S, DATA = sys.argv[1], sys.argv[2]
D = f'{S}/za/moueza/Resources/Descriptions'
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower().replace('(', '').replace(')', ''))
FR = {norm(re.sub(r'-FR\.txt$', '', f)): f'{D}/French definitions/{f}' for f in os.listdir(f'{D}/French definitions')}
EN = {norm(f[:-4]): f'{D}/OriginalDescriptions/{f}' for f in os.listdir(f'{D}/OriginalDescriptions')}

def clean(path, limit):
    t = open(path, encoding='utf-8', errors='replace').read().replace('\r', '')
    lines = t.split('\n')
    while lines and (not lines[0].strip() or lines[0].strip().lstrip('/').isupper() or lines[0].strip().startswith('/')): lines.pop(0)   # title block
    t = re.sub(r'\n\s*\n+', '\n\n', '\n'.join(l.rstrip() for l in lines)).strip()
    if len(t) > limit:
        cut = t[:limit]; t = cut[:max(cut.rfind('\n\n'), cut.rfind('. ') + 1)].strip()
    return t

def candidates(en):
    en = re.sub(r'\s*\((left|right)\)$', '', en).strip()
    out = [en, re.sub(r'^(Left|Right) ', '', en)]
    m = re.search(r' of (.+)$', en)
    if m: out += [m.group(1), m.group(1) + ' muscle', re.sub(r' muscle$', '', m.group(1))]
    out += [en + ' muscle', re.sub(r' muscle$', '', en), re.sub(r'\s*\(.*?\)', '', en)]
    return [c for c in out if c]

base = lambda i: re.sub(r'_[lr]$', '', i)
strip_side = lambda n: re.sub(r'(,\s*côté (gauche|droit)| (gauche|droite|droit))(?=( \(|$))', '', n).strip()
bones_za = json.load(open(f'{S}/za/bones_za.json'))
html = open(f'{DATA}/../index.html', encoding='utf-8').read()
systems = {'bones': json.loads(re.search(r'const BONES_DATA = (\{.*?\});\n', html).group(1))}
for k in ('muscles', 'nerves', 'vessels', 'lymph', 'organs'): systems[k] = json.load(open(f'{DATA}/{k}.json'))
os.makedirs(f'{S}/desc', exist_ok=True)
for k, d in systems.items():
    regions = {r['key']: r for r in d['regions']}
    subs = {s['key']: s['label'] for r in d['regions'] for s in r['subs']}
    out = {}
    for b in d['bones']:
        key = base(b['id'])
        if key in out: continue
        en = re.sub(r'\.(l|r)$', '', bones_za[b['id']][0]) if k == 'bones' else b['en']
        if k == 'bones' and key == 'sternum': en = 'Sternum'
        cands = candidates(en)
        frc = next((c for c in cands if norm(c) in FR), None); fr = FR[norm(frc)] if frc else None
        enc = next((c for c in cands if norm(c) in EN), None); eng = EN[norm(enc)] if enc else None
        own = {norm(c) for c in cands[:2]}
        e = {'key': key, 'nom': strip_side(b.get('tech') or b['name']), 'en': re.sub(r'\s*\((left|right)\)$', '', en), 'latin': b.get('la', ''),
             'region': regions[b['region']]['label'], 'sous_region': subs[b['sub']], 'type': b.get('kind', 'bone')}
        if fr:
            e['src'] = 'za'; e['texte'] = clean(fr, 1800)
            if norm(frc) not in own: e['parent'] = True   # definition of the whole structure (the muscle for one of its heads)
        elif eng: e['src'] = 'wiki'; e['anglais'] = clean(eng, 1500)
        else: e['src'] = 'atlas'
        out[key] = e
    json.dump(list(out.values()), open(f'{S}/desc/{k}.src.json', 'w'), ensure_ascii=False, indent=1)
    c = {s: sum(1 for e in out.values() if e['src'] == s) for s in ('za', 'wiki', 'atlas')}
    print(f'{k:8} {len(out):4} fiches : définition française {c["za"]:4}, à résumer depuis l’anglais {c["wiki"]:4}, à rédiger {c["atlas"]:4}')
