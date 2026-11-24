import { KANSAS_LIDAR_SOURCE_CATALOG, LIDAR_CATALOG_CHECKED_AT, LIDAR_COMPARISON_REQUIREMENTS } from "../../../lidar-source-catalog";

/** Public source metadata only. No provider acquisition or file serving. */
export function GET() {
  return Response.json({
    format: "kfm-lidar-sources-v1",
    coveragePriority: "kansas",
    catalogCheckedAt: LIDAR_CATALOG_CHECKED_AT,
    scope: "Source families and implementation readiness; not an exhaustive survey, native file or installed dataset inventory.",
    sourceFamilies: KANSAS_LIDAR_SOURCE_CATALOG,
    comparisonRequirements: LIDAR_COMPARISON_REQUIREMENTS,
  }, { headers: { "Cache-Control": "public, max-age=900, s-maxage=3600", "X-Content-Type-Options": "nosniff" } });
}
