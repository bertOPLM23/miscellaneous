# Table des muscles : nom Z-Anatomy (anglais, sans .l/.r) -> données françaises.
# Format de chaque ligne : anglais | nom officiel | nom usuel (vide si aucun) | section (région/loge) | type | groupe
#   type   : muscle, tendon (tendons, aponévroses, ligaments, tarses), fascia (fascias, septums, rétinaculums), bourse, gaine
#   groupe : clé du groupe « essentiels » (fusionne gauche/droite et les chefs d'un même muscle) ;
#            vide = groupe propre ; « - » = hors essentiels.
ROWS = r"""
Superficial investing cervical fascia|Lame superficielle du fascia cervical|aponévrose cervicale superficielle|annex/fhead|fascia|-
Diaphragmatic fascia|Fascia diaphragmatique||annex/ftrunk|fascia|-
Iliopsoas fascia|Fascia iliaque|fascia du muscle ilio-psoas|annex/ftrunk|fascia|-
Transversalis fascia|Fascia transversalis||annex/ftrunk|fascia|-
Investing abdominal fascia|Fascia de revêtement de l'abdomen||annex/ftrunk|fascia|-
Masseteric fascia|Fascia massétérique||annex/fhead|fascia|-
Superficial layer of temporal fascia|Lame superficielle du fascia temporal||annex/fhead|fascia|-
Anterior intermuscular septum of leg|Septum intermusculaire antérieur de la jambe||annex/fll|fascia|-
Crural fascia|Fascia de la jambe|aponévrose jambière|annex/fll|fascia|-
Fascia lata|Fascia lata|aponévrose fémorale|annex/fll|fascia|-
Flexor retinaculum of ankle|Rétinaculum des fléchisseurs de la cheville|ligament annulaire interne|annex/fll|fascia|-
Iliopectineal arch|Arcade iliopectinée|bandelette iliopectinée|annex/ftrunk|fascia|-
Inferior extensor retinaculum of ankle|Rétinaculum inférieur des extenseurs de la cheville|ligament frondiforme|annex/fll|fascia|-
Inferior fibular retinaculum|Rétinaculum inférieur des fibulaires|rétinaculum inférieur des péroniers|annex/fll|fascia|-
Lateral femoral intermuscular septum|Septum intermusculaire latéral de la cuisse||annex/fll|fascia|-
Medial femoral intermuscular septum|Septum intermusculaire médial de la cuisse||annex/fll|fascia|-
Piriformis fascia|Fascia du muscle piriforme||annex/fll|fascia|-
Plantar aponeurosis|Aponévrose plantaire||annex/fll|tendon|plantar_aponeurosis
Popliteal fascia|Fascia poplité||annex/fll|fascia|-
Posterior intermuscular septum of leg|Septum intermusculaire postérieur de la jambe||annex/fll|fascia|-
Superficial transverse metatarsal ligament|Ligament métatarsien transverse superficiel||annex/fll|tendon|-
Superior extensor retinaculum of ankle|Rétinaculum supérieur des extenseurs de la cheville|ligament annulaire antérieur|annex/fll|fascia|-
Superior fibular retinaculum|Rétinaculum supérieur des fibulaires|rétinaculum supérieur des péroniers|annex/fll|fascia|-
Transverse intermuscular septum of leg|Septum intermusculaire transverse de la jambe||annex/fll|fascia|-
Clavipectoral fascia|Fascia clavipectoral|aponévrose clavipectorale|annex/ftrunk|fascia|-
Pectoral fascia|Fascia pectoral||annex/ftrunk|fascia|-
Antebrachial fascia|Fascia antébrachial|aponévrose antébrachiale|annex/ful|fascia|-
Extensor retinaculum of wrist|Rétinaculum des extenseurs du poignet|ligament annulaire postérieur du carpe|annex/ful|fascia|-
Brachial fascia|Fascia brachial|aponévrose brachiale|annex/ful|fascia|-
Deltoid fascia|Fascia deltoïdien||annex/ful|fascia|-
Dorsal fascia of hand|Fascia dorsal de la main||annex/ful|fascia|-
Flexor retinaculum of wrist|Rétinaculum des fléchisseurs du poignet|ligament annulaire antérieur du carpe|annex/ful|fascia|flexor_retinaculum_wrist
Lateral intermuscular septum of arm|Septum intermusculaire latéral du bras||annex/ful|fascia|-
Medial intermuscular septum of arm|Septum intermusculaire médial du bras||annex/ful|fascia|-
Palmar aponeurosis|Aponévrose palmaire|aponévrose palmaire moyenne|annex/ful|tendon|palmar_aponeurosis
Superficial transverse metacarpal ligament|Ligament métacarpien transverse superficiel||annex/ful|tendon|-
Anterior layer of thoracolumbar fascia|Lame antérieure du fascia thoracolombaire||annex/ftrunk|fascia|-
Middle layer of thoracolumbar fascia|Lame moyenne du fascia thoracolombaire||annex/ftrunk|fascia|-
Posterior layer of thoracolumbar fascia|Lame postérieure du fascia thoracolombaire|aponévrose lombaire|annex/ftrunk|fascia|-
External abdominal oblique muscle|Muscle oblique externe de l'abdomen|grand oblique|trunk/abdomen|muscle|
Inguinal ligament|Ligament inguinal|arcade crurale|trunk/abdomen|tendon|
Internal abdominal oblique muscle|Muscle oblique interne de l'abdomen|petit oblique|trunk/abdomen|muscle|
Linea alba|Ligne blanche||trunk/abdomen|tendon|
Pyramidalis muscle|Muscle pyramidal de l'abdomen||trunk/abdomen|muscle|
Quadratus lumborum muscle|Muscle carré des lombes||trunk/abdomen|muscle|
Rectus abdominis muscle|Muscle droit de l'abdomen|grand droit|trunk/abdomen|muscle|
Transversus abdominis muscle|Muscle transverse de l'abdomen||trunk/abdomen|muscle|
Omohyoid muscle|Muscle omohyoïdien||neck/infrahy|muscle|
Sternohyoid muscle|Muscle sternohyoïdien|sterno-cléido-hyoïdien|neck/infrahy|muscle|
Sternothyroid muscle|Muscle sternothyroïdien||neck/infrahy|muscle|
Thyrohyoid muscle|Muscle thyrohyoïdien||neck/infrahy|muscle|
Ary-epiglottic part of oblique arytenoid muscle|Partie ary-épiglottique du muscle aryténoïdien oblique||neck/pharynx|muscle|arytenoid
External part of thyro-arytenoid muscle|Partie externe du muscle thyro-aryténoïdien||neck/pharynx|muscle|thyroarytenoid
Lateral crico-arytenoid muscle|Muscle crico-aryténoïdien latéral||neck/pharynx|muscle|
Oblique part of cricothyroid muscle|Partie oblique du muscle cricothyroïdien||neck/pharynx|muscle|cricothyroid
Posterior crico-arytenoid muscle|Muscle crico-aryténoïdien postérieur||neck/pharynx|muscle|
Straight part of cricothyroid muscle|Partie droite du muscle cricothyroïdien||neck/pharynx|muscle|cricothyroid
Thyro-epiglottic part of thyro-arytenoid muscle|Partie thyro-épiglottique du muscle thyro-aryténoïdien||neck/pharynx|muscle|thyroarytenoid
Transverse arytenoid muscle|Muscle aryténoïdien transverse||neck/pharynx|muscle|arytenoid
Longus capitis muscle|Muscle long de la tête|grand droit antérieur de la tête|neck/neckm|muscle|
Longus colli muscle|Muscle long du cou||neck/neckm|muscle|
Inferior pharyngeal constrictor|Muscle constricteur inférieur du pharynx||neck/pharynx|muscle|
Middle pharyngeal constrictor|Muscle constricteur moyen du pharynx||neck/pharynx|muscle|
Stylopharyngeus muscle|Muscle stylopharyngien||neck/pharynx|muscle|
Superior pharyngeal constrictor|Muscle constricteur supérieur du pharynx||neck/pharynx|muscle|
Platysma|Muscle platysma|peaucier du cou|neck/neckm|muscle|
Rectus anterior capitis muscle|Muscle droit antérieur de la tête|petit droit antérieur de la tête|neck/neckm|muscle|
Rectus lateralis capitis muscle|Muscle droit latéral de la tête||neck/neckm|muscle|
Scalenus anterior muscle|Muscle scalène antérieur||neck/neckm|muscle|
Scalenus medius muscle|Muscle scalène moyen||neck/neckm|muscle|
Scalenus posterior muscle|Muscle scalène postérieur||neck/neckm|muscle|
Sternocleidomastoid muscle|Muscle sternocléidomastoïdien|SCM|neck/neckm|muscle|
Anterior belly of digastric muscle|Ventre antérieur du muscle digastrique||neck/suprahy|muscle|digastric
Intermediate tendon of digastric muscle|Tendon intermédiaire du muscle digastrique||neck/suprahy|tendon|digastric
Posterior belly of digastric muscle|Ventre postérieur du muscle digastrique||neck/suprahy|muscle|digastric
Geniohyoid muscle|Muscle géniohyoïdien||neck/suprahy|muscle|
Mylohyoid muscle|Muscle mylohyoïdien||neck/suprahy|muscle|
Stylohyoid muscle|Muscle stylohyoïdien||neck/suprahy|muscle|
Common tendinous ring|Anneau tendineux commun|tendon de Zinn|head/eye|tendon|-
Inferior oblique muscle|Muscle oblique inférieur de l'œil|petit oblique de l'œil|head/eye|muscle|
Inferior rectus muscle|Muscle droit inférieur de l'œil||head/eye|muscle|
Inferior tarsus|Tarse inférieur||head/eye|tendon|-
Lateral rectus muscle|Muscle droit latéral de l'œil|droit externe|head/eye|muscle|
Levator palpebrae superioris|Muscle releveur de la paupière supérieure||head/eye|muscle|
Medial rectus muscle|Muscle droit médial de l'œil|droit interne|head/eye|muscle|
Superior oblique muscle|Muscle oblique supérieur de l'œil|grand oblique de l'œil|head/eye|muscle|
Superior rectus muscle|Muscle droit supérieur de l'œil||head/eye|muscle|
Superior tarsus|Tarse supérieur||head/eye|tendon|-
Trochlea of superior oblique muscle|Trochlée du muscle oblique supérieur|poulie du grand oblique|head/eye|tendon|-
Deep part of masseter|Partie profonde du muscle masséter||head/mastic|muscle|masseter
Inferior head of lateral pterygoid muscle|Chef inférieur du muscle ptérygoïdien latéral|ptérygoïdien externe|head/mastic|muscle|lateral_pterygoid
Medial pterygoid muscle|Muscle ptérygoïdien médial|ptérygoïdien interne|head/mastic|muscle|
Superficial part of masseter|Partie superficielle du muscle masséter||head/mastic|muscle|masseter
Superior head of lateral pterygoid muscle|Chef supérieur du muscle ptérygoïdien latéral|ptérygoïdien externe|head/mastic|muscle|lateral_pterygoid
Temporalis muscle|Muscle temporal||head/mastic|muscle|
Palatopharyngeus muscle|Muscle palatopharyngien|pharyngo-staphylin|neck/pharynx|muscle|
Genioglossus muscle|Muscle génioglosse||head/tongue|muscle|
Hyoglossus muscle|Muscle hyoglosse||head/tongue|muscle|
Epicranial aponeurosis|Aponévrose épicrânienne|galéa aponévrotique|head/face|tendon|epicranius
Frontalis muscle|Ventre frontal du muscle occipitofrontal|muscle frontal|head/face|muscle|epicranius
Occipitalis muscle|Ventre occipital du muscle occipitofrontal|muscle occipital|head/face|muscle|epicranius
Temporoparietalis muscle|Muscle temporopariétal||head/face|muscle|
Bucinator|Muscle buccinateur||head/face|muscle|
Corrugator supercilii|Muscle corrugateur du sourcil|sourcilier|head/face|muscle|
Depressor anguli oris|Muscle abaisseur de l'angle de la bouche|triangulaire des lèvres|head/face|muscle|
Depressor labii inferioris|Muscle abaisseur de la lèvre inférieure|carré du menton|head/face|muscle|
Depressor septi nasi|Muscle abaisseur du septum nasal|myrtiforme|head/face|muscle|
Levator anguli oris|Muscle élévateur de l'angle de la bouche|canin|head/face|muscle|
Levator labii superioris|Muscle élévateur de la lèvre supérieure||head/face|muscle|
Levator nasolabialis|Muscle élévateur de la lèvre supérieure et de l'aile du nez||head/face|muscle|
Mentalis muscle|Muscle mentonnier|muscle de la houppe du menton|head/face|muscle|
Nasalis muscle|Muscle nasal|transverse du nez|head/face|muscle|
Orbicularis oris muscle|Muscle orbiculaire de la bouche|orbiculaire des lèvres|head/face|muscle|
Orbital part of orbicularis oculi|Partie orbitaire du muscle orbiculaire de l'œil||head/face|muscle|orbicularis_oculi
Palpebral part of orbicularis oculi|Partie palpébrale du muscle orbiculaire de l'œil||head/face|muscle|orbicularis_oculi
Procerus muscle|Muscle procérus|pyramidal du nez|head/face|muscle|
Risorius muscle|Muscle risorius||head/face|muscle|
Zygomaticus major muscle|Muscle grand zygomatique||head/face|muscle|
Zygomaticus minor muscle|Muscle petit zygomatique||head/face|muscle|
Iliocostalis colli muscle|Muscle iliocostal du cou|ilio-costal cervical|back/backdeep|muscle|erector_spinae
Iliocostalis lumborum muscle|Muscle iliocostal des lombes||back/backdeep|muscle|erector_spinae
Iliocostalis thoracis muscle|Muscle iliocostal du thorax||back/backdeep|muscle|erector_spinae
Longissimus capitis muscle|Muscle longissimus de la tête|petit complexus|back/backdeep|muscle|erector_spinae
Longissimus colli muscle|Muscle longissimus du cou|transversaire du cou|back/backdeep|muscle|erector_spinae
Longissimus thoracis muscle|Muscle longissimus du thorax|long dorsal|back/backdeep|muscle|erector_spinae
Spinalis capitis muscle|Muscle épineux de la tête||back/backdeep|muscle|erector_spinae
Spinalis colli muscle|Muscle épineux du cou||back/backdeep|muscle|erector_spinae
Spinalis thoracis muscle|Muscle épineux du thorax|épi-épineux|back/backdeep|muscle|erector_spinae
Interspinales colli muscles|Muscles interépineux du cou||back/backdeep|muscle|interspinales
Interspinales lumborum muscles|Muscles interépineux des lombes||back/backdeep|muscle|interspinales
Interspinales thoracis muscles|Muscles interépineux du thorax||back/backdeep|muscle|interspinales
Splenius capitis muscle|Muscle splénius de la tête||back/backmid|muscle|splenius
Splenius colli muscle|Muscle splénius du cou||back/backmid|muscle|splenius
Obliquus inferior capitis muscle|Muscle oblique inférieur de la tête|grand oblique de la tête|back/subocc|muscle|
Obliquus superior capitis muscle|Muscle oblique supérieur de la tête|petit oblique de la tête|back/subocc|muscle|
Rectus posterior major capitis muscle|Muscle grand droit postérieur de la tête||back/subocc|muscle|
Rectus posterior minor capitis muscle|Muscle petit droit postérieur de la tête||back/subocc|muscle|
Multifidus colli muscle|Muscle multifide du cou||back/backdeep|muscle|transversospinales
Multifidus lumborum muscle|Muscle multifide des lombes||back/backdeep|muscle|transversospinales
Multifidus thoracis muscle|Muscle multifide du thorax||back/backdeep|muscle|transversospinales
Rotatores|Muscles rotateurs||back/backdeep|muscle|transversospinales
Semispinalis colli muscle|Muscle semi-épineux du cou||back/backdeep|muscle|transversospinales
Semispinalis thoracis muscle|Muscle semi-épineux du thorax||back/backdeep|muscle|transversospinales
Dorsal parts of lateral intertransversarii lumborum muscles|Parties dorsales des muscles intertransversaires latéraux des lombes||back/backdeep|muscle|intertransversarii
Latissimus dorsi muscle|Muscle grand dorsal||back/backsup|muscle|
Levator scapulae|Muscle élévateur de la scapula|angulaire de l'omoplate|back/backsup|muscle|
Rhomboid major muscle|Muscle grand rhomboïde||back/backsup|muscle|rhomboid
Rhomboid minor muscle|Muscle petit rhomboïde||back/backsup|muscle|rhomboid
Serratus posterior inferior muscle|Muscle dentelé postérieur et inférieur|petit dentelé postérieur et inférieur|back/backmid|muscle|
Serratus posterior superior muscle|Muscle dentelé postérieur et supérieur|petit dentelé postérieur et supérieur|back/backmid|muscle|
Ascending part of trapezius muscle|Partie ascendante du muscle trapèze|faisceau inférieur|back/backsup|muscle|trapezius
Descending part of trapezius muscle|Partie descendante du muscle trapèze|faisceau supérieur|back/backsup|muscle|trapezius
Transverse part of trapezius muscle|Partie transverse du muscle trapèze|faisceau moyen|back/backsup|muscle|trapezius
Ventral parts of lateral intertransversarii lumborum muscles|Parties ventrales des muscles intertransversaires latéraux des lombes||back/backdeep|muscle|intertransversarii
(Iliopectineal bursa)|Bourse iliopectinée||annex/fll|bourse|-
Anserine bursa|Bourse ansérine|bourse de la patte d'oie|annex/fll|bourse|-
Bursa of piriformis muscle|Bourse du muscle piriforme||annex/fll|bourse|-
Deep infrapatellar bursa|Bourse infrapatellaire profonde||annex/fll|bourse|-
Inferior subtendinous bursa of biceps femoris muscle|Bourse subtendineuse inférieure du muscle biceps fémoral||annex/fll|bourse|-
Intermuscular gluteal bursae|Bourses intermusculaires glutéales||annex/fll|bourse|-
Lateral subtendinous bursa of gastrocnemius muscle|Bourse subtendineuse latérale du muscle gastrocnémien||annex/fll|bourse|-
Medial subtendinous bursa of gastrocnemius muscle|Bourse subtendineuse médiale du muscle gastrocnémien||annex/fll|bourse|-
Sciatic bursa of gluteus maximus muscle|Bourse ischiatique du muscle grand fessier||annex/fll|bourse|-
Sciatic bursa of obturator internus|Bourse ischiatique du muscle obturateur interne||annex/fll|bourse|-
Semimembranosus bursa|Bourse du muscle semi-membraneux||annex/fll|bourse|-
Subcutaneous bursa of lateral malleolus|Bourse subcutanée de la malléole latérale||annex/fll|bourse|-
Subcutaneous bursa of medial malleolus|Bourse subcutanée de la malléole médiale||annex/fll|bourse|-
Subcutaneous bursa of tuberosity of tibia|Bourse subcutanée de la tubérosité tibiale||annex/fll|bourse|-
Subcutaneous calcaneal bursa|Bourse subcutanée calcanéenne||annex/fll|bourse|-
Subcutaneous infrapatellar bursa|Bourse subcutanée infrapatellaire||annex/fll|bourse|-
Subcutaneous prepatellar bursa|Bourse subcutanée prépatellaire||annex/fll|bourse|-
Subcutaneous trochanteric bursa|Bourse subcutanée trochantérique||annex/fll|bourse|-
Subfacial prepatellar bursa|Bourse subfasciale prépatellaire||annex/fll|bourse|-
Subtendinous bursa of iliacus muscle|Bourse subtendineuse du muscle iliaque||annex/fll|bourse|-
Subtendinous bursa of obturator internus|Bourse subtendineuse du muscle obturateur interne||annex/fll|bourse|-
Subtendinous bursa of sartorius muscle|Bourse subtendineuse du muscle sartorius||annex/fll|bourse|-
Subtendinous bursa of tibialis anterior|Bourse subtendineuse du muscle tibial antérieur||annex/fll|bourse|-
Subtendinous calcaneal bursa|Bourse subtendineuse calcanéenne|bourse rétrocalcanéenne|annex/fll|bourse|-
Subtendinous prepatellar bursa|Bourse subtendineuse prépatellaire||annex/fll|bourse|-
Superior bursa of biceps femoris muscle|Bourse supérieure du muscle biceps fémoral||annex/fll|bourse|-
Suprapatellar bursa|Bourse suprapatellaire|cul-de-sac sous-quadricipital|annex/fll|bourse|-
Trochanteric bursa of gluteus maximus muscle|Bourse trochantérique du muscle grand fessier||annex/fll|bourse|-
Trochanteric bursa of gluteus medius muscle|Bourse trochantérique du muscle moyen fessier||annex/fll|bourse|-
Trochanteric bursa of gluteus minimus muscle|Bourse trochantérique du muscle petit fessier||annex/fll|bourse|-
Extensor digitorum longus|Muscle long extenseur des orteils|extenseur commun des orteils|ll/legant|muscle|
Tendon of extensor digitorum longus|Tendons du muscle long extenseur des orteils||ll/legant|tendon|extensor_digitorum_longus
Extensor hallucis longus|Muscle long extenseur de l'hallux|extenseur propre du gros orteil|ll/legant|muscle|
Fibularis tertius muscle|Muscle troisième fibulaire|péronier antérieur|ll/legant|muscle|
Tibialis anterior muscle|Muscle tibial antérieur|jambier antérieur|ll/legant|muscle|
Lateral patellar retinaculum|Rétinaculum patellaire latéral|aileron rotulien externe|ll/thant|fascia|-
Medial patellar retinaculum|Rétinaculum patellaire médial|aileron rotulien interne|ll/thant|fascia|-
Rectus femoris muscle|Muscle droit fémoral|droit antérieur de la cuisse|ll/thant|muscle|
Sartorius muscle|Muscle sartorius|couturier|ll/thant|muscle|
Vastus intermedius muscle|Muscle vaste intermédiaire|crural|ll/thant|muscle|
Vastus lateralis muscle|Muscle vaste latéral|vaste externe|ll/thant|muscle|
Vastus medialis muscle|Muscle vaste médial|vaste interne|ll/thant|muscle|
Inferior gemellus muscle|Muscle jumeau inférieur||ll/glut|muscle|
Obturator internus|Muscle obturateur interne||ll/glut|muscle|
Piriformis muscle|Muscle piriforme|pyramidal du bassin|ll/glut|muscle|
Quadratus femoris muscle|Muscle carré fémoral|carré crural|ll/glut|muscle|
Superior gemellus muscle|Muscle jumeau supérieur||ll/glut|muscle|
Iliacus muscle|Muscle iliaque||ll/thant|muscle|
Psoas major|Muscle grand psoas||ll/thant|muscle|
Fibularis brevis muscle|Muscle court fibulaire|court péronier latéral|ll/leglat|muscle|
Fibularis longus muscle|Muscle long fibulaire|long péronier latéral|ll/leglat|muscle|
Adductor brevis|Muscle court adducteur|petit adducteur|ll/thmed|muscle|
Adductor longus|Muscle long adducteur|moyen adducteur|ll/thmed|muscle|
Adductor magnus|Muscle grand adducteur||ll/thmed|muscle|
(Adductor minimus)|Muscle adducteur minime|faisceau supérieur du grand adducteur|ll/thmed|muscle|
Gracilis muscle|Muscle gracile|droit interne|ll/thmed|muscle|
Obturator externus|Muscle obturateur externe||ll/thmed|muscle|
Pectineus muscle|Muscle pectiné||ll/thmed|muscle|
(Opponens digiti minimi muscle of foot)|Muscle opposant du petit orteil||ll/foot|muscle|
Abductor digiti minimi of foot|Muscle abducteur du petit orteil|abducteur du 5e orteil|ll/foot|muscle|
Abductor hallucis|Muscle abducteur de l'hallux||ll/foot|muscle|
Oblique head of adductor hallucis|Chef oblique du muscle adducteur de l'hallux||ll/foot|muscle|adductor_hallucis
Transverse head of adductor hallucis|Chef transverse du muscle adducteur de l'hallux||ll/foot|muscle|adductor_hallucis
Dorsal interossei muscles of foot|Muscles interosseux dorsaux du pied||ll/foot|muscle|
Extensor digitorum brevis|Muscle court extenseur des orteils|pédieux|ll/foot|muscle|
Extensor hallucis brevis|Muscle court extenseur de l'hallux|faisceau interne du pédieux|ll/foot|muscle|
Flexor digiti minimi of foot|Muscle court fléchisseur du petit orteil||ll/foot|muscle|
Flexor digitorum brevis|Muscle court fléchisseur des orteils|court fléchisseur plantaire|ll/foot|muscle|
Lateral head of flexor hallucis brevis|Chef latéral du muscle court fléchisseur de l'hallux||ll/foot|muscle|flexor_hallucis_brevis
Medial head of flexor hallucis brevis|Chef médial du muscle court fléchisseur de l'hallux||ll/foot|muscle|flexor_hallucis_brevis
Lumbrical muscles of foot|Muscles lombricaux du pied||ll/foot|muscle|
Plantar interossei muscles|Muscles interosseux plantaires||ll/foot|muscle|
Quadratus plantae muscle|Muscle carré plantaire|chair carrée de Sylvius|ll/foot|muscle|
Flexor digitorum longus|Muscle long fléchisseur des orteils|fléchisseur commun des orteils|ll/legpost|muscle|
Flexor hallucis longus|Muscle long fléchisseur de l'hallux|fléchisseur propre du gros orteil|ll/legpost|muscle|
Popliteus muscle|Muscle poplité||ll/legpost|muscle|
Tibialis posterior muscle|Muscle tibial postérieur|jambier postérieur|ll/legpost|muscle|
Calcaneal tendon|Tendon calcanéen|tendon d'Achille|ll/legpost|tendon|
Lateral head of gastrocnemius|Chef latéral du muscle gastrocnémien|jumeau externe|ll/legpost|muscle|gastrocnemius
Medial head of gastrocnemius|Chef médial du muscle gastrocnémien|jumeau interne|ll/legpost|muscle|gastrocnemius
Plantaris muscle|Muscle plantaire|plantaire grêle|ll/legpost|muscle|
Soleus muscle|Muscle soléaire||ll/legpost|muscle|
Long head of biceps femoris|Chef long du muscle biceps fémoral||ll/thpost|muscle|biceps_femoris
Semimembranosus muscle|Muscle semi-membraneux|demi-membraneux|ll/thpost|muscle|
Semitendinosus muscle|Muscle semi-tendineux|demi-tendineux|ll/thpost|muscle|
Short head of biceps femoris|Chef court du muscle biceps fémoral||ll/thpost|muscle|biceps_femoris
Gluteus maximus muscle|Muscle grand fessier||ll/glut|muscle|
Gluteus medius muscle|Muscle moyen fessier||ll/glut|muscle|
Gluteus minimus muscle|Muscle petit fessier||ll/glut|muscle|
Tensor fasciae latae|Muscle tenseur du fascia lata||ll/glut|muscle|
Iliotibial tract|Tractus iliotibial|bandelette de Maissiat|ll/thant|tendon|
Tendon sheath of extensor digitorum longus|Gaine tendineuse du muscle long extenseur des orteils||annex/fll|gaine|-
Tendon sheath of tibialis anterior|Gaine tendineuse du muscle tibial antérieur||annex/fll|gaine|-
Common tendon sheath of fibularis muscles|Gaine tendineuse commune des muscles fibulaires||annex/fll|gaine|-
Plantar tendon sheath of fibularis longus muscle|Gaine tendineuse plantaire du muscle long fibulaire||annex/fll|gaine|-
Tendon sheath of flexor digitorum longus|Gaine tendineuse du muscle long fléchisseur des orteils||annex/fll|gaine|-
Tendon sheath of flexor hallucis longus|Gaine tendineuse du muscle long fléchisseur de l'hallux||annex/fll|gaine|-
Tendon sheath of tibialis posterior muscle|Gaine tendineuse du muscle tibial postérieur||annex/fll|gaine|-
Bicipitoradial bursa|Bourse bicipitoradiale||annex/ful|bourse|-
Coracobrachial bursa|Bourse du muscle coracobrachial||annex/ful|bourse|-
Subacromial bursa|Bourse subacromiale|bourse sous-acromiale|annex/ful|bourse|-
Subcutaneous acromial bursa|Bourse subcutanée acromiale||annex/ful|bourse|-
Subdeltoid bursa|Bourse subdeltoïdienne|bourse sous-deltoïdienne|annex/ful|bourse|-
Subtendinous bursa of infraspinatus muscle|Bourse subtendineuse du muscle infra-épineux||annex/ful|bourse|-
Subtendinous bursa of teres major muscle|Bourse subtendineuse du muscle grand rond||annex/ful|bourse|-
Subtendinous bursa of trapezius muscle|Bourse subtendineuse du muscle trapèze||annex/ful|bourse|-
Subtendinous bursa of triceps brachii muscle|Bourse subtendineuse du muscle triceps brachial||annex/ful|bourse|-
Long head of biceps brachii|Chef long du muscle biceps brachial||ul/armc|muscle|biceps_brachii
Short head of biceps brachii|Chef court du muscle biceps brachial||ul/armc|muscle|biceps_brachii
Brachialis muscle|Muscle brachial|brachial antérieur|ul/armc|muscle|
Coracobrachialis muscle|Muscle coracobrachial||ul/armc|muscle|
Flexor digitorum profundus|Muscle fléchisseur profond des doigts|fléchisseur commun profond des doigts|ul/fant|muscle|
Flexor pollicis longus|Muscle long fléchisseur du pouce|fléchisseur propre du pouce|ul/fant|muscle|
Pronator quadratus|Muscle carré pronateur||ul/fant|muscle|
Deep head of pronator teres|Chef ulnaire du muscle rond pronateur|chef profond|ul/fant|muscle|pronator_teres
Flexor carpi radialis|Muscle fléchisseur radial du carpe|grand palmaire|ul/fant|muscle|
Humeral head of flexor carpi ulnaris|Chef huméral du muscle fléchisseur ulnaire du carpe|cubital antérieur|ul/fant|muscle|flexor_carpi_ulnaris
Humero-ulnar head of flexor digitorum superficialis|Chef huméro-ulnaire du muscle fléchisseur superficiel des doigts|fléchisseur commun superficiel|ul/fant|muscle|flexor_digitorum_superficialis
Palmaris longus muscle|Muscle long palmaire|petit palmaire|ul/fant|muscle|
Radial head of flexor digitorum superficialis|Chef radial du muscle fléchisseur superficiel des doigts|fléchisseur commun superficiel|ul/fant|muscle|flexor_digitorum_superficialis
Superficial head of pronator teres|Chef huméral du muscle rond pronateur|chef superficiel|ul/fant|muscle|pronator_teres
Ulnar head of flexor carpi ulnaris|Chef ulnaire du muscle fléchisseur ulnaire du carpe|cubital antérieur|ul/fant|muscle|flexor_carpi_ulnaris
Abductor digiti minimi of hand|Muscle abducteur du petit doigt|abducteur du 5e doigt|ul/hand|muscle|
Abductor pollicis brevis|Muscle court abducteur du pouce||ul/hand|muscle|
Deep head of flexor pollicis brevis|Chef profond du muscle court fléchisseur du pouce||ul/hand|muscle|flexor_pollicis_brevis
Dorsal interossei muscles of hand|Muscles interosseux dorsaux de la main||ul/hand|muscle|
Flexor digiti minimi of hand|Muscle court fléchisseur du petit doigt||ul/hand|muscle|
Lumbrical muscles of hand|Muscles lombricaux de la main||ul/hand|muscle|
Oblique head of adductor pollicis|Chef oblique du muscle adducteur du pouce||ul/hand|muscle|adductor_pollicis
Opponens digiti minimi muscle of hand|Muscle opposant du petit doigt||ul/hand|muscle|
Opponens pollicis muscle|Muscle opposant du pouce||ul/hand|muscle|
Palmar interossei muscles|Muscles interosseux palmaires||ul/hand|muscle|
Superficial head of flexor pollicis brevis|Chef superficiel du muscle court fléchisseur du pouce||ul/hand|muscle|flexor_pollicis_brevis
Transverse head of adductor pollicis|Chef transverse du muscle adducteur du pouce||ul/hand|muscle|adductor_pollicis
Lateral head of triceps brachii|Chef latéral du muscle triceps brachial|vaste externe du triceps|ul/armc|muscle|triceps_brachii
Long head of triceps brachii|Chef long du muscle triceps brachial||ul/armc|muscle|triceps_brachii
Medial head of triceps brachii|Chef médial du muscle triceps brachial|vaste interne du triceps|ul/armc|muscle|triceps_brachii
Abductor pollicis longus|Muscle long abducteur du pouce||ul/fpost|muscle|
Extensor indicis|Muscle extenseur de l'index|extenseur propre de l'index|ul/fpost|muscle|
Extensor pollicis brevis|Muscle court extenseur du pouce||ul/fpost|muscle|
Extensor pollicis longus|Muscle long extenseur du pouce||ul/fpost|muscle|
Supinator|Muscle supinateur|court supinateur|ul/fpost|muscle|
Anconeus muscle|Muscle anconé||ul/fpost|muscle|
Brachioradialis muscle|Muscle brachioradial|long supinateur|ul/fpost|muscle|
Extensor carpi radialis brevis|Muscle court extenseur radial du carpe|2e radial|ul/fpost|muscle|
Extensor carpi radialis longus|Muscle long extenseur radial du carpe|1er radial|ul/fpost|muscle|
Extensor digiti minimi|Muscle extenseur du petit doigt|extenseur propre du 5e doigt|ul/fpost|muscle|
Extensor digitorum|Muscle extenseur des doigts|extenseur commun des doigts|ul/fpost|muscle|
Humeral head of extensor carpi ulnaris|Chef huméral du muscle extenseur ulnaire du carpe|cubital postérieur|ul/fpost|muscle|extensor_carpi_ulnaris
Ulnar head of extensor carpi ulnaris|Chef ulnaire du muscle extenseur ulnaire du carpe|cubital postérieur|ul/fpost|muscle|extensor_carpi_ulnaris
Acromial part of deltoid muscle|Partie acromiale du muscle deltoïde|faisceau moyen|ul/shoulder|muscle|deltoid
Clavicular part of deltoid muscle|Partie claviculaire du muscle deltoïde|faisceau antérieur|ul/shoulder|muscle|deltoid
Scapular spinal part of deltoid muscle|Partie spinale du muscle deltoïde|faisceau postérieur|ul/shoulder|muscle|deltoid
Infraspinatus muscle|Muscle infra-épineux|sous-épineux|ul/shoulder|muscle|
Subscapularis muscle|Muscle subscapulaire|sous-scapulaire|ul/shoulder|muscle|
Supraspinatus muscle|Muscle supra-épineux|sus-épineux|ul/shoulder|muscle|
Teres minor muscle|Muscle petit rond||ul/shoulder|muscle|
Teres major muscle|Muscle grand rond||ul/shoulder|muscle|
Tendon sheath - abd. pollicis longus - ext. pollicis brevis|Gaine tendineuse des muscles long abducteur et court extenseur du pouce||annex/ful|gaine|-
Tendon sheath of extensor digitorum and extensor indicis|Gaine tendineuse des muscles extenseur des doigts et extenseur de l'index||annex/ful|gaine|-
Tendon sheath of extensors carpi radialis|Gaine tendineuse des muscles extenseurs radiaux du carpe||annex/ful|gaine|-
Common flexor tendon sheath|Gaine commune des tendons fléchisseurs|gaine digito-carpienne ulnaire|annex/ful|gaine|-
Cruciform part of fibrous sheath of digit of hand|Partie cruciforme des gaines fibreuses des doigts||annex/ful|gaine|-
Synovial sheaths of digits of hand|Gaines synoviales des doigts||annex/ful|gaine|-
Coccygeus muscle|Muscle coccygien|ischio-coccygien|trunk/pelvis|muscle|
Iliococcygeus muscle|Muscle ilio-coccygien||trunk/pelvis|muscle|levator_ani
Pubo-analis muscle|Muscle pubo-anal||trunk/pelvis|muscle|levator_ani
Pubococcygeus muscle|Muscle pubo-coccygien||trunk/pelvis|muscle|levator_ani
Tendinous arch of levator ani|Arc tendineux du muscle élévateur de l'anus||trunk/pelvis|tendon|-
External anal sphincter|Muscle sphincter externe de l'anus||trunk/pelvis|muscle|
Diaphragm|Diaphragme||trunk/thorax|muscle|
External intercostal muscles|Muscles intercostaux externes||trunk/thorax|muscle|
Innermost intercostal muscles|Muscles intercostaux intimes||trunk/thorax|muscle|
Internal intercostal muscles|Muscles intercostaux internes||trunk/thorax|muscle|
Levatores breves costarum|Muscles élévateurs courts des côtes|surcostaux courts|trunk/thorax|muscle|levatores_costarum
Levatores longi costarum|Muscles élévateurs longs des côtes|surcostaux longs|trunk/thorax|muscle|levatores_costarum
(Abdominal part of pectoralis major muscle)|Partie abdominale du muscle grand pectoral||trunk/thorax|muscle|pectoralis_major
Clavicular head of pectoralis major muscle|Partie claviculaire du muscle grand pectoral||trunk/thorax|muscle|pectoralis_major
Sternocostal head of pectoralis major muscle|Partie sternocostale du muscle grand pectoral||trunk/thorax|muscle|pectoralis_major
Pectoralis minor muscle|Muscle petit pectoral||trunk/thorax|muscle|
Serratus anterior muscle|Muscle dentelé antérieur|grand dentelé|trunk/thorax|muscle|
Subclavius muscle|Muscle subclavier|sous-clavier|trunk/thorax|muscle|
Transversus thoracis muscle|Muscle transverse du thorax|triangulaire du sternum|trunk/thorax|muscle|
"""

