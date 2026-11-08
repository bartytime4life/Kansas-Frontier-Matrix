import type { Aircraft, TrafficEnvelope } from "./aviation-traffic";

/** Session memory only. No database, extrapolation, or inferred flight identity. */
export type SkyPoint = Omit<Aircraft, "observedAt"> & Readonly<{ observedAt: number; providerId: string; breakBefore?: boolean }>;
export type SkyTracks = ReadonlyMap<string, readonly SkyPoint[]>;
export const SKY_MAX_GAP_MS = 60_000;
export const SKY_REGIONAL_MS = 600_000;
export const SKY_SELECTED_MS = 3_600_000;
export const SKY_MAX_REGIONAL_POINTS = 100_000;
export const SKY_MAX_SELECTED_POINTS = 10_000;
export const SKY_MAX_TRAIL_POINTS = 20_000;
export const SKY_MAX_HEIGHT_GUIDES = 96;
export const SKY_MAX_PROFILE_POINTS = 800;
export const SKY_LIVE_DELAY_MS = 30_000;

export type SkyCatalogPart=Readonly<{id:string;hex?:string;day?:string;provider:string;start:string;end:string;part?:number;partCount?:number}>;
/** Catalog navigation only: no cross-file concatenation, gap filling or prefetch. */
export function skyPartNeighbors<T extends SkyCatalogPart>(catalog:readonly T[],current:T|null):{previous:T|null;next:T|null;available:number;expected:number;multipart:boolean}{
  if(!current||!current.hex||!current.day||!current.part||!current.partCount)return {previous:null,next:null,available:current?1:0,expected:current?1:0,multipart:false};
  const matching=catalog.filter(part=>part.hex===current.hex&&part.day===current.day&&part.provider===current.provider&&part.partCount===current.partCount);
  const exact=(number:number)=>{const entries=matching.filter(part=>part.part===number);return entries.length===1?entries[0]:null;};
  const before=exact(current.part-1),after=exact(current.part+1);
  return {previous:before&&Date.parse(before.end)<=Date.parse(current.start)?before:null,next:after&&Date.parse(after.start)>=Date.parse(current.end)?after:null,
    available:new Set(matching.map(part=>part.part)).size,expected:current.partCount,multipart:current.partCount>1};
}

/** readsb positive roll is right bank: the right wing descends. */
export const bankHeightOffset = (rightWingMetres: number, rollDegrees: number | null | undefined): number =>
  -rightWingMetres * Math.sin((rollDegrees ?? 0) * Math.PI / 180);

/** Resume from the retained start when expiry has moved beyond a paused cursor. */
export function advanceSkyCursor(cursor: number, range: readonly [number, number], elapsed: number, speed: number): number {
  return Math.min(range[1], Math.max(range[0], cursor) + Math.max(0, elapsed) * speed);
}

export function validSkyPoint(point: SkyPoint): boolean {
  return Boolean(point && /^~?[0-9a-f]{6}$/.test(point.hex) && Number.isFinite(point.observedAt) && point.observedAt > 0 &&
    Number.isFinite(point.lon) && point.lon >= -103.2 && point.lon <= -93.6 && Number.isFinite(point.lat) && point.lat >= 36.2 && point.lat <= 40.9 &&
    typeof point.providerId === "string" && /^[a-z0-9-]{1,40}$/.test(point.providerId));
}

