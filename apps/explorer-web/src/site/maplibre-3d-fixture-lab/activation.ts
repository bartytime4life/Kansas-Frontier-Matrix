export const MAPLIBRE_3D_FIXTURE_QUERY_PARAMETER =
  "kfm-maplibre-3d-fixture";
export const MAPLIBRE_3D_FIXTURE_QUERY_VALUE = "1";

export function isMapLibre3DFixtureLabEnabled(
  input: string | URL,
): boolean {
  const url =
    input instanceof URL
      ? input
      : new URL(input, "https://kfm.invalid/");
  return (
    url.searchParams.get(MAPLIBRE_3D_FIXTURE_QUERY_PARAMETER) ===
    MAPLIBRE_3D_FIXTURE_QUERY_VALUE
  );
}