# Noms des groupes qui fusionnent plusieurs pièces (les groupes d'une seule pièce prennent le nom de la pièce).
GROUPS = {
    'arytenoid': ('Muscles aryténoïdiens', 'Muscles aryténoïdiens transverse et oblique'),
    'thyroarytenoid': ('Muscle thyro-aryténoïdien', 'Muscle thyro-aryténoïdien'),
    'cricothyroid': ('Muscle cricothyroïdien', 'Muscle cricothyroïdien'),
    'digastric': ('Muscle digastrique', 'Muscle digastrique'),
    'masseter': ('Muscle masséter', 'Muscle masséter'),
    'lateral_pterygoid': ('Muscle ptérygoïdien latéral (ptérygoïdien externe)', 'Muscle ptérygoïdien latéral'),
    'epicranius': ('Muscle épicrânien (occipitofrontal et aponévrose)', 'Muscle épicrânien'),
    'orbicularis_oculi': ('Muscle orbiculaire de l’œil', 'Muscle orbiculaire de l’œil'),
    'erector_spinae': ('Muscle érecteur du rachis (iliocostal, longissimus, épineux)', 'Muscle érecteur du rachis'),
    'interspinales': ('Muscles interépineux', 'Muscles interépineux'),
    'splenius': ('Muscle splénius (de la tête et du cou)', 'Muscle splénius'),
    'transversospinales': ('Muscles transversaires épineux (multifide, rotateurs, semi-épineux)', 'Muscles transversaires épineux'),
    'intertransversarii': ('Muscles intertransversaires des lombes', 'Muscles intertransversaires des lombes'),
    'rhomboid': ('Muscles rhomboïdes', 'Muscles rhomboïdes'),
    'trapezius': ('Muscle trapèze', 'Muscle trapèze'),
    'extensor_digitorum_longus': (None, None),   # le tendon rejoint le groupe du muscle
    'adductor_hallucis': ('Muscle adducteur de l’hallux', 'Muscle adducteur de l’hallux'),
    'flexor_hallucis_brevis': ('Muscle court fléchisseur de l’hallux', 'Muscle court fléchisseur de l’hallux'),
    'gastrocnemius': ('Muscle gastrocnémien (jumeaux)', 'Muscle gastrocnémien'),
    'biceps_femoris': ('Muscle biceps fémoral', 'Muscle biceps fémoral'),
    'biceps_brachii': ('Muscle biceps brachial', 'Muscle biceps brachial'),
    'pronator_teres': ('Muscle rond pronateur', 'Muscle rond pronateur'),
    'flexor_carpi_ulnaris': ('Muscle fléchisseur ulnaire du carpe (cubital antérieur)', 'Muscle fléchisseur ulnaire du carpe'),
    'flexor_digitorum_superficialis': ('Muscle fléchisseur superficiel des doigts', 'Muscle fléchisseur superficiel des doigts'),
    'flexor_pollicis_brevis': ('Muscle court fléchisseur du pouce', 'Muscle court fléchisseur du pouce'),
    'adductor_pollicis': ('Muscle adducteur du pouce', 'Muscle adducteur du pouce'),
    'triceps_brachii': ('Muscle triceps brachial', 'Muscle triceps brachial'),
    'extensor_carpi_ulnaris': ('Muscle extenseur ulnaire du carpe (cubital postérieur)', 'Muscle extenseur ulnaire du carpe'),
    'deltoid': ('Muscle deltoïde', 'Muscle deltoïde'),
    'levator_ani': ('Muscle élévateur de l’anus', 'Muscle élévateur de l’anus'),
    'levatores_costarum': ('Muscles élévateurs des côtes', 'Muscles élévateurs des côtes'),
    'pectoralis_major': ('Muscle grand pectoral', 'Muscle grand pectoral'),
}

