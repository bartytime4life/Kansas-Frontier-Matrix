export function createFocusPanel() {
  const panel = document.createElement("section");
  panel.className = "panel";
  panel.innerHTML = `
    <h2>Focus Mode</h2>
    <p>Question runtime is delegated to the governed API.</p>
    <div class="runtime-outcome">Latest outcome: <strong>ABSTAIN</strong> (insufficient released support).</div>
  `;
  return panel;
}
