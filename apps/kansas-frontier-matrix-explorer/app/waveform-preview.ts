export const WAVEFORM_PREVIEW_MAX_BYTES = 2 * 1024 * 1024;
export const WAVEFORM_PREVIEW_MAX_SECONDS = 10 * 60;
export const WAVEFORM_PREVIEW_MAX_SAMPLES = 100_000;
export const WAVEFORM_PREVIEW_MAX_POINTS = 1_200;
export const WAVEFORM_PREVIEW_NETWORK = "AM";
const RECORD_CONTINUITY_TOLERANCE_MS = 2;

export type WaveformGateState = "PASS" | "WARN" | "HOLD" | "DENY" | "BLOCK";

export type WaveformGate = Readonly<{
  id: string;
  label: string;
  state: WaveformGateState;
  detail: string;
}>;

export type WaveformPoint = readonly [offsetSeconds: number, low: number, high: number];

export type MiniSeedRecordSummary = Readonly<{
  nslc: string;
  network: string;
  station: string;
  location: string;
  channel: string;
  startTime: string;
  endTime: string;
  startEpochMs: number;
  endEpochMs: number;
  sampleCount: number;
  sampleRate: number;
  encoding: number;
  encodingLabel: string;
}>;

export type StationXmlSummary = Readonly<{
  network: string;
  station: string;
  location: string;
  channel: string;
  responsePresent: boolean;
  instrumentSensitivity: number | null;
  inputUnit: string | null;
  startDate: string | null;
  endDate: string | null;
  externalReferenceCount: number;
}>;

export type WaveformPreview = Readonly<{
  format: "kfm-browser-waveform-preview-v1";
  authority: "UNADMITTED_BROWSER_PREVIEW";
  publicEffect: "NONE";
  sourceActivation: "NOT_REQUESTED";
  waveformFileName: string;
  stationXmlFileName: string;
  inspectedAt: string;
  byteLength: number;
  sha256: string;
  nslc: string;
  network: string;
  station: string;
  location: string;
  channel: string;
  startTime: string;
  endTime: string;
  durationSeconds: number;
  sampleRate: number;
  sampleCount: number;
  recordCount: number;
  encoding: number;
  encodingLabel: string;
  stationXml: StationXmlSummary;
  points: readonly WaveformPoint[];
  attribution: string | null;
  gates: readonly WaveformGate[];
  outcome: "HOLD" | "BLOCK";
  plotAllowed: boolean;
}>;

type ParsedRecord = MiniSeedRecordSummary & Readonly<{ samples: readonly number[] }>;

const text = (value: DataView, offset: number, length: number) => {
  let output = "";
  for (let index = 0; index < length; index += 1) {
    const code = value.getUint8(offset + index);
    output += code === 0 ? " " : String.fromCharCode(code);
  }
  return output.trim();
};


const readUint16 = (view: DataView, offset: number, littleEndian: boolean) => {
  if (offset < 0 || offset + 2 > view.byteLength) throw new Error("MiniSEED header is truncated.");
  return view.getUint16(offset, littleEndian);
};

const readInt16 = (view: DataView, offset: number, littleEndian: boolean) => {
  if (offset < 0 || offset + 2 > view.byteLength) throw new Error("MiniSEED header is truncated.");
  return view.getInt16(offset, littleEndian);
};

const readInt32 = (view: DataView, offset: number, littleEndian: boolean) => {
  if (offset < 0 || offset + 4 > view.byteLength) throw new Error("MiniSEED sample data is truncated.");
  return view.getInt32(offset, littleEndian);
};

const readFloat32 = (view: DataView, offset: number, littleEndian: boolean) => {
  if (offset < 0 || offset + 4 > view.byteLength) throw new Error("MiniSEED sample data is truncated.");
  return view.getFloat32(offset, littleEndian);
};

const readFloat64 = (view: DataView, offset: number, littleEndian: boolean) => {
  if (offset < 0 || offset + 8 > view.byteLength) throw new Error("MiniSEED sample data is truncated.");
  return view.getFloat64(offset, littleEndian);
};

const chooseHeaderEndian = (view: DataView) => {
  const bigYear = view.getUint16(20, false);
  const bigDay = view.getUint16(22, false);
  if (bigYear >= 1900 && bigYear <= 2200 && bigDay >= 1 && bigDay <= 366) return false;
  const littleYear = view.getUint16(20, true);
  const littleDay = view.getUint16(22, true);
  if (littleYear >= 1900 && littleYear <= 2200 && littleDay >= 1 && littleDay <= 366) return true;
  throw new Error("MiniSEED start time is not a valid FDSN BTime header.");
};

