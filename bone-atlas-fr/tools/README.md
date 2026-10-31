# Outils de génération des systèmes

Scripts qui produisent les fichiers d'un système à partir des modèles Z-Anatomy.

## Sources (non incluses dans le dépôt)

- `nq/muscular.glb` : modèle des muscles du projet [nqwrc/3d-anatomy](https://github.com/nqwrc/3d-anatomy)
  (`public/models/`), exporté du fichier Blender de Z-Anatomy. Licence CC BY-SA 4.0 (Z-Anatomy) et
  CC BY-SA 2.1 Japon (BodyParts3D).
- `lexicon.json` : noms latins, du même projet (`public/data/lexicon.json`).
- `inv/nq_muscular.json` : inventaire du modèle, produit par `inventory.mjs`.

Les scripts attendent ces fichiers dans un dossier de travail `<travail>/za/` (voir les chemins en tête de
`build_muscles.py`).

## Muscles

1. `muscles_fr.py` : la table de correspondance, à corriger en cas d'erreur de nom. Une ligne par structure :
   nom anglais Z-Anatomy, nom officiel français, nom usuel, région/loge, type, groupe des essentiels.
   On y trouve aussi les régions et les astuces affichées dans la page.
2. `python3 build_muscles.py <travail> ../data` : écrit `data/muscles.json` (données de la page),
   `data/muscles-noms.csv` (tableau de relecture) et la table de renommage des nœuds du modèle.
3. `node build_model.mjs <travail>/za/nq/muscular.glb <travail>/za/muscles_rename.json ../muscles.glb 0.1 0.005` :
   renomme les nœuds, simplifie les maillages (ratio 0,1, erreur 0,5 %) et compresse
   (quantification + EXT_meshopt_compression). Dépendances npm : `@gltf-transform/core`,
   `@gltf-transform/extensions`, `@gltf-transform/functions`, `meshoptimizer`, `draco3dgltf`.
4. Reporter la taille de `muscles.glb` dans `MUSCLES_BYTES` (index.html), pour la barre de progression.
