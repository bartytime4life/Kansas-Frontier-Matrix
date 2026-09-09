import {
  TERRAIN_SOURCES,
  type TerrainSourceRecord,
  type TerrainSourceRole,
} from "./terrain-source-registry";

export const TERRAIN_MODE_POSTURE = Object.freeze([
  Object.freeze({ label: "2D", detail: "parity path", active: false }),
  Object.freeze({ label: "Terrain 3D", detail: "fixture-only HOLD", active: false }),
  Object.freeze({ label: "3DEP", detail: "admission candidate", active: false }),
] as const);

const ROLE_LABELS: Readonly<Record<TerrainSourceRole, string>> = Object.freeze({
  DISPLAY_CONTEXT: "DISPLAY CONTEXT",
  AUTHORITATIVE_CANDIDATE: "CANDIDATE",
  IMPLEMENTATION_SPEC: "RENDERER SPEC",
});

const appendDefinition = (
  list: HTMLDListElement,
  term: string,
  detail: string,
): void => {
  const group = document.createElement("div");
  const dt = document.createElement("dt");
  const dd = document.createElement("dd");
  dt.textContent = term;
  dd.textContent = detail;
  group.append(dt, dd);
  list.append(group);
};

const buildSourceCard = (source: TerrainSourceRecord): HTMLElement => {
  const article = document.createElement("article");
  article.className = "terrain-source-card";
  article.dataset.role = source.role;

  const meta = document.createElement("header");
  const organization = document.createElement("span");
  const role = document.createElement("strong");
  organization.textContent = source.organization;
  role.textContent = ROLE_LABELS[source.role];
  meta.append(organization, role);

  const title = document.createElement("h4");
  title.textContent = source.title;

  const facts = document.createElement("dl");
  appendDefinition(facts, "Resolution", source.resolution);
  appendDefinition(facts, "Format", source.format);
  appendDefinition(facts, "Coverage", source.coverage);
  appendDefinition(facts, "Attribution", source.attribution);

  const boundary = document.createElement("p");
  boundary.textContent = source.boundary;

  const link = document.createElement("a");
  link.href = source.sourceUrl;
  link.target = "_blank";
  link.rel = "noreferrer";
  link.textContent = "Open primary source ↗";

  article.append(meta, title, facts, boundary, link);
  return article;
};

/**
 * Adds a source-first terrain lane to the public map workspace.
 * This is a documentation and governance surface only; it does not start a
 * raster request or change the held NullMapRuntime seam.
 */
export const mountTerrainSourceLedger = (
  root: ParentNode,
): HTMLElement | null => {
  const mapSection = root.querySelector<HTMLElement>("#map");
  if (mapSection === null) return null;

  const existing = mapSection.querySelector<HTMLElement>(
    "[data-terrain-source-ledger]",
  );
  if (existing !== null) return existing;

  const section = document.createElement("section");
  section.className = "terrain-source-ledger";
  section.dataset.terrainSourceLedger = "true";
  section.setAttribute("aria-labelledby", "terrain-source-ledger-title");

  const header = document.createElement("header");
  const headingCopy = document.createElement("div");
  const eyebrow = document.createElement("span");
  const title = document.createElement("h3");
  const state = document.createElement("strong");
  eyebrow.textContent = "TERRAIN SOURCE LEDGER";
  title.id = "terrain-source-ledger-title";
  title.textContent = "3D terrain, with the evidence boundary visible";
  state.textContent = "ROLE-SEPARATED";
  headingCopy.append(eyebrow, title);
  header.append(headingCopy, state);

  const modeStrip = document.createElement("div");
  modeStrip.className = "terrain-mode-strip";
  modeStrip.setAttribute("aria-label", "Terrain implementation posture");
  for (const { label, detail, active } of TERRAIN_MODE_POSTURE) {
    const item = document.createElement("span");
    item.dataset.active = String(active);
    const name = document.createElement("b");
    const description = document.createElement("small");
    name.textContent = label;
    description.textContent = detail;
    item.append(name, description);
    modeStrip.append(item);
  }

  const cards = document.createElement("div");
  cards.className = "terrain-source-grid";
  for (const source of TERRAIN_SOURCES) {
    cards.append(buildSourceCard(source));
  }

  const law = document.createElement("p");
  law.className = "terrain-source-law";
  law.textContent =
    "Rendered relief is visual context. Elevation becomes evidence only through a pinned, lineage-preserving, reviewed, and released KFM artifact.";

  section.append(header, modeStrip, cards, law);
  mapSection.querySelector(".map-grid")?.insertAdjacentElement("afterend", section);
  if (!section.isConnected) mapSection.append(section);
  return section;
};
