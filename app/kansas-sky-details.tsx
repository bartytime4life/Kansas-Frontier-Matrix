"use client";
import { useMemo } from "react";
import type { Aircraft } from "./aviation-traffic";
import { heightProfile, skyHeightFt, skyHeightReference, samplesAt, type SkyPoint } from "./kansas-sky";

const value=(input:string|number|null|undefined,suffix="")=>input===null||input===undefined?"Unavailable":`${input}${suffix}`;
export const skyMeasurement=(input:number|null|undefined,suffix="",digits=0)=>input===null||input===undefined||!Number.isFinite(input)?"Unavailable":`${input.toLocaleString("en-US",{maximumFractionDigits:digits})}${suffix}`;
const time=(ms:number)=>new Date(ms).toISOString().slice(11,19)+" UTC";

export function SkyAircraftBrief({aircraft,observationCount,gap=false}:{aircraft:Aircraft;observationCount:number;gap?:boolean}){
  const name=aircraft.callsign??aircraft.registration??aircraft.hex.toUpperCase();
  const bracket=aircraft.interpolation;
  const model=bracket?.model==="bounded-hermite"?"a bounded curve using reported speed and track":"a great-circle path between reports";
  const direction=aircraft.trueHeadingDeg!=null?"The aircraft nose follows reported true heading.":aircraft.renderedTrackDeg!=null?"The schematic points along the estimated path; this is not reported aircraft heading.":aircraft.trackDeg!=null?"The schematic follows reported ground track, which can differ from aircraft heading.":"Direction is unavailable; the symbol is a position marker.";
  return <div className="kansas-sky-brief"><p><strong>{name}</strong>{aircraft.registration&&aircraft.registration!==name?` (${aircraft.registration})`:""} is reported as {aircraft.type??"an aircraft of unavailable type"}{aircraft.onGround?" on the ground":" airborne"}{aircraft.interpolated?"; its estimated position is displayed near ":" near "}{skyMeasurement(aircraft.lat,"°",3)}, {skyMeasurement(aircraft.lon,"°",3)}.</p><p>{aircraft.groundSpeedKt!==null?`Reported ground speed is ${skyMeasurement(aircraft.groundSpeedKt," knots",1)}. `:"Ground speed is unavailable. "}{aircraft.verticalRateFpm!==null?`${aircraft.interpolated?"Interpolated":"Reported"} vertical rate is ${skyMeasurement(aircraft.verticalRateFpm," ft/min")} (${aircraft.verticalRateReference??"reference unavailable"}). `:""}</p>{bracket&&<p className="sky-motion-explanation"><strong>Estimated position · {aircraft.sampledAt?time(Date.parse(aircraft.sampledAt)):"playback time unavailable"}</strong> Between reports at {time(Date.parse(bracket.fromObservedAt))} and {time(Date.parse(bracket.toObservedAt))}, motion follows {model}. It is a bounded estimate, not another observation or a future route.</p>}<p>{direction} Heights use the reported WGS84 or pressure reference; terrain is a different surface, so the guides do not measure clearance.</p><p>{observationCount.toLocaleString()} observations are retained for this selection. These cover observed regional segments, not a confirmed origin-to-destination flight.</p>{gap&&<p>Observation gap. This brief uses the retained report at {aircraft.observedAt??"an unavailable time"}; no aircraft position is drawn for this gap.</p>}</div>;
}