const sampleRateFrom = (factor: number, multiplier: number) => {
  if (!factor || !multiplier) return 0;
  return Math.pow(Math.abs(factor), factor / Math.abs(factor))
    * Math.pow(Math.abs(multiplier), multiplier / Math.abs(multiplier));
};

const isoFromBTime = (year: number, day: number, hour: number, minute: number, second: number, fraction: number) => {
  // MiniSEED BTime stores fractional seconds in 10,000ths (0.1 ms), not tenths.
  const epoch = Date.UTC(year, 0, 1, hour, minute, second, 0) + (day - 1) * 86_400_000 + fraction / 10;
  const date = new Date(epoch);
  if (!Number.isFinite(date.getTime())) throw new Error("MiniSEED start time is not representable.");
  return { epochMs: epoch, iso: date.toISOString() };
};

const encodingName = (encoding: number) => {
  const names: Record<number, string> = {
    0: "ASCII",
    1: "16-bit integer",
    2: "24-bit integer",
    3: "32-bit integer",
    4: "32-bit float",
    5: "64-bit float",
    10: "Steim-1",
    11: "Steim-2",
  };
  return names[encoding] ?? "encoding " + encoding;
};

const decodeSamples = (
  view: DataView,
  offset: number,
  availableBytes: number,
  sampleCount: number,
  encoding: number,
  littleEndian: boolean,
) => {
  const bytesPerSample: Record<number, number> = { 1: 2, 3: 4, 4: 4, 5: 8 };
  const width = bytesPerSample[encoding];
  if (!width) {
    throw new Error("MiniSEED " + encodingName(encoding) + " is intentionally not decoded in this preview; compressed or uncommon encodings stay held.");
  }
  if (sampleCount < 0 || sampleCount > WAVEFORM_PREVIEW_MAX_SAMPLES) throw new Error("MiniSEED sample count exceeds the 100,000-sample preview cap.");
  if (sampleCount * width > availableBytes) throw new Error("MiniSEED sample payload is truncated.");
  const samples: number[] = [];
  for (let index = 0; index < sampleCount; index += 1) {
    const sampleOffset = offset + index * width;
    if (encoding === 1) samples.push(readInt16(view, sampleOffset, littleEndian));
    else if (encoding === 3) samples.push(readInt32(view, sampleOffset, littleEndian));
    else if (encoding === 4) samples.push(readFloat32(view, sampleOffset, littleEndian));
    else samples.push(readFloat64(view, sampleOffset, littleEndian));
  }
  if (samples.some((sample) => !Number.isFinite(sample))) throw new Error("MiniSEED contains a non-finite sample.");
  return samples;
};

