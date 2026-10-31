# Table du système sanguin : nom Z-Anatomy (anglais, sans .l/.r) -> données françaises.
# Format : anglais | nom officiel | nom usuel (vide si aucun) | section (région/sous-région) | type | groupe
#   type   : artery, vein, pulmart (artère pulmonaire, sang pauvre en oxygène), pulmvein (veine pulmonaire), heart, valve
#   groupe : clé du groupe « essentiels » ; vide = groupe propre ; « - » = hors essentiels (fines branches).
ROWS = r"""
Left coronary artery|Artère coronaire gauche||heart/coronary|artery|
Anterior interventricular artery|Artère interventriculaire antérieure|IVA|heart/coronary|artery|
Septal branches of anterior interventricular artery|Rameaux interventriculaires septaux||heart/coronary|artery|-
Circumflex artery of heart|Rameau circonflexe de l'artère coronaire gauche|artère circonflexe|heart/coronary|artery|
Right coronary artery|Artère coronaire droite||heart/coronary|artery|
Right inferolateral branch of right coronary artery|Rameau inférolatéral droit de l'artère coronaire droite|rétroventriculaire|heart/coronary|artery|
Left atrium|Atrium gauche|oreillette gauche|heart/cavities|heart|
Left ventricle|Ventricule gauche||heart/cavities|heart|
Inferior papillary muscle of left ventricle|Muscle papillaire inférieur du ventricule gauche|pilier postérieur|heart/cavities|heart|
Right atrium|Atrium droit|oreillette droite|heart/cavities|heart|
Right ventricle|Ventricule droit||heart/cavities|heart|
Anterior papillary muscle of right ventricle|Muscle papillaire antérieur du ventricule droit||heart/cavities|heart|papillary_rv
Inferior papillary muscle of right ventricle|Muscle papillaire inférieur du ventricule droit||heart/cavities|heart|papillary_rv
Septal papillary muscle of right ventricle|Muscle papillaire septal du ventricule droit||heart/cavities|heart|papillary_rv
Inferior leaflet of right atrioventricular valve|Cuspide inférieure de la valve tricuspide||heart/valves|valve|tricuspid
Posterior leaflet of left atrioventricular valve|Cuspide postérieure de la valve mitrale||heart/valves|valve|
Septal leaflet of right atrioventricular valve|Cuspide septale de la valve tricuspide||heart/valves|valve|tricuspid
Left coronary leaflet|Valvule semi-lunaire coronaire gauche de la valve aortique|sigmoïde aortique gauche|heart/valves|valve|aortic_valve
Non-coronary leaflet|Valvule semi-lunaire non coronaire de la valve aortique|sigmoïde aortique postérieure|heart/valves|valve|aortic_valve
Right coronary leaflet|Valvule semi-lunaire coronaire droite de la valve aortique|sigmoïde aortique droite|heart/valves|valve|aortic_valve
Anterior semilunar leaflet of pulmonary valve|Valvule semi-lunaire antérieure de la valve pulmonaire||heart/valves|valve|pulmonary_valve
Left semilunar leaflet of pulmonary valve|Valvule semi-lunaire gauche de la valve pulmonaire||heart/valves|valve|pulmonary_valve
Right semilunar leaflet of pulmonary valve|Valvule semi-lunaire droite de la valve pulmonaire||heart/valves|valve|pulmonary_valve
Left pulmonary artery|Artère pulmonaire gauche||pulm/partery|pulmart|
Anterior basal segmental artery of left lung|Artère segmentaire basale antérieure du poumon gauche||pulm/partery|pulmart|-
Lateral basal segmental artery of left lung|Artère segmentaire basale latérale du poumon gauche||pulm/partery|pulmart|-
Medial basal segmental artery of left lung|Artère segmentaire basale médiale du poumon gauche||pulm/partery|pulmart|-
Posterior basal segmental artery of left lung|Artère segmentaire basale postérieure du poumon gauche||pulm/partery|pulmart|-
Superior segmental artery of left lung|Artère segmentaire supérieure du poumon gauche|artère de Nelson|pulm/partery|pulmart|-
Anterior segmental artery of left lung|Artère segmentaire antérieure du poumon gauche||pulm/partery|pulmart|-
Apical segmental artery of left lung|Artère segmentaire apicale du poumon gauche||pulm/partery|pulmart|-
Inferior lingular artery of left lung|Artère lingulaire inférieure du poumon gauche||pulm/partery|pulmart|-
Posterior segmental artery of left lung|Artère segmentaire postérieure du poumon gauche||pulm/partery|pulmart|-
Superior lingular artery of left lung|Artère lingulaire supérieure du poumon gauche||pulm/partery|pulmart|-
Pulmonary trunk|Tronc pulmonaire|artère pulmonaire|pulm/partery|pulmart|
Bifurcation of pulmonary trunk|Bifurcation du tronc pulmonaire||pulm/partery|pulmart|-
Right pulmonary artery|Artère pulmonaire droite||pulm/partery|pulmart|
Inferior lobar artery of right lung|Artère lobaire inférieure du poumon droit||pulm/partery|pulmart|
Anterior basal segmental artery of right lung|Artère segmentaire basale antérieure du poumon droit||pulm/partery|pulmart|-
Lateral basal segmental artery of right lung|Artère segmentaire basale latérale du poumon droit||pulm/partery|pulmart|-
Medial basal segmental artery of right lung|Artère segmentaire basale médiale du poumon droit||pulm/partery|pulmart|-
Posterior basal segmental artery of right lung|Artère segmentaire basale postérieure du poumon droit||pulm/partery|pulmart|-
Superior segmental artery of right lung|Artère segmentaire supérieure du poumon droit|artère de Nelson|pulm/partery|pulmart|-
Middle lobar artery of right lung|Artère lobaire moyenne du poumon droit||pulm/partery|pulmart|
Lateral segmental artery of right lung|Artère segmentaire latérale du poumon droit||pulm/partery|pulmart|-
Medial segmental artery of right lung|Artère segmentaire médiale du poumon droit||pulm/partery|pulmart|-
Superior lobar artery of right lung|Artère lobaire supérieure du poumon droit|tronc artériel supérieur|pulm/partery|pulmart|
Anterior segmental artery of right lung|Artère segmentaire antérieure du poumon droit||pulm/partery|pulmart|-
Apical segmental artery of right lung|Artère segmentaire apicale du poumon droit||pulm/partery|pulmart|-
Posterior segmental artery of right lung|Artère segmentaire postérieure du poumon droit||pulm/partery|pulmart|-
Abdominal aorta|Aorte abdominale||aorta/abdo|artery|
Coeliac trunk|Tronc cœliaque||aorta/digest|artery|
Common hepatic artery|Artère hépatique commune||aorta/digest|artery|
Gastroduodenal artery|Artère gastroduodénale||aorta/digest|artery|
Proper hepatic artery|Artère hépatique propre||aorta/digest|artery|
Left gastric artery|Artère gastrique gauche|artère coronaire stomachique|aorta/digest|artery|
Splenic artery|Artère splénique||aorta/digest|artery|
Inferior mesenteric artery|Artère mésentérique inférieure||aorta/digest|artery|
Left colic artery|Artère colique gauche||aorta/digest|artery|
Ascending branch of left colic artery|Rameau ascendant de l'artère colique gauche||aorta/digest|artery|-
Descending branch of left colic artery|Rameau descendant de l'artère colique gauche||aorta/digest|artery|-
Sigmoid arteries|Artères sigmoïdiennes||aorta/digest|artery|
Superior anorectal artery|Artère rectale supérieure|artère hémorroïdale supérieure|aorta/digest|artery|
Inferior phrenic artery|Artère phrénique inférieure|artère diaphragmatique inférieure|aorta/abdo|artery|
Left renal artery|Artère rénale gauche||aorta/abdo|artery|
Anterior branch of renal artery|Rameau antérieur de l'artère rénale||aorta/abdo|artery|-
Inferior suprarenal artery|Artère surrénale inférieure|artère capsulaire inférieure|aorta/abdo|artery|
Intrarenal arteries of left kidney|Artères intrarénales du rein gauche||aorta/abdo|artery|-
Posterior branch of renal artery|Rameau postérieur de l'artère rénale||aorta/abdo|artery|-
Left testicular artery|Artère testiculaire gauche|artère spermatique|aorta/abdo|artery|
Lumbar arteries|Artères lombales|artères lombaires|aorta/abdo|artery|
Right renal artery|Artère rénale droite||aorta/abdo|artery|
Intrarenal arteries of right kidney|Artères intrarénales du rein droit||aorta/abdo|artery|-
Right testicular artery|Artère testiculaire droite|artère spermatique|aorta/abdo|artery|
Superior mesenteric artery|Artère mésentérique supérieure||aorta/digest|artery|
Ileocolic artery|Artère iléocolique||aorta/digest|artery|
Appendicular artery|Artère appendiculaire||aorta/digest|artery|
Colic branch of ileocolic artery|Rameau colique de l'artère iléocolique||aorta/digest|artery|-
Ileal branch of ileocolic artery|Rameau iléal de l'artère iléocolique||aorta/digest|artery|-
Inferior pancreaticoduodenal artery|Artère pancréaticoduodénale inférieure||aorta/digest|artery|
Anterior inferior pancreaticoduodenal artery|Rameau antérieur de l'artère pancréaticoduodénale inférieure||aorta/digest|artery|-
Marginal artery|Artère marginale du côlon|arcade de Riolan|aorta/digest|artery|
Middle colic artery|Artère colique moyenne||aorta/digest|artery|
Right colic artery|Artère colique droite||aorta/digest|artery|
Aortic arch|Arc de l'aorte|crosse de l'aorte|aorta/thor|artery|
Brachiocephalic trunk|Tronc brachiocéphalique|tronc artériel brachio-céphalique|aorta/thor|artery|
Common iliac artery|Artère iliaque commune|artère iliaque primitive|aorta/pelvis|artery|
External iliac artery|Artère iliaque externe||aorta/pelvis|artery|
Inferior epigastric artery|Artère épigastrique inférieure||aorta/pelvis|artery|
Internal iliac artery|Artère iliaque interne|artère hypogastrique|aorta/pelvis|artery|
Anterior division of internal iliac artery|Tronc antérieur de l'artère iliaque interne||aorta/pelvis|artery|
Inferior gluteal artery|Artère glutéale inférieure|artère ischiatique|aorta/pelvis|artery|
Internal pudendal artery|Artère pudendale interne|artère honteuse interne|aorta/pelvis|artery|
Deep artery of penis|Artère profonde du pénis|artère caverneuse|aorta/pelvis|artery|
Dorsal artery of penis|Artère dorsale du pénis||aorta/pelvis|artery|
Posterior division of internal iliac artery|Tronc postérieur de l'artère iliaque interne||aorta/pelvis|artery|
Iliolumbar artery|Artère iliolombale||aorta/pelvis|artery|
Iliacus branch of iliolumbar artery|Rameau iliaque de l'artère iliolombale||aorta/pelvis|artery|-
Lumbar branch of iliolumbar artery|Rameau lombal de l'artère iliolombale||aorta/pelvis|artery|-
Spinal branch of iliolumbar artery|Rameau spinal de l'artère iliolombale||aorta/pelvis|artery|-
Superior gluteal artery|Artère glutéale supérieure|artère fessière|aorta/pelvis|artery|
Obturator artery|Artère obturatrice||aorta/pelvis|artery|
Median sacral artery|Artère sacrale médiane||aorta/abdo|artery|
Ascending aorta|Aorte ascendante||aorta/thor|artery|
Thoracic aorta|Aorte thoracique|aorte descendante|aorta/thor|artery|
Posterior intercostal arteries|Artères intercostales postérieures||aorta/thor|artery|
Subcostal artery|Artère subcostale||aorta/thor|artery|
Superior phrenic arteries|Artères phréniques supérieures||aorta/thor|artery|
Anterior spinal artery|Artère spinale antérieure||headart/brain|artery|
Anterior communicating artery|Artère communicante antérieure||headart/brain|artery|
Posterior communicating artery|Artère communicante postérieure||headart/brain|artery|
Femoral artery|Artère fémorale|artère fémorale commune et superficielle|llart/femoral|artery|
Deep external pudendal artery|Artère pudendale externe profonde||llart/femoral|artery|-
Deep femoral artery|Artère profonde de la cuisse|artère fémorale profonde|llart/femoral|artery|
Lateral circumflex femoral artery|Artère circonflexe fémorale latérale||llart/femoral|artery|
Descending branch of lateral circumflex femoral artery|Rameau descendant de l'artère circonflexe fémorale latérale||llart/femoral|artery|-
Medial circumflex femoral artery|Artère circonflexe fémorale médiale||llart/femoral|artery|
Perforating femoral arteries|Artères perforantes de la cuisse||llart/femoral|artery|
Popliteal artery|Artère poplitée||llart/leg|artery|
Anterior tibial artery|Artère tibiale antérieure||llart/leg|artery|
Dorsalis pedis artery|Artère dorsale du pied|artère pédieuse|llart/foot|artery|
Arcuate artery|Artère arquée||llart/foot|artery|
Dorsal metatarsal arteries|Artères métatarsiennes dorsales||llart/foot|artery|-
Dorsal digital arteries of foot|Artères digitales dorsales du pied||llart/foot|artery|-
Deep plantar artery|Artère plantaire profonde||llart/foot|artery|-
Lateral tarsal artery|Artère tarsienne latérale||llart/foot|artery|-
Inferior lateral genicular artery|Artère inférieure latérale du genou|artère articulaire inféro-externe|llart/leg|artery|genicular
Inferior medial genicular artery|Artère inférieure médiale du genou|artère articulaire inféro-interne|llart/leg|artery|genicular
Middle genicular artery|Artère moyenne du genou||llart/leg|artery|genicular
Patellar anastomosis|Réseau patellaire|cercle artériel péripatellaire|llart/leg|artery|-
Posterior tibial artery|Artère tibiale postérieure||llart/leg|artery|
Calcaneal branches of posterior tibial artery|Rameaux calcanéens de l'artère tibiale postérieure||llart/foot|artery|-
Fibular artery|Artère fibulaire|artère péronière|llart/leg|artery|
Calcaneal branches of fibular artery|Rameaux calcanéens de l'artère fibulaire||llart/foot|artery|-
Lateral plantar artery|Artère plantaire latérale|artère plantaire externe|llart/foot|artery|
Plantar arch|Arcade plantaire profonde||llart/foot|artery|
Plantar metatarsal arteries|Artères métatarsiennes plantaires||llart/foot|artery|-
Common plantar digital arteries|Artères digitales plantaires communes||llart/foot|artery|-
Proper plantar digital arteries|Artères digitales plantaires propres||llart/foot|artery|-
Perforating branches of plantar metatarsal arteries|Rameaux perforants des artères métatarsiennes plantaires||llart/foot|artery|-
Medial plantar artery|Artère plantaire médiale|artère plantaire interne|llart/foot|artery|
Superficial branch of medial plantar artery|Rameau superficiel de l'artère plantaire médiale||llart/foot|artery|-
Superior lateral genicular artery|Artère supérieure latérale du genou|artère articulaire supéro-externe|llart/leg|artery|genicular
Superior medial genicular artery|Artère supérieure médiale du genou|artère articulaire supéro-interne|llart/leg|artery|genicular
Superficial epigastric artery|Artère épigastrique superficielle|artère sous-cutanée abdominale|llart/femoral|artery|
Superficial external pudendal artery|Artère pudendale externe superficielle||llart/femoral|artery|-
Left common carotid artery|Artère carotide commune gauche|carotide primitive gauche|aorta/thor|artery|common_carotid
External carotid artery|Artère carotide externe||headart/extcar|artery|
Ascending pharyngeal artery|Artère pharyngienne ascendante||headart/extcar|artery|
Facial artery|Artère faciale||headart/extcar|artery|
Angular artery|Artère angulaire||headart/extcar|artery|
Inferior labial artery|Artère labiale inférieure|artère coronaire labiale inférieure|headart/extcar|artery|
Submental artery|Artère submentale||headart/extcar|artery|
Superior labial artery|Artère labiale supérieure|artère coronaire labiale supérieure|headart/extcar|artery|
Maxillary artery|Artère maxillaire|artère maxillaire interne|headart/extcar|artery|
Anterior deep temporal artery|Artère temporale profonde antérieure||headart/extcar|artery|-
Artery of pterygoid canal|Artère du canal ptérygoïdien|artère vidienne|headart/extcar|artery|-
Buccal artery|Artère buccale||headart/extcar|artery|-
Descending palatine artery|Artère palatine descendante||headart/extcar|artery|-
Greater palatine artery|Artère grande palatine||headart/extcar|artery|-
Inferior alveolar artery|Artère alvéolaire inférieure|artère dentaire inférieure|headart/extcar|artery|
Mental branch of inferior alveolar artery|Rameau mentonnier de l'artère alvéolaire inférieure||headart/extcar|artery|-
Mylohyoid branch of inferior alveolar artery|Rameau mylohyoïdien de l'artère alvéolaire inférieure||headart/extcar|artery|-
Infra-orbital artery|Artère infra-orbitaire|artère sous-orbitaire|headart/extcar|artery|
Middle meningeal artery|Artère méningée moyenne||headart/extcar|artery|
Accessory branch of middle meningeal artery|Rameau accessoire de l'artère méningée moyenne||headart/extcar|artery|-
Posterior deep temporal artery|Artère temporale profonde postérieure||headart/extcar|artery|-
Posterior lateral nasal branches of sphenopalatine artery.|Artères nasales postérieures latérales||headart/extcar|artery|-
Posterior septal branches of sphenopalatine artery|Rameaux septaux postérieurs de l'artère sphénopalatine||headart/extcar|artery|-
Posterior superior alveolar artery|Artère alvéolaire supérieure postérieure||headart/extcar|artery|-
Occipital artery|Artère occipitale||headart/extcar|artery|
Superficial temporal artery|Artère temporale superficielle||headart/extcar|artery|
Frontal branch of superficial temporal artery|Rameau frontal de l'artère temporale superficielle||headart/extcar|artery|-
Transverse facial artery|Artère transverse de la face||headart/extcar|artery|-
Internal carotid artery|Artère carotide interne||headart/intcar|artery|
Middle cerebral artery (M1-segment)|Segment M1 de l'artère cérébrale moyenne|segment sphénoïdal, artère sylvienne|headart/brain|artery|
Distal lateral striate branches|Rameaux striés latéraux distaux||headart/brain|artery|lenticulostriate
Insular branches of middle cerebral artery (M2-segment)|Segment M2 de l'artère cérébrale moyenne, premier tronçon|segment insulaire|headart/brain|artery|mca_m2
Anterior temporal branch|Rameau temporal antérieur de l'artère cérébrale moyenne||headart/brain|artery|-
Artery of precentral sulcus|Artère du sillon précentral||headart/brain|artery|-
Middle cerebral artery (M3 segment)|Segment M3 de l'artère cérébrale moyenne, premier tronçon|segment operculaire|headart/brain|artery|mca_m3
Artery of central sulcus|Artère du sillon central|artère rolandique|headart/brain|artery|-
Parietal branches of middle cerebral artery|Rameaux pariétaux de l'artère cérébrale moyenne||headart/brain|artery|-
Postcentral arterial branch|Artère du sillon postcentral||headart/brain|artery|-
Posterior parietal artery|Artère pariétale postérieure||headart/brain|artery|-
Posterior temporal branch|Rameau temporal postérieur de l'artère cérébrale moyenne||headart/brain|artery|-
Temporal branches of middle cerebral artery|Rameaux temporaux de l'artère cérébrale moyenne||headart/brain|artery|-
Temporo-occipital branch|Rameau temporo-occipital de l'artère cérébrale moyenne||headart/brain|artery|-
Branch to angular gyrus|Artère du gyrus angulaire||headart/brain|artery|-
Prefrontal artery|Artère préfrontale||headart/brain|artery|-
Lateral frontobasal artery|Artère frontobasale latérale|artère orbitofrontale latérale|headart/brain|artery|-
Proximal lateral striate branches|Rameaux striés latéraux proximaux|artères lenticulostriées|headart/brain|artery|lenticulostriate
Ophthalmic artery|Artère ophtalmique||headart/intcar|artery|
Anterior ethmoidal artery|Artère ethmoïdale antérieure||headart/intcar|artery|
Anterior septal branches of anterior ethmoidal artery|Rameaux septaux antérieurs de l'artère ethmoïdale antérieure||headart/intcar|artery|-
Central retinal artery|Artère centrale de la rétine||headart/intcar|artery|
Lacrimal artery|Artère lacrymale||headart/intcar|artery|
Long posterior ciliary arteries|Artères ciliaires postérieures longues||headart/intcar|artery|-
Posterior ethmoidal artery|Artère ethmoïdale postérieure||headart/intcar|artery|
Septal branches of posterior ethmoidal artery|Rameaux septaux de l'artère ethmoïdale postérieure||headart/intcar|artery|-
Short posterior ciliary arteries|Artères ciliaires postérieures courtes||headart/intcar|artery|-
Supra-orbital artery|Artère supra-orbitaire|artère sus-orbitaire|headart/intcar|artery|
Supratrochlear artery|Artère supratrochléaire|artère frontale interne|headart/intcar|artery|
Left subclavian artery|Artère subclavière gauche|artère sous-clavière gauche|aorta/thor|artery|subclavian
Axillary artery|Artère axillaire||ulart/axbr|artery|
Anterior circumflex humeral artery|Artère circonflexe humérale antérieure||ulart/axbr|artery|
Brachial artery|Artère brachiale|artère humérale|ulart/axbr|artery|
Deep brachial artery|Artère profonde du bras|artère humérale profonde|ulart/axbr|artery|
Middle collateral artery|Artère collatérale moyenne||ulart/axbr|artery|-
Radial collateral artery|Artère collatérale radiale||ulart/axbr|artery|-
Inferior ulnar collateral artery|Artère collatérale ulnaire inférieure||ulart/axbr|artery|-
Radial artery|Artère radiale||ulart/forearm|artery|
Deep palmar arch|Arcade palmaire profonde||ulart/forearm|artery|
Palmar metacarpal arteries|Artères métacarpiennes palmaires||ulart/forearm|artery|-
Dorsal carpal anastomosis|Réseau carpien dorsal||ulart/forearm|artery|-
Dorsal metacarpal arteries|Artères métacarpiennes dorsales||ulart/forearm|artery|-
Dorsal digital arteries of hand|Artères digitales dorsales de la main||ulart/forearm|artery|-
Palmar carpal branch of radial artery|Rameau carpien palmaire de l'artère radiale||ulart/forearm|artery|-
Superior ulnar collateral artery|Artère collatérale ulnaire supérieure||ulart/axbr|artery|-
Ulnar artery|Artère ulnaire|artère cubitale|ulart/forearm|artery|
(Ulnar recurrent artery)|Artère récurrente ulnaire||ulart/forearm|artery|-
Common interosseous artery|Artère interosseuse commune|tronc des interosseuses|ulart/forearm|artery|
Posterior interosseous artery|Artère interosseuse postérieure||ulart/forearm|artery|
Recurrent interosseous artery|Artère interosseuse récurrente||ulart/forearm|artery|-
Dorsal carpal branch of ulnar artery|Rameau carpien dorsal de l'artère ulnaire||ulart/forearm|artery|-
Superficial palmar arch|Arcade palmaire superficielle||ulart/forearm|artery|
Common palmar digital arteries|Artères digitales palmaires communes||ulart/forearm|artery|-
Proper palmar digital arteries|Artères digitales palmaires propres||ulart/forearm|artery|-
Lateral thoracic artery|Artère thoracique latérale|artère mammaire externe|ulart/axbr|artery|
Posterior circumflex humeral artery|Artère circonflexe humérale postérieure||ulart/axbr|artery|
Subscapular artery|Artère subscapulaire|artère scapulaire inférieure|ulart/axbr|artery|
Circumflex scapular artery|Artère circonflexe de la scapula||ulart/axbr|artery|
Thoracodorsal artery|Artère thoracodorsale||ulart/axbr|artery|
Thoraco-acromial artery|Artère thoraco-acromiale|artère acromio-thoracique|ulart/axbr|artery|
Pectoral branches of thoraco-acromial artery|Rameaux pectoraux de l'artère thoraco-acromiale||ulart/axbr|artery|-
Costocervical trunk|Tronc costocervical|tronc cervico-intercostal|ulart/subclav|artery|
Deep cervical artery|Artère cervicale profonde||ulart/subclav|artery|
Supreme intercostal artery|Artère intercostale suprême||ulart/subclav|artery|
First posterior intercostal artery|Première artère intercostale postérieure||ulart/subclav|artery|-
Second posterior intercostal artery|Deuxième artère intercostale postérieure||ulart/subclav|artery|-
Internal thoracic artery|Artère thoracique interne|artère mammaire interne|ulart/subclav|artery|
Musculophrenic artery|Artère musculophrénique||ulart/subclav|artery|
Superior epigastric artery|Artère épigastrique supérieure||ulart/subclav|artery|
Thyrocervical trunk|Tronc thyrocervical|tronc thyro-bicervico-scapulaire|ulart/subclav|artery|
Inferior thyroid artery|Artère thyroïdienne inférieure||ulart/subclav|artery|
Suprascapular artery|Artère suprascapulaire|artère scapulaire supérieure|ulart/subclav|artery|
Transverse cervical artery|Artère transverse du cou|artère cervicale transverse|ulart/subclav|artery|
(Deep branch of transverse cervical artery)|Rameau profond de l'artère transverse du cou|artère scapulaire dorsale|ulart/subclav|artery|-
(Superficial branch of transverse cervical artery)|Rameau superficiel de l'artère transverse du cou||ulart/subclav|artery|-
Vertebral artery|Artère vertébrale||headart/brain|artery|
Posterior inferior cerebellar artery|Artère cérébelleuse inférieure et postérieure|PICA|headart/brain|artery|
Right common carotid artery|Artère carotide commune droite|carotide primitive droite|aorta/thor|artery|common_carotid
Anterior cerebral artery|Artère cérébrale antérieure||headart/brain|artery|
Callosomarginal artery|Artère calloso-marginale||headart/brain|artery|-
Frontal branches of callosomarginal artery|Rameaux frontaux de l'artère calloso-marginale||headart/brain|artery|-
Orbitofrontal branches of anterior cerebral artery|Rameaux orbitofrontaux de l'artère cérébrale antérieure||headart/brain|artery|-
Pericallosal artery|Artère péricalleuse||headart/brain|artery|
Insular branches of middle cerebral artery (M2)|Segment M2 de l'artère cérébrale moyenne, second tronçon|segment insulaire|headart/brain|artery|mca_m2
Middle cerebral artery (M3-segment)|Segment M3 de l'artère cérébrale moyenne, second tronçon|segment operculaire|headart/brain|artery|mca_m3
Right subclavian artery|Artère subclavière droite|artère sous-clavière droite|aorta/thor|artery|subclavian
Basilar artery|Artère basilaire|tronc basilaire|headart/brain|artery|
Anterior inferior cerebellar artery|Artère cérébelleuse inférieure et antérieure|AICA|headart/brain|artery|
Lateral pontine branches of basilar artery|Rameaux pontiques latéraux de l'artère basilaire||headart/brain|artery|-
Medial pontine branches of basilar artery|Rameaux pontiques médiaux de l'artère basilaire||headart/brain|artery|-
Posterior cerebral artery|Artère cérébrale postérieure||headart/brain|artery|
Lateral occipital artery|Artère occipitale latérale||headart/brain|artery|-
Medial occipital artery|Artère occipitale médiale||headart/brain|artery|-
Parieto-occipital artery|Artère pariéto-occipitale||headart/brain|artery|-
Superior cerebellar artery|Artère cérébelleuse supérieure||headart/brain|artery|
Coronary sinus|Sinus coronaire||heart/coronary|vein|
Great cardiac vein|Grande veine du cœur|grande veine coronaire|heart/coronary|vein|
Inferior vein of left ventricle|Veine inférieure du ventricule gauche||heart/coronary|vein|lv_vein
Inferior vein of left ventricle (//Posterior '')|Veine postérieure du ventricule gauche||heart/coronary|vein|lv_vein
Middle cardiac vein|Veine moyenne du cœur|veine interventriculaire inférieure|heart/coronary|vein|
Left inferior pulmonary vein|Veine pulmonaire inférieure gauche||pulm/pvein|pulmvein|
Inferior basal vein of left lung|Veine basale inférieure du poumon gauche||pulm/pvein|pulmvein|-
Superior basal vein of left lung|Veine basale supérieure du poumon gauche||pulm/pvein|pulmvein|-
Superior vein of left lung|Veine supérieure du lobe inférieur gauche||pulm/pvein|pulmvein|-
Left superior pulmonary vein|Veine pulmonaire supérieure gauche||pulm/pvein|pulmvein|
Anterior vein of left lung|Veine antérieure du poumon gauche||pulm/pvein|pulmvein|-
Apicoposterior vein of left lung|Veine apico-postérieure du poumon gauche||pulm/pvein|pulmvein|-
Lingular vein of left lung|Veine lingulaire du poumon gauche||pulm/pvein|pulmvein|-
Inferior lingular vein of left lung|Veine lingulaire inférieure du poumon gauche||pulm/pvein|pulmvein|-
Superior lingular vein of left lung|Veine lingulaire supérieure du poumon gauche||pulm/pvein|pulmvein|-
Right inferior pulmonary vein|Veine pulmonaire inférieure droite||pulm/pvein|pulmvein|
Inferior basal vein of right lung|Veine basale inférieure du poumon droit||pulm/pvein|pulmvein|-
Superior basal vein of right lung|Veine basale supérieure du poumon droit||pulm/pvein|pulmvein|-
Superior vein of right lung|Veine supérieure du lobe inférieur droit||pulm/pvein|pulmvein|-
Right superior pulmonary vein|Veine pulmonaire supérieure droite||pulm/pvein|pulmvein|
Anterior vein of right lung|Veine antérieure du poumon droit||pulm/pvein|pulmvein|-
Apical vein of right lung|Veine apicale du poumon droit||pulm/pvein|pulmvein|-
Lateral vein of right lung|Veine latérale du lobe moyen||pulm/pvein|pulmvein|-
Medial vein of right lung|Veine médiale du lobe moyen||pulm/pvein|pulmvein|-
Posterior vein of right lung|Veine postérieure du poumon droit||pulm/pvein|pulmvein|-
Inferior petrosal sinus|Sinus pétreux inférieur||headvein/sinus|vein|
Basilar venous plexus|Plexus basilaire||headvein/sinus|vein|
Anterior intercavernous sinus|Sinus intercaverneux antérieur|sinus coronaire antérieur|headvein/sinus|vein|intercavernous
Posterior intercavernous sinus|Sinus intercaverneux postérieur||headvein/sinus|vein|intercavernous
Cavernous sinus|Sinus caverneux||headvein/sinus|vein|
Sigmoid sinus|Sinus sigmoïde||headvein/sinus|vein|
Transverse sinus|Sinus transverse|sinus latéral|headvein/sinus|vein|
Superior petrosal sinus|Sinus pétreux supérieur||headvein/sinus|vein|
Inferior sagittal sinus|Sinus sagittal inférieur|sinus longitudinal inférieur|headvein/sinus|vein|
Occipital sinus|Sinus occipital||headvein/sinus|vein|
Straight sinus|Sinus droit||headvein/sinus|vein|
Superior sagittal sinus|Sinus sagittal supérieur|sinus longitudinal supérieur|headvein/sinus|vein|
Inferior ophthalmic vein|Veine ophtalmique inférieure||headvein/sinus|vein|
Superior ophthalmic vein|Veine ophtalmique supérieure||headvein/sinus|vein|
Femoral vein|Veine fémorale||llvein/deepll|vein|
Deep femoral vein|Veine profonde de la cuisse|veine fémorale profonde|llvein/deepll|vein|
Perforating veins|Veines perforantes de la cuisse||llvein/deepll|vein|-
Great saphenous vein|Grande veine saphène|veine saphène interne|llvein/supll|vein|
External pudendal veins|Veines pudendales externes||llvein/supll|vein|-
Superficial epigastric vein|Veine épigastrique superficielle||llvein/supll|vein|
Lateral circumflex femoral veins|Veines circonflexes fémorales latérales||llvein/deepll|vein|-
Medial circumflex femoral veins|Veines circonflexes fémorales médiales||llvein/deepll|vein|-
Popliteal vein|Veine poplitée||llvein/deepll|vein|
Anterior tibial veins|Veines tibiales antérieures||llvein/deepll|vein|
Genicular veins|Veines du genou|veines articulaires du genou|llvein/deepll|vein|-
Posterior tibial veins|Veines tibiales postérieures||llvein/deepll|vein|
Fibular veins|Veines fibulaires|veines péronières|llvein/deepll|vein|
Lateral plantar veins|Veines plantaires latérales||llvein/deepll|vein|
Plantar venous arch|Arcade veineuse plantaire||llvein/deepll|vein|
Plantar metatarsal veins|Veines métatarsiennes plantaires||llvein/deepll|vein|-
Plantar digital veins|Veines digitales plantaires||llvein/deepll|vein|-
Medial plantar veins|Veines plantaires médiales||llvein/deepll|vein|
Small saphenous vein|Petite veine saphène|veine saphène externe|llvein/supll|vein|
Dorsal venous arch of foot|Arcade veineuse dorsale du pied||llvein/supll|vein|
Dorsal metatarsal veins|Veines métatarsiennes dorsales||llvein/supll|vein|-
Dorsal digital veins of foot|Veines digitales dorsales du pied||llvein/supll|vein|-
Intercapitular veins of foot|Veines intercapitulaires du pied||llvein/deepll|vein|-
Superficial dorsal veins of penis|Veines dorsales superficielles du pénis||trunkvein/vci|vein|-
Hepatic portal vein|Veine porte hépatique|veine porte|trunkvein/portal|vein|
Splenic vein|Veine splénique||trunkvein/portal|vein|
Inferior mesenteric vein|Veine mésentérique inférieure|petite mésaraïque|trunkvein/portal|vein|
Sigmoid veins|Veines sigmoïdiennes||trunkvein/portal|vein|-
Left gastro-omental vein|Veine gastro-omentale gauche|veine gastro-épiploïque gauche|trunkvein/portal|vein|-
Superior mesenteric vein|Veine mésentérique supérieure|grande mésaraïque|trunkvein/portal|vein|
Middle colic vein|Veine colique moyenne||trunkvein/portal|vein|-
Right colic vein|Veine colique droite||trunkvein/portal|vein|-
Right gastro-omental vein|Veine gastro-omentale droite|veine gastro-épiploïque droite|trunkvein/portal|vein|-
Inferior vena cava (thoracic part)|Veine cave inférieure, partie thoracique||trunkvein/vci|vein|ivc
Hepatic veins|Veines hépatiques|veines sus-hépatiques|trunkvein/vci|vein|
Inferior vena cava (abdominal part)|Veine cave inférieure, partie abdominale||trunkvein/vci|vein|ivc
Common iliac vein|Veine iliaque commune|veine iliaque primitive|trunkvein/vci|vein|
External iliac vein|Veine iliaque externe||trunkvein/vci|vein|
Inferior epigastric vein|Veine épigastrique inférieure||trunkvein/vci|vein|
Iliolumbar vein|Veine iliolombale||trunkvein/vci|vein|-
Internal iliac vein|Veine iliaque interne|veine hypogastrique|trunkvein/vci|vein|
Inferior gluteal veins|Veines glutéales inférieures||trunkvein/vci|vein|-
Internal pudendal vein|Veine pudendale interne|veine honteuse interne|trunkvein/vci|vein|
Lateral sacral veins|Veines sacrales latérales||trunkvein/vci|vein|-
Superior gluteal veins|Veines glutéales supérieures||trunkvein/vci|vein|-
Deep dorsal vein of penis|Veine dorsale profonde du pénis||trunkvein/vci|vein|-
Left renal vein|Veine rénale gauche||trunkvein/vci|vein|
Intrarenal veins of left kidney|Veines intrarénales du rein gauche||trunkvein/vci|vein|-
Left testicular vein|Veine testiculaire gauche|veine spermatique gauche|trunkvein/vci|vein|
Lumbar veins|Veines lombales|veines lombaires|trunkvein/vci|vein|
Right renal vein|Veine rénale droite||trunkvein/vci|vein|
Intrarenal veins of right kidney|Veines intrarénales du rein droit||trunkvein/vci|vein|-
Right testicular vein|Veine testiculaire droite|veine spermatique droite|trunkvein/vci|vein|
Internal jugular vein|Veine jugulaire interne||headvein/neckv|vein|
Common facial vein|Tronc veineux thyro-linguo-facial||headvein/neckv|vein|
Anterior division of retromandibular vein|Branche antérieure de la veine rétromandibulaire||headvein/neckv|vein|-
Retromandibular vein|Veine rétromandibulaire|veine jugulaire externe supérieure|headvein/neckv|vein|
Maxillary veins|Veines maxillaires||headvein/neckv|vein|-
Superficial temporal veins|Veines temporales superficielles||headvein/neckv|vein|
Facial vein|Veine faciale||headvein/neckv|vein|
Angular vein|Veine angulaire||headvein/neckv|vein|
Inferior labial veins|Veines labiales inférieures||headvein/neckv|vein|-
Submental vein|Veine submentale||headvein/neckv|vein|-
Superior labial vein|Veine labiale supérieure||headvein/neckv|vein|-
Lingual vein|Veine linguale||headvein/neckv|vein|
Superior thyroid vein|Veine thyroïdienne supérieure||headvein/neckv|vein|
Left subclavian vein|Veine subclavière gauche|veine sous-clavière gauche|ulvein/deepul|vein|subclavian_vein
Axillary vein|Veine axillaire||ulvein/deepul|vein|
Anterior circumflex humeral vein|Veine circonflexe humérale antérieure||ulvein/deepul|vein|-
Basilic vein|Veine basilique||ulvein/supul|vein|
Median cubital vein|Veine intermédiaire du coude|veine médiane basilique|ulvein/supul|vein|
Median antebrachial vein|Veine intermédiaire de l'avant-bras|veine médiane|ulvein/supul|vein|
Brachial veins|Veines brachiales|veines humérales|ulvein/deepul|vein|
Radial veins|Veines radiales||ulvein/deepul|vein|
Deep venous palmar arch|Arcade veineuse palmaire profonde||ulvein/deepul|vein|
Ulnar veins|Veines ulnaires|veines cubitales|ulvein/deepul|vein|
Superficial venous palmar arch|Arcade veineuse palmaire superficielle||ulvein/deepul|vein|
Palmar digital veins|Veines digitales palmaires||ulvein/deepul|vein|-
Cephalic vein|Veine céphalique||ulvein/supul|vein|
Dorsal venous network of hand|Réseau veineux dorsal de la main||ulvein/supul|vein|
Dorsal digital veins of hand|Veines digitales dorsales de la main||ulvein/supul|vein|-
Lateral thoracic vein|Veine thoracique latérale||ulvein/deepul|vein|
Posterior circumflex humeral vein|Veine circonflexe humérale postérieure||ulvein/deepul|vein|-
Subscapular vein|Veine subscapulaire||ulvein/deepul|vein|
Circumflex scapular vein|Veine circonflexe de la scapula||ulvein/deepul|vein|-
Thoracodorsal vein|Veine thoracodorsale||ulvein/deepul|vein|-
External jugular vein|Veine jugulaire externe||headvein/neckv|vein|
Anterior jugular vein|Veine jugulaire antérieure||headvein/neckv|vein|
Posterior auricular vein|Veine auriculaire postérieure||headvein/neckv|vein|-
Posterior division of retromandibular vein|Branche postérieure de la veine rétromandibulaire||headvein/neckv|vein|-
Suprascapular vein|Veine suprascapulaire||headvein/neckv|vein|-
Right subclavian vein|Veine subclavière droite|veine sous-clavière droite|ulvein/deepul|vein|subclavian_vein
Superior vena cava|Veine cave supérieure||trunkvein/vcs|vein|
Azygos vein|Veine azygos|grande veine azygos|trunkvein/vcs|vein|
Accessory hemi-azygos vein|Veine hémi-azygos accessoire|petite azygos supérieure|trunkvein/vcs|vein|
Hemi-azygos vein|Veine hémi-azygos|petite azygos inférieure|trunkvein/vcs|vein|
Left ascending lumbar vein|Veine lombale ascendante gauche||trunkvein/vcs|vein|ascending_lumbar
Left subcostal vein|Veine subcostale gauche||trunkvein/vcs|vein|-
Right ascending lumbar vein|Veine lombale ascendante droite||trunkvein/vcs|vein|ascending_lumbar
Right subcostal vein|Veine subcostale droite||trunkvein/vcs|vein|-
Right superior intercostal vein|Veine intercostale supérieure droite||trunkvein/vcs|vein|-
Right superior phrenic vein|Veine phrénique supérieure droite||trunkvein/vcs|vein|-
Left brachiocephalic vein|Veine brachiocéphalique gauche|tronc veineux brachio-céphalique gauche|trunkvein/vcs|vein|brachiocephalic_vein
Internal thoracic veins|Veines thoraciques internes|veines mammaires internes|trunkvein/vcs|vein|
Musculophrenic veins|Veines musculophréniques||trunkvein/vcs|vein|-
Superior epigastric veins|Veines épigastriques supérieures||trunkvein/vcs|vein|-
Left superior intercostal vein|Veine intercostale supérieure gauche||trunkvein/vcs|vein|-
Vertebral vein|Veine vertébrale||headvein/neckv|vein|
Occipital vein|Veine occipitale||headvein/neckv|vein|-
Right brachiocephalic vein|Veine brachiocéphalique droite|tronc veineux brachio-céphalique droit|trunkvein/vcs|vein|brachiocephalic_vein
"""

