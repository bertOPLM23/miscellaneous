# Outils de génération des systèmes

Scripts qui produisent les fichiers d'un système (muscles, nerfs…) à partir des modèles Z-Anatomy.

## Sources (non incluses dans le dépôt)

- `nq/<système>.glb` : modèles du projet [nqwrc/3d-anatomy](https://github.com/nqwrc/3d-anatomy)
  (`public/models/`), exportés du fichier Blender de Z-Anatomy. Licence CC BY-SA 4.0 (Z-Anatomy) et
  CC BY-SA 2.1 Japon (BodyParts3D).
- `lexicon.json` : noms latins, du même projet (`public/data/lexicon.json`).
- `inv/nq_<système>.json` : inventaire du modèle, produit par `node inventory.mjs nq/<système>.glb inv/nq_<système>.json`.

Ces fichiers sont attendus dans `<travail>/za/`, et les tables `<système>_fr.py` dans `<travail>/`.

## Générer un système

1. `<système>_fr.py` (`muscles_fr.py`, `nerves_fr.py`, `vessels_fr.py`) : la table de correspondance, à corriger en cas d'erreur
   de nom. Une ligne par structure : nom anglais Z-Anatomy, nom officiel français, nom usuel, région/sous-région,
   type, groupe des essentiels. Le fichier contient aussi les régions, les astuces, les groupes à plusieurs
   pièces, les régions révisées à part et la règle de cadrage de la caméra (`camera`).
2. `python3 build_system.py <système> <travail> ../data` : écrit `data/<système>.json` (données de la page),
   `data/<système>-noms.csv` (tableau de relecture) et la table de renommage des nœuds du modèle.
3. `node build_model.mjs <travail>/za/nq/<modèle>.glb <travail>/za/<système>_rename.json ../<système>.glb 0.1 0.005` :
   renomme les nœuds, simplifie les maillages (ratio 0,1, erreur 0,5 %) et compresse
   (quantification + EXT_meshopt_compression). Dépendances npm : `@gltf-transform/core`,
   `@gltf-transform/extensions`, `@gltf-transform/functions`, `meshoptimizer`, `draco3dgltf`.
4. Reporter la taille du `.glb` dans la constante `<SYSTÈME>_BYTES` d'index.html (barre de progression).