/** First sample with time >= target, O(log n), used by replay and trail clipping. */
function lowerBound(points: readonly SkyPoint[], time: number): number {
  let low = 0, high = points.length;
  while (low < high) { const mid = (low + high) >>> 1; if (points[mid].observedAt < time) low = mid + 1; else high = mid; }
  return low;
}
export function connected(left: SkyPoint, right: SkyPoint): boolean {
  return !right.breakBefore && left.providerId === right.providerId && left.onGround === right.onGround && left.positionMethod === right.positionMethod &&
    right.observedAt > left.observedAt && right.observedAt - left.observedAt <= SKY_MAX_GAP_MS;
}
/** Explicit navigation across a missing span; never automatic playback or interpolation. */
export function nextSkyObservationAfterGap(points: readonly SkyPoint[], timeMs: number): number | null {
  if (!Number.isFinite(timeMs)) return null;
  const index = lowerBound(points, timeMs), next = points[index], previous = points[index - 1];
  return previous && next && next.observedAt !== timeMs && !connected(previous, next) ? next.observedAt : null;
}
const asAircraft = (point: SkyPoint): Aircraft => ({ ...point, observedAt: new Date(point.observedAt).toISOString(), interpolated: false });
const blend = (a: number | null, b: number | null, ratio: number) => a === null || b === null ? null : a + (b - a) * ratio;

/** A height graph may not join pressure and geometric datums or unknown heights. */
export const skyHeightReference = (point: Pick<SkyPoint,"onGround"|"altGeomFt"|"altBaroFt">) =>
  point.onGround ? null : point.altGeomFt !== null && point.altGeomFt !== undefined ? "WGS84" : point.altBaroFt !== null && point.altBaroFt !== undefined ? "pressure" : null;
export const skyHeightFt = (point: Pick<SkyPoint,"onGround"|"altGeomFt"|"altBaroFt">) => skyHeightReference(point) ? point.altGeomFt ?? point.altBaroFt : null;

/** Split before thinning: budgets can omit detail but cannot manufacture continuity. */
export function heightProfile(points: readonly SkyPoint[], budget = SKY_MAX_PROFILE_POINTS): readonly (readonly SkyPoint[])[] {
  const segments: SkyPoint[][] = []; let segment: SkyPoint[] = [];
  for (const point of points) {
    if (segment.length && (!connected(segment.at(-1)!,point) || skyHeightReference(segment.at(-1)!) !== skyHeightReference(point))) { segments.push(segment); segment=[]; }
    if (skyHeightReference(point)) segment.push(point); else if(segment.length){segments.push(segment);segment=[];}
  }
  if(segment.length)segments.push(segment);
  const cap=Math.max(0,Math.floor(budget));
  // Retain recent disconnected segments, then preserve both endpoints of each.
  const kept=segments.slice(-Math.floor(cap/2));let remaining=cap;
  return kept.map((part,index)=>{const quota=Math.min(part.length,Math.floor(remaining/(kept.length-index)));remaining-=quota;
    return quota>=part.length?part:Array.from({length:quota},(_,i)=>part[Math.round(i*(part.length-1)/Math.max(1,quota-1))]);});
}

/** Shared frame budget: lower redraw frequency before removing aircraft. */
export class SkyFrameBudget {
  private average=0;
  record(milliseconds:number):void { if(Number.isFinite(milliseconds)&&milliseconds>=0)this.average=this.average*.85+milliseconds*.15; }
  interval(reduced=false):number { return reduced?200:this.average>24?50:this.average>12?1000/30:1000/60; }
}

/** One cancellable clock for smooth positions; React readouts receive at most 5 updates/s. */
export function animateSkyReplay(options:{start:number;range:readonly [number,number];speed:number;reduced:boolean;
  requestFrame:(callback:(timestamp:number)=>void)=>number;cancelFrame:(id:number)=>void;now:()=>number;
  render:(time:number)=>void;readout:(time:number)=>void;ended:()=>void}) {
  let active=true,id=0,lastFrame=-Infinity,lastReadout=-Infinity;
  const began=options.now(),budget=new SkyFrameBudget();
  const frame=(stamp:number)=>{
    if(!active)return;
    const at=advanceSkyCursor(options.start,options.range,stamp-began,options.speed);
    if(stamp-lastFrame>=budget.interval(options.reduced)-1||at>=options.range[1]){
      const before=options.now();options.render(at);budget.record(options.now()-before);lastFrame=stamp;
    }
    if(stamp-lastReadout>=200||at>=options.range[1]){options.readout(at);lastReadout=stamp;}
    if(at>=options.range[1]){active=false;options.ended();return;}
    id=options.requestFrame(frame);
  };
  id=options.requestFrame(frame);
  return ()=>{active=false;options.cancelFrame(id);};
}

