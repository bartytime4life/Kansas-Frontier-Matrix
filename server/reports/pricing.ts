import { createHash, randomUUID } from "node:crypto";

export const REPORT_PRODUCTS = ["brief", "standard", "technical"] as const;
export const EVIDENCE_BANDS = ["source-context", "corroborated", "measured"] as const;
export type ReportProduct = typeof REPORT_PRODUCTS[number];
export type EvidenceBand = typeof EVIDENCE_BANDS[number];

export class ReportServiceError extends Error {
  constructor(public readonly code: string, public readonly status: number) {
    super(code);
  }
}

export type PricingPolicy = Readonly<{
  schemaVersion: 1;
  version: string;
  currency: string;
  minimumMinor: number;
  maximumMinor: number;
  laborRateMinorPerHour: number;
  productBaseMinor: Readonly<Record<ReportProduct, number>>;
  evidenceBaseMinor: Readonly<Record<EvidenceBand, number>>;
  quoteTtlSeconds: number;
}>;

export type ReportSourceSnapshot = Readonly<{
  sourceId: string;
  title: string;
  digest: string;
  officialUrl: string;
  rights: "public" | "restricted" | "unreviewed";
  observationTime: string | null;
  retrievedAt: string;
  units: readonly string[];
  limitations: readonly string[];
}>;

/** Constructed by server source adapters, never from a purchaser's assessment. */
export type ServerReportAssessment = Readonly<{
  input: unknown;
  product: ReportProduct;
  eligibility: "eligible" | "insufficient" | "held" | "restricted";
  evidenceBand: EvidenceBand;
  evidenceBasis: string;
  measuredValidation?: Readonly<{ method: string; value: number; unit: string; basisUrl: string }>;
  estimatedManualMinutes: number;
  effortBasis: string;
  sources: readonly ReportSourceSnapshot[];
  limitations: readonly string[];
}>;

export type ReportQuote = Readonly<{
  id: string;
  ownerId: string;
  createdAt: string;
  expiresAt: string;
  policyVersion: string;
  policyDigest: string;
  inputDigest: string;
  sourceDigest: string;
  assessmentDigest: string;
  currency: string;
  amountMinor: number;
  breakdown: Readonly<{
    productMinor: number;
    evidenceMinor: number;
    effortMinor: number;
    minimumAdjustmentMinor: number;
  }>;
  assessment: ServerReportAssessment;
}>;

const fail = (code: string, status = 422): never => { throw new ReportServiceError(code, status); };
const integer = (value: unknown, minimum: number, maximum = Number.MAX_SAFE_INTEGER): value is number =>
  typeof value === "number" && Number.isSafeInteger(value) && value >= minimum && value <= maximum;
const boundedText = (value: unknown, maximum = 2000): value is string =>
  typeof value === "string" && value.trim().length > 0 && value.length <= maximum;
const digestPattern = /^[a-f0-9]{64}$/;

/** Reject ambiguous/non-JSON values; object key order cannot change a quote. */
export function canonicalJson(value: unknown, depth = 0): string {
  if (depth > 24) return fail("REPORT_INPUT_TOO_COMPLEX", 400);
  if (value === null || typeof value === "boolean" || typeof value === "string") return JSON.stringify(value);
  if (typeof value === "number" && Number.isFinite(value)) return JSON.stringify(value);
  if (Array.isArray(value)) return `[${Array.from(value, (item) => canonicalJson(item, depth + 1)).join(",")}]`;
  if (typeof value === "object" && value && Object.getPrototypeOf(value) === Object.prototype) {
    return `{${Object.keys(value).sort().map((key) => `${JSON.stringify(key)}:${canonicalJson((value as Record<string, unknown>)[key], depth + 1)}`).join(",")}}`;
  }
  return fail("REPORT_INPUT_INVALID", 400);
}

export const reportDigest = (value: unknown): string => createHash("sha256").update(canonicalJson(value)).digest("hex");

function httpsUrl(value: string): boolean {
  try {
    const url = new URL(value);
    return url.protocol === "https:" && !url.username && !url.password && Boolean(url.hostname);
  } catch { return false; }
}

export function validatePricingPolicy(value: unknown): PricingPolicy {
  if (!value || typeof value !== "object") return fail("REPORT_PRICING_NOT_CONFIGURED", 503);
  const policy = value as PricingPolicy;
  if (policy.schemaVersion !== 1 || !boundedText(policy.version, 128)
    || typeof policy.currency !== "string" || !Intl.supportedValuesOf("currency").includes(policy.currency)
    || !integer(policy.minimumMinor, 1) || !integer(policy.maximumMinor, policy.minimumMinor)
    || !integer(policy.laborRateMinorPerHour, 0) || !integer(policy.quoteTtlSeconds, 60, 86400)
    || !REPORT_PRODUCTS.every((key) => integer(policy.productBaseMinor?.[key], 0))
    || !EVIDENCE_BANDS.every((key) => integer(policy.evidenceBaseMinor?.[key], 0))) {
    return fail("REPORT_PRICING_NOT_CONFIGURED", 503);
  }
  return JSON.parse(canonicalJson(policy)) as PricingPolicy;
}