# pièces sans nom dans Z-Anatomy : retirées de la page et du modèle
IGNORE = {'?x', '????????'}

GROUPS = {
    'papillary_rv': ('Muscles papillaires du ventricule droit', 'Muscles papillaires du ventricule droit'),
    'tricuspid': ('Valve tricuspide (atrioventriculaire droite)', 'Valve atrioventriculaire droite'),
    'aortic_valve': ('Valve aortique (valvules sigmoïdes)', 'Valve aortique'),
    'pulmonary_valve': ('Valve du tronc pulmonaire (valvules sigmoïdes)', 'Valve du tronc pulmonaire'),
    'common_carotid': ('Artères carotides communes (carotides primitives)', 'Artères carotides communes'),
    'subclavian': ('Artères subclavières (sous-clavières)', 'Artères subclavières'),
    'genicular': ('Artères du genou (articulaires)', 'Artères du genou'),
    'lenticulostriate': ('Rameaux striés latéraux (artères lenticulostriées)', 'Rameaux striés latéraux'),
    'mca_m2': ('Segment M2 de l’artère cérébrale moyenne (insulaire)', 'Segment M2 de l’artère cérébrale moyenne'),
    'mca_m3': ('Segment M3 de l’artère cérébrale moyenne (operculaire)', 'Segment M3 de l’artère cérébrale moyenne'),
    'lv_vein': ('Veines inférieure et postérieure du ventricule gauche', 'Veines inférieure et postérieure du ventricule gauche'),
    'intercavernous': ('Sinus intercaverneux', 'Sinus intercaverneux'),
    'ivc': ('Veine cave inférieure', 'Veine cave inférieure'),
    'subclavian_vein': ('Veines subclavières (sous-clavières)', 'Veines subclavières'),
    'ascending_lumbar': ('Veines lombales ascendantes', 'Veines lombales ascendantes'),
    'brachiocephalic_vein': ('Veines brachiocéphaliques (troncs veineux brachio-céphaliques)', 'Veines brachiocéphaliques'),
}

