// Inventaire d'un GLB : nœuds maillés, triangles, hiérarchie (collections), boîte englobante monde.
// Usage : node inventory.mjs fichier.glb sortie.json
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import fs from 'fs';
import draco3d from 'draco3dgltf';

const [file, out] = process.argv.slice(2);
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS).registerDependencies({ 'draco3d.decoder': await draco3d.createDecoderModule() });
const doc = await io.read(file);
const root = doc.getRoot();

function mul(a, b) {
  const o = new Array(16).fill(0);
  for (let i = 0; i < 4; i++) for (let j = 0; j < 4; j++) for (let k = 0; k < 4; k++) o[j * 4 + i] += a[k * 4 + i] * b[j * 4 + k];
  return o;
}
const ident = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1];
const meshes = [];
const gmin = [Infinity, Infinity, Infinity], gmax = [-Infinity, -Infinity, -Infinity];

function walk(node, parentM, path) {
  const m = mul(parentM, node.getMatrix());
  const p = [...path, node.getName()];
  const mesh = node.getMesh();
  if (mesh) {
    let tris = 0;
    const mn = [Infinity, Infinity, Infinity], mx = [-Infinity, -Infinity, -Infinity];
    for (const prim of mesh.listPrimitives()) {
      const pos = prim.getAttribute('POSITION');
      const idx = prim.getIndices();
      tris += (idx ? idx.getCount() : pos.getCount()) / 3;
      const v = [0, 0, 0];
      for (let i = 0; i < pos.getCount(); i += Math.max(1, Math.floor(pos.getCount() / 200))) {
        pos.getElement(i, v);
        const w = [0, 1, 2].map(r => m[r] * v[0] + m[4 + r] * v[1] + m[8 + r] * v[2] + m[12 + r]);
        for (let r = 0; r < 3; r++) { mn[r] = Math.min(mn[r], w[r]); mx[r] = Math.max(mx[r], w[r]); gmin[r] = Math.min(gmin[r], w[r]); gmax[r] = Math.max(gmax[r], w[r]); }
      }
    }
    meshes.push({ name: node.getName(), path: p.slice(0, -1).join(' / '), tris, min: mn, max: mx });
  }
  for (const c of node.listChildren()) walk(c, m, p);
}
for (const scene of root.listScenes()) for (const n of scene.listChildren()) walk(n, ident, []);

const res = {
  file, meshes: meshes.length, triangles: meshes.reduce((s, x) => s + x.tris, 0),
  bbox: { min: gmin, max: gmax }, list: meshes,
};
fs.writeFileSync(out, JSON.stringify(res, null, 1));
console.log(file, 'meshes', res.meshes, 'tris', Math.round(res.triangles), 'bbox', gmin.map(x => x.toFixed(3)), gmax.map(x => x.toFixed(3)));
