import { resolveBaselineShell } from "../features/shell";
import {
  mountGovernedMapWorkspace,
  type GovernedMapWorkspaceController,
  type GovernedMapWorkspaceDependencies,
} from "./mount-governed-map-workspace";
import {
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

export type ExplorerSiteDependencies = GovernedMapWorkspaceDependencies;
export type ExplorerSiteController = Readonly<{
  ready: Promise<void>;
  destroy: () => void;
}>;

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

export function mountExplorerSite(
  root: HTMLElement,
  dependencies: ExplorerSiteDependencies,
): ExplorerSiteController {
  const document = root.ownerDocument;
  const baseline = resolveBaselineShell();
  const cleanup: Array<() => void> = [];
  let governedMap: GovernedMapWorkspaceController | null = null;
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
  headerState.append(chip(document, "Shell", baseline.outcome, "caution"), chip(document, "Broader renderer", "HOLD", "critical"));
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
  posture.append(text(document, "p", "Current composed posture", "eyebrow"), text(document, "p", `${baseline.outcome} / ${baseline.code}`, "posture__outcome"), text(document, "p", baseline.message), text(document, "p", "One bounded synthetic map/evidence integration is active. No live KFM source activation, model runtime, broader renderer readiness, release, deployment, or publication.", "guardrail"));
  hero.append(heroCopy, posture);
  main.append(hero);

  const mapSection = el(document, "section", "section-shell");
  mapSection.id = "map";
  mapSection.append(
    heading(
      document,
      "Map workspace",
      "A real map with an evidence-preserving fallback",
      "The canonical synthetic layer arrives through the governed API, binds through the package-owned MapLibre adapter, and reuses one selection identity for pointer and keyboard interaction.",
    ),
  );
  const governedMapHost = el(document, "div", "governed-map-host");
  mapSection.append(governedMapHost);
  governedMap = mountGovernedMapWorkspace(governedMapHost, dependencies);
  main.append(mapSection);

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
  const ready = governedMap.start();

  return Object.freeze({
    ready,
    destroy: () => {
      cleanup.forEach((fn) => fn());
      governedMap?.destroy();
      governedMap = null;
      root.replaceChildren();
      root.className = "";
      delete document.documentElement.dataset.kfmExplorer;
    },
  });
}
