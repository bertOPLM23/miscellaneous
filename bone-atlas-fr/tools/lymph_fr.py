# Table du système lymphatique : nom (Z-Anatomy, ou vaisseau modélisé par gen_lymph.mjs) -> données françaises.
# Format : anglais | nom officiel | nom usuel (vide si aucun) | section (région/sous-région) | type | groupe
#   type   : node (nœud lymphatique), organ (organe lymphoïde), duct (conduit, citerne, tronc), collector (collecteurs)
#   groupe : clé du groupe « essentiels » ; vide = groupe propre ; « - » = hors essentiels.
ROWS = r"""
Left lobe of thymus|Lobe gauche du thymus||organs/organs|organ|thymus
Right lobe of thymus|Lobe droit du thymus||organs/organs|organ|thymus
Spleen|Rate||organs/organs|organ|
Palatine tonsil|Tonsille palatine|amygdale palatine|organs/organs|organ|
Thoracic duct|Conduit thoracique|canal thoracique|ducts/main|duct|
Cisterna chyli|Citerne du chyle|citerne de Pecquet|ducts/main|duct|
Right lymphatic duct|Conduit lymphatique droit|grande veine lymphatique|ducts/main|duct|
Jugular trunk|Tronc jugulaire||ducts/trunks|duct|
Subclavian trunk|Tronc subclavier|tronc sous-clavier|ducts/trunks|duct|
Bronchomediastinal trunk|Tronc bronchomédiastinal||ducts/trunks|duct|
Lumbar trunk|Tronc lombal|tronc lombaire|ducts/trunks|duct|
Intestinal trunk|Tronc intestinal||ducts/trunks|duct|
Superficial medial collecting lymphatics of lower limb|Collecteurs superficiels médiaux du membre inférieur|courant de la grande saphène|coll/llc|collector|
Superficial lateral collecting lymphatics of lower limb|Collecteurs superficiels latéraux du membre inférieur|courant de la petite saphène|coll/llc|collector|
Deep collecting lymphatics of leg|Collecteurs profonds de la jambe||coll/llc|collector|
Deep collecting lymphatics of thigh|Collecteurs profonds de la cuisse|satellites des vaisseaux fémoraux|coll/llc|collector|
External iliac collecting lymphatics|Collecteurs iliaques externes||coll/pelvc|collector|
Internal iliac collecting lymphatics|Collecteurs iliaques internes||coll/pelvc|collector|
Mesenteric collecting lymphatics|Collecteurs mésentériques||coll/pelvc|collector|
Coeliac collecting lymphatics|Collecteurs cœliaques||coll/pelvc|collector|
Superficial medial collecting lymphatics of upper limb|Collecteurs superficiels médiaux du membre supérieur|courant de la veine basilique|coll/ulc|collector|
Superficial lateral collecting lymphatics of upper limb|Collecteurs superficiels latéraux du membre supérieur|courant de la veine céphalique|coll/ulc|collector|
Deep collecting lymphatics of upper limb|Collecteurs profonds du membre supérieur|satellites des vaisseaux brachiaux|coll/ulc|collector|
Axillary collecting lymphatics|Collecteurs des nœuds axillaires||coll/ulc|collector|
Deep cervical collecting lymphatics|Collecteurs cervicaux profonds|chaîne jugulaire interne|coll/hnc|collector|
Posterior superficial collecting lymphatics of head|Collecteurs superficiels postérieurs de la tête||coll/hnc|collector|
Anterior superficial collecting lymphatics of head|Collecteurs superficiels antérieurs de la tête||coll/hnc|collector|
Superficial cervical collecting lymphatics|Collecteurs cervicaux superficiels|chaîne jugulaire externe|coll/hnc|collector|
Parasternal collecting lymphatics|Collecteurs parasternaux|chaîne mammaire interne|coll/thc|collector|
Intercostal collecting lymphatics|Collecteurs intercostaux||coll/thc|collector|
Infra-auricular nodes|Nœuds infra-auriculaires|ganglions sous-auriculaires|hn/head|node|
Intraglandular parotid nodes|Nœuds parotidiens intraglandulaires|ganglions parotidiens profonds|hn/head|node|
Pre-auricular nodes|Nœuds pré-auriculaires||hn/head|node|
Bucinator node|Nœud buccinateur|ganglion génien|hn/head|node|facial_nodes
Mandibular node|Nœud mandibulaire||hn/head|node|facial_nodes
Nasolabial node|Nœud nasolabial||hn/head|node|facial_nodes
Mastoid nodes|Nœuds mastoïdiens|ganglions rétro-auriculaires|hn/head|node|
Occipital nodes|Nœuds occipitaux||hn/head|node|
Superficial parotid nodes|Nœuds parotidiens superficiels||hn/head|node|
Paratracheal cervical nodes|Nœuds paratrachéaux du cou|chaîne récurrentielle|hn/neck|node|
Pretracheal nodes|Nœuds prétrachéaux||hn/neck|node|
Thyroid nodes|Nœuds thyroïdiens||hn/neck|node|
Superficial anterior cervical nodes|Nœuds cervicaux antérieurs superficiels|chaîne jugulaire antérieure|hn/neck|node|
Inferior deep lateral cervical nodes|Nœuds cervicaux latéraux profonds inférieurs|chaîne jugulaire interne basse|hn/neck|node|
Anterior inferior jugular nodes|Nœuds jugulaires inférieurs antérieurs||hn/neck|node|
Superficial lateral cervical nodes|Nœuds cervicaux latéraux superficiels|chaîne jugulaire externe|hn/neck|node|
Jugulodigastric node|Nœud jugulodigastrique|ganglion de Küttner|hn/neck|node|
Lateral superior jugular node|Nœud jugulaire supérieur latéral||hn/neck|node|
Retropharyngeal nodes|Nœuds rétropharyngiens||hn/neck|node|
Submandibular nodes|Nœuds submandibulaires|ganglions sous-maxillaires|hn/neck|node|
Submental nodes|Nœuds submentaux|ganglions sous-mentaux|hn/neck|node|
Supraclavicular nodes|Nœuds supraclaviculaires|ganglion de Troisier à gauche|hn/neck|node|
Anterior axillary nodes|Nœuds axillaires antérieurs|ganglions pectoraux|ul/axil|node|
Apical axillary nodes|Nœuds axillaires apicaux|ganglions sous-claviculaires|ul/axil|node|
Central axillary nodes|Nœuds axillaires centraux||ul/axil|node|
Lateral axillary nodes|Nœuds axillaires latéraux|ganglions huméraux|ul/axil|node|
Posterior axillary nodes|Nœuds axillaires postérieurs|ganglions subscapulaires|ul/axil|node|
Interpectoral nodes|Nœuds interpectoraux|ganglions de Rotter|ul/axil|node|
Infraclavicular nodes|Nœuds infraclaviculaires|ganglions deltopectoraux|ul/axil|node|
Brachial nodes|Nœuds brachiaux||ul/arm|node|
Cubital nodes|Nœuds cubitaux|ganglions épitrochléens|ul/arm|node|
Supratrochlear nodes|Nœuds supratrochléaires||ul/arm|node|
Brachiocephalic nodes|Nœuds brachiocéphaliques||thorax/tvisc|node|
Inferior tracheobronchial nodes|Nœuds trachéobronchiques inférieurs|ganglions intertrachéobronchiques|thorax/tvisc|node|
Superior tracheobronchial nodes|Nœuds trachéobronchiques supérieurs||thorax/tvisc|node|
Paratracheal thoracic nodes|Nœuds paratrachéaux du thorax||thorax/tvisc|node|
Juxta-oesophageal nodes|Nœuds juxta-œsophagiens||thorax/tvisc|node|
Lateral pericardial nodes|Nœuds péricardiques latéraux||thorax/tvisc|node|
Node of arch of azygos vein|Nœud de l'arc de la veine azygos||thorax/tvisc|node|
Node of ligamentum arteriosum|Nœud du ligament artériel||thorax/tvisc|node|
Prepericardial nodes|Nœuds prépéricardiques||thorax/tvisc|node|
Intrapulmonary nodes|Nœuds intrapulmonaires||thorax/tvisc|node|
Intercostal nodes|Nœuds intercostaux||thorax/tpariet|node|
Parasternal nodes|Nœuds parasternaux|ganglions mammaires internes|thorax/tpariet|node|
Prevertebral nodes|Nœuds prévertébraux||thorax/tpariet|node|
Superior diaphragmatic nodes|Nœuds phréniques supérieurs||thorax/tpariet|node|
Inferior diaphragmatic nodes|Nœuds phréniques inférieurs||abdo/apariet|node|
Inferior epigastric nodes|Nœuds épigastriques inférieurs||abdo/apariet|node|
Lateral aortic nodes|Nœuds aortiques latéraux|ganglions latéro-aortiques|abdo/apariet|node|lumbar_nodes
Pre-aortic nodes|Nœuds pré-aortiques||abdo/apariet|node|lumbar_nodes
Retro-aortic nodes|Nœuds rétro-aortiques||abdo/apariet|node|lumbar_nodes
Lateral caval nodes|Nœuds caves latéraux|ganglions latéro-caves|abdo/apariet|node|lumbar_nodes
Precaval nodes|Nœuds précaves||abdo/apariet|node|lumbar_nodes
Retrocaval nodes|Nœuds rétrocaves||abdo/apariet|node|lumbar_nodes
Intermediate lumbar nodes|Nœuds lombaux intermédiaires|ganglions inter-aortico-caves|abdo/apariet|node|lumbar_nodes
Coeliac nodes|Nœuds cœliaques||abdo/avisc|node|
Cystic node|Nœud cystique|ganglion de Mascagni|abdo/avisc|node|
Left colic nodes|Nœuds coliques gauches||abdo/avisc|node|
Sigmoid nodes|Nœuds sigmoïdiens||abdo/avisc|node|
Inferior pancreatic nodes|Nœuds pancréatiques inférieurs||abdo/avisc|node|
Superior pancreatic nodes|Nœuds pancréatiques supérieurs||abdo/avisc|node|
Superior pancreaticoduodenal nodes|Nœuds pancréaticoduodénaux supérieurs||abdo/avisc|node|
(Retropyloric nodes)|Nœuds rétropyloriques||abdo/avisc|node|pyloric
(Subpyloric nodes)|Nœuds subpyloriques|ganglions sous-pyloriques|abdo/avisc|node|pyloric
(Suprapyloric node)|Nœud suprapylorique|ganglion sus-pylorique|abdo/avisc|node|pyloric
Right gastric nodes|Nœuds gastriques droits||abdo/avisc|node|
Right gastro-omental nodes|Nœuds gastro-omentaux droits|ganglions gastro-épiploïques droits|abdo/avisc|node|
Splenic nodes|Nœuds spléniques||abdo/avisc|node|
Appendicular nodes|Nœuds appendiculaires||abdo/avisc|node|
Central superior mesenteric nodes|Nœuds mésentériques supérieurs centraux||abdo/avisc|node|
Ileocolic nodes|Nœuds iléocoliques||abdo/avisc|node|
Juxta-intestinal mesenteric nodes|Nœuds mésentériques juxta-intestinaux||abdo/avisc|node|
Middle colic nodes|Nœuds coliques moyens||abdo/avisc|node|
Paracolic superior mesenteric nodes|Nœuds mésentériques supérieurs paracoliques||abdo/avisc|node|
Precaecal nodes|Nœuds précæcaux||abdo/avisc|node|caecal
Retrocaecal nodes|Nœuds rétrocæcaux||abdo/avisc|node|caecal
Right colic nodes|Nœuds coliques droits||abdo/avisc|node|
Intermediate common iliac nodes|Nœuds iliaques communs intermédiaires||pelvis/iliac|node|common_iliac
Lateral common iliac nodes|Nœuds iliaques communs latéraux||pelvis/iliac|node|common_iliac
Medial common iliac nodes|Nœuds iliaques communs médiaux||pelvis/iliac|node|common_iliac
Subaortic nodes|Nœuds subaortiques|ganglions du promontoire|pelvis/iliac|node|
(Lateral lacunar node)|Nœud lacunaire latéral||pelvis/iliac|node|
Intermediate external iliac nodes|Nœuds iliaques externes intermédiaires||pelvis/iliac|node|external_iliac
Medial external iliac nodes|Nœuds iliaques externes médiaux||pelvis/iliac|node|external_iliac
Obturator nodes|Nœuds obturateurs||pelvis/intil|node|
Inferior gluteal nodes|Nœuds glutéaux inférieurs||pelvis/intil|node|
Superior gluteal nodes|Nœuds glutéaux supérieurs||pelvis/intil|node|
Lateral sacral nodes|Nœuds sacraux latéraux||pelvis/intil|node|
Pararectal nodes|Nœuds pararectaux||pelvis/intil|node|
Lateral vesical nodes|Nœuds vésicaux latéraux||pelvis/intil|node|vesical
Postvesical nodes|Nœuds rétrovésicaux||pelvis/intil|node|vesical
Prevesical nodes|Nœuds prévésicaux||pelvis/intil|node|vesical
(Anterior tibial node)|Nœud tibial antérieur||ll/legn|node|
(Fibular node)|Nœud fibulaire||ll/legn|node|
(Posterior tibial node)|Nœud tibial postérieur||ll/legn|node|
Deep popliteal nodes|Nœuds poplités profonds||ll/legn|node|
Superficial popliteal nodes|Nœuds poplités superficiels||ll/legn|node|
(Intermediate deep inguinal node)|Nœud inguinal profond intermédiaire||ll/inguinal|node|deep_inguinal
(Proximal deep inguinal node)|Nœud inguinal profond proximal|ganglion de Cloquet|ll/inguinal|node|deep_inguinal
Inferior superficial inguinal nodes|Nœuds inguinaux superficiels inférieurs||ll/inguinal|node|
Superolateral superficial inguinal nodes|Nœuds inguinaux superficiels supérolatéraux||ll/inguinal|node|
Superomedial superficial inguinal nodes|Nœuds inguinaux superficiels supéromédiaux||ll/inguinal|node|
"""

