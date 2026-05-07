## 1. Purpose
Fixture-backed USDA PLANTS catalog closure, evidence-linking, and release-candidate artifacts.
## 2. Lifecycle placement
PROCESSED -> CATALOG/TRIPLET -> release candidate (not published).
## 3. Why this layer is not publication
No promotion or publication claims; publication gate remains blocked.
## 4. Evidence-link model
Dedicated non-occurrence evidence-link contract with source, rights, lineage, and decision.
## 5. Catalog model
Deterministic usda_plants_catalog plus dcat_like, stac_like, and prov_like companion files.
## 6. Release-candidate model
Release candidate manifest with blockers and not_promoted/not_published states.
## 7. Evidence Drawer DTO contract
UI-safe payloads: no raw fixture contents, no coordinates, no geometry.
## 8. MapLibre layer contract
Draft wiring contract only; currently_available=false; future FIPS join.
## 9. Policy gates
Additional Rego gates validate closure, states, leak prevention, and publication blocking.
## 10. CI expectations
Pytest coverage for builders and deterministic fixed generated_at runs.
## 11. What is intentionally not implemented
This layer does not download USDA PLANTS data.
This layer does not publish a public map.
This layer does not generate county geometries.
This layer does not promote a release.
This layer only proves catalog closure and release-candidate readiness for fixture-backed USDA PLANTS records.
## 12. Future work
Live USDA ingestion remains future work.
Actual county geometry joins remain future work.
Public map publication remains future work.
