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
// Same accepted-speed ceiling as TRAFFIC_MAX_SPEED_KT (pinned by a regression).
// These are conservative animation tolerances, not aircraft-performance claims.
export const SKY_MAX_SPEED_KT = 1500;
export const SKY_POSITION_TOLERANCE_M = 1000;
export const SKY_TIME_TOLERANCE_S = 2;
const KNOTS_TO_MPS = 1852 / 3600, RAD = Math.PI / 180;
const SKY_TRAIL_SUBDIVISIONS = 4;
const metricScales = (latitude: number) => {
  const w = 1 - 6.6943799901413165e-3 * Math.sin(latitude * RAD) ** 2;
  return { x: 6378137 / Math.sqrt(w) * Math.cos(latitude * RAD) * RAD, y: 6378137 * (1 - 6.6943799901413165e-3) / w ** 1.5 * RAD };
};
const metricSpan = (left: SkyPoint, right: SkyPoint) => {
  const scale = metricScales((left.lat + right.lat) / 2);
  return { scale, x: (right.lon - left.lon) * scale.x, y: (right.lat - left.lat) * scale.y };
};

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
  if (right.breakBefore || left.providerId !== right.providerId || left.onGround !== right.onGround || left.positionMethod !== right.positionMethod ||
    skyHeightReference(left) !== skyHeightReference(right) || ![left.lon,left.lat,right.lon,right.lat].every(Number.isFinite)) return false;
  const seconds = (right.observedAt - left.observedAt) / 1000;
  if (!(seconds > 0 && seconds <= SKY_MAX_GAP_MS / 1000)) return false;
  const { x, y } = metricSpan(left, right);
  return Math.hypot(x, y) <= SKY_MAX_SPEED_KT * KNOTS_TO_MPS * (seconds + SKY_TIME_TOLERANCE_S) + SKY_POSITION_TOLERANCE_M;
}
/** Explicit navigation across a missing span; never automatic playback or interpolation. */
export function nextSkyObservationAfterGap(points: readonly SkyPoint[], timeMs: number): number | null {
  if (!Number.isFinite(timeMs)) return null;
  const index = lowerBound(points, timeMs), next = points[index], previous = points[index - 1];
  return previous && next && next.observedAt !== timeMs && !connected(previous, next) ? next.observedAt : null;
}
const asAircraft = (point: SkyPoint): Aircraft => ({ ...point, observedAt: new Date(point.observedAt).toISOString(), interpolated: false });
const blend = (a: number | null, b: number | null, ratio: number) => a === null || b === null ? null : a + (b - a) * ratio;

type SkySpan = Readonly<{ model: "bounded-hermite" | "great-circle"; scale: { x: number; y: number }; x: number; y: number;
  m0: readonly [number,number]; m1: readonly [number,number]; a: readonly [number,number,number]; b: readonly [number,number,number]; angle: number }>;
