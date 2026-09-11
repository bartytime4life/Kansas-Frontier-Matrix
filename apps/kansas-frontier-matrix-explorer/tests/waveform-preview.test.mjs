import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const ts = await import("typescript");
const source = await readFile(new URL("../app/waveform-preview.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  fileName: "waveform-preview.ts",
}).outputText;
const waveform = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
if (!globalThis.crypto) globalThis.crypto = (await import("node:crypto")).webcrypto;

const stationXml = (withResponse = true) => `<?xml version="1.0"?>
<FDSNStationXML xmlns="http://www.fdsn.org/xml/station/1" schemaVersion="1.2">
  <Network code="AM"><Station code="TEST">
    <Channel code="EHZ" locationCode="00" startDate="2026-09-01T00:00:00Z">
      ${withResponse ? "<Response><InstrumentSensitivity><Value>1</Value><InputUnits><Name>Counts</Name></InputUnits></InstrumentSensitivity></Response>" : ""}
    </Channel>
  </Station></Network>
</FDSNStationXML>`;

const putAscii = (view, offset, value, length) => {
  for (let index = 0; index < length; index += 1) view.setUint8(offset + index, value.charCodeAt(index) || 32);
};

const miniSeedRecord = (samples = [1, -2, 3, -4], station = "TEST", second = 0) => {
  const bytes = new ArrayBuffer(512);
  const view = new DataView(bytes);
  putAscii(view, 0, "000001", 6);
  view.setUint8(6, "D".charCodeAt(0));
  putAscii(view, 8, station, 5);
  putAscii(view, 13, "00", 2);
  putAscii(view, 15, "EHZ", 3);
  putAscii(view, 18, "AM", 2);
  view.setUint16(20, 2026, false);
  view.setUint16(22, 254, false);
  view.setUint8(24, 0); view.setUint8(25, 0); view.setUint8(26, second);
  view.setUint16(28, 0, false);
  view.setInt16(30, samples.length, false);
  view.setInt16(32, 1, false); view.setInt16(34, 1, false);
  view.setUint8(39, 1);
  view.setUint16(44, 56, false); view.setUint16(46, 48, false);
  view.setUint16(48, 1000, false); view.setUint16(50, 0, false);
  view.setUint8(52, 3); view.setUint8(53, 1); view.setUint8(54, 9); view.setUint8(55, 0);
  samples.forEach((sample, index) => view.setInt32(56 + index * 4, sample, false));
  return bytes;
};

test("accepts one bounded local raw-count channel and keeps the outcome held", async () => {
  const preview = await waveform.buildLocalWaveformPreview({
    waveformFileName: "AM.TEST.00.EHZ.mseed", stationXmlFileName: "AM.TEST.stationxml",
    waveformBytes: miniSeedRecord([1, -2, 3, -4, 5]), stationXmlText: stationXml(),
    inspectedAt: "2026-09-11T00:00:00.000Z", attribution: "Data provided by Raspberry Shake.",
  });
  assert.equal(preview.authority, "UNADMITTED_BROWSER_PREVIEW");
  assert.equal(preview.publicEffect, "NONE");
  assert.equal(preview.outcome, "HOLD");
  assert.equal(preview.plotAllowed, true);
  assert.equal(preview.nslc, "AM.TEST.00.EHZ");
  assert.equal(preview.sampleCount, 5);
  assert.equal(preview.stationXml.responsePresent, true);
  assert.equal(preview.gates.find((gate) => gate.id === "redistribution").state, "DENY");
  assert.equal(preview.gates.find((gate) => gate.id === "correction-rollback").state, "HOLD");
  assert.match(preview.sha256, /^[0-9a-f]{64}$/);
  assert.ok(preview.points.length > 0);
  const audit = waveform.waveformPreviewAudit(preview);
  assert.equal(audit.samples.points, "OMITTED_FROM_AUDIT");
  assert.equal(audit.effects, "NO_UPLOAD_NO_CACHE_NO_PROXY_NO_SOURCE_ADMISSION_NO_REDISTRIBUTION_NO_CORRECTION");
});

