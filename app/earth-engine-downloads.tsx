"use client";
import Link from "next/link";
import { earthEngineUrl, type EarthEngineDataset } from "./earth-engine-data";
import type { LocalDownloads } from "./use-local-downloads";
import styles from "./earth-engine/workspace.module.css";

type Props = { dataset: EarthEngineDataset; year: number | undefined; invalid: boolean;
  downloads?: LocalDownloads; blockedByOtherDownload?: boolean; onViewActivity?: () => void; compact?: boolean };

/** Hosted discovery does not connect to a visitor's operator or start an unconfigured capture. */
export default function EarthEngineDownloads({ dataset, year, invalid }: Props) {
  return <section className={styles.downloadPanel} aria-label="Source files and reviewed captures">
    <h3>Source files &amp; reviewed captures</h3>
    <p>{dataset.provider} · {year ?? "source mosaic"} · {dataset.resolution}</p>
    <p>{dataset.limitation}</p>
    <p role="status">{invalid ? "Choose a valid source period above." : "Hosted capture is not configured for this source. Reviewed map layers remain separate from original provider files."}</p>
    <a href={earthEngineUrl(dataset)} target="_blank" rel="noreferrer">Open provider catalog ↗</a>
    <p><Link href="/?layers=sources">View source status in Layers →</Link></p>
  </section>;
}