GROUPS = {
    'thymus': ('Thymus', 'Thymus'),
    'facial_nodes': ('Nœuds faciaux (buccinateur, mandibulaire, nasolabial)', 'Nœuds faciaux'),
    'lumbar_nodes': ('Nœuds lombaux (latéro-aortiques, pré- et rétro-aortiques, caves)', 'Nœuds lombaux'),
    'pyloric': ('Nœuds pyloriques', 'Nœuds pyloriques'),
    'caecal': ('Nœuds cæcaux', 'Nœuds cæcaux'),
    'common_iliac': ('Nœuds iliaques communs', 'Nœuds iliaques communs'),
    'external_iliac': ('Nœuds iliaques externes', 'Nœuds iliaques externes'),
    'vesical': ('Nœuds vésicaux', 'Nœuds vésicaux'),
    'deep_inguinal': ('Nœuds inguinaux profonds', 'Nœuds inguinaux profonds'),
}

REGIONS = [
    ('ducts', 'Conduits et troncs', [('main', 'Conduits et citerne du chyle'), ('trunks', 'Troncs lymphatiques')]),
    ('coll', 'Collecteurs lymphatiques', [('hnc', 'Tête et cou'), ('ulc', 'Membre supérieur'), ('thc', 'Thorax'), ('pelvc', 'Abdomen et bassin'), ('llc', 'Membre inférieur')]),
    ('organs', 'Organes lymphoïdes', [('organs', 'Thymus, rate, tonsille')]),
    ('hn', 'Nœuds de la tête et du cou', [('head', 'Tête'), ('neck', 'Cou')]),
    ('ul', 'Nœuds du membre supérieur', [('axil', 'Aisselle'), ('arm', 'Bras et coude')]),
    ('thorax', 'Nœuds du thorax', [('tpariet', 'Nœuds pariétaux'), ('tvisc', 'Nœuds viscéraux')]),
    ('abdo', 'Nœuds de l’abdomen', [('apariet', 'Nœuds pariétaux (lombaux)'), ('avisc', 'Nœuds viscéraux')]),
    ('pelvis', 'Nœuds du bassin', [('iliac', 'Nœuds iliaques communs et externes'), ('intil', 'Nœuds iliaques internes et viscéraux')]),
    ('ll', 'Nœuds du membre inférieur', [('inguinal', 'Région inguinale'), ('legn', 'Genou et jambe')]),
]

