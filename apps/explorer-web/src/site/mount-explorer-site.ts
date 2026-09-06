import {
  createNullMapRuntime,
  type MapRuntimeTrustState,
} from "@kfm/maplibre";
import { resolveBaselineShell } from "../features/shell";
import {
  MAP_FEATURE_SELECTION_PROFILE,
  mountMapFeatureEvidenceFixture,
  mountMapRuntimeTrustStatus,
  type MapEvidenceFixtureCase,
  type MapEvidenceFixtureController,
  type MapRuntimeTrustStatusController,
} from "../features/map_runtime";
import {
  CURRENT_MAPLIBRE_READINESS,
  FEATURE_CATALOG,
  KNOWLEDGE_DOMAINS,
  KNOWLEDGE_PRINCIPLES,
  REPOSITORY_SNAPSHOT,
  filterFeatures,
  findDomain,
  repositoryUrl,
  type FeatureArea,
  type FeatureEntry,
  type FeatureMaturity,
  type KnowledgeDomain,
} from "./catalog";

export type ExplorerSiteController = Readonly<{ destroy: () => void }>;

export const SUPPORTED_SYNTHETIC_STREAMFLOW_EVIDENCE_REFS = Object.freeze([
  "kfm:evidence:synthetic:flow-001",
]);
export const SUPPORTED_SYNTHETIC_STREAMFLOW_HISTORY_EVIDENCE_REFS =
  Object.freeze(["kfm:evidence:synthetic:flow-000"]);

export const SUPPORTED_SYNTHETIC_STREAMFLOW_PROJECTION = Object.freeze({
  profile: "kfm.explorer.evidence-drawer.public-safe.v1",
  id: "kfm:ui:evidence-drawer:answer-001",
  outcome: "ANSWER",
  reason_code: "SUPPORTED",
  title: "Synthetic streamflow observation",
  summary: "A synthetic, generalized flow observation is supported by the cited fixture evidence.",
  evidence_refs: Object.freeze(["kfm:evidence:synthetic:flow-001"]),
  citations: Object.freeze([
    Object.freeze({
      label: "Synthetic fixture evidence",
      href: `https://github.com/${REPOSITORY_SNAPSHOT.repository}/blob/${REPOSITORY_SNAPSHOT.commit}/fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json`,
    }),
  ]),
  limitations: Object.freeze(["Fixture-only demonstration; not a live observation or life-safety instruction."]),
  trust_state: Object.freeze({
    source_role: "official",
    policy: "ALLOW",
    review: "REVIEWED",
    release: "RELEASED",
    freshness: "CURRENT",
    correction: "CORRECTED",
  }),
  history: Object.freeze({
    negative_outcomes: Object.freeze([
      Object.freeze({
        evidence_ref: "kfm:evidence:synthetic:flow-000",
        state: "SUPERSEDED",
        reason_code: "SUPERSEDED_EVIDENCE",
        recorded_at: "2026-08-01T00:00:00Z",
        visible_in_runtime: true,
        resolvable_as_current: false,
      }),
    ]),
    corrections: Object.freeze([
      Object.freeze({
        prior_evidence_ref: "kfm:evidence:synthetic:flow-000",
        active_evidence_ref: "kfm:evidence:synthetic:flow-001",
        status: "ACTIVE_CORRECTION",
        recorded_at: "2026-08-01T00:00:00Z",
      }),
    ]),
  }),
});

const restrictedProjection = Object.freeze({
  profile: "kfm.explorer.evidence-drawer.public-safe.v1",
  id: "kfm:ui:evidence-drawer:deny-sensitive-001",
  outcome: "DENY",
  reason_code: "SENSITIVE_DETAIL_RESTRICTED",
  title: "Restricted map detail",
  summary: "The requested detail is restricted by policy.",
  evidence_refs: Object.freeze([]),
  citations: Object.freeze([]),
  limitations: Object.freeze(["Protected spatial detail is not exposed."]),
  trust_state: Object.freeze({
    source_role: "context",
    policy: "DENY",
    review: "PENDING",
    release: "UNRELEASED",
    freshness: "UNKNOWN",
    correction: "NONE",
  }),
  history: Object.freeze({ negative_outcomes: Object.freeze([]), corrections: Object.freeze([]) }),
});

