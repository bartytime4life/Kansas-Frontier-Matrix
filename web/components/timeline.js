// web/components/timeline.js
// Kansas-Frontier-Matrix — Timeline / Year Slider Component
// ---------------------------------------------------------
// Lightweight, framework-free time control with:
//  - Min/Max range, current value, and step
//  - Label with tabular-nums, keyboard nudging, wheel support
//  - Optional play/pause (auto-advance) and step ± buttons
//  - Emits change events via onChange(cb)
//  - Dock mode (uses .kfm-timeline-dock CSS if you mount without a container)
//
// Example:
//
// import Timeline from "./components/timeline.js";
//
// const tl = new Timeline({
//   min: 1700, max: 2100, value: 1900, step: 1,
//   autoplay: false, fps: 12, loop: true,
//   formatLabel: (y) => String(y)
// }).mount(document.getElementById("timebox"));
//
// tl.onChange((y) => KFM.setYear(y));
//
// // Update programmatically:
// tl.setValue(1936);
//
// // Change range:
// tl.setRange(1800, 2025).setValue(1900);

export default class Timeline {
  /**
   * @param {Object} opts
   * @param {number} [opts.min=1700]
   * @param {number} [opts.max=2100]
   * @param {number} [opts.value=1900]
   * @param {number} [opts.step=1]
   * @param {boolean} [opts.autoplay=false]
   * @param {number} [opts.fps=8] - frames/steps per second when playing
   * @param {boolean} [opts.loop=true]
   * @param {Function} [opts.formatLabel] - (val) => string
   * @param {boolean} [opts.showControls=true] - show play/prev/next controls
   * @param {string} [opts.label="Year:"] - label prefix
   */
  constructor(opts = {}) {
    this.min = Number.isFinite(opts.min) ? +opts.min : 1700;
    this.max = Number.isFinite(opts.max) ? +opts.max : 2100;
    this.step = Number.isFinite(opts.step) ? +opts.step : 1;
    this.value = this._clamp(Number.isFinite(opts.value) ? +opts.value : this.min);
    this.autoplay = !!opts.autoplay;
    this.fps = Number.isFinite(opts.fps) ? +opts.fps : 8;
    this.loop = opts.loop !== false;
    this.formatLabel = typeof opts.formatLabel === "function" ? opts.formatLabel : (y) => String(y);
    this.showControls = opts.showControls !== false;
    this.labelText = opts.label ?? "Year:";

    this._root = null;
    this._label = null;
    this._slider = null;
    this._btnPlay = null;
    this._raf = null;
    this._lastTick = 0;
    this._subscribers = new Set();
  }

  // ---------------------------------------------------------------------------
  // Mount & DOM
  // ---------------------------------------------------------------------------
  mount(container) {
    // If no container is provided, create a dock in the map using CSS hooks
    if (!container) {
      const dock = document.createElement("div");
      dock.className = "kfm-timeline-dock";
      document.body.appendChild(dock);
      container = dock;
    }

    // Skeleton
    this._root = Timeline.el("div", {}, [
      Timeline.el("div", { class: "kfm-timeline-label" }, [this.labelText]),
      Timeline.el("div", { style: { display: "grid", gridTemplateColumns: this.showControls ? "auto 1fr auto" : "1fr", gap: "8px", alignItems: "center" } }, [
        this.showControls ? this._controlsLeft() : "",
        this._sliderBlock(),
        this.showControls ? this._controlsRight() : ""
      ])
    ]);

    container.appendChild(this._root);

    // Kick off autoplay if requested
    if (this.autoplay) this.play();

    return this;
  }

  _controlsLeft() {
    const wrap = Timeline.el("div", { style: { display: "flex", gap: "6px", alignItems: "center" } });
    const btnPrev = Timeline.btn("⟨", "Step backward", () => this.stepBy(-this.step));
    this._btnPlay = Timeline.btn("▶", "Play", () => this.toggle());
    wrap.appendChild(btnPrev);
    wrap.appendChild(this._btnPlay);
    return wrap;
  }

  _controlsRight() {
    const wrap = Timeline.el("div", { style: { display: "flex", gap: "6px", alignItems: "center", justifyContent: "flex-end" } });
    const btnNext = Timeline.btn("⟩", "Step forward", () => this.stepBy(+this.step));
    wrap.appendChild(btnNext);
    return wrap;
  }

