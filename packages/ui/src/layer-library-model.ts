/** UI projections and reversible workspace edits, not catalog or policy authority.
 * Callers supply already-disclosable metadata and revalidate delivery separately.
 * This module has no network, geometry, camera, storage, or renderer capability.
 */
export type Match = true | false | null;
export type Release = "released" | "unreleased" | "withdrawn" | "unknown";
export type Runtime = "held" | "idle" | "loading" | "ready" | "error";
export type CatalogCard = Readonly<{
  id: string; title: string; description: string; provider: string; domain: string;
  representation: string; coverageLabel: string; areaMatch: Match;
  timeLabel: string; timeMatch: Match; sourceTime: string; releaseTime: string;
  sourceId: string; datasetVersion: string; artifactVersion: string;
  disclosure: "allow"; access: "allow" | "deny" | "unknown";
  rights: "cleared" | "unknown"; sensitivity: "public" | "unknown";
  release: Release; fixture: boolean; generalized: boolean;
  workspaceAction: "add" | "preview" | "none"; runtime: Runtime;
  renderGroup: string | null; defaultOpacity: number; evidenceRef: string; units: string; limitations: string;
}>;
export type CardInput = Partial<Omit<CatalogCard, "disclosure">> & { disclosure?: "allow" | "deny" | "unknown" };
export type Filters = Readonly<{
  query: string; domain: string; provider: string; representation: string;
  areaOnly: boolean; timeOnly: boolean; mode: "eligible" | "fixtures" | "discovery";
}>;
export const EMPTY_FILTERS: Filters = Object.freeze({
  query: "", domain: "", provider: "", representation: "", areaOnly: false,
  timeOnly: false, mode: "eligible",
});
export const MAX_CATALOG_CARDS = 20_000; // Safety cap, not a measured performance budget.
export const MAX_WORKSPACE_LAYERS = 100;
export const PAGE_SIZE = 24;
const text = (v: unknown, max = 300): string => typeof v === "string" ? v.slice(0, max) : "";
const choice = <T extends string>(v: unknown, values: readonly T[], fallback: T): T =>
  values.includes(v as T) ? v as T : fallback;
const match = (v: unknown): Match => v === true ? true : v === false ? false : null;
const idPattern = /^[A-Za-z0-9][A-Za-z0-9_.:/-]{0,199}$/;
const reserved = new Set(["__proto__", "constructor", "prototype"]);
export const validId = (v: unknown): v is string =>
  typeof v === "string" && idPattern.test(v) && !reserved.has(v);
const opacity = (v: unknown): number => typeof v === "number" && Number.isFinite(v)
  ? Math.min(1, Math.max(0, v)) : 1;

/** Denied/unknown disclosure objects are not inspected beyond disclosure.
 * Duplicate IDs are entirely suppressed rather than choosing an ambiguous record.
 * No object spread: payloads, tokens, URLs and extra upstream fields never survive.
 */