REGIONS = [
    ('head', 'Tête', [('face', 'Muscles de la face'), ('mastic', 'Muscles masticateurs'), ('eye', 'Muscles de l’œil'), ('tongue', 'Langue')]),
    ('neck', 'Cou', [('suprahy', 'Muscles suprahyoïdiens'), ('infrahy', 'Muscles infrahyoïdiens'), ('neckm', 'Muscles latéraux et prévertébraux'), ('pharynx', 'Pharynx et larynx')]),
    ('back', 'Dos', [('backsup', 'Plan superficiel'), ('backmid', 'Plan intermédiaire'), ('backdeep', 'Plan profond'), ('subocc', 'Muscles suboccipitaux')]),
    ('trunk', 'Thorax et abdomen', [('thorax', 'Paroi thoracique et diaphragme'), ('abdomen', 'Paroi abdominale'), ('pelvis', 'Plancher pelvien')]),
    ('ul', 'Membre supérieur', [('shoulder', 'Épaule'), ('armc', 'Bras'), ('fant', 'Avant-bras, loge antérieure'), ('fpost', 'Avant-bras, loge postérieure'), ('hand', 'Main')]),
    ('ll', 'Membre inférieur', [('glut', 'Région glutéale'), ('thant', 'Cuisse, loge antérieure'), ('thmed', 'Cuisse, loge médiale'), ('thpost', 'Cuisse, loge postérieure'), ('legant', 'Jambe, loge antérieure'), ('leglat', 'Jambe, loge latérale'), ('legpost', 'Jambe, loge postérieure'), ('foot', 'Pied')]),
    ('annex', 'Fascias, bourses et gaines', [('fhead', 'Tête et cou'), ('ftrunk', 'Tronc'), ('ful', 'Membre supérieur'), ('fll', 'Membre inférieur')]),
]

