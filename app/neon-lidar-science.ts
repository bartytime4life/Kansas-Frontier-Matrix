/** One reusable science view of the validated dev-backed raster. No I/O or source admission. */
import { parseNeonPilotReceipt } from "./neon-lidar-pilot-client";
import { neonLidarProbe } from "./neon-lidar-preview";

export type NeonScienceRow = {
  id: string; name: string; row: number; column: number; sample_set: string;
  easting_m: number; northing_m: number;
  dtm_m: number | null; dsm_m: number | null; chm_m: number | null;
  surface_above_ground_m: number | null;
  difference_status: "valid" | "missing" | "negative" | "nonfinite";
};
export type NeonScienceColumn = {
  key: keyof NeonScienceRow; label: string; type: "number" | "string";
  unit?: string; displayDigits?: number; metric?: boolean; analysis?: boolean;
};
const LIDAR_METHODS = "https://www.neonscience.org/data-collection/lidar";
const LIMITS = [
  "These are regularly spaced preview samples from one historical 1 km tile, not the complete native raster or a random sample of Kansas.",
  "Each display cell retains one nearest native 1 m sample. A 10 m display footprint is not a measured vegetation area, cell average or cell maximum.",
  "Adjacent samples are spatially dependent. Correlations and fitted lines describe these selected pairs; they do not establish independent observations, causation or statistical significance.",
  "DSM minus DTM is calculated from those two inputs and can be arithmetically correlated with them. It includes structures and is not the independent provider canopy product.",
  "Provider canopy outliers remain under review. A preview maximum cannot replace the native maximum, and zero canopy does not establish bare ground.",
  "Recorded reference systems do not establish horizontal or vertical accuracy. No frame, epoch, height-datum or unit conversion is performed.",
  "No species, biomass, carbon, growth, change, field accuracy or admitted KFM evidence is inferred. Display precision is not measurement accuracy.",
];
const COLUMNS: NeonScienceColumn[] = [
  { key: "row", label: "Grid row · north to south", type: "number", displayDigits: 0, metric: false, analysis: false },
  { key: "column", label: "Grid column · west to east", type: "number", displayDigits: 0, metric: false, analysis: false },
  { key: "easting_m", label: "Nearest native sample easting", type: "number", unit: "m", displayDigits: 1, metric: false, analysis: false },
  { key: "northing_m", label: "Nearest native sample northing", type: "number", unit: "m", displayDigits: 1, metric: false, analysis: false },
  { key: "dtm_m", label: "Ground elevation · DTM", type: "number", unit: "m", displayDigits: 2 },
  { key: "dsm_m", label: "Surface elevation · DSM", type: "number", unit: "m", displayDigits: 2 },
  { key: "chm_m", label: "Provider canopy · CHM", type: "number", unit: "m", displayDigits: 2 },
  { key: "surface_above_ground_m", label: "Surface minus ground · DSM − DTM", type: "number", unit: "m", displayDigits: 2 },
  { key: "sample_set", label: "Sample set", type: "string", metric: false, analysis: false },
  { key: "difference_status", label: "DSM − DTM quality", type: "string", metric: false, analysis: false },
];