TIPS = {
    'all': 'Les conduits, troncs et collecteurs sont modélisés sur les repères anatomiques (veines, artères, nœuds) : tracé fidèle, calibre simplifié. Nœuds et organes viennent de Z-Anatomy.',
    'ducts': 'Toute la lymphe rejoint le sang aux angles veineux (union des veines jugulaire interne et subclavière) : à gauche par le conduit thoracique, à droite par le conduit lymphatique droit.',
    'main': 'Le conduit thoracique (environ 40 cm) naît de la citerne du chyle vers L1-L2, traverse le hiatus aortique, monte entre aorte et veine azygos, passe à gauche vers T5 et se termine à l’angle veineux gauche.',
    'trunks': 'Troncs jugulaire, subclavier et bronchomédiastinal de chaque côté ; troncs lombaux et intestinal vers la citerne du chyle.',
    'coll': 'Les collecteurs suivent les veines : superficiels avec les veines superficielles, profonds avec les vaisseaux profonds. Ils traversent des relais de nœuds.',
    'hnc': 'Toute la lymphe de la tête et du cou finit dans la chaîne jugulaire interne (nœuds cervicaux profonds), puis dans le tronc jugulaire.',
    'ulc': 'Courant médial (veine basilique) vers les nœuds cubitaux puis axillaires latéraux ; courant latéral (veine céphalique) vers les nœuds deltopectoraux puis apicaux.',
    'thc': 'La chaîne parasternale draine la paroi antérieure du thorax et la partie médiale du sein ; les collecteurs intercostaux rejoignent le conduit thoracique.',
    'pelvc': 'Collecteurs iliaques vers les nœuds iliaques communs puis lombaux ; collecteurs cœliaques et mésentériques vers les nœuds pré-aortiques et le tronc intestinal.',
    'llc': 'Courant superficiel médial (grande saphène) vers les nœuds inguinaux superficiels ; courant latéral (petite saphène) vers les nœuds poplités.',
    'organs': 'Organes lymphoïdes : thymus (maturation des lymphocytes T, régresse après la puberté), rate (filtre le sang), tonsilles (anneau de Waldeyer).',
    'hn': 'Cercle péricervical (occipitaux, mastoïdiens, parotidiens, submandibulaires, submentaux) puis chaîne cervicale profonde le long de la veine jugulaire interne.',
    'head': 'Les nœuds de la tête forment un collier à la jonction tête-cou : occipitaux en arrière, mastoïdiens et parotidiens sur le côté, faciaux en avant.',
    'neck': 'Le nœud jugulodigastrique draine la tonsille palatine. Un nœud supraclaviculaire gauche palpable (ganglion de Troisier) évoque un cancer digestif.',
    'ul': 'Cinq groupes axillaires : antérieurs (pectoraux), postérieurs (subscapulaires), latéraux (huméraux), centraux et apicaux, ces derniers formant le tronc subclavier.',
    'axil': 'Les nœuds axillaires drainent le membre supérieur et environ 75 % du sein : premier relais du cancer du sein (ganglion sentinelle).',
    'arm': 'Les nœuds cubitaux (épitrochléens) reçoivent la lymphe des doigts médiaux et du bord ulnaire de la main.',
    'thorax': 'Nœuds pariétaux (paroi) et viscéraux (médiastin). Les nœuds trachéobronchiques drainent les poumons vers les troncs bronchomédiastinaux.',
    'tpariet': 'Nœuds parasternaux le long des vaisseaux thoraciques internes, intercostaux près des têtes des côtes, phréniques sur le diaphragme.',
    'tvisc': 'Nœuds trachéobronchiques et paratrachéaux autour de la trachée et des bronches, juxta-œsophagiens et péricardiques dans le médiastin.',
    'apariet': 'Les nœuds lombaux entourent l’aorte et la veine cave inférieure ; ils reçoivent la lymphe des membres inférieurs, du bassin, des reins et des gonades.',
    'avisc': 'Les nœuds viscéraux suivent les artères digestives : cœliaques (estomac, foie, rate, pancréas), mésentériques supérieurs (grêle, côlon droit), mésentériques inférieurs (côlon gauche).',
    'abdo': 'Nœuds lombaux autour de l’aorte et de la veine cave inférieure (troncs lombaux) ; nœuds viscéraux autour des branches de l’aorte (tronc intestinal).',
    'pelvis': 'Le bassin se draine vers les nœuds iliaques interne, externe puis commun, et enfin vers les nœuds lombaux.',
    'iliac': 'Les nœuds iliaques externes reçoivent la lymphe des nœuds inguinaux ; les iliaques communs la transmettent aux nœuds lombaux.',
    'intil': 'Nœuds iliaques internes : viscères du bassin (vessie, rectum, organes génitaux internes), fesse et périnée profond.',
    'll': 'Nœuds inguinaux superficiels (sous la peau, autour de la crosse de la grande saphène) et profonds (le long de la veine fémorale), et nœuds poplités.',
    'inguinal': 'Les nœuds inguinaux superficiels drainent le membre inférieur, la paroi abdominale sous l’ombilic, le périnée et l’anus.',
    'legn': 'Les nœuds poplités reçoivent les collecteurs profonds de la jambe et ceux de la petite saphène.',
}

