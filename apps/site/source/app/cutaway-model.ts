import type { AquiferVolume } from "./aquifer-volume";
import { meters, type Borehole, type DepthInterval } from "./subsurface-model";

/** Independent record-depth diagrams; no correlation or common elevation is inferred. */
export function cutawayRecords(volume: AquiferVolume, records: Borehole[]) {
  const [west, south, east, north] = volume.bounds;
  const limit = volume.envelopes.length ? Math.max(...volume.envelopes.map(e => e.deepMeters)) + 50 : 500;
  const intervals: { record: Borehole; interval: DepthInterval; top: number; bottom: number }[] = [];
  const visible = new Set<string>();
  let clipped = false;
  for (const record of records.slice(0, 50)) {
    const [lon, lat] = record.coordinates;
    if (lon < west || lon > east || lat < south || lat > north) continue;
    for (const interval of record.intervals) {
      const top = meters(interval.top, record.depthUnit), originalBottom = meters(interval.bottom, record.depthUnit);
      if (!Number.isFinite(top) || !Number.isFinite(originalBottom) || top < 0 || originalBottom <= top) continue;
      if (originalBottom > limit) clipped = true;
      const bottom = Math.min(limit, originalBottom);
      if (bottom <= top) continue;
      if (intervals.length >= 400) { clipped = true; break; }
      intervals.push({ record, interval, top, bottom }); visible.add(record.id);
    }
  }
  return { intervals, recordCount: visible.size, limit, clipped,
    deepest: Math.max(1, ...volume.envelopes.map(e => e.deepMeters), ...intervals.map(i => i.bottom)) };
}

/** Fit actual projected corners and screen-sized depth labels, not a bounding sphere. */
export function cutawayCameraFit(width: number, length: number, depth: number, aspect: number,
  direction: readonly [number, number, number] = [.55, .6, 1], viewportHeight = 460) {
  const norm = Math.hypot(...direction), d = direction.map(n => n / norm);
  const rightLength = Math.hypot(d[2], d[0]);
  const right = rightLength > 1e-10 ? [d[2] / rightLength, 0, -d[0] / rightLength] : [1, 0, 0];
  const up = [d[1] * right[2] - d[2] * right[1], d[2] * right[0] - d[0] * right[2], d[0] * right[1] - d[1] * right[0]];
  const dot = (a: number[], b: number[]) => a.reduce((sum, n, i) => sum + n * b[i], 0);
  const height = Math.max(64, viewportHeight), viewWidth = Math.max(64, height * Math.max(.1, aspect));
  const tanV = Math.tan(40 * Math.PI / 360), tanH = tanV * Math.max(.1, aspect);
  const marginY = Math.max(12, height * .07), marginX = Math.max(10, viewWidth * .025);
  let distance = .01, closest = -Infinity, farthest = Infinity;
  const projected: {across:number;above:number;toward:number;padX:number;padY:number}[]=[];
  const include = (point: number[], halfLabelWidth = 0, halfLabelHeight = 0) => {
    const toward = dot(point, d);
    projected.push({across:dot(point,right),above:dot(point,up),toward,padX:halfLabelWidth*2/viewWidth,padY:halfLabelHeight*2/height});
    const horizontal = Math.max(.1, 1 - 2 * (marginX + halfLabelWidth) / viewWidth);
    const vertical = Math.max(.1, 1 - 2 * (marginY + halfLabelHeight) / height);
    distance = Math.max(distance, toward + Math.abs(dot(point, right)) / (tanH * horizontal), toward + Math.abs(dot(point, up)) / (tanV * vertical));
    closest = Math.max(closest, toward); farthest = Math.min(farthest, toward);
  };
  for (const x of [-width / 2, width / 2]) for (const y of [-depth / 2, depth / 2]) for (const z of [-length / 2, length / 2]) include([x, y, z]);
  for (const f of [0, .25, .5, .75, 1]) include([-width / 2 - .42, depth / 2 - depth * f, length / 2], 45, 12);
  const extents=(at:number)=>{
    let minX=Infinity,maxX=-Infinity,minY=Infinity,maxY=-Infinity;
    for(const p of projected){const x=p.across/((at-p.toward)*tanH),y=p.above/((at-p.toward)*tanV);
      minX=Math.min(minX,x-p.padX);maxX=Math.max(maxX,x+p.padX);minY=Math.min(minY,y-p.padY);maxY=Math.max(maxY,y+p.padY);}
    return {minX,maxX,minY,maxY};
  };
  // Recenter the asymmetric perspective bounds so one near corner does not
  // force a much smaller object than the viewport actually needs.
  let lower=closest+Math.max(1e-8,Math.abs(closest)*1e-12),upper=distance;
  for(let i=0;i<55;i++){const mid=(lower+upper)/2,b=extents(mid);
    if(b.maxX-b.minX<=2*(1-2*marginX/viewWidth)&&b.maxY-b.minY<=2*(1-2*marginY/height))upper=mid;else lower=mid;}
  distance=upper*1.025;const b=extents(distance);
  return { distance, offsetX:(b.minX+b.maxX)/2, offsetY:(b.minY+b.maxY)/2, near: Math.max(.000001, (distance - closest) / 100), far: Math.max(100, (distance - farthest) * 4) };
}

/** Pick only the source-owner meshes. Decorative interval edges are not evidence. */
export function pickCutawaySource(ray: import("three").Raycaster, owners: import("three").Mesh[]) {
  return ray.intersectObjects(owners, false)[0];
}