// Source points are immutable; weak keys release controls when session history expires.
const spanCache = new WeakMap<SkyPoint,WeakMap<SkyPoint,SkySpan>>();
const vector = (point: SkyPoint): readonly [number,number,number] => [Math.cos(point.lat*RAD)*Math.cos(point.lon*RAD),Math.cos(point.lat*RAD)*Math.sin(point.lon*RAD),Math.sin(point.lat*RAD)];
function spanControls(left: SkyPoint, right: SkyPoint): SkySpan {
  let neighbors=spanCache.get(left);const cached=neighbors?.get(right);if(cached)return cached;
  const { scale,x,y }=metricSpan(left,right),length=Math.hypot(x,y),seconds=(right.observedAt-left.observedAt)/1000;
  const a=vector(left),b=vector(right),angle=Math.atan2(Math.hypot(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]),a[0]*b[0]+a[1]*b[1]+a[2]*b[2]);
  let model:SkySpan["model"]="great-circle",m0:readonly [number,number]=[0,0],m1:readonly [number,number]=[0,0];
  const velocityKnown=(point:SkyPoint)=>Number.isFinite(point.groundSpeedKt)&&point.groundSpeedKt!==null&&point.groundSpeedKt>=0&&point.groundSpeedKt<=SKY_MAX_SPEED_KT&&Number.isFinite(point.trackDeg)&&point.trackDeg!==null&&point.trackDeg>=0&&point.trackDeg<=360;
  if(!left.onGround&&!right.onGround&&length>=1&&seconds>0&&seconds<=60&&velocityKnown(left)&&velocityKnown(right)){
    m0=[left.groundSpeedKt!*KNOTS_TO_MPS*Math.sin(left.trackDeg!*RAD)*seconds,left.groundSpeedKt!*KNOTS_TO_MPS*Math.cos(left.trackDeg!*RAD)*seconds];
    m1=[right.groundSpeedKt!*KNOTS_TO_MPS*Math.sin(right.trackDeg!*RAD)*seconds,right.groundSpeedKt!*KNOTS_TO_MPS*Math.cos(right.trackDeg!*RAD)*seconds];
    const ratios=[Math.hypot(...m0)/length,Math.hypot(...m1)/length];
    const q0=(m0[0]*x+m0[1]*y)/(3*length*length),q1=1-(m1[0]*x+m1[1]*y)/(3*length*length);
    const lateral=Math.max(Math.abs(m0[0]*y-m0[1]*x),Math.abs(m1[0]*y-m1[1]*x))/(3*length*length);
    // Bezier control hull: monotone progress and a 25%-of-chord lateral corridor.
    // This bounds the estimate; it establishes no acceleration or flight-plan guarantee.
    if(ratios.every(ratio=>ratio>=.5&&ratio<=2)&&q0>=0&&q0<=q1&&q1<=1&&lateral<=.25)model="bounded-hermite";
  }
  const controls={model,scale,x,y,m0,m1,a,b,angle};
  if(!neighbors){neighbors=new WeakMap();spanCache.set(left,neighbors);}neighbors.set(right,controls);return controls;
}
function spanPosition(left:SkyPoint,right:SkyPoint,ratio:number){
  const span=spanControls(left,right);
  if(span.model==="bounded-hermite"){
    const t2=ratio*ratio,t3=t2*ratio,h10=t3-2*t2+ratio,h01=-2*t3+3*t2,h11=t3-t2;
    const lon=left.lon+(h10*span.m0[0]+h01*span.x+h11*span.m1[0])/span.scale.x;
    const lat=left.lat+(h10*span.m0[1]+h01*span.y+h11*span.m1[1])/span.scale.y;
    const scale=metricScales(lat),d10=3*t2-4*ratio+1,d01=-6*t2+6*ratio,d11=3*t2-2*ratio;
    const east=(d10*span.m0[0]+d01*span.x+d11*span.m1[0])*scale.x/span.scale.x;
    const north=(d10*span.m0[1]+d01*span.y+d11*span.m1[1])*scale.y/span.scale.y;
    return {lon,lat,renderedTrackDeg:Math.hypot(east,north)>1e-8?(Math.atan2(east,north)/RAD+360)%360:null,model:span.model};
  }
  if(span.angle<1e-10)return {lon:left.lon+(right.lon-left.lon)*ratio,lat:left.lat+(right.lat-left.lat)*ratio,renderedTrackDeg:null,model:span.model};
  const sine=Math.sin(span.angle),w0=Math.sin((1-ratio)*span.angle)/sine,w1=Math.sin(ratio*span.angle)/sine;
  const v=span.a.map((n,index)=>n*w0+span.b[index]*w1),lon=Math.atan2(v[1],v[0]),lat=Math.atan2(v[2],Math.hypot(v[0],v[1]));
  const derivative=span.a.map((n,index)=>span.angle*(-n*Math.cos((1-ratio)*span.angle)+span.b[index]*Math.cos(ratio*span.angle))/sine);
  const east=-Math.sin(lon)*derivative[0]+Math.cos(lon)*derivative[1];
  const north=-Math.sin(lat)*Math.cos(lon)*derivative[0]-Math.sin(lat)*Math.sin(lon)*derivative[1]+Math.cos(lat)*derivative[2];
  return {lon:lon/RAD,lat:lat/RAD,renderedTrackDeg:(Math.atan2(east,north)/RAD+360)%360,model:span.model};
}

/** One source-bounded sampler for aircraft and display paths. No extrapolation or flight-plan inference. */
export function sampleSkySpan(previous:SkyPoint,next:SkyPoint,timeMs:number):Aircraft|null {
  if(!Number.isFinite(timeMs)||timeMs<previous.observedAt||timeMs>next.observedAt)return null;
  if(timeMs===previous.observedAt)return asAircraft(previous);
  if(timeMs===next.observedAt)return asAircraft(next);
  if(!connected(previous,next))return null;
  const ratio=(timeMs-previous.observedAt)/(next.observedAt-previous.observedAt),position=spanPosition(previous,next,ratio),source=asAircraft(previous);
  return {...source,lon:position.lon,lat:position.lat,renderedTrackDeg:position.renderedTrackDeg,
    sampledAt:new Date(timeMs).toISOString(),interpolation:{fromObservedAt:source.observedAt!,toObservedAt:new Date(next.observedAt).toISOString(),model:position.model},
    altBaroFt:blend(previous.altBaroFt,next.altBaroFt,ratio),altGeomFt:blend(previous.altGeomFt,next.altGeomFt,ratio),
    // Source ground speed and track remain measurements; the rendered tangent is separate.
    verticalRateFpm:previous.verticalRateReference===next.verticalRateReference?blend(previous.verticalRateFpm,next.verticalRateFpm,ratio):null,
    rollDeg:blend(previous.rollDeg??null,next.rollDeg??null,ratio),indicatedAirSpeedKt:blend(previous.indicatedAirSpeedKt??null,next.indicatedAirSpeedKt??null,ratio),
    mach:blend(previous.mach??null,next.mach??null,ratio),interpolated:true};
}

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
    if (!previous || !next) continue;
    const sample=sampleSkySpan(previous,next,timeMs);if(sample)result.push(sample);
  }
  return result;
}