/** A single delayed timeline, filtered by today's still-eligible feed identities. */
export function bufferedSkySamples(tracks:SkyTracks,time:number,eligible:ReadonlySet<string>):readonly Aircraft[]{
  return samplesAt(tracks,time).filter(aircraft=>eligible.has(aircraft.hex));
}
export function animateSkyBuffered(options:{requestFrame:(callback:(timestamp:number)=>void)=>number;cancelFrame:(id:number)=>void;now:()=>number;wallTime:()=>number;
  render:(time:number)=>void;readout:(time:number)=>void}){
  let active=true,id=0,lastFrame=-Infinity,lastReadout=-Infinity;const budget=new SkyFrameBudget();
  const frame=(stamp:number)=>{if(!active)return;const at=options.wallTime()-SKY_LIVE_DELAY_MS;
    if(stamp-lastFrame>=budget.interval()-1){const before=options.now();options.render(at);budget.record(options.now()-before);lastFrame=stamp;}
    if(stamp-lastReadout>=200){options.readout(at);lastReadout=stamp;}id=options.requestFrame(frame);
  };
  id=options.requestFrame(frame);return()=>{active=false;options.cancelFrame(id);};
}

/** Exact observations or interpolation bounded by two observations. Never dead-reckon into unseen time. */
export function samplesAt(tracks: SkyTracks, timeMs: number): readonly Aircraft[] {
  if (!Number.isFinite(timeMs)) return [];
  const result: Aircraft[] = [];
  for (const points of tracks.values()) {
    const index = lowerBound(points, timeMs), next = points[index];
    if (next?.observedAt === timeMs) { result.push(asAircraft(next)); continue; }
    const previous = points[index - 1];
    if (!previous || !next || !connected(previous, next)) continue;
    const ratio = (timeMs - previous.observedAt) / (next.observedAt - previous.observedAt);
    const turn = previous.trackDeg === null || next.trackDeg === null ? null : ((next.trackDeg - previous.trackDeg + 540) % 360) - 180;
    result.push({ ...asAircraft(previous), lon: previous.lon + (next.lon - previous.lon) * ratio, lat: previous.lat + (next.lat - previous.lat) * ratio,
      altBaroFt: blend(previous.altBaroFt, next.altBaroFt, ratio), altGeomFt: blend(previous.altGeomFt, next.altGeomFt, ratio),
      trackDeg: turn === null ? null : (previous.trackDeg! + turn * ratio + 360) % 360,
      // Optional instruments are not synthesized or carried past missing endpoints.
      groundSpeedKt: blend(previous.groundSpeedKt, next.groundSpeedKt, ratio), verticalRateFpm: previous.verticalRateReference === next.verticalRateReference ? blend(previous.verticalRateFpm, next.verticalRateFpm, ratio) : null,
      rollDeg: blend(previous.rollDeg ?? null, next.rollDeg ?? null, ratio),
      indicatedAirSpeedKt: blend(previous.indicatedAirSpeedKt ?? null, next.indicatedAirSpeedKt ?? null, ratio),
      mach: blend(previous.mach ?? null, next.mach ?? null, ratio), interpolated: true });
  }
  return result;
}

