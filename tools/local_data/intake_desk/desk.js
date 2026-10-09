// KFM Intake Desk — same-origin client for tools/local_data/intake_service.py.
// All data is rendered with textContent / DOM APIs; nothing from the store is parsed as HTML.
"use strict";

const TOKEN = document.querySelector('meta[name="kfm-session"]').content;
const PAGE = 50;
const VIEW = { lon0: -102.6, lon1: -94.0, lat0: 36.55, lat1: 40.45, w: 800, h: 420 };
// Approximate Kansas outline (WGS84); the north-east edge follows the Missouri River coarsely.
const KANSAS = [[-102.0517, 40.0031], [-95.3083, 40.0], [-95.08, 39.87], [-94.95, 39.90], [-94.88, 39.77], [-95.0, 39.68],
  [-94.95, 39.56], [-94.82, 39.48], [-94.89, 39.40], [-94.71, 39.28], [-94.6077, 39.16], [-94.6077, 36.9986], [-102.0417, 36.9930]];
const TIER_LABELS = { local_store: "Local PC store", database: "Intake database", work_lane: "WORK review lane", git_repo: "Git repository", github_release: "GitHub release" };
const ACTION_LABELS = { keep: "Bytes stay here", index: "Indexed", stage: "Stage review copy", capture_first: "Capture into quarantine first", hold: "On hold",
  metadata_card: "Metadata card eligible", candidate: "Release candidate", bundle: "Bundle with its collection", deny: "Not for GitHub" };
const HOLD_TEXT = {
  RIGHTS_UNKNOWN: "Redistribution rights are unknown. Capture the file with manage.py and declare rights.",
  RIGHTS_RESTRICTED: "Rights restrict redistribution; keep local only.", RIGHTS_DENIED: "Rights deny redistribution; keep local only.",
  SENSITIVITY_UNKNOWN: "Sensitivity has not been declared.", SENSITIVITY_RESTRICTED: "Restricted sensitivity; keep local only.",
  SENSITIVITY_CONTROLLED: "Controlled sensitivity; keep local only.", REVIEW_FLAGS: "Names or content suggest sensitive material; review before sharing.",
  DOMAIN_UNRESOLVED: "No domain could be inferred; declare one when capturing.", FORMAT_UNRECOGNIZED: "The file format was not recognized.",
  CAPTURE_REQUIRED: "This inbox file is not in the store yet.", OUTSIDE_KANSAS: "The extent lies outside Kansas.",
  GITHUB_BUDGET_EXCEEDED: "It would not fit in the remaining GitHub data budget.",
};

const $ = (id) => document.getElementById(id);
const state = { offset: 0, total: 0, bbox: null, selected: null, items: [], timer: null, running: false };

function el(tag, attrs = {}, ...children) {
  const node = document.createElement(tag);
  for (const [key, value] of Object.entries(attrs)) {
    if (key === "class") node.className = value;
    else if (key === "text") node.textContent = value;
    else if (key.startsWith("on")) node.addEventListener(key.slice(2), value);
    else node.setAttribute(key, value);
  }
  for (const child of children) if (child != null) node.append(child);
  return node;
}
function svg(tag, attrs = {}) {
  const node = document.createElementNS("http://www.w3.org/2000/svg", tag);
  for (const [key, value] of Object.entries(attrs)) node.setAttribute(key, value);
  return node;
}
function bytes(n) {
  if (n == null) return "–";
  for (const [unit, size] of [["TB", 1e12], ["GB", 1e9], ["MB", 1e6], ["kB", 1e3]]) if (n >= size) return `${(n / size).toFixed(n >= 10 * size ? 1 : 2)} ${unit}`;
  return `${n} B`;
}
function toast(message) {
  const node = $("toast");
  node.textContent = message;
  node.hidden = false;
  clearTimeout(toast.timer);
  toast.timer = setTimeout(() => { node.hidden = true; }, 5000);
}
async function api(path, body) {
  const options = body === undefined ? { cache: "no-store" }
    : { method: "POST", cache: "no-store", headers: { "Content-Type": "application/json", "X-KFM-Session": TOKEN }, body: JSON.stringify(body) };
  const response = await fetch(path, options);
  const value = await response.json().catch(() => ({ error: "INVALID_RESPONSE" }));
  if (!response.ok) throw new Error(value.error || `HTTP_${response.status}`);
  return value;
}
const project = ([lon, lat]) => [((lon - VIEW.lon0) / (VIEW.lon1 - VIEW.lon0)) * VIEW.w, ((VIEW.lat1 - lat) / (VIEW.lat1 - VIEW.lat0)) * VIEW.h];
const unproject = (x, y) => [VIEW.lon0 + (x / VIEW.w) * (VIEW.lon1 - VIEW.lon0), VIEW.lat1 - (y / VIEW.h) * (VIEW.lat1 - VIEW.lat0)];

