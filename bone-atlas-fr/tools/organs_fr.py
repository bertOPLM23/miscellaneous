# Table des viscères : nom Z-Anatomy (anglais, sans .l/.r) -> données françaises.
# Format : anglais | nom officiel | nom usuel (vide si aucun) | section (région/sous-région) | type | groupe
#   type : gut, liver, gland, bile, lung, airway, kidney, urinary, genital, endocrine, mucosa, serosa
ROWS = r"""
Greater omentum|Grand omentum|grand épiploon|perit/perit|serosa|
Lesser omentum|Petit omentum|petit épiploon|perit/perit|serosa|
Mesocolon|Mésocôlon||perit/perit|serosa|
Meso-appendix|Méso-appendice||perit/perit|serosa|
Pleura|Plèvre||perit/perit|serosa|
Ascending colon|Côlon ascendant|côlon droit|digest/gut|gut|
Descending colon|Côlon descendant|côlon gauche|digest/gut|gut|
Sigmoid colon|Côlon sigmoïde||digest/gut|gut|
Free taenia|Ténia libre|bandelette libre|digest/gut|gut|taeniae
Mesocolic taenia|Ténia mésocolique||digest/gut|gut|taeniae
Omental taenia|Ténia omental||digest/gut|gut|taeniae
Transverse colon|Côlon transverse||digest/gut|gut|
Vermiform appendix|Appendice vermiforme|appendice|digest/gut|gut|
Oesophagus|Œsophage||digest/pharynx|gut|
Duodenum|Duodénum||digest/gut|gut|
Jejunum|Jéjunum et iléum|intestin grêle|digest/gut|gut|
Stomach|Estomac||digest/gut|gut|
Bile duct|Conduit cholédoque|canal cholédoque|digest/glands|bile|
Gallbladder|Vésicule biliaire||digest/glands|bile|
Liver|Foie||digest/glands|liver|
Anterior lateral segment of liver (VI)|Segment antérieur latéral droit du foie (VI)||liverseg/liverseg|liver|
Anterior medial segment of liver (V)|Segment antérieur médial droit du foie (V)||liverseg/liverseg|liver|
Left anterior lateral segment of liver (III)|Segment antérieur latéral gauche du foie (III)||liverseg/liverseg|liver|
Left medial segment of liver (IV)|Segment médial gauche du foie (IV)|lobe carré|liverseg/liverseg|liver|
Left posterior lateral segment of liver (II)|Segment postérieur latéral gauche du foie (II)||liverseg/liverseg|liver|
Posterior lateral segment of liver (VII)|Segment postérieur latéral droit du foie (VII)||liverseg/liverseg|liver|
Posterior medial segment of liver (VIII)|Segment postérieur médial droit du foie (VIII)||liverseg/liverseg|liver|
Posterior segment of liver (I)|Segment postérieur du foie (I)|lobe caudé|liverseg/liverseg|liver|
Gingiva|Gencive||digest/mouth|mucosa|
(Accessory parotid gland)|Glande parotide accessoire||digest/mouth|gland|parotid
Parotid duct|Conduit parotidien|canal de Sténon|digest/mouth|gland|
Parotid gland|Glande parotide||digest/mouth|gland|parotid
Sublingual gland|Glande sublinguale||digest/mouth|gland|
Submandibular duct|Conduit submandibulaire|canal de Wharton|digest/mouth|gland|
Submandibular gland|Glande submandibulaire|glande sous-maxillaire|digest/mouth|gland|
Soft palate|Palais mou|voile du palais|digest/mouth|mucosa|
Tongue|Langue||digest/mouth|mucosa|
Uvula of palate|Uvule palatine|luette|digest/mouth|mucosa|
Pancreas|Pancréas||digest/glands|gland|
Accessory pancreatic duct|Conduit pancréatique accessoire|canal de Santorini|digest/glands|gland|
Pancreatic duct|Conduit pancréatique|canal de Wirsung|digest/glands|gland|
Laryngopharynx|Partie laryngée du pharynx|hypopharynx|digest/pharynx|mucosa|pharynx
Nasopharynx|Partie nasale du pharynx|rhinopharynx, cavum|digest/pharynx|mucosa|pharynx
Oropharynx|Partie orale du pharynx|oropharynx|digest/pharynx|mucosa|pharynx
Adenohypophysis|Adénohypophyse|hypophyse antérieure|endo/endo|endocrine|hypophysis
Neurohypophysis|Neurohypophyse|hypophyse postérieure|endo/endo|endocrine|hypophysis
Inferior parathyroid gland|Glande parathyroïde inférieure||endo/endo|endocrine|parathyroid
Superior parathyroid gland|Glande parathyroïde supérieure||endo/endo|endocrine|parathyroid
Pineal gland|Glande pinéale|épiphyse|endo/endo|endocrine|
Suprarenal gland|Glande surrénale|capsule surrénale|endo/endo|endocrine|
Thyroid gland|Glande thyroïde|thyroïde|endo/endo|endocrine|
Corpus cavernosum of penis|Corps caverneux du pénis||genital/male|genital|penis
Corpus spongiosum of penis|Corps spongieux du pénis||genital/male|genital|penis
Glans penis|Gland du pénis||genital/male|genital|penis
Ductus deferens|Conduit déférent|canal déférent|genital/male|genital|
Ejaculatory duct|Conduit éjaculateur|canal éjaculateur|genital/male|genital|
Epididymis|Épididyme||genital/male|genital|
Prostate|Prostate||genital/male|genital|
Seminal gland|Glande séminale|vésicule séminale|genital/male|genital|
Testis|Testicule||genital/male|genital|
Epiglottis|Épiglotte||resp/upper|airway|
Inferior lobe of left lung|Lobe inférieur du poumon gauche||resp/lungs|lung|
Superior lobe of left lung|Lobe supérieur du poumon gauche||resp/lungs|lung|
Inferior lobe of right lung|Lobe inférieur du poumon droit||resp/lungs|lung|
Middle lobe of right lung|Lobe moyen du poumon droit||resp/lungs|lung|
Superior lobe of right lung|Lobe supérieur du poumon droit||resp/lungs|lung|
Mucosa of nasal cavity|Muqueuse de la cavité nasale|muqueuse pituitaire|resp/upper|mucosa|
Left main bronchus|Bronche principale gauche|bronche souche gauche|resp/bronchi|airway|
Left inferior lobar bronchus|Bronche lobaire inférieure gauche||resp/bronchi|airway|
(Anteromedial basal segmental bronchus of left lung)|Bronche segmentaire basale antéro-médiale gauche||resp/bronchi|airway|-
Anterior basal segmental bronchus of left lung (BVIII)|Bronche segmentaire basale antérieure gauche (B VIII)||resp/bronchi|airway|-
Lateral basal segmental bronchus of left lung (BIX)|Bronche segmentaire basale latérale gauche (B IX)||resp/bronchi|airway|-
Medial basal segmental bronchus of left lung (BVII)|Bronche segmentaire basale médiale gauche (B VII)||resp/bronchi|airway|-
Posterior basal segmental bronchus of left lung (BX)|Bronche segmentaire basale postérieure gauche (B X)||resp/bronchi|airway|-
Superior segmental bronchus of left lung (BVI)|Bronche segmentaire supérieure gauche (B VI)|bronche de Nelson|resp/bronchi|airway|-
Left superior lobar bronchus|Bronche lobaire supérieure gauche||resp/bronchi|airway|
Anterior segmental bronchus of left lung (BIII)|Bronche segmentaire antérieure gauche (B III)||resp/bronchi|airway|-
Apicoposterior segmental bronchus of left lung (BI+BII)|Bronche segmentaire apico-postérieure gauche (B I+II)||resp/bronchi|airway|-
Inferior lingular segmental bronchus of left lung (BV)|Bronche segmentaire lingulaire inférieure (B V)||resp/bronchi|airway|-
Superior lingular segmental bronchus of left lung (BIV)|Bronche segmentaire lingulaire supérieure (B IV)||resp/bronchi|airway|-
Right main bronchus|Bronche principale droite|bronche souche droite|resp/bronchi|airway|
Intermediate bronchus|Bronche intermédiaire|tronc intermédiaire|resp/bronchi|airway|
Middle lobar bronchus|Bronche lobaire moyenne||resp/bronchi|airway|
Lateral segmental bronchus of right lung (BIV)|Bronche segmentaire latérale droite (B IV)||resp/bronchi|airway|-
Medial segmental bronchus of right lung (BV)|Bronche segmentaire médiale droite (B V)||resp/bronchi|airway|-
Right inferior lobar bronchus|Bronche lobaire inférieure droite||resp/bronchi|airway|
Anterior basal segmental bronchus of right lung (BVIII)|Bronche segmentaire basale antérieure droite (B VIII)||resp/bronchi|airway|-
Lateral basal segmental bronchus of right lung (BIX)|Bronche segmentaire basale latérale droite (B IX)||resp/bronchi|airway|-
Medial basal segmental bronchus of right lung (BVII)|Bronche segmentaire basale médiale droite (B VII)||resp/bronchi|airway|-
Posterior basal segmental bronchus of right lung (BX)|Bronche segmentaire basale postérieure droite (B X)||resp/bronchi|airway|-
Superior segmental bronchus of right lung (BVI)|Bronche segmentaire supérieure droite (B VI)|bronche de Nelson|resp/bronchi|airway|-
Right superior lobar bronchus|Bronche lobaire supérieure droite|bronche lobaire supérieure (épartérielle)|resp/bronchi|airway|
Anterior segmental bronchus of right lung (BIII)|Bronche segmentaire antérieure droite (B III)||resp/bronchi|airway|-
Apical segmental bronchus of right lung (BI)|Bronche segmentaire apicale droite (B I)||resp/bronchi|airway|-
Posterior segmental bronchus of right lung (BII)|Bronche segmentaire postérieure droite (B II)||resp/bronchi|airway|-
Trachea|Trachée||resp/upper|airway|
Kidney|Rein||uro/uro|kidney|
Renal pelvis|Pelvis rénal|bassinet|uro/uro|urinary|
Ureter|Uretère||uro/uro|urinary|
Urethra|Urètre||uro/uro|urinary|
Urinary bladder|Vessie||uro/uro|urinary|
"""