export type SkyTrail = Readonly<{ hex: string; points: readonly SkyPoint[]; future?: boolean; heightReference?: ReturnType<typeof skyHeightReference> }>;
/** Sample only within already separated source segments. Never infer gaps from display spacing. */
export function limitSkyTrailPoints(segments:readonly SkyTrail[],budget:number):readonly SkyTrail[]{
  const cap=Math.max(0,Math.floor(budget));
  if(segments.reduce((sum,segment)=>sum+segment.points.length,0)<=cap)return segments;
  const kept=[...segments].sort((a,b)=>b.points.at(-1)!.observedAt-a.points.at(-1)!.observedAt).slice(0,Math.floor(cap/2));
  let remaining=cap;
  return kept.map((segment,index)=>{const quota=Math.min(segment.points.length,Math.floor(remaining/(kept.length-index)));remaining-=quota;
    return {...segment,points:quota>=segment.points.length?segment.points:Array.from({length:quota},(_,i)=>segment.points[Math.round(i*(segment.points.length-1)/Math.max(1,quota-1))])};});
}
/** Internal trail metadata records continuity before thinning; legacy raw input is split first. */
export function skyDrawableTrails(trails:readonly SkyTrail[],flat=false):readonly SkyTrail[]{
  return flat?trails:trails.flatMap(trail=>trail.heightReference!==undefined
    ? trail.heightReference?[trail]:[]
    :heightProfile(trail.points,SKY_MAX_TRAIL_POINTS).map(points=>({...trail,points,heightReference:skyHeightReference(points[0])})));
}
/** A recorded route ahead of its cursor is retained history, never a live prediction. */
export function selectedJourney(points:readonly SkyPoint[],time:number):readonly SkyTrail[] {
  if(!points.length)return [];
  const tracks=new Map([[points[0].hex,points]]);
  const whole=trailSegments(tracks,points.at(-1)!.observedAt,points.at(-1)!.observedAt-points[0].observedAt+1);
  const at=samplesAt(tracks,time)[0];
  const cursorPoint:SkyPoint|undefined=at?.interpolated?{...at,observedAt:time,providerId:points[Math.max(0,lowerBound(points,time)-1)].providerId}:undefined;
  return whole.flatMap(segment=>{
    const before=segment.points.filter(point=>point.observedAt<=time),after=segment.points.filter(point=>point.observedAt>time);
    if(cursorPoint&&segment.points[0].observedAt<time&&segment.points.at(-1)!.observedAt>time){before.push(cursorPoint);after.unshift(cursorPoint);}
    else if(before.length&&after.length)after.unshift(before.at(-1)!);
    return [...(before.length>1?[{...segment,points:before,future:false}]:[]),...(after.length>1?[{...segment,points:after,future:true}]:[])];
  });
}
/** Gaps and provider changes split trails. Rendering budget thins geometry, never current aircraft. */
export function trailSegments(tracks: SkyTracks, timeMs: number, windowMs = SKY_REGIONAL_MS): readonly SkyTrail[] {
  const segments: SkyTrail[] = [];
  for (const [hex, points] of tracks) {
    let segment: SkyPoint[] = [];
    for (let i = lowerBound(points, timeMs - windowMs); i < points.length && points[i].observedAt <= timeMs; i++) {
      const point = points[i];
      if (segment.length && (!connected(segment[segment.length - 1], point)||skyHeightReference(segment.at(-1)!)!==skyHeightReference(point))) { if (segment.length > 1) segments.push({ hex, points: segment, heightReference:skyHeightReference(segment[0]) }); segment = []; }
      segment.push(point);
    }
    if (segment.length > 1) segments.push({ hex, points: segment, heightReference:skyHeightReference(segment[0]) });
  }
  return limitSkyTrailPoints(segments,SKY_MAX_TRAIL_POINTS);
}