// --- summary and budget ----------------------------------------------------

function renderOverview(o) {
  $("sum-files").textContent = o.files.toLocaleString();
  $("sum-bytes").textContent = bytes(o.bytes);
  for (const status of ["ready", "review", "blocked"]) $(`sum-${status}`).textContent = (o.by_status[status]?.files ?? 0).toLocaleString();
  const b = o.budget;
  const level = $("budget-level");
  level.textContent = b.level === "ok" ? "within budget" : b.level === "warn" ? "nearing ceiling" : "over ceiling";
  level.className = `chip ${b.level}`;
  const segments = [
    ["Committed (repo + releases)", b.committed_bytes, "var(--committed)"],
    ["Planned release candidates", b.planned_bytes, "var(--planned)"],
    ["Free for new data", b.available_for_new_data_bytes, "var(--free)"],
    ["Reserved for code & interface", b.reserved_for_code_and_interface_bytes, "var(--reserve)"],
  ];
  const gauge = $("gauge");
  const legend = $("gauge-legend");
  gauge.replaceChildren();
  legend.replaceChildren();
  for (const [label, value, color] of segments) {
    const span = el("span", { title: `${label}: ${bytes(value)}` });
    span.style.width = `${Math.max(0, (value / b.github_limit_bytes) * 100)}%`;
    span.style.background = color;
    gauge.append(span);
    const swatch = el("i");
    swatch.style.background = color;
    legend.append(el("li", {}, swatch, `${label} ${bytes(value)}`));
  }
  gauge.setAttribute("aria-label", `GitHub storage: ${bytes(b.committed_bytes)} committed of ${bytes(b.github_limit_bytes)}; ${bytes(b.available_for_new_data_bytes)} free for data`);
  fillSelect($("f-family"), Object.keys(o.by_family), "Any format");
  fillSelect($("f-domain"), Object.keys(o.by_domain).filter((d) => d !== "None"), "Any domain");
}
function fillSelect(select, values, blank) {
  const current = select.value;
  select.replaceChildren(el("option", { value: "", text: blank }), ...values.sort().map((v) => el("option", { value: v, text: v })));
  select.value = values.includes(current) ? current : "";
}

// --- job -------------------------------------------------------------------

function renderJob(status) {
  const job = status.job;
  state.running = job.state === "running";
  $("analyze").disabled = state.running;
  $("cancel").hidden = !state.running;
  $("include-inbox").disabled = !status.inboxConfigured;
  $("include-inbox").parentElement.title = status.inboxConfigured ? "" : "Start the service with --inbox to analyze downloads";
  const counts = `${job.discovered} found · ${job.analyzed} analyzed · ${job.reused} unchanged${job.failed ? ` · ${job.failed} failed` : ""}`;
  $("job").textContent = state.running ? `Analyzing… ${counts}` : job.state === "idle" ? "" : `Last run ${job.state}: ${counts}${job.error ? ` (${job.error})` : ""}`;
}
async function poll() {
  try {
    const status = await api("/api/status");
    const wasRunning = state.running;
    renderJob(status);
    if (wasRunning && !state.running) await refresh();
    clearTimeout(state.timer);
    state.timer = setTimeout(poll, state.running ? 1000 : 10000);
  } catch (error) {
    $("job").textContent = `Service unavailable (${error.message})`;
    state.timer = setTimeout(poll, 5000);
  }
}