GROUPS = {
    'taeniae': ('Ténias du côlon (bandelettes)', 'Ténias du côlon'),
    'parotid': ('Glande parotide', 'Glande parotide'),
    'pharynx': ('Pharynx', 'Pharynx'),
    'hypophysis': ('Hypophyse', 'Hypophyse'),
    'parathyroid': ('Glandes parathyroïdes', 'Glandes parathyroïdes'),
    'penis': ('Pénis (corps caverneux, corps spongieux, gland)', 'Pénis'),
}

REGIONS = [
    ('digest', 'Appareil digestif', [('mouth', 'Bouche et glandes salivaires'), ('pharynx', 'Pharynx et œsophage'), ('gut', 'Estomac et intestins'), ('glands', 'Foie, voies biliaires et pancréas')]),
    ('resp', 'Appareil respiratoire', [('upper', 'Voies aériennes supérieures et trachée'), ('bronchi', 'Bronches'), ('lungs', 'Poumons')]),
    ('uro', 'Appareil urinaire', [('uro', 'Reins et voies urinaires')]),
    ('genital', 'Appareil génital', [('male', 'Appareil génital masculin')]),
    ('endo', 'Glandes endocrines', [('endo', 'Glandes endocrines')]),
    ('perit', 'Péritoine et plèvre', [('perit', 'Séreuses')]),
    ('liverseg', 'Segments du foie', [('liverseg', 'Segmentation hépatique (Couinaud)')]),
]

