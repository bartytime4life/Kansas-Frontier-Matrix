export function createEvidenceDrawer() {
  const panel = document.createElement("section");
  panel.className = "panel";
  panel.innerHTML = `
    <h2>Evidence Drawer</h2>
    <p>Status: <strong>Support available</strong></p>
    <ul>
      <li>Source role: state agency</li>
      <li>EvidenceBundle: eb://placeholder/1</li>
      <li>Policy: public-safe generalized geometry</li>
    </ul>
  `;
  return panel;
}
