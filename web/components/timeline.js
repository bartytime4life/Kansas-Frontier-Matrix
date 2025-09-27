// web/components/timeline.js
// Kansas-Frontier-Matrix — Timeline / Year Slider Component (refined)
// -------------------------------------------------------------------
// Backward compatible. Improvements:
// - A11y: aria-valuemin/max/now + optional aria-valuetext formatter
// - Ticks: datalist-based tick marks (opts.showTicks / opts.ticks / opts.tickInterval)
// - Methods: focus(), isPlaying(), setDisabled(bool), setBounds(min,max,value?)
// - Safer autoplay (matchMedia guard), safer CustomEvent poly, cleanup
// - Wheel/keyboard polish; prevents flooding; respects reduced motion
//
// Usage:
//   import Timeline from "./components/timeline.js";
//   const tl = new Timeline({ min: 1800, max: 2025, value: 1900, step: 1, showControls: true })
//       .mount("#timebox")
//       .onChange(y => KFM.setYear(y));
//
//   tl.addEventListener("change", e => console.log(e.detail.value));
//   tl.setOptions({ fps: 12, loop: true, showTicks: true, tickInterval: 25 });

export default class Timeline extends EventTarget {
  /**
   * @param {Object} opts
   * @param {number}   [opts.min=1700]
   * @param {number}   [opts.max=2100]
   * @param {number}   [opts.value=1900]
   * @param {number}   [opts.step=1]
   * @param {boolean}  [opts.autoplay=false]
   * @param {number}   [opts.fps=8]                 1..60
   * @param {boolean}  [opts.loop=true]
   * @param {Function} [opts.formatLabel]           (val:number) => string
   * @param {Function} [opts.formatValueText]       (val:number) => string (for aria-valuetext)
   * @param {boolean}  [opts.showControls=true]
   * @param {string}   [opts.label="Year:"]
   * @param {string}   [opts.ariaLabel]             for the whole group
   * @param {boolean}  [opts.showTicks=false]
   * @param {number[]} [opts.ticks]                 explicit tick values
   * @param {number}   [opts.tickInterval]          e.g., 10 → ticks every 10
   * @param {boolean}  [opts.disabled=false]
   */
  constructor(opts = {}) {
    super();

    this.min = Number.isFinite(opts.min) ? +opts.min : 1700;
    this.max = Number.isFinite(opts.max) ? +opts.max : 2100;
    this.step = Number.isFinite(opts.step) ? +opts.step : 1;
    this.value = this._clamp(Number.isFinite(opts.value) ? +opts.value : this.min);

    const prefersReduce = (() => {
      try { return typeof matchMedia === "function" && !!matchMedia("(prefers-reduced-motion: reduce)")?.matches; }
      catch { return false; }
    })();

    this.autoplay = !!opts.autoplay && !prefersReduce;
    this.fps = this._clampFps(Number.isFinite(opts.fps) ? +opts.fps : 8);
    this.loop = opts.loop !== false;
    this.formatLabel = typeof opts.formatLabel === "function" ? opts.formatLabel : (y) => String(y);
    this.formatValueText = typeof opts.formatValueText === "function" ? opts.formatValueText : null;
    this.showControls = opts.showControls !== false;
    this.labelText = opts.label ?? "Year:";
    this.ariaLabel = opts.ariaLabel ?? "Timeline year slider";
    this.showTicks = !!opts.showTicks;
    this.ticks = Array.isArray(opts.ticks) ? opts.ticks.slice() : null;
    this.tickInterval = Number.isFinite(opts.tickInterval) ? Math.max(1, +opts.tickInterval) : null;
    this.disabled = !!opts.disabled;

    this._root = null;
    this._label = null;
    this._slider = null;
    this._btnPlay = null;
    this._datalistId = `kfm-ticks-${Math.random().toString(36).slice(2, 8)}`;
    this._raf = null;
    this._accum = 0;
    this._lastTs = 0;
    this._subscribers = new Set();
    this._wheelPending = false;

    this._bound = {
      tick: (ts) => this._tick(ts),
      keydown: (e) => this._onKeydown(e),
      wheel: (e) => this._onWheel(e),
      visibility: () => this._onVisibility(),
    };

    // CustomEvent poly for very old browsers (kept minimal)
    this._CustomEvent = typeof CustomEvent === "function"
      ? CustomEvent
      : function (type, params) {
          const evt = document.createEvent("CustomEvent");
          evt.initCustomEvent(type, true, true, params?.detail ?? null);
          return evt;
        };
  }