function validateAssessment(assessment: ServerReportAssessment): void {
  if (assessment.eligibility !== "eligible") return fail("REPORT_EVIDENCE_INSUFFICIENT");
  if (!REPORT_PRODUCTS.includes(assessment.product) || !EVIDENCE_BANDS.includes(assessment.evidenceBand)
    || !boundedText(assessment.evidenceBasis) || !boundedText(assessment.effortBasis)
    || !integer(assessment.estimatedManualMinutes, 0, 525600)
    || !Array.isArray(assessment.limitations) || assessment.limitations.length > 100
    || !assessment.limitations.every((value) => boundedText(value))
    || !Array.isArray(assessment.sources) || assessment.sources.length === 0 || assessment.sources.length > 100) {
    return fail("REPORT_ASSESSMENT_INVALID");
  }
  const uniqueSources = new Set<string>();
  for (const source of assessment.sources) {
    if (!boundedText(source.sourceId, 128) || uniqueSources.has(source.sourceId)
      || !boundedText(source.title, 500) || !digestPattern.test(source.digest)
      || !httpsUrl(source.officialUrl) || source.rights !== "public"
      || (source.observationTime !== null && !boundedText(source.observationTime, 200))
      || !Number.isFinite(Date.parse(source.retrievedAt))
      || !Array.isArray(source.units) || source.units.length > 100 || !source.units.every((value: unknown) => boundedText(value, 100))
      || !Array.isArray(source.limitations) || source.limitations.length > 100 || !source.limitations.every((value: unknown) => boundedText(value))) {
      return fail("REPORT_SOURCE_NOT_ELIGIBLE");
    }
    uniqueSources.add(source.sourceId);
  }
  if (assessment.evidenceBand === "measured") {
    const metric = assessment.measuredValidation;
    if (!metric || !boundedText(metric.method) || !Number.isFinite(metric.value)
      || !boundedText(metric.unit, 100) || !httpsUrl(metric.basisUrl)) return fail("REPORT_VALIDATION_MISSING");
  }
  const serialized = canonicalJson(assessment);
  if (Buffer.byteLength(serialized) > 262144 || Buffer.byteLength(canonicalJson(assessment.input)) > 32768) {
    return fail("REPORT_INPUT_TOO_LARGE", 413);
  }
}

function deepFreeze<T>(value: T): T {
  if (value && typeof value === "object") {
    for (const nested of Object.values(value)) deepFreeze(nested);
    Object.freeze(value);
  }
  return value;
}

export function createReportQuote(ownerId: string, assessment: ServerReportAssessment, rawPolicy: unknown, now = new Date()): ReportQuote {
  if (!boundedText(ownerId, 256) || !Number.isFinite(now.getTime())) return fail("REPORT_SESSION_REQUIRED", 401);
  const policy = validatePricingPolicy(rawPolicy);
  validateAssessment(assessment);
  const productMinor = policy.productBaseMinor[assessment.product];
  const evidenceMinor = policy.evidenceBaseMinor[assessment.evidenceBand];
  // Ceiling division in integer minor units, never floating-point money.
  const effort = (BigInt(assessment.estimatedManualMinutes) * BigInt(policy.laborRateMinorPerHour) + 59n) / 60n;
  const subtotal = BigInt(productMinor) + BigInt(evidenceMinor) + effort;
  const total = subtotal < BigInt(policy.minimumMinor) ? BigInt(policy.minimumMinor) : subtotal;
  if (total > BigInt(policy.maximumMinor)) return fail("REPORT_REQUIRES_CUSTOM_QUOTE");
  const captured = JSON.parse(canonicalJson(assessment)) as ServerReportAssessment;
  const sourceSnapshots = [...captured.sources].sort((left, right) => left.sourceId < right.sourceId ? -1 : left.sourceId > right.sourceId ? 1 : 0);
  return deepFreeze({
    id: randomUUID(), ownerId, createdAt: now.toISOString(),
    expiresAt: new Date(now.getTime() + policy.quoteTtlSeconds * 1000).toISOString(),
    policyVersion: policy.version, policyDigest: reportDigest(policy),
    inputDigest: reportDigest(captured.input), sourceDigest: reportDigest(sourceSnapshots),
    assessmentDigest: reportDigest(captured), currency: policy.currency, amountMinor: Number(total),
    breakdown: { productMinor, evidenceMinor, effortMinor: Number(effort), minimumAdjustmentMinor: Number(total - subtotal) },
    assessment: captured,
  });
}

export function assertQuoteOwner(quote: ReportQuote, ownerId: string): void {
  if (quote.ownerId !== ownerId) return fail("REPORT_NOT_FOUND", 404);
}

export function assertQuoteCurrent(quote: ReportQuote, ownerId: string, input: unknown, now = new Date()): void {
  assertQuoteOwner(quote, ownerId);
  if (!Number.isFinite(now.getTime()) || now.getTime() >= Date.parse(quote.expiresAt)) return fail("REPORT_QUOTE_EXPIRED", 409);
  if (quote.inputDigest !== reportDigest(input)) return fail("REPORT_SCOPE_CHANGED", 409);
  if (quote.assessmentDigest !== reportDigest(quote.assessment)) return fail("REPORT_QUOTE_CORRUPT", 409);
}