# ---- réglages du générateur (build_system.py) ----
INVENTORY = 'nq_lymph'
PREFIX = 'l_'
SEPARATE = set()
FEMININE = ['rate', 'tonsille', 'citerne']
PLURAL = ['nœuds', 'collecteurs']
BACK_IDS = {'Occipital nodes', 'Mastoid nodes', 'Superficial popliteal nodes', 'Deep popliteal nodes', '(Posterior tibial node)', '(Fibular node)',
            'Superficial lateral collecting lymphatics of lower limb', 'Intercostal nodes', 'Intercostal collecting lymphatics', 'Inferior gluteal nodes',
            'Superior gluteal nodes', 'Lateral sacral nodes', 'Pararectal nodes', 'Posterior superficial collecting lymphatics of head', 'Posterior axillary nodes'}

def camera(reg, sub, en, c):
    """Zone de caméra (clés des régions osseuses) et vue de dos éventuelle."""
    cy = c[1]
    if cy > 1.48 or sub in ('head', 'neck', 'hnc'): zone = 'head'
    elif reg == 'ul' or sub == 'ulc': zone = 'arm'
    elif sub in ('llc',) or reg == 'll': zone = 'foot' if cy < 0.13 else ('torso/pelvis' if cy > 0.78 else 'leg')
    elif cy > 1.2: zone = 'torso/ribcage'
    else: zone = 'torso/pelvis'
    return zone, 'back' if en in BACK_IDS else ''