export function projectCatalog(inputs: readonly CardInput[]): readonly CatalogCard[] {
  if (!Array.isArray(inputs) || inputs.length > MAX_CATALOG_CARDS) {
    throw new RangeError("Catalog metadata limit exceeded; use a paginated adapter.");
  }
  const cards: CatalogCard[] = [];
  const seen = new Set<string>();
  const duplicates = new Set<string>();
  for (const input of inputs) {
    if (!input || input.disclosure !== "allow" || !validId(input.id)) continue;
    const id = input.id;
    if (seen.has(id)) { duplicates.add(id); continue; }
    seen.add(id);
    const card: CatalogCard = Object.freeze({
      id, disclosure: "allow", title: text(input.title, 160) || id,
      description: text(input.description, 800), provider: text(input.provider, 180),
      domain: text(input.domain, 100), representation: text(input.representation, 80),
      coverageLabel: text(input.coverageLabel), areaMatch: match(input.areaMatch),
      timeLabel: text(input.timeLabel), timeMatch: match(input.timeMatch),
      sourceTime: text(input.sourceTime, 180), releaseTime: text(input.releaseTime, 180),
      sourceId: text(input.sourceId, 200), datasetVersion: text(input.datasetVersion, 200),
      artifactVersion: text(input.artifactVersion, 200),
      access: choice(input.access, ["allow", "deny", "unknown"], "unknown"),
      rights: choice(input.rights, ["cleared", "unknown"], "unknown"),
      sensitivity: choice(input.sensitivity, ["public", "unknown"], "unknown"),
      release: choice(input.release, ["released", "unreleased", "withdrawn", "unknown"], "unknown"),
      fixture: input.fixture === true, generalized: input.generalized === true,
      workspaceAction: choice(input.workspaceAction, ["add", "preview", "none"], "none"),
      runtime: choice(input.runtime, ["held", "idle", "loading", "ready", "error"], "held"),
      renderGroup: validId(input.renderGroup) ? input.renderGroup : null,
      defaultOpacity: opacity(input.defaultOpacity),
      evidenceRef: text(input.evidenceRef, 240), units: text(input.units, 180),
      limitations: text(input.limitations, 1600),
    });
    cards.push(card);
  }
  return Object.freeze(cards.filter((card) => !duplicates.has(card.id)));
}

export function availability(card: CatalogCard): "eligible" | "fixture" | "unavailable" {
  if (card.access !== "allow" || card.rights !== "cleared" || card.sensitivity !== "public"
      || card.release === "withdrawn") return "unavailable";
  if (card.fixture) return card.workspaceAction === "preview" ? "fixture" : "unavailable";
  return card.workspaceAction === "add" && card.release === "released"
    && !!card.datasetVersion && !!card.artifactVersion && !!card.evidenceRef
    ? "eligible" : "unavailable";
}
export function selectCards(cards: readonly CatalogCard[], f: Filters, page = 0) {
  const q = text(f.query, 200).trim().toLocaleLowerCase("en-US");
  const filtered = cards.filter((c) => {
    const a = availability(c);
    return (f.mode === "eligible" ? a === "eligible" : f.mode === "fixtures" ? a === "fixture" : a === "unavailable")
      && (!f.domain || c.domain === f.domain) && (!f.provider || c.provider === f.provider)
      && (!f.representation || c.representation === f.representation)
      && (!f.areaOnly || c.areaMatch === true) && (!f.timeOnly || c.timeMatch === true)
      && (!q || `${c.title} ${c.description} ${c.provider} ${c.domain}`.toLocaleLowerCase("en-US").includes(q));
  });
  const pages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
  const current = Math.max(0, Math.min(pages - 1, Number.isSafeInteger(page) ? page : 0));
  return { cards: filtered.slice(current * PAGE_SIZE, (current + 1) * PAGE_SIZE),
    total: filtered.length, pages, page: current };
}
export type LayerState = Readonly<{ id: string; visible: boolean; opacity: number }>;
export type Workspace = readonly LayerState[]; // Requested top-to-bottom order only.
export function normalizeWorkspace(input: Workspace, cards: readonly CatalogCard[]): Workspace {
  if (!Array.isArray(input) || input.length > MAX_WORKSPACE_LAYERS) throw new RangeError("Workspace layer limit exceeded.");
  const allowed = new Set(cards.filter((c) => availability(c) !== "unavailable").map((c) => c.id));
  const seen = new Set<string>();
  return Object.freeze(input.filter((item) => item && validId(item.id) && allowed.has(item.id)
    && !seen.has(item.id) && !!seen.add(item.id))
    .map((item) => Object.freeze({ id: item.id, visible: item.visible === true, opacity: opacity(item.opacity) })));
}
export const sameWorkspace = (a: Workspace, b: Workspace): boolean => a.length === b.length
  && a.every((v, i) => v.id === b[i].id && v.visible === b[i].visible && v.opacity === b[i].opacity);
