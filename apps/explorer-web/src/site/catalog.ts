/** Repository-grounded, descriptive catalog for the Explorer composition shell. */
export const REPOSITORY_SNAPSHOT = Object.freeze({
  repository: "bartytime4life/Kansas-Frontier-Matrix",
  ref: "main",
  commit: "67cf9bcd8d4044beb2f7ec4ec17e1bf162ca30aa",
  commitRecordedAt: "2026-08-19T05:22:18Z",
  explorerPath: "apps/explorer-web",
  mapLibre: Object.freeze({
    family: "MapLibre GL JS",
    packageHome: "packages/maplibre",
    readinessCandidate: "6.4.0",
    readinessState: "HOLD" as const,
    dependencyAdmitted: false,
    runtimeImplemented: false,
    governanceIssue: 2957,
    runtimeEvidenceIssue: 2906,
  }),
});

/** Current MapLibre readiness facts, intentionally separate from the pinned snapshot. */
export const CURRENT_MAPLIBRE_READINESS = Object.freeze({
  evidenceCommit: "1a3a4075537ea47b7b87b3e2dccbb044b6a62e0f",
  evidenceRecordedAt: "2026-08-27T18:33:32Z",
  family: "MapLibre GL JS",
  packageHome: "packages/maplibre",
  readinessCandidate: "6.6.0",
  readinessState: "HOLD" as const,
  packagePresent: true,
  adapterImplemented: true,
  browserRuntimeActivated: false,
  browserEvidenceComplete: false,
  governanceIssue: 2957,
  runtimeEvidenceIssue: 2906,
});

export type FeatureArea =
  | "Shell"
  | "Map and layers"
  | "Evidence and trust"
  | "Environmental insight"
  | "Governance and operations"
  | "User workflows";
export type FeatureMaturity = "VERIFIED_SLICE" | "FIXTURE_FIRST" | "DOCUMENTED" | "HOLD";
export type FeatureEntry = Readonly<{
  id: string;
  name: string;
  area: FeatureArea;
  maturity: FeatureMaturity;
  summary: string;
  path: string;
  keywords: readonly string[];
}>;

