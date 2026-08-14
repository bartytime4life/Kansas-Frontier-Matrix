<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/kgs-m118-source-descriptor-source-map
title: KGS Map M-118 SourceDescriptor — Source and Repository Reconciliation Map
type: source-map
version: v1.0.0
status: proposed; exploratory; non-canonical; no-source-activation
owners: OWNER_TBD — KGS source steward · Geology steward · Rights reviewer · Validation steward · Docs steward
created: 2026-08-14
updated: 2026-08-14
owning_root: docs/
policy_label: internal; intake; exploratory; geology; kgs; source-descriptor; inactive
responsibility: Reconcile current official KGS Map M-118 metadata and reuse guidance with the repository SourceDescriptor contract, Geology source-role doctrine, registry topology, and connector-placement conflict before creating one inactive source registry candidate.
truth_posture: "CONFIRMED official KGS metadata and current repository evidence at main@103323d7d2916c650e8e9829dd1073ee474d61f0; PROPOSED inactive SourceDescriptor candidate; CONFLICTED official reuse guidance; UNKNOWN legal/steward rights decision, content digest, connector placement, source activation, evidence fitness, release, and public use; NEEDS VERIFICATION hosted exact-head CI and human review"
related:
  - ../../../data/registry/sources/geology/README.md
  - ../../../data/registry/sources/geology/kgs-m118-surficial-geology.source.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../tools/validators/sources/validate_source_descriptor.py
  - ../../domains/geology/SOURCE_ROLE_MATRIX.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# KGS Map M-118 SourceDescriptor — Source and Repository Reconciliation Map

## 1. Decision

`IMPLEMENT_REPOSITORY_SLICE` — add one proposed, inactive `SourceDescriptor`
registry record for KGS Map M-118, *Surficial Geology of Kansas*. Do not choose
a connector implementation path, download or hash the source PDF, activate a
source, ingest data, decide rights, make a policy or review decision, create
evidence, or authorize release or public use.

## 2. Current official-source evidence

Official KGS pages reviewed on 2026-08-14 establish the following bounded facts:

| Official source | CONFIRMED finding | Limitation |
|---|---|---|
| `https://www.kgs.ku.edu/General/Geology/state23.html` | Identifies Map M-118 as *Surficial Geology of Kansas*, 68 × 39 inches, scale 1:500,000, and links full-size PDF and JPEG distributions. | The PDF bytes were not downloaded, hashed, or admitted. No edition date or update cadence is inferred beyond the page metadata. |
| `https://kgs.ku.edu/maps` | KGS presents its maps as important sources about Kansas geology and natural resources and lists the statewide surficial-geology map. | Source importance does not make every map statement a direct observation or point-level truth. |
| `https://kgs.ku.edu/kansas-geologic-maps` | KGS explains geologic maps as compiled representations used for near-surface geology and planning. | The descriptor preserves interpreted, scale-bound map authority rather than observation authority. |
| `https://www.kgs.ku.edu/General/copyright.html` | The legacy KGS website Terms of Use describes broad reuse with attribution and says source data should be acquired directly from KGS. | The page is dated July 2002 and does not settle all publication-specific reuse questions. |
| `https://kgs.ku.edu/kgs-publishing-policy-and-guidelines` | Current KGS publishing guidance allows educational/noncommercial reuse with attribution and requires permission for commercial use or licensing. | Its scope overlaps but is not identical to the legacy site-wide terms. Qualified rights review is required. |

The two official reuse surfaces create a material interpretation tension. This
packet therefore records `rights_status = unknown`, leaves redistribution and
commercial use unresolved, disables public release, and requires review. It does
not choose the more permissive statement by convenience.

## 3. Current repository evidence

Pinned comparison: `main@103323d7d2916c650e8e9829dd1073ee474d61f0`.

| Evidence | CONFIRMED finding |
|---|---|
| `data/registry/sources/geology/README.md` | The subtype-first Geology source registry is the likely descriptor home; it is empty apart from its README and `.gitkeep`, and it forbids duplicate domain-first registration. |
| `schemas/contracts/v1/source/source_descriptor.schema.json` | The rich shared SourceDescriptor implementation shape already owns source identity, role, authority, rights, sensitivity, cadence, access, citation, source head, admissibility, review, release, lifecycle, and activation posture. |
| `schemas/contracts/v1/sources/source_descriptor.schema.json` | The plural path is a compatibility alias to the rich singular implementation schema and adds no independent authority. |
| `tools/validators/sources/validate_source_descriptor.py` | Existing compatibility entry point validates descriptors without admitting or activating a source or deciding rights, policy, review, evidence, release, or publication. |
| `docs/domains/geology/SOURCE_ROLE_MATRIX.md` | Draft Geology doctrine permits KGS geologic and surficial map families to carry role-bounded map authority while preserving model/aggregate/administrative/candidate distinctions and denying direct-observation collapse. |
| `connectors/geology/kgs/README.md` | KGS connector placement is materially conflicted among source-first and compatibility paths; no executable connector, product descriptor, activation record, or passing connector test is established there. |
| Repository candidate search | No product-specific M-118 SourceDescriptor exists in the Geology registry. |

## 4. Descriptor posture

The candidate is intentionally conservative:

- `source_type = map_artifact`;
- `source_role = authoritative_for_claim` only for the named, scale-bound
  interpreted map artifact;
- allowed claims are map display, citation support, historical context, and
  derived summary after review;
- direct observation, occurrence, regulatory, operational, title, and
  life-safety roles are prohibited;
- rights remain `unknown`;
- connector activation is `disabled`;
- review is `needs_review`;
- registry state is `proposed`;
- release state is `not_released`; and
- public release is denied.

The record includes official locators and metadata only. It contains no source
payload, source snapshot, credential, connector path, map geometry, catalog item,
EvidenceBundle, proof, or release object.

## 5. Directory Rules decision

Accepted ADR-0029 and the adopted Directory Rules assign:

- source identity and registry state to `data/registry/sources/geology/`;
- existing machine shape to `schemas/contracts/v1/sources/`;
- existing reusable validation to `tools/validators/sources/`;
- focused contract verification to `tests/schemas/`;
- read-only orchestration to `.github/workflows/`;
- non-canonical external/repository reconciliation to
  `docs/intake/exploratory/`; and
- AI authoring provenance to `data/receipts/generated/`.

This slice creates no connector and does not resolve the documented connector
path conflict. It creates no new responsibility root or parallel source, schema,
policy, evidence, receipt, proof, release, or publication authority.

## 6. Validation and authority boundary

Local authoring checks prove JSON syntax, deterministic `spec_hash`, stable
inactive/release-denied assertions, official-host endpoint restriction, workflow
YAML syntax, and generated-receipt hash closure.

The path-scoped exact-head workflow must additionally prove the candidate against
the repository-owned SourceDescriptor schema and focused tests. It cannot prove
legal or steward rights approval, PDF byte identity, map-unit correctness,
source fitness, source activation, evidence closure, policy, review, release,
deployment, publication, or public use.

## 7. Rollback

Before merge, close the draft pull request and abandon the branch. After an
authorized merge, revert the one additive implementation commit. No live source,
connector, source material, lifecycle record, cache, catalog, release,
deployment, or public artifact requires restoration.
