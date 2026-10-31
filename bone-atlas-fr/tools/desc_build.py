# Assemble data/<système>-desc.json : { identifiant sans côté : [texte, source] }
# Sources : za (définition Z-Anatomy), zap (définition de la structure entière), wiki (résumé d'après Wikipédia), atlas (rédigé).
# Usage : python3 -I desc_build.py <travail> <dossier data>
import json, os, sys, re
S, DATA = sys.argv[1], sys.argv[2]
for k in ('bones', 'muscles', 'nerves', 'vessels', 'lymph'):
    src = json.load(open(f'{S}/desc/{k}.src.json'))
    fr = {}
    for f in sorted(os.listdir(f'{S}/desc')):
        if re.fullmatch(rf'{k}\d?\.fr\.json', f): fr.update(json.load(open(f'{S}/desc/{f}')))
    out, miss = {}, []
    for e in src:
        if e['src'] == 'za': out[e['key']] = [e['texte'], 'zap' if e.get('parent') else 'za']
        elif e['key'] in fr and len(fr[e['key']].strip()) > 80: out[e['key']] = [fr[e['key']].strip(), e['src']]
        else: miss.append(e['key'])
    json.dump(out, open(f'{DATA}/{k}-desc.json', 'w'), ensure_ascii=False, separators=(',', ':'))
    print(f'{k:8} fiches {len(out):4} / {len(src):4}  manquantes {len(miss)}  ({os.path.getsize(f"{DATA}/{k}-desc.json") // 1024} Ko)')
