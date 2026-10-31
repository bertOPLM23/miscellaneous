// Vérifie le tracé des vaisseaux modélisés par rapport aux repères (mesures en mm).
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import draco3d from 'draco3dgltf';
const [lymphV, vessels, skel] = process.argv.slice(2);
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS).registerDependencies({ 'draco3d.decoder': await draco3d.createDecoderModule() });
const V = new Map();
const mul = (a, b) => { const o = new Array(16).fill(0); for (let i = 0; i < 4; i++) for (let j = 0; j < 4; j++) for (let k = 0; k < 4; k++) o[j * 4 + i] += a[k * 4 + i] * b[j * 4 + k]; return o; };
for (const f of [lymphV, vessels, skel]) {
  const doc = await io.read(f);
  const walk = (n, pm) => { const m = mul(pm, n.getMatrix()); if (n.getMesh()) { const P = V.get(n.getName()) || []; for (const pr of n.getMesh().listPrimitives()) { const a = pr.getAttribute('POSITION'), v = [0, 0, 0]; for (let i = 0; i < a.getCount(); i++) { a.getElement(i, v); P.push([0, 1, 2].map(r => m[r] * v[0] + m[4 + r] * v[1] + m[8 + r] * v[2] + m[12 + r])); } } V.set(n.getName(), P); } for (const c of n.listChildren()) walk(c, m); };
  for (const s of doc.getRoot().listScenes()) for (const n of s.listChildren()) walk(n, [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]);
}
const slice = (name, y, w = 0.003) => V.get(name).filter(p => Math.abs(p[1] - y) < w);
const mean = (l) => l.reduce((s, p) => [s[0] + p[0], s[1] + p[1], s[2] + p[2]], [0, 0, 0]).map(x => x / l.length);
const cy = (n) => mean(V.get(n))[1];
console.log('Conduit thoracique, à chaque vertèbre : x conduit / x aorte / x azygos ; z conduit - z face antérieure du corps vertébral');
for (const b of ['t11', 't10', 't8', 't6', 't5', 't4', 't3', 't1']) {
  const y = cy(b), td = slice('Thoracic duct', y, 0.004); if (!td.length) { console.log(b, 'pas de conduit'); continue; }
  const T = mean(td), ao = slice(y > cy('t4') ? 'Aortic arch' : 'Thoracic aorta', y, 0.004), az = slice('Azygos vein', y, 0.004);
  const vb = V.get(b).filter(p => Math.abs(p[0] - T[0]) < 0.01 && Math.abs(p[1] - y) < 0.006);
  const front = vb.length ? Math.max(...vb.map(p => p[2])) : NaN;
  console.log(b.padEnd(4), (T[0] * 1000).toFixed(0).padStart(4), ao.length ? (mean(ao)[0] * 1000).toFixed(0).padStart(5) : '    -', az.length ? (mean(az)[0] * 1000).toFixed(0).padStart(5) : '    -', '  devant le corps vertébral de', ((T[2] - front) * 1000).toFixed(1), 'mm');
}
// distance moyenne des collecteurs à leur veine (sur la partie qui la longe)
const near = (A, B) => { const ds = []; for (let i = 0; i < A.length; i += 23) { let d = Infinity; for (let j = 0; j < B.length; j += 3) { const q = B[j]; d = Math.min(d, Math.hypot(A[i][0] - q[0], A[i][1] - q[1], A[i][2] - q[2])); } ds.push(d); } ds.sort((a, b) => a - b); return 'médiane ' + (ds[ds.length >> 1] * 1000).toFixed(1); };
for (const [c, v] of [['Superficial medial collecting lymphatics of lower limb.l', 'Great saphenous vein.l'], ['Superficial lateral collecting lymphatics of lower limb.l', 'Small saphenous vein.l'],
  ['Deep collecting lymphatics of thigh.l', 'Femoral vein.l'], ['Superficial lateral collecting lymphatics of upper limb.l', 'Cephalic vein.l'], ['Superficial medial collecting lymphatics of upper limb.l', 'Basilic vein.l'],
  ['Jugular trunk.l', 'Internal jugular vein.l'], ['Parasternal collecting lymphatics.l', 'Internal thoracic veins.l'], ['Thoracic duct', 'Azygos vein']])
  console.log('distance moyenne', c, '→', v, ':', near(V.get(c), V.get(v)), 'mm');
// fin du conduit thoracique et du conduit droit : distance à la jonction jugulaire interne / subclavière
const end = (name, ij) => { const P = V.get(name); const top = P.reduce((b, p) => p[1] < b[1] ? b : b, P[0]); const ijv = V.get(ij); const low = ijv.reduce((b, p) => p[1] < b[1] ? p : b, ijv[0]); let d = Infinity; for (const p of P) d = Math.min(d, Math.hypot(p[0] - low[0], p[1] - low[1], p[2] - low[2])); return (d * 1000).toFixed(1); };
console.log('conduit thoracique → bas de la jugulaire interne gauche :', end('Thoracic duct', 'Internal jugular vein.l'), 'mm');
console.log('conduit lymphatique droit → bas de la jugulaire interne droite :', end('Right lymphatic duct', 'Internal jugular vein.r'), 'mm');
