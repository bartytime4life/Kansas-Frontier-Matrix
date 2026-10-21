import { THREE, HALF, terrain, liveSurface, blockSides, riverWater, heroCamera, stage, orbit, glowPoints, scanCurtain, smooth, window01, lerp, easeInOut } from './kit.mjs';
// Terrain & elevation: the surface assembles from elevation, a circling sun
// re-lights the hillshade, then a colour ramp and contours map elevation.

export function create() {
 const scene = new THREE.Scene(), camera = heroCamera();
 const { key, hemi } = stage(scene, { fog: .022 });
 const land = terrain({ segments: 256 });
 const u = liveSurface(land);
 const sides = blockSides(land.sample);
 const water = riverWater(land.sample);
 sides.traverse(o => { if (o.material) { o.material.transparent = true; } });
 scene.add(land.mesh, sides, water);

 // Survey lattice that the elevation build sweeps across.
 const lattice = terrain({ segments: 56, material: { wireframe: true, color: '#86dcf0', vertexColors: false, transparent: true, opacity: 0, emissive: '#2c7f99', emissiveIntensity: 1 } });
 const lu = liveSurface(lattice);
 lattice.mesh.position.y = .015;
 scene.add(lattice.mesh);
 const curtain = scanCurtain({ height: 2.6 });
 scene.add(curtain);

 // Sun: a bright point riding a faint dial at the horizon, with a ray to the land.
 const sun = glowPoints(1, { size: 3.2, color: '#ffd89a', depthTest: false });
 const dial = new THREE.Mesh(new THREE.RingGeometry(9.2, 9.26, 180), new THREE.MeshBasicMaterial({ color: '#f0cf8a', transparent: true, opacity: 0, side: THREE.DoubleSide, depthWrite: false }));
 dial.rotation.x = -Math.PI / 2; dial.position.y = .2;
 const rayGeo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(0, .8, 0), new THREE.Vector3()]);
 const ray = new THREE.Line(rayGeo, new THREE.LineBasicMaterial({ color: '#ffd89a', transparent: true, opacity: 0, depthWrite: false }));
 scene.add(sun, dial, ray);
 const sunDir = new THREE.Vector3(), rest = new THREE.Vector3(6, 9, 4).normalize(), dir = new THREE.Vector3();

 function update(t) {
  // Beat 1 (0–6 s): a scan front raises the surface west → east under a lattice.
  const build = easeInOut(smooth(.3, 5.2, t));
  u.sweep.value = lu.sweep.value = lerp(-HALF - 1.6, HALF + 1.6, build);
  curtain.at(u.sweep.value - .1);
  curtain.material.opacity = window01(t, .2, 5.6, .5) * .8;
  lattice.mesh.material.opacity = window01(t, 0, 6.4, 1) * .2;
  const solid = smooth(4.6, 6, t) * (1 - smooth(17.4, 18, t));
  sides.traverse(o => { if (o.material) o.material.opacity = solid; });
  sides.visible = solid > .01;
  water.material.opacity = smooth(4.8, 6.2, t) * .93;

  // Beat 2 (6–12 s): grey hillshade under a sun sweeping azimuth and altitude.
  const shade = window01(t, 5.6, 12.6, 1.1);
  u.grey.value = shade * .62;
  const p = smooth(5.8, 12.4, t);
  const az = -2.2 + p * Math.PI * 2.1, alt = lerp(.12, .95, .5 + .5 * Math.sin(p * Math.PI * 2 - Math.PI / 2));
  sunDir.set(Math.cos(az) * Math.cos(alt), Math.sin(alt), Math.sin(az) * Math.cos(alt));
  dir.copy(rest).lerp(sunDir, shade).normalize();
  key.position.copy(dir).multiplyScalar(14);
  key.intensity = lerp(2.4, 2.9, shade);
  hemi.intensity = lerp(.9, .22, shade);
  const sx = sunDir.x * 9.2, sy = Math.max(.6, sunDir.y * 9.2), sz = sunDir.z * 9.2;
  sun.positions.set([sx, sy, sz]); sun.alphas[0] = shade; sun.commit();
  dial.material.opacity = shade * .3;
  rayGeo.attributes.position.setXYZ(1, sx, sy, sz); rayGeo.attributes.position.needsUpdate = true;
  ray.material.opacity = shade * .35;

  // Beat 3 (12–18 s): hypsometric colour, contours and a pulse of exaggeration.
  u.hypso.value = window01(t, 11.6, 18.4, 1.2);
  u.contour.value = smooth(12.6, 14, t) * (1 - smooth(17.2, 18, t));
  const k = 1 + .75 * Math.sin(smooth(13.6, 17.4, t) * Math.PI);
  u.relief.value = lu.relief.value = k;
  sides.scale.y = water.scale.y = k;

  orbit(camera, t, { radius: 21.5, height: lerp(11, 9, smooth(6, 12, t) * (1 - smooth(16, 18, t))), target: [0, -.7, 0], start: -.95 + .32 * Math.sin(t / 18 * Math.PI * 2), speed: 0 }); // sway, so the loop restarts seamlessly
 }
 update(0);
 return { scene, camera, update, dispose() { rayGeo.dispose(); } };
}
