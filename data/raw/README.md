<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/readme
title: data/raw/ — Immutable Source Capture
type: data-lifecycle-readme
version: v0.2.4
prior_version: v0.2.3
status: repository-grounded draft; source-first identity required; physical placement and payload/runtime enforcement unverified
owners: NEEDS VERIFICATION — source and data stewards
created: 2025-09-17
updated: 2026-10-11
supersedes: prior README at the same path; no payload, lifecycle, release, runtime, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: "restricted-review; no-direct-public-path; release-gated"
current_path: data/raw/README.md
owning_root: data/
responsibility: Own the canonical RAW lifecycle boundary while requiring one source-first capture identity, preventing duplicated domain-scoped RAW bytes, and leaving exact physical capture placement and legacy domain-lane disposition to an accepted migration decision.
review_packet_id: kfm-data-parent-wave-20260724
truth_posture: CONFIRMED exact path, accepted Directory Rules rule DIR-SOURCE-001 requiring source-first capture identity, parent data-root contract, and tracked documentation-only topology (52 README files and 6 .gitkeep markers, no payload files at main@9e8bf3e6) / CONFIRMED a domain directory does not authorize a second physical capture / CONFIRMED child READMEs reconciled to the source-first contract on 2026-10-11 / HOLD exact physical source-first placement and legacy domain-lane migration or reference contracts / UNKNOWN external or untracked payloads, active writers/consumers, runtime, release, hosting, and public effects / NEEDS VERIFICATION owners, enforcement, retention, correction propagation, cache invalidation, and rollback drills
evidence_snapshot_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_snapshot_base_commit: b125a21e83f727c45a2d36709bbb594d38a904ad
evidence_snapshot_review_branch: agent/modernize-data-readme-20260724-v3
evidence_snapshot_parent_commit: 0cfcb790ee461e16a4e2cebb30c37dc588bd0c2f
evidence_snapshot_prior_blob: 771a4684341622aa684a3724f0c1a95b900f7335
evidence_snapshot_directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
evidence_snapshot_method: exact parent README read plus carried-forward child/path evidence; no recursive clone or runtime inspection
reconciliation_snapshot_base_commit: 8739edbfecabbde6367a2084740b6c94f07a0425
reconciliation_snapshot_target_prior_blob: 46dd82857f5e881452f39580ffa73bfc9a43b7c8
reconciliation_snapshot_directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
reconciliation_snapshot_adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
reconciliation_snapshot_scope: "Same-path correction of the RAW operating contract and domain-lane interpretation only; no path, payload, writer, descriptor, lifecycle object, runtime, or public state changes."
subtree_refresh_base_commit: 9e8bf3e62bf4b1f4c2e9e30570195132ec7a9475
subtree_refresh_prior_blob: 570ad3c66878ea618f43c13c077ff53776d1cbdb
subtree_refresh_method: recursive tracked-file inventory of data/raw plus required meta-block and link checks over every README in the subtree; no external store, runtime, or writer inspection
notes:
  - "The 2026-10-11 subtree refresh reconciles every child README to the source-first contract, normalizes all subtree metadata to the required meta-block profile, records the tracked documentation-only inventory, and links the full child-lane index; it does not select a physical RAW home, admit a source, or move, add, or delete payloads."
  - "The 2026-09-24 readback adds the exact-schema quarantine-only owner decision and corrects the displayed version; it does not authorize RAW placement or promotion."
  - "The 2026-09-21 readback distinguishes the external local-data QUARANTINE capture from this repository's held RAW placement; it does not admit a source or select a physical RAW home."
  - "The first twelve H2 sections follow Directory Rules section 15 exactly."
  - "Markdown-only parent-lane convergence; no payload or operational state changed."
  - "v0.2.1 removes a domain-first physical-path prescription that conflicted with accepted DIR-SOURCE-001. Exact source-first physical placement and legacy child-lane disposition remain HOLD."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `data/raw/` — Immutable Source Capture