type FeatureRow = readonly [string, string, FeatureArea, FeatureMaturity, string, string, string];
const rows: readonly FeatureRow[] = [
  ["shell", "Governed shell", "Shell", "VERIFIED_SLICE", "Finite fail-closed application state and composition root.", "shell", "navigation abstain composition"],
  ["trust-header", "Trust Header", "Shell", "VERIFIED_SLICE", "Visible policy, review, release, freshness, and correction state.", "trust_header", "trust policy review"],
  ["time-banner", "Time Banner", "Shell", "FIXTURE_FIRST", "Keeps material time kinds distinct and visible.", "time_banner", "time freshness temporal"],
  ["map-runtime", "Map evidence bridge", "Map and layers", "VERIFIED_SLICE", "Renderer-neutral selection to governed Evidence Drawer resolution.", "map_runtime", "map selection evidence"],
  ["domains", "Domain explorer", "Map and layers", "DOCUMENTED", "Navigation boundary for thirteen Kansas knowledge domains.", "domains", "domains knowledge Kansas"],
  ["layer-catalog", "Layer Catalog", "Map and layers", "DOCUMENTED", "Layer discovery with release, rights, time, and evidence context.", "layer_catalog", "layers legend catalog"],
  ["layer-lineage", "Layer lineage timeline", "Map and layers", "FIXTURE_FIRST", "Correction, supersession, derivation, and release lineage.", "layer_lineage_timeline", "lineage correction history"],
  ["huc-crosswalk", "HUC crosswalk explorer", "Map and layers", "FIXTURE_FIRST", "Bounded watershed identifier and crosswalk inspection.", "huc_crosswalk_explorer", "hydrology huc watershed"],
  ["pmtiles-diagnostics", "PMTiles range diagnostics", "Map and layers", "FIXTURE_FIRST", "Archive, range, index, and render verification for governed artifacts.", "pmtiles_range_diagnostics", "pmtiles tiles range"],
  ["stac-inspector", "STAC conformance inspector", "Map and layers", "FIXTURE_FIRST", "Read-only release-facing STAC metadata inspection.", "stac_conformance_inspector", "stac catalog metadata"],
  ["view-registry", "View registry inspector", "Map and layers", "FIXTURE_FIRST", "Read-only inspection of governed view projections.", "view_registry_inspector", "view registry projection"],
  ["maplibre-runtime", "MapLibre browser runtime", "Map and layers", "HOLD", "The package-owned adapter is present; Explorer activation and authenticated browser proof remain open.", "packages/maplibre", "maplibre renderer adapter hold"],
  ["evidence-drawer", "Evidence Drawer", "Evidence and trust", "VERIFIED_SLICE", "Keyboard-operable evidence, citation, limitation, and correction inspection.", "evidence_drawer", "evidence citations correction"],
  ["evidence-tooltip", "Evidence tooltip", "Evidence and trust", "FIXTURE_FIRST", "Compact finite evidence support summary.", "evidence_tooltip", "evidence tooltip support"],
  ["citation-pill", "Citation pill", "Evidence and trust", "FIXTURE_FIRST", "Compact citation status and resolution affordance.", "citation_pill", "citation source support"],
  ["provenance-citations", "Provenance citations", "Evidence and trust", "FIXTURE_FIRST", "Bounded provenance and citation projection.", "provenance_citations", "provenance citations lineage"],
  ["attestation-badge", "Attestation badge", "Evidence and trust", "FIXTURE_FIRST", "Attestation status without replacing evidence or review authority.", "attestation_badge", "attestation verification trust"],
  ["consent-card", "Consent card", "Evidence and trust", "FIXTURE_FIRST", "Visible consent, permission, and rights context.", "consent_card", "consent rights policy"],
  ["denial-reason", "Denial reason explorer", "Evidence and trust", "FIXTURE_FIRST", "Safe fixed-copy denial explanations without protected-detail leakage.", "denial_reason_explorer", "deny restricted policy"],
  ["redaction-preview", "Redaction preview", "Evidence and trust", "FIXTURE_FIRST", "Shows governed generalization without reconstructing protected detail.", "redaction_preview", "redaction privacy generalization"],
  ["reveal-session", "Reveal session", "Evidence and trust", "FIXTURE_FIRST", "Bounded reveal-state projection with purpose and duration visible.", "reveal_session", "reveal access session"],
  ["air-quality", "Air quality trigger panel", "Environmental insight", "FIXTURE_FIRST", "Finite trigger projection for governed air-quality observations.", "air_quality_trigger_panel", "atmosphere air quality"],
  ["environmental-cadence", "County environmental cadence", "Environmental insight", "FIXTURE_FIRST", "County-scale observation and freshness cadence.", "county_environmental_cadence_calendar", "county calendar environment"],
  ["ndvi-change", "County NDVI change panel", "Environmental insight", "FIXTURE_FIRST", "Bounded vegetation-change projection with limitations.", "county_ndvi_change_panel", "ndvi vegetation change"],
  ["anomaly-scorecard", "Environmental anomaly scorecard", "Environmental insight", "FIXTURE_FIRST", "Evidence-bounded anomaly summary with finite outcomes.", "environmental_anomaly_scorecard", "anomaly environment evidence"],
  ["soil-change", "Soil yearly change viewer", "Environmental insight", "FIXTURE_FIRST", "Year-over-year soil projection preserving component and horizon identity.", "soil_yearly_change_viewer", "soil yearly horizon"],
  ["streamflow-qc", "Streamflow quality dashboard", "Environmental insight", "FIXTURE_FIRST", "Quality, freshness, and correction state for streamflow observations.", "streamflow_qc_dashboard", "streamflow hydrology quality"],
  ["source-watchlist", "Source availability watchlist", "Environmental insight", "FIXTURE_FIRST", "Availability and staleness visibility without source activation.", "source_availability_watchlist", "source availability stale"],
  ["promotion-gate", "Promotion gate status board", "Governance and operations", "FIXTURE_FIRST", "Read-only gate, blocker, receipt, and non-effect status.", "promotion_gate_status_board", "promotion gate release"],
  ["oci-browser", "OCI artifact browser", "Governance and operations", "FIXTURE_FIRST", "Read-only bounded artifact and integrity metadata.", "oci_artifact_browser", "oci artifact integrity"],
  ["watcher-registry", "Watcher registry browser", "Governance and operations", "FIXTURE_FIRST", "Watcher inventory preserving the watcher-is-not-publisher rule.", "watcher_registry_browser", "watcher registry monitoring"],
  ["review-console", "Review Console read-only", "Governance and operations", "DOCUMENTED", "Review projection that cannot mutate lifecycle or decisions.", "review_console_readonly", "review readonly audit"],
  ["focus-panel", "Focus panel", "User workflows", "FIXTURE_FIRST", "Evidence-bounded synthesis with finite outcomes and no browser model authority.", "focus_panel", "focus AI evidence"],
  ["story-player", "Story Player", "User workflows", "FIXTURE_FIRST", "Playback of already-governed public-safe story projections.", "story_player", "story narrative map"],
  ["compare", "Compare", "User workflows", "DOCUMENTED", "Comparison boundary for evidence, time, rights, and corrections.", "compare", "compare time layers"],
  ["export", "Governed export", "User workflows", "DOCUMENTED", "Export boundary preserving citations, rights, redaction, and release context.", "export", "export citations rights"],
  ["settings", "Settings", "User workflows", "DOCUMENTED", "Display and accessibility preferences that cannot weaken policy.", "settings", "settings accessibility preferences"],
  ["diagnostics", "Safe diagnostics", "User workflows", "DOCUMENTED", "Redacted diagnostics excluding secrets and protected internals.", "diagnostics", "diagnostics health redaction"],
];

export const FEATURE_CATALOG: readonly FeatureEntry[] = Object.freeze(
  rows.map(([id, name, area, maturity, summary, childPath, keywords]) =>
    Object.freeze({
      id,
      name,
      area,
      maturity,
      summary,
      path: childPath.startsWith("packages/")
        ? childPath
        : `apps/explorer-web/src/features/${childPath}`,
      keywords: Object.freeze(keywords.split(" ")),
    }),
  ),
);