REGIONS = [
    ('heart', 'Cœur', [('cavities', 'Cavités et muscles papillaires'), ('valves', 'Valves'), ('coronary', 'Vaisseaux coronaires')]),
    ('pulm', 'Circulation pulmonaire', [('partery', 'Artères pulmonaires'), ('pvein', 'Veines pulmonaires')]),
    ('aorta', 'Aorte et ses branches', [('thor', 'Aorte thoracique et arc'), ('abdo', 'Aorte abdominale'), ('digest', 'Artères digestives'), ('pelvis', 'Artères iliaques et du bassin')]),
    ('headart', 'Artères de la tête et du cou', [('extcar', 'Artère carotide externe'), ('intcar', 'Artère carotide interne et ophtalmique'), ('brain', 'Artères de l’encéphale')]),
    ('ulart', 'Artères du membre supérieur', [('subclav', 'Branches de l’artère subclavière'), ('axbr', 'Artères axillaire et brachiale'), ('forearm', 'Avant-bras et main')]),
    ('llart', 'Artères du membre inférieur', [('femoral', 'Artère fémorale'), ('leg', 'Genou et jambe'), ('foot', 'Pied')]),
    ('headvein', 'Veines de la tête et du cou', [('sinus', 'Sinus veineux de la dure-mère'), ('neckv', 'Veines jugulaires et de la face')]),
    ('trunkvein', 'Veines du tronc', [('vcs', 'Veine cave supérieure et azygos'), ('vci', 'Veine cave inférieure et affluents'), ('portal', 'Système porte')]),
    ('ulvein', 'Veines du membre supérieur', [('deepul', 'Veines profondes'), ('supul', 'Veines superficielles')]),
    ('llvein', 'Veines du membre inférieur', [('deepll', 'Veines profondes'), ('supll', 'Veines superficielles')]),
]