TIPS = {
    'all': 'Les viscères des appareils digestif, respiratoire, urinaire, génital (modèle masculin) et endocrinien. Péritoine, plèvre et segments du foie se révisent à part.',
    'digest': 'Bouche → pharynx → œsophage → estomac → duodénum → jéjunum et iléum → côlon → rectum. Glandes annexes : glandes salivaires, foie, pancréas.',
    'mouth': 'Trois paires de grandes glandes salivaires : parotides (conduit parotidien vers la joue), submandibulaires et sublinguales (sous la langue).',
    'pharynx': 'Le pharynx a trois étages : nasal (rhinopharynx), oral et laryngé. L’œsophage lui fait suite au niveau de C6 et traverse le diaphragme vers T10.',
    'gut': 'Le côlon encadre l’intestin grêle : ascendant à droite, transverse, descendant à gauche, puis sigmoïde. Les ténias sont trois bandelettes longitudinales du côlon.',
    'glands': 'La bile descend par le conduit cholédoque, qui s’unit au conduit pancréatique (de Wirsung) pour s’ouvrir dans le duodénum (ampoule de Vater).',
    'resp': 'Fosses nasales → pharynx → larynx → trachée → bronches principales → bronches lobaires → bronches segmentaires → poumons.',
    'upper': 'La trachée descend de C6 à T4-T5 où elle se divise (carène). L’épiglotte ferme le larynx pendant la déglutition.',
    'bronchi': 'La bronche principale droite est plus courte, plus large et plus verticale que la gauche : les corps étrangers inhalés y vont plus souvent.',
    'lungs': 'Le poumon droit a trois lobes (supérieur, moyen, inférieur), le gauche deux (supérieur avec la lingula, inférieur). Dix segments à droite, huit à dix à gauche.',
    'uro': 'Reins (rétropéritonéaux, de T12 à L3, le droit plus bas), pelvis rénal, uretères, vessie, urètre.',
    'genital': 'Le modèle Z-Anatomy est masculin : testicules, épididymes, conduits déférents, glandes séminales, prostate et pénis.',
    'male': 'Trajet des spermatozoïdes : testicule → épididyme → conduit déférent → conduit éjaculateur (dans la prostate) → urètre.',
    'endo': 'Hypophyse (dans la selle turcique), glande pinéale, thyroïde et parathyroïdes (cou), glandes surrénales (au sommet des reins).',
    'perit': 'Le grand omentum pend de l’estomac devant l’intestin comme un tablier ; la plèvre enveloppe chaque poumon (feuillets viscéral et pariétal).',
    'liverseg': 'Segmentation de Couinaud : huit segments numérotés de I (lobe caudé) à VIII, dans le sens des aiguilles d’une montre en vue antérieure.',
}

# ---- réglages du générateur (build_system.py) ----
INVENTORY = 'nq_visceral'
PREFIX = 'o_'
SEPARATE = {'perit', 'liverseg'}   # recouvriraient l'intestin, les poumons et le foie
FEMININE = ['partie', 'glande', 'langue', 'gencive', 'uvule', 'muqueuse', 'bronche', 'trachée', 'plèvre', 'vésicule', 'vessie', 'prostate', 'épiglotte']
PLURAL = ['glandes']
BACK_IDS = {'Kidney', 'Renal pelvis', 'Suprarenal gland', 'Seminal gland', 'Posterior segment of liver (I)'}

def camera(reg, sub, en, c):
    cy = c[1]
    if cy > 1.44: zone = 'head'
    elif reg in ('resp', 'perit') or en in ('Oesophagus',): zone = 'torso/ribcage'
    else: zone = 'torso/pelvis'
    return zone, 'back' if en in BACK_IDS else ''
