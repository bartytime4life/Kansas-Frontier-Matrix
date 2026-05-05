const evidenceDrawer = {
  id: "drawer-hydro-001",
  ui_trust_state: "EVIDENCE_MISSING",
  release_status: "ABSTAIN",
  evidence_ref: "evr-hydro-synth-001",
  evidence_bundle_id: "evb-hydro-synth-001",
};

document.getElementById("app").innerHTML = `
  <p>Timeline: 2026 synthetic scope</p>
  <p>Selected hydrology fixture: hydro-feature-001</p>
  <div>Trust chips: <span class="chip">EVIDENCE_RESOLVED</span><span class="chip">POLICY_ALLOW</span></div>

  <h3>Evidence Drawer</h3>
  <div class="drawer">
    <p><strong>id:</strong> ${evidenceDrawer.id}</p>
    <p><strong>trust:</strong> ${evidenceDrawer.ui_trust_state}</p>
    <p><strong>release:</strong> ${evidenceDrawer.release_status}</p>
    <p><strong>evidence_ref:</strong> ${evidenceDrawer.evidence_ref}</p>
    <p><strong>bundle:</strong> ${evidenceDrawer.evidence_bundle_id}</p>
  </div>

  <h3>Focus Mode</h3>
  <ul><li>ANSWER</li><li>ABSTAIN</li><li>DENY</li><li>ERROR</li></ul>
  <p>Negative states: MISSING_EVIDENCE, SOURCE_STALE, DENIED_BY_POLICY, GENERALIZED_GEOMETRY, RESTRICTED_ACCESS, CITATION_FAILED, RELEASE_WITHDRAWN, RUNTIME_ERROR</p>
`;
