// web/components/legend-control.js
// Minimal MapLibre legend control with a live Year badge.
// Exposes window.LegendControl for app.js optional wiring.

(function (global) {
  class LegendControl {
    constructor(opts = {}) {
      this._container = null;
      this._pos = opts.position || "top-right";
      this._title = opts.title || "Legend";
      this._year = opts.year ?? null;
    }

    onAdd(map) {
      this._map = map;
      const root = document.createElement("div");
      root.className = "kfm-legend maplibregl-ctrl";
      root.setAttribute("role", "region");
      root.setAttribute("aria-label", this._title);

      const header = document.createElement("div");
      header.className = "kfm-legend-header";
      header.textContent = this._title;

      const year = document.createElement("div");
      year.className = "kfm-legend-year";
      year.title = "Current timeline year";

      const badge = document.createElement("span");
      badge.className = "kfm-year-badge";
      badge.textContent = this._year == null ? "—" : String(this._year);
      year.append("Year: ", badge);

      const body = document.createElement("div");
      body.className = "kfm-legend-body";
      // (Optional) You can inject swatches/rows later into body.

      root.append(header, year, body);
      this._container = root;
      this._badge = badge;
      return root;
    }

    onRemove() {
      if (this._container?.parentNode) this._container.parentNode.removeChild(this._container);
      this._container = this._badge = this._map = null;
    }

    getDefaultPosition() {
      return this._pos;
    }

    setYear(y) {
      this._year = y;
      if (this._badge) this._badge.textContent = y == null ? "—" : String(y);
    }
  }

  // Helper to wire a Timeline instance to this control
  function wireTimelineToLegend(timeline, legendControl) {
    if (!timeline || !legendControl) return () => {};
    // Initial sync
    legendControl.setYear(timeline.getState().value);
    // Live updates (DOM events or callback)
    const onDom = (e) => legendControl.setYear(e.detail?.value ?? timeline.getState().value);
    const cb = (y) => legendControl.setYear(y);
    timeline.addEventListener?.("change", onDom);
    timeline.onChange?.(cb);
    return () => {
      timeline.removeEventListener?.("change", onDom);
      timeline.offChange?.(cb);
    };
  }

  global.LegendControl = LegendControl;
  global.wireTimelineToLegend = wireTimelineToLegend;
})(window);
