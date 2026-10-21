/** Selection clock shared by edition/layer/Present actions. No network or AI SQL. */
export function createAviationSession() {
  let generation = 0, controller;
  return {
    begin() { controller?.abort(); controller = new AbortController(); const ticket = ++generation; return { signal: controller.signal, current: () => ticket === generation && !controller.signal.aborted }; },
    retire() { generation++; controller?.abort(); },
  };
}

export function aviationQuestion(tool, context) {
  if (!["county-airports", "selected-facility"].includes(tool)) return { outcome: "DENY", reason_code: "TOOL_NOT_ALLOWED", evidence_refs: [] };
  // No observation/ownership/mission analysis and no general-purpose SQL surface.
  return { outcome: "ABSTAIN", reason_code: "AVIATION_RELEASE_PROFILE_REQUIRED", evidence_refs: [], context: { county: context.county ?? null, edition: context.edition ?? null } };
}
