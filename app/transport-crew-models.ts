import * as THREE from "three";
/** Original procedural models; metres throughout. Representative equipment,
 * not a reconstruction of a particular contractor, machine or workforce. */
const paint = (color: number, metalness = .15, roughness = .75) => new THREE.MeshStandardMaterial({ color, metalness, roughness, side: THREE.DoubleSide });
export function createTransportCrew(mode: "road" | "rail", year: number, workers: boolean) {
  const yellow = paint(0xc98c27), edge = paint(0x78521f), rubber = paint(0x202329), steel = paint(0x737d80, .75, .35), glass = paint(0x2b454c, .45, .23), vest = paint(0xe69034), skin = paint(0xad8061);
  const group = new THREE.Group();
  const animated: { object: THREE.Object3D; kind: "arm" | "wheel" | "worker"; phase: number }[] = [];
  function box(parent: THREE.Object3D, dimensions: number[], position: number[], material: THREE.Material) {
    const mesh = new THREE.Mesh(new THREE.BoxGeometry(...dimensions as [number, number, number]), material);
    mesh.position.set(...position as [number, number, number]); parent.add(mesh); return mesh;
  }
  function cylinder(parent: THREE.Object3D, radius: number, length: number, position: number[], material: THREE.Material, axis: "y" | "z" = "y") {
    const mesh = new THREE.Mesh(new THREE.CylinderGeometry(radius, radius, length, 16), material);
    if (axis === "z") mesh.rotation.x = Math.PI / 2;
    mesh.position.set(...position as [number, number, number]); parent.add(mesh); return mesh;
  }
  function rod(parent: THREE.Object3D, a: THREE.Vector3, b: THREE.Vector3, radius: number, material: THREE.Material) {
    const mesh = new THREE.Mesh(new THREE.CylinderGeometry(radius, radius, a.distanceTo(b), 10), material);
    mesh.position.copy(a).add(b).multiplyScalar(.5);
    mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), b.clone().sub(a).normalize()); parent.add(mesh);
  }
  // Fine, deterministic aggregate noise is an original material, not imagery.
  const pixels = new Uint8Array(128 * 128 * 4);
  let seed = 907;
  for (let i = 0; i < 128 * 128; i++) {
    seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0;
    const value = 125 + (seed >>> 27) * 3;
    pixels.set([value, value, value, 255], i * 4);
  }
  const texture = new THREE.DataTexture(pixels, 128, 128); texture.needsUpdate = true;
  texture.wrapS = texture.wrapT = THREE.RepeatWrapping; texture.repeat.set(6, 2);
  const aggregate = paint(0x847b68); aggregate.map = texture;
  const asphalt = paint(0x323638); asphalt.map = texture;
  box(group, [37, mode === "rail" ? 4.2 : 6, .12], [-15, 0, -.08], aggregate);
  if (mode === "road") {
    box(group, [20, 5.8, .045], [-23, 0, .005], asphalt);
    // Subtle roller streaks follow the work, with no unsupported lane markings.
    for (const y of [-1.4, 1.4]) box(group, [20, .015, .003], [-23, y, .03], rubber);
  } else {
    for (let i = 0; i < 48; i++) box(group, [.22, 2.6, .16], [-33 + i * .6, 0, .05], edge);
    for (const y of [-.7175, .7175]) {
      box(group, [29, .075, .16], [-18.5, y, .2], steel);
      box(group, [29, .15, .025], [-18.5, y, .13], steel);
    }
  }
  const machine = new THREE.Group(); group.add(machine);
  const modern = year >= 1970;
  if (year < 1920) {
    // Keep early history free of modern high-visibility clothing and machinery.
    box(machine, [2.4, 1.5, .15], [0, 0, .75], edge);
    for (const x of [-.8, .8]) for (const y of [-.85, .85]) cylinder(machine, .45, .1, [x, y, .45], steel);
    for (let i = 0; i < 6; i++) box(machine, [1.8, .12, .12], [0, -.55 + i * .2, .9], edge);
  } else if (mode === "rail") {
    // Track maintenance / laying machine: flanged wheels, work deck, glazed cab,
    // hydraulic working heads and handrails. No whole-train approximation.
    box(machine, [8, 2.6, .5], [0, 0, 1], yellow);
    for (const x of [-2.8, 2.8]) {
      cylinder(machine, .38, 1.8, [x, 0, .4], steel);
      for (const y of [-.76, .76]) cylinder(machine, .44, .06, [x, y, .4], edge);
    }
    box(machine, [2.1, 2.3, 1.7], [-1.6, 0, 2.1], yellow);
    box(machine, [2.12, 2.32, .85], [-1.6, 0, 2.38], glass);
    box(machine, [2.35, 2.55, .12], [-1.6, 0, 3.04], yellow);
    for (const y of [-.72, .72]) {
      const head = new THREE.Group(); head.position.set(1.4, y, .8); machine.add(head);
      cylinder(head, .13, .9, [0, 0, 0], steel, "z");
      box(head, [.35, .32, .23], [0, 0, -.38], edge); animated.push({ object: head, kind: "arm", phase: y });
    }
    for (const y of [-1.2, 1.2]) {
      rod(machine, new THREE.Vector3(.1, y, 1.3), new THREE.Vector3(3.7, y, 1.3), .035, steel);
      for (const x of [.2, 1.9, 3.6]) rod(machine, new THREE.Vector3(x, y, 1), new THREE.Vector3(x, y, 1.7), .035, steel);
    }
  } else {
    // Crawler excavator with individual tread plates, rollers, glazed cab,
    // articulated boom, stick, bucket and exposed hydraulic cylinders.
    for (const y of [-1.05, 1.05]) {
      box(machine, [3.8, .55, .55], [-.3, y, .45], rubber);
      for (let i = 0; i < 22; i++) for (const z of [.2, .72]) box(machine, [.12, .6, .06], [-2.1 + i * .17, y, z], steel);
      for (let i = 0; i < 6; i++) cylinder(machine, .22, .57, [-1.8 + i * .58, y, .45], edge);
    }
    cylinder(machine, .9, .28, [-.2, 0, .9], steel, "z");
    box(machine, [2.9, 2.45, 1.05], [-.65, 0, 1.5], yellow);
    box(machine, [1.35, 1.05, 1.55], [-.2, -.55, 2.25], modern ? glass : edge);
    box(machine, [1.5, 1.2, .12], [-.2, -.55, 3.05], yellow);
    for (let i = 0; i < 7; i++) box(machine, [.06, 1.2, .03], [-1.8 + i * .13, .3, 2.05], rubber);
    const boom = new THREE.Group(); boom.position.set(.45, .55, 1.8); machine.add(boom);
    const a = new THREE.Vector3(0, 0, 0), b = new THREE.Vector3(2.1, 0, 2.4), c = new THREE.Vector3(4.3, 0, .15);
    rod(boom, a, b, .2, yellow); rod(boom, b, c, .15, yellow);
    rod(boom, new THREE.Vector3(.1, 0, .5), new THREE.Vector3(1.7, 0, 2.1), .09, steel);
    rod(boom, new THREE.Vector3(2, 0, 2.6), new THREE.Vector3(3.4, 0, 1.2), .075, steel);
    box(boom, [.8, .85, .55], [4.3, 0, -.1], edge);
    for (let i = 0; i < 5; i++) box(boom, [.35, .1, .1], [4.65, -.36 + i * .18, -.35], steel);
    animated.push({ object: boom, kind: "arm", phase: 0 });
    // Compactor follows with adequate spacing; the same equipment never loops
    // through another machine or across the active work front.
    const roller = new THREE.Group(); roller.position.x = -12; group.add(roller);
    box(roller, [3.5, 1.9, .5], [0, 0, 1.05], yellow);
    for (const x of [-1.2, 1.2]) { const wheel = cylinder(roller, .65, 2.1, [x, 0, .65], steel); animated.push({ object: wheel, kind: "wheel", phase: x }); }
    box(roller, [1.4, 1.8, 1.1], [-.5, 0, 1.8], modern ? glass : edge);
    box(roller, [1.55, 2, .12], [-.5, 0, 2.42], yellow);
    // Work-zone taper; metre spacing, not screen-space confetti.
    for (let i = 0; i < 6; i++) {
      const cone = new THREE.Mesh(new THREE.ConeGeometry(.18, .6, 12), vest);
      cone.rotation.x = Math.PI / 2; cone.position.set(-18 + i * 4, -2.3, .3); group.add(cone);
      box(group, [.4, .4, .05], [-18 + i * 4, -2.3, .025], rubber);
    }
  }
  if (workers) for (let i = 0; i < 3; i++) {
    const person = new THREE.Group(); person.position.set(-3 - i * 3, 2 + (i % 2) * .5, 0); group.add(person);
    box(person, [.42, .25, .55], [0, 0, 1.12], modern ? vest : edge);
    for (const y of [-.11, .11]) {
      box(person, [.16, .14, .62], [0, y, .52], rubber);
      box(person, [.3, .15, .12], [.07, y, .12], rubber);
      rod(person, new THREE.Vector3(0, y * 2, 1.3), new THREE.Vector3(.25, y * 3, .9), .065, skin);
    }
    const head = new THREE.Mesh(new THREE.SphereGeometry(.14, 12, 8), skin); head.position.z = 1.55; person.add(head);
    cylinder(person, .18, .07, [0, 0, 1.68], modern ? yellow : edge, "z");
    if (modern) for (const y of [-.14, .14]) box(person, [.38, .015, .045], [0, y, 1.1], paint(0xe1e0b5));
    animated.push({ object: person, kind: "worker", phase: i * 2 });
  }
  return { group, update(seconds: number) {
    for (const { object, kind, phase } of animated) {
      if (kind === "arm") object.rotation.y = Math.sin(seconds * .7 + phase) * .045;
      else if (kind === "worker") object.rotation.z = Math.sin(seconds * .9 + phase) * .06;
      else object.rotation.y = seconds * .15;
    }
  }, dispose() {
    const geometries = new Set<THREE.BufferGeometry>(), materials = new Set<THREE.Material>();
    group.traverse(object => { if (object instanceof THREE.Mesh) { geometries.add(object.geometry); for (const m of [object.material].flat()) materials.add(m); } });
    geometries.forEach(g => g.dispose()); materials.forEach(m => m.dispose()); texture.dispose();
  } };
}