  // ---------------------------------------------------------------------------
  // Mount & DOM
  // ---------------------------------------------------------------------------
  mount(container) {
    if (typeof container === "string") container = document.querySelector(container);
    if (!container) {
      const dock = document.createElement("div");
      dock.className = "kfm-timeline-dock";
      document.body.appendChild(dock);
      container = dock;
    }

    this._root = Timeline.el("div", {
      class: "kfm-timeline",
      role: "group",
      "aria-label": this.ariaLabel,
      style: { display: "grid", gap: "8px", userSelect: "none" }
    });

    // Label row
    const labelRow = Timeline.el("div", {
      class: "kfm-timeline-row kfm-timeline-label",
      style: { display: "flex", alignItems: "center", gap: "8px" }
    }, [
      Timeline.el("strong", { style: { fontSize: "13px" } }, [this.labelText]),
      (this._label = Timeline.el("span", {
        style: { fontVariantNumeric: "tabular-nums" },
        "aria-live": "polite",
        "aria-atomic": "true"
      }, [this.formatLabel(this.value)]))
    ]);

    // Slider row
    const row = Timeline.el("div", {
      class: "kfm-timeline-row",
      style: {
        display: "grid",
        gridTemplateColumns: this.showControls ? "auto 1fr auto" : "1fr",
        gap: "8px",
        alignItems: "center"
      }
    }, [
      this.showControls ? this._controlsLeft() : "",
      this._sliderBlock(),
      this.showControls ? this._controlsRight() : ""
    ]);

    this._root.append(labelRow, row);
    container.appendChild(this._root);

    document.addEventListener("visibilitychange", this._bound.visibility);

    if (this.autoplay) this.play();
    if (this.disabled) this.setDisabled(true);

    return this;
  }

  _controlsLeft() {
    const wrap = Timeline.el("div", { style: { display: "flex", gap: "6px", alignItems: "center" } });
    const btnPrev = Timeline.btn("⟨", "Step backward", () => this.stepBy(-this.step));
    this._btnPlay = Timeline.btn("▶", "Play", () => this.toggle());
    wrap.append(btnPrev, this._btnPlay);
    return wrap;
  }

  _controlsRight() {
    const wrap = Timeline.el("div", { style: { display: "flex", gap: "6px", alignItems: "center", justifyContent: "flex-end" } });
    const btnNext = Timeline.btn("⟩", "Step forward", () => this.stepBy(+this.step));
    wrap.append(btnNext);
    return wrap;
  }

  _buildTicksIfNeeded() {
    if (!this.showTicks && !this.ticks && !this.tickInterval) return null;

    const ticks = [];
    if (Array.isArray(this.ticks) && this.ticks.length) {
      for (const v of this.ticks) {
        const n = Math.round(+v);
        if (Number.isFinite(n) && n >= this.min && n <= this.max) ticks.push(n);
      }
    } else if (Number.isFinite(this.tickInterval)) {
      const start = Math.ceil(this.min / this.tickInterval) * this.tickInterval;
      for (let v = start; v <= this.max; v += this.tickInterval) ticks.push(v);
    } else if (this.showTicks) {
      // default heuristics: ~8-12 ticks
      const span = this.max - this.min;
      const approx = Math.max(1, Math.round(span / 10));
      const step = Math.max(this.step, approx);
      for (let v = this.min; v <= this.max; v += step) ticks.push(Math.round(v));
    }

    if (!ticks.length) return null;

    const list = document.createElement("datalist");
    list.id = this._datalistId;
    for (const v of ticks) {
      const opt = document.createElement("option");
      opt.value = String(v);
      list.appendChild(opt);
    }
    return list;
  }

  _sliderBlock() {
    const block = Timeline.el("div", { style: { display: "grid", gap: "6px" } });

    const datalist = this._buildTicksIfNeeded();
    if (datalist) block.appendChild(datalist);

    this._slider = Timeline.el("input", {
      type: "range",
      min: String(this.min),
      max: String(this.max),
      step: String(this.step),
      value: String(this.value),
      style: { width: "100%" },
      "aria-label": this.ariaLabel,
      "aria-valuemin": String(this.min),
      "aria-valuemax": String(this.max),
      "aria-valuenow": String(this.value),
      ...(datalist ? { list: this._datalistId } : {}),
      oninput: (e) => {
        const v = this._clamp(+e.target.value);
        this._updateLabel(v);
        this._emit(v, /*fromInteraction*/true);
      }
    });

    // Keyboard: fine + coarse
    this._slider.addEventListener("keydown", this._bound.keydown, { passive: false });

    // Wheel: modifier-aware, debounced by frame (only when hovering the slider)
    this._slider.addEventListener("wheel", this._bound.wheel, { passive: false });

    block.append(this._slider);
    return block;
  }

  // ---------------------------------------------------------------------------
  // Playback (requestAnimationFrame-driven; drift-free)
  // ---------------------------------------------------------------------------
  play() {
    if (this._raf || this.disabled) return this;
    this._lastTs = 0;
    this._accum = 0;
    this._raf = requestAnimationFrame(this._bound.tick);
    this._setPlayLabel(true);
    this._dispatch("play", { value: this.value });
    return this;
  }