const mapCases: readonly MapEvidenceFixtureCase[] = Object.freeze([
  { caseId: "supported", label: "Supported synthetic streamflow", selection: { profile: MAP_FEATURE_SELECTION_PROFILE, selection_id: "selection:flow-001", layer_id: "layer:synthetic-streamflow", feature_id: "feature:flow-001", evidence_refs: SUPPORTED_SYNTHETIC_STREAMFLOW_EVIDENCE_REFS, history_evidence_refs: SUPPORTED_SYNTHETIC_STREAMFLOW_HISTORY_EVIDENCE_REFS } },
  { caseId: "missing", label: "Feature without governed evidence", selection: { profile: MAP_FEATURE_SELECTION_PROFILE, selection_id: "selection:missing", layer_id: "layer:synthetic-streamflow", feature_id: "feature:missing", evidence_refs: [] } },
  { caseId: "restricted", label: "Policy-restricted feature", selection: { profile: MAP_FEATURE_SELECTION_PROFILE, selection_id: "selection:restricted", layer_id: "layer:synthetic-restricted", feature_id: "feature:restricted", evidence_refs: ["kfm:evidence:synthetic:restricted"] } },
  { caseId: "mismatch", label: "Mismatched evidence scope", selection: { profile: MAP_FEATURE_SELECTION_PROFILE, selection_id: "selection:mismatch", layer_id: "layer:synthetic-streamflow", feature_id: "feature:mismatch", evidence_refs: ["kfm:evidence:synthetic:other"] } },
  { caseId: "error", label: "Governed resolver error", selection: { profile: MAP_FEATURE_SELECTION_PROFILE, selection_id: "selection:error", layer_id: "layer:synthetic-streamflow", feature_id: "feature:error", evidence_refs: ["kfm:evidence:synthetic:flow-001"] } },
]);

function el<K extends keyof HTMLElementTagNameMap>(document: Document, tag: K, className?: string): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className) node.className = className;
  return node;
}
function text<K extends keyof HTMLElementTagNameMap>(document: Document, tag: K, value: string, className?: string): HTMLElementTagNameMap[K] {
  const node = el(document, tag, className);
  node.textContent = value;
  return node;
}
function link(document: Document, label: string, href: string, className?: string): HTMLAnchorElement {
  const node = el(document, "a", className);
  node.textContent = label;
  node.href = href;
  if (href.startsWith("https://")) {
    node.target = "_blank";
    node.rel = "noreferrer";
  }
  return node;
}
function chip(document: Document, label: string, value: string, tone = "neutral"): HTMLElement {
  const node = el(document, "span", `chip chip--${tone}`);
  node.append(text(document, "span", `${label}: `, "sr-only"), document.createTextNode(value));
  return node;
}
function heading(document: Document, eyebrow: string, title: string, summary: string): HTMLElement {
  const wrap = el(document, "header", "section-heading");
  wrap.append(text(document, "p", eyebrow, "eyebrow"), text(document, "h2", title), text(document, "p", summary, "section-summary"));
  return wrap;
}
function option(document: Document, select: HTMLSelectElement, value: string, label: string): void {
  const node = el(document, "option");
  node.value = value;
  node.textContent = label;
  select.append(node);
}

const SVG_NAMESPACE = "http://www.w3.org/2000/svg";

function svgElement(
  document: Document,
  tagName: string,
  attributes: Readonly<Record<string, string>> = {},
): SVGElement {
  const node = document.createElementNS(SVG_NAMESPACE, tagName);
  for (const [name, value] of Object.entries(attributes)) {
    node.setAttribute(name, value);
  }
  return node;
}

function svgText(
  document: Document,
  value: string,
  attributes: Readonly<Record<string, string>> = {},
): SVGElement {
  const node = svgElement(document, "text", attributes);
  node.textContent = value;
  return node;
}

