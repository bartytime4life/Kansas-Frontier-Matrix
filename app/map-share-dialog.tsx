"use client";

import { useLayoutEffect, useRef, useState } from "react";
import { modalFocusableElements, modalReturnTarget } from "./modal-background";
import styles from "./map-share-dialog.module.css";

export type MapShareRequest = Readonly<{
  url: string;
  redacted: boolean;
  initialCopy: Promise<boolean>;
  returnTarget: HTMLElement | null;
}>;

// Start from the activating click, preserving browser clipboard user activation.
export async function copyMapLink(url: string): Promise<boolean> {
  try { await navigator.clipboard.writeText(url); return true; }
  catch { return false; }
}

export function MapShareDialog({ request, fallbackTarget, onClose }: {
  request: MapShareRequest;
  fallbackTarget: HTMLElement | null;
  onClose: () => void;
}) {
  const dialogRef = useRef<HTMLDialogElement>(null);
  const linkRef = useRef<HTMLTextAreaElement>(null);
  const sequence = useRef({ value: 0 });
  const [status, setStatus] = useState<"copying" | "copied" | "manual">("copying");

  const watchCopy = (result: Promise<boolean>) => {
    const token = sequence.current;
    const attempt = ++token.value;
    setStatus("copying");
    void result.then(copied => {
      if (token.value === attempt) setStatus(copied ? "copied" : "manual");
    });
  };

  useLayoutEffect(() => {
    const dialog = dialogRef.current;
    if (!dialog) return;
    const handleKey = (event: KeyboardEvent) => {
      // Own the event at the dialog before existing document listeners run.
      // React's delegated handler can run after those workspace shortcuts.
      event.stopPropagation();
      if (event.key === "Escape") { event.preventDefault(); onClose(); }
      if (event.key === "Tab") {
        const items = modalFocusableElements(dialog);
        const next = event.shiftKey ? items.at(-1) : items[0];
        if (document.activeElement === (event.shiftKey ? items[0] : items.at(-1))) {
          event.preventDefault();
          next?.focus();
        }
      }
    };
    dialog.addEventListener("keydown", handleKey);
    dialog.showModal();
    linkRef.current?.focus();
    linkRef.current?.select();
    return () => {
      dialog.removeEventListener("keydown", handleKey);
      dialog.close();
      modalReturnTarget(request.returnTarget, fallbackTarget)?.focus({ preventScroll: true });
    };
  }, [request.returnTarget, fallbackTarget, onClose]);

  useLayoutEffect(() => {
    const token = sequence.current;
    const attempt = ++token.value;
    void request.initialCopy.then(copied => {
      if (token.value === attempt) setStatus(copied ? "copied" : "manual");
    });
    return () => { token.value++; };
  }, [request.initialCopy]);

  return <dialog ref={dialogRef} id="map-share-dialog" className={styles.dialog}
    aria-labelledby="map-share-title" aria-describedby="map-share-description"
    onCancel={event => { event.preventDefault(); onClose(); }}>
    <header className={styles.heading}>
      <div><span>MAP LINK</span><h2 id="map-share-title">Share this map view</h2></div>
      <button type="button" className={styles.close} onClick={onClose} aria-label="Close share dialog">×</button>
    </header>
    <p id="map-share-description">This link reopens the captured map settings. Source availability and observations may change.</p>
    {request.redacted && <p className={styles.privacy}>Location-derived camera replaced with statewide Kansas. The analysis area is omitted.</p>}
    <label className={styles.link}>
      <span>Map link</span>
      <textarea ref={linkRef} readOnly rows={4} value={request.url} spellCheck={false} autoCapitalize="off"
        aria-describedby="map-share-status" onFocus={event => event.currentTarget.select()} />
    </label>
    <p id="map-share-status" className={styles.status} role="status" aria-live="polite" aria-atomic="true">
      {status === "copying" ? "Copying link… You can also select and copy it yourself."
        : status === "copied" ? "Link copied."
        : "Automatic copying is unavailable. Select the link and copy it using your browser."}
    </p>
    <div className={styles.actions}>
      <button type="button" onClick={() => watchCopy(copyMapLink(request.url))}>{status === "copied" ? "Copy again" : "Copy link"}</button>
      <button type="button" onClick={() => { linkRef.current?.focus(); linkRef.current?.select(); }}>Select link</button>
      <button type="button" onClick={onClose}>Done</button>
    </div>
  </dialog>;
}