TIPS = {
    'all': 'Essentiels : chaque vaisseau une seule fois, côtés réunis ; les fines branches sont dans « Toutes ». Artères en rouge, veines en bleu (l’inverse pour la circulation pulmonaire).',
    'heart': 'Sang pauvre en oxygène : atrium droit → valve tricuspide → ventricule droit → tronc pulmonaire. Sang oxygéné : veines pulmonaires → atrium gauche → valve mitrale → ventricule gauche → aorte.',
    'cavities': 'La paroi du ventricule gauche est environ trois fois plus épaisse que celle du droit. Les muscles papillaires tendent les cordages des valves atrioventriculaires.',
    'valves': 'Deux valves atrioventriculaires (tricuspide à droite, mitrale à gauche) et deux valves artérielles à trois valvules semi-lunaires (aortique et pulmonaire).',
    'coronary': 'Coronaire gauche → interventriculaire antérieure (IVA) et circonflexe. Coronaire droite → face inférieure. Les veines du cœur rejoignent le sinus coronaire, dans l’atrium droit.',
    'pulm': 'Les artères pulmonaires portent le sang pauvre en oxygène vers les poumons ; les quatre veines pulmonaires ramènent le sang oxygéné à l’atrium gauche.',
    'partery': 'Le tronc pulmonaire se divise sous l’arc de l’aorte. Les artères se divisent ensuite comme les bronches : lobaires puis segmentaires.',
    'pvein': 'Quatre veines pulmonaires (deux par poumon, supérieure et inférieure) se jettent dans l’atrium gauche.',
    'aorta': 'Aorte ascendante → arc → aorte thoracique (descendante) → aorte abdominale, qui se divise en artères iliaques communes vers L4.',
    'thor': 'Trois branches de l’arc de l’aorte, de droite à gauche : tronc brachiocéphalique, carotide commune gauche, subclavière gauche.',
    'abdo': 'Branches pariétales (phréniques inférieures, lombales, sacrale médiane) et viscérales paires (rénales, surrénales, testiculaires).',
    'digest': 'Trois artères impaires : tronc cœliaque (vers T12 : foie, estomac, rate), mésentérique supérieure (intestin grêle, côlon droit), mésentérique inférieure (côlon gauche, rectum).',
    'pelvis': 'L’artère iliaque externe devient fémorale sous le ligament inguinal ; l’iliaque interne irrigue le bassin, le périnée et la fesse.',
    'headart': 'Carotide externe : face et cou. Carotide interne : encéphale et œil (artère ophtalmique). Les artères vertébrales s’unissent en artère basilaire.',
    'extcar': 'Branches de la carotide externe : thyroïdienne supérieure, linguale, faciale, pharyngienne ascendante, occipitale, auriculaire postérieure, puis temporale superficielle et maxillaire.',
    'intcar': 'La carotide interne ne donne aucune branche au cou ; dans le crâne, elle donne l’artère ophtalmique puis se termine en artères cérébrales antérieure et moyenne.',
    'brain': 'Cercle artériel du cerveau (polygone de Willis) : cérébrales antérieures et communicante antérieure, carotides internes, communicantes postérieures, cérébrales postérieures.',
    'ulart': 'Subclavière → axillaire (après la 1re côte) → brachiale (après le muscle grand rond) → radiale et ulnaire au pli du coude.',
    'subclav': 'Branches de la subclavière : vertébrale, thoracique interne, tronc thyrocervical, tronc costocervical.',
    'axbr': 'L’artère brachiale se palpe à la face médiale du bras ; c’est là qu’on prend la tension artérielle.',
    'forearm': 'L’arcade palmaire superficielle vient surtout de l’ulnaire, la profonde surtout de la radiale. On prend le pouls à l’artère radiale, au poignet.',
    'llart': 'Iliaque externe → fémorale (sous le ligament inguinal) → poplitée (dans le canal des adducteurs) → tibiales antérieure et postérieure.',
    'femoral': 'L’artère profonde de la cuisse irrigue la cuisse par ses artères perforantes et circonflexes ; la fémorale poursuit vers le genou.',
    'leg': 'L’artère poplitée donne les artères du genou, puis se divise en tibiale antérieure et tronc tibio-fibulaire (tibiale postérieure et fibulaire).',
    'foot': 'Pouls pédieux sur le dos du pied (artère dorsale du pied) ; pouls tibial postérieur derrière la malléole médiale.',
    'headvein': 'Le sang de l’encéphale passe par les sinus de la dure-mère, puis le sinus sigmoïde et la veine jugulaire interne.',
    'sinus': 'Sinus sagittal supérieur → confluent des sinus → sinus transverse → sinus sigmoïde → veine jugulaire interne. Le sinus caverneux entoure la carotide interne.',
    'neckv': 'La veine jugulaire interne rejoint la subclavière pour former la veine brachiocéphalique ; la jugulaire externe se jette dans la subclavière.',
    'trunkvein': 'Deux veines caves rejoignent l’atrium droit. Le système porte ramène le sang des intestins au foie avant la veine cave inférieure.',
    'vcs': 'Les deux veines brachiocéphaliques forment la veine cave supérieure. La veine azygos draine la paroi du thorax et se jette dans la veine cave supérieure.',
    'vci': 'La veine cave inférieure naît de l’union des veines iliaques communes vers L5. La veine rénale gauche passe devant l’aorte (pince aorto-mésentérique).',
    'portal': 'Veine porte = veine splénique + veine mésentérique supérieure (la mésentérique inférieure rejoint en général la splénique).',
    'ulvein': 'Veines profondes doublant les artères (souvent par deux) et veines superficielles sous la peau (céphalique en dehors, basilique en dedans).',
    'deepul': 'Les veines brachiales s’unissent pour former la veine axillaire, qui devient subclavière au bord de la 1re côte.',
    'supul': 'Au pli du coude, la veine intermédiaire du coude relie céphalique et basilique : c’est la veine des prises de sang.',
    'llvein': 'Veines profondes satellites des artères, et deux veines superficielles : grande saphène (en dedans) et petite saphène (en arrière).',
    'deepll': 'La veine poplitée devient fémorale dans le canal des adducteurs, puis iliaque externe sous le ligament inguinal. Lieu des thromboses veineuses profondes.',
    'supll': 'La grande saphène passe devant la malléole médiale et rejoint la veine fémorale à la crosse ; la petite saphène rejoint la veine poplitée.',
}