TIPS = {
    'all': 'Essentiels : chaque muscle une seule fois, côtés et chefs réunis. Fascias, bourses et gaines se révisent à part.',
    'head': 'Deux grandes familles : les muscles de la face (peauciers, innervés par le nerf facial VII) et les masticateurs (nerf mandibulaire, branche du V3).',
    'face': 'Les muscles de la face s’insèrent sur la peau : ce sont des peauciers, tous innervés par le nerf facial (VII). Le buccinateur forme la joue.',
    'mastic': 'Quatre masticateurs : temporal, masséter, ptérygoïdiens médial et latéral, tous innervés par le nerf mandibulaire (V3). Seul le ptérygoïdien latéral ouvre la bouche.',
    'eye': 'Six muscles oculomoteurs : 4 droits et 2 obliques. Moyen mnémotechnique « LR6 SO4 » : droit latéral par le VI, oblique supérieur par le IV, tous les autres par le III.',
    'tongue': 'Le génioglosse est le muscle « de sécurité » : il propulse la langue en avant. Les muscles de la langue sont innervés par le nerf hypoglosse (XII).',
    'neck': 'Le sternocléidomastoïdien divise le cou en trigones antérieur et postérieur. L’os hyoïde sépare muscles suprahyoïdiens et infrahyoïdiens.',
    'suprahy': 'Les suprahyoïdiens (digastrique, stylohyoïdien, mylohyoïdien, géniohyoïdien) élèvent l’os hyoïde et abaissent la mandibule.',
    'infrahy': 'Les infrahyoïdiens (« muscles en ruban ») abaissent l’os hyoïde et le larynx ; ils sont innervés par l’anse cervicale.',
    'neckm': 'Les scalènes antérieur et moyen délimitent le défilé où passent le plexus brachial et l’artère subclavière.',
    'pharynx': 'Trois constricteurs du pharynx s’emboîtent comme des gobelets. Le crico-aryténoïdien postérieur est le seul muscle qui ouvre la glotte.',
    'back': 'Trois plans : superficiel (muscles qui vont au membre supérieur), intermédiaire (dentelés postérieurs, respiratoires) et profond (muscles propres du dos, innervés par les rameaux dorsaux).',
    'backsup': 'Trapèze et grand dorsal recouvrent tout le dos. Le trapèze est innervé par le nerf accessoire (XI), le grand dorsal par le nerf thoracodorsal.',
    'backmid': 'Les dentelés postérieurs sont des muscles respiratoires accessoires ; les splénius étendent et tournent la tête.',
    'backdeep': 'L’érecteur du rachis compte trois colonnes, de dehors en dedans : iliocostal, longissimus, épineux (« I Love Spine »). Les transversaires épineux sont dessous.',
    'subocc': 'Quatre muscles suboccipitaux délimitent le trigone suboccipital, traversé par l’artère vertébrale ; innervés par le nerf suboccipital (C1).',
    'trunk': 'Le diaphragme est le principal muscle inspiratoire. La paroi abdominale compte trois muscles larges superposés et le droit de l’abdomen.',
    'thorax': 'Les intercostaux externes sont inspirateurs, les internes expirateurs. Le dentelé antérieur plaque la scapula contre le thorax (nerf thoracique long).',
    'abdomen': 'De la surface vers la profondeur : oblique externe, oblique interne, transverse. Leurs aponévroses forment la gaine des droits et la ligne blanche.',
    'pelvis': 'Le diaphragme pelvien est formé de l’élévateur de l’anus (pubo-coccygien, ilio-coccygien, pubo-anal) et du muscle coccygien.',
    'ul': 'Au bras et à l’avant-bras, la loge antérieure fléchit et la loge postérieure étend. Le brachioradial, loge postérieure, fléchit pourtant le coude.',
    'shoulder': 'Coiffe des rotateurs : supra-épineux, infra-épineux, petit rond, subscapulaire (« SIPS »). Le deltoïde est innervé par le nerf axillaire.',
    'armc': 'Loge antérieure (nerf musculocutané) : biceps, brachial, coracobrachial. Loge postérieure (nerf radial) : triceps.',
    'fant': 'Les fléchisseurs naissent surtout de l’épicondyle médial. Plan superficiel, de dehors en dedans : rond pronateur, fléchisseur radial du carpe, long palmaire, fléchisseur ulnaire du carpe.',
    'fpost': 'Les extenseurs naissent surtout de l’épicondyle latéral et sont tous innervés par le nerf radial. Le long abducteur et les extenseurs du pouce bordent la tabatière anatomique.',
    'hand': 'Éminence thénar (pouce, nerf médian) et hypothénar (petit doigt, nerf ulnaire). Interosseux : les palmaires rapprochent (PAD), les dorsaux écartent (DAB).',
    'll': 'À la cuisse : loge antérieure (nerf fémoral) qui étend le genou, loge médiale (nerf obturateur) qui adducte, loge postérieure (nerf sciatique) qui fléchit.',
    'glut': 'Grand fessier : extenseur de la hanche. Moyen et petit fessiers : abducteurs, ils stabilisent le bassin à la marche (signe de Trendelenburg).',
    'thant': 'Le quadriceps réunit droit fémoral et trois vastes, sur le tendon quadricipital et la patella. Le sartorius est le plus long muscle du corps.',
    'thmed': 'Adducteurs de dehors en dedans au plan superficiel : pectiné, long adducteur, gracile. Ils sont innervés par le nerf obturateur (sauf le pectiné, souvent fémoral).',
    'thpost': 'Les ischio-jambiers (semi-tendineux, semi-membraneux, biceps fémoral) étendent la hanche et fléchissent le genou.',
    'legant': 'Loge antérieure (nerf fibulaire profond) : tibial antérieur, long extenseur de l’hallux, long extenseur des orteils, troisième fibulaire. Ils font la flexion dorsale du pied.',
    'leglat': 'Long et court fibulaires (nerf fibulaire superficiel) : éversion du pied. Leurs tendons passent derrière la malléole latérale.',
    'legpost': 'Triceps sural = gastrocnémien + soléaire, sur le tendon calcanéen. En profondeur, derrière la malléole médiale : « Tom, Dick ANd Harry » (tibial postérieur, long fléchisseur des orteils, artère et nerf, long fléchisseur de l’hallux).',
    'foot': 'Quatre couches plantaires. Le seul muscle dorsal est le court extenseur des orteils (pédieux), avec le court extenseur de l’hallux.',
    'annex': 'Fascias, bourses séreuses et gaines tendineuses : ils guident et protègent muscles et tendons. Les bourses réduisent les frottements près des os.',
    'fhead': 'Le fascia cervical a trois lames : superficielle, prétrachéale et prévertébrale.',
    'ftrunk': 'Le fascia thoracolombaire enveloppe les muscles profonds du dos et donne insertion au grand dorsal et au transverse de l’abdomen.',
    'ful': 'Les rétinaculums du poignet maintiennent les tendons ; sous le rétinaculum des fléchisseurs passe le canal carpien (nerf médian).',
    'fll': 'Les bourses du genou (prépatellaire, infrapatellaire, suprapatellaire) sont souvent en cause dans les bursites ; la suprapatellaire communique avec l’articulation.',
}