export function createNeonScienceDataset(input: unknown) {
  const receipt = parseNeonPilotReceipt(input);
  if (!receipt) return null;
  const { preview, review, cache } = receipt;
  const { source, grid } = preview;
  const id = `neon-${source.site.toLowerCase()}-${source.month}-${source.tile}-${source.release}`;
  const sampleSet = `${source.site} · ${source.acquisition_run}`;
  const records: NeonScienceRow[] = [];
  for (let row = 0; row < grid.height; row++) for (let column = 0; column < grid.width; column++) {
    const probe = neonLidarProbe(preview, row, column);
    // The receipt parser guarantees integral bounded grids; keep this fail-closed guard for other callers.
    if (!probe) return null;
    const issue = probe.differenceIssue;
    if (issue !== null && issue !== "missing" && issue !== "negative" && issue !== "nonfinite") return null;
    records.push({
      id: `${id}:r${row + 1}:c${column + 1}`, name: `Row ${row + 1} · column ${column + 1}`,
      row: row + 1, column: column + 1, sample_set: sampleSet,
      easting_m: probe.easting, northing_m: probe.northing,
      dtm_m: probe.dtm, dsm_m: probe.dsm, chm_m: probe.chm,
      surface_above_ground_m: probe.surfaceAboveGround,
      difference_status: issue ?? "valid",
    });
  }
  const sourceSnapshots = source.files.map(file => ({
    kind: file.kind, name: file.name, product: file.product, bytes: file.bytes,
    rawSha256: file.sha256, retrievedAt: null, queryUrl: null,
  }));
  const analysisContext = {
    format: "kfm-neon-analysis-context-v1", dataset_id: id,
    source: {
      site: source.site, catalog_month: source.month, acquisition_run: source.acquisition_run,
      release: source.release, tile: source.tile,
    },
    sampling: {
      source_resolution_m: grid.source_resolution_m, display_resolution_m: grid.preview_resolution_m,
      width: grid.width, height: grid.height, method: "nearest native sample to each display-cell center",
      rows: records.length, zero_is_not_missing: true, no_data: null,
      coordinate_kind: "native projected sample center; row and column are one-based",
    },
    references: {
      horizontal_crs_reference: "Full recorded CRS is in the dataset JSON; source file identities are retained in snapshot_sha256.",
      vertical_reference: source.vertical_reference,
      coordinate_epoch: null, horizontal_accuracy_m: null,
      height_values_transformed: false, canopy_floor_m: source.canopy_floor_m,
    },
    time: {
      observation_date: null, original_file_retrieval_times: null,
      preview_prepared_at: preview.generated_at, package_prepared_at: receipt.generatedAt,
      cache: { ...cache },
    },
    review: {
      status: review.status, scientific_accuracy_verified: false, source_admitted: false,
      canopy_native_max_m: review.canopy_native_max_m,
      canopy_native_cells_above_50m: review.canopy_native_cells_above_50m,
      surface_minus_ground_native_max_m: review.surface_minus_ground_native_max_m,
    },
    interpretation: {
      spatially_independent_samples: false, representative_of_native_population: false,
      provider_canopy_equals_dsm_minus_dtm: false, zero_canopy_proves_bare_ground: false,
      area_species_biomass_carbon_or_change_estimated: false,
      full_source_metadata_and_limits: "Retained in the source-linked dataset JSON, not duplicated in every CSV row.",
    },
  };
  const bundle = {
    format: "kfm-neon-science-records-v1", id, story: "neon-terrain", built_at: receipt.generatedAt,
    sources: [{ name: "National Ecological Observatory Network (NEON)", url: LIDAR_METHODS, citation: source.attribution }],
    observed: { from: null, to: null },
    data: {
      title: "Konza Prairie · terrain & vegetation samples",
      description: "Read the ground, surface and independent provider canopy at the same sampled places. Compare distributions and descriptive relationships without changing the source values.",
      recordKind: "raster-sample", sourceLabel: "PROVIDER PREVIEW · REVIEW PENDING",
      coverage: `${grid.width} × ${grid.height} preview samples across one 1 km tile. Catalog month ${source.month}; run ${source.acquisition_run}; ${source.release}. Exact observation dates are not supplied here.`,
      columns: COLUMNS.map(column => ({ ...column })), records,
      valueField: "chm_m", categoryField: "sample_set", preferredView: "chart",
      sourceSnapshots, analysisContext, limits: [...LIMITS, ...review.notes],
    },
  };
  return { format: "kfm-neon-science-v1" as const, id, receipt, bundle };
}
export type NeonScienceDataset = NonNullable<ReturnType<typeof createNeonScienceDataset>>;

/** Portable, source-linked data for another KFM tool. Cache time never becomes observation time. */
export function neonScienceDatasetJSON(dataset: NeonScienceDataset): string {
  // Revalidate at the export boundary and regenerate derived rows instead of trusting a modified bundle.
  const current = createNeonScienceDataset(dataset.receipt);
  if (!current) throw new Error("The NEON science dataset is no longer valid.");
  return JSON.stringify(current, null, 2) + "\n";
}
