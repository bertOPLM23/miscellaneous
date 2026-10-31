# Table du système nerveux : nom Z-Anatomy (anglais, sans .l/.r) -> données françaises.
# Format : anglais | nom officiel | nom usuel (vide si aucun) | section (région/sous-région) | type | groupe
#   type   : grey (substance grise de surface), sulcus, nucleus, white, ventricle, meninge, nerve, ganglion, sense
#   groupe : clé du groupe « essentiels » ; vide = groupe propre ; « - » = hors essentiels (fins rameaux).
ROWS = r"""
Fourth ventricle|Quatrième ventricule|V4|enc/vent|ventricle|
Medulla oblongata|Moelle allongée|bulbe rachidien|enc/stem|grey|
Olive|Olive bulbaire||enc/stem|grey|
Pyramid of medulla oblongata|Pyramide de la moelle allongée|pyramide bulbaire|enc/stem|white|
Anterior cochlear nucleus|Noyau cochléaire antérieur||enc/stem|nucleus|
Inferior salivatory nucleus|Noyau salivaire inférieur||enc/stem|nucleus|
Nucleus ambiguus|Noyau ambigu||enc/stem|nucleus|
Nucleus of hypoglossal nerve|Noyau du nerf hypoglosse|noyau du XII|enc/stem|nucleus|
Posterior cochlear nucleus|Noyau cochléaire postérieur||enc/stem|nucleus|
Posterior nucleus of vagus nerve|Noyau postérieur du nerf vague|noyau dorsal du X|enc/stem|nucleus|
Aqueduct of midbrain|Aqueduc du mésencéphale|aqueduc de Sylvius|enc/vent|ventricle|
Base of peduncle|Base du pédoncule cérébral|pied du pédoncule|enc/stem|white|
Nucleus of trochlear nerve|Noyau du nerf trochléaire|noyau du IV|enc/stem|nucleus|
Accessory nucleus of oculomotor nerve|Noyau accessoire du nerf oculomoteur|noyau d'Edinger-Westphal|enc/stem|nucleus|
Nucleus of oculomotor nerve|Noyau du nerf oculomoteur|noyau du III|enc/stem|nucleus|
Red nucleus|Noyau rouge||enc/stem|nucleus|
Interpeduncular fossa|Fosse interpédonculaire||enc/stem|grey|
Midbrain|Mésencéphale||enc/stem|grey|
Inferior colliculus|Colliculus inférieur|tubercule quadrijumeau inférieur|enc/stem|grey|
Superior colliculus|Colliculus supérieur|tubercule quadrijumeau supérieur|enc/stem|grey|
Pons|Pont|protubérance annulaire|enc/stem|grey|
Motor nucleus of facial nerve|Noyau moteur du nerf facial|noyau du VII|enc/stem|nucleus|
Nucleus of abducens nerve|Noyau du nerf abducens|noyau du VI|enc/stem|nucleus|
Superior salivatory nucleus|Noyau salivaire supérieur||enc/stem|nucleus|
Vestibular nuclei|Noyaux vestibulaires||enc/stem|nucleus|
Anterior quadrangular lobule|Lobule quadrangulaire antérieur||enc/cereb|grey|
Biventral lobule|Lobule biventre||enc/cereb|grey|
Central lobule|Lobule central du vermis||enc/cereb|grey|
Culmen|Culmen||enc/cereb|grey|
Declive|Déclive||enc/cereb|grey|
Flocculus|Flocculus||enc/cereb|grey|
Folium of vermis|Folium du vermis||enc/cereb|grey|
Gracile lobule|Lobule grêle||enc/cereb|grey|
Inferior semilunar lobule|Lobule semi-lunaire inférieur||enc/cereb|grey|
Lingula of cerebellum|Lingula du cervelet||enc/cereb|grey|
Nodule of vermis|Nodule du vermis||enc/cereb|grey|
Peduncle of flocculus|Pédoncule du flocculus||enc/cereb|white|
Posterior quadrangular lobule|Lobule quadrangulaire postérieur||enc/cereb|grey|
Pyramis of vermis|Pyramide du vermis||enc/cereb|grey|
Superior cerebellar peduncle|Pédoncule cérébelleux supérieur||enc/cereb|white|
Superior semilunar lobule|Lobule semi-lunaire supérieur||enc/cereb|grey|
Tonsil of cerebellum|Tonsille du cervelet|amygdale cérébelleuse|enc/cereb|grey|
Tuber of vermis|Tuber du vermis||enc/cereb|grey|
Uvula of vermis|Uvule du vermis||enc/cereb|grey|
Wing of central lobule|Aile du lobule central||enc/cereb|grey|
Habenula|Habénula||enc/dien|grey|
Hypothalamus|Hypothalamus||enc/dien|grey|
Lateral geniculate body|Corps géniculé latéral|corps genouillé externe|enc/dien|nucleus|
Mamillary body|Corps mamillaire||enc/dien|nucleus|
Medial geniculate body|Corps géniculé médial|corps genouillé interne|enc/dien|nucleus|
Optic chiasm|Chiasma optique||enc/dien|white|
Optic tract|Tractus optique|bandelette optique|enc/dien|white|
Thalamus|Thalamus||enc/dien|nucleus|
Third ventricle|Troisième ventricule|V3|enc/vent|ventricle|
Posterior commissure|Commissure postérieure||enc/dien|white|
Stria medullaris thalami|Strie médullaire du thalamus||enc/dien|white|
Amygdaloid body|Corps amygdaloïde|amygdale|enc/limbic|nucleus|
Septal nuclei|Noyaux septaux||enc/limbic|nucleus|
Caudate nucleus|Noyau caudé||enc/deep|nucleus|
Putamen|Putamen||enc/deep|nucleus|
Globus pallidus|Globus pallidus|pallidum|enc/deep|nucleus|
Lentiform nucleus|Noyau lenticulaire||enc/deep|nucleus|
Inferior frontal sulcus|Sillon frontal inférieur||enc/frontal|sulcus|
Orbital part of  inferior frontal gyrus|Partie orbitaire du gyrus frontal inférieur||enc/frontal|grey|
Lat_Fis-ant-Horizont|Rameau antérieur horizontal du sillon latéral||enc/sulci|sulcus|lateral_sulcus
Lat_Fis-ant-Vertical|Rameau antérieur ascendant du sillon latéral||enc/sulci|sulcus|lateral_sulcus
Middle frontal gyrus|Gyrus frontal moyen|2e circonvolution frontale, F2|enc/frontal|grey|
Olfactory sulcus|Sillon olfactif||enc/frontal|sulcus|
Opercular part of inferior frontal gyrus|Partie operculaire du gyrus frontal inférieur|pied de F3, aire de Broca|enc/frontal|grey|
Orbital gyri (Frontomarginal gyrus and sulcus*)|Gyrus et sillon frontomarginaux||enc/frontal|grey|orbital_gyri
Orbital gyri|Gyrus orbitaires||enc/frontal|grey|orbital_gyri
Orbital sulci (H-shaped orbital sulci*)|Sillons orbitaires en H||enc/frontal|sulcus|orbital_sulci
Orbital sulci (Lateral Orbital sulcus*)|Sillon orbitaire latéral||enc/frontal|sulcus|orbital_sulci
Paracentral gyrus and sulcus*|Lobule paracentral||enc/frontal|grey|
Paracentral sulcus|Sillon paracentral||enc/frontal|sulcus|
Precentral gyrus|Gyrus précentral|frontale ascendante, aire motrice primaire|enc/frontal|grey|
Precentral sulcus (inferior part)*|Partie inférieure du sillon précentral||enc/frontal|sulcus|precentral_sulcus
Precentral sulcus (Superior part)*|Partie supérieure du sillon précentral||enc/frontal|sulcus|precentral_sulcus
Straight gyrus (Gyrus rectus)|Gyrus droit|gyrus rectus|enc/frontal|grey|
Superior frontal gyrus|Gyrus frontal supérieur|1re circonvolution frontale, F1|enc/frontal|grey|
Superior frontal sulcus|Sillon frontal supérieur||enc/frontal|sulcus|
Transverse frontopolar gyrus and sulcus*|Gyrus et sillon frontopolaires transverses||enc/frontal|grey|
Triangular part of inferior frontal gyrus|Partie triangulaire du gyrus frontal inférieur|cap de F3, aire de Broca|enc/frontal|grey|
Insula (Subcentral gyrus and ant. and post. sulci*)|Insula|lobe de l'insula|enc/limbic|grey|
Posterior transverse collateral sulcus|Sillon collatéral transverse postérieur||enc/occipital|sulcus|
Anterior occipital sulcus*|Sillon occipital antérieur||enc/sulci|sulcus|
Central sulcus|Sillon central|scissure de Rolando|enc/sulci|sulcus|
Circular sulcus of insula|Sillon circulaire de l'insula||enc/sulci|sulcus|
Collateral sulcus|Sillon collatéral||enc/sulci|sulcus|
Lat_Fis-post|Rameau postérieur du sillon latéral|scissure de Sylvius|enc/sulci|sulcus|lateral_sulcus
Parieto-occipital sulcus|Sillon pariéto-occipital|scissure perpendiculaire interne|enc/sulci|sulcus|
Subparietal sulcus|Sillon subpariétal||enc/sulci|sulcus|
Sulcus interm_prim-Jensen|Sillon intermédiaire primaire|sillon de Jensen|enc/sulci|sulcus|
Lateral ventricle|Ventricule latéral||enc/vent|ventricle|
Cingulate gyrus (Posteroventral part*)|Partie postéro-ventrale du gyrus cingulaire||enc/limbic|grey|cingulate
Cingulate gyrus and sulcus (Middle anterior part)|Partie moyenne antérieure du gyrus cingulaire||enc/limbic|grey|cingulate
Cingulate gyrus and sulcus (Middle posterior part)|Partie moyenne postérieure du gyrus cingulaire||enc/limbic|grey|cingulate
Cingulate gyrus and sulcus (Posterior dorsal part)|Partie postéro-dorsale du gyrus cingulaire||enc/limbic|grey|cingulate
Cingulate sulcus (Marginal part*)|Partie marginale du sillon cingulaire||enc/sulci|sulcus|
Hippocampus|Hippocampe||enc/limbic|grey|
Calcarine sulcus|Sillon calcarin|scissure calcarine|enc/occipital|sulcus|
Cuneus|Cunéus||enc/occipital|grey|
Inferior occipital gyrus and sulcus*|Gyrus et sillon occipitaux inférieurs||enc/occipital|grey|
Lateral occipital gyrus (Middle occipital gyrus*)|Gyrus occipital moyen||enc/occipital|grey|
Lingual gyrus|Gyrus lingual||enc/occipital|grey|
Lunate sulcus|Sillon semi-lunaire||enc/occipital|sulcus|
Occipital pole|Pôle occipital||enc/occipital|grey|
Superior occipital gyri|Gyrus occipital supérieur||enc/occipital|grey|
Transverse occipital sulcus|Sillon occipital transverse||enc/occipital|sulcus|
Angular gyrus|Gyrus angulaire|pli courbe|enc/parietal|grey|
Intraparietal sulcus|Sillon intrapariétal||enc/parietal|sulcus|
Postcentral gyrus|Gyrus postcentral|pariétale ascendante, aire somesthésique primaire|enc/parietal|grey|
Postcentral sulcus|Sillon postcentral||enc/parietal|sulcus|
Precuneus|Précunéus||enc/parietal|grey|
Superior parietal lobule|Lobule pariétal supérieur||enc/parietal|grey|
Supramarginal gyrus|Gyrus supramarginal||enc/parietal|grey|
Inferior temporal gyrus|Gyrus temporal inférieur|T3|enc/temporal|grey|
Inferior temporal sulcus|Sillon temporal inférieur||enc/temporal|sulcus|
Lateral occipitotemporal gyrus|Gyrus occipito-temporal latéral|gyrus fusiforme|enc/temporal|grey|
Medial occipitotemporal gyrus (Parahippocampal*)|Gyrus parahippocampique||enc/limbic|grey|
Middle temporal gyrus|Gyrus temporal moyen|T2|enc/temporal|grey|
Occipitotemporal sulcus (Lateral part*)|Sillon occipito-temporal||enc/temporal|sulcus|
Superior temporal gyrus (Lateral part)|Gyrus temporal supérieur|T1, aire de Wernicke en arrière|enc/temporal|grey|
Superior temporal sulcus|Sillon temporal supérieur||enc/temporal|sulcus|
Temporal plane|Planum temporal||enc/temporal|grey|
Temporal pole|Pôle temporal||enc/temporal|grey|
Transverse temporal gyri|Gyrus temporaux transverses|gyrus de Heschl, aire auditive primaire|enc/temporal|grey|
Septum pellucidum|Septum pellucidum|septum lucidum|enc/vent|white|
White matter of telencephalon|Substance blanche du télencéphale|centre ovale|enc/deep|white|
Stria terminalis|Strie terminale||enc/deep|white|
Anterior commissure|Commissure antérieure|commissure blanche antérieure|enc/deep|white|
Corpus callosum|Corps calleux||enc/deep|white|
Hippocampal commissure|Commissure du fornix|commissure hippocampique|enc/deep|white|
Fornix|Fornix|trigone cérébral|enc/limbic|white|
Falx cerebri|Faux du cerveau||men/men|meninge|
Tentorium cerebelli|Tente du cervelet||men/men|meninge|
Spinal dura|Dure-mère spinale||men/men|meninge|
Choroid plexus|Plexus choroïde||enc/vent|ventricle|
Central canal|Canal central de la moelle spinale|canal de l'épendyme|spinal/grey|ventricle|central_canal
Central canal'|Canal central, partie bulbaire||spinal/grey|ventricle|central_canal
Anterior horn of spinal cord|Corne antérieure de la moelle spinale|corne ventrale, motrice|spinal/grey|grey|
Nucleus of accessory nerve|Noyau du nerf accessoire|noyau du XI|spinal/grey|nucleus|
Intermediolateral nucleus|Noyau intermédio-latéral|corne latérale, sympathique|spinal/grey|nucleus|
Intermediomedial nucleus|Noyau intermédio-médial||spinal/grey|nucleus|
Lateral intermediate substance|Substance intermédiaire latérale||spinal/grey|grey|
Nucleus proprius|Noyau propre de la corne postérieure||spinal/grey|nucleus|
Posterior horn of spinal cord|Corne postérieure de la moelle spinale|corne dorsale, sensitive|spinal/grey|grey|
Spinal reticular process|Processus réticulaire de la moelle spinale||spinal/grey|grey|
Anterior corticospinal tract|Faisceau corticospinal antérieur|faisceau pyramidal direct|spinal/tracts|white|
Anterior fasciculus proprius|Faisceau propre antérieur||spinal/tracts|white|
Lateral vestibulospinal tract|Faisceau vestibulospinal latéral||spinal/tracts|white|
Medial reticulospinal tract|Faisceau réticulospinal médial||spinal/tracts|white|
Medial vestibulospinal tract|Faisceau vestibulospinal médial||spinal/tracts|white|
Tectospinal tract|Faisceau tectospinal||spinal/tracts|white|
Anterior spinothalamic tract|Faisceau spinothalamique antérieur||spinal/tracts|white|
Lateral spinothalamic tract|Faisceau spinothalamique latéral||spinal/tracts|white|
Spinotectal tract|Faisceau spinotectal||spinal/tracts|white|
Anterior spinocerebellar tract|Faisceau spinocérébelleux antérieur|faisceau de Gowers|spinal/tracts|white|
Lateral corticospinal tract|Faisceau corticospinal latéral|faisceau pyramidal croisé|spinal/tracts|white|
Lateral fasciculus proprius|Faisceau propre latéral||spinal/tracts|white|
Lateral reticulospinal tract|Faisceau réticulospinal latéral||spinal/tracts|white|
Posterior spinocerebellar tract|Faisceau spinocérébelleux postérieur|faisceau de Flechsig|spinal/tracts|white|
Rubrospinal tract|Faisceau rubrospinal||spinal/tracts|white|
Cuneate fasciculus|Faisceau cunéiforme|faisceau de Burdach|spinal/tracts|white|
Gracile fasciculus|Faisceau gracile|faisceau de Goll|spinal/tracts|white|
Posterior fasciculus proprius|Faisceau propre postérieur||spinal/tracts|white|
Posterolateral tract|Faisceau dorsolatéral|zone de Lissauer|spinal/tracts|white|
White matter of spinal cord|Substance blanche de la moelle spinale||spinal/tracts|white|
Sympathetic nerves|Nerfs sympathiques||trunk/auto|nerve|
Sympathetic trunk|Tronc sympathique|chaîne sympathique latéro-vertébrale|trunk/auto|nerve|
Ganglia of sympathetic trunk|Ganglions du tronc sympathique||trunk/auto|ganglion|
Abducens nerve (VI)|Nerf abducens (VI)|moteur oculaire externe|cranial/cn|nerve|
Facial nerve (VII)|Nerf facial (VII)||cranial/cn|nerve|
Chorda tympani|Corde du tympan||cranial/cn|nerve|
Glossopharyngeal nerve (IX)|Nerf glossopharyngien (IX)||cranial/cn|nerve|
Hypoglossal nerve (XII)|Nerf hypoglosse (XII)|grand hypoglosse|cranial/cn|nerve|
Oculomotor nerve (III)|Nerf oculomoteur (III)|moteur oculaire commun|cranial/cn|nerve|
Olfactory nerve (I)|Nerf olfactif (I)||cranial/cn|nerve|
Optic nerve (II)|Nerf optique (II)||cranial/cn|nerve|
Trigeminal nerve (V)|Nerf trijumeau (V)||cranial/trig|nerve|
Maxillary nerve|Nerf maxillaire (V2)||cranial/trig|nerve|
Meningeal branch of maxillary nerve|Rameau méningé du nerf maxillaire||cranial/trig|nerve|-
Motor root of trigeminal nerve|Racine motrice du nerf trijumeau||cranial/trig|nerve|
Ophthalmic nerve|Nerf ophtalmique (V1)|nerf ophtalmique de Willis|cranial/trig|nerve|
Sensory root of trigeminal nerve|Racine sensitive du nerf trijumeau||cranial/trig|nerve|
Anterior division of mandibular nerve|Tronc antérieur du nerf mandibulaire (V3)||cranial/trig|nerve|
Buccal nerve|Nerf buccal||cranial/trig|nerve|
Posterior division of mandibular nerve|Tronc postérieur du nerf mandibulaire (V3)||cranial/trig|nerve|
Inferior alveolar nerve|Nerf alvéolaire inférieur|nerf dentaire inférieur|cranial/trig|nerve|
Mental nerve|Nerf mentonnier||cranial/trig|nerve|
Nerve to mylohyoid muscle|Nerf mylohyoïdien||cranial/trig|nerve|
Lingual nerve|Nerf lingual||cranial/trig|nerve|
Trochlear nerve (IV)|Nerf trochléaire (IV)|nerf pathétique|cranial/cn|nerve|
Vagus nerve (X)|Nerf vague (X)|nerf pneumogastrique|cranial/cn|nerve|
Vestibulocochlear nerve (VIII)|Nerf vestibulocochléaire (VIII)|nerf auditif|cranial/cn|nerve|
Cochlear nerve|Nerf cochléaire||cranial/cn|nerve|
Vestibular nerve|Nerf vestibulaire||cranial/cn|nerve|
Spinal ganglion|Ganglion spinal|ganglion rachidien|trunk/spn|ganglion|
Cauda equina|Queue de cheval||trunk/spn|nerve|
Anterior root of spinal nerve|Racine antérieure du nerf spinal|racine ventrale, motrice|trunk/spn|nerve|
Lateral pectoral nerve|Nerf pectoral latéral||ul/other|nerve|
Musculocutaneous nerve|Nerf musculocutané||ul/other|nerve|
Lateral antebrachial cutaneous nerve|Nerf cutané latéral de l'avant-bras||ul/other|nerve|
Medial antebrachial cutaneous nerve|Nerf cutané médial de l'avant-bras|brachial cutané interne|ul/other|nerve|
Anterior branch of medial antebrachial cutaneous nerve|Rameau antérieur du nerf cutané médial de l'avant-bras||ul/other|nerve|-
Posterior branch of medial antebrachial cutaneous nerve|Rameau postérieur du nerf cutané médial de l'avant-bras||ul/other|nerve|-
Medial brachial cutaneous nerve|Nerf cutané médial du bras|accessoire du brachial cutané interne|ul/other|nerve|
Medial pectoral nerve|Nerf pectoral médial||ul/other|nerve|
Ulnar nerve|Nerf ulnaire|nerf cubital|ul/ulnar|nerve|
Deep branch of ulnar nerve|Rameau profond du nerf ulnaire||ul/ulnar|nerve|
Dorsal branch of ulnar nerve|Rameau dorsal du nerf ulnaire||ul/ulnar|nerve|
Dorsal digital branches of ulnar nerve|Nerfs digitaux dorsaux du nerf ulnaire||ul/ulnar|nerve|-
Muscular branches of ulnar nerve|Rameaux musculaires du nerf ulnaire||ul/ulnar|nerve|-
Palmar branch of ulnar nerve|Rameau palmaire du nerf ulnaire||ul/ulnar|nerve|
Superficial branch of ulnar nerve|Rameau superficiel du nerf ulnaire||ul/ulnar|nerve|
Common palmar digital branches of ulnar nerve|Nerfs digitaux palmaires communs du nerf ulnaire||ul/ulnar|nerve|-
Proper palmar digital branches of ulnar nerve|Nerfs digitaux palmaires propres du nerf ulnaire||ul/ulnar|nerve|-
Axillary nerve|Nerf axillaire|nerf circonflexe|ul/other|nerve|
Muscular branches of axillary nerve|Rameaux musculaires du nerf axillaire||ul/other|nerve|-
Superior lateral brachial cutaneous nerve|Nerf cutané latéral supérieur du bras||ul/other|nerve|
Inferior subscapular nerve|Nerf subscapulaire inférieur||ul/other|nerve|
Radial nerve|Nerf radial||ul/radial|nerve|
Deep branch of radial nerve|Rameau profond du nerf radial||ul/radial|nerve|
Posterior interosseous nerve of forearm|Nerf interosseux postérieur de l'avant-bras||ul/radial|nerve|
Inferior lateral brachial cutaneous nerve|Nerf cutané latéral inférieur du bras||ul/radial|nerve|
Muscular branches of radial nerve|Rameaux musculaires du nerf radial||ul/radial|nerve|-
Posterior antebrachial cutaneous nerve|Nerf cutané postérieur de l'avant-bras||ul/radial|nerve|
Superficial branch of radial nerve|Rameau superficiel du nerf radial||ul/radial|nerve|
Dorsal digital branches of radial nerve|Nerfs digitaux dorsaux du nerf radial||ul/radial|nerve|-
Superior subscapular nerve|Nerf subscapulaire supérieur||ul/other|nerve|
Thoracodorsal nerve|Nerf thoracodorsal|nerf du grand dorsal|ul/other|nerve|
Posterior cord of brachial plexus|Faisceau postérieur du plexus brachial|tronc secondaire postérieur|ul/plexus|nerve|
Median nerve|Nerf médian||ul/median|nerve|
(Communicating branch of median nerve with ulnar nerve)|Rameau communicant du nerf médian avec le nerf ulnaire||ul/median|nerve|-
Anterior interosseous nerve of forearm|Nerf interosseux antérieur de l'avant-bras||ul/median|nerve|
Common palmar digital branches of median nerve|Nerfs digitaux palmaires communs du nerf médian||ul/median|nerve|-
Proper palmar digital branches of median nerve|Nerfs digitaux palmaires propres du nerf médian||ul/median|nerve|-
Muscular branches of median nerve|Rameaux musculaires du nerf médian||ul/median|nerve|-
Palmar branch of median nerve|Rameau palmaire du nerf médian||ul/median|nerve|
Dorsal scapular nerve|Nerf dorsal de la scapula|nerf de l'angulaire et du rhomboïde|ul/other|nerve|
Long thoracic nerve|Nerf thoracique long|nerf de Charles Bell|ul/other|nerve|
Subclavian nerve|Nerf subclavier||ul/other|nerve|
Suprascapular nerve|Nerf suprascapulaire|nerf sus-scapulaire|ul/other|nerve|
Inferior trunk of brachial plexus|Tronc inférieur du plexus brachial|tronc primaire inférieur|ul/plexus|nerve|
Anterior division of inferior trunk of brachial plexus|Division antérieure du tronc inférieur du plexus brachial||ul/plexus|nerve|
Posterior division of inferior trunk of brachial plexus|Division postérieure du tronc inférieur du plexus brachial||ul/plexus|nerve|
Middle trunk of brachial plexus|Tronc moyen du plexus brachial|tronc primaire moyen|ul/plexus|nerve|
Anterior division of middle trunk of brachial plexus|Division antérieure du tronc moyen du plexus brachial||ul/plexus|nerve|
Posterior division of middle trunk of brachial plexus|Division postérieure du tronc moyen du plexus brachial||ul/plexus|nerve|
Roots of brachial plexus|Racines du plexus brachial|C5 à T1|ul/plexus|nerve|
Superior trunk of brachial plexus|Tronc supérieur du plexus brachial|tronc primaire supérieur|ul/plexus|nerve|
Anterior division of superior trunk of brachial plexus|Division antérieure du tronc supérieur du plexus brachial||ul/plexus|nerve|
Posterior division of superior trunk of brachial plexus|Division postérieure du tronc supérieur du plexus brachial||ul/plexus|nerve|
Accessory nerve (XI)|Nerf accessoire (XI)|nerf spinal|cranial/cn|nerve|
Ilio-inguinal nerve|Nerf ilio-inguinal|nerf petit abdomino-génital|ll/lumbar|nerve|
Iliohypogastric nerve|Nerf ilio-hypogastrique|nerf grand abdomino-génital|ll/lumbar|nerve|
Genitofemoral nerve|Nerf génitofémoral|nerf génito-crural|ll/lumbar|nerve|
Femoral branch of genitofemoral nerve|Rameau fémoral du nerf génitofémoral||ll/lumbar|nerve|
Genital branch of genitofemoral nerve|Rameau génital du nerf génitofémoral||ll/lumbar|nerve|
Obturator nerve|Nerf obturateur||ll/lumbar|nerve|
Anterior branch of obturator nerve|Rameau antérieur du nerf obturateur||ll/lumbar|nerve|
Posterior branch of obturator nerve|Rameau postérieur du nerf obturateur||ll/lumbar|nerve|
Femoral nerve|Nerf fémoral|nerf crural|ll/lumbar|nerve|
Anterior cutaneous branches of femoral nerve|Rameaux cutanés antérieurs du nerf fémoral||ll/lumbar|nerve|-
Saphenous nerve|Nerf saphène|nerf saphène interne|ll/lumbar|nerve|
Infrapatellar branch of saphenous nerve|Rameau infrapatellaire du nerf saphène||ll/lumbar|nerve|
Medial crural cutaneous branches of saphenous nerve|Rameaux cutanés médiaux de la jambe du nerf saphène||ll/lumbar|nerve|-
Lateral femoral cutaneous nerve|Nerf cutané latéral de la cuisse|nerf fémoro-cutané|ll/lumbar|nerve|
Anterior root of posterior femoral cutaneous nerve|Racine antérieure du nerf cutané postérieur de la cuisse||ll/sacral|nerve|-
Nerve to piriformis muscle|Nerf du muscle piriforme||ll/sacral|nerve|
Nerve to quadratus femoris muscle|Nerf du muscle carré fémoral||ll/sacral|nerve|
Posterior femoral cutaneous nerve|Nerf cutané postérieur de la cuisse|nerf petit sciatique|ll/sacral|nerve|
Posterior root of posterior femoral cutaneous nerve|Racine postérieure du nerf cutané postérieur de la cuisse||ll/sacral|nerve|-
Pudendal nerve|Nerf pudendal|nerf honteux interne|ll/sacral|nerve|
Sciatic nerve|Nerf ischiatique|nerf grand sciatique|ll/sacral|nerve|
Common fibular nerve|Nerf fibulaire commun|nerf sciatique poplité externe|ll/fibular|nerve|
Deep fibular nerve|Nerf fibulaire profond|nerf tibial antérieur|ll/fibular|nerve|
Dorsal digital branches of deep fibular nerve|Nerfs digitaux dorsaux du nerf fibulaire profond||ll/fibular|nerve|-
Muscular branches of deep fibular nerve|Rameaux musculaires du nerf fibulaire profond||ll/fibular|nerve|-
Superficial fibular nerve|Nerf fibulaire superficiel|nerf musculo-cutané de la jambe|ll/fibular|nerve|
Dorsal digital branches of superficial fibular nerve|Nerfs digitaux dorsaux du nerf fibulaire superficiel||ll/fibular|nerve|-
Intermediate dorsal cutaneous nerve of foot|Nerf cutané dorsal intermédiaire du pied||ll/fibular|nerve|
Medial dorsal cutaneous nerve of foot|Nerf cutané dorsal médial du pied||ll/fibular|nerve|
Sural communicating branch of common fibular nerve|Rameau communicant sural du nerf fibulaire commun|nerf accessoire du saphène externe|ll/fibular|nerve|
Tibial nerve|Nerf tibial|nerf sciatique poplité interne|ll/tibial|nerve|
Lateral plantar nerve|Nerf plantaire latéral|nerf plantaire externe|ll/tibial|nerve|
Common plantar digital branches of lateral plantar nerve|Nerfs digitaux plantaires communs du nerf plantaire latéral||ll/tibial|nerve|-
Proper plantar digital branches of lateral plantar nerve|Nerfs digitaux plantaires propres du nerf plantaire latéral||ll/tibial|nerve|-
Medial plantar nerve|Nerf plantaire médial|nerf plantaire interne|ll/tibial|nerve|
Common plantar digital branches of medial plantar nerve|Nerfs digitaux plantaires communs du nerf plantaire médial||ll/tibial|nerve|-
Proper plantar digital branches of medial plantar nerve|Nerfs digitaux plantaires propres du nerf plantaire médial||ll/tibial|nerve|-
Medial sural cutaneous nerve|Nerf cutané sural médial||ll/tibial|nerve|
Sural nerve|Nerf sural|nerf saphène externe|ll/tibial|nerve|
Superior gluteal nerve|Nerf glutéal supérieur|nerf fessier supérieur|ll/sacral|nerve|
Posterior root of spinal nerve|Racine postérieure du nerf spinal|racine dorsale, sensitive|trunk/spn|nerve|
Intercostal nerves|Nerfs intercostaux||trunk/spn|nerve|
Tympanic membrane|Membrane du tympan|tympan|sense/ear|sense|
Cochlea|Cochlée|limaçon|sense/ear|sense|
Vestibule|Vestibule de l'oreille interne||sense/ear|sense|
Auditory tube|Trompe auditive|trompe d'Eustache|sense/ear|sense|
Lacrimal canaliculus|Canalicule lacrymal||sense/lacr|sense|
Ampulla of lacrimal canaliculus|Ampoule du canalicule lacrymal||sense/lacr|sense|
Lacrimal gland|Glande lacrymale||sense/lacr|sense|
Lacrimal sac|Sac lacrymal||sense/lacr|sense|
Nasolacrimal duct|Conduit lacrymonasal|canal lacrymo-nasal|sense/lacr|sense|
Suspensory ligament of eyeball|Ligament suspenseur du bulbe de l'œil|ligament de Lockwood|sense/eye|sense|
Anterior segment of eyeball|Segment antérieur du bulbe de l'œil||sense/eye|sense|
Anterior chamber of eyeball|Chambre antérieure du bulbe de l'œil||sense/eye|sense|
Zonular fibres|Fibres zonulaires|zonule de Zinn|sense/eye|sense|
Cornea|Cornée||sense/eye|sense|
Iris|Iris||sense/eye|sense|
Lens|Lentille|cristallin|sense/eye|sense|
Posterior segment of eyeball|Segment postérieur du bulbe de l'œil||sense/eye|sense|
Vitreous body|Corps vitré||sense/eye|sense|
Retina|Rétine||sense/eye|sense|
Sclera|Sclère|sclérotique|sense/eye|sense|
"""