# ---- réglages du générateur (build_system.py) ----
INVENTORY = 'nq_cardiovascular'
PREFIX = 'v_'
SEPARATE = set()
FEMININE = ['artère', 'veine', 'valve', 'valvule', 'cuspide', 'aorte', 'arcade', 'bifurcation', 'branche', 'grande', 'petite', 'première', 'deuxième']
PLURAL = ['artères', 'veines', 'rameaux', 'muscles', 'sinus']
BACK_IDS = {'Popliteal artery', 'Posterior tibial artery', 'Fibular artery', 'Popliteal vein', 'Posterior tibial veins', 'Fibular veins', 'Small saphenous vein',
            'Inferior gluteal artery', 'Superior gluteal artery', 'Inferior gluteal veins', 'Superior gluteal veins', 'Posterior intercostal arteries',
            'Transverse sinus', 'Sigmoid sinus', 'Straight sinus', 'Occipital sinus', 'Occipital artery', 'Occipital vein', 'Azygos vein', 'Hemi-azygos vein',
            'Accessory hemi-azygos vein', 'Deep brachial artery', 'Posterior circumflex humeral artery', 'Circumflex scapular artery', 'Posterior interosseous artery',
            'Superior lateral genicular artery', 'Superior medial genicular artery', 'Inferior lateral genicular artery', 'Inferior medial genicular artery', 'Middle genicular artery',
            'Genicular veins', 'Deep cervical artery', 'Lumbar arteries', 'Lumbar veins'}

def camera(reg, sub, en, c):
    """Zone de caméra (clés des régions osseuses) et vue de dos éventuelle."""
    cy = c[1]
    if reg in ('heart', 'pulm') or sub in ('thor', 'vcs'): zone = 'torso/ribcage'
    elif sub in ('abdo', 'digest', 'pelvis', 'vci', 'portal'): zone = 'torso/pelvis'
    elif reg in ('headart', 'headvein'): zone = 'head'
    elif reg in ('ulart', 'ulvein'):
        if cy < 0.83: zone = 'hand'
        elif any(w in en for w in ('thoracic', 'intercostal', 'epigastric', 'Musculophrenic')): zone = 'torso/ribcage'
        elif cy > 1.43: zone = 'head'
        else: zone = 'arm'
    else: zone = 'foot' if cy < 0.13 else ('torso/pelvis' if cy > 0.78 else 'leg')
    return zone, 'back' if en in BACK_IDS and zone != 'foot' else ''