/** Source-provided fields only. Interpretation is kept separate from measurements. */
export function SkyAircraftDossier({aircraft,source,expanded=false}:{aircraft:Aircraft;source:string;expanded?:boolean}){
  const quality=aircraft.positionQuality;
  const groups:readonly (readonly [string,readonly (readonly [string,string])[]])[]=[
    ["Identity",[["Callsign",value(aircraft.callsign)],["ICAO / address",aircraft.hex.toUpperCase()],["Registration",value(aircraft.registration)],["Aircraft type",value(aircraft.type)],["Emitter category",value(aircraft.category)],["Provider military flag",aircraft.military?"Flagged by provider":"Not flagged by provider"]]],
    ["Position & time",[["Latitude",skyMeasurement(aircraft.lat,"°",6)],["Longitude",skyMeasurement(aircraft.lon,"°",6)],["Ground state",aircraft.onGround?"Reported on ground":"Reported airborne"],["Source",source],["Position method",value(aircraft.positionMethod)],["Observation time",value(aircraft.observedAt)],["Time basis",value(aircraft.timestampBasis)],["Position age at receipt",skyMeasurement(aircraft.positionAgeS," s",1)],["Displayed position",aircraft.interpolated?"Estimated between observations":"Reported observation"],["Evaluated playback time",value(aircraft.sampledAt)],["Earlier bounding report",value(aircraft.interpolation?.fromObservedAt)],["Later bounding report",value(aircraft.interpolation?.toObservedAt)],["Position model",value(aircraft.interpolation?.model)]]],
    ["Height & movement",[["Pressure altitude",skyMeasurement(aircraft.altBaroFt," ft · pressure")],["Geometric height",skyMeasurement(aircraft.altGeomFt," ft · WGS84")],["Ground speed",skyMeasurement(aircraft.groundSpeedKt," kt",1)],["Indicated airspeed",skyMeasurement(aircraft.indicatedAirSpeedKt," kt",1)],["Mach",skyMeasurement(aircraft.mach,"",3)],["Reported ground track",skyMeasurement(aircraft.trackDeg,"°",1)],["Reported true heading",skyMeasurement(aircraft.trueHeadingDeg,"°",1)],["Estimated path direction",skyMeasurement(aircraft.renderedTrackDeg,"°",1)],[aircraft.interpolated?"Interpolated roll":"Reported roll",skyMeasurement(aircraft.rollDeg,"°",1)],["Vertical rate",skyMeasurement(aircraft.verticalRateFpm," ft/min")],["Vertical-rate reference",value(aircraft.verticalRateReference)]]],
    ["Status & signal quality",[["Squawk",value(aircraft.squawk)],["Emergency declaration",aircraft.emergency??"None reported"],["NIC · integrity category",value(quality?.nic)],["NACp · position accuracy",value(quality?.nacP)],["SIL · source integrity",value(quality?.sil)],["Containment radius",value(quality?.rcM," m")],["Signal strength",value(quality?.rssi," dBFS")],["Trace flags (raw)",value(aircraft.traceFlags)]]],
  ];
  return <details className="kansas-sky-dossier" open={expanded||undefined}><summary>Aircraft dossier <span>All available source fields</span></summary><p>Display precision is rounded for readability. Missing fields stay unavailable. These reports do not establish an owner, destination or mission. Signal categories are provider measurements, not a safety rating.</p>{aircraft.interpolated&&<p>Position and height are estimated within the displayed source bracket. Ground speed, ground track, identity, flags and observation time come from the earlier report. Other available motion instruments may be interpolated; the path direction is calculated separately.</p>}{groups.map(([title,rows])=><section key={title}><h6>{title}</h6><dl>{rows.map(([name,content])=><div key={name}><dt>{name}</dt><dd>{content}</dd></div>)}</dl></section>)}<details className="kansas-sky-exact-values"><summary>Exact displayed values</summary><p>{aircraft.interpolated?"These include calculated interpolation values, not extra measurement precision.":"Unrounded fields from this retained source report."}</p><pre>{JSON.stringify(aircraft,null,2)}</pre></details></details>;
}

