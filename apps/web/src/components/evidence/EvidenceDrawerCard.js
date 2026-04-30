export function renderEvidenceDrawerCard(payload) {
  return {
    claimId: payload.claimId,
    claimText: payload.claimText,
    sources: payload.sources ?? [],
    trustState: payload.trustState ?? "unknown"
  };
}