> **One-line purpose.** Own immutable source captures or immutable source references plus the admission and retrieval context required to preserve source identity, role, rights, sensitivity, time, and integrity before normalization.

[![Status: grounded draft](https://img.shields.io/badge/status-grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: Canonical](https://img.shields.io/badge/authority-canonical-0969da?style=flat-square)](#authority-level)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](#validation)

> [!IMPORTANT]
> Path placement, a generated derivative, a successful check, a pull request, or a merge does not create truth, evidence closure, policy permission, release approval, or KFM publication.

> [!WARNING]
> Secrets and restricted or harmful-precision material require approved storage and access controls outside ordinary public-repository paths.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Operating contract](#operating-contract) · [Children](#current-bounded-child-lane-index) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

Own immutable source captures or immutable source references plus the admission and retrieval context required to preserve source identity, role, rights, sensitivity, time, and integrity before normalization.

Artifacts here may carry or support inspectable claims, but directory placement cannot make a claim true, rights-cleared, policy-admitted, reviewed, released, or public.

## Authority level

**Canonical; RAW responsibility.**

This path does not own object meaning, machine shape, policy, release decisions, public serving, or factual truth. Those remain under `contracts/`, `schemas/`, `policy/`, `release/`, and governed delivery interfaces.

Accepted Directory Rules rule `DIR-SOURCE-001` governs capture identity: one source-first capture may support several domains without duplicated RAW bytes. This README cannot select an exact physical source-first path until an accepted placement and migration decision establishes one.

## Status

| Field | Bounded result |
|---|---|
| Path | `data/raw/` |
| Version | `v0.2.4` |
| Prior blob | `570ad3c66878ea618f43c13c077ff53776d1cbdb` (v0.2.3) |
| Evidence base | Original v0.2.0 snapshot retained in metadata; source-first reconciliation at `main@8739edbfecabbde6367a2084740b6c94f07a0425`; external quarantine decision readback at `main@bb08d3e9b9`; subtree refresh at `main@9e8bf3e62bf4b1f4c2e9e30570195132ec7a9475` |
| Tracked subtree inventory | `CONFIRMED` documentation only: 52 `README.md` files and 6 `.gitkeep` markers; no tracked payload files at `main@9e8bf3e6` |
| External, untracked, or LFS payload inventory | `UNKNOWN` |
| Active writers/consumers | `UNKNOWN` |
| Public readiness | `DENY BY DEFAULT` |

### Current local capture boundary

At `main@32ab26478b7186bd1a0983951c1a4fbf5adf33aa` (2026-09-21), [`tools/local_data/`](../../tools/local_data/README.md) provides `doctor`, `init`, `plan`, `sync`, and `verify` for explicitly selected files already on an operator's computer. Its store is private and **outside** the Git checkout. `init` prepares empty lifecycle destinations there, including `data/raw/`; `sync` writes source-first objects and immutable bindings under the external `data/quarantine/<source>/` and process receipts under external `data/receipts/`. It does not write this tracked `data/raw/` tree, activate the `local_upload` connector, or promote captured bytes into RAW.

The [local-PC runbook](../../docs/runbooks/local-pc-data-store.md) supplies a synthetic exercise and backup/readback procedure. Local capture identity and integrity are useful prerequisites, but its source URI, domain label, and receipt do not settle source admission, rights, sensitivity, evidence, release, or a future physical RAW placement. Keep the source-first placement and domain-lane migration **HOLD** until their separate decision and writer contracts exist.

[Owner decision #4613](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4613) accepts the exact manifest schema and contract for private, offline capture into the **external QUARANTINE store**. It does not authorize writing to this tracked RAW lane or promoting captured bytes into RAW.

## What belongs here

- one source-first capture identity for admitted source-native payloads or immutable references;
- retrieval metadata, source-head snapshots, checksums, digests, and capture indexes;
- domain references or projections that point to the source-first capture without duplicating bytes;
- source-role, source-version, observation/source/retrieval-time, rights, sensitivity, and citation sidecars;
- RAW-local README and inventory material that does not become registry, proof, receipt, catalog, or release authority;

Local README, inventory, digest, migration, and disposition sidecars may explain the boundary without creating parallel authority.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| mutable normalization, joins, repairs, redaction trials, or derived candidates | `data/work/` |
| failed, unsafe, rights-unclear, sensitivity-unclear, or invalid material | `data/quarantine/` |
| accepted source descriptors and activation decisions | `data/registry/sources/` or the accepted registry family |
| receipts, proof support, catalog/triplet projections, release decisions, or public artifacts | their dedicated `data/` lanes or `release/` |
| Credentials, private keys, private endpoints, or unsafe logs | Approved secret and restricted operational systems |
| Maps, reports, graphs, indexes, or AI output presented as sovereign truth | Resolve governed evidence/release state or abstain |

## Inputs

Governed connectors and source-admission processes. Connectors may write RAW or QUARANTINE candidates only through an accepted source-first physical placement; a domain lane does not become that placement by convention. Connectors do not publish.

As applicable, inputs must resolve stable identity, source role, space/time scope, rights, sensitivity, contract/schema, code/spec/run, validation/receipt, evidence/proof, policy/review, release, correction, and rollback references.

## Outputs

One source-first immutable capture identity plus governed references or projections for WORK processing or QUARANTINE review. RAW has no direct public-client path.

Public clients must not use an internal or compatibility lane as a direct data service.

## Validation

Validate placement; identity/digest/version; source role and lineage; rights/sensitivity; spatial/temporal support; contract/schema; execution and receipts; evidence/citations/proofs; policy/review; catalog/triplet parity; release/correction/rollback dependencies; links/anchors/metadata; and sensitive-content exposure.

No complete lane-wide validator was verified. A pass proves only the check’s declared scope.

Focused documentation checks from the repository root:

```bash
python tools/validators/docs/link-check/check_links.py data/raw/README.md
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required data/raw/README.md

# whole subtree (every child README)
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required data/raw
git ls-files data/raw | grep -Ev '(README\.md|\.gitkeep)$'   # expect no output while placement is HOLD
```

These commands do not select a physical RAW path, inspect external or restricted payloads, admit a source, exercise a writer, or authorize release or publication.

## Review burden

Accountable ownership remains **NEEDS VERIFICATION**. Changes should include source and data stewards as applicable. Payload, source activation, rights/sensitivity, migration, public-serving, correction, or rollback changes require corresponding specialist and independent review. CODEOWNERS routing is not approval evidence.

## Related folders

- Parent: [`data/`](../README.md)
- Lifecycle: [`raw/`](../raw/README.md) · [`work/`](../work/README.md) · [`quarantine/`](../quarantine/README.md) · [`processed/`](../processed/README.md) · [`catalog/`](../catalog/README.md) · [`triplets/`](../triplets/README.md) · [`published/`](../published/README.md)
- Trust support: [`receipts/`](../receipts/README.md) · [`proofs/`](../proofs/README.md) · [`registry/`](../registry/README.md) · [`rollback/`](../rollback/README.md)
- Authority: [`contracts/`](../../contracts/README.md) · [`schemas/`](../../schemas/README.md) · [`policy/`](../../policy/README.md) · [`release/`](../../release/README.md)
- Doctrine: [Directory Rules](../../docs/doctrine/directory-rules.md) · [Lifecycle Law](../../docs/doctrine/lifecycle-law.md) · [Trust Membrane](../../docs/doctrine/trust-membrane.md)

## ADRs

Relevant proposed decisions include ADR-0001 (schema home), ADR-0011 (receipt/proof/manifest/catalog separation), ADR-0012 (connector output boundary), ADR-0015 (published aliases and rollback split), and ADR-0025 (public clients do not read internal stores). This README accepts none. An accepted ADR plus migration and rollback plan is required before changing a canonical lifecycle family, promoting compatibility, or creating parallel authority.

## Last reviewed

- **Date:** 2026-10-11
- **Evidence boundary:** `main@9e8bf3e62bf4b1f4c2e9e30570195132ec7a9475`
- **Review type:** recursive tracked-file inventory of `data/raw/`, every child README read and reconciled, required meta-block and link checks over the subtree
- **External payload/runtime inspection:** not performed
- **Owners, independent review, retention, and operational rollback:** needs verification

Re-review on authority/topology, writer, policy, release, public-consumer, correction, or rollback changes—or within six months.

## Operating contract

```text
admitted source edge
  -> one registered source_id + one source-first capture identity
  -> accepted physical RAW placement (NEEDS VERIFICATION)
  -> zero or more governed domain references or projections
  -> WORK or QUARANTINE through their owning procedures
```

The accepted rules determine identity, not an exact physical RAW path. Do not infer `data/raw/<domain>/` or any other existing directory as the capture home. Physical placement, writer interfaces, reference shape, migration, deduplication, readback, and rollback require a separate accepted decision.

Every transition must preserve immutable input identity, source role, rights/sensitivity posture, temporal context, retrieval context, content digest, and receipt references. A filename, directory, successful fetch, or connector run does not establish source authority or admissibility.

## Current bounded child-lane index

The child directories below are tracked topology, not default physical capture homes. Until an accepted source-first placement and migration decision says otherwise, treat domain lanes as compatibility/reference projections or unresolved legacy paths. Do not create domain-scoped copies of cross-domain captures.

As of the 2026-10-11 subtree refresh, every child README below states that compatibility/reference role and passes the required meta-block profile. A tracked README does not show that payloads, SourceDescriptors, writers, receipts, or enforcement exist.

| Child lane | Tracked sub-lanes | Bounded posture |
|---|---|---|
| [`agriculture/`](agriculture/README.md) | [`usda-nass/`](agriculture/usda-nass/README.md) | Compatibility/reference index; documentation only; payloads and enforcement unverified. |
| [`archaeology/`](archaeology/README.md) | — | Compatibility/reference index; sensitive site-location protections preserved; payloads and enforcement unverified. |
| [`atmosphere/`](atmosphere/README.md) | [`administrative/`](atmosphere/administrative/README.md) · [`aggregate/`](atmosphere/aggregate/README.md) · [`modeled/`](atmosphere/modeled/README.md) ([`cams/`](atmosphere/modeled/cams/README.md), [`hrrr-smoke/`](atmosphere/modeled/hrrr-smoke/README.md)) · [`observed/`](atmosphere/observed/README.md) ([`goes-abi/`](atmosphere/observed/goes-abi/README.md), [`hms/`](atmosphere/observed/hms/README.md), [`viirs/`](atmosphere/observed/viirs/README.md)) · `regulatory/` (`.gitkeep` only) | Source-role compatibility/reference index; documentation only; payloads and enforcement unverified. |
| [`fauna/`](fauna/README.md) | [`ebird/`](fauna/ebird/README.md) · [`eddmaps/`](fauna/eddmaps/README.md) · [`gbif/`](fauna/gbif/README.md) · [`inaturalist/`](fauna/inaturalist/README.md) · [`natureserve/`](fauna/natureserve/README.md) · [`usfws_ecos/`](fauna/usfws_ecos/README.md) | Compatibility/reference index; documentation only; payloads and enforcement unverified. |
| [`flora/`](flora/README.md) | `gbif/` · `inaturalist/` · `natureserve/` · `usfws_ecos/` (`.gitkeep` only) | Source-first-safe compatibility/reference hold; payloads absent and physical capture placement unresolved. |
| [`geology/`](geology/README.md) | — | Compatibility/reference index; exact subsurface protections preserved; payloads and enforcement unverified. |
| [`habitat/`](habitat/README.md) | [`ecoregions/`](habitat/ecoregions/README.md) · [`gap-landfire/`](habitat/gap-landfire/README.md) · [`kdwp/`](habitat/kdwp/README.md) · [`natureserve/`](habitat/natureserve/README.md) · [`nlcd/`](habitat/nlcd/README.md) · [`nwi/`](habitat/nwi/README.md) · [`occurrence-context/`](habitat/occurrence-context/README.md) · [`pad-us/`](habitat/pad-us/README.md) · [`usfws-ecos/`](habitat/usfws-ecos/README.md) | Compatibility/reference index; documentation only; payloads and enforcement unverified. |
| [`hazards/`](hazards/README.md) | [`fema/`](hazards/fema/README.md) · [`firms/`](hazards/firms/README.md) · [`nfhl/`](hazards/nfhl/README.md) | Compatibility/reference index; documentation only; payloads and enforcement unverified. |
| [`hydrology/`](hydrology/README.md) | [`fema_nfhl/`](hydrology/fema_nfhl/README.md) · [`usgs_3dep/`](hydrology/usgs_3dep/README.md) · [`usgs_nhdplus_hr/`](hydrology/usgs_nhdplus_hr/README.md) · [`usgs_water_data/`](hydrology/usgs_water_data/README.md) · [`usgs_wbd/`](hydrology/usgs_wbd/README.md) | Compatibility/reference index; documentation only; payloads and enforcement unverified. |
| [`people/`](people/README.md) | [`dna/`](people/dna/README.md) | Compatibility lane; consent, privacy, and living-person protections preserved; payloads and enforcement unverified. |
| [`people-dna-land/`](people-dna-land/README.md) | [`land-ownership/`](people-dna-land/land-ownership/README.md) | Compatibility/reference index; documentation only; payloads and enforcement unverified. |
| [`roads-rail-trade/`](roads-rail-trade/README.md) | — | Compatibility/reference index; documentation only; payloads and enforcement unverified. |
| [`settlement/`](settlement/README.md) | — | Compatibility lane; documentation only; payloads and enforcement unverified. |
| [`settlements-infrastructure/`](settlements-infrastructure/README.md) | — | Compatibility/reference index; documentation only; payloads and enforcement unverified. |
| [`soil/`](soil/README.md) | — | Compatibility/reference index; documentation only; payloads and enforcement unverified. |
| [`usda-nass/`](usda-nass/README.md) | — | Top-level source-family compatibility lane; documentation only; payloads and enforcement unverified. |

### Overlapping lanes that must share one capture

Several tracked lanes document the same upstream source from different domains. Under `DIR-SOURCE-001` each pair or group resolves to **one** registered `source_id` and **one** source-first capture; the lanes may reference it but must never hold separate copies.

| Upstream source | Overlapping lanes |
|---|---|
| USDA NASS | [`usda-nass/`](usda-nass/README.md) · [`agriculture/usda-nass/`](agriculture/usda-nass/README.md) |
| FEMA NFHL | [`hazards/nfhl/`](hazards/nfhl/README.md) · [`hydrology/fema_nfhl/`](hydrology/fema_nfhl/README.md) |
| NatureServe | [`fauna/natureserve/`](fauna/natureserve/README.md) · [`habitat/natureserve/`](habitat/natureserve/README.md) · `flora/natureserve/` |
| USFWS ECOS | [`fauna/usfws_ecos/`](fauna/usfws_ecos/README.md) · [`habitat/usfws-ecos/`](habitat/usfws-ecos/README.md) · `flora/usfws_ecos/` |
| GBIF / iNaturalist occurrences | [`fauna/gbif/`](fauna/gbif/README.md) · [`fauna/inaturalist/`](fauna/inaturalist/README.md) · `flora/gbif/` · `flora/inaturalist/` · [`habitat/occurrence-context/`](habitat/occurrence-context/README.md) |
| VIIRS active-fire / FIRMS hotspots | [`atmosphere/observed/viirs/`](atmosphere/observed/viirs/README.md) · [`hazards/firms/`](hazards/firms/README.md) — shared capture identity `NEEDS VERIFICATION` |
| USGS 3DEP terrain | [`hydrology/usgs_3dep/`](hydrology/usgs_3dep/README.md) · [`geology/`](geology/README.md) (source-family backlog) |
| Soil and climate-station families (SSURGO, Mesonet, SCAN, USCRN, SMAP) | [`soil/`](soil/README.md) · [`agriculture/`](agriculture/README.md) |
| Settlement sources | [`settlement/`](settlement/README.md) · [`settlements-infrastructure/`](settlements-infrastructure/README.md) |
| People / DNA / land sources | [`people/`](people/README.md) · [`people-dna-land/`](people-dna-land/README.md) |

Which lane names survive, and how references are shaped, remains part of the **HOLD** placement and migration decision.

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Tracked subtree inventory | `CONFIRMED` 2026-10-11 | 52 READMEs plus 6 `.gitkeep` markers, no tracked payloads, at `main@9e8bf3e6`; re-run on any new file under `data/raw/` |
| External, untracked, or LFS payload inventory | `NEEDS VERIFICATION` | Payload families, LFS/external stores, rights/sensitivity, owners |
| Owner placeholders across child READMEs | `NEEDS VERIFICATION` | Named stewards replacing `<...-steward>` placeholders; do not invent owners |
| Source-first physical placement and child-lane disposition | `HOLD` | Accepted path/contract decision, reference shape, migration, deduplication, readback, and rollback |
| Writers and consumers | `UNKNOWN` | Connector, pipeline, tool, runtime, API/UI, workflow, deployed consumer inventory |
| Contract/schema/policy enforcement | `UNKNOWN` | Accepted versions, fixtures, validators, decisions, CI and negative cases |
| Receipt/proof/catalog/release closure | `UNKNOWN` | Emitted instances, identity agreement, review, release and rollback links |
| Public serving/invalidation | `UNKNOWN` | Governed routes, hosting, access, caches, stale/correction/withdrawal, drills |

Unknowns narrow claims and block higher-risk transitions; they do not invite plausible defaults.

## No-loss ledger

| Prior element | Disposition |
|---|---|
| Stable path/document identity | Preserved |
| Core lifecycle or compatibility role | Preserved; source-first identity clarified and domain-first path prescription removed |
| Child-lane index | Preserved; expanded to link every tracked sub-lane and the overlapping-lane groups; omission is not retirement |
| Child README domain content | Preserved; capture-home wording reframed as compatibility/reference wording in the 2026-10-11 refresh |
| Trust membrane and anti-collapse rules | Preserved and strengthened |
| Rights, sensitivity, evidence, policy, release, correction, rollback controls | Preserved |
| Prior blob and rollback target | Recorded |
| Payload, move, deletion, redirect, migration, or public-state change | None |

### Change history

#### v0.2.4 — 2026-10-11

- reconciled every child README under `data/raw/` to the source-first contract: domain and source-family lanes now describe compatibility/reference roles rather than physical capture homes;
- normalized all 52 subtree READMEs to the required meta-block profile (`title`, `owning_root`, `responsibility`, single-token `type`, one-line `truth_posture`, no nested mappings);
- recorded the tracked documentation-only inventory, linked every child and sub-lane, and added an overlapping-lane table for sources documented in more than one domain;
- changed documentation only; physical placement, writers, payloads, runtime, release, and publication remain on hold.

#### v0.2.3 — 2026-09-24

- added the exact-schema, quarantine-only owner decision ([#4613](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4613)) and corrected the displayed version;
- changed documentation only.

#### v0.2.2 — 2026-09-21

- linked the implemented offline local-data workflow and its external QUARANTINE/receipt write boundaries;
- clarified that prepared external RAW directories and local capture receipts do not resolve this tracked RAW lane's placement hold;
- changed documentation only.

#### v0.2.1 — 2026-08-28

- replaced the conflicting domain-first operating path with the accepted source-first identity flow;
- classified domain child lanes as compatibility/reference or unresolved legacy topology rather than default physical capture homes;
- left physical placement, migration, writers, payloads, runtime, release, and publication on hold;
- changed Markdown only.

#### v0.2.0 — 2026-07-24

- normalized the parent README to Directory Rules §15;
- preserved substantive boundaries and explicit uncertainty;
- added validation, review, verification, and no-loss controls;
- changed Markdown only.

[Back to top](#top)
