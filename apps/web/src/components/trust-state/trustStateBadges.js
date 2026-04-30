export const TRUST_STATES = ["ANSWER", "ABSTAIN", "DENY", "ERROR", "STALE", "REDACTED", "SUPERSEDED"];

export function isKnownTrustState(value) {
  return TRUST_STATES.includes(value);
}
