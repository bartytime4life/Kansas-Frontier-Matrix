/** Aviation public boundary. No environment toggle can admit a candidate.
 * Future release integration must reuse KFM policy/evidence replay, not this hold.
 */
export const AVIATION_RELEASE_PROFILE_READY = false;
export const AVIATION_HEADERS = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" };
export const aviationHoldDecision = (evaluated_at = new Date().toISOString()) => ({
  decision_id: "kfm:decision:aviation-public-hold:v1", outcome: "ABSTAIN", policy_family: "capability",
  reasons: ["AVIATION_RELEASE_PROFILE_REQUIRED"], obligations: ["WITHHOLD_PUBLIC_FEATURES", "NO_RAW_OR_CANDIDATE_ACCESS"], evaluated_at,
});
export const aviationNegative = (reason_code, outcome = "ABSTAIN") => ({ envelope: { outcome, reason_code, evidence_refs: [], policy_state: "withheld", freshness: "unknown" } });
export function parseAviationQuery(url) {
  if (url.search.length > 256) throw new Error("INVALID_QUERY");
  const entries = [...url.searchParams];
  if (entries.length > 3 || new Set(entries.map(([key]) => key)).size !== entries.length || entries.some(([key]) => !["county", "edition", "q"].includes(key))) throw new Error("INVALID_QUERY");
  const county = url.searchParams.get("county") ?? "", edition = url.searchParams.get("edition") ?? "present", q = url.searchParams.get("q") ?? "";
  if (county && !/^[A-Z][A-Z .'-]{0,63}$/.test(county) || q.length > 64 || /[\u0000-\u001f]/.test(q)
      || edition !== "present" && (!/^\d{4}-\d{2}-\d{2}$/.test(edition) || new Date(edition + "T00:00:00Z").toISOString().slice(0, 10) !== edition)) throw new Error("INVALID_QUERY");
  return { county, edition, q };
}
export async function aviationRead(request) {
  try { parseAviationQuery(new URL(request.url)); }
  catch { return Response.json(aviationNegative("INVALID_QUERY", "ERROR"), { status: 400, headers: AVIATION_HEADERS }); }
  // Deliberately before acquiring a database, storage, credential or provider client.
  const decision = aviationHoldDecision();
  return Response.json({ ...aviationNegative(decision.reasons[0]), policy_decision: decision }, { headers: AVIATION_HEADERS });
}
