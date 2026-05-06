# Root Surface Compatibility Register

Source of truth: `control_plane/root_surface_register.yaml`.

## Purpose
Classify each repository root surface for governance and compatibility handling, including enforcement roots.

## Allowed classes
- canonical
- compatibility
- transitional
- generated
- data-lifecycle
- release/proof
- runtime
- policy
- UNKNOWN

## Cross-links (required)
The register explicitly cross-links these surfaces:
- `.github`, `docs`, `control_plane`, `contracts`, `schemas`, `policy`, `policies`, `ui`, `web`, `jsonschema`, `styles`, `viewer_templates`.

## Notes
- Some cross-linked compatibility/transitional roots may be absent in current checkout.
- Absent roots are tracked for compatibility governance, not as active canonical roots.
