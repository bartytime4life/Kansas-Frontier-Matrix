"use client";
import { useEffect, useState } from "react";
import { basemapCacheAction, basemapCacheEnabled, connectBasemapCache, setBasemapCacheEnabled, type BasemapCacheStatus } from "./basemap-cache";

export function BasemapCacheControls() {
  const [status, setStatus] = useState<BasemapCacheStatus | null>(null);
  const [enabled, setEnabled] = useState(true);
  const [message, setMessage] = useState("Checking this computer’s basemap cache…");
  const [busy, setBusy] = useState(false);
  useEffect(() => {
    let active = true;
    setEnabled(basemapCacheEnabled());
    const refresh = () => { void connectBasemapCache(true).then(s => { if (active) { setStatus(s); setMessage(s ? "Connected to this PC" : "PC cache unavailable · maps use the provider directly"); } }); };
    refresh(); const timer = setInterval(refresh, 10_000);
    return () => { active = false; clearInterval(timer); };
  }, []);
  const action = async (name: "overview" | "cancel" | "connect") => {
    setBusy(true);
    try { const s = name === "connect" ? await connectBasemapCache(true) : await basemapCacheAction(name); setStatus(s); setMessage(s ? "Connected to this PC" : "PC cache unavailable · maps use the provider directly"); }
    catch (error) { setMessage(error instanceof Error ? error.message : "Cache unavailable"); }
    finally { setBusy(false); }
  };
  return <section className="basemap-pc-cache" aria-label="Basemaps on this PC">
    <h3>Basemaps on this PC</h3>
    <p>Save viewed Kansas aerial, standard vector and USGS topo tiles for faster repeat visits, including the cutaway. Original tile detail is preserved.</p>
    <label><input type="checkbox" checked={enabled} onChange={event => { setEnabled(event.target.checked); setBasemapCacheEnabled(event.target.checked); }} /> Use and save local basemap tiles</label>
    <p role="status">{message}</p>
    {status && <><p><strong>{(status.usedBytes / 1e9).toFixed(3)} / 10 GB</strong> · {status.tiles.toLocaleString()} tiles · {status.hits.toLocaleString()} disk hits this session. Older cache tiles are removed automatically.</p><p>Folder: <code>{status.destination}</code></p><p>Kansas overview: {status.job.state} {status.job.total > 0 ? `· ${status.job.completed} / ${status.job.total} tiles${status.job.failed ? ` · ${status.job.failed} unavailable` : ""}` : ""}</p></>}
    <div className="panel-footer-actions"><button type="button" disabled={busy} onClick={() => void action("connect")}>Reconnect</button><button type="button" disabled={!status || busy || status.job.state === "running"} onClick={() => void action("overview")}>Save Kansas overview</button>{status?.job.state === "running" && <button type="button" disabled={busy} onClick={() => void action("cancel")}>Stop download</button>}</div>
    <small>The overview saves Kansas aerial and USGS topo zooms 4–9, up to 512 MiB per run. Fine aerial detail saves as you zoom; whole-state high-resolution packages are excluded. Esri and OpenStreetMap raster stay online. This is a partial display cache, not an offline copy of the app.</small>
    <p><strong>Display context, not KFM evidence.</strong> Cached imagery keeps its original source date. Kansas aerial remains 2024; exact local flight date is unresolved. Download time is not observation time. Expired tiles refresh from their provider; failed refreshes remain unavailable.</p>
    <details><summary>Set up another PC</summary><p>Run the basemap cache service from <code>scripts/basemap-cache.py</code> against an initialized <code>KFM_DATA_ROOT</code>. The <code>docs/BASEMAP_CACHE.md</code> runbook includes startup and removal. Your browser may ask to allow access to this PC.</p></details>
  </section>;
}