export type Undo = Readonly<{ before: Workspace; after: Workspace }>;
export type EditResult = Readonly<{ next: Workspace; undo: Undo | null; notice: string; rejected: number }>;
export function stagePlan(ids: readonly string[], current: Workspace, cards: readonly CatalogCard[]) {
  if (ids.length > MAX_WORKSPACE_LAYERS) throw new RangeError("Selection limit exceeded.");
  const byId = new Map(cards.map((c) => [c.id, c]));
  const existing = new Set(current.map((c) => c.id));
  const accepted: string[] = [];
  let rejected = 0; let duplicates = 0;
  for (const id of new Set(ids)) {
    const card = byId.get(id);
    if (!card || availability(card) === "unavailable") { rejected++; continue; }
    if (existing.has(id)) { duplicates++; continue; }
    if (current.length + accepted.length >= MAX_WORKSPACE_LAYERS) { rejected++; continue; }
    accepted.push(id);
  }
  // Return counts only for exclusions: never echo a denied ID or its previous title.
  return { accepted, rejected, duplicates };
}
export function addStaged(ids: readonly string[], current: Workspace, cards: readonly CatalogCard[], fixedOrder?: readonly string[]): EditResult {
  const before = normalizeWorkspace(current, cards);
  const plan = stagePlan(ids, before, cards); // Delivery-time defensive recheck.
  const byId = new Map(cards.map((card) => [card.id, card]));
  const next = Object.freeze([...before, ...plan.accepted.map((id) => Object.freeze({
    id, visible: true, opacity: byId.get(id)!.defaultOpacity,
  }))]);
  // Hosts with held/unknown render groups may require their existing order.
  // Adding a member must not silently reorder those groups or fake readback.
  let ordered = next;
  if (fixedOrder) {
    const ranks = new Map(fixedOrder.map((id, index) => [id, index]));
    if (ranks.size !== fixedOrder.length || next.some((item) => !ranks.has(item.id))) {
      return { next: before, undo: null, rejected: plan.accepted.length + plan.rejected,
        notice: "Host layer order is unavailable; no additions were applied." };
    }
    ordered = Object.freeze([...next].sort((a, b) => ranks.get(a.id)! - ranks.get(b.id)!));
  }
  return { next: ordered, undo: plan.accepted.length ? { before, after: ordered } : null, rejected: plan.rejected,
    notice: `${plan.accepted.length} added to the requested stack. ${plan.duplicates} already present. ${plan.rejected} unavailable or over the limit. Rendering is a separate state.` };
}
export type Edit = { kind: "visible"; id: string; value: boolean }
  | { kind: "opacity"; id: string; value: number } | { kind: "remove"; id: string }
  | { kind: "move"; id: string; direction: -1 | 1 };
export function editWorkspace(current: Workspace, cards: readonly CatalogCard[], edit: Edit): EditResult {
  const before = normalizeWorkspace(current, cards);
  const next = [...before];
  const index = next.findIndex((x) => x.id === edit.id);
  if (index < 0) return { next: before, undo: null, rejected: 1, notice: "This action is unavailable." };
  if (edit.kind === "remove") next.splice(index, 1);
  else if (edit.kind === "visible") next[index] = Object.freeze({ ...next[index], visible: edit.value === true });
  else if (edit.kind === "opacity") {
    if (!Number.isFinite(edit.value) || edit.value < 0 || edit.value > 1) return { next: before, undo: null, rejected: 1, notice: "Opacity must be between 0 and 1." };
    next[index] = Object.freeze({ ...next[index], opacity: edit.value });
  } else {
    const target = index + edit.direction;
    const byId = new Map(cards.map((c) => [c.id, c]));
    const group = byId.get(edit.id)?.renderGroup;
    if ((edit.direction !== -1 && edit.direction !== 1) || !next[target] || !group
      || byId.get(next[target].id)?.renderGroup !== group) {
      return { next: before, undo: null, rejected: 1, notice: "Reordering needs adjacent layers in the same declared render group. Unknown groups remain fixed." };
    }
    [next[index], next[target]] = [next[target], next[index]];
  }
  const frozen = Object.freeze(next);
  return { next: frozen, undo: sameWorkspace(before, frozen) ? null : { before, after: frozen }, rejected: 0, notice: "Requested stack updated; camera and feature selection unchanged." };
}
export function undoEdit(undo: Undo, current: Workspace, cards: readonly CatalogCard[]): EditResult {
  if (!sameWorkspace(current, undo.after)) return { next: normalizeWorkspace(current, cards), undo: null, rejected: 1,
    notice: "Undo was not applied because the workspace changed. Your later work was preserved." };
  const next = normalizeWorkspace(undo.before, cards); // Never resurrect withdrawn/denied references.
  return { next, undo: null, rejected: undo.before.length - next.length,
    notice: "Previous requested stack restored after current eligibility checks. Revoked references stay removed." };
}
export function nonvisibility(card: CatalogCard, layer: LayerState): string {
  if (availability(card) === "unavailable") return "Unavailable";
  if (!layer.visible) return "Disabled";
  if (card.runtime === "held") return "Renderer held — not drawn";
  if (card.runtime === "loading") return "Loading";
  if (card.runtime === "error") return "Delivery failed";
  if (card.areaMatch === false) return "Outside selected area coverage";
  if (card.timeMatch === false) return "No matching time";
  if (layer.opacity === 0) return "Opacity is zero";
  return card.runtime === "ready" ? "Delivery ready; visibility still depends on renderer scale and filters" : "Awaiting delivery";
}


