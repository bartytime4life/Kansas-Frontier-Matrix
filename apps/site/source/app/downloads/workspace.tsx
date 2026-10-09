"use client";
import Link from "next/link";
import { useEffect, useMemo, useState } from "react";
import { useLocalDownloads } from "../use-local-downloads";
import { usePublicMapDownloads } from "../use-public-map-downloads";
import { useEarthEngineContext } from "../earth-engine-context-client";
import { normalizeDownloadActivity } from "../download-activity";
import { ActivityWorkspace, TransferPanel } from "../download-activity-panel";
import PublicMapBrowser from "../public-map-browser";
import EarthEnginePicker from "../earth-engine-picker";
import DownloadLibrary from "../download-library";
import styles from "./workspace.module.css";

type View = "find" | "library" | "activity";
export default function DownloadsWorkspace() {
  const local = useLocalDownloads(), reviewed = useEarthEngineContext();
  const maps = usePublicMapDownloads({ onTransferTerminal: local.refreshLibrary, blockedByOtherDownload: Boolean(local.status?.active) || local.starting });
  const [view, setView] = useState<View>("find"), [source, setSource] = useState<"maps" | "satellite">("maps");
  const items = useMemo(() => normalizeDownloadActivity(local.status, maps.status), [local.status, maps.status]);
  const active = items.filter(item => item.active), allConnected = local.connection === "connected" && maps.connection === "connected";
  const someConnected = local.connection === "connected" || maps.connection === "connected", connecting = local.connection === "connecting" || maps.connection === "connecting";
  const checked = local.lastChecked && maps.lastChecked ? new Date(Math.min(Date.parse(local.lastChecked), Date.parse(maps.lastChecked))).toLocaleTimeString(undefined, { hour: "numeric", minute: "2-digit" }) : null;
  const connect = () => { local.connect(); maps.connect(); };
  const openActivity = () => setView("activity");
  useEffect(() => {
    const deepLink = () => { if (window.location.hash === "#public-maps") { setView("find"); setSource("maps"); } };
    window.addEventListener("hashchange", deepLink); return () => window.removeEventListener("hashchange", deepLink);
  }, []);
  return <main className={styles.page} data-download-scroll data-transfer-active={active.length > 0 || local.starting || maps.busy === "download" || local.library?.state === "scanning" || maps.status?.refresh.state === "running"}>
    <div className={styles.wrap}>
      <header className={styles.header}><Link href="/" className={styles.brand}>KFM <span>EXPLORER</span></Link><nav aria-label="Data navigation"><Link href="/">← Explorer map</Link><Link href="/earth-engine">Advanced recipes</Link><Link href="/acquisition">Receipts</Link></nav></header>
      <section className={styles.intro}><div><p className={styles.eyebrow}>YOUR KANSAS DATA WORKBENCH</p><h1>Data &amp; downloads</h1><p>Source maps, satellite imagery, and your local library — in one place.</p></div><span className={styles.localBadge}>LOCAL WORKSPACE</span></section>
      <div className={styles.connection} aria-label="Local service connection"><div><span className={styles.connectionDot} data-connected={allConnected} aria-hidden="true" /><strong>{allConnected ? "Connected to this computer" : connecting ? "Connecting to this computer…" : someConnected ? "Partly connected" : "Browse now. Connect to download."}</strong>{checked && allConnected && <span>Checked {checked}</span>}</div>
        {!allConnected && <button type="button" disabled={connecting} aria-busy={connecting} onClick={connect}>{connecting ? "Connecting…" : someConnected ? "Reconnect channels" : "Connect this computer"}</button>}
        <details className={styles.connectionDetails}><summary>Connection details</summary><p>Library &amp; Earth Engine: <strong>{local.connection}</strong><br />Public maps: <strong>{maps.connection}</strong></p><p>Catalog browsing works offline. Progress refreshes automatically while this page is visible; transfers continue in the local operator.</p><div className={styles.linkActions}><button type="button" disabled={connecting} onClick={connect}>Recheck connection</button><Link href="/earth-engine-downloads/setup">Setup help →</Link></div></details>
      </div>
      <p className={styles.srOnly} role="status" aria-live="polite" aria-atomic="true">{local.announcement} {maps.announcement}</p>
      <nav className={styles.workspaceNav} aria-label="Download workspace"><button type="button" aria-controls="download-find" aria-current={view === "find" ? "page" : undefined} onClick={() => setView("find")}>Find data</button><button type="button" aria-controls="download-library" aria-current={view === "library" ? "page" : undefined} onClick={() => setView("library")}>My library</button><button type="button" aria-controls="download-activity" aria-current={view === "activity" ? "page" : undefined} onClick={openActivity}>Activity{active.length > 0 && <span>{active.length}</span>}</button></nav>
      <div className={styles.workbench}>
        <div className={styles.mainColumn}>
          <div id="download-find" hidden={view !== "find"}>
            <nav className={styles.sourceNav} aria-label="Source categories"><button type="button" aria-pressed={source === "maps"} onClick={() => setSource("maps")}><span>01</span><strong>Maps &amp; geology</strong><small>Free direct files</small></button><button type="button" aria-pressed={source === "satellite"} onClick={() => setSource("satellite")}><span>02</span><strong>Satellite &amp; climate</strong><small>Earth Engine sources</small></button></nav>
            <div hidden={source !== "maps"}><PublicMapBrowser downloads={maps} blockedByOtherDownload={Boolean(local.status?.active) || local.starting} onViewActivity={openActivity} /></div>
            <div hidden={source !== "satellite"}><EarthEnginePicker downloads={local} blockedByOtherDownload={Boolean(maps.status?.active) || maps.busy === "download"} onViewActivity={openActivity} /></div>
          </div>
          <div id="download-library" hidden={view !== "library"}><DownloadLibrary downloads={local} reviewed={reviewed} /></div>
          <div id="download-activity" hidden={view !== "activity"}><ActivityWorkspace items={items} local={local} maps={maps} /></div>
        </div>
        <TransferPanel items={items} local={local} maps={maps} onViewActivity={openActivity} />
      </div>
      <footer className={styles.footer}><span>Private storage · explicit download limits · source attribution retained</span><Link href="/acquisition">Review receipts →</Link></footer>
    </div>
  </main>;
}
