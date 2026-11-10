"use client";

import { useId, useLayoutEffect, useRef } from "react";
import { MAX_PLACE_TRAIL_STOPS, PLACES_FULL_MESSAGE } from "./places-trail";
import styles from "./places-save-controls.module.css";

export type PlacesControlContext = "places" | "workspace";
export type PlacesFocusRequest = Readonly<{ version: number; context: PlacesControlContext; target: "name" | "undo" }>;

export function PlacesSaveControls({ context, count, name, notice, removedName, focusRequest, onName, onSave, onUndo, onBackup }: {
  context: PlacesControlContext;
  count: number;
  name: string;
  notice: string;
  removedName: string | null;
  focusRequest: PlacesFocusRequest | null;
  onName: (name: string) => void;
  onSave: () => void;
  onUndo: () => void;
  onBackup: () => void;
}) {
  const id = useId();
  const nameRef = useRef<HTMLInputElement>(null);
  const undoRef = useRef<HTMLButtonElement>(null);
  const full = count >= MAX_PLACE_TRAIL_STOPS;
  useLayoutEffect(() => {
    if (focusRequest?.context !== context) return;
    const node = focusRequest.target === "undo" ? undoRef.current : nameRef.current;
    if (node && !node.closest('[hidden], [inert], [aria-hidden="true"]') && node.getClientRects().length) node.focus();
  }, [context, focusRequest]);

  return <div className={styles.controls}>
    <form aria-label={context === "places" ? "Save a place" : "Save a workspace"} onSubmit={event => { event.preventDefault(); onSave(); }}>
      <label htmlFor={`${id}-name`}>Place name <span>(optional)</span></label>
      <div className={styles.row}>
        <input ref={nameRef} id={`${id}-name`} type="text" value={name} maxLength={50} aria-describedby={`${id}-capacity`}
          onChange={event => onName(event.target.value.slice(0, 50))} placeholder="Name this investigation step" />
        <button type="submit" disabled={full}>{context === "places" ? "Add place" : "Save current"}</button>
      </div>
      <p id={`${id}-capacity`} className={styles.capacity}>{count} of {MAX_PLACE_TRAIL_STOPS} places saved. {full ? PLACES_FULL_MESSAGE : "Saved only in this browser."}</p>
    </form>
    <div className={styles.feedback} role="status" aria-live="polite" aria-atomic="true">
      {notice && <p>{notice}</p>}
      {removedName && <div className={styles.undo}>
        <button ref={undoRef} type="button" onClick={onUndo} aria-label={`Undo removal of ${removedName}`}>Undo removal</button>
        <small>Undo stays available until you change the list or reload.</small>
      </div>}
    </div>
    <div className={styles.backup}>
      <button type="button" onClick={onBackup}>Download Places backup</button>
      <small>A recovery file containing your original stored data, including unreadable records. It may contain private place names and locations.</small>
    </div>
  </div>;
}
