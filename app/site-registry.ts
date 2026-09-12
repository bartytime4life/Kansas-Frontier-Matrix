import { SITE_CODE_SURFACES, SITE_ROUTE_CONTRACTS } from "./site-architecture";
import { SITE_CONNECTIONS } from "./site-connections";
import { SITE_ACTIONS } from "./site-actions";
import { SITE_FEATURES } from "./site-features";

export const SITE_REGISTRY_VERSION = "kfm-site-registry-v1";

export type SiteRegistryValidation = Readonly<{
  ok: boolean;
  errors: readonly string[];
}>;

const duplicateIds = (ids: readonly string[]): string[] => {
  const seen = new Set<string>();
  const duplicates = new Set<string>();
  for (const id of ids) {
    if (seen.has(id)) duplicates.add(id);
    seen.add(id);
  }
  return [...duplicates];
};

const hasNoItems = (items: readonly unknown[]): boolean => items.length === 0;

/** Validate cross-file references without making the UI depend on a runtime throw. */
export const validateSiteRegistry = (): SiteRegistryValidation => {
  const errors: string[] = [];
  const connectionIds = new Set(SITE_CONNECTIONS.map((connection) => connection.id));
  const actionIds = new Set(SITE_ACTIONS.map((action) => action.id));

  for (const id of duplicateIds(SITE_FEATURES.map((feature) => feature.id))) errors.push(`duplicate feature id: ${id}`);
  for (const id of duplicateIds(SITE_CONNECTIONS.map((connection) => connection.id))) errors.push(`duplicate connection id: ${id}`);
  for (const id of duplicateIds(SITE_ACTIONS.map((action) => action.id))) errors.push(`duplicate action id: ${id}`);
  for (const id of duplicateIds(SITE_CODE_SURFACES.map((surface) => surface.id))) errors.push(`duplicate code surface id: ${id}`);
  for (const id of duplicateIds(SITE_ROUTE_CONTRACTS.map((route) => route.id))) errors.push(`duplicate route id: ${id}`);

  for (const feature of SITE_FEATURES) {
    for (const sourceId of feature.sourceIds) if (!connectionIds.has(sourceId)) errors.push(`feature ${feature.id} references unknown connection: ${sourceId}`);
    for (const actionId of feature.actionIds) if (!actionIds.has(actionId)) errors.push(`feature ${feature.id} references unknown action: ${actionId}`);
    if (hasNoItems(feature.codePaths)) errors.push(`feature ${feature.id} has no code path`);
  }
  for (const connection of SITE_CONNECTIONS) {
    for (const actionId of connection.actionIds) if (!actionIds.has(actionId)) errors.push(`connection ${connection.id} references unknown action: ${actionId}`);
    if (hasNoItems(connection.codePaths)) errors.push(`connection ${connection.id} has no code path`);
  }
  for (const action of SITE_ACTIONS) {
    if (action.handlerPath.length === 0) errors.push(`action ${action.id} has no handler path`);
    if (hasNoItems(action.outcomes)) errors.push(`action ${action.id} has no declared outcome`);
  }
  for (const surface of SITE_CODE_SURFACES) if (hasNoItems(surface.paths)) errors.push(`code surface ${surface.id} has no path`);

  return Object.freeze({ ok: errors.length === 0, errors: Object.freeze(errors) });
};

export const SITE_REGISTRY_VALIDATION = validateSiteRegistry();

export const SITE_REGISTRY = Object.freeze({
  version: SITE_REGISTRY_VERSION,
  features: SITE_FEATURES,
  connections: SITE_CONNECTIONS,
  actions: SITE_ACTIONS,
  codeSurfaces: SITE_CODE_SURFACES,
  routes: SITE_ROUTE_CONTRACTS,
  validation: SITE_REGISTRY_VALIDATION,
});

export const SITE_REGISTRY_COUNTS = Object.freeze({
  features: SITE_FEATURES.length,
  connections: SITE_CONNECTIONS.length,
  actions: SITE_ACTIONS.length,
  codeSurfaces: SITE_CODE_SURFACES.length,
  routes: SITE_ROUTE_CONTRACTS.length,
});