  pause() {
    if (!this._raf) return this;
    cancelAnimationFrame(this._raf);
    this._raf = null;
    this._setPlayLabel(false);
    this._dispatch("pause", { value: this.value });
    return this;
  }

  toggle() {
    return this._raf ? this.pause() : this.play();
  }

  isPlaying() {
    return !!this._raf;
  }

  _tick(ts) {
    if (!this._lastTs) this._lastTs = ts;
    const dt = ts - this._lastTs;
    this._lastTs = ts;

    const interval = 1000 / Math.max(1, this.fps);
    this._accum += dt;
    while (this._accum >= interval) {
      this._accum -= interval;
      let next = this.value + this.step;
      if (next > this.max) next = this.loop ? this.min : this.max;
      this._setValueInternal(next, /*fromInteraction*/false);
      if (!this._raf) return; // paused in callback
      if (!this.loop && this.value === this.max) this.pause();
    }

    this._raf = requestAnimationFrame(this._bound.tick);
  }

  _setPlayLabel(playing) {
    if (!this._btnPlay) return;
    this._btnPlay.textContent = playing ? "⏸" : "▶";
    this._btnPlay.title = playing ? "Pause" : "Play";
    this._btnPlay.setAttribute("aria-pressed", String(playing));
  }

  // ---------------------------------------------------------------------------
  // Public API
  // ---------------------------------------------------------------------------
  onChange(cb) { if (typeof cb === "function") this._subscribers.add(cb); return this; }
  offChange(cb) { this._subscribers.delete(cb); return this; }

  setRange(min, max) { return this.setBounds(min, max); }
  setBounds(min, max, value) {
    const lo = Number.isFinite(min) ? +min : this.min;
    const hi = Number.isFinite(max) ? +max : this.max;
    const newMin = Math.min(lo, hi);
    const newMax = Math.max(lo, hi);
    if (newMin === this.min && newMax === this.max && value === undefined) return this;
    this.min = newMin;
    this.max = newMax;
    if (this._slider) {
      this._slider.min = String(this.min);
      this._slider.max = String(this.max);
      this._slider.setAttribute("aria-valuemin", String(this.min));
      this._slider.setAttribute("aria-valuemax", String(this.max));
    }
    this.setValue(value !== undefined ? value : this.value); // re-clamp
    this._dispatch("rangechange", { min: this.min, max: this.max });
    return this;
  }

  setStep(step) {
    if (Number.isFinite(step) && step > 0) {
      this.step = +step;
      if (this._slider) this._slider.step = String(this.step);
    }
    return this;
  }

  setValue(v) { this._setValueInternal(v, false); return this; }

  stepBy(delta) {
    const v = this._clamp(this.value + (Number.isFinite(delta) ? +delta : this.step));
    this._setValueInternal(v, true);
    return this;
  }

  setOptions(opts = {}) {
    if ("min" in opts || "max" in opts) this.setBounds(opts.min ?? this.min, opts.max ?? this.max, opts.value);
    if ("step" in opts) this.setStep(opts.step);
    if ("fps" in opts) this.fps = this._clampFps(+opts.fps);
    if ("loop" in opts) this.loop = !!opts.loop;
    if ("autoplay" in opts) this.autoplay = !!opts.autoplay;
    if ("formatLabel" in opts && typeof opts.formatLabel === "function") {
      this.formatLabel = opts.formatLabel; this._updateLabel(this.value);
    }
    if ("formatValueText" in opts && typeof opts.formatValueText === "function") {
      this.formatValueText = opts.formatValueText; this._updateAriaNow(this.value);
    }
    if ("label" in opts) this.setLabel(opts.label);
    if ("ariaLabel" in opts) {
      this.ariaLabel = String(opts.ariaLabel);
      if (this._root) this._root.setAttribute("aria-label", this.ariaLabel);
      if (this._slider) this._slider.setAttribute("aria-label", this.ariaLabel);
    }
    if ("showTicks" in opts || "ticks" in opts || "tickInterval" in opts) {
      this.showTicks = !!opts.showTicks;
      this.ticks = Array.isArray(opts.ticks) ? opts.ticks.slice() : this.ticks;
      this.tickInterval = Number.isFinite(opts.tickInterval) ? Math.max(1, +opts.tickInterval) : this.tickInterval;
      // Rebuild slider block for ticks — cheap since it's tiny
      if (this._slider?.parentNode) {
        const parent = this._slider.parentNode;
        parent.replaceWith(this._sliderBlock());
      }
    }
    if ("disabled" in opts) this.setDisabled(!!opts.disabled);
    if ("value" in opts) this.setValue(opts.value);
    return this;
  }