// --- list and map -----------------------------------------------------------

function query(extra = {}) {
  const params = new URLSearchParams();
  for (const [key, id] of [["text", "f-text"], ["status", "f-status"], ["lane", "f-lane"], ["family", "f-family"], ["domain", "f-domain"]]) {
    const value = $(id).value.trim();
    if (value) params.set(key, value);
  }
  if (state.bbox) params.set("bbox", state.bbox.map((v) => v.toFixed(4)).join(","));
  for (const [key, value] of Object.entries(extra)) params.set(key, String(value));
  return params.toString();
}
async function loadItems() {
  const listing = await api(`/api/items?${query({ limit: PAGE, offset: state.offset })}`);
  state.items = listing.items;
  state.total = listing.total;
  const rows = $("rows");
  rows.replaceChildren();
  if (!listing.items.length) rows.append(el("tr", {}, el("td", { colspan: "7", class: "muted", text: "No files match. Run an analysis or change the filters." })));
  for (const item of listing.items) {
    const name = item.name;
    const time = item.time_start ? (item.time_start === item.time_end ? item.time_start : `${item.time_start} → ${item.time_end}`) : "–";
    const row = el("tr", { tabindex: "0", "data-id": item.id, onclick: () => openItem(item.id), onkeydown: (e) => { if (e.key === "Enter") openItem(item.id); } },
      el("td", {}, el("span", { class: "path", title: item.relative_path, text: name }), el("span", { class: "sub", text: item.declared_label || `${item.lane} · ${item.relative_path}` })),
      el("td", { text: item.kind }), el("td", { text: item.domain || "–" }), el("td", { text: item.kansas }), el("td", { class: "time", text: time }),
      el("td", { class: "num", text: bytes(item.size_bytes) }), el("td", {}, el("span", { class: `chip ${item.status}`, text: item.status })));
    if (item.id === state.selected) row.classList.add("selected");
    rows.append(row);
  }
  const last = Math.min(state.offset + PAGE, state.total);
  $("page").textContent = state.total ? `${state.offset + 1}–${last} of ${state.total.toLocaleString()}` : "";
  $("prev").disabled = state.offset === 0;
  $("next").disabled = last >= state.total;
}
async function loadMap() {
  const collection = await api(`/api/extents?${query()}`);
  const map = $("map");
  map.replaceChildren();
  for (let lon = -102; lon <= -94; lon += 2) {
    const [x] = project([lon, 0]);
    map.append(svg("line", { class: "grid", x1: x, x2: x, y1: 0, y2: VIEW.h }));
    const label = svg("text", { class: "gridlabel", x: x + 3, y: VIEW.h - 4 });
    label.textContent = `${-lon}°W`;
    map.append(label);
  }
  for (let lat = 37; lat <= 40; lat += 1) {
    const [, y] = project([0, lat]);
    map.append(svg("line", { class: "grid", x1: 0, x2: VIEW.w, y1: y, y2: y }));
    const label = svg("text", { class: "gridlabel", x: 3, y: y - 3 });
    label.textContent = `${lat}°N`;
    map.append(label);
  }
  map.append(svg("polygon", { class: "state", points: KANSAS.map((p) => project(p).join(",")).join(" ") }));
  const features = [...collection.features].sort((a, b) => area(b) - area(a));
  for (const feature of features) {
    const p = feature.properties;
    const cls = `ext ${p.status}${p.id === state.selected ? " selected" : ""}`;
    let shape;
    if (feature.geometry.type === "Point") {
      const [x, y] = project(feature.geometry.coordinates);
      shape = svg("circle", { class: `${cls} pt`, cx: x, cy: y, r: 5 });
    } else {
      const ring = feature.geometry.coordinates[0];
      const [x0, y1] = project(ring[0]);
      const [x1, y0] = project(ring[2]);
      shape = svg("rect", { class: cls, x: x0, y: y0, width: Math.max(2, x1 - x0), height: Math.max(2, y1 - y0) });
    }
    const title = svg("title");
    title.textContent = `${p.label} · ${p.kind} · ${p.status}`;
    shape.append(title);
    shape.dataset.id = p.id;
    map.append(shape);
  }
  if (state.bbox) {
    const [x0, y0] = project([state.bbox[0], state.bbox[3]]);
    const [x1, y1] = project([state.bbox[2], state.bbox[1]]);
    map.append(svg("rect", { class: "brush", x: x0, y: y0, width: x1 - x0, height: y1 - y0 }));
  }
}
const area = (f) => (f.geometry.type === "Point" ? 0 : Math.abs((f.geometry.coordinates[0][2][0] - f.geometry.coordinates[0][0][0]) * (f.geometry.coordinates[0][2][1] - f.geometry.coordinates[0][0][1])));