function mapArtwork(document: Document): HTMLElement {
  const figure = el(document, "figure", "map-artwork");
  figure.setAttribute(
    "aria-label",
    "Illustrative Kansas map stage; decorative geometry is not factual map data.",
  );

  const svg = svgElement(document, "svg", {
    viewBox: "0 0 760 410",
    role: "img",
    "aria-labelledby": "map-art-title map-art-desc",
  });
  const title = svgElement(document, "title", { id: "map-art-title" });
  title.textContent = "Illustrative Kansas evidence map";
  const description = svgElement(document, "desc", { id: "map-art-desc" });
  description.textContent =
    "A decorative Kansas outline with survey grid, river paths, and evidence markers.";

  const defs = svgElement(document, "defs");
  const pattern = svgElement(document, "pattern", {
    id: "grid",
    width: "34",
    height: "34",
    patternUnits: "userSpaceOnUse",
  });
  pattern.append(
    svgElement(document, "path", {
      d: "M34 0H0V34",
      fill: "none",
      stroke: "currentColor",
      opacity: ".13",
    }),
  );
  defs.append(pattern);

  const mapShape = svgElement(document, "path", {
    class: "map-shape",
    d: "M96 75 650 80 666 304 115 327 88 154Z",
  });
  const mapGrid = svgElement(document, "path", {
    class: "map-grid",
    d: "M96 75 650 80 666 304 115 327 88 154Z",
  });
  const river = svgElement(document, "path", {
    class: "river",
    d: "M112 216C210 170 250 250 355 205S530 146 646 229",
  });
  const minorRiver = svgElement(document, "path", {
    class: "river river--minor",
    d: "M220 92c56 42 40 90 94 120s91 57 126 106",
  });

  const marker = svgElement(document, "g", { class: "marker" });
  marker.append(
    svgElement(document, "circle", { cx: "355", cy: "205", r: "20" }),
    svgElement(document, "circle", { cx: "355", cy: "205", r: "6" }),
  );
  const secondaryMarker = svgElement(document, "g", {
    class: "marker marker--secondary",
  });
  secondaryMarker.append(
    svgElement(document, "circle", { cx: "526", cy: "171", r: "14" }),
    svgElement(document, "circle", { cx: "526", cy: "171", r: "5" }),
  );

  svg.append(
    defs,
    title,
    description,
    mapShape,
    mapGrid,
    river,
    minorRiver,
    marker,
    secondaryMarker,
    svgText(document, "SYNTHETIC MAP STAGE", { x: "120", y: "120" }),
    svgText(document, "Rendered features scope requests — not claims", {
      x: "120",
      y: "145",
    }),
  );
  figure.append(svg);
  return figure;
}
function domainDetail(document: Document, domain: KnowledgeDomain): HTMLElement {
  const article = el(document, "article", "domain-detail card");
  article.id = `domain-${domain.id}`;
  const title = text(document, "h3", domain.name);
  title.tabIndex = -1;
  article.append(
    text(document, "p", "Knowledge domain", "eyebrow"),
    title,
    text(document, "p", domain.summary),
    text(document, "p", domain.safeguard, "guardrail"),
    link(document, "Inspect repository boundary", repositoryUrl(domain.path), "text-link"),
  );
  return article;
}

function featureCard(document: Document, entry: FeatureEntry): HTMLElement {
  const article = el(document, "article", "feature-card card");
  article.append(
    el(document, "div", "feature-card__meta"),
    text(document, "h3", entry.name),
    text(document, "p", entry.summary),
    link(document, "Open source boundary", repositoryUrl(entry.path), "text-link"),
  );
  article.firstElementChild?.append(chip(document, "Area", entry.area), chip(document, "Maturity", entry.maturity, entry.maturity === "HOLD" ? "critical" : "neutral"));
  return article;
}

