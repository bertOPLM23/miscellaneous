// Modélise les vaisseaux lymphatiques absents de Z-Anatomy : conduits, troncs et collecteurs, tracés comme des tubes
// ancrés sur la géométrie réelle du modèle (axe des veines et artères, centre des groupes de nœuds, vertèbres).
// Usage : node gen_lymph.mjs <lymphatic.glb> <cardiovascular.glb> <skeleton.glb> <sortie.glb>
// Repère : x vers la gauche du corps, y vers le haut, z vers l'avant ; unités en mètres.
import { NodeIO, Document } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import draco3d from 'draco3dgltf';

const [lymphFile, vesselFile, skeletonFile, outFile] = process.argv.slice(2);
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS).registerDependencies({ 'draco3d.decoder': await draco3d.createDecoderModule() });

/* ---------- world-space vertices of every named mesh ---------- */
function mul(a, b) {
  const o = new Array(16).fill(0);
  for (let i = 0; i < 4; i++) for (let j = 0; j < 4; j++) for (let k = 0; k < 4; k++) o[j * 4 + i] += a[k * 4 + i] * b[j * 4 + k];
  return o;
}
const VERTS = new Map();
async function load(file) {
  const doc = await io.read(file);
  const walk = (node, parent) => {
    const m = mul(parent, node.getMatrix());
    const mesh = node.getMesh();
    if (mesh) {
      const pts = VERTS.get(node.getName()) || [];
      for (const prim of mesh.listPrimitives()) {
        const pos = prim.getAttribute('POSITION'), v = [0, 0, 0];
        for (let i = 0; i < pos.getCount(); i++) {
          pos.getElement(i, v);
          pts.push([0, 1, 2].map(r => m[r] * v[0] + m[4 + r] * v[1] + m[8 + r] * v[2] + m[12 + r]));
        }
      }
      VERTS.set(node.getName(), pts);
    }
    for (const c of node.listChildren()) walk(c, m);
  };
  for (const s of doc.getRoot().listScenes()) for (const n of s.listChildren()) walk(n, [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]);
}
await load(lymphFile); await load(vesselFile); await load(skeletonFile);

const pts = (name) => { const p = VERTS.get(name); if (!p || !p.length) throw new Error('repère introuvable : ' + name); return p; };
const add = (a, b) => [a[0] + b[0], a[1] + b[1], a[2] + b[2]];
const lerp = (a, b, t) => [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t];
const mean = (list) => { const s = [0, 0, 0]; for (const p of list) { s[0] += p[0]; s[1] += p[1]; s[2] += p[2]; } return s.map(x => x / list.length); };
const AX = { x: 0, y: 1, z: 2 };
// centre of a mesh
const C = (name) => mean(pts(name));
// point on the axis of a tubular mesh: centre of the slice at fraction t of its extent along an axis (0 = low end)
function P(name, axis, t) {
  const a = AX[axis], p = pts(name);
  let lo = Infinity, hi = -Infinity; for (const v of p) { lo = Math.min(lo, v[a]); hi = Math.max(hi, v[a]); }
  return At(name, axis, lo + (hi - lo) * t);
}
// same, at a given coordinate along the axis (slice 4 mm thick, widened until it holds points)
function At(name, axis, value) {
  const a = AX[axis], p = pts(name);
  for (let w = 0.002; w < 0.05; w *= 1.6) { const s = p.filter(v => Math.abs(v[a] - value) < w); if (s.length >= 3) return mean(s); }
  throw new Error(`coupe vide : ${name} ${axis}=${value}`);
}
// several points along a tubular mesh
const along = (name, axis, t0, t1, n, off = [0, 0, 0]) => Array.from({ length: n }, (_, i) => add(P(name, axis, t0 + (t1 - t0) * i / (n - 1)), off));
const yOf = (bone) => C(bone)[1];

