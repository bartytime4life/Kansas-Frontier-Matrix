export function createEvidenceDrawer() {
  const panel = document.createElement("section");
  panel.className = "panel";
  panel.setAttribute("aria-labelledby", "evidence-drawer-heading");
  panel.innerHTML = `
    <h2 id="evidence-drawer-heading">Evidence Drawer</h2>
    <p id="evidence-drawer-status" role="status" aria-live="polite">Status: <strong>Support available</strong></p>
    <ul>
      <li>Source role: state agency</li>
      <li>EvidenceBundle: eb://placeholder/1</li>
      <li>Policy: public-safe generalized geometry</li>
    </ul>
  `;
  return panel;
}
