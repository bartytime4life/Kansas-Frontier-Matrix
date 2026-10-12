# IIIF historic-overlay readiness — source map

Status: `PROPOSED_INACTIVE`

## Repository evidence mined

The implementation adapts the existing KFM conformance posture in `docs/standards/IIIF.md`.
That standard currently records:

- IIIF Image API 3.0 and Presentation API 3.0 as the preferred new-work baseline;
- legacy 2.1.1 as admissible input that must be recorded as served rather than silently coerced;
- Presentation 4.0 preview as monitor-only;
- the Georeference Extension / Allmaps path as interpretive georeference evidence, not authority;
- exact annotation digest, GCP, resource-mask, transform, rights, CARE, plugin allowlist,
  no-public-RAW-path, EvidenceBundle, citation, and rollback expectations;
- negative-state coverage as an implementation backlog; and
- build / CI as TODO.

Repository search at authoring time found no indexed `historic_overlay_manifest`,
`WarpedMapLayer`, or executable IIIF readiness validator.

## Adaptation

This slice implements only the deterministic, fixture-only portion of that checklist.
It deliberately does not create the proposed independent `historic_overlay_manifest`
object family, because doing so would widen object-family governance and migration scope.

The assessment instead carries a bounded overlay declaration and produces finite
`READY`, `HOLD`, `DENY`, or `ERROR` results.

## Deferred

- live IIIF response capture and JSON-LD validation;
- a canonical historic-overlay object family;
- georeference execution and transform-quality measurement;
- rights / CARE policy evaluation and consent authentication;
- plugin runtime integration;
- EvidenceBundle resolution;
- release-manifest, Story Node, Evidence Drawer, and rollback integration.