export function SkyAltitudeProfile({points,cursor,canSeek,onSeek,compact=false,showRange=true}:{points:readonly SkyPoint[];cursor:number;canSeek:boolean;onSeek:(time:number)=>void;compact?:boolean;showRange?:boolean}){
  const profile=useMemo(()=>heightProfile(points),[points]);
  const chart=useMemo(()=>{
    const valid=profile.flat();if(!valid.length)return null;
    const start=points[0].observedAt,end=points.at(-1)!.observedAt;
    const heights=valid.map(p=>skyHeightFt(p)!);const low=Math.min(0,...heights),high=Math.max(1000,...heights)*1.05;
    const x=(t:number)=>32+(t-start)/Math.max(1,end-start)*272,y=(h:number)=>104-(h-low)/Math.max(1,high-low)*86;
    return {start,end,low,high,x,y,paths:profile.map(part=>({reference:skyHeightReference(part[0]),path:part.map((p,i)=>`${i?"L":"M"}${x(p.observedAt).toFixed(2)},${y(skyHeightFt(p)!).toFixed(2)}`).join(" "),startX:x(part[0].observedAt),endX:x(part.at(-1)!.observedAt),point:part.length===1?part[0]:null})),count:valid.length};
  },[profile,points]);
  if(!chart)return <p className="kansas-sky-profile-empty">Altitude profile unavailable: no reported airborne heights in this retained path.</p>;
  const at=Math.min(chart.end,Math.max(chart.start,cursor));
  const observation=samplesAt(new Map([[points[0].hex,points]]),at)[0],currentHeight=observation?skyHeightFt(observation):null;
  return <section className={`kansas-sky-profile${compact?" is-compact":""}`} aria-label="Aircraft altitude over time">
    <header><strong>Altitude journey</strong><span>{canSeek?"Select a moment":"Observed history"}</span></header>
    <svg viewBox="0 0 320 132" role="img" aria-label={`Reported altitude profile, ${time(chart.start)} to ${time(chart.end)}. Gold is WGS84 height; cyan is pressure altitude. Gaps are disconnected.`} onPointerDown={event=>{if(!canSeek||chart.start===chart.end)return;const rect=event.currentTarget.getBoundingClientRect();const x=(event.clientX-rect.left)/rect.width*320;onSeek(chart.start+Math.max(0,Math.min(1,(x-32)/272))*(chart.end-chart.start));}}>
      {[0,.5,1].map(f=><g key={f}><line x1="32" x2="304" y1={18+86*f} y2={18+86*f} className="sky-profile-grid"/><text x="27" y={21+86*f} textAnchor="end">{Math.round((chart.high-(chart.high-chart.low)*f)/1000)}k</text></g>)}
      {chart.paths.map((part,index)=><g key={index} className={part.reference==="WGS84"?"sky-profile-geom":"sky-profile-baro"}>{!part.point&&<path className="sky-profile-area" d={`${part.path} L${part.endX},104 L${part.startX},104 Z`}/>}<path d={part.path}/>{part.point&&<circle cx={chart.x(part.point.observedAt)} cy={chart.y(skyHeightFt(part.point)!)} r="2"/>}</g>)}
      <line className="sky-profile-cursor" x1={chart.x(at)} x2={chart.x(at)} y1="14" y2="108"/><circle className="sky-profile-time" cx={chart.x(at)} cy="109" r="3"/>
      {currentHeight!==null&&<circle className="sky-profile-position" cx={chart.x(at)} cy={chart.y(currentHeight)} r="3.5"/>}
      <text x="32" y="124">{time(chart.start)}</text><text x="304" y="124" textAnchor="end">{time(chart.end)}</text><text x="4" y="11">ft</text>
    </svg>
    {canSeek&&showRange&&chart.start!==chart.end&&<input type="range" aria-label={compact?"Map altitude profile time":"Altitude profile time"} min={chart.start} max={chart.end} step={100} value={at} aria-valuetext={new Date(at).toISOString()} onChange={event=>onSeek(Number(event.target.value))}/>}
    <small><span className="sky-profile-key-geom">WGS84</span> · <span className="sky-profile-key-baro">Pressure</span> · Separate height references; not MSL. {chart.count<points.length?`${chart.count} display points; gaps and missing heights remain.`:"Gaps remain disconnected."}</small>
  </section>;
}
