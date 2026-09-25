"use client";

import { useState } from "react";
import {
  EARTH_ENGINE_CONTEXT_PREFIX,
  parseEarthEngineManifest,
  parseEarthEnginePointer,
  type EarthEngineContextManifest,
  type EarthEngineContextPointer,
} from "../../earth-engine-context";

type Prepared = { files: { key: string; file: File }[]; pointer: EarthEngineContextPointer; manifest: EarthEngineContextManifest };

function hex(bytes: ArrayBuffer) {
  return Array.from(new Uint8Array(bytes), (part) => part.toString(16).padStart(2, "0")).join("");
}

async function digest(bytes: ArrayBuffer) { return hex(await crypto.subtle.digest("SHA-256", bytes)); }

async function inspect(files: FileList): Promise<Prepared> {
  const all = Array.from(files);
  const pointerFile = all.find((file) => file.webkitRelativePath.endsWith(`/${EARTH_ENGINE_CONTEXT_PREFIX}/active.json`));
  if (!pointerFile) throw new Error("Choose the complete prepared display-set folder, including active.json.");
  const pointer = parseEarthEnginePointer(JSON.parse(await pointerFile.text()));
  if (!pointer) throw new Error("The display-set pointer failed validation.");
  const prefix = `${EARTH_ENGINE_CONTEXT_PREFIX}/sets/${pointer.setId}/`;
  const entries = all.map((file) => ({ file, path: file.webkitRelativePath }));
  const manifestFile = entries.find((entry) => entry.path.endsWith(`${prefix}manifest.json`))?.file;
  if (!manifestFile) throw new Error("The selected folder has no matching manifest.");
  const manifestBytes = await manifestFile.arrayBuffer();
  if (await digest(manifestBytes) !== pointer.manifestSha256) throw new Error("The manifest hash does not match active.json.");
  const manifest = parseEarthEngineManifest(JSON.parse(new TextDecoder().decode(manifestBytes)));
  if (!manifest || manifest.setId !== pointer.setId) throw new Error("The display-set manifest failed validation.");
  const upload = entries.filter(({ path }) => path.includes(prefix)).map(({ file, path }) => ({ key: path.slice(path.indexOf(prefix)), file }));
  if (!upload.length || new Set(upload.map((entry) => entry.key)).size !== upload.length) throw new Error("The selected folder has missing or duplicate display files.");
  return { files: upload, pointer, manifest };
}

export function EarthEngineInstaller() {
  const [prepared, setPrepared] = useState<Prepared | null>(null);
  const [progress, setProgress] = useState(0);
  const [message, setMessage] = useState("Select the prepared folder from KFM's private data store.");
  const [working, setWorking] = useState(false);
  const [uploaded, setUploaded] = useState(false);

  async function select(files: FileList | null) {
    setPrepared(null); setUploaded(false); setProgress(0);
    if (!files) return;
    try {
      const candidate = await inspect(files);
      setPrepared(candidate);
      setMessage(`${candidate.manifest.layers.filter((layer) => layer.status === "approved").length} reviewed layers · ${candidate.files.length} immutable files. Check the set before uploading.`);
    } catch (error) { setMessage(error instanceof Error ? error.message : "The display folder failed validation."); }
  }

  async function upload() {
    if (!prepared || working) return;
    setWorking(true); setMessage("Uploading reviewed files to the private display prefix…");
    let next = 0, completed = 0;
    try {
      let firstError: Error | null = null;
      const workers = Array.from({ length: Math.min(4, prepared.files.length) }, async () => {
        while (next < prepared.files.length && !firstError) {
          const entry = prepared.files[next++];
          try {
            const bytes = await entry.file.arrayBuffer();
            const sha256 = await digest(bytes);
            const contentType = entry.key.endsWith(".png") ? "image/png" : "application/json";
            const response = await fetch(`/api/earth-engine-context/stage?key=${encodeURIComponent(entry.key)}`, {
              method: "PUT", headers: { "content-type": contentType, "x-kfm-ee-sha256": sha256 }, body: bytes,
            });
            if (!response.ok) throw new Error(`${entry.key}: ${response.status} ${(await response.json().catch(() => ({}))).error ?? "upload failed"}`);
            completed++; setProgress(completed);
          } catch (error) { firstError ??= error instanceof Error ? error : new Error("Upload failed."); }
        }
      });
      await Promise.all(workers);
      if (firstError) throw firstError;
      setUploaded(true); setMessage("All files were read back from private storage. Activate after checking the manifest below.");
    } catch (error) { setMessage(error instanceof Error ? error.message : "Upload failed. No display set was activated."); }
    finally { setWorking(false); }
  }

  async function activate() {
    if (!prepared || !uploaded || working) return;
    setWorking(true); setMessage("Checking the complete tile inventory before activation…");
    try {
      const response = await fetch("/api/earth-engine-context/activate", {
        method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(prepared.pointer),
      });
      const result = await response.json();
      if (!response.ok) throw new Error(result.error ?? "Activation failed.");
      setMessage(`Active owner-only display set: ${result.setId} · ${result.tileCount} checked tiles. Reload the map to see it.`);
    } catch (error) { setMessage(error instanceof Error ? error.message : "Activation failed; the previous set remains selected."); }
    finally { setWorking(false); }
  }

  return <main style={{ maxWidth: 760, margin: "3rem auto", padding: "0 1rem", lineHeight: 1.5 }}>
    <h1>Install reviewed Earth Engine context</h1>
    <p>Owner access only. These processed snapshots are visual context, not KFM claim evidence. Live Earth Engine remains disconnected.</p>
    <label htmlFor="ee-display-folder">Prepared display-set folder</label><br />
    <input id="ee-display-folder" type="file" multiple disabled={working} onChange={(event) => void select(event.target.files)} {...({ webkitdirectory: "" } as Record<string, string>)} />
    <p role="status" aria-live="polite">{message}</p>
    {prepared && <>
      <p><b>Set:</b> {prepared.pointer.setId} · <b>Files:</b> {progress}/{prepared.files.length}</p>
      <ul>{prepared.manifest.layers.map((layer) => <li key={layer.id}><b>{layer.id}</b> · {layer.period} · {layer.resolutionMeters} m · {layer.attribution} · {layer.limits}</li>)}</ul>
      <button type="button" disabled={working} onClick={() => void upload()}>Upload and verify files</button>{" "}
      <button type="button" disabled={!uploaded || working} onClick={() => void activate()}>Activate reviewed set</button>
    </>}
  </main>;
}