GROUPS = {
    'lateral_sulcus': ('Sillon latéral (scissure de Sylvius)', 'Sillon latéral'),
    'orbital_gyri': ('Gyrus orbitaires', 'Gyrus orbitaires'),
    'orbital_sulci': ('Sillons orbitaires', 'Sillons orbitaires'),
    'precentral_sulcus': ('Sillon précentral', 'Sillon précentral'),
    'cingulate': ('Gyrus cingulaire (circonvolution du corps calleux)', 'Gyrus cingulaire'),
    'central_canal': ('Canal central de la moelle spinale (canal de l’épendyme)', 'Canal central de la moelle spinale'),
}

REGIONS = [
    ('enc', 'Encéphale', [('frontal', 'Lobe frontal'), ('parietal', 'Lobe pariétal'), ('temporal', 'Lobe temporal'), ('occipital', 'Lobe occipital'),
                          ('limbic', 'Lobe limbique et insula'), ('sulci', 'Sillons interlobaires'), ('deep', 'Noyaux gris centraux et substance blanche'),
                          ('vent', 'Ventricules'), ('dien', 'Diencéphale'), ('stem', 'Tronc cérébral'), ('cereb', 'Cervelet')]),
    ('spinal', 'Moelle spinale', [('grey', 'Substance grise'), ('tracts', 'Substance blanche et faisceaux')]),
    ('cranial', 'Nerfs crâniens', [('cn', 'Les douze paires'), ('trig', 'Nerf trijumeau et ses branches')]),
    ('trunk', 'Nerfs spinaux et système autonome', [('spn', 'Nerfs spinaux'), ('auto', 'Système sympathique')]),
    ('ul', 'Membre supérieur', [('plexus', 'Plexus brachial'), ('median', 'Nerf médian'), ('ulnar', 'Nerf ulnaire'), ('radial', 'Nerf radial'), ('other', 'Autres nerfs')]),
    ('ll', 'Membre inférieur', [('lumbar', 'Plexus lombaire'), ('sacral', 'Plexus sacral et nerf ischiatique'), ('fibular', 'Nerf fibulaire commun'), ('tibial', 'Nerf tibial')]),
    ('sense', 'Organes des sens', [('eye', 'Œil'), ('lacr', 'Appareil lacrymal'), ('ear', 'Oreille')]),
    ('men', 'Méninges', [('men', 'Dure-mère')]),
]

