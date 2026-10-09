"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import seed from "./public-map-catalog.json";
import { canDownloadPublicMap, parsePublicMapCatalog, type PublicMapAsset, type PublicMapCatalog } from "./public-map-catalog";
import { parsePublicMapStatus, publicMapJobLabels, publicMapReason, publicMapRequest, type PublicMapEndpoint, type PublicMapStatus } from "./public-map-client";
import { automaticLocalConnection } from "./local-download-client";
import { observeDownloadTransitions } from "./download-activity";
import { startDownloadPolling } from "./download-polling";

type Options = { onTransferTerminal?: () => void; blockedByOtherDownload?: boolean };
export type PublicMapDownloads = ReturnType<typeof usePublicMapDownloads>;
export function usePublicMapDownloads(options: Options = {}) {
  const [catalog, setCatalog] = useState<PublicMapCatalog | null>(() => parsePublicMapCatalog(seed));
  const [status, setStatus] = useState<PublicMapStatus | null>(null);
  const [connection, setConnection] = useState<"idle" | "connecting" | "connected" | "unavailable">("idle");
  const [catalogError, setCatalogError] = useState<string | null>(null), [notice, setNotice] = useState("");
  const [announcement, setAnnouncement] = useState(""), [lastChecked, setLastChecked] = useState<string | null>(null);
  const [busy, setBusy] = useState<"refresh" | "download" | "cancel" | null>(null), [epoch, setEpoch] = useState(0);
  const [awaitingStatus, setAwaitingStatus] = useState(false);
  const life = useRef<AbortController | null>(null), current = useRef<PublicMapStatus | null>(null), ready = useRef(false);
  const operation = useRef(false), selected = useRef<string | null>(null), selectionVersion = useRef(0);
  const pending = useRef<{ key: string; id: string } | null>(null), jobs = useRef<Map<string, string> | null>(null);
  const previousRefresh = useRef<string | null>(null), catalogNeeded = useRef(true), callbacks = useRef(options);
  const poller = useRef<ReturnType<typeof startDownloadPolling> | null>(null);
  const acceptedStart = useRef<object | null>(null);
  useEffect(() => { callbacks.current = options; }, [options]);
  const connect = useCallback(() => { ready.current = false; catalogNeeded.current = true; setConnection("connecting"); setEpoch(value => value + 1); }, []);
  const refresh = useCallback(() => poller.current?.refresh(), []);
  useEffect(() => {
    const controller = new AbortController(); life.current = controller;
    if (automaticLocalConnection(window.location.origin)) queueMicrotask(() => { if (!controller.signal.aborted) connect(); });
    return () => { controller.abort(); ready.current = false; };
  }, [connect]);
  useEffect(() => {
    if (!epoch) return;
    const polling = startDownloadPolling(async signal => {
      const observedStart = acceptedStart.current;
      let parsed: PublicMapStatus;
      try {
        const result = await publicMapRequest("/status", signal), checked = result.response.ok ? parsePublicMapStatus(result.body) : null;
        if (!checked) throw new Error("Unrecognized local map service.");
        if (signal.aborted) return false;
        parsed = checked; current.current = parsed; ready.current = true;
        setStatus(parsed); setConnection("connected"); setLastChecked(new Date().toISOString());
        if (observedStart && observedStart === acceptedStart.current) { acceptedStart.current = null; setAwaitingStatus(false); }
        const observed = observeDownloadTransitions(jobs.current, parsed.jobs); jobs.current = observed.next;
        if (observed.changed.length) setAnnouncement(observed.changed.map(job => `${parsed.jobs.find(item => item.id === job.id)?.title}: ${publicMapJobLabels[job.state as keyof typeof publicMapJobLabels]}.`).join(" "));
        if (observed.terminal.length) callbacks.current.onTransferTerminal?.();
        const refreshComplete = parsed.refresh.state === "complete" && previousRefresh.current !== "complete";
        previousRefresh.current = parsed.refresh.state;
        if (catalogNeeded.current || refreshComplete) {
          // One cached read per connection or completed discovery, never per progress poll.
          catalogNeeded.current = false;
          try {
            const result = await publicMapRequest("/catalog", signal), checkedCatalog = result.response.ok ? parsePublicMapCatalog(result.body) : null;
            if (!checkedCatalog) throw new Error("Invalid catalog");
            if (!signal.aborted) { setCatalog(checkedCatalog); setCatalogError(null); }
          } catch {
            catalogNeeded.current = true;
            if (!signal.aborted) setCatalogError("The current catalog is unavailable. Previously checked metadata remains visible; current statewide completeness is unknown.");
          }
        }
      } catch {
        if (!signal.aborted) { ready.current = false; setConnection("unavailable"); setAnnouncement("Map downloads are unavailable. Retained jobs may be out of date; the reference catalog remains available."); }
        return false;
      }
      return parsed.active !== null || Boolean(parsed.queued) || parsed.refresh.state === "running";
    });
    poller.current = polling;
    return () => { polling.dispose(); if (poller.current === polling) poller.current = null; };
  }, [epoch]);

  const selectAsset = useCallback((assetId: string | null) => {
    if (selected.current === assetId) return;
    selected.current = assetId; selectionVersion.current++; pending.current = null; setNotice("");
  }, []);
  const action = useCallback(async (path: PublicMapEndpoint, payload: unknown, kind: "refresh" | "download" | "cancel", selectionBound = false) => {
    const controller = life.current, active = current.current, version = selectionVersion.current;
    if (!controller || controller.signal.aborted || !active || !ready.current || operation.current) return null;
    operation.current = true; setBusy(kind); setNotice("");
    try {
      const result = await publicMapRequest(path, controller.signal, payload, active.sessionToken);
      if (controller.signal.aborted || life.current !== controller) return null;
      return { ...result, relevant: !selectionBound || version === selectionVersion.current };
    } catch {
      if (!controller.signal.aborted && life.current === controller && (!selectionBound || version === selectionVersion.current)) {
        setNotice(kind === "download" ? "Start was not confirmed. Check Activity before retrying; the same selection retains its request ID." : "The request was not confirmed. Reconnect to inspect its current state before retrying.");
      }
      return null;
    } finally {
      if (life.current === controller) { operation.current = false; if (!controller.signal.aborted) setBusy(null); }
    }
  }, []);
  const startDownload = useCallback(async (asset: PublicMapAsset, maxBytes: number) => {
    if (operation.current || acceptedStart.current || !ready.current || current.current?.active || callbacks.current.blockedByOtherDownload
      || !canDownloadPublicMap(asset) || !Number.isSafeInteger(maxBytes) || maxBytes < 1 || maxBytes > (current.current?.limitBytes ?? 0)
      || asset.expectedBytes !== null && maxBytes < asset.expectedBytes) return;
    const key = JSON.stringify([asset.id, maxBytes]);
    const request = pending.current?.key === key ? pending.current : { key, id: crypto.randomUUID().replaceAll("-", "") };
    pending.current = request;
    const result = await action("/downloads", { requestId: request.id, assetId: asset.id, maxBytes }, "download", true);
    if (!result) { refresh(); return; }
    const body = result.body as { id?: string; assetId?: string; maxBytes?: number; mapReady?: boolean; error?: string } | null;
    // HTTP failure may still follow an accepted operation; only clear after confirmation.
    const confirmed = result.response.ok && body?.id === request.id && body.assetId === asset.id && body.maxBytes === maxBytes && body.mapReady === false;
    if (confirmed && pending.current === request) pending.current = null;
    if (confirmed) { acceptedStart.current = {}; setAwaitingStatus(true); }
    if (result.relevant) setNotice(confirmed ? "Download started. Follow its progress in Activity; captured originals remain candidates."
      : `${body?.error ? publicMapReason(body.error) + " " : ""}Start was not confirmed. Check Activity before retrying; this selection retains its request ID.`);
    refresh();
  }, [action, refresh]);
  /** Queue several verified files under one maximum per file; the local operator runs them in order. */
  const startQueue = useCallback(async (assets: readonly PublicMapAsset[], maxBytes: number) => {
    if (operation.current || acceptedStart.current || !ready.current || current.current?.active || current.current?.queued || callbacks.current.blockedByOtherDownload
      || !assets.length || assets.length > 300 || !assets.every(canDownloadPublicMap) || !Number.isSafeInteger(maxBytes) || maxBytes < 1 || maxBytes > (current.current?.limitBytes ?? 0)
      || assets.some(asset => asset.expectedBytes !== null && maxBytes < asset.expectedBytes)) return;
    const key = JSON.stringify([assets.map(asset => asset.id), maxBytes]);
    const request = pending.current?.key === key ? pending.current : { key, id: crypto.randomUUID().replaceAll("-", "") };
    pending.current = request;
    const result = await action("/queue", { requestId: request.id, assetIds: assets.map(asset => asset.id), maxBytes }, "download");
    if (!result) { refresh(); return; }
    const body = result.body as { batchId?: string; jobs?: number; mapReady?: boolean; error?: string } | null;
    const confirmed = result.response.ok && body?.batchId === request.id && body.jobs === assets.length && body.mapReady === false;
    if (confirmed && pending.current === request) pending.current = null;
    if (confirmed) { acceptedStart.current = {}; setAwaitingStatus(true); }
    setNotice(confirmed ? `${assets.length} files queued. They download one at a time; follow progress in Activity. Captured originals remain candidates.`
      : `${body?.error ? publicMapReason(body.error) + " " : ""}The queue was not confirmed. Check Activity before retrying; this selection retains its request ID.`);
    refresh();
  }, [action, refresh]);
  const cancelQueue = useCallback(async () => {
    if (!current.current?.queued) return;
    const result = await action("/queue/cancel", {}, "cancel");
    if (result?.response.ok) { setNotice("Queued files cancelled and the running file is stopping. Captured bytes remain available for inspection."); refresh(); }
    else if (result) setNotice("Cancelling the queue was not confirmed. Reconnect to inspect its current state.");
  }, [action, refresh]);
  const refreshCatalog = useCallback(async () => {
    if (current.current?.refresh.state === "running") return;
    const result = await action("/refresh", {}, "refresh");
    if (result?.response.ok) { previousRefresh.current = "running"; setNotice("Kansas catalog refresh requested. Existing records remain available while sources are checked."); refresh(); }
    else if (result) setNotice("Catalog refresh was not confirmed. Reconnect to inspect its current state.");
  }, [action, refresh]);
  const cancelJob = useCallback(async (id: string) => {
    if (current.current?.active !== id) return;
    const result = await action("/cancel", { id }, "cancel");
    if (result?.response.ok) { setNotice("Cancellation requested. Captured bytes remain available for inspection."); refresh(); }
    else if (result) setNotice("Cancellation was not confirmed. Reconnect to inspect the active job.");
  }, [action, refresh]);
  return { catalog, status, connection, catalogError, notice, announcement, lastChecked, connect, refresh, refreshCatalog, startDownload, startQueue, cancelQueue, cancelJob, selectAsset,
    busy: busy ?? (awaitingStatus ? "download" as const : null) };
}
