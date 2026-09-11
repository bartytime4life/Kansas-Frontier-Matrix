"use client";

import { useRef, useState } from "react";
import {
  buildLocalWaveformPreview,
  WAVEFORM_PREVIEW_MAX_BYTES,
  waveformPreviewAudit,
  type WaveformGateState,
  type WaveformPreview,
} from "./waveform-preview";

const stationXmlLimitBytes = 256 * 1024;

const gateTone = (state: WaveformGateState) => {
  if (state === "PASS") return "pass";
  if (state === "WARN") return "warn";
  if (state === "HOLD") return "hold";
  return "block";
};


const chartLines = (preview: WaveformPreview) => {
  if (!preview.points.length) return { low: "", high: "" };
  const values = preview.points.flatMap((point) => [point[1], point[2]]);
  const minimum = Math.min(...values);
  const maximum = Math.max(...values);
  const span = maximum - minimum || 1;
  const end = preview.durationSeconds || (preview.sampleCount / preview.sampleRate) || 1;
  const coordinate = (offset: number, value: number) => {
    const x = 12 + (offset / end) * 616;
    const y = 12 + ((maximum - value) / span) * 116;
    return x.toFixed(2) + "," + y.toFixed(2);
  };
  const low = preview.points.map((point) => coordinate(point[0], point[1])).join(" ");
  const high = preview.points.map((point) => coordinate(point[0], point[2])).join(" ");
  return { low, high };
};