function setupBrush() {
  const map = $("map");
  let start = null;
  let brush = null;
  const point = (event) => {
    const box = map.getBoundingClientRect();
    return [((event.clientX - box.left) / box.width) * VIEW.w, ((event.clientY - box.top) / box.height) * VIEW.h];
  };
  map.addEventListener("pointerdown", (event) => {
    start = point(event);
    start.target = event.target;
    brush = svg("rect", { class: "brush", x: start[0], y: start[1], width: 0, height: 0 });
    map.append(brush);
    map.setPointerCapture(event.pointerId);
  });
  map.addEventListener("pointermove", (event) => {
    if (!start) return;
    const [x, y] = point(event);
    brush.setAttribute("x", Math.min(x, start[0]));
    brush.setAttribute("y", Math.min(y, start[1]));
    brush.setAttribute("width", Math.abs(x - start[0]));
    brush.setAttribute("height", Math.abs(y - start[1]));
  });
  map.addEventListener("pointerup", (event) => {
    if (!start) return;
    const end = point(event);
    const moved = Math.abs(end[0] - start[0]) > 6 && Math.abs(end[1] - start[1]) > 6;
    brush.remove();
    if (moved) {
      const [lonA, latA] = unproject(Math.min(start[0], end[0]), Math.max(start[1], end[1]));
      const [lonB, latB] = unproject(Math.max(start[0], end[0]), Math.min(start[1], end[1]));
      state.bbox = [lonA, latA, lonB, latB].map((v, i) => Math.max(i % 2 ? -90 : -180, Math.min(i % 2 ? 90 : 180, v)));
      $("clear-area").hidden = false;
      state.offset = 0;
      reload();
    } else if (start.target.dataset && start.target.dataset.id) openItem(start.target.dataset.id);
    start = null;
  });
}

// --- details -----------------------------------------------------------------

