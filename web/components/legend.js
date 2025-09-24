// web/components/legend.js
// Kansas-Frontier-Matrix — Dynamic Legend Component
// --------------------------------------------------
// Notes:
// - Reads visible layers from MapLibre map + config/layers.json
// - Builds a collapsible legend control
// - Each layer can define symbology in layers.json under "legend" key
// - Example: { "id": "usgs_topo", "title": "USGS Topo Maps", "legend": [{ "color": "#654321", "label": "Contours" }] }

export default class LegendControl {
  constructor(options = {}) {
    this._container = null;
    this._map = null;
    this._layersConfig = options.layersConfig || [];
    this._title = options.title || "Legend";
  }

  onAdd(map) {
    this._map = map;
    this._container = document.createElement("div");
    this._container.className = "kfm-legend maplibregl-ctrl";

    const header = document.createElement("div");
    header.className = "kfm-legend-header";
    header.innerText = this._title;
    header.onclick = () => this._toggleCollapse();

    const body = document.createElement("div");
    body.className = "kfm-legend-body";

    this._container.appendChild(header);
    this._container.appendChild(body);

    this._renderLayers(body);

    return this._container;
  }

  onRemove() {
    if (this._container && this._container.parentNode) {
      this._container.parentNode.removeChild(this._container);
    }
    this._map = null;
  }

  _renderLayers(body) {
    body.innerHTML = "";

    this._layersConfig.forEach((layer) => {
      if (!layer.legend || !Array.isArray(layer.legend)) return;

      const section = document.createElement("div");
      section.className = "kfm-legend-section";

      const title = document.createElement("div");
      title.className = "kfm-legend-title";
      title.innerText = layer.title || layer.id;

      section.appendChild(title);

      layer.legend.forEach((item) => {
        const row = document.createElement("div");
        row.className = "kfm-legend-row";

        const swatch = document.createElement("span");
        swatch.className = "kfm-legend-swatch";
        swatch.style.backgroundColor = item.color || "#ccc";

        const label = document.createElement("span");
        label.className = "kfm-legend-label";
        label.innerText = item.label || "";

        row.appendChild(swatch);
        row.appendChild(label);
        section.appendChild(row);
      });

      body.appendChild(section);
    });
  }

  _toggleCollapse() {
    this._container.classList.toggle("collapsed");
  }
}