  setLabel(text) {
    this.labelText = String(text ?? "");
    const strong = this._root?.querySelector(".kfm-timeline-label strong");
    if (strong) strong.textContent = this.labelText;
    return this;
  }

  setDisabled(disabled) {
    this.disabled = !!disabled;
    if (this.disabled && this._raf) this.pause();
    if (this._slider) this._slider.disabled = this.disabled;
    if (this._btnPlay) this._btnPlay.disabled = this.disabled;
    return this;
  }

  focus() { this._slider?.focus(); return this; }

  getState() {
    return { min: this.min, max: this.max, value: this.value, step: this.step, playing: !!this._raf, fps: this.fps, loop: this.loop, disabled: this.disabled };
  }

  destroy() {
    this.pause();
    document.removeEventListener("visibilitychange", this._bound.visibility);
    if (this._slider) {
      this._slider.removeEventListener("keydown", this._bound.keydown);
      this._slider.removeEventListener("wheel", this._bound.wheel);
    }
    if (this._root?.parentNode) this._root.parentNode.removeChild(this._root);
    this._root = this._label = this._slider = this._btnPlay = null;
    this._subscribers.clear();
  }

  // ---------------------------------------------------------------------------
  // Internals
  // ---------------------------------------------------------------------------
  _setValueInternal(v, fromInteraction) {
    const clamped = this._clamp(v);
    const changed = clamped !== this.value;
    this.value = clamped;

    if (this._slider) {
      if (this._slider.value !== String(clamped)) this._slider.value = String(clamped);
      this._slider.setAttribute("aria-valuenow", String(clamped));
      this._updateAriaNow(clamped);
    }

    this._updateLabel(clamped);
    if (changed || fromInteraction) {
      for (const cb of this._subscribers) {
        try { cb(clamped); } catch (err) { console.error("Timeline onChange error:", err); }
      }
      this._dispatch("change", { value: clamped, user: !!fromInteraction });
    }
  }

  _emit(v, fromInteraction = false) { this._setValueInternal(v, fromInteraction); }

  _updateLabel(v) { if (this._label) this._label.textContent = this.formatLabel(v); }

  _updateAriaNow(v) {
    if (this._slider && this.formatValueText) {
      try { this._slider.setAttribute("aria-valuetext", String(this.formatValueText(v))); }
      catch {}
    }
  }

  _clamp(v) { const num = Number.isFinite(v) ? +v : this.min; return Math.max(this.min, Math.min(this.max, num)); }
  _clampFps(v) { const n = Number.isFinite(v) ? v : 8; return Math.max(1, Math.min(60, Math.round(n))); }

  _onKeydown(e) {
    const key = e.key;
    const big = Math.max(this.step, Math.ceil((this.max - this.min) / 20)); // coarse step ~5%
    if (["ArrowLeft","ArrowDown","ArrowRight","ArrowUp","PageUp","PageDown","Home","End"].includes(key)) e.preventDefault();
    switch (key) {
      case "ArrowLeft":
      case "ArrowDown": this.stepBy(-this.step); break;
      case "ArrowRight":
      case "ArrowUp":   this.stepBy(+this.step); break;
      case "PageDown":  this.stepBy(-big); break;
      case "PageUp":    this.stepBy(+big); break;
      case "Home":      this.setValue(this.min); break;
      case "End":       this.setValue(this.max); break;
    }
  }

  _onWheel(e) {
    // Only react when the pointer is on the slider (listener is on slider), prevent page scroll
    e.preventDefault();
    if (this._wheelPending || this.disabled) return;
    this._wheelPending = true;
    const dir = e.deltaY > 0 ? +1 : -1;
    const modifier = e.ctrlKey || e.metaKey ? 5 : (e.altKey ? 0.25 : 1);
    const raw = this.step * modifier;
    const delta = dir * (modifier >= 1 ? Math.max(1, Math.round(raw)) : Math.max(this.step * 0.25, raw));
    requestAnimationFrame(() => {
      this.stepBy(delta);
      this._wheelPending = false;
    });
  }

  _onVisibility() { if (document.hidden && this._raf) this.pause(); }

  _dispatch(type, detail) {
    const evt = new this._CustomEvent(type, { detail });
    if (this._root) this._root.dispatchEvent(evt);
    // also bubble on instance for addEventListener on Timeline itself
    this.dispatchEvent(new this._CustomEvent(type, { detail }));
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
    b.className = "kfm-btn";
    b.style.padding = "4px 8px";
    b.style.border = "1px solid var(--kfm-border, #d1d5db)";
    b.style.borderRadius = "6px";
    b.style.background = "var(--kfm-bg, #fff)";
    b.style.color = "var(--kfm-fg, #111827)";
    b.style.cursor = "pointer";
    b.addEventListener("click", onClick);
    b.addEventListener("keydown", (e) => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); onClick(e); } });
    return b;
  }
}