function kv(pairs) {
  const list = el("dl", { class: "kv" });
  for (const [key, value] of pairs) if (value != null && value !== "") list.append(el("dt", { text: key }), el("dd", { text: String(value) }));
  return list;
}
async function openItem(id) {
  state.selected = id;
  let item;
  try { item = await api(`/api/items/${id}`); } catch (error) { toast(`Could not load item: ${error.message}`); return; }
  const p = item.profile;
  const d = item.decision;
  const s = p.spatial;
  const t = p.temporal || {};
  $("d-title").textContent = (item.declared?.relative_path || item.relative_path).split("/").pop();
  const body = $("d-body");
  body.replaceChildren();
  body.append(el("p", {}, el("span", { class: `chip ${d.status}`, text: d.status }), " ", el("span", { class: "muted", text: `${item.lane} · ${bytes(item.size_bytes)}` })));
  if (d.holds.length) {
    body.append(el("h3", { text: "What needs attention" }));
    const holds = el("ul");
    for (const hold of d.holds) holds.append(el("li", { text: HOLD_TEXT[hold] || hold }));
    body.append(holds);
  }
  body.append(el("h3", { text: "Where it goes" }));
  const placements = el("ul", { class: "placements" });
  for (const placement of d.placements) {
    const button = placement.tier === "work_lane" && placement.action === "stage" ? applyButton(id, "stage", "Stage copy")
      : placement.tier === "git_repo" && placement.action === "metadata_card" ? applyButton(id, "card", "Write card") : el("span", { class: "muted", text: ACTION_LABELS[placement.action] || placement.action });
    const why = [placement.reason, placement.target || placement.path, placement.bytes != null ? bytes(placement.bytes) : null, placement.asset_parts > 1 ? `${placement.asset_parts} release parts` : null].filter(Boolean).join(" · ");
    placements.append(el("li", {}, el("span", { class: "tier", text: TIER_LABELS[placement.tier] || placement.tier }), button, el("span", { class: "why", text: why })));
  }
  body.append(placements);
  body.append(el("h3", { text: "What is in it" }), kv([
    ["Format", `${p.format.kind} (${p.format.family})`], ["Media type", p.format.media_type], ["CRS", s.crs], ["Extent (WGS84)", s.bbox_wgs84?.map((v) => v.toFixed(4)).join(", ")],
    ["Kansas", s.kansas], ["Geometry", Object.keys(s.geometry_types || {}).join(", ")], ["Rows", p.structure.rows], ["Features", p.structure.features], ["Points", p.structure.points],
    ["Raster", p.structure.width ? `${p.structure.width} × ${p.structure.height} px, ${p.structure.bands ?? 1} band(s)` : null], ["Pages", p.structure.pages],
    ["Members", p.structure.members], ["Fields", (p.structure.fields || []).slice(0, 20).join(", ")],
  ]));
  body.append(el("h3", { text: "Time (kept separate)" }), kv([
    ["Content coverage", t.content_start ? `${t.content_start} → ${t.content_end}` : "not found in content"], ["From fields", (t.time_fields || []).join(", ")],
    ["File metadata", t.file_metadata_time], ["Path year hint", t.path_year_hint?.join("–")], ["Profiled", p.profiled_at],
  ]));
  if (item.declared) {
    body.append(el("h3", { text: "Declared at capture" }), kv([
      ["Source", item.declared.source_id], ["Dataset", item.declared.dataset_id], ["Version", item.declared.version], ["Domain", item.declared.domain],
      ["Source URI", item.declared.source_uri], ["License", item.declared.rights?.license_id], ["Redistribution", item.declared.rights?.redistribution],
      ["Sensitivity", item.declared.sensitivity], ["Captured", item.declared.captured_at],
    ]));
  }
  if (p.issues.length || d.review_flags.length) {
    body.append(el("h3", { text: "Analysis notes" }));
    const notes = el("div", { class: "holds" });
    for (const note of [...d.review_flags, ...p.issues]) notes.append(el("span", { class: "hold", text: note }));
    body.append(notes);
  }
  if (item.applications.length) {
    body.append(el("h3", { text: "Applied" }));
    const applied = el("ul");
    for (const a of item.applications) applied.append(el("li", { text: `${a.applied_at} · ${a.action} → ${a.target}` }));
    body.append(applied);
  }
  body.append(el("details", {}, el("summary", { text: "Full record (JSON)" }), el("pre", { text: JSON.stringify(item, null, 2) })));
  $("drawer").hidden = false;
  for (const row of document.querySelectorAll("#rows tr")) row.classList.toggle("selected", row.dataset.id === id);
  loadMap().catch(() => {});
}
function applyButton(id, action, label) {
  return el("button", { type: "button", class: "primary", text: label, onclick: async (event) => {
    event.target.disabled = true;
    try {
      const result = await api("/api/apply", { id, action });
      toast(result.outcome === "APPLIED" ? `Done: ${result.target}` : `${result.outcome}: ${result.target}`);
      await openItem(id);
    } catch (error) {
      toast(`Not applied: ${error.message}`);
      event.target.disabled = false;
    }
  } });
}

