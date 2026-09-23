"use client";

import { boundedUtcDay, utcDayFromOrdinal, utcDayOrdinal } from "./source-time";

type ArchiveDaySliderProps = {
  sourceLabel: string;
  minDay: string;
  maxDay: string;
  day: string;
  nextAction: string;
  onSelect: (day: string) => void;
};

/** Selecting a date is a draft action. The caller's check/open action queries it. */
export function ArchiveDaySlider({ sourceLabel, minDay, maxDay, day, nextAction, onSelect }: ArchiveDaySliderProps) {
  const selectedDay = boundedUtcDay(day, minDay, maxDay);
  const hasDraft = utcDayOrdinal(day) !== null;
  const min = utcDayOrdinal(minDay);
  const max = utcDayOrdinal(maxDay);
  if (!selectedDay || min === null || max === null) return null;

  return <div className="archive-day-range">
    <div><span>OLDER DAY</span><strong>{selectedDay} UTC · {hasDraft ? "draft" : "move to select"}</strong></div>
    <input
      type="range"
      min={min}
      max={max}
      step={1}
      value={utcDayOrdinal(selectedDay) ?? max}
      onChange={(event) => onSelect(utcDayFromOrdinal(Number(event.target.value)))}
      aria-label={`${sourceLabel} older UTC day`}
      aria-valuetext={`${selectedDay} UTC ${hasDraft ? "draft" : "suggested day; move the slider to select"}. ${nextAction} to check records.`}
    />
    <small>{minDay} → {maxDay} · Select a day, then {nextAction}. Days between bounds may have no records.</small>
  </div>;
}