# ---- réglages du générateur (build_system.py) ----
INVENTORY = 'nq_muscular'
PREFIX = 'm_'
SEPARATE = {'annex'}   # révisés à part, jamais dans « Corps entier » (ils recouvriraient les muscles)
FEMININE = ['partie', 'parties', 'bourse', 'bourses', 'gaine', 'gaines', 'aponévrose', 'arcade', 'lame', 'trochlée', 'ligne']
PLURAL = ['muscles', 'parties', 'bourses', 'gaines', 'tendons']
ZONE = {'face': 'head', 'mastic': 'head', 'eye': 'head', 'tongue': 'head', 'suprahy': 'head', 'infrahy': 'head', 'neckm': 'head', 'pharynx': 'head',
        'backsup': 'torso/spine', 'backmid': 'torso/spine', 'backdeep': 'torso/spine', 'subocc': 'head',
        'thorax': 'torso/ribcage', 'abdomen': 'torso/pelvis', 'pelvis': 'torso/pelvis',
        'shoulder': 'arm', 'armc': 'arm', 'fant': 'arm', 'fpost': 'arm', 'hand': 'hand',
        'glut': 'torso/pelvis', 'thant': 'leg', 'thmed': 'leg', 'thpost': 'leg', 'legant': 'leg', 'leglat': 'leg', 'legpost': 'leg', 'foot': 'foot'}
BACK_SUBS = {'backsup', 'backmid', 'backdeep', 'subocc', 'glut', 'thpost', 'legpost', 'fpost'}
BACK_IDS = {'Long head of triceps brachii', 'Lateral head of triceps brachii', 'Medial head of triceps brachii', 'Quadratus lumborum muscle'}

def camera(reg, sub, en, c):
    """Zone de caméra (clés des régions osseuses) et vue de dos éventuelle."""
    cy, cz = c[1], c[2]
    if reg == 'annex':
        if sub == 'fhead': zone = 'head'
        elif sub == 'ftrunk': zone = 'torso/spine' if 'thoracolumbar' in en else ('torso/ribcage' if cy > 1.2 else 'torso/pelvis')
        elif sub == 'ful': zone = 'hand' if cy < 0.83 else 'arm'
        else: zone = 'foot' if cy < 0.13 else ('torso/pelvis' if cy > 0.75 else 'leg')
        return zone, 'back' if cz < -0.035 else ''
    return ZONE[sub], 'back' if (sub in BACK_SUBS or en in BACK_IDS) else ''