// --- release plan -------------------------------------------------------------

async function loadPlan() {
  const plan = await api("/api/release-plan");
  const host = $("plan");
  host.replaceChildren();
  const after = plan.budget_after_plan;
  host.append(el("p", { class: "muted", text: `${plan.selected.length} candidate file(s), ${bytes(plan.selected_bytes)}. Free for data after this plan: ${bytes(after.available_for_new_data_bytes)} of the ${bytes(after.data_ceiling_bytes)} data ceiling; ${bytes(after.reserved_for_code_and_interface_bytes)} stays reserved for code and interface work.` }));
  if (!plan.selected.length && !plan.deferred.length) {
    host.append(el("p", { class: "muted", text: "Only files with allowed redistribution, public sensitivity and no review flags become candidates. Everything else stays on this PC." }));
    return;
  }
  const table = el("table", {}, el("thead", {}, el("tr", {}, ...["File", "Domain", "Parts", "Size", "SHA-256"].map((h) => el("th", { text: h })))));
  const tbody = el("tbody");
  for (const row of plan.selected) tbody.append(el("tr", { onclick: () => openItem(row.id) }, el("td", { text: row.relative_path }), el("td", { text: row.domain || "–" }),
    el("td", { text: String(row.asset_parts) }), el("td", { class: "num", text: bytes(row.bytes) }), el("td", { text: row.sha256.slice(0, 16) + "…" })));
  for (const row of plan.deferred) tbody.append(el("tr", { onclick: () => openItem(row.id) }, el("td", { text: row.id }), el("td", { text: "deferred" }), el("td", { text: "–" }),
    el("td", { class: "num", text: bytes(row.bytes) }), el("td", { text: row.reason })));
  table.append(tbody);
  host.append(table);
}

// --- wiring ---------------------------------------------------------------------

async function reload() {
  try { await Promise.all([loadItems(), loadMap()]); } catch (error) { toast(`Could not load files: ${error.message}`); }
}
async function refresh() {
  try { renderOverview(await api("/api/overview")); } catch (error) { toast(`Could not load summary: ${error.message}`); }
  await reload();
  loadPlan().catch((error) => toast(`Could not load plan: ${error.message}`));
}
let debounce;
$("filters").addEventListener("input", () => { clearTimeout(debounce); debounce = setTimeout(() => { state.offset = 0; reload(); }, 250); });
$("filters").addEventListener("submit", (event) => event.preventDefault());
$("prev").addEventListener("click", () => { state.offset = Math.max(0, state.offset - PAGE); loadItems(); });
$("next").addEventListener("click", () => { state.offset += PAGE; loadItems(); });
$("clear-area").addEventListener("click", () => { state.bbox = null; $("clear-area").hidden = true; state.offset = 0; reload(); });
$("d-close").addEventListener("click", () => { $("drawer").hidden = true; state.selected = null; reload(); });
document.addEventListener("keydown", (event) => { if (event.key === "Escape" && !$("drawer").hidden) $("d-close").click(); });
$("analyze").addEventListener("click", async () => {
  try {
    await api("/api/analyze", { includeInbox: $("include-inbox").checked });
    state.running = true;
    poll();
  } catch (error) { toast(`Analysis not started: ${error.message}`); }
});
$("cancel").addEventListener("click", () => api("/api/cancel", {}).catch((error) => toast(error.message)));
setupBrush();
refresh();
poll();