/* ---------- curves and tubes ---------- */
// centripetal Catmull-Rom through the anchors, sampled about every 2.5 mm
function curve(anchors) {
  const P0 = anchors;
  const ext = [lerp(P0[0], P0[1], -0.1), ...P0, lerp(P0[P0.length - 1], P0[P0.length - 2], -0.1)];
  const out = [];
  for (let i = 1; i < ext.length - 2; i++) {
    const [p0, p1, p2, p3] = [ext[i - 1], ext[i], ext[i + 1], ext[i + 2]];
    const d = (a, b) => Math.max(1e-6, Math.sqrt(Math.hypot(b[0] - a[0], b[1] - a[1], b[2] - a[2])));
    const t0 = 0, t1 = t0 + d(p0, p1), t2 = t1 + d(p1, p2), t3 = t2 + d(p2, p3);
    const seg = Math.hypot(p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]);
    const n = Math.max(2, Math.ceil(seg / 0.0025));
    for (let k = 0; k < n; k++) {
      const t = t1 + (t2 - t1) * k / n;
      const A1 = lerp(p0, p1, (t - t0) / (t1 - t0)), A2 = lerp(p1, p2, (t - t1) / (t2 - t1)), A3 = lerp(p2, p3, (t - t2) / (t3 - t2));
      const B1 = lerp(A1, A2, (t - t0) / (t2 - t0)), B2 = lerp(A2, A3, (t - t1) / (t3 - t1));
      out.push(lerp(B1, B2, (t - t1) / (t2 - t1)));
    }
  }
  out.push(P0[P0.length - 1]);
  return out;
}
const sub = (a, b) => [a[0] - b[0], a[1] - b[1], a[2] - b[2]];
const cross = (a, b) => [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]];
const norm = (a) => { const l = Math.hypot(...a) || 1; return a.map(x => x / l); };
// tube along a sampled curve, radius r(u) for u in 0..1, with rounded caps; parallel-transport frames (no twisting)
function tube(points, radius, seg = 8) {
  const pos = [], nrm = [], idx = [];
  const n = points.length;
  let T = norm(sub(points[1], points[0]));
  let N = norm(cross(T, Math.abs(T[1]) < 0.9 ? [0, 1, 0] : [1, 0, 0]));
  const len = [0]; for (let i = 1; i < n; i++) len.push(len[i - 1] + Math.hypot(...sub(points[i], points[i - 1])));
  const total = len[n - 1] || 1;
  for (let i = 0; i < n; i++) {
    const Ti = norm(sub(points[Math.min(n - 1, i + 1)], points[Math.max(0, i - 1)]));
    N = norm(sub(N, Ti.map(x => x * (N[0] * Ti[0] + N[1] * Ti[1] + N[2] * Ti[2]))));   // carry the frame along: no twist
    T = Ti; const Bn = norm(cross(T, N));
    const r = radius(len[i] / total);
    for (let k = 0; k < seg; k++) {
      const a = 2 * Math.PI * k / seg, c = Math.cos(a), s = Math.sin(a);
      const dir = [N[0] * c + Bn[0] * s, N[1] * c + Bn[1] * s, N[2] * c + Bn[2] * s];
      pos.push(...add(points[i], dir.map(x => x * r))); nrm.push(...dir);
    }
  }
  for (let i = 0; i < n - 1; i++) for (let k = 0; k < seg; k++) {
    const a = i * seg + k, b = i * seg + (k + 1) % seg, c = a + seg, d = b + seg;
    idx.push(a, c, b, b, c, d);
  }
  // caps: a point at each end
  for (const [i, sign] of [[0, -1], [n - 1, 1]]) {
    const ci = pos.length / 3; const tdir = norm(sub(points[Math.min(n - 1, i + (sign > 0 ? 0 : 1))], points[Math.max(0, i - (sign > 0 ? 1 : 0))]));
    pos.push(...add(points[i], tdir.map(x => x * radius(i ? 1 : 0) * sign * 0.6))); nrm.push(...tdir.map(x => x * sign));
    for (let k = 0; k < seg; k++) { const a = i * seg + k, b = i * seg + (k + 1) % seg; if (sign < 0) idx.push(ci, a, b); else idx.push(ci, b, a); }
  }
  return { pos, nrm, idx };
}
const R = (r0, r1 = r0) => (u) => r0 + (r1 - r0) * u;

/* ---------- the vessels ---------- */
// Each entry: name (as a Z-Anatomy-style name, .l/.r for paired ones) -> list of curves (anchor lists) and a radius profile.
const V = [];
const vessel = (name, curves, radius) => V.push({ name, curves, radius });

