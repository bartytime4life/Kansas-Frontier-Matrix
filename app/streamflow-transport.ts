/** Lossless wire representation only; the canonical observation contract remains unchanged. */
export const STREAMFLOW_TRANSPORT = "kfm-usgs-observation-dictionaries-v1";
const KEYS = ["stationId", "observedAt", "value", "unit", "parameterCode", "statisticId", "approvalStatus", "qualifier", "qualifiers", "lastModified"] as const;
const MAX_ROWS = 100_000;
const record = (value: unknown): value is Record<string, unknown> => Boolean(value) && typeof value === "object" && !Array.isArray(value);

export const encodeStreamflowTransport = (bundle: Record<string, unknown>): Record<string, unknown> => {
  const observations = bundle.observations;
  // If a future adapter adds fields, use its complete legacy payload rather than drop them.
  if (!Array.isArray(observations) || observations.length > MAX_ROWS || !observations.every(row => record(row)
    && Object.keys(row).length === KEYS.length && KEYS.every(key => Object.hasOwn(row, key)))) return bundle;
  const values: unknown[][] = KEYS.map(() => []);
  const indices = KEYS.map(() => new Map<string, number>());
  const rows = observations.map(observation => KEYS.map((key, column) => {
    const value = observation[key], serialized = JSON.stringify(value);
    if (serialized === undefined) throw new Error("A streamflow observation field cannot be encoded.");
    let index = indices[column].get(serialized);
    if (index === undefined) { index = values[column].length; values[column].push(value); indices[column].set(serialized, index); }
    return index;
  }));
  return { ...bundle, transport: STREAMFLOW_TRANSPORT, observations: { values, rows } };
};

/** Expand only bounded fixed columns; the existing canonical parser still validates every value. */
export const decodeStreamflowTransport = (value: unknown): unknown => {
  if (!record(value) || !Object.hasOwn(value, "transport")) return value;
  if (value.transport !== STREAMFLOW_TRANSPORT || !record(value.observations)) throw new Error("Unsupported streamflow transport contract.");
  const { values, rows } = value.observations;
  if (!Array.isArray(rows) || rows.length > MAX_ROWS || !Array.isArray(values) || values.length !== KEYS.length
    || !values.every(column => Array.isArray(column) && column.length <= rows.length)) throw new Error("Invalid compact streamflow dimensions.");
  const observations = rows.map(row => {
    if (!Array.isArray(row) || row.length !== KEYS.length || !row.every((index, column) => Number.isSafeInteger(index)
      && index >= 0 && index < values[column].length)) throw new Error("Invalid compact streamflow observation index.");
    return Object.fromEntries(KEYS.map((key, column) => [key, values[column][row[column]]]));
  });
  const { transport: _transport, ...bundle } = value;
  return { ...bundle, observations };
};