export type KnowledgeDomain = Readonly<{
  id: string;
  name: string;
  summary: string;
  safeguard: string;
  path: string;
}>;
type DomainRow = readonly [string, string, string, string];
const domainRows: readonly DomainRow[] = [
  ["agriculture", "Agriculture", "Crops, land use, production context, and agricultural change.", "Do not infer farm-level claims from generalized layers."],
  ["archaeology", "Archaeology", "Cultural-resource and material-history context.", "Sensitive locations default to restriction or generalization."],
  ["atmosphere", "Atmosphere", "Weather, climate, air quality, and atmospheric observations.", "Observation and validity time must remain distinct."],
  ["fauna", "Fauna", "Species observations, movement, and ecological relationships.", "Protected-species locations may be obscured or denied."],
  ["flora", "Flora", "Vegetation, native plants, invasives, and plant communities.", "Preserve source scale and observation limitations."],
  ["geology", "Geology", "Bedrock, surficial geology, landforms, and mineral context.", "General context is not a site investigation."],
  ["habitat", "Habitat", "Biotopes, ecological connectivity, and environmental relationships.", "Derived suitability is not direct observation."],
  ["hazards", "Hazards", "Drought, flood, wildfire, severe weather, and exposure context.", "Never replace emergency or authoritative current guidance."],
  ["hydrology", "Hydrology", "Watersheds, streams, flow, water supply, and drought observations.", "A map selection scopes a request; it is not flow evidence."],
  ["people_dna_land", "People, DNA, and land", "Community, genealogy, identity-adjacent, and land context.", "Default deny for protected personal or genetic detail."],
  ["roads_rail_trade", "Roads, rail, and trade", "Networks, corridors, movement, and economic connections.", "Do not expose restricted operational detail."],
  ["settlements_infrastructure", "Settlements and infrastructure", "Communities, services, facilities, and the built environment.", "Public context must not become an operational blueprint."],
  ["soil", "Soil", "Soil units, components, horizons, properties, condition, and change.", "Do not collapse component, horizon, method, or time identity."],
];
export const KNOWLEDGE_DOMAINS: readonly KnowledgeDomain[] = Object.freeze(
  domainRows.map(([id, name, summary, safeguard]) =>
    Object.freeze({
      id,
      name,
      summary,
      safeguard,
      path: `apps/explorer-web/src/features/domains/${id}`,
    }),
  ),
);

export type KnowledgePrinciple = Readonly<{ id: string; name: string; summary: string }>;
export const KNOWLEDGE_PRINCIPLES: readonly KnowledgePrinciple[] = Object.freeze([
  ["evidence", "Evidence first", "EvidenceBundle-derived support outranks generated language; cite the support or abstain."],
  ["outcomes", "Finite outcomes", "Claim-bearing views resolve to ANSWER, ABSTAIN, DENY, or ERROR."],
  ["membrane", "Governed trust membrane", "Public clients consume governed responses or released public-safe artifacts."],
  ["time", "Time-aware", "Observed, valid, source, retrieval, release, correction, and freshness time stay distinct."],
  ["correction", "Correctable and reversible", "Correction, supersession, withdrawal, receipts, proofs, and rollback remain visible."],
  ["map", "The map is not proof", "Rendered geometry and properties scope a governed request; they do not establish truth."],
  ["accessibility", "Accessible trust", "Status uses text, keyboard paths, focus behavior, and non-map alternatives—not color alone."],
  ["renderer", "One renderer seam", "Explorer remains renderer-neutral while the admitted MapLibre runtime stays behind one KFM-owned boundary."],
].map(([id, name, summary]) => Object.freeze({ id, name, summary })));

export type FeatureQuery = Readonly<{
  text?: string;
  area?: FeatureArea | "ALL";
  maturity?: FeatureMaturity | "ALL";
}>;
const normalize = (value: string): string => value.trim().toLocaleLowerCase();
export function filterFeatures(query: FeatureQuery = {}): readonly FeatureEntry[] {
  const text = normalize(query.text ?? "");
  return FEATURE_CATALOG.filter((entry) => {
    if (query.area && query.area !== "ALL" && entry.area !== query.area) return false;
    if (query.maturity && query.maturity !== "ALL" && entry.maturity !== query.maturity) return false;
    if (!text) return true;
    return normalize([entry.name, entry.area, entry.maturity, entry.summary, entry.path, ...entry.keywords].join(" ")).includes(text);
  });
}
export function findDomain(id: string): KnowledgeDomain | null {
  return KNOWLEDGE_DOMAINS.find((entry) => entry.id === id) ?? null;
}
export function repositoryUrl(path: string): string {
  const encoded = path.split("/").map(encodeURIComponent).join("/");
  return `https://github.com/${REPOSITORY_SNAPSHOT.repository}/tree/${REPOSITORY_SNAPSHOT.commit}/${encoded}`;
}