TIPS = {
    'all': 'Essentiels : chaque structure une seule fois, côtés réunis ; les fins rameaux sont dans « Toutes ». Les méninges se révisent à part.',
    'enc': 'L’encéphale comprend le cerveau (télencéphale et diencéphale), le tronc cérébral et le cervelet. Les structures profondes se voient mieux en rayons X.',
    'frontal': 'Le gyrus précentral est l’aire motrice primaire ; l’aire de Broca (langage articulé) occupe les parties operculaire et triangulaire du gyrus frontal inférieur, à gauche.',
    'parietal': 'Le gyrus postcentral est l’aire somesthésique primaire, organisée en homoncule. Gyrus supramarginal et angulaire : langage et lecture.',
    'temporal': 'Les gyrus temporaux transverses (de Heschl) sont l’aire auditive primaire ; l’aire de Wernicke (compréhension) est en arrière du gyrus temporal supérieur.',
    'occipital': 'Le cortex visuel primaire borde le sillon calcarin, entre le cunéus (au-dessus) et le gyrus lingual (au-dessous).',
    'limbic': 'Le système limbique (gyrus cingulaire, hippocampe, gyrus parahippocampique, corps amygdaloïde, fornix) gère mémoire et émotions.',
    'sulci': 'Le sillon central sépare lobes frontal et pariétal ; le sillon latéral sépare le lobe temporal ; le sillon pariéto-occipital limite le lobe occipital.',
    'deep': 'Corps strié = noyau caudé + noyau lenticulaire (putamen + globus pallidus). Le corps calleux relie les deux hémisphères.',
    'vent': 'Ventricules latéraux → foramens interventriculaires → troisième ventricule → aqueduc du mésencéphale → quatrième ventricule. Les plexus choroïdes sécrètent le LCS.',
    'dien': 'Le thalamus est le relais sensitif vers le cortex ; corps géniculés latéral (vision) et médial (audition). L’hypothalamus commande l’hypophyse.',
    'stem': 'De haut en bas : mésencéphale, pont, moelle allongée. Noyaux des nerfs crâniens : III et IV dans le mésencéphale, V à VIII dans le pont, IX à XII dans la moelle allongée.',
    'cereb': 'Le vermis est au milieu, les hémisphères cérébelleux de chaque côté. Le flocculus et le nodule forment le lobe flocculo-nodulaire (équilibre).',
    'spinal': 'Substance grise en papillon au centre, substance blanche autour. Corne antérieure motrice, corne postérieure sensitive.',
    'grey': 'La corne latérale (noyau intermédio-latéral, de T1 à L2) contient les neurones sympathiques préganglionnaires.',
    'tracts': 'Voies ascendantes : cordons postérieurs (gracile et cunéiforme, tact fin), spinothalamiques (douleur, température). Voie descendante principale : corticospinale latérale.',
    'cranial': 'I olfactif, II optique, III oculomoteur, IV trochléaire, V trijumeau, VI abducens, VII facial, VIII vestibulocochléaire, IX glossopharyngien, X vague, XI accessoire, XII hypoglosse.',
    'cn': 'Moteurs de l’œil : III, IV (oblique supérieur) et VI (droit latéral). Le nerf vague descend jusqu’à l’abdomen (innervation parasympathique des viscères).',
    'trig': 'Trois branches du trijumeau : ophtalmique (V1), maxillaire (V2) et mandibulaire (V3), seule à avoir une part motrice (muscles masticateurs).',
    'trunk': '31 paires de nerfs spinaux, chacun formé d’une racine antérieure (motrice) et d’une racine postérieure (sensitive, avec le ganglion spinal).',
    'spn': 'La moelle s’arrête vers L1-L2 ; en dessous, les racines forment la queue de cheval. Les nerfs intercostaux sont les rameaux antérieurs de T1 à T11.',
    'auto': 'Le tronc sympathique longe la colonne de chaque côté, avec une chaîne de ganglions reliés aux nerfs spinaux.',
    'ul': 'Plexus brachial (C5-T1) : racines, troncs, divisions, faisceaux, branches terminales (« Robert Taylor Drinks Cold Beer »).',
    'plexus': 'Trois troncs (supérieur C5-C6, moyen C7, inférieur C8-T1), chacun divisé en division antérieure et postérieure ; les postérieures forment le faisceau postérieur.',
    'median': 'Le nerf médian passe dans le canal carpien ; son atteinte (syndrome du canal carpien) touche l’éminence thénar et la sensibilité des trois premiers doigts.',
    'ulnar': 'Le nerf ulnaire passe derrière l’épicondyle médial, juste sous la peau (le choc électrique quand on se cogne le coude) ; il innerve l’hypothénar, les interosseux et le 5e doigt.',
    'radial': 'Le nerf radial contourne l’humérus dans le sillon du nerf radial ; il innerve tous les extenseurs. Atteinte : main tombante.',
    'other': 'Nerf axillaire : deltoïde et petit rond (autour du col chirurgical de l’humérus). Nerf musculocutané : loge antérieure du bras.',
    'll': 'Plexus lombaire (L1-L4) en avant : nerfs fémoral et obturateur. Plexus sacral (L4-S4) en arrière : nerf ischiatique, le plus gros nerf du corps.',
    'lumbar': 'Nerf fémoral : loge antérieure de la cuisse (quadriceps) ; nerf obturateur : adducteurs. Le nerf saphène est sa branche sensitive jusqu’au pied.',
    'sacral': 'Le nerf ischiatique sort sous le muscle piriforme et se divise, au-dessus du genou, en nerfs tibial et fibulaire commun.',
    'fibular': 'Le nerf fibulaire commun contourne le col de la fibula, où il est vulnérable : son atteinte donne un pied tombant (steppage).',
    'tibial': 'Le nerf tibial descend derrière le genou et la jambe, passe derrière la malléole médiale et se divise en nerfs plantaires médial et latéral.',
    'sense': 'Organes des sens présents ici : œil et appareil lacrymal, oreille moyenne et interne.',
    'eye': 'Trois tuniques du bulbe : fibreuse (sclère, cornée), vasculaire (iris), nerveuse (rétine). La lentille (cristallin) est suspendue par la zonule.',
    'lacr': 'Les larmes vont de la glande lacrymale aux canalicules lacrymaux, au sac lacrymal puis au conduit lacrymonasal, qui s’ouvre dans le méat nasal inférieur.',
    'ear': 'Oreille moyenne : membrane du tympan, trompe auditive vers le pharynx. Oreille interne : cochlée (audition) et vestibule (équilibre).',
    'men': 'Trois méninges : dure-mère, arachnoïde, pie-mère. Replis de la dure-mère : faux du cerveau (entre les hémisphères) et tente du cervelet.',
}

