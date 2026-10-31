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

1. `<système>_fr.py` (`muscles_fr.py`, `nerves_fr.py`, `vessels_fr.py`, `lymph_fr.py`, `organs_fr.py`) : la table de correspondance, à corriger en cas d'erreur
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

## Système lymphatique : vaisseaux modélisés

Z-Anatomy ne contient que les nœuds et les organes lymphoïdes. Les conduits, troncs et collecteurs sont modélisés :

1. `node gen_lymph.mjs <travail>/za/nq/lymphatic.glb <travail>/za/nq/cardiovascular.glb ../skeleton.glb <travail>/za/lymph_vessels.glb` :
   trace chaque vaisseau comme un tube passant par des points d'ancrage pris sur la géométrie réelle (axe des veines
   et artères, centre des groupes de nœuds, face antérieure des vertèbres). Les tracés sont décrits en tête de la
   section « the vessels » du script : c'est là qu'on corrige un trajet.
2. `node check_lymph.mjs <travail>/za/lymph_vessels.glb <travail>/za/nq/cardiovascular.glb ../skeleton.glb` : contrôle
   chiffré (position du conduit thoracique vertèbre par vertèbre entre aorte et azygos, distance des collecteurs à
   leur veine, arrivée des conduits aux angles veineux).
3. `node merge.mjs <travail>/za/nq/lymphatic.glb <travail>/za/lymph_vessels.glb <travail>/za/lymph_src.glb`, puis
   `node inventory.mjs <travail>/za/lymph_src.glb <travail>/za/inv/nq_lymph.json`, puis les étapes 2 à 4 ci-dessus avec
   `lymph` (modèle : `lymph_src.glb`, simplification légère `0.5 0.001` pour ne pas déformer les tubes fins).

## Fiches descriptives

Chaque structure a une fiche (`data/<système>-desc.json`, une entrée pour la gauche et la droite) :
- `desc_src.py` rassemble la définition française de Z-Anatomy quand elle existe (dépôt moueza/Z-Anatomy,
  `Resources/Descriptions/French definitions`), sinon la description anglaise (`OriginalDescriptions`, d'après Wikipédia) ;
- les fiches sans définition française ont été rédigées en français pour l'atlas (en partie d'après ces textes anglais,
  souvent hors sujet) ; elles sont marquées « à vérifier » dans la page ;
- `desc_build.py` assemble le tout. Pour corriger une fiche, modifier directement son texte dans `data/<système>-desc.json`.
