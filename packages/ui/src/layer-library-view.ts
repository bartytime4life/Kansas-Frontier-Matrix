import {
  EMPTY_FILTERS, MAX_WORKSPACE_LAYERS, availability, addStaged, editWorkspace,
  nonvisibility, normalizeWorkspace, projectCatalog, sameWorkspace, selectCards,
  stagePlan, undoEdit, confirmWorkspaceWrite, type CardInput, type CatalogCard, type EditResult,
  type Filters, type Undo, type Workspace,
} from "./layer-library-model.js";

export type LibraryPort = Readonly<{
  read: () => Workspace;
  /** Atomic compare-and-set. A false return preserves externally changed work. */
  write: (next: Workspace, expected: Workspace) => boolean;
  inspect: (id: string) => void;
}>;
export type LibraryContext = Readonly<{
  cards: readonly CardInput[]; areaLabel: string; timeLabel: string;
  /** Optional host-owned order and session restore epoch; neither is persisted here. */
  fixedOrder?: readonly string[]; workspaceEpoch?: number;
}>;
function element<K extends keyof HTMLElementTagNameMap>(tag: K, text?: string, className?: string) {
  const el = document.createElement(tag);
  if (text !== undefined) el.textContent = text;
  if (className) el.className = className;
  return el;
}
function button(label: string, action: () => void, disabled = false) {
  const b = element("button", label); b.type = "button"; b.disabled = disabled;
  b.addEventListener("click", action); return b;
}
function labeledControl(label: string, control: HTMLElement) {
  const node = element("label");
  if (!control.hasAttribute("aria-label")) control.setAttribute("aria-label", label);
  node.append(element("span", label), control); return node;
}
let nextInstance = 0;

/** Browser-native UI. No fetch, renderer, browser location, URL state or persistence.
 * The host map and its camera are deliberately outside this component's capability.
 */