// landmarks
const Ao = 'Abdominal aorta', AoT = 'Thoracic aorta', Az = 'Azygos vein';
const angle = (s) => P(`Internal jugular vein.${s}`, 'y', 0.02);            // venous angle: lower end of the internal jugular vein
const yL2 = yOf('l2'), yL1 = yOf('l1'), yT12 = yOf('t12');
// cisterna chyli: in front of L1-L2, behind and to the right of the aorta
const cisLow = add(At(Ao, 'y', yL2), [-0.012, 0, -0.013]);
const cisHigh = add(At(Ao, 'y', (yL1 + yT12) / 2), [-0.010, 0, -0.014]);
vessel('Cisterna chyli', [[cisLow, lerp(cisLow, cisHigh, 0.5), cisHigh]], (u) => 0.0025 + 0.0025 * Math.sin(Math.PI * Math.min(1, Math.max(0, u * 1.1 - 0.05))));
// thoracic duct: aortic hiatus, then between aorta (left) and azygos vein (right), crosses to the left at T5,
// rises along the left of the oesophagus, arches over the subclavian artery and ends at the left venous angle
// anterior surface of the vertebral body nearest to height y, at lateral position x
const VERTEBRAE = ['c7', 't1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 'l1', 'l2'];
function vbFront(y, x) {
  const v = VERTEBRAE.reduce((b, n) => Math.abs(yOf(n) - y) < Math.abs(yOf(b) - y) ? n : b, VERTEBRAE[0]);
  const s = pts(v).filter(p => Math.abs(p[0] - x) < 0.01 && Math.abs(p[1] - yOf(v)) < 0.006);
  return Math.max(...s.map(p => p[2]));
}
// between aorta (left) and azygos vein (right), just in front of the vertebral bodies
const mid = (y) => { const a = At(y > yOf('t4') ? 'Aortic arch' : AoT, 'y', y), z = At(Az, 'y', y), x = (a[0] + z[0]) / 2; return [x, y, vbFront(y, x) + 0.003]; };
const t = (b) => C(b), aL = angle('l');
const pre = (b, dx, dz = 0.003) => { const x = t(b)[0] + dx; return [x, yOf(b), vbFront(yOf(b), t(b)[0] + Math.max(-0.01, Math.min(0.01, dx))) + dz]; };   // front measured on the body, not the transverse process
const tdPts = [
  cisHigh, add(At(Ao, 'y', yT12), [-0.006, 0.006, -0.012]),
  mid(yOf('t10')), mid(yOf('t8')), mid(yOf('t6')),
  pre('t5', 0.004), pre('t4', 0.008), pre('t3', 0.013), pre('t1', 0.019, 0.006),
  [t('c7')[0] + 0.028, yOf('c7') + 0.004, t('c7')[2] + 0.030],
  add(aL, [0.006, 0.012, -0.004]), add(aL, [0.002, 0.003, -0.002]),
];
vessel('Thoracic duct', [tdPts], (u) => u > 0.93 ? 0.0024 + (u - 0.93) * 0.012 : 0.0019);
// right lymphatic duct: short, at the right venous angle
const aR = angle('r'), rldStart = add(aR, [-0.010, 0.008, -0.006]);
vessel('Right lymphatic duct', [[rldStart, add(aR, [-0.005, 0.004, -0.003]), add(aR, [-0.001, 0.001, -0.001])]], R(0.0022, 0.0026));
const trunkEnd = (s) => s === 'l' ? [add(aL, [0.010, 0.016, -0.005]), add(aL, [0.006, 0.012, -0.004])] : [add(rldStart, [-0.004, 0.004, -0.002]), rldStart];

for (const s of ['l', 'r']) {
  const sx = s === 'l' ? 1 : -1, ij = `Internal jugular vein.${s}`;
  // jugular trunk: from the inferior deep lateral cervical nodes, behind and outside the internal jugular vein
  const n0 = C(`Inferior deep lateral cervical nodes.${s}`);
  vessel(`Jugular trunk.${s}`, [[n0, add(At(ij, 'y', n0[1] - 0.012), [sx * 0.006, 0, -0.006]), ...trunkEnd(s)]], R(0.0012));
  // subclavian trunk: from the apical axillary nodes, above and behind the subclavian vein
  const sv = s === 'l' ? 'Left subclavian vein' : 'Right subclavian vein';
  vessel(`Subclavian trunk.${s}`, [[C(`Apical axillary nodes.${s}`), ...[0.75, 0.45].map(f => add(P(sv, 'x', s === 'l' ? f : 1 - f), [0, 0.005, -0.006])), ...trunkEnd(s)]], R(0.0012));
  // bronchomediastinal trunk: from the tracheobronchial and paratracheal nodes, up beside the trachea
  const tb = C('Superior tracheobronchial nodes'), pt = C('Paratracheal thoracic nodes');
  vessel(`Bronchomediastinal trunk.${s}`, [[add(tb, [sx * 0.012, 0, 0]), add(pt, [sx * 0.014, 0.004, 0]), add(pt, [sx * 0.018, 0.030, 0.006]), ...trunkEnd(s)]], R(0.0012));
  // lumbar trunk: from the common iliac nodes, up beside the aorta to the cisterna
  const ci = C('Intermediate common iliac nodes');
  vessel(`Lumbar trunk.${s}`, [[add(ci, [sx * 0.014, 0, -0.004]), add(At(Ao, 'y', yOf('l4')), [sx * 0.015, 0, -0.008]), add(At(Ao, 'y', yOf('l3')), [sx * 0.014, 0, -0.010]), add(cisLow, [sx > 0 ? 0.008 : -0.002, -0.006, 0])]], R(0.0013));
}
// intestinal trunk: from the pre-aortic nodes, around the right side of the aorta to the cisterna
{ const pa = C('Pre-aortic nodes'), a = At(Ao, 'y', pa[1]);
  vessel('Intestinal trunk', [[pa, [a[0] - 0.013, pa[1] - 0.004, a[2]], add(cisLow, [-0.002, 0.004, 0.004])]], R(0.0014)); }

/* collecting vessels (one bundle per pathway, drawn as one or a few tubes) */
for (const s of ['l', 'r']) {
  const sx = s === 'l' ? 1 : -1;
  const L = (n) => C(`${n}.${s}`);
  // lower limb, superficial medial bundle: along the great saphenous vein to the inferior superficial inguinal nodes
  vessel(`Superficial medial collecting lymphatics of lower limb.${s}`, [[...along(`Great saphenous vein.${s}`, 'y', 0.02, 0.93, 9, [0, 0, 0.004]), L('Inferior superficial inguinal nodes')]], R(0.0007));
  // lower limb, superficial lateral bundle: along the small saphenous vein to the superficial popliteal nodes
  vessel(`Superficial lateral collecting lymphatics of lower limb.${s}`, [[...along(`Small saphenous vein.${s}`, 'y', 0.03, 0.9, 7, [0, 0, -0.004]), L('Superficial popliteal nodes')]], R(0.0007));
  // leg, deep: along the posterior tibial veins and the anterior tibial veins to the popliteal nodes
  vessel(`Deep collecting lymphatics of leg.${s}`, [
    [...along(`Posterior tibial veins.${s}`, 'y', 0.05, 0.9, 6, [0, 0, -0.003]), L('(Posterior tibial node)'), L('Deep popliteal nodes')],
    [...along(`Anterior tibial veins.${s}`, 'y', 0.05, 0.9, 6, [0, 0, 0.003]), L('(Anterior tibial node)'), L('Deep popliteal nodes')],
  ], R(0.0007));
  // thigh, deep: popliteal nodes along the femoral vein to the deep inguinal nodes
  vessel(`Deep collecting lymphatics of thigh.${s}`, [[L('Deep popliteal nodes'), ...along(`Femoral vein.${s}`, 'y', 0.06, 0.9, 7, [sx * 0.004, 0, -0.003]), L('(Proximal deep inguinal node)')]], R(0.0008));
  // pelvis: inguinal nodes along the external iliac vessels to the common iliac nodes
  const ci = add(C('Intermediate common iliac nodes'), [sx * 0.012, 0, 0]);
  vessel(`External iliac collecting lymphatics.${s}`, [[L('Superolateral superficial inguinal nodes'), L('(Proximal deep inguinal node)'), L('(Lateral lacunar node)'),
    ...along(`External iliac vein.${s}`, 'y', 0.3, 0.8, 3, [sx * 0.005, 0, 0.003]), L('Intermediate external iliac nodes'), ci]], R(0.0008));
  vessel(`Internal iliac collecting lymphatics.${s}`, [[L('Obturator nodes'), L('Inferior gluteal nodes'), add(P(`Internal iliac vein.${s}`, 'y', 0.6), [0, 0, 0.004]), ci],
    [L('Lateral sacral nodes'), L('Superior gluteal nodes'), add(P(`Internal iliac vein.${s}`, 'y', 0.85), [0, 0, 0.004]), ci]], R(0.0008));
  // upper limb: basilic bundle (cubital nodes), cephalic bundle (deltopectoral nodes), deep bundle (brachial veins)
  const hand = C(`Dorsal venous network of hand.${s}`);
  vessel(`Superficial medial collecting lymphatics of upper limb.${s}`, [[hand, ...along(`Basilic vein.${s}`, 'y', 0.04, 0.45, 4, [0, 0, 0.003]), L('Cubital nodes'),
    ...along(`Basilic vein.${s}`, 'y', 0.7, 0.97, 3, [0, 0, 0.003]), L('Lateral axillary nodes')]], R(0.0007));
  vessel(`Superficial lateral collecting lymphatics of upper limb.${s}`, [[hand, ...along(`Cephalic vein.${s}`, 'y', 0.04, 0.92, 8, [0, 0, 0.003]), L('Infraclavicular nodes'), L('Apical axillary nodes')]], R(0.0007));
  vessel(`Deep collecting lymphatics of upper limb.${s}`, [[...along(`Radial veins.${s}`, 'y', 0.1, 0.9, 4, [0, 0, -0.003]), ...along(`Brachial veins.${s}`, 'y', 0.05, 0.92, 6, [0, 0, -0.004]), L('Lateral axillary nodes')]], R(0.0007));
  vessel(`Axillary collecting lymphatics.${s}`, [[L('Lateral axillary nodes'), L('Central axillary nodes'), L('Apical axillary nodes')],
    [L('Anterior axillary nodes'), L('Central axillary nodes')], [L('Posterior axillary nodes'), L('Central axillary nodes')]], R(0.0009));
  // head and neck
  vessel(`Deep cervical collecting lymphatics.${s}`, [[L('Jugulodigastric node'), L('Lateral superior jugular node'), add(At(`Internal jugular vein.${s}`, 'y', 1.465), [sx * 0.005, 0, -0.004]), L('Inferior deep lateral cervical nodes')]], R(0.0009));
  vessel(`Posterior superficial collecting lymphatics of head.${s}`, [[L('Occipital nodes'), L('Mastoid nodes'), L('Infra-auricular nodes'), L('Jugulodigastric node')],
    [L('Pre-auricular nodes'), L('Superficial parotid nodes'), L('Infra-auricular nodes')]], R(0.0007));
  vessel(`Anterior superficial collecting lymphatics of head.${s}`, [[L('Nasolabial node'), L('Bucinator node'), L('Mandibular node'), L('Submandibular nodes'), L('Jugulodigastric node')],
    [L('Submental nodes'), L('Submandibular nodes')]], R(0.0007));
  vessel(`Superficial cervical collecting lymphatics.${s}`, [[L('Superficial lateral cervical nodes'), L('Supraclavicular nodes'), L('Inferior deep lateral cervical nodes')]], R(0.0007));
  // thorax: parasternal chain along the internal thoracic vessels; intercostal collectors to the thoracic duct
  vessel(`Parasternal collecting lymphatics.${s}`, [[...along(`Internal thoracic veins.${s}`, 'y', 0.05, 0.92, 7, [sx * 0.003, 0, 0.002]), add(angle(s), [-sx * 0.004, -0.004, 0.004])]], R(0.0008));
  vessel(`Intercostal collecting lymphatics.${s}`, [[add(L('Intercostal nodes'), [sx * 0.03, -0.01, 0]), L('Intercostal nodes'), mid(yOf('t6'))]], R(0.0007));
}
// abdomen: mesenteric and coeliac pathways to the pre-aortic nodes
vessel('Mesenteric collecting lymphatics', [[C('Juxta-intestinal mesenteric nodes'), C('Paracolic superior mesenteric nodes'), C('Central superior mesenteric nodes'), C('Pre-aortic nodes')],
  [C('Ileocolic nodes'), C('Central superior mesenteric nodes')]], R(0.0008));
vessel('Coeliac collecting lymphatics', [[C('Splenic nodes'), C('Superior pancreatic nodes'), C('Coeliac nodes'), C('Pre-aortic nodes')],
  [C('Right gastro-omental nodes'), C('(Subpyloric nodes)'), C('Coeliac nodes')]], R(0.0008));

/* ---------- write the meshes ---------- */
const doc = new Document(); const buf = doc.createBuffer(); const scene = doc.createScene();
const mat = doc.createMaterial('lymph');
let tris = 0;
for (const v of V) {
  const pos = [], nrm = [], idx = [];
  for (const c of v.curves) {
    const g = tube(curve(c), v.radius); const off = pos.length / 3;
    pos.push(...g.pos); nrm.push(...g.nrm); idx.push(...g.idx.map(i => i + off));
  }
  tris += idx.length / 3;
  const prim = doc.createPrimitive().setMaterial(mat)
    .setAttribute('POSITION', doc.createAccessor().setType('VEC3').setArray(new Float32Array(pos)).setBuffer(buf))
    .setAttribute('NORMAL', doc.createAccessor().setType('VEC3').setArray(new Float32Array(nrm)).setBuffer(buf))
    .setIndices(doc.createAccessor().setType('SCALAR').setArray(new Uint32Array(idx)).setBuffer(buf));
  scene.addChild(doc.createNode(v.name).setMesh(doc.createMesh(v.name).addPrimitive(prim)));
}
await new NodeIO().write(outFile, doc);
console.log(`${V.length} vaisseaux modélisés, ${tris} triangles`);
