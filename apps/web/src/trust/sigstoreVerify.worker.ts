export type TrustDecision = "ALLOW_RENDER" | "DENY_RENDER" | "ABSTAIN" | "ERROR";
export type VerifyInput = { manifest: any; expectedArtifactDigest: string; policyProfile?: string; nowIso?: string };
export type VerifyResult = { decision: TrustDecision; reason_codes: string[]; receipt_ref?: string };

const SUPPORTED_IDENTITY_PREFIX = "spiffe://kfm/signers/";

export function verifyManifest(input: VerifyInput): VerifyResult {
  try {
    const m = input.manifest;
    if (!m?.signature?.bundle) return { decision: "DENY_RENDER", reason_codes: ["MISSING_BUNDLE"] };
    if (!m?.signature?.signature) return { decision: "DENY_RENDER", reason_codes: ["MISSING_SIGNATURE"] };
    if (!m?.artifacts?.[0]?.digest) return { decision: "DENY_RENDER", reason_codes: ["MISSING_DIGEST"] };
    if (m.signature.signed_digest !== m.artifacts[0].digest || m.artifacts[0].digest !== input.expectedArtifactDigest) return { decision: "DENY_RENDER", reason_codes: ["ARTIFACT_DIGEST_MISMATCH"] };
    if (!String(m.signer_identity || "").startsWith(SUPPORTED_IDENTITY_PREFIX)) return { decision: "DENY_RENDER", reason_codes: ["UNSUPPORTED_SIGNER_IDENTITY"] };
    const now = new Date(input.nowIso || "2026-05-02T00:00:00Z");
    if (new Date(m.trust_root_expires_at) <= now) return { decision: "ABSTAIN", reason_codes: ["STALE_TRUST_ROOT"] };
    if (m.release_state !== "released" || m.policy_label !== "public-safe" || input.policyProfile === "deny") return { decision: "DENY_RENDER", reason_codes: ["POLICY_DENIED"] };
    return { decision: "ALLOW_RENDER", reason_codes: ["VERIFIED"], receipt_ref: `receipt:${m.manifest_id}` };
  } catch {
    return { decision: "ERROR", reason_codes: ["VERIFICATION_ERROR"] };
  }
}

self.onmessage = (ev: MessageEvent<VerifyInput>) => {
  const result = verifyManifest(ev.data);
  self.postMessage(result);
};