# ---- réglages du générateur (build_system.py) ----
INVENTORY = 'nq_nervous'
PREFIX = 'n_'
SEPARATE = {'men'}   # la dure-mère spinale recouvre la moelle : révisée à part
FEMININE = ['moelle', 'olive', 'pyramide', 'fosse', 'base', 'aile', 'lingula', 'tonsille', 'uvule', 'habénula', 'strie', 'commissure', 'partie',
            'insula', 'substance', 'faux', 'tente', 'dure-mère', 'corne', 'queue', 'racine', 'division', 'corde', 'ampoule', 'glande', 'membrane',
            'cochlée', 'trompe', 'chambre', 'cornée', 'lentille', 'sclère', 'rétine']
PLURAL = ['noyaux', 'nerfs', 'rameaux', 'racines', 'sillons', 'fibres', 'ganglions', 'gyrus']
BACK_SUBS = {'cereb', 'occipital', 'grey', 'tracts', 'sacral', 'tibial'}
BACK_IDS = {'Sciatic nerve', 'Posterior femoral cutaneous nerve', 'Common fibular nerve', 'Sural communicating branch of common fibular nerve', 'Superior gluteal nerve',
            'Posterior root of spinal nerve', 'Spinal ganglion', 'Cauda equina', 'Inferior colliculus', 'Superior colliculus', 'Fourth ventricle'}
