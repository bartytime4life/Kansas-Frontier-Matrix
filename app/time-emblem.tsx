"use client";
import { useEffect, useState } from "react";
const eras = ["Hourglass", "Stone toolmaker", "Medieval knight", "Civil War era", "Internet", "AI", "Imagined future"];
/** Era illustrations are decorative UI art, never a clock or a coverage claim. */
export function TimeEmblem({ animated, reducedMotion, visible = true }: { animated: boolean; reducedMotion: boolean; visible?: boolean }) {
  const [era, setEra] = useState(0), [hidden, setHidden] = useState(false);
  const moving = animated && !reducedMotion && visible && !hidden;
  useEffect(() => {
    const sync = () => setHidden(document.hidden);
    document.addEventListener("visibilitychange", sync);
    const initial = window.setTimeout(sync, 0);
    return () => { window.clearTimeout(initial); document.removeEventListener("visibilitychange", sync); };
  }, []);
  useEffect(() => {
    if (!moving) return;
    const timer = window.setTimeout(() => setEra(current => (current + 1) % eras.length), 3200);
    return () => window.clearTimeout(timer);
  }, [era, moving]);
  return <span key={moving ? era : 0} className="time-emblem-sprite" aria-hidden="true" data-era={eras[moving ? era : 0]} data-moving={moving} style={{ backgroundPositionY: ((moving ? era : 0) / 6 * 100) + "%" }} />;
}
