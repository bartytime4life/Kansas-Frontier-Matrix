export function createFocusPanel() {
  const panel = document.createElement("section");
  panel.className = "panel";
  panel.setAttribute("aria-labelledby", "focus-panel-heading");
  panel.innerHTML = `
    <h2 id="focus-panel-heading">Focus Mode</h2>
    <p>Question runtime is delegated to the governed API.</p>
    <div class="runtime-outcome" role="status" aria-live="polite">Latest outcome: <strong>ABSTAIN</strong> (insufficient released support).</div>
  `;
  return panel;
}