const parseRecord = (bytes: ArrayBuffer, offset: number): { record: ParsedRecord; recordSize: number } => {
  if (offset + 48 > bytes.byteLength) throw new Error("MiniSEED record is shorter than the fixed data header.");
  const view = new DataView(bytes, offset);
  const littleHeader = chooseHeaderEndian(view);
  const network = text(view, 18, 2);
  const station = text(view, 8, 5);
  const location = text(view, 13, 2);
  const channel = text(view, 15, 3);
  const year = readUint16(view, 20, littleHeader);
  const day = readUint16(view, 22, littleHeader);
  const hour = view.getUint8(24);
  const minute = view.getUint8(25);
  const second = view.getUint8(26);
  const fraction = readUint16(view, 28, littleHeader);
  const sampleCount = readInt16(view, 30, littleHeader);
  const rateFactor = readInt16(view, 32, littleHeader);
  const rateMultiplier = readInt16(view, 34, littleHeader);
  // Fixed-header time correction is expressed in 0.1 ms units. Bit 1 of
  // activity flags says the correction has already been applied to the data.
  const activityFlags = view.getUint8(36);
  const timeCorrection = readInt32(view, 40, littleHeader);
  const blocketteCount = view.getUint8(39);
  const dataOffset = readUint16(view, 44, littleHeader);
  const blocketteOffset = readUint16(view, 46, littleHeader);
  if (!network || !station || !channel) throw new Error("MiniSEED record is missing an NSLC code.");
  if (sampleCount < 0) throw new Error("MiniSEED record has a negative sample count.");
  if (dataOffset < 48 || dataOffset > bytes.byteLength - offset) throw new Error("MiniSEED data offset is outside the record.");
  let encoding = -1;
  let littleData = false;
  let recordSize = 0;
  let sampleRate = sampleRateFrom(rateFactor, rateMultiplier);
  let microseconds = 0;
  let cursor = blocketteOffset;
  for (let index = 0; index < blocketteCount; index += 1) {
    if (cursor < 48 || cursor + 4 > bytes.byteLength - offset) throw new Error("MiniSEED blockette chain is truncated.");
    const type = readUint16(view, cursor, littleHeader);
    let next = readUint16(view, cursor + 2, littleHeader);
    if (next === 0) next = dataOffset;
    if (next <= cursor && index + 1 < blocketteCount) throw new Error("MiniSEED blockette chain does not advance.");
    if (type === 1000) {
      if (cursor + 8 > bytes.byteLength - offset) throw new Error("MiniSEED blockette 1000 is truncated.");
      encoding = view.getUint8(cursor + 4);
      littleData = view.getUint8(cursor + 5) === 0;
      const exponent = view.getUint8(cursor + 6);
      if (exponent < 8 || exponent > 12) throw new Error("MiniSEED record length is outside the 256–4096 byte bound.");
      recordSize = 1 << exponent;
    } else if (type === 100) {
      if (cursor + 8 > bytes.byteLength - offset) throw new Error("MiniSEED blockette 100 is truncated.");
      sampleRate = view.getFloat32(cursor + 4, littleHeader);
    } else if (type === 1001) {
      if (cursor + 6 > bytes.byteLength - offset) throw new Error("MiniSEED blockette 1001 is truncated.");
      microseconds = view.getInt8(cursor + 5);
    }
    cursor = next;
  }
  if (encoding < 0 || !recordSize) throw new Error("MiniSEED blockette 1000 with encoding and record length is required.");
  if (offset + recordSize > bytes.byteLength) throw new Error("MiniSEED record is truncated at its declared record length.");
  if (!Number.isFinite(sampleRate) || sampleRate <= 0 || sampleRate > 2_000) throw new Error("MiniSEED sample rate is outside the bounded preview range.");
  const start = isoFromBTime(year, day, hour, minute, second, fraction);
  const correctionApplied = (activityFlags & 0x02) !== 0;
  const startEpochMs = start.epochMs
    + (correctionApplied ? 0 : timeCorrection / 10)
    // Blockette 1001 stores signed microseconds; convert to milliseconds.
    + microseconds / 1_000;
  const startTime = new Date(startEpochMs).toISOString();
  const endEpochMs = sampleCount > 0 ? startEpochMs + ((sampleCount - 1) / sampleRate) * 1_000 : startEpochMs;
  const endTime = new Date(endEpochMs).toISOString();
  const samples = decodeSamples(view, dataOffset, recordSize - dataOffset, sampleCount, encoding, littleData);
  return {
    record: {
      nslc: network + "." + station + "." + location + "." + channel,
      network,
      station,
      location,
      channel,
      startTime,
      endTime,
      startEpochMs,
      endEpochMs,
      sampleCount,
      sampleRate,
      encoding,
      encodingLabel: encodingName(encoding),
      samples,
    },
    recordSize,
  };
};

const parseMiniSeed = (bytes: ArrayBuffer): ParsedRecord[] => {
  if (bytes.byteLength === 0) throw new Error("The MiniSEED file is empty.");
  if (bytes.byteLength > WAVEFORM_PREVIEW_MAX_BYTES) throw new Error("The waveform preview is limited to files no larger than 2 MB.");
  const records: ParsedRecord[] = [];
  let offset = 0;
  while (offset < bytes.byteLength) {
    if (records.length >= 1_024) throw new Error("The waveform preview is limited to 1,024 MiniSEED records.");
    const parsed = parseRecord(bytes, offset);
    records.push(parsed.record);
    offset += parsed.recordSize;
  }
  if (offset !== bytes.byteLength) throw new Error("MiniSEED contains an incomplete trailing record.");
  return records;
};

const attributeValue = (attributes: string, name: string) => {
  const match = attributes.match(new RegExp("\\b" + name + "\\s*=\\s*([\"'])(.*?)\\1", "i"));
  return match?.[2]?.trim() ?? "";
};

const tagMatch = (value: string, name: string) => value.match(new RegExp("<(?:(?:[\\w.-]+):)?" + name + "\\b([^>]*)>([\\s\\S]*?)<\\/(?:(?:[\\w.-]+):)?" + name + "\\s*>", "i"));

