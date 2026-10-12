<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/catalog-distribution-mapping-profile-source-map
title: Catalog Distribution Mapping Profile Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Catalog steward · Provenance steward · Release steward · Contract steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: source-grounded adaptation of STAC/DCAT/PROV distribution cross-mapping into a bounded fixture-only candidate
truth_posture: CONFIRMED source transcription and repository comparison / PROPOSED bounded adaptation pending review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/data/catalog_distribution_mapping_profile.md
  - ../../../contracts/data/catalog_matrix_closure_profile.md
  - ../../../contracts/data/catalog_trust_extension.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, atlas, stac, dcat, prov, catalog, distribution, provenance, source-map]
[/KFM_META_BLOCK_V2] -->

# Catalog Distribution Mapping Profile Source Map

## Source lineage

| Source | Confirmed contribution | Boundary |
|---|---|---|
| Google Drive `KFM_Full_Atlas_seed_cards`, document `1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho` | The `STAC DCAT PROV Distribution Cross-Mapping Pattern` proposes that a STAC PMTiles asset `href`, a DCAT distribution `accessURL`, and PROV generation/attribution reference the same digest-bound artifact; it also proposes cross-standard tests and a manifest carrying the three record references. | Proposal register, not proof of a catalog, registry, artifact, attestation, release, or publication. |
| Attached `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, SHA-256 `efc0d159761581b5ae043c607dfa28bbc58b3ca5423c9d18a659e650271d73b9`, page 351 | `KFM-P18-INV-047` requires explicit STAC/DCAT/PROV asset roles and checksums for renderable vector, raster, tile, and metadata artifacts. | `EXPANDED` and `PROPOSED`; the card explicitly states catalog metadata is not sovereign truth without evidence and policy. |
| Repository `main` at `7335ed9ea0f81342ae0b1c7828a21ac74711c78b` | The existing CatalogMatrix closure profile aligns artifact ID, digest, and release reference; the catalog-trust extension carries common trust fields. | Neither existing packet cross-checks locator/access URL/entity location, media type, role, and PROV generation identity as one bounded tuple. |

## Repository reconciliation

GitHub was inspected on 2026-08-09. There were no open pull requests, and
recent merged catalog work covered matrix closure, catalog health, trust-field
carriage, and STAC search behavior. Live `main` did not contain
`CatalogDistributionMappingProfileCandidate`, its schema, fixtures, validator,
tests, workflow, source map, or receipt.

The packet therefore fills a field-level mapping gap without duplicating the
existing matrix-closure tuple. It introduces no STAC Item, DCAT Distribution,
PROV Bundle, TileArtifactManifest, registry client, artifact bytes, network
transport, OCI/ORAS activation, credential path, or publication surface.

## Bounded adaptation

| Source pressure | Retained behavior | Held boundary |
|---|---|---|
| One digest-bound locator across standards | STAC `href`, DCAT `access_url`, and PROV `location` must equal one synthetic artifact locator. | The URN is never dereferenced; OCI/ORAS and registry selection remain inactive. |
| Explicit roles and media types | Each carrier must repeat the artifact role and media type exactly. | This does not replace each standard's native vocabulary or create a production crosswalk. |
| Checksums are mandatory | Every carrier repeats the canonical SHA-256 digest, and the locator's digest suffix must agree. | Digest agreement is integrity evidence only, not truth or release authority. |
| PROV generation and attribution | The generated entity must equal the declared entity; generation activity and attributed agent references are required. | References are synthetic and are not resolved or authenticated. |
| Cross-standard tests | Exact positive and polarity fixtures exercise every carrier and summary field. | Fixture PASS remains `REVIEW_REQUIRED`; no records are emitted. |

## Path decision

~~~yaml
path_decision:
  artifact: CatalogDistributionMappingProfileCandidate
  proposed_path: contracts/data/catalog_distribution_mapping_profile.md
  artifact_kind: semantic contract
  authority_owner: fixture-only standards-carrier alignment meaning
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: data
  scope_id: catalog-distribution-mapping
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - contracts/data/catalog_matrix_closure_profile.md
    - contracts/data/catalog_trust_extension.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-SIGNATURE-002
    - DIR-PLACE-001
    - DIR-DEP-001
  outcome: PLACE
~~~

The semantic contract belongs in the established `contracts/data/` catalog
lane. Machine shape, examples, enforcement, tests, CI, source lineage, and the
authoring receipt stay in their distinct responsibility roots.

## Non-effects

This packet does not fetch, discover, upload, sign, attest, register, emit,
mutate, release, deploy, publish, or dereference an artifact or catalog record;
activate OCI or ORAS; read lifecycle-private stores; resolve evidence; decide
policy; approve review; alter an allowlist or manifest; or authorize public
use.