export default function WaveformPreviewPanel() {
  const inputRef = useRef<HTMLInputElement>(null);
  const generationRef = useRef(0);
  const [attribution, setAttribution] = useState("");
  const [preview, setPreview] = useState<WaveformPreview | null>(null);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  const [notice, setNotice] = useState("");

  const inspectFiles = async (fileList?: FileList | null) => {
    const generation = ++generationRef.current;
    const files = Array.from(fileList ?? []);
    if (!files.length) return;
    setBusy(true);
    setError("");
    setNotice("");
    setPreview(null);
    try {
      const waveformFile = files.find((file) => /\.(?:mseed|miniseed)$/i.test(file.name) || file.type === "application/vnd.fdsn.mseed");
      const stationXmlFile = files.find((file) => /\.(?:stationxml|xml)$/i.test(file.name) || file.type.includes("xml"));
      if (!waveformFile || !stationXmlFile) throw new Error("Choose one MiniSEED file and one matching StationXML file.");
      if (waveformFile.size > WAVEFORM_PREVIEW_MAX_BYTES) throw new Error("The waveform preview is limited to files no larger than 2 MB.");
      if (stationXmlFile.size > stationXmlLimitBytes) throw new Error("The StationXML preview is limited to 256 KB.");
      const next = await buildLocalWaveformPreview({
        waveformFileName: waveformFile.name,
        stationXmlFileName: stationXmlFile.name,
        waveformBytes: await waveformFile.arrayBuffer(),
        stationXmlText: await stationXmlFile.text(),
        inspectedAt: new Date().toISOString(),
        attribution: attribution.trim() || null,
      });
      if (generation !== generationRef.current) return;
      setPreview(next);
      setNotice(next.outcome === "HOLD"
        ? "Local waveform inspected; source admission and publication remain held."
        : "Waveform inspection is blocked; no samples were drawn.");
    } catch (caught) {
      if (generation !== generationRef.current) return;
      setError(caught instanceof Error ? caught.message : "The waveform files could not be inspected.");
      setNotice("");
    } finally {
      if (generation === generationRef.current) {
        setBusy(false);
        if (inputRef.current) inputRef.current.value = "";
      }
    }
  };

  const clear = () => {
    generationRef.current += 1;
    setPreview(null);
    setError("");
    setNotice("");
    setBusy(false);
    if (inputRef.current) inputRef.current.value = "";
  };

  const copyAudit = async () => {
    if (!preview) return;
    try {
      await navigator.clipboard.writeText(JSON.stringify(waveformPreviewAudit(preview), null, 2));
      setNotice("Copied the redacted waveform inspection record; samples stayed in browser memory.");
    } catch {
      setNotice("Clipboard access was blocked; no waveform inspection record left the browser.");
    }
  };

  const lines = preview ? chartLines(preview) : { low: "", high: "" };

  return <section className="waveform-preview-panel" aria-labelledby="waveform-preview-title">
    <div className="waveform-preview-heading">
      <span>WAVEFORM PREVIEW · HOLD</span>
      <h4 id="waveform-preview-title">Inspect a local MiniSEED + StationXML pair</h4>
      <p>Raw values only, one NSLC channel, and no provider retrieval. This is a browser-local review surface, not a live Raspberry Shake connection.</p>
    </div>
    <div className="waveform-gate-grid" aria-label="Waveform preview boundary">
      <article><span>01</span><strong>Local bytes</strong><small>One MiniSEED file; 2 MB maximum.</small></article>
      <article><span>02</span><strong>Response proof</strong><small>Matching StationXML response metadata is required.</small></article>
      <article><span>03</span><strong>Fail closed</strong><small>No cache, proxy, download, source activation, or release.</small></article>
    </div>
    <label className="waveform-attribution-field">
      <span>Visible attribution (required to draw)</span>
      <input value={attribution} onChange={(event) => setAttribution(event.target.value)} placeholder="Enter the source-provided attribution text" />
      <small>Do not infer or copy provider rights from this field; it is only a local display acknowledgement.</small>
    </label>
    <label className="waveform-dropzone" data-busy={busy} onDragOver={(event) => { event.preventDefault(); event.dataTransfer.dropEffect = "copy"; }} onDrop={(event) => { event.preventDefault(); void inspectFiles(event.dataTransfer.files); }}>
      <input ref={inputRef} type="file" multiple accept=".mseed,.miniseed,.stationxml,.xml,application/vnd.fdsn.mseed,application/vnd.fdsn.stationxml+xml" onChange={(event) => void inspectFiles(event.target.files)} />
      <span aria-hidden="true">∿</span>
      <strong>{busy ? "Inspecting local waveform…" : "Choose or drop MiniSEED + StationXML"}</strong>
      <small>Files stay in browser memory · no URL input · no upload</small>
    </label>
    {error && <div className="waveform-error" role="alert"><strong>Waveform preview blocked</strong><p>{error}</p></div>}
    {notice && <div className="waveform-notice" role="status"><strong>{notice}</strong></div>}
    {!preview && !error && <div className="map-utility-empty waveform-empty"><strong>No waveform pair inspected</strong><p>The local preview does not add a source, observation, catalog record, report value, or public artifact.</p></div>}
    {preview && <div className="waveform-preview-result">
      <div className="waveform-summary-grid" aria-label="Waveform preview summary">
        <article><span>OUTCOME</span><strong data-state={gateTone(preview.outcome)}>{preview.outcome}</strong><small>Unadmitted browser preview</small></article>
        <article><span>CHANNEL</span><strong>{preview.nslc}</strong><small>{preview.encodingLabel}</small></article>
        <article><span>SAMPLES</span><strong>{preview.sampleCount.toLocaleString("en-US")}</strong><small>{preview.sampleRate} Hz · {preview.durationSeconds.toFixed(3)} s</small></article>
        <article><span>PROVENANCE</span><strong>{preview.sha256.slice(0, 12)}…</strong><small>SHA-256 exact bytes</small></article>
      </div>
      {preview.plotAllowed && <figure className="waveform-plot">
        <figcaption>Raw values/counts · response correction not applied</figcaption>
        <svg viewBox="0 0 640 140" role="img" aria-label="Bounded raw waveform preview">
          <polyline points={lines.high} fill="none" stroke="var(--import-accent)" strokeWidth="1.5" vectorEffect="non-scaling-stroke" />
          <polyline points={lines.low} fill="none" stroke="rgba(229,139,240,.46)" strokeWidth="1" vectorEffect="non-scaling-stroke" />
        </svg>
      </figure>}
      {!preview.plotAllowed && <div className="waveform-no-plot"><strong>No samples drawn</strong><p>Resolve every blocking gate before any local raw-value preview; no fallback chart is permitted.</p></div>}
      <dl className="waveform-file-metadata">
        <div><dt>Time window</dt><dd>{preview.startTime} → {preview.endTime}</dd></div>
        <div><dt>StationXML</dt><dd>{preview.stationXmlFileName} · response {preview.stationXml.responsePresent ? "present" : "missing"}</dd></div>
        <div><dt>Sensitivity</dt><dd>{preview.stationXml.instrumentSensitivity ?? "NOT SUPPLIED"} {preview.stationXml.inputUnit ?? ""}</dd></div>
        <div><dt>Attribution</dt><dd>{preview.attribution ?? "NOT SUPPLIED"}</dd></div>
      </dl>
      <div className="waveform-check-list" aria-label="Waveform preview gate trace">
        {preview.gates.map((gate) => <article key={gate.id} data-state={gateTone(gate.state)}><header><span>{gate.label}</span><strong>{gate.state}</strong></header><p>{gate.detail}</p></article>)}
      </div>
      <div className="map-utility-actions waveform-actions"><button type="button" onClick={() => void copyAudit()}>Copy inspection</button><button type="button" onClick={clear}>Clear</button></div>
      <aside className="map-utility-boundary" data-tone="warning"><strong>HOLD means no source activation.</strong><p>Exact bytes and sample arrays remain transient. The audit includes a digest and bounded metadata only; it is not evidence of provider permission, freshness, correction state, release, or deployment.</p></aside>
    </div>}
  </section>;
}