export type SkyTrail = Readonly<{ hex: string; points: readonly SkyPoint[]; future?: boolean; heightReference?: ReturnType<typeof skyHeightReference> }>;
/** Allocate the final geometry budget before sampling original neighbor pairs.
 * No oversized temporary curve array and no curve fitted across thinned observations.
 * Synthetic vertices are display geometry only; source tracks stay intact. */
export function tessellateSkyTrails(segments:readonly SkyTrail[],budget=SKY_MAX_TRAIL_POINTS):readonly SkyTrail[]{
  const cap=Math.max(0,Math.floor(budget)),valid=segments.filter(segment=>segment.points.length>1);
  const kept=valid.length*2<=cap?valid:[...valid].sort((a,b)=>b.points.at(-1)!.observedAt-a.points.at(-1)!.observedAt).slice(0,Math.floor(cap/2));
  let remaining=cap;
  return kept.map((segment,index)=>{
    const source=segment.points,desired=1+(source.length-1)*SKY_TRAIL_SUBDIVISIONS;
    const count=Math.min(desired,Math.floor(remaining/(kept.length-index)));remaining-=count;
    // Under contention, reduce historical detail before adding curve vertices.
    // Endpoints remain exact; no new curve is fitted across skipped reports.
    if(count<=source.length)return {...segment,points:count===source.length?source:Array.from({length:count},(_,i)=>source[Math.round(i*(source.length-1)/(count-1))])};
    const points:SkyPoint[]=[];
    for(let i=0;i<count;i++){
      const sourceIndex=i*(source.length-1)/(count-1),leftIndex=Math.floor(sourceIndex),ratio=sourceIndex-leftIndex;
      if(ratio===0||leftIndex===source.length-1){points.push(source[leftIndex]);continue;}
      const left=source[leftIndex],right=source[leftIndex+1],at=left.observedAt+(right.observedAt-left.observedAt)*ratio;
      // Geometry needs numeric positions/heights, not instrument interpolation,
      // timestamp strings or source-bracket receipts for every display vertex.
      const position=spanPosition(left,right,ratio);
      points.push({...left,lon:position.lon,lat:position.lat,observedAt:at,
        altBaroFt:blend(left.altBaroFt,right.altBaroFt,ratio),altGeomFt:blend(left.altGeomFt,right.altGeomFt,ratio),interpolated:true,breakBefore:false});
    }
    return {...segment,points};
  });
}
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
let journeyGeometryCache=new WeakMap<readonly SkyPoint[],{first:SkyPoint;last:SkyPoint;count:number;whole:readonly SkyTrail[]}>();
export function selectedJourney(points:readonly SkyPoint[],time:number):readonly SkyTrail[] {
  if(!points.length)return [];
  const tracks=new Map([[points[0].hex,points]]);
  let cached=journeyGeometryCache.get(points);
  if(!cached||cached.first!==points[0]||cached.last!==points.at(-1)||cached.count!==points.length){
    const whole=trailSegments(tracks,points.at(-1)!.observedAt,points.at(-1)!.observedAt-points[0].observedAt+1,SKY_MAX_TRAIL_POINTS-2);
    cached={first:points[0],last:points.at(-1)!,count:points.length,whole};
    // One weakly owned selected geometry, with at most the existing display cap.
    journeyGeometryCache=new WeakMap([[points,cached]]);
  }
  const whole=cached.whole;
  const at=samplesAt(tracks,time)[0];
  const cursorPoint:SkyPoint|undefined=at?.interpolated?{...at,observedAt:time,providerId:points[Math.max(0,lowerBound(points,time)-1)].providerId}:undefined;
  return whole.flatMap(segment=>{
    const before=segment.points.filter(point=>point.observedAt<=time),after=segment.points.filter(point=>point.observedAt>time);
    if(cursorPoint&&segment.points[0].observedAt<time&&segment.points.at(-1)!.observedAt>time){if(before.at(-1)?.observedAt!==time)before.push(cursorPoint);after.unshift(cursorPoint);}
    else if(before.length&&after.length)after.unshift(before.at(-1)!);
    return [...(before.length>1?[{...segment,points:before,future:false}]:[]),...(after.length>1?[{...segment,points:after,future:true}]:[])];
  });
}
/** Gaps and provider changes split trails. Rendering budget thins geometry, never current aircraft. */
export function trailSegments(tracks: SkyTracks, timeMs: number, windowMs = SKY_REGIONAL_MS, budget = SKY_MAX_TRAIL_POINTS): readonly SkyTrail[] {
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
  return tessellateSkyTrails(segments,budget);
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