export function mountLayerLibrary(host: HTMLElement, port: LibraryPort, initial: LibraryContext, options: Readonly<{ dialogHost?: HTMLElement }> = {}) {
  const instance = `kfm-library-${++nextInstance}`;
  let context = initial;
  let cards = projectCatalog(initial.cards);
  let filters: Filters = { ...EMPTY_FILTERS };
  let staged = new Set<string>();
  let page = 0; let view: "cards" | "table" = "cards";
  let tab: "library" | "stack" = "library";
  let undo: Undo | null = null;
  let timer: ReturnType<typeof setTimeout> | null = null;
  let queryGeneration = 0; let disposed = false;
  let returnFocus: HTMLElement | null = null;
  let workspaceReadable = true;
  const hostClassAdded = !host.classList.contains("kfm-layer-library");
  host.classList.add("kfm-layer-library");
  const trigger = button("Library", () => open());
  trigger.className = "kfm-library-trigger";
  trigger.setAttribute("aria-haspopup", "dialog");
  trigger.setAttribute("aria-controls", instance);
  const dialog = element("dialog"); dialog.id = instance;
  dialog.className = "kfm-library-dialog";
  dialog.setAttribute("aria-labelledby", `${instance}-title`);
  dialog.setAttribute("aria-describedby", `${instance}-boundary`);
  const heading = element("header", undefined, "kfm-library-heading");
  const headingText = element("div");
  const title = element("h2", "Layer library"); title.id = `${instance}-title`;
  const scope = element("p", "", "kfm-library-scope");
  headingText.append(element("small", "KANSAS FRONTIER MATRIX"), title, scope);
  heading.append(headingText, button("Close", () => cancel()));
  const boundary = element("p", "Fixture previews are not released data. Adding a layer does not authorize delivery.", "kfm-library-boundary");
  boundary.id = `${instance}-boundary`;
  const navigation = element("nav"); navigation.setAttribute("aria-label", "Layer workspace views");
  const libraryTab = button("Discover", () => { tab = "library"; render(); });
  const stackTab = button("On map", () => { tab = "stack"; render(); });
  navigation.append(libraryTab, stackTab);
  const browse = element("section"); browse.setAttribute("aria-label", "Discover layers");
  const toolbar = element("div", undefined, "kfm-library-toolbar");
  const search = element("input"); search.type = "search"; search.maxLength = 200;
  search.placeholder = "Search title, provider, or domain";
  search.addEventListener("input", () => {
    if (timer !== null) clearTimeout(timer);
    const generation = ++queryGeneration;
    const value = search.value;
    timer = setTimeout(() => {
      timer = null;
      if (disposed || generation !== queryGeneration) return;
      filters = { ...filters, query: value }; page = 0; render();
    }, 140);
  });
  toolbar.append(labeledControl("Search layers", search));
  const mode = element("select");
  for (const [value, label] of [["eligible", "Eligible layers"], ["fixtures", "Fixture previews"], ["discovery", "Discovery only"]]) {
    const o = element("option", label); o.value = value; mode.append(o);
  }
  mode.addEventListener("change", () => { filters = { ...filters, mode: mode.value as Filters["mode"] }; page = 0; render(); });
  toolbar.append(labeledControl("Availability", mode));
  const refinements = element("details", undefined, "kfm-library-refinements");
  refinements.append(element("summary", "Refine search: domain, provider, coverage and time"));
  const refineControls = element("div", undefined, "kfm-library-refine-controls");
  refinements.append(refineControls);
  const selectors = new Map<"domain" | "provider" | "representation", HTMLSelectElement>();
  for (const key of ["domain", "provider", "representation"] as const) {
    const select = element("select"); selectors.set(key, select);
    select.addEventListener("change", () => { filters = { ...filters, [key]: select.value }; page = 0; render(); });
    refineControls.append(labeledControl(key[0].toUpperCase() + key.slice(1), select));
  }
  const checkboxes = new Map<"areaOnly" | "timeOnly", HTMLInputElement>();
  for (const [key, label] of [["areaOnly", "Known coverage in selected analysis area"], ["timeOnly", "Matches selected time"]] as const) {
    const checkbox = element("input"); checkbox.type = "checkbox"; checkboxes.set(key, checkbox);
    checkbox.addEventListener("change", () => { filters = { ...filters, [key]: checkbox.checked }; page = 0; render(); });
    refineControls.append(labeledControl(label, checkbox));
  }
  const clear = button("Clear filters", () => clearFilters());
  const switchView = button("Compact table", () => { view = view === "cards" ? "table" : "cards"; render(); });
  toolbar.append(clear, switchView, refinements);
  const chips = element("div", undefined, "kfm-library-chips"); chips.setAttribute("aria-label", "Applied filters");
  const resultsLabel = element("p"); resultsLabel.setAttribute("role", "status");
  const results = element("div", undefined, "kfm-library-results");
  const pager = element("nav"); pager.setAttribute("aria-label", "Catalog pages");
  browse.append(toolbar, chips, resultsLabel, results, pager);
  const stack = element("section"); stack.setAttribute("aria-label", "Requested map layer stack");
  const footer = element("footer", undefined, "kfm-library-footer");
  const selectionCount = element("span");
  const notice = element("p", "", "kfm-library-notice"); notice.setAttribute("role", "status"); notice.setAttribute("aria-live", "polite");
  const add = button("Add to workspace", () => {
    // Current host state and current disclosure projection are read at commit.
    const current = readWorkspace();
    if (current === null) { render(); return; }
    const result = addStaged([...staged], current, cards, context.fixedOrder);
    if (commit(result, current)) staged.clear();
    render();
  });
  const undoButton = button("Undo", () => {
    if (!undo) return;
    const current = readWorkspace();
    if (current === null) { render(); return; }
    commit(undoEdit(undo, current, cards), current);
    undo = null; render();
  }, true);
  footer.append(selectionCount, button("Cancel selection", () => cancel()), undoButton, add);
  dialog.append(heading, boundary, navigation, browse, stack, notice, footer);
  host.append(trigger);
  (options.dialogHost ?? host).append(dialog);

  function readWorkspace(): Workspace | null {
    try {
      const current = port.read();
      normalizeWorkspace(current, cards); // Check bounded shape before using host values.
      workspaceReadable = true;
      return current;
    } catch {
      workspaceReadable = false;
      undo = null;
      notice.textContent = "Workspace unavailable; no successful change is confirmed.";
      return null;
    }
  }
  function currentWorkspace(): Workspace { return normalizeWorkspace(readWorkspace() ?? [], cards); }
  function commit(result: EditResult, expected: Workspace): boolean {
    const confirmation = confirmWorkspaceWrite(port, result.next, expected);
    if (confirmation.outcome !== "APPLIED") {
      notice.textContent = confirmation.notice;
      undo = null; return false;
    }
    if (result.undo) undo = result.undo;
    notice.textContent = result.notice;
    return true;
  }
  function cancel() {
    staged.clear();
    if (timer !== null) clearTimeout(timer);
    timer = null; queryGeneration++;
    // No preview edits ever reached the workspace, so cancel has no inverse side effect.
    filters = { ...filters, query: search.value };
    dialog.close();
    (returnFocus?.isConnected ? returnFocus : trigger).focus({ preventScroll: true });
    render();
  }
  function open() {
    if (disposed || dialog.open) return;
    returnFocus = document.activeElement instanceof HTMLElement ? document.activeElement : trigger;
    staged.clear(); tab = "library"; notice.textContent = "";
    render(); dialog.showModal(); search.focus();
  }
  function clearFilters() {
    if (timer !== null) clearTimeout(timer);
    timer = null; queryGeneration++;
    filters = { ...EMPTY_FILTERS, mode: filters.mode }; search.value = ""; page = 0; render();
  }
  // Keep host shortcuts from opening a competing panel. Tab stays native, but
  // Escape must dismiss even when a populated search field consumes its default.
  dialog.addEventListener("keydown", (event) => {
    event.stopPropagation();
    if (event.key === "Escape") { event.preventDefault(); cancel(); }
  });
  dialog.addEventListener("cancel", (event) => { event.preventDefault(); cancel(); });
  dialog.addEventListener("click", (event) => { if (event.target === dialog) {
    const r = dialog.getBoundingClientRect();
    const mouse = event as MouseEvent;
    if (mouse.clientX < r.left || mouse.clientX > r.right || mouse.clientY < r.top || mouse.clientY > r.bottom) cancel();
  } });

  function selectControl(card: CatalogCard): HTMLInputElement {
    const control = element("input"); control.type = "checkbox";
    control.setAttribute("aria-label", `Select ${card.title}`);
    const present = currentWorkspace().some((item) => item.id === card.id);
    control.disabled = !workspaceReadable || present || availability(card) === "unavailable";
    control.checked = staged.has(card.id); control.dataset.layerId = card.id;
    control.addEventListener("change", () => {
      if (control.checked && staged.size >= MAX_WORKSPACE_LAYERS) {
        control.checked = false; notice.textContent = "Selection limit reached."; return;
      }
      if (control.checked) staged.add(card.id); else staged.delete(card.id);
      renderFooter();
    });
    return control;
  }
  function detail(card: CatalogCard) {
    const details = element("details"); details.append(element("summary", "Details and evidence"));
    const dl = element("dl");
    for (const [label, value] of [
      ["Source", card.sourceId], ["Dataset version", card.datasetVersion], ["Artifact version", card.artifactVersion],
      ["Source time", card.sourceTime], ["Release time", card.releaseTime], ["Units", card.units],
      ["Evidence reference", card.evidenceRef], ["Release", card.release], ["Access", card.access],
      ["Rights", card.rights], ["Generalized", card.generalized ? "Yes" : "No"], ["Limits", card.limitations],
    ]) { dl.append(element("dt", label), element("dd", value || "Unknown / not supplied")); }
    details.append(dl, button("Open feature inspector", () => {
      const current = cards.find((c) => c.id === card.id);
      if (!current || availability(current) === "unavailable") { notice.textContent = "Inspection is unavailable."; return; }
      cancel(); port.inspect(card.id);
    }, availability(card) === "unavailable"));
    return details;
  }
  function renderFooter() {
    const plan = stagePlan([...staged], currentWorkspace(), cards);
    selectionCount.textContent = workspaceReadable
      ? `${staged.size} selected · ${plan.accepted.length} new`
      : `${staged.size} selected · workspace unavailable`;
    add.disabled = !workspaceReadable || plan.accepted.length === 0;
    undoButton.disabled = undo === null;
  }
  function render() {
    if (disposed) return;
    scope.textContent = `${context.areaLabel} · ${context.timeLabel}`;
    libraryTab.setAttribute("aria-pressed", String(tab === "library"));
    stackTab.setAttribute("aria-pressed", String(tab === "stack"));
    browse.hidden = tab !== "library"; stack.hidden = tab !== "stack";
    mode.value = filters.mode;
    for (const [key, checkbox] of checkboxes) checkbox.checked = filters[key];
    for (const [key, select] of selectors) {
      const options = [...new Set(cards.map((c) => c[key]).filter(Boolean))].sort();
      select.replaceChildren(); const all = element("option", `All ${key}s`); all.value = ""; select.append(all);
      for (const value of options) { const o = element("option", value); o.value = value; select.append(o); }
      select.value = filters[key];
    }
    chips.replaceChildren();
    for (const key of ["query", "domain", "provider", "representation", "areaOnly", "timeOnly"] as const) {
      if (!filters[key]) continue;
      chips.append(button(`Remove ${key}: ${filters[key] === true ? "on" : filters[key]}`, () => {
        if (key === "query") { if (timer !== null) clearTimeout(timer); timer = null; queryGeneration++; search.value = ""; }
        filters = { ...filters, [key]: typeof filters[key] === "boolean" ? false : "" }; page = 0; render();
      }));
    }
    const selection = selectCards(cards, filters, page); page = selection.page;
    resultsLabel.textContent = `${selection.total} disclosable matches · page ${page + 1} of ${selection.pages}. Unknown coverage or time is not a match.`;
    switchView.textContent = view === "cards" ? "Compact table" : "Card view";
    results.classList.toggle("kfm-library-card-grid", view === "cards"); results.replaceChildren();
    if (!selection.total) {
      results.append(element("p", filters.mode === "eligible" ? "No eligible released layers are supplied by this host." : "No layers match these filters."));
      if (filters.mode === "eligible") results.append(button("Browse fixture previews", () => { clearFilters(); filters = { ...EMPTY_FILTERS, mode: "fixtures" }; page = 0; render(); }));
    } else if (view === "cards") {
      for (const card of selection.cards) {
        const article = element("article", undefined, "kfm-library-card");
        article.append(element("div", "Preview not supplied", "kfm-library-thumbnail"), labeledControl(card.title, selectControl(card)),
          element("p", `${card.provider} · ${card.domain}`), element("p", card.description),
          element("p", `${card.coverageLabel || "Unknown coverage"} · ${card.timeLabel || "Unknown time"}`),
          element("p", `${card.representation} · ${availability(card)} · ${card.runtime}`), detail(card));
        results.append(article);
      }
    } else {
      const table = element("table"); table.append(element("caption", "Layer metadata — no map payloads"));
      const thead = element("thead"); const labels = element("tr");
      for (const label of ["Select", "Layer / provider", "Coverage / time", "Type / availability", "Details"]) {
        const th = element("th", label); th.scope = "col"; labels.append(th);
      }
      thead.append(labels); const tbody = element("tbody");
      for (const card of selection.cards) {
        const row = element("tr"); const check = element("td"); check.append(selectControl(card));
        const info = element("td"); info.append(detail(card));
        row.append(check, element("td", `${card.title} · ${card.provider}`),
          element("td", `${card.coverageLabel || "Unknown coverage"} · ${card.timeLabel || "Unknown time"}`),
          element("td", `${card.representation} · ${availability(card)}`), info); tbody.append(row);
      }
      table.append(thead, tbody); results.append(table);
    }
    pager.replaceChildren(button("Previous page", () => changePage(-1), page === 0),
      button("Next page", () => changePage(1), page + 1 >= selection.pages));
    renderStack(); renderFooter();
  }
  function changePage(delta: -1 | 1) {
    page += delta; render();
    const preferred = delta === 1 ? "Next page" : "Previous page";
    const buttons = [...pager.querySelectorAll<HTMLButtonElement>("button:not(:disabled)")];
    (buttons.find((b) => b.textContent === preferred) ?? buttons[0] ?? switchView).focus({ preventScroll: true });
  }
  function renderStack() {
    const workspace = currentWorkspace();
    stack.replaceChildren(element("h3", "Requested stack"), element("p", "Top to bottom is requested order, not proof of rendering. Reordering is disabled when renderer groups are unknown. Fit and style edits remain with the host renderer."));
    if (!workspaceReadable) {
      stack.append(element("p", "Requested layers could not be read from the host."));
      return;
    }
    if (!workspace.length) stack.append(element("p", "No layers requested. Use Discover to stage a selection."));
    const list = element("ol");
    workspace.forEach((layer, index) => {
      const card = cards.find((c) => c.id === layer.id)!;
      const row = element("li", undefined, "kfm-library-stack-row");
      row.append(element("h4", card.title), element("p", nonvisibility(card, layer)),
        element("small", `${card.fixture ? "Fixture · " : ""}${card.release} · access ${card.access}${card.generalized ? " · generalized" : ""}`));
      const visible = element("input"); visible.type = "checkbox"; visible.checked = layer.visible;
      visible.addEventListener("change", () => edit({ kind: "visible", id: layer.id, value: visible.checked }));
      const alpha = element("input"); alpha.type = "range"; alpha.min = "0"; alpha.max = "1"; alpha.step = "0.05"; alpha.value = String(layer.opacity);
      alpha.addEventListener("change", () => edit({ kind: "opacity", id: layer.id, value: Number(alpha.value) }));
      row.append(labeledControl(`Enable ${card.title}`, visible), labeledControl(`Opacity ${card.title}`, alpha));
      for (const direction of [-1, 1] as const) {
        const neighbor = workspace[index + direction];
        const group = neighbor && cards.find((c) => c.id === neighbor.id)?.renderGroup;
        const move = button(direction === -1 ? "Move up" : "Move down", () => edit({ kind: "move", id: layer.id, direction }),
          !card.renderGroup || !group || card.renderGroup !== group);
        move.setAttribute("aria-label", `${move.textContent}: ${card.title}`); row.append(move);
      }
      row.append(button(`Remove ${card.title}`, () => edit({ kind: "remove", id: layer.id })), detail(card)); list.append(row);
    });
    stack.append(list);
  }
  function edit(edit: Parameters<typeof editWorkspace>[2]) {
    const active = document.activeElement;
    const label = active?.getAttribute("aria-label") ?? active?.closest("label")?.textContent;
    const textContent = active?.textContent;
    const current = readWorkspace();
    if (current === null) { render(); return; }
    commit(editWorkspace(current, cards, edit), current); render();
    const controls = [...stack.querySelectorAll<HTMLElement>("button,input")];
    (controls.find((el) => label ? (el.getAttribute("aria-label") ?? el.closest("label")?.textContent) === label
      : el.textContent === textContent) ?? stackTab).focus({ preventScroll: true });
  }
  render();
  return Object.freeze({
    open,
    update(next: LibraryContext) {
      if (disposed) return;
      if (next.workspaceEpoch !== context.workspaceEpoch) {
        undo = null; staged.clear();
        notice.textContent = "Workspace restored; staged changes and undo cleared.";
      }
      // Project before replacing: invalid/oversized responses fail closed instead of retaining stale cards.
      try { cards = projectCatalog(next.cards); context = next; }
      catch { cards = []; context = { ...next, cards: [] }; notice.textContent = "Catalog unavailable. No previous metadata is retained."; }
      // A withdrawn metadata value must not survive in an old filter chip.
      for (const key of ["domain", "provider", "representation"] as const) {
        if (filters[key] && !cards.some((card) => card[key] === filters[key])) {
          filters = { ...filters, [key]: "" };
        }
      }
      const allowed = new Set(cards.filter((c) => availability(c) !== "unavailable").map((c) => c.id));
      const removed = [...staged].filter((id) => !allowed.has(id)).length;
      staged = new Set([...staged].filter((id) => allowed.has(id)));
      if (removed) notice.textContent = "Some staged selections are no longer available. No identifiers are disclosed.";
      const previous = readWorkspace();
      const safe = normalizeWorkspace(previous ?? [], cards);
      if (previous !== null && !sameWorkspace(previous, safe)) {
        const confirmation = confirmWorkspaceWrite(port, safe, previous);
        if (confirmation.outcome !== "APPLIED") {
          undo = null;
          notice.textContent = confirmation.notice;
        }
      }
      render();
    },
    destroy() {
      if (disposed) return;
      disposed = true; queryGeneration++;
      if (timer !== null) clearTimeout(timer);
      timer = null; staged.clear(); undo = null;
      const wasOpen = dialog.open;
      dialog.close(); dialog.remove(); trigger.remove();
      if (hostClassAdded) host.classList.remove("kfm-layer-library");
      if (wasOpen && returnFocus?.isConnected) returnFocus.focus({ preventScroll: true });
    },
  });
}