export class SkyBuffer {
  private data = new Map<string, SkyPoint[]>();
  private selected: string | null = null;
  private latest = 0;
  private current = new Set<string>();
  truncated = false;
  clear(): void { this.data.clear(); this.current.clear(); this.latest = 0; this.truncated = false; }
  select(hex: string | null): void { this.selected = hex; this.prune(); }
  tracks(): SkyTracks { return this.data; }
  range(hex?: string): readonly [number, number] | null {
    let low = Infinity, high = -Infinity;
    for (const [id, points] of this.data) if ((!hex || id === hex) && points.length) { low = Math.min(low, points[0].observedAt); high = Math.max(high, points[points.length - 1].observedAt); }
    return Number.isFinite(low) ? [low, high] : null;
  }
  at(timeMs: number): readonly Aircraft[] { return samplesAt(this.data, timeMs); }
  ingest(envelope: TrafficEnvelope): void {
    const retrieved = Date.parse(envelope.retrievedAt);
    if (!Number.isFinite(retrieved) || !envelope.provider?.id || !Array.isArray(envelope.records)) return;
    const currentSnapshot = retrieved >= this.latest;
    if (currentSnapshot) this.current.clear();
    this.latest = Math.max(this.latest, retrieved);
    this.truncated ||= Boolean(envelope.truncated || envelope.records.length > 3000);
    for (const record of envelope.records.slice(0, 3000)) {
      if (!record || typeof record !== "object") continue;
      const observedAt = record.observedAt ? Date.parse(record.observedAt) : retrieved - record.positionAgeS * 1000;
      const point: SkyPoint = { ...record, observedAt, providerId: envelope.provider.id };
      if (!validSkyPoint(point) || observedAt > retrieved + 5000 || observedAt < retrieved - SKY_MAX_GAP_MS) continue;
      if (currentSnapshot) this.current.add(record.hex);
      let points = this.data.get(record.hex);
      if (!points) { points = []; this.data.set(record.hex, points); }
      const index = lowerBound(points, observedAt);
      // Same-time duplicates retain first observed provenance, never append invented motion.
      if (points[index]?.observedAt === observedAt) continue;
      points.splice(index, 0, point);
    }
    this.prune();
  }
  private prune(): void {
    let regionalCount = 0;
    for (const [hex, points] of this.data) {
      const selected = hex === this.selected;
      const cut = lowerBound(points, this.latest - (selected ? SKY_SELECTED_MS : SKY_REGIONAL_MS));
      if (cut) points.splice(0, cut);
      if (selected && points.length > SKY_MAX_SELECTED_POINTS) { points.splice(0, points.length - SKY_MAX_SELECTED_POINTS); this.truncated = true; }
      if (!points.length) this.data.delete(hex);
      else if (!selected) regionalCount += points.length;
    }
    if (regionalCount <= SKY_MAX_REGIONAL_POINTS) return;
    this.truncated = true;
    // A global time cutoff preserves the freshest samples fairly across all aircraft.
    const times = [...this.data].filter(([hex]) => hex !== this.selected).flatMap(([, points]) => points.map(point => point.observedAt)).sort((a, b) => a - b);
    const threshold = times[regionalCount - SKY_MAX_REGIONAL_POINTS];
    for (const [hex, points] of this.data) if (hex !== this.selected) {
      const cut = lowerBound(points, threshold);
      points.splice(0, cut); regionalCount -= cut;
      if (!points.length) this.data.delete(hex);
    }
    // Resolve equal timestamps deterministically while retaining newest samples per aircraft.
    for (const [hex, points] of this.data) if (hex !== this.selected && regionalCount > SKY_MAX_REGIONAL_POINTS) {
      const cut = Math.min(lowerBound(points, threshold + 1), Math.max(0, points.length - 1), regionalCount - SKY_MAX_REGIONAL_POINTS);
      points.splice(0, cut); regionalCount -= cut;
      if (!points.length) this.data.delete(hex);
    }
    // Adversarial identity churn can leave more than the cap in one-point,
    // same-time historical tracks. Preserve the latest feed (at most 3,000)
    // and selected aircraft; retire historical ties in stable insertion order.
    for (const [hex, points] of this.data) if (hex !== this.selected && !this.current.has(hex) && regionalCount > SKY_MAX_REGIONAL_POINTS) {
      const cut = Math.min(points.length, regionalCount - SKY_MAX_REGIONAL_POINTS);
      points.splice(0, cut); regionalCount -= cut;
      if (!points.length) this.data.delete(hex);
    }
  }
}
