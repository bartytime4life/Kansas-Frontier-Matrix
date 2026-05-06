import { createMapPane } from "../map/map-pane.js";
import { createEvidenceDrawer } from "../evidence/evidence-drawer.js";
import { createFocusPanel } from "../focus/focus-panel.js";

export function createShellFrame() {
  const shell = document.createElement("main");
  shell.className = "shell-frame";

  shell.innerHTML = `
    <a class="skip-link" href="#workspace-start">Skip to workspace</a>
    <header class="top-bar">
      <h1>KFM Governed Web Shell</h1>
      <p class="subtitle">Map-first · Evidence-first · Cite-or-abstain</p>
    </header>
    <section class="workspace" id="workspace-start" tabindex="-1" aria-label="Map and trust workspace">
      <aside class="left-rail" aria-label="Primary">
        <h2>Layers</h2>
        <ul>
          <li>Hydrology (released)</li>
          <li>Habitat suitability (reviewed)</li>
          <li>Policy overlays (role-gated)</li>
        </ul>
      </aside>
      <section class="map-column"></section>
      <aside class="right-stack"></aside>
    </section>
  `;

  shell.querySelector(".map-column")?.appendChild(createMapPane());
  const rightStack = shell.querySelector(".right-stack");
  rightStack?.appendChild(createEvidenceDrawer());
  rightStack?.appendChild(createFocusPanel());

  return shell;
}
