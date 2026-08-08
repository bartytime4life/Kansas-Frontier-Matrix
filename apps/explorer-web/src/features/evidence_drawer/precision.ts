export type PrecisionDisclosure = Readonly<{
  spatial: Readonly<{
    statement: string;
    representation: string;
    resolution: Readonly<{ value: number; unit: string }> | null;
    generalization_applied: boolean;
    generalization_ref: string | null;
  }>;
  temporal: Readonly<{
    statement: string;
    granularity: string;
    observation_interval: Readonly<{ start: string; end: string }> | null;
  }>;
  attribute: Readonly<{
    statement: string;
    measure: string;
    unit: string | null;
    significant_digits: number | null;
    classification_granularity: string | null;
  }>;
  basis: Readonly<{
    evidence_refs: readonly unknown[];
    source_refs: readonly string[];
    transform_refs: readonly string[];
  }>;
}>;

const ownKeys = (value: Record<string, unknown>, expected: readonly string[]): boolean =>
  Object.keys(value).sort().join("\u0000") === [...expected].sort().join("\u0000");

const record = (value: unknown): value is Record<string, unknown> =>
  typeof value === "object" && value !== null && !Array.isArray(value);

const bounded = (value: unknown, maximum = 512): value is string =>
  typeof value === "string" && value.length > 0 && value.length <= maximum;

const nullableBounded = (value: unknown): value is string | null =>
  value === null || bounded(value);

const stringArray = (value: unknown, minimum: number): value is string[] =>
  Array.isArray(value) &&
  value.length >= minimum &&
  value.every((item) => bounded(item)) &&
  new Set(value).size === value.length;

export function parsePrecisionDisclosure(value: unknown): PrecisionDisclosure | null {
  if (
    !record(value) ||
    !ownKeys(value, ["spatial", "temporal", "attribute", "basis"]) ||
    !record(value.spatial) ||
    !record(value.temporal) ||
    !record(value.attribute) ||
    !record(value.basis)
  ) {
    return null;
  }

  const spatial = value.spatial;
  const temporal = value.temporal;
  const attribute = value.attribute;
  const basis = value.basis;

  if (
    !ownKeys(spatial, [
      "statement",
      "representation",
      "resolution",
      "generalization_applied",
      "generalization_ref",
    ]) ||
    !bounded(spatial.statement, 240) ||
    !bounded(spatial.representation, 64) ||
    typeof spatial.generalization_applied !== "boolean" ||
    !nullableBounded(spatial.generalization_ref)
  ) {
    return null;
  }

  if (spatial.resolution !== null) {
    if (
      !record(spatial.resolution) ||
      !ownKeys(spatial.resolution, ["value", "unit"]) ||
      typeof spatial.resolution.value !== "number" ||
      !Number.isFinite(spatial.resolution.value) ||
      spatial.resolution.value < 0 ||
      !bounded(spatial.resolution.unit, 64)
    ) {
      return null;
    }
  }

  if (
    !ownKeys(temporal, ["statement", "granularity", "observation_interval"]) ||
    !bounded(temporal.statement, 240) ||
    !bounded(temporal.granularity, 64)
  ) {
    return null;
  }
  if (temporal.observation_interval !== null) {
    if (
      !record(temporal.observation_interval) ||
      !ownKeys(temporal.observation_interval, ["start", "end"]) ||
      !bounded(temporal.observation_interval.start) ||
      !bounded(temporal.observation_interval.end)
    ) {
      return null;
    }
  }

  if (
    !ownKeys(attribute, [
      "statement",
      "measure",
      "unit",
      "significant_digits",
      "classification_granularity",
    ]) ||
    !bounded(attribute.statement, 240) ||
    !bounded(attribute.measure, 128) ||
    !nullableBounded(attribute.unit) ||
    !nullableBounded(attribute.classification_granularity) ||
    !(
      attribute.significant_digits === null ||
      (Number.isInteger(attribute.significant_digits) &&
        Number(attribute.significant_digits) >= 0 &&
        Number(attribute.significant_digits) <= 15)
    )
  ) {
    return null;
  }

  if (
    !ownKeys(basis, ["evidence_refs", "source_refs", "transform_refs"]) ||
    !Array.isArray(basis.evidence_refs) ||
    basis.evidence_refs.length < 1 ||
    !stringArray(basis.source_refs, 1) ||
    !stringArray(basis.transform_refs, 0)
  ) {
    return null;
  }

  return value as PrecisionDisclosure;
}

export function precisionDisclosureLabels(value: unknown): readonly string[] | null {
  const parsed = parsePrecisionDisclosure(value);
  if (!parsed) return null;

  const labels = [
    `Spatial: ${parsed.spatial.statement}`,
    `Temporal: ${parsed.temporal.statement}`,
    `Attribute: ${parsed.attribute.statement}`,
  ];
  if (parsed.spatial.generalization_applied) {
    labels.push("Spatial generalization applied");
  }
  return labels;
}
