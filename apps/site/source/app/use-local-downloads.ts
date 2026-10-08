"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import { automaticLocalConnection, jobStateLabels, localDownloadRequest, parseDownloadStatus, parseLocalLibrary, type DownloadEndpoint, type DownloadStatus, type LocalLibrary } from "./local-download-client";

export function useLocalDownloads() {
  const [requested, setRequested] = useState(false), [revision, setRevision] = useState(0);
  const [connection, setConnection] = useState<"idle" | "connecting" | "connected" | "unavailable">("idle");
  const [status, setStatus] = useState<DownloadStatus | null>(null), [library, setLibrary] = useState<LocalLibrary | null>(null);
  const [libraryError, setLibraryError] = useState<string | null>(null), [announcement, setAnnouncement] = useState("");
  const [actionNotice, setActionNotice] = useState("");
  const [lastChecked, setLastChecked] = useState<string | null>(null), [refreshingLibrary, setRefreshingLibrary] = useState(false), [cancelling, setCancelling] = useState(false);
  const life = useRef<AbortController | null>(null), currentStatus = useRef<DownloadStatus | null>(null), ready = useRef(false);
  const previous = useRef<{ jobs: Map<string, string>; library: string | null; connected: boolean }>({ jobs: new Map(), library: null, connected: false });
  const connect = useCallback(() => { ready.current = false; setConnection("connecting"); setRequested(true); setRevision(value => value + 1); }, []);
  const refresh = useCallback(() => setRevision(value => value + 1), []);
  useEffect(() => {
    const controller = new AbortController(); life.current = controller;
    // This opt-in is limited to the established local Site origin, after hydration.
    if (automaticLocalConnection(window.location.origin)) queueMicrotask(() => { if (!controller.signal.aborted) connect(); });
    return () => { controller.abort(); ready.current = false; };
  }, [connect]);
  useEffect(() => {
    if (!requested) return;
    let disposed = false, running = false, resumeOnReturn = false, timer: ReturnType<typeof setTimeout> | undefined, round: AbortController | null = null;
    const isVisible = () => document.visibilityState !== "hidden";
    const run = async () => {
      if (disposed || running || !isVisible()) return;
      running = true; const controller = new AbortController(); round = controller;
      let fast = false;
      try {
        const results = await Promise.allSettled([
          localDownloadRequest("/status", controller.signal), localDownloadRequest("/library", controller.signal),
        ]);
        if (disposed || controller.signal.aborted) return;
        const statusResult = results[0], libraryResult = results[1];
        const checkedStatus = statusResult.status === "fulfilled" && statusResult.value.response.ok ? parseDownloadStatus(statusResult.value.body) : null;
        const messages: string[] = [];
        if (checkedStatus) {
          currentStatus.current = checkedStatus; ready.current = true; setStatus(checkedStatus); setConnection("connected");
          if (!previous.current.connected) messages.push("Connected to this computer’s download service.");
          for (const job of checkedStatus.jobs) {
            const prior = previous.current.jobs.get(job.id);
            if (prior && prior !== job.state) messages.push(`${job.selection.dataset}, ${job.selection.year ?? "fixed period"}: ${jobStateLabels[job.state]}.`);
          }
          previous.current.jobs = new Map(checkedStatus.jobs.map(job => [job.id, job.state]));
          previous.current.connected = true; fast = checkedStatus.active !== null || checkedStatus.authentication === "validating";
          setLastChecked(new Date().toISOString());
        } else {
          ready.current = false; setConnection("unavailable");
          if (previous.current.connected || !currentStatus.current) messages.push("Local downloads are unavailable. Last known jobs may be out of date; reconnect before retrying a download.");
          previous.current.connected = false;
        }
        const checkedLibrary = libraryResult.status === "fulfilled" && libraryResult.value.response.ok ? parseLocalLibrary(libraryResult.value.body) : null;
        if (checkedLibrary) {
          setLibrary(checkedLibrary); setLibraryError(null); fast ||= checkedLibrary.state === "scanning";
          if (previous.current.library !== checkedLibrary.state) {
            if (checkedLibrary.state === "scanning") messages.push("Scanning the local library in the background.");
            if (checkedLibrary.state === "complete") messages.push("Local library scan complete.");
            if (checkedLibrary.state === "failed") messages.push("Library scan could not finish. Any previous snapshot remains visible.");
          }
          previous.current.library = checkedLibrary.state;
        } else {
          setLibraryError(libraryResult.status === "fulfilled" && libraryResult.value.response.status === 404
            ? "This local service does not support library summaries yet. Update the local service, then reconnect."
            : "The library could not be checked. Any previous scan remains visible; current storage is unknown.");
        }
        if (messages.length) setAnnouncement(messages.join(" "));
      } finally {
        running = false;
        if (!disposed && isVisible()) { const delay = resumeOnReturn ? 0 : fast ? 2500 : 15000; resumeOnReturn = false; timer = setTimeout(() => void run(), delay); }
      }
    };
    const visibility = () => {
      if (timer !== undefined) clearTimeout(timer);
      if (document.visibilityState === "hidden") round?.abort(); else if (running) resumeOnReturn = true; else void run();
    };
    document.addEventListener("visibilitychange", visibility); void run();
    return () => { disposed = true; round?.abort(); if (timer !== undefined) clearTimeout(timer); document.removeEventListener("visibilitychange", visibility); };
  }, [requested, revision]);

  const post = useCallback(async (path: DownloadEndpoint, payload: unknown) => {
    const controller = life.current, active = currentStatus.current;
    if (!controller || !active || !ready.current) throw new Error("Connect local downloads before continuing.");
    return localDownloadRequest(path, controller.signal, payload, active.sessionToken);
  }, []);
  const refreshLibrary = async () => {
    if (refreshingLibrary) return;
    setRefreshingLibrary(true);
    try {
      const { response, body } = await post("/library/refresh", {}), checked = response.ok ? parseLocalLibrary(body) : null;
      if (!checked) throw new Error("The library scan was not confirmed. Reconnect to check before retrying.");
      if (!life.current?.signal.aborted) { setLibrary(checked); setLibraryError(null); setAnnouncement("Library refresh requested. Existing results remain visible while the scan runs."); refresh(); }
    } catch (error) { if (!life.current?.signal.aborted) setLibraryError(error instanceof Error ? error.message : "Library refresh was not confirmed."); }
    finally { if (!life.current?.signal.aborted) setRefreshingLibrary(false); }
  };
  const cancelJob = async () => {
    if (cancelling || !currentStatus.current?.active) return;
    setCancelling(true);
    try {
      const { response } = await post("/cancel", { id: currentStatus.current.active });
      if (!response.ok) throw new Error("Cancellation was not confirmed. Reconnect to inspect the running job.");
      if (!life.current?.signal.aborted) { const message = "Cancellation requested. The current provider request may take up to 90 seconds to finish. Partial files will be retained."; setAnnouncement(message); setActionNotice(message); refresh(); }
    } catch (error) { if (!life.current?.signal.aborted) { const message = error instanceof Error ? error.message : "Cancellation was not confirmed."; setAnnouncement(message); setActionNotice(message); } }
    finally { if (!life.current?.signal.aborted) setCancelling(false); }
  };
  return { status, library, connection, libraryError, lastChecked, announcement, actionNotice, connect, refresh, post, refreshingLibrary, refreshLibrary, cancelling, cancelJob };
}