test("blocks missing attribution and response metadata", async () => {
  const noAttribution = await waveform.buildLocalWaveformPreview({
    waveformFileName: "waveform.mseed", stationXmlFileName: "station.xml", waveformBytes: miniSeedRecord(),
    stationXmlText: stationXml(), inspectedAt: "2026-09-11T00:00:00.000Z", attribution: null,
  });
  assert.equal(noAttribution.outcome, "BLOCK");
  assert.equal(noAttribution.plotAllowed, false);
  assert.equal(noAttribution.gates.find((gate) => gate.id === "attribution").state, "BLOCK");

  const noResponse = await waveform.buildLocalWaveformPreview({
    waveformFileName: "waveform.mseed", stationXmlFileName: "station.xml", waveformBytes: miniSeedRecord(),
    stationXmlText: stationXml(false), inspectedAt: "2026-09-11T00:00:00.000Z", attribution: "User-supplied file",
  });
  assert.equal(noResponse.outcome, "BLOCK");
  assert.equal(noResponse.gates.find((gate) => gate.id === "response-metadata").state, "BLOCK");
});

test("rejects compressed encodings and mixed NSLC channels instead of guessing", async () => {
  const compressed = new DataView(miniSeedRecord());
  compressed.setUint8(52, 11);
  await assert.rejects(() => waveform.buildLocalWaveformPreview({
    waveformFileName: "compressed.mseed", stationXmlFileName: "station.xml", waveformBytes: compressed.buffer,
    stationXmlText: stationXml(), inspectedAt: "2026-09-11T00:00:00.000Z", attribution: "User-supplied file",
  }), /intentionally not decoded/);

  const first = new Uint8Array(miniSeedRecord());
  const second = new Uint8Array(miniSeedRecord([1, 2], "OTHER"));
  const combined = new Uint8Array(first.byteLength + second.byteLength);
  combined.set(first); combined.set(second, first.byteLength);
  await assert.rejects(() => waveform.buildLocalWaveformPreview({
    waveformFileName: "mixed.mseed", stationXmlFileName: "station.xml", waveformBytes: combined.buffer,
    stationXmlText: stationXml(), inspectedAt: "2026-09-11T00:00:00.000Z", attribution: "User-supplied file",
  }), /one NSLC channel/);

  const firstContiguous = new Uint8Array(miniSeedRecord([1, 2]));
  const gap = new Uint8Array(miniSeedRecord([3, 4], "TEST", 10));
  const gapped = new Uint8Array(firstContiguous.byteLength + gap.byteLength);
  gapped.set(firstContiguous); gapped.set(gap, firstContiguous.byteLength);
  const gappedPreview = await waveform.buildLocalWaveformPreview({
    waveformFileName: "gapped.mseed", stationXmlFileName: "station.xml", waveformBytes: gapped.buffer,
    stationXmlText: stationXml(), inspectedAt: "2026-09-11T00:00:00.000Z", attribution: "User-supplied file",
  });
  assert.equal(gappedPreview.outcome, "BLOCK");
  assert.equal(gappedPreview.gates.find((gate) => gate.id === "continuity").state, "BLOCK");
});

test("keeps the implementation browser-local and finite", async () => {
  assert.equal(waveform.WAVEFORM_PREVIEW_MAX_BYTES, 2 * 1024 * 1024);
  assert.equal(waveform.WAVEFORM_PREVIEW_MAX_SECONDS, 600);
  assert.equal(waveform.WAVEFORM_PREVIEW_MAX_SAMPLES, 100000);
  assert.deepEqual(waveform.waveformPreviewConstants.supportedEncodings, [1, 3, 4, 5]);
  assert.doesNotMatch(source, /\bfetch\s*\(/);
  assert.doesNotMatch(source, /\/api\//);
  assert.doesNotMatch(source, /localStorage|sessionStorage|indexedDB/i);
});