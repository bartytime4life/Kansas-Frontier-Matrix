import { browserJsonRequest } from "./browser-json-request";
import { publicKnowledgeRecord, type KnowledgeRecord, type KnowledgeQuery } from "./kansas-knowledge";

export type KnowledgeResult = {
  envelope: { outcome: string; reason_code: string };
  data?: { records: KnowledgeRecord[]; release_id: string; reviewed_at: string; released_at: string; has_more: boolean };
};
export const knowledgeUnavailable = (): KnowledgeResult => ({ envelope: { outcome: "ERROR", reason_code: "STORAGE_UNAVAILABLE" } });

export function parseKnowledgeRead(value: unknown, query: KnowledgeQuery): KnowledgeResult {
  const result = value as KnowledgeResult | null;
  if (!result?.envelope) throw new Error("Invalid knowledge response");
  const { outcome, reason_code } = result.envelope;
  if (outcome !== "ANSWER") {
    if (!(outcome === "ABSTAIN" && ["NO_APPROVED_KNOWLEDGE", "RECORD_NOT_FOUND", "RELEASE_HELD", "INVALID_QUERY"].includes(reason_code)) &&
        !(outcome === "ERROR" && reason_code === "STORAGE_UNAVAILABLE")) throw new Error("Invalid knowledge outcome");
    // Negative responses cannot carry records, even if a malformed response includes data.
    return { envelope: { outcome, reason_code } };
  }
  const data = result.data;
  if (reason_code !== "RELEASED" || !data || !/^sha256:[0-9a-f]{64}$/.test(data.release_id) ||
      !Array.isArray(data.records) || data.records.length < 1 || data.records.length > (query.kind === "record" ? 1 : 20) ||
      typeof data.has_more !== "boolean" || !Number.isFinite(Date.parse(data.reviewed_at)) ||
      !Number.isFinite(Date.parse(data.released_at)) || Date.parse(data.reviewed_at) > Date.parse(data.released_at)) throw new Error("Invalid knowledge release");
  const records = data.records.map(record => {
    const { assertions, ...row } = record;
    const checked = publicKnowledgeRecord({ ...row, assertions_json: JSON.stringify(assertions) });
    if (checked.release_id !== data.release_id || (query.kind === "record" && checked.record_id !== query.id)) throw new Error("Knowledge identity mismatch");
    return checked;
  });
  if (new Set(records.map(record => record.record_id)).size !== records.length) throw new Error("Duplicate knowledge records");
  return { envelope: { outcome, reason_code }, data: { ...data, records } };
}

export async function readKnowledge(query: KnowledgeQuery, signal: AbortSignal): Promise<KnowledgeResult> {
  const params = new URLSearchParams(query.kind === "record" ? { id: query.id } : { term: query.term });
  const { response, body } = await browserJsonRequest(`/api/governed/v1/knowledge?${params}`, { signal, maxBytes: 1024 * 1024 });
  const result = parseKnowledgeRead(body, query);
  if (!response.ok && result.envelope.reason_code !== "INVALID_QUERY") throw new Error("Knowledge unavailable");
  return result;
}
