import { FEATURE_CATALOG } from "./catalog";

/**
 * Public, composition-owned workspace destinations for the current Explorer.
 *
 * This registry is navigation metadata only. It grants no policy, review,
 * source, lifecycle, release, deployment, or publication authority.
 */
export const PUBLIC_WORKSPACE_IDS = [
  "explore",
  "knowledge",
  "features",
  "trust",
] as const;

export type PublicWorkspaceId = (typeof PUBLIC_WORKSPACE_IDS)[number];
export type PublicWorkspaceSectionId = "map" | "knowledge" | "features" | "trust";

export type PublicWorkspaceDescriptor = Readonly<{
  id: PublicWorkspaceId;
  navLabel: string;
  title: string;
  summary: string;
  sectionId: PublicWorkspaceSectionId;
  href: `#${PublicWorkspaceSectionId}`;
  featureIds: readonly string[];
  publicSafe: true;
  privileged: false;
}>;

const catalogFeatureIds = new Set(FEATURE_CATALOG.map((entry) => entry.id));
const allFeatureIds = Object.freeze(FEATURE_CATALOG.map((entry) => entry.id));

function freezeFeatureIds(featureIds: readonly string[]): readonly string[] {
  const unique = [...new Set(featureIds)];
  const unknown = unique.filter((featureId) => !catalogFeatureIds.has(featureId));
  if (unknown.length > 0) {
    throw new Error(`Unknown Explorer feature IDs: ${unknown.join(", ")}`);
  }
  return Object.freeze(unique);
}

function workspace(
  id: PublicWorkspaceId,
  navLabel: string,
  title: string,
  summary: string,
  sectionId: PublicWorkspaceSectionId,
  featureIds: readonly string[],
): PublicWorkspaceDescriptor {
  return Object.freeze({
    id,
    navLabel,
    title,
    summary,
    sectionId,
    href: `#${sectionId}`,
    featureIds: freezeFeatureIds(featureIds),
    publicSafe: true,
    privileged: false,
  });
}

export const PUBLIC_WORKSPACES: readonly PublicWorkspaceDescriptor[] = Object.freeze([
  workspace(
    "explore",
    "Map",
    "Explore",
    "Map-first, renderer-neutral exploration with time and governed evidence resolution.",
    "map",
    [
      "map-runtime",
      "time-banner",
      "layer-catalog",
      "evidence-drawer",
      "focus-panel",
      "compare",
      "export",
    ],
  ),
  workspace(
    "knowledge",
    "Knowledge",
    "Knowledge",
    "Browse the thirteen bounded Kansas knowledge domains and their public safeguards.",
    "knowledge",
    ["domains", "layer-catalog"],
  ),
  workspace(
    "features",
    "Features",
    "Features",
    "Inspect the repository-grounded Explorer feature catalog and conservative maturity labels.",
    "features",
    allFeatureIds,
  ),
  workspace(
    "trust",
    "Trust",
    "Trust",
    "Inspect evidence, citations, limitations, denials, redaction, consent, and attestation cues.",
    "trust",
    [
      "trust-header",
      "evidence-drawer",
      "citation-pill",
      "provenance-citations",
      "denial-reason",
      "redaction-preview",
      "consent-card",
      "attestation-badge",
    ],
  ),
]);

const workspaceById = new Map(
  PUBLIC_WORKSPACES.map((entry) => [entry.id, entry] as const),
);
const workspaceBySectionId = new Map(
  PUBLIC_WORKSPACES.map((entry) => [entry.sectionId, entry] as const),
);

export function isPublicWorkspaceId(value: unknown): value is PublicWorkspaceId {
  return typeof value === "string" && workspaceById.has(value as PublicWorkspaceId);
}

export function findPublicWorkspace(
  value: unknown,
): PublicWorkspaceDescriptor | null {
  return isPublicWorkspaceId(value) ? workspaceById.get(value) ?? null : null;
}

function normalizeHash(hash: string): string | null {
  const raw = hash.startsWith("#") ? hash.slice(1) : hash;
  if (!raw) return null;
  try {
    return decodeURIComponent(raw).trim().toLocaleLowerCase();
  } catch {
    return null;
  }
}

export function findPublicWorkspaceByHash(
  hash: string,
): PublicWorkspaceDescriptor | null {
  const sectionId = normalizeHash(hash);
  if (!sectionId) return null;
  return workspaceBySectionId.get(sectionId as PublicWorkspaceSectionId) ?? null;
}
