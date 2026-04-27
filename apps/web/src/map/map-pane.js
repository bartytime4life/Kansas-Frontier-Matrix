export function createMapPane() {
  const section = document.createElement("section");
  section.className = "map-pane";
  section.innerHTML = `
    <h2>Map Canvas</h2>
    <div class="map-surface">MapLibre adapter placeholder</div>
    <p class="note">Render released layers only; no direct RAW/WORK/QUARANTINE access.</p>
  `;
  return section;
}
