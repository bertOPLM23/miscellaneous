// Fusionne les nœuds et organes Z-Anatomy avec les vaisseaux modélisés : node merge.mjs a.glb b.glb sortie.glb
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import { mergeDocuments, unpartition } from '@gltf-transform/functions';
import draco3d from 'draco3dgltf';
const [a, b, out] = process.argv.slice(2);
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS).registerDependencies({ 'draco3d.decoder': await draco3d.createDecoderModule() });
const doc = await io.read(a);
for (const e of doc.getRoot().listExtensionsUsed()) if (e.extensionName === 'KHR_draco_mesh_compression') e.dispose();
mergeDocuments(doc, await io.read(b));
const scenes = doc.getRoot().listScenes();
for (const s of scenes.slice(1)) { for (const n of s.listChildren()) scenes[0].addChild(n); s.dispose(); }
await doc.transform(unpartition());
await io.write(out, doc);
console.log('ok', doc.getRoot().listNodes().length, 'nœuds');