FRONT_IDS = {'Lateral plantar nerve', 'Medial plantar nerve', 'Common plantar digital branches of lateral plantar nerve', 'Proper plantar digital branches of lateral plantar nerve',
             'Common plantar digital branches of medial plantar nerve', 'Proper plantar digital branches of medial plantar nerve'}

def camera(reg, sub, en, c):
    """Zone de caméra (clés des régions osseuses) et vue de dos éventuelle."""
    cy = c[1]
    if reg in ('enc', 'cranial') or sub in ('eye', 'lacr'):
        zone = ('head/ear' if en in ('Cochlear nerve', 'Vestibular nerve', 'Vestibulocochlear nerve (VIII)') else 'torso/ribcage' if en == 'Vagus nerve (X)'
                else 'torso/spine' if en == 'Accessory nerve (XI)' else 'head')   # X et XI descendent loin dans le cou et le thorax
    elif sub == 'ear': zone = 'head/ear'
    elif reg == 'men': zone = 'torso/spine' if en == 'Spinal dura' else 'head'
    elif reg == 'spinal': zone = 'torso/spine'
    elif reg == 'trunk': zone = 'torso/ribcage' if en == 'Intercostal nerves' else ('torso/pelvis' if en == 'Cauda equina' else 'torso/spine')
    elif reg == 'ul': zone = 'hand' if cy < 0.83 else 'arm'
    else: zone = 'foot' if cy < 0.13 else ('torso/pelvis' if cy > 0.78 else 'leg')
    back = (sub in BACK_SUBS or en in BACK_IDS) and en not in FRONT_IDS and zone != 'foot'
    return zone, 'back' if back else ''