const tagText = (value: string, name: string) => (tagMatch(value, name)?.[2] ?? "")
  .replace(/<[^>]*>/g, " ")
  .replace(/\s+/g, " ")
  .trim();

const externalReferenceCount = (value: string) => {
  const withoutNamespaces = value.replace(/\sxmlns(?::[\w.-]+)?\s*=\s*(["']).*?\1/gi, "");
  return (withoutNamespaces.match(/https?:\/\/[^\s"'<>]+/gi) ?? []).length;
};

const tagMatches = (value: string, name: string) => {
  const pattern = new RegExp(
    "<(?:(?:[\\w.-]+):)?" + name + "\\b([^>]*)>([\\s\\S]*?)<\\/(?:(?:[\\w.-]+):)?" + name + "\\s*>",
    "gi",
  );
  return Array.from(value.matchAll(pattern), (match) => ({ attributes: match[1], body: match[2] }));
};

const stationXmlCandidate = (
  networkCode: string,
  stationCode: string,
  channelAttributes: string,
  channelBody: string,
  externalReferences: number,
): StationXmlSummary => {
  const location = attributeValue(channelAttributes, "locationCode");
  const channel = attributeValue(channelAttributes, "code");
  if (!networkCode || !stationCode || !channel) throw new Error("StationXML is missing a network, station, or channel code.");
  const responseMatch = tagMatch(channelBody, "Response");
  const sensitivityMatch = responseMatch ? tagMatch(responseMatch[2], "InstrumentSensitivity") : null;
  const sensitivityText = sensitivityMatch ? tagText(sensitivityMatch[2], "Value") : "";
  const sensitivityValue = sensitivityText === "" ? Number.NaN : Number(sensitivityText);
  const inputUnit = sensitivityMatch ? tagText(sensitivityMatch[2], "InputUnits") : "";
  const startDate = attributeValue(channelAttributes, "startDate") || null;
  const endDate = attributeValue(channelAttributes, "endDate") || null;
  return Object.freeze({
    network: networkCode,
    station: stationCode,
    location,
    channel,
    responsePresent: Boolean(responseMatch && sensitivityMatch && sensitivityText !== "" && Number.isFinite(sensitivityValue)),
    instrumentSensitivity: Number.isFinite(sensitivityValue) ? sensitivityValue : null,
    inputUnit: inputUnit || null,
    startDate,
    endDate,
    externalReferenceCount: externalReferences,
  });
};

const parseStationXmlCandidates = (xml: string): StationXmlSummary[] => {
  if (!xml.trim()) throw new Error("The StationXML file is empty.");
  if (/<!DOCTYPE|<!ENTITY|<!--|<!\[CDATA\[/i.test(xml)) throw new Error("StationXML document types, comments, and CDATA sections are not supported.");
  const root = tagMatch(xml, "FDSNStationXML");
  if (!root) throw new Error("The response file is not a well-formed FDSN StationXML document.");
  const references = externalReferenceCount(xml);
  const candidates: StationXmlSummary[] = [];
  for (const network of tagMatches(root[2], "Network")) {
    const networkCode = attributeValue(network.attributes, "code");
    for (const station of tagMatches(network.body, "Station")) {
      const stationCode = attributeValue(station.attributes, "code");
      for (const channel of tagMatches(station.body, "Channel")) {
        candidates.push(stationXmlCandidate(
          networkCode,
          stationCode,
          channel.attributes,
          channel.body,
          references,
        ));
      }
    }
  }
  if (!candidates.length) throw new Error("StationXML must include a Network, Station, and Channel element.");
  return candidates;
};

const stationXmlCovers = (
  candidate: StationXmlSummary,
  waveform: Readonly<{ startEpochMs: number; endEpochMs: number }>,
) => {
  const start = candidate.startDate ? Date.parse(candidate.startDate) : Number.NEGATIVE_INFINITY;
  const end = candidate.endDate ? Date.parse(candidate.endDate) : Number.POSITIVE_INFINITY;
  const lower = Number.isFinite(start) ? start : Number.NEGATIVE_INFINITY;
  const upper = Number.isFinite(end) ? end : Number.POSITIVE_INFINITY;
  return waveform.startEpochMs >= lower && waveform.endEpochMs <= upper;
};

const parseStationXml = (
  xml: string,
  waveform: Readonly<{
    network: string;
    station: string;
    location: string;
    channel: string;
    startEpochMs: number;
    endEpochMs: number;
  }>,
): StationXmlSummary => {
  const candidates = parseStationXmlCandidates(xml);
  const codeMatches = candidates.filter((candidate) => (
    equalCode(candidate.network, waveform.network)
    && equalCode(candidate.station, waveform.station)
    && equalCode(candidate.location, waveform.location)
    && equalCode(candidate.channel, waveform.channel)
  ));
  const timeMatch = codeMatches.find((candidate) => stationXmlCovers(candidate, waveform));
  return timeMatch ?? codeMatches[0] ?? candidates[0];
};

const equalCode = (left: string, right: string) => left.trim() === right.trim();

const downsample = (samples: readonly number[], sampleRate: number): readonly WaveformPoint[] => {
  if (!samples.length) return Object.freeze([]);
  const bucketSize = Math.max(1, Math.ceil(samples.length / WAVEFORM_PREVIEW_MAX_POINTS));
  const points: WaveformPoint[] = [];
  for (let start = 0; start < samples.length; start += bucketSize) {
    const bucket = samples.slice(start, Math.min(samples.length, start + bucketSize));
    const low = Math.min(...bucket);
    const high = Math.max(...bucket);
    points.push(Object.freeze([(start + (bucket.length - 1) / 2) / sampleRate, low, high] as const));
  }
  return Object.freeze(points);
};

const digestHex = async (bytes: ArrayBuffer) => {
  if (!globalThis.crypto?.subtle) throw new Error("This browser cannot create the required SHA-256 provenance digest.");
  const digest = await globalThis.crypto.subtle.digest("SHA-256", bytes);
  return Array.from(new Uint8Array(digest), (value) => value.toString(16).padStart(2, "0")).join("");
};

const statusDetail = (state: WaveformGateState, detail: string) => state + " — " + detail;

export const buildLocalWaveformPreview = async (input: Readonly<{
  waveformFileName: string;
  stationXmlFileName: string;
  waveformBytes: ArrayBuffer;
  stationXmlText: string;
  inspectedAt: string;
  attribution: string | null;
}>): Promise<WaveformPreview> => {
  const records = parseMiniSeed(input.waveformBytes);
  const first = records[0];
  const nslc = first.nslc;
  if (records.some((record) => record.nslc !== nslc)) throw new Error("The preview accepts one NSLC channel at a time.");
  if (records.some((record) => Math.abs(record.sampleRate - first.sampleRate) > 1e-9)) throw new Error("MiniSEED records must share one sample rate.");
  const orderedRecords = [...records].sort((left, right) => left.startEpochMs - right.startEpochMs);
  const sampleCount = orderedRecords.reduce((sum, record) => sum + record.sampleCount, 0);
  if (sampleCount > WAVEFORM_PREVIEW_MAX_SAMPLES) throw new Error("The waveform preview is limited to 100,000 samples.");
  const startEpochMs = Math.min(...orderedRecords.map((record) => record.startEpochMs));
  const endEpochMs = Math.max(...orderedRecords.map((record) => record.endEpochMs));
  const stationXml = parseStationXml(input.stationXmlText, {
    network: first.network,
    station: first.station,
    location: first.location,
    channel: first.channel,
    startEpochMs,
    endEpochMs,
  });
  const durationSeconds = Math.max(0, (endEpochMs - startEpochMs) / 1_000);
  if (durationSeconds > WAVEFORM_PREVIEW_MAX_SECONDS) throw new Error("The waveform preview is limited to a 10-minute window.");
  const continuity = orderedRecords.slice(1).every((record, index) => {
    const previous = orderedRecords[index];
    const expectedStart = previous.startEpochMs + (previous.sampleCount / previous.sampleRate) * 1_000;
    // Only absorb BTime/blockette timestamp precision; never a whole sample period.
    return Math.abs(record.startEpochMs - expectedStart) <= RECORD_CONTINUITY_TOLERANCE_MS;
  });
  const stationMatches = equalCode(stationXml.network, first.network)
    && equalCode(stationXml.station, first.station)
    && equalCode(stationXml.location, first.location)
    && equalCode(stationXml.channel, first.channel);
  const samples = orderedRecords.flatMap((record) => record.samples);
  const attribution = input.attribution?.trim() || null;
  const gates: WaveformGate[] = [
    { id: "use-class", label: "Use class", state: "PASS", detail: "Browser-local user file only; no provider retrieval is requested." },
    { id: "transport", label: "Caching / proxy", state: "PASS", detail: "No server fetch, proxy, upload, persistent cache, or provider URL is accepted." },
    { id: "window", label: "Bounded window", state: "PASS", detail: sampleCount + " samples across " + durationSeconds.toFixed(3) + " seconds; limits are 100,000 samples and 10 minutes." },
    { id: "continuity", label: "Record continuity", state: continuity ? "PASS" : "BLOCK", detail: continuity ? "MiniSEED records are contiguous within one sample period." : "A gap or overlap was found between MiniSEED records; the preview will not connect it as a false trace." },
    { id: "attribution", label: "Attribution", state: attribution ? "PASS" : "BLOCK", detail: attribution ? "Visible attribution supplied for this browser-local inspection." : "Supply visible attribution before a waveform may be drawn." },
    { id: "redistribution", label: "Redistribution permission", state: "DENY", detail: "Raw bytes, samples, downloads, server redistribution, and derived persistence are disabled by scope." },
    { id: "response-metadata", label: "Response metadata", state: stationXml.responsePresent && stationMatches ? "PASS" : "BLOCK", detail: stationXml.responsePresent ? stationMatches ? "StationXML response and NSLC identity match the waveform." : "StationXML response exists but its NSLC does not match the waveform." : "StationXML response and InstrumentSensitivity are required; no response correction is performed." },
    { id: "provenance", label: "Provenance", state: "PASS", detail: "SHA-256 covers the exact local waveform bytes; StationXML identity and inspection time are retained." },
    { id: "correction-rollback", label: "Correction / rollback", state: "HOLD", detail: "No correction or rollback lane is present in a browser preview; source admission and publication remain held." },
  ];
  const hasBlock = gates.some((gate) => gate.state === "BLOCK");
  const allSamples = samples.length === sampleCount && sampleCount > 0;
  return Object.freeze({
    format: "kfm-browser-waveform-preview-v1",
    authority: "UNADMITTED_BROWSER_PREVIEW",
    publicEffect: "NONE",
    sourceActivation: "NOT_REQUESTED",
    waveformFileName: input.waveformFileName,
    stationXmlFileName: input.stationXmlFileName,
    inspectedAt: input.inspectedAt,
    byteLength: input.waveformBytes.byteLength,
    sha256: await digestHex(input.waveformBytes),
    nslc,
    network: first.network,
    station: first.station,
    location: first.location,
    channel: first.channel,
    startTime: new Date(startEpochMs).toISOString(),
    endTime: new Date(endEpochMs).toISOString(),
    durationSeconds,
    sampleRate: first.sampleRate,
    sampleCount,
    recordCount: records.length,
    encoding: first.encoding,
    encodingLabel: first.encodingLabel,
    stationXml,
    points: allSamples && !hasBlock ? downsample(samples, first.sampleRate) : Object.freeze([]),
    attribution,
    gates: Object.freeze(gates.map((gate) => Object.freeze(gate))),
    outcome: hasBlock ? "BLOCK" : "HOLD",
    plotAllowed: allSamples && !hasBlock,
  });
};

export const waveformPreviewAudit = (preview: WaveformPreview) => Object.freeze({
  format: preview.format,
  authority: preview.authority,
  publicEffect: preview.publicEffect,
  sourceActivation: preview.sourceActivation,
  files: {
    waveform: { name: preview.waveformFileName, byteLength: preview.byteLength, sha256: preview.sha256 },
    stationXml: { name: preview.stationXmlFileName },
  },
  inspectedAt: preview.inspectedAt,
  nslc: preview.nslc,
  time: { start: preview.startTime, end: preview.endTime, durationSeconds: preview.durationSeconds },
  samples: { count: preview.sampleCount, sampleRate: preview.sampleRate, points: "OMITTED_FROM_AUDIT" },
  stationXml: preview.stationXml,
  attribution: preview.attribution,
  gates: preview.gates,
  outcome: preview.outcome,
  effects: "NO_UPLOAD_NO_CACHE_NO_PROXY_NO_SOURCE_ADMISSION_NO_REDISTRIBUTION_NO_CORRECTION",
});

export const waveformPreviewConstants = Object.freeze({
  maxBytes: WAVEFORM_PREVIEW_MAX_BYTES,
  maxSeconds: WAVEFORM_PREVIEW_MAX_SECONDS,
  maxSamples: WAVEFORM_PREVIEW_MAX_SAMPLES,
  maxPoints: WAVEFORM_PREVIEW_MAX_POINTS,
  supportedEncodings: Object.freeze([1, 3, 4, 5]),
});