export function mountExplorerSite(root: HTMLElement): ExplorerSiteController {
  const document = root.ownerDocument;
  const baseline = resolveBaselineShell();
  const cleanup: Array<() => void> = [];
  const mapRuntime = createNullMapRuntime();
  let mapFixture: MapEvidenceFixtureController | null = null;
  let mapRuntimeStatus: MapRuntimeTrustStatusController | null = null;
  root.className = "kfm-explorer-root";
  document.documentElement.dataset.kfmExplorer = "true";

  const skip = link(document, "Skip to Explorer content", "#explorer-main", "skip-link");
  const header = el(document, "header", "site-header");
  const headerInner = el(document, "div", "site-header__inner");
  const brand = el(document, "a", "brand");
  brand.href = "#top";
  brand.append(text(document, "span", "KFM", "brand__mark"), text(document, "span", "Kansas Frontier Matrix", "brand__name"));
  const nav = el(document, "nav", "site-nav");
  nav.setAttribute("aria-label", "Explorer sections");
  [["Map", "#map"], ["Knowledge", "#knowledge"], ["Features", "#features"], ["Trust", "#trust"]].forEach(([label, href]) => nav.append(link(document, label, href)));
  const headerState = el(document, "div", "header-state");
  headerState.append(chip(document, "Shell", baseline.outcome, "caution"), chip(document, "Renderer", "HOLD", "critical"));
  headerInner.append(brand, nav, headerState);
  header.append(headerInner);

  const main = el(document, "main", "site-main");
  main.id = "explorer-main";
  const hero = el(document, "section", "hero section-shell");
  hero.id = "top";
  const heroCopy = el(document, "div", "hero__copy");
  const title = text(document, "h1", "Explore Kansas knowledge without losing the evidence");
  title.id = "explorer-title";
  heroCopy.append(
    text(document, "p", "Kansas-first · map-first · time-aware · evidence-first", "eyebrow"),
    title,
    text(document, "p", "KFM connects place, time, sources, policy, review, release, correction, and rollback in one trust-visible browser shell.", "hero__summary"),
    el(document, "div", "hero__actions"),
  );
  heroCopy.lastElementChild?.append(link(document, "Open map workspace", "#map", "button button--primary"), link(document, "Browse all features", "#features", "button button--secondary"));
  const posture = el(document, "aside", "posture card");
  posture.setAttribute("aria-label", "Current Explorer posture");
  posture.append(text(document, "p", "Current composed posture", "eyebrow"), text(document, "p", `${baseline.outcome} / ${baseline.code}`, "posture__outcome"), text(document, "p", baseline.message), text(document, "p", "Repository-grounded synthetic proof. No live KFM data, source activation, model runtime, renderer admission, release, or publication.", "guardrail"));
  hero.append(heroCopy, posture);
  main.append(hero);

  const mapSection = el(document, "section", "section-shell");
  mapSection.id = "map";
  mapSection.append(heading(document, "Map workspace", "A governed map starts with the evidence boundary", "The stage is renderer-neutral. Its controls exercise the existing strict selection-to-Evidence-Drawer bridge without importing MapLibre."));
  const mapGrid = el(document, "div", "map-grid");
  const mapCard = el(document, "div", "map-card card");
  const mapToolbar = el(document, "div", "map-toolbar");
  mapToolbar.append(chip(document, "Interaction", "Synthetic"), chip(document, "Evidence bridge", "Active", "positive"), chip(document, "MapLibre", "HOLD", "critical"));
  mapCard.append(mapToolbar, mapArtwork(document));
  const runtime = el(document, "aside", "runtime-card card");
  const runtimeStatusHost = el(document, "div", "runtime-status-host");
  runtimeStatusHost.dataset.component = "explorer-map-runtime-status-host";
  const runtimeControls = el(document, "div", "runtime-controls");
  runtimeControls.setAttribute("aria-label", "Synthetic map runtime controls");
  const runtimeActions: readonly Readonly<{
    label: string;
    state: MapRuntimeTrustState | null;
  }>[] = Object.freeze([
    Object.freeze({ label: "Initialize or recover synthetic runtime", state: null }),
    Object.freeze({ label: "Mark synthetic runtime stale", state: "STALE" }),
    Object.freeze({ label: "Withdraw synthetic runtime", state: "WITHDRAWN" }),
    Object.freeze({ label: "Mark synthetic runtime error", state: "ERROR" }),
  ]);
  runtimeActions.forEach((action) => {
    const button = el(document, "button");
    button.type = "button";
    button.textContent = action.label;
    const handleRuntimeAction = (): void => {
      if (action.state === null) {
        void mapRuntime.initialize();
        return;
      }
      mapRuntime.emitTrustState(action.state);
    };
    button.addEventListener("click", handleRuntimeAction);
    cleanup.push(() => button.removeEventListener("click", handleRuntimeAction));
    runtimeControls.append(button);
  });
  runtime.append(
    text(document, "p", "Renderer gate", "eyebrow"),
    text(document, "h3", "MapLibre integration remains governed"),
    text(document, "p", "The package-owned adapter is present, but Explorer activation, dependency review, and authenticated browser probes remain separate gates."),
    chip(document, "Candidate", CURRENT_MAPLIBRE_READINESS.readinessCandidate),
    chip(document, "Package", "Present"),
    chip(document, "Browser evidence", "Pending", "critical"),
    text(document, "p", "This workspace still exercises the dependency-free NullMapRuntime and finite renderer-neutral status contract. READY does not establish MapLibre readiness, release, deployment, or publication authority.", "guardrail"),
    runtimeStatusHost,
    runtimeControls,
    link(document, "Open governance issue #2957", `https://github.com/${REPOSITORY_SNAPSHOT.repository}/issues/${CURRENT_MAPLIBRE_READINESS.governanceIssue}`, "text-link"),
  );
  mapGrid.append(mapCard, runtime);
  mapSection.append(mapGrid);
  const lab = el(document, "div", "selection-lab card");
  lab.append(text(document, "p", "Deterministic interaction lab", "eyebrow"), text(document, "h3", "Map click → governed evidence outcome"), text(document, "p", "Exercise supported, missing, restricted, mismatched, and resolver-error paths. Rendered properties never become evidence."));
  const fixtureHost = el(document, "div", "selection-lab__fixture");
  lab.append(fixtureHost);
  mapSection.append(lab);
  main.append(mapSection);
  mapFixture = mountMapFeatureEvidenceFixture(fixtureHost, mapCases, async (selection) => {
    await Promise.resolve();
    if (selection.selectionId === "selection:restricted") return restrictedProjection;
    if (selection.selectionId === "selection:error") throw new Error("Synthetic governed resolver failure");
    return SUPPORTED_SYNTHETIC_STREAMFLOW_PROJECTION;
  });
  mapRuntimeStatus = mountMapRuntimeTrustStatus(runtimeStatusHost, mapRuntime);

  const knowledge = el(document, "section", "section-shell");
  knowledge.id = "knowledge";
  knowledge.append(heading(document, "Knowledge matrix", "Thirteen connected Kansas knowledge domains", "Each domain is a bounded organizing lens with visible public-safety guardrails, not a claim that live data is available."));
  const domainLayout = el(document, "div", "domain-layout");
  const domainButtons = el(document, "div", "domain-buttons");
  domainButtons.setAttribute("aria-label", "Knowledge domains");
  const domainHost = el(document, "div", "domain-host");
  const selectDomain = (id: string, focus: boolean): void => {
    const domain = findDomain(id);
    if (!domain) return;
    domainButtons.querySelectorAll<HTMLButtonElement>("button").forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.domainId === id)));
    domainHost.replaceChildren(domainDetail(document, domain));
    if (focus) domainHost.querySelector<HTMLElement>("h3")?.focus();
  };
  KNOWLEDGE_DOMAINS.forEach((domain) => {
    const button = el(document, "button", "domain-button");
    button.type = "button";
    button.textContent = domain.name;
    button.dataset.domainId = domain.id;
    button.setAttribute("aria-pressed", "false");
    const handler = (): void => selectDomain(domain.id, true);
    button.addEventListener("click", handler);
    cleanup.push(() => button.removeEventListener("click", handler));
    domainButtons.append(button);
  });
  domainLayout.append(domainButtons, domainHost);
  knowledge.append(domainLayout);
  main.append(knowledge);
  selectDomain("hydrology", false);

  const features = el(document, "section", "section-shell");
  features.id = "features";
  features.append(heading(document, "Repository features", "All current Explorer feature families in one catalog", "Search and filter the repository-grounded inventory. Maturity labels distinguish verified slices, fixture-first work, documentation, and held runtime admission."));
  const filters = el(document, "form", "feature-filters");
  filters.setAttribute("role", "search");
  const search = el(document, "input");
  search.type = "search";
  search.placeholder = "Search evidence, hydrology, PMTiles…";
  search.setAttribute("aria-label", "Search Explorer features");
  const area = el(document, "select");
  area.setAttribute("aria-label", "Filter by feature area");
  option(document, area, "ALL", "All areas");
  [...new Set(FEATURE_CATALOG.map((entry) => entry.area))].forEach((value) => option(document, area, value, value));
  const maturity = el(document, "select");
  maturity.setAttribute("aria-label", "Filter by maturity");
  option(document, maturity, "ALL", "All maturity states");
  (["VERIFIED_SLICE", "FIXTURE_FIRST", "DOCUMENTED", "HOLD"] as const).forEach((value) => option(document, maturity, value, value.replaceAll("_", " ")));
  const preventSubmit = (event: SubmitEvent): void => event.preventDefault();
  filters.addEventListener("submit", preventSubmit);
  cleanup.push(() => filters.removeEventListener("submit", preventSubmit));
  filters.append(search, area, maturity);
  const resultStatus = text(document, "p", "", "result-status");
  resultStatus.setAttribute("role", "status");
  resultStatus.setAttribute("aria-live", "polite");
  const featureGrid = el(document, "div", "feature-grid");
  const renderFeatures = (): void => {
    const matches = filterFeatures({ text: search.value, area: area.value as FeatureArea | "ALL", maturity: maturity.value as FeatureMaturity | "ALL" });
    featureGrid.replaceChildren(...matches.map((entry) => featureCard(document, entry)));
    resultStatus.textContent = `${matches.length} of ${FEATURE_CATALOG.length} feature families shown.`;
  };
  [search, area, maturity].forEach((control) => {
    control.addEventListener("input", renderFeatures);
    cleanup.push(() => control.removeEventListener("input", renderFeatures));
  });
  features.append(filters, resultStatus, featureGrid);
  main.append(features);
  renderFeatures();

  const trust = el(document, "section", "section-shell");
  trust.id = "trust";
  trust.append(heading(document, "Trust architecture", "The rules remain visible at the point of use", "The interface is downstream of evidence, policy, review, release, correction, and rollback. Honest negative outcomes are product behavior, not error decoration."));
  const principleGrid = el(document, "div", "principle-grid");
  KNOWLEDGE_PRINCIPLES.forEach((principle) => {
    const card = el(document, "article", "principle-card card");
    card.append(text(document, "h3", principle.name), text(document, "p", principle.summary));
    principleGrid.append(card);
  });
  const snapshot = el(document, "article", "snapshot card");
  snapshot.append(text(document, "p", "Evidence snapshot", "eyebrow"), text(document, "h3", `main@${REPOSITORY_SNAPSHOT.commit.slice(0, 12)}`), text(document, "p", "The displayed catalog is a repository snapshot. It does not create runtime, release, deployment, or publication authority."), link(document, "Open exact repository tree", `https://github.com/${REPOSITORY_SNAPSHOT.repository}/tree/${REPOSITORY_SNAPSHOT.commit}`, "text-link"));
  trust.append(principleGrid, snapshot);
  main.append(trust);

  const footer = el(document, "footer", "site-footer");
  footer.append(text(document, "p", "Kansas Frontier Matrix · governed synthetic Explorer composition"), text(document, "p", "Not for emergency, legal-title, regulatory, or life-safety decisions."));
  root.replaceChildren(skip, header, main, footer);

  return Object.freeze({
    destroy: () => {
      cleanup.forEach((fn) => fn());
      mapRuntimeStatus?.destroy();
      mapRuntimeStatus = null;
      mapRuntime.dispose();
      mapFixture?.destroy();
      mapFixture = null;
      root.replaceChildren();
      root.className = "";
      delete document.documentElement.dataset.kfmExplorer;
    },
  });
}
