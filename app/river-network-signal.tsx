"use client";
import { useMemo, type CSSProperties } from "react";
import { riverSignalGroups } from "./river-pulse-visuals";
import type { StreamflowFrame } from "./streamflow";

export function RiverNetworkSignal({ frame, selected, onSelect }: {
  frame: StreamflowFrame | null; selected: string | null; onSelect: (id: string) => void;
}) {
  const groups = useMemo(() => riverSignalGroups(frame), [frame]);
  const total = groups.reduce((sum, group) => sum + group.stations.length, 0);
  const reporting = total - groups.at(-1)!.stations.length;
  const precedingCounts = groups.map((_, index) => groups.slice(0, index).reduce((sum, group) => sum + group.stations.length, 0));
  return <section className="river-network-signal" aria-label="Gauge conditions at the selected frame">
    <div className="river-network-dial">
      <svg viewBox="0 0 120 120" aria-hidden="true">
        <circle cx="60" cy="60" r="49" fill="none" stroke="#19333e" strokeWidth="8" />
        {groups.map((group, index) => {
          const fraction = total ? group.stations.length / total : 0;
          const start = total ? precedingCounts[index] / total : 0;
          return fraction > 0 ? <circle key={group.id} cx="60" cy="60" r="49" fill="none" stroke={group.color} strokeWidth="8" pathLength="100"
            strokeDasharray={`${Math.max(0, fraction * 100 - 0.8)} 100`} strokeDashoffset={-start * 100} transform="rotate(-90 60 60)" /> : null;
        })}
      </svg>
      <div><strong>{total ? Math.round(reporting / total * 100) : "—"}<small>{total ? "%" : ""}</small></strong><span>reporting</span></div>
    </div>
    <div className="river-network-content"><header><span>NETWORK AT THIS FRAME</span><strong>{reporting}<small> / {total} gauges</small></strong></header>
      <div className="river-signal-buttons">{groups.map(group => <button key={group.id} type="button" style={{ "--signal": group.color } as CSSProperties}
        disabled={!group.stations.length} aria-label={`${group.label}: ${group.stations.length} gauges. Select next gauge.`}
        onClick={() => onSelect(group.stations[(group.stations.indexOf(selected ?? "") + 1) % group.stations.length])}>
        <i aria-hidden="true" /><span>{group.label}</span><b>{group.stations.length}</b></button>)}</div>
      <small>Select a condition to cycle through its gauges.</small>
    </div>
  </section>;
}