  _sliderBlock() {
    const block = Timeline.el("div", {});
    const row = Timeline.el("div", { style: { display: "flex", alignItems: "center", gap: "8px", marginBottom: "6px" } }, [
      Timeline.el("strong", { style: { fontSize: "13px" } }, ["Year:"]),
      (this._label = Timeline.el("span", { style: { fontVariantNumeric: "tabular-nums" } }, [this.formatLabel(this.value)]))
    ]);

    this._slider = Timeline.el("input", {
      type: "range",
      min: String(this.min),
      max: String(this.max),
      step: String(this.step),
      value: String(this.value),
      style: { width: "100%" },
      oninput: (e) => {
        const v = this._clamp(+e.target.value);
        this._updateLabel(v);
        this._emit(v);
      }
    });

    // Keyboard nudging (while focused)
    this._slider.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft" || e.key === "ArrowDown") this.stepBy(-this.step, true);
      if (e.key === "ArrowRight" || e.key === "ArrowUp") this.stepBy(+this.step, true);
    });

    // Mouse wheel adjusts value
    this._slider.addEventListener("wheel", (e) => {
      e.preventDefault();
      const delta = e.deltaY > 0 ? this.step : -this.step;
      this.stepBy(delta, true);
    }, { passive: false });

    block.append(row, this._slider);
    return block;
  }

  // ---------------------------------------------------------------------------
  // Playback (requestAnimationFrame-driven)
  // ---------------------------------------------------------------------------
  play() {
    if (this._raf) return this;
    this._lastTick = performance.now();
    this._tick = this._tick.bind(this);
    this._raf = requestAnimationFrame(this._tick);
    this._setPlayLabel(true);
    return this;
  }

  pause() {
    if (!this._raf) return this;
    cancelAnimationFrame(this._raf);
    this._raf = null;
    this._setPlayLabel(false);
    return this;
  }

  toggle() {
    return this._raf ? this.pause() : this.play();
  }

  _tick(now) {
    const interval = 1000 / Math.max(1, this.fps);
    if (now - this._lastTick >= interval) {
      this._lastTick = now;
      // Advance value by +step; clamp/loop if needed
      let next = this.value + this.step;
      if (next > this.max) next = this.loop ? this.min : this.max;
      this._setValueInternal(next, true);
    }
    this._raf = requestAnimationFrame(this._tick);
  }

  _setPlayLabel(playing) {
    if (!this._btnPlay) return;
    this._btnPlay.textContent = playing ? "⏸" : "▶";
    this._btnPlay.title = playing ? "Pause" : "Play";
  }

  // ---------------------------------------------------------------------------
  // Public API
  // ---------------------------------------------------------------------------
  onChange(cb) {
    if (typeof cb === "function") this._subscribers.add(cb);
    return this;
  }

  offChange(cb) {
    this._subscribers.delete(cb);
    return this;
  }

  setRange(min, max) {
    const lo = Number.isFinite(min) ? +min : this.min;
    const hi = Number.isFinite(max) ? +max : this.max;
    this.min = Math.min(lo, hi);
    this.max = Math.max(lo, hi);
    if (this._slider) {
      this._slider.min = String(this.min);
      this._slider.max = String(this.max);
    }
    // Re-clamp current value
    this.setValue(this.value);
    return this;
  }

  setStep(step) {
    this.step = Number.isFinite(step) ? +step : this.step;
    if (this._slider) this._slider.step = String(this.step);
    return this;
  }

  setValue(v) {
    this._setValueInternal(v, false);
    return this;
  }

  stepBy(delta, fromInteraction = false) {
    const v = this._clamp(this.value + (Number.isFinite(delta) ? +delta : this.step));
    this._setValueInternal(v, fromInteraction);
    return this;
  }

  destroy() {
    this.pause();
    if (this._root?.parentNode) this._root.parentNode.removeChild(this._root);
    this._root = this._label = this._slider = this._btnPlay = null;
    this._subscribers.clear();
  }

  // ---------------------------------------------------------------------------
  // Internals
  // ---------------------------------------------------------------------------
  _setValueInternal(v, fromInteraction) {
    const clamped = this._clamp(v);
    if (clamped === this.value && fromInteraction) {
      // still notify on UI interactions, to keep external state in sync
      this._emit(clamped);
      return;
    }
    this.value = clamped;
    if (this._slider) this._slider.value = String(clamped);
    this._updateLabel(clamped);
    this._emit(clamped);
  }

  _emit(v) {
    for (const cb of this._subscribers) {
      try { cb(v); } catch (err) { console.error("Timeline onChange error:", err); }
    }
  }

  _updateLabel(v) {
    if (this._label) this._label.textContent = this.formatLabel(v);
  }

  _clamp(v) {
    const num = Number.isFinite(v) ? +v : this.min;
    return Math.max(this.min, Math.min(this.max, num));
  }

  // ---------------------------------------------------------------------------
  // Static helpers
  // ---------------------------------------------------------------------------
  static el(tag, attrs = {}, children = []) {
    const n = document.createElement(tag);
    for (const [k, v] of Object.entries(attrs)) {
      if (k === "class") n.className = v;
      else if (k === "style") Object.assign(n.style, v);
      else if (k.startsWith("on") && typeof v === "function") n.addEventListener(k.slice(2), v);
      else if (v != null) n.setAttribute(k, String(v));
    }
    const arr = Array.isArray(children) ? children : [children];
    for (const c of arr) {
      if (c == null || c === "") continue;
      n.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    }
    return n;
  }

  static btn(text, title, onClick) {
    const b = document.createElement("button");
    b.type = "button";
    b.textContent = text;
    b.title = title;
    b.className = "kfm-btn"; // optional hook; styled by global or map.css if desired
    b.style.padding = "4px 8px";
    b.style.border = "1px solid var(--kfm-border, #d1d5db)";
    b.style.borderRadius = "6px";
    b.style.background = "var(--kfm-bg, #fff)";
    b.style.color = "var(--kfm-fg, #111827)";
    b.style.cursor = "pointer";
    b.addEventListener("click", onClick);
    b.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") { e.preventDefault(); onClick(e); }
    });
    return b;
  }
}

