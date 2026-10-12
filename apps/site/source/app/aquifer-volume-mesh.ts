import { projectVolumePosition, volumeDepthScale, type AquiferVolume } from "./aquifer-volume";

/** Render the verified polygons below local ground; keep holes and the original range bounds. */
export function aquiferGeometries(T: typeof import("three"), volume: AquiferVolume) {
  const k = volumeDepthScale(volume.bounds);
  return volume.envelopes.flatMap(envelope => envelope.geometry.map(polygon => {
    const ringPath = (ring: number[][], path: InstanceType<typeof T.Path>) => {
      ring.forEach(([lon, lat], i) => {
        const p = projectVolumePosition(lon, lat, volume.bounds);
        if (i === 0) path.moveTo(p.x, p.z); else path.lineTo(p.x, p.z);
      });
      path.closePath();
    };
    const shape = new T.Shape(); ringPath(polygon[0], shape);
    for (const hole of polygon.slice(1)) { const path = new T.Path(); ringPath(hole, path); shape.holes.push(path); }
    const geometry = new T.ExtrudeGeometry(shape, {depth: (envelope.deepMeters - envelope.shallowMeters) * k, bevelEnabled: false, steps: 1});
    geometry.rotateX(Math.PI / 2); geometry.translate(0, -envelope.shallowMeters * k, 0);
    return {envelope, geometry};
  }));
}
