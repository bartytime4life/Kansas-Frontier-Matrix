"use client";
import { useEffect, useState } from "react";
/** Decorative ten-second sand transfer. It never changes map time or coverage. */
export function TimeEmblem({ animated, reducedMotion, visible = true }: { animated: boolean; reducedMotion: boolean; visible?: boolean }) {
 const [hidden,setHidden]=useState(()=>typeof document!=="undefined"&&document.hidden);
 useEffect(()=>{const sync=()=>setHidden(document.hidden);document.addEventListener("visibilitychange",sync);return()=>document.removeEventListener("visibilitychange",sync);},[]);
 const moving=animated&&!reducedMotion&&visible&&!hidden;
 return <span className="time-hourglass" aria-hidden="true" data-moving={moving}><span className="time-hourglass-sand" /></span>;
}
