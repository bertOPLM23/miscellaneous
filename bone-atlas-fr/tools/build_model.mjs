// Prépare le modèle d'un système pour la page : renomme les nœuds (identifiants de la page), retire tout le reste,
// simplifie les maillages et compresse (quantification + EXT_meshopt_compression).
// Usage : node build_model.mjs entrée.glb renommage.json sortie.glb ratio erreur
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import { weld, simplify, quantize, meshopt, prune, dedup, reorder, joinPrimitives } from '@gltf-transform/functions';
import { MeshoptSimplifier, MeshoptEncoder, MeshoptDecoder } from 'meshoptimizer';
import draco3d from 'draco3dgltf';
import fs from 'fs';

const [input, renameFile, output, ratioArg, errorArg] = process.argv.slice(2);
const rename = JSON.parse(fs.readFileSync(renameFile, 'utf8'));
await Promise.all([MeshoptSimplifier.ready, MeshoptEncoder.ready, MeshoptDecoder.ready]);
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS).registerDependencies({
  'draco3d.decoder': await draco3d.createDecoderModule(), 'meshopt.encoder': MeshoptEncoder, 'meshopt.decoder': MeshoptDecoder,
});
const doc = await io.read(input);
const root = doc.getRoot();
for (const ext of root.listExtensionsUsed()) if (ext.extensionName === 'KHR_draco_mesh_compression') ext.dispose();

// one plain material: the page sets its own colours
const mat = doc.createMaterial('structure');
let kept = 0, dropped = 0;
for (const node of root.listNodes()) {
  const id = rename[node.getName()];
  if (!id || !node.getMesh()) { if (!node.listChildren().length) { node.dispose(); dropped++; } continue; }
  node.setName(id); node.setExtras({}); kept++;
}
for (const mesh of root.listMeshes()) { mesh.setExtras({}); for (const p of mesh.listPrimitives()) { p.setMaterial(mat); for (const s of p.listSemantics()) if (s !== 'POSITION' && s !== 'NORMAL') p.setAttribute(s, null); } }
for (const m of root.listMaterials()) if (m !== mat) m.dispose();
// one primitive per mesh, so each structure loads as a single three.js mesh named after it
for (const mesh of root.listMeshes()) {
  const prims = mesh.listPrimitives();
  if (prims.length < 2) continue;
  for (const p of prims) if (!p.getIndices()) { const n = p.getAttribute('POSITION').getCount(); const idx = doc.createAccessor().setType('SCALAR').setArray(new Uint32Array([...Array(n).keys()])); p.setIndices(idx); }
  const joined = joinPrimitives(prims);
  for (const p of prims) { mesh.removePrimitive(p); p.dispose(); }
  mesh.addPrimitive(joined);
}

const tris = () => root.listMeshes().reduce((n, m) => n + m.listPrimitives().reduce((k, p) => k + (p.getIndices() ? p.getIndices().getCount() : p.getAttribute('POSITION').getCount()) / 3, 0), 0);
const before = tris();
await doc.transform(
  prune(), dedup(),
  weld(),
  simplify({ simplifier: MeshoptSimplifier, ratio: Number(ratioArg), error: Number(errorArg) }),
  reorder({ encoder: MeshoptEncoder }),
  quantize({ quantizePosition: 14, quantizeNormal: 8 }),
  meshopt({ encoder: MeshoptEncoder, level: 'high' }),
  prune(),
);
// quantize() moves the mesh of a node that has children (a structure with another nested under it) onto a new
// unnamed child: give that child the structure's name, so the page finds it
for (const node of root.listNodes()) {
  const par = node.getParentNode();
  if (node.getMesh() && !node.getName() && par) { node.setName(par.getName()); par.setName(par.getName() + '.group'); }   // three.js would rename a duplicate
}
await io.write(output, doc);
console.log(`nœuds gardés ${kept}, retirés ${dropped} ; triangles (maillages uniques) ${Math.round(before)} -> ${Math.round(tris())} ; ${(fs.statSync(output).size / 1e6).toFixed(2)} Mo`);