export type WorkspaceWritePort = Readonly<{
  read: () => Workspace;
  write: (next: Workspace, expected: Workspace) => boolean;
}>;
export type WriteConfirmation = Readonly<{
  outcome: "APPLIED" | "CONFLICT" | "UNCONFIRMED" | "ERROR";
  notice: string;
}>;

/** Capture values, not mutable host references. This is a UI transaction shape,
 * not a canonical identity, policy or workspace-persistence contract.
 */
function captureWorkspace(input: Workspace): Workspace {
  if (!Array.isArray(input) || input.length > MAX_WORKSPACE_LAYERS) throw new RangeError("Invalid workspace.");
  const seen = new Set<string>();
  return Object.freeze(input.map((item) => {
    if (!item || !validId(item.id) || seen.has(item.id) || typeof item.visible !== "boolean"
      || typeof item.opacity !== "number" || !Number.isFinite(item.opacity)
      || item.opacity < 0 || item.opacity > 1) throw new TypeError("Invalid workspace.");
    seen.add(item.id);
    return Object.freeze({ id: item.id, visible: item.visible, opacity: item.opacity });
  }));
}

/** One synchronous compare-and-set followed by value readback. Never retries,
 * compensates, logs an exception, or turns an uncertain write into success.
 * APPLIED confirms only this requested-state port, not React paint or rendering.
 * A host can mutate and then fail; ERROR/UNCONFIRMED therefore do not mean that
 * nothing changed. An independently enforced server transaction is still separate.
 */
export function confirmWorkspaceWrite(
  port: WorkspaceWritePort, next: Workspace, expected: Workspace,
): WriteConfirmation {
  try {
    const before = captureWorkspace(expected);
    const intended = captureWorkspace(next);
    if (!sameWorkspace(captureWorkspace(port.read()), before)) return {
      outcome: "CONFLICT", notice: "Workspace changed elsewhere. No stale write was sent; review the current stack.",
    };
    if (sameWorkspace(before, intended)) return { outcome: "APPLIED", notice: "Requested state already matches." };
    const accepted = port.write(intended, before);
    if (accepted === false) return {
      outcome: "CONFLICT", notice: "The host declined the workspace change. Review the current stack before trying again.",
    };
    if (accepted !== true || !sameWorkspace(captureWorkspace(port.read()), intended)) return {
      outcome: "UNCONFIRMED", notice: "Workspace write was not confirmed by readback. No retry or automatic rollback was attempted.",
    };
    return { outcome: "APPLIED", notice: "Requested workspace state confirmed by readback; rendering remains separate." };
  } catch {
    return { outcome: "ERROR", notice: "Workspace result could not be confirmed. No retry or automatic rollback was attempted." };
  }
}
