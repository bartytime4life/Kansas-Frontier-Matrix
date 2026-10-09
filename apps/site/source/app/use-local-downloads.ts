"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import { automaticLocalConnection, jobStateLabels, localDownloadRequest, parseDownloadStatus, parseLocalLibrary, type DownloadEndpoint, type DownloadStatus, type LocalLibrary } from "./local-download-client";
import { observeDownloadTransitions } from "./download-activity";
import { startDownloadPolling } from "./download-polling";

export type LocalDownloads = ReturnType<typeof useLocalDownloads>;
export function useLocalDownloads() {
  const [epoch, setEpoch] = useState(0), [starting, setStartingState] = useState(false);
  const [connection, setConnection] = useState<"idle" | "connecting" | "connected" | "unavailable">("idle");
  const [status, setStatus] = useState<DownloadStatus | null>(null), [library, setLibrary] = useState<LocalLibrary | null>(null);
  const [libraryError, setLibraryError] = useState<string | null>(null), [announcement, setAnnouncement] = useState("");
  const [actionNotice, setActionNotice] = useState("");
  const [lastChecked, setLastChecked] = useState<string | null>(null), [refreshingLibrary, setRefreshingLibrary] = useState(false), [cancelling, setCancelling] = useState(false);
  const life = useRef<AbortController | null>(null), currentStatus = useRef<DownloadStatus | null>(null), ready = useRef(false);
  const currentLibrary = useRef<LocalLibrary | null>(null), refreshQueued = useRef(false);
  const libraryGeneration = useRef<object>({});
  const previous = useRef<{ jobs: Map<string, string> | null; library: string | null; connected: boolean }>({ jobs: null, library: null, connected: false });
  const refreshing = useRef(false), cancellingNow = useRef(false), poller = useRef<ReturnType<typeof startDownloadPolling> | null>(null);
  const startPhase = useRef<{ state: "idle" | "posting" | "accepted" }>({ state: "idle" });
  const setStarting = useCallback((value: boolean) => { startPhase.current = { state: value ? "posting" : "idle" }; setStartingState(value); }, []);
  const confirmStart = useCallback(() => { startPhase.current = { state: "accepted" }; }, []);
  const connect = useCallback(() => { ready.current = false; setConnection("connecting"); setEpoch(value => value + 1); }, []);
  const refresh = useCallback(() => poller.current?.refresh(), []);
  const post = useCallback(async (path: DownloadEndpoint, payload: unknown) => {
    const controller = life.current, active = currentStatus.current;
    if (!controller || controller.signal.aborted || !active || !ready.current) throw new Error("Connect local downloads before continuing.");
    const result = await localDownloadRequest(path, controller.signal, payload, active.sessionToken);
    controller.signal.throwIfAborted();
    return result;
  }, []);
  const refreshLibrary = useCallback(async () => {
    // The worker coalesces refresh requests during a scan. Retain one trailing
    // request so a newly captured file is not missed by an already-passed path.
    if (refreshing.current || currentLibrary.current?.state === "scanning") { refreshQueued.current = true; return; }
    const controller = life.current;
    if (!controller || controller.signal.aborted) return;
    if (!ready.current) { refreshQueued.current = true; return; }
    refreshing.current = true; setRefreshingLibrary(true);
    try {
      const { response, body } = await post("/library/refresh", {}), checked = response.ok ? parseLocalLibrary(body) : null;
      if (!checked) throw new Error("The library scan was not confirmed. Reconnect to check before retrying.");
      if (!controller.signal.aborted && life.current === controller) {
        // Retire reads issued before this acknowledgement. They can still carry
        // the previous completed scan even after the worker has begun a new one.
        libraryGeneration.current = {};
        currentLibrary.current = checked; setLibrary(checked); setLibraryError(null); setAnnouncement("Library refresh requested. Existing results remain visible while the scan runs."); refresh();
      }
    } catch (error) { if (!controller.signal.aborted && life.current === controller) setLibraryError(error instanceof Error ? error.message : "Library refresh was not confirmed."); }
    finally { if (life.current === controller) { refreshing.current = false; if (!controller.signal.aborted) setRefreshingLibrary(false); } }
  }, [post, refresh]);
  useEffect(() => {
    const controller = new AbortController(); life.current = controller;
    if (automaticLocalConnection(window.location.origin)) queueMicrotask(() => { if (!controller.signal.aborted) connect(); });
    return () => { controller.abort(); ready.current = false; };
  }, [connect]);
  useEffect(() => {
    if (!epoch) return;
    const polling = startDownloadPolling(async signal => {
      const observedStart = startPhase.current;
      const observedLibrary = libraryGeneration.current;
      const results = await Promise.allSettled([localDownloadRequest("/status", signal), localDownloadRequest("/library", signal)]);
      if (signal.aborted) return false;
      const statusResult = results[0], libraryResult = results[1];
      const checkedStatus = statusResult.status === "fulfilled" && statusResult.value.response.ok ? parseDownloadStatus(statusResult.value.body) : null;
      const messages: string[] = []; let fast = false, terminal = false;
      if (checkedStatus) {
        currentStatus.current = checkedStatus; ready.current = true; setStatus(checkedStatus); setConnection("connected");
        if (observedStart.state === "accepted" && startPhase.current === observedStart) setStarting(false);
        if (!previous.current.connected) messages.push("Connected to this computer’s download service.");
        const observed = observeDownloadTransitions(previous.current.jobs, checkedStatus.jobs);
        for (const job of observed.changed) {
          const native = checkedStatus.jobs.find(item => item.id === job.id)!;
          messages.push(`${native.selection.dataset}, ${native.selection.year ?? "fixed period"}: ${jobStateLabels[native.state]}.`);
        }
        previous.current.jobs = observed.next; terminal = observed.terminal.length > 0;
        previous.current.connected = true; fast = checkedStatus.active !== null || ["validating", "waiting"].includes(checkedStatus.authentication ?? "");
        setLastChecked(new Date().toISOString());
      } else {
        ready.current = false; setConnection("unavailable");
        if (previous.current.connected || !currentStatus.current) messages.push("Local downloads are unavailable. Last known jobs may be out of date; reconnect before retrying a download.");
        previous.current.connected = false;
      }
      const libraryCurrent = observedLibrary === libraryGeneration.current;
      const checkedLibrary = libraryCurrent && libraryResult.status === "fulfilled" && libraryResult.value.response.ok ? parseLocalLibrary(libraryResult.value.body) : null;
      if (checkedLibrary) {
        currentLibrary.current = checkedLibrary; setLibrary(checkedLibrary); setLibraryError(null); fast ||= checkedLibrary.state === "scanning";
        if (previous.current.library !== checkedLibrary.state) {
          if (checkedLibrary.state === "scanning") messages.push("Scanning the local library in the background.");
          if (checkedLibrary.state === "complete") messages.push("Local library scan complete.");
          if (checkedLibrary.state === "failed") messages.push("Library scan could not finish. Any previous snapshot remains visible.");
        }
        previous.current.library = checkedLibrary.state;
      } else if (libraryCurrent) {
        setLibraryError(libraryResult.status === "fulfilled" && libraryResult.value.response.status === 404
          ? "This local service does not support library summaries yet. Update the local service, then reconnect."
          : "The library could not be checked. Any previous scan remains visible; current storage is unknown.");
      }
      if (messages.length) setAnnouncement(messages.join(" "));
      if (terminal || refreshQueued.current && checkedStatus && checkedLibrary && checkedLibrary.state !== "scanning") {
        refreshQueued.current = false;
        void refreshLibrary();
      }
      fast ||= currentLibrary.current?.state === "scanning";
      return fast;
    });
    poller.current = polling;
    return () => { polling.dispose(); if (poller.current === polling) poller.current = null; };
  }, [epoch, refreshLibrary, setStarting]);
  const cancelJob = useCallback(async () => {
    if (cancellingNow.current || !currentStatus.current?.active) return;
    const controller = life.current;
    if (!controller || controller.signal.aborted) return;
    cancellingNow.current = true; setCancelling(true);
    try {
      const { response } = await post("/cancel", { id: currentStatus.current.active });
      if (!response.ok) throw new Error("Cancellation was not confirmed. Reconnect to inspect the running job.");
      if (!controller.signal.aborted && life.current === controller) { const message = "Cancellation requested. The current provider request may take up to 90 seconds to finish. Partial files will be retained."; setAnnouncement(message); setActionNotice(message); refresh(); }
    } catch (error) { if (!controller.signal.aborted && life.current === controller) { const message = error instanceof Error ? error.message : "Cancellation was not confirmed."; setAnnouncement(message); setActionNotice(message); } }
    finally { if (life.current === controller) { cancellingNow.current = false; if (!controller.signal.aborted) setCancelling(false); } }
  }, [post, refresh]);
  return { status, library, connection, libraryError, lastChecked, announcement, actionNotice, connect, refresh, post, refreshingLibrary, refreshLibrary, cancelling, cancelJob, starting, setStarting, confirmStart };
}
