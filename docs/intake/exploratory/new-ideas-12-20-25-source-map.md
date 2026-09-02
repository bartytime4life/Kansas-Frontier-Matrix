<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/new-ideas-12-20-25-source-map
title: New Ideas 12-20-25 - Governed Source Map and Follow-on Register
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; repository-grounded
owners: OWNER_TBD - Intake steward; atlas steward; docs steward; affected domain and subsystem stewards
created: 2026-08-03
updated: 2026-08-03
policy_label: public; intake; exploratory; cite-or-abstain
owning_root: docs/
responsibility: Preserve a reviewable map from the New Ideas 12-20-25 packet to current KFM repository evidence, reusable concepts, conflicts, unsafe transfers, and dependency-ordered follow-on work without promoting packet prose, code, source claims, standards, thresholds, trust scores, or publication recipes into authority.
source_evidence:
  captured_filename: New Ideas 12-20-25.docx.pdf
  pdf_title: New Ideas 12-20-25.docx
  source_date: 2025-12-20
  capture_date: 2026-08-03
  sha256: 89b0231a26c34e8a383d5bbfcafa7e84b5e1072b26859ce8b2dcc0aaf2d9add2
  byte_count: 717542
  page_count: 37
  extracted_text_lines: 1548
  extracted_text_words: 6641
  extracted_text_bytes: 53027
repository_evidence:
  repository: bartytime4life/Kansas-Frontier-Matrix
  remote_main_snapshot: 99e73d87e0aed536b25f2f282f88a386f35654b5
  remote_state_verified_at: 2026-08-03T05:51:15Z
  open_pull_requests_at_verification: 1
  nonoverlap_pull_request: 1936
related:
  - ../README.md
  - ../NEW_IDEAS_INDEX.md
  - ../new-ideas-register.md
  - ./README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/atmosphere/README.md
  - ../../domains/roads-rail-trade/README.md
  - ../../../migrations/graph/README.md
  - ../../../pipelines/README.md
tags: [kfm, intake, new-ideas, calibration, pm25, stac, zarr, graph-migration, incident-fusion, deterministic-replay]
notes:
  - "The PDF is not committed by this change. Its filename, metadata, digest, byte count, page count, and extracted-text counts preserve attachment identity."
  - "Page references identify locations in the supplied packet; they do not make packet claims current, scientifically accepted, standards-conformant, implemented, source-admitted, or publishable."
  - "External labels and links in the PDF were not treated as complete citations; versions, rights, availability, and technical claims remain NEEDS VERIFICATION."
  - "Merged PR #1936 was inspected at the final verification snapshot and changes release/promotion-gate surfaces only; it does not overlap this Atmosphere/intake slice."
  - "No packet code, live source, standard, dependency, schema, policy, migration, corrected observation, incident, pipeline, release object, deployment, or publication is created by this source map."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# New Ideas 12-20-25 - governed source map and follow-on register

> **Outcome:** The 37-page packet is identity-pinned and reconciled as five exploratory families: low-cost PM2.5 calibration pedigree, STAC/Zarr array discovery, graph migration change control, multi-source transportation incident fusion, and deterministic pipeline replay. This change implements the strongest repository-native slice: a fixture-only Atmosphere calibration-pedigree validator that proves synthetic shape and anti-collapse boundaries without training a model, correcting a real observation, admitting a source, computing authoritative trust, executing Rego, or authorizing promotion.

> [!IMPORTANT]
> `New Ideas 12-20-25.docx.pdf` proves only that these ideas and code sketches were proposed in the captured document. It does not prove that cited research, upstream standards, services, source roles, thresholds, tools, package versions, paths, workflows, or trust rankings are current or accepted by KFM.

**Quick links:** [Source identity](#source-identity-and-review-method) · [Placement](#directory-rules-and-authority-basis) · [Packet map](#packet-structure) · [Reconciliation](#repository-grounded-reconciliation) · [Candidate assay](#candidate-assay) · [Unsafe transfers](#unsafe-direct-transfers) · [Sequence](#dependency-ordered-continuation) · [Validation](#validation-and-review-boundary) · [Rollback](#rollback-and-correction)

## Source identity and review method

### Confirmed attachment facts

| Field | Confirmed value |
|---|---|
| Captured filename | `New Ideas 12-20-25.docx.pdf` |
| PDF title metadata | `New Ideas 12-20-25.docx` |
| Source date | `2025-12-20`, supported by the filename and PDF title metadata |
| Capture and triage date | `2026-08-03` |
| SHA-256 | `89b0231a26c34e8a383d5bbfcafa7e84b5e1072b26859ce8b2dcc0aaf2d9add2` |
| Byte count | `717,542` |
| Page count | `37` |
| Extracted text | `1,548` lines; `6,641` words; `53,027` bytes |
| PDF posture | tagged; unencrypted; no JavaScript; no form |
| Repository comparison snapshot | remote `main@99e73d87e0aed536b25f2f282f88a386f35654b5`, verified `2026-08-03T06:19:17Z` |
| Open pull requests at verification | `0`; merged PR #1936 was separately checked and has no overlap with this artifact set |

### Review method and limits

This pass:

1. extracted the complete PDF with page boundaries;
2. visually inspected pages 1, 7, 12, 19, and 29 across all five proposal families;
3. inspected current-main Atmosphere, catalog-schema, catalog-validator, graph-migration, roads/rail/trade, pipeline, Directory Rules, intake, and generated-receipt surfaces;
4. compared the packet with current repository maturity instead of treating its implementation-looking examples as repository state;
5. treated external source labels, standards claims, co-location durations, predictor rankings, source authority, trust tiers, staleness values, package choices, and workflow recipes as `NEEDS VERIFICATION`; and
6. retained only dependency-ordered, reversible candidates that can begin with synthetic, no-network evidence.

No external endpoint or live service was called. The packet's short labels such as MDPI, PMC, AMT, WZDx, ArcGIS, GTFS, GeoZarr, DVC, lakeFS, OPA, and Cosign are not complete evidence records in this intake slice.

[Back to top](#top)

## Directory Rules and authority basis

The accepted [Directory Rules v2](../../doctrine/directory-rules.md), adopted through [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), place artifacts by responsibility, authority, lifecycle, exposure, mutability, and retention.

| Packet material | Current or future responsibility |
|---|---|
| Exploratory source identity, clustering, disposition, and blockers | `docs/intake/` |
| Atmosphere meaning, correction caveats, and knowledge-character boundaries | Existing Atmosphere documentation and, only after review, `contracts/` |
| Machine-checkable shape | `schemas/` after profile and schema-home review |
| Synthetic proof inputs and expected denials | Existing `fixtures/` and `tests/` responsibilities |
| Executable validation | Existing `tools/validators/` responsibility |
| Catalog and array-discovery meaning | Existing catalog contract/schema/validator responsibilities; no parallel STAC or Zarr authority |
| Graph change payloads and recovery pairing | Existing [graph migration lane](../../../migrations/graph/README.md) and rollback responsibility |
| Roads, rail, work-zone, and transit domain meaning | Existing [Roads / Rail / Trade domain lane](../../domains/roads-rail-trade/README.md) |
| Source identity, rights, cadence, authority, and access | Source documentation plus the accepted source registry after admission |
| Pipeline execution and declarative specifications | Existing [pipeline root](../../../pipelines/README.md) and `pipeline_specs/`, subject to activation authority |
| Receipts, proofs, catalog records, and releases | Their separate governed roots; none may substitute for another |

The packet's generic `data/`, `src/`, `policy/`, `attest/`, workflow, migration-log, and publication paths are not carried forward as current KFM locations.

[Back to top](#top)

## Packet structure

| Pages | Proposal family | Durable design pressure |
|---:|---|---|
| 1-7 | Adaptive and meteorology-aware calibration for low-cost PM2.5 sensors | Preserve raw versus corrected character, reference anchoring, model/version identity, drift and transfer limits, confidence, caveats, and abstention |
| 7-11 | STAC/Zarr array metadata, multiscale layout, and EOPF-style asset navigation | Make array access characteristics discoverable without probing; keep evolving field names and standards profiles provisional |
| 12-18 | Governed graph migration enforcement | Declare intent and blast radius; preserve invariants, provenance, pre/post state, rollback evidence, and non-release semantics |
| 19-28 | WZDx, ArcGIS, and GTFS-Realtime incident fusion | Preserve source observations, deterministic deltas, stale/conflict states, and lineage without source-count or trust-tier promotion shortcuts |
| 29-37 | lakeFS, DVC, LangGraph, OPA, and Cosign deterministic-run prototype | Reinforces replay, pinned inputs, receipts, gates, and rollback; packet code and workflow are not safe as drop-in implementation |

[Back to top](#top)

## Repository-grounded reconciliation

Disposition terms:

- `CORROBORATIVE` - reinforces stronger current repository responsibilities.
- `REPO_GAP` - identifies a bounded missing behavior at the pinned snapshot.
- `PARTIAL` - adjacent meaning or scaffolding exists, but the proposed behavior is not established.
- `CONFLICTED` - depends on unresolved source, standards, profile, contract, policy, or authority decisions.
- `REJECTED_AS_WRITTEN` - direct transfer would create drift, overclaim maturity, or weaken trust boundaries.

| Candidate cluster | Packet pages | Repository evidence at the inspected snapshot | Disposition | Smallest safe continuation |
|---|---:|---|---|---|
| Low-cost PM2.5 calibration, drift, meteorology, trust, and transferability | 1-7 | The [Atmosphere lane](../../domains/atmosphere/README.md) already requires correction, caveats, confidence, and limitations for low-cost sensor release. This change adds a profile-local, fixture-only calibration-pedigree validator with exact denials. | `IMPLEMENTED IN CHANGE / PROPOSED FOR MERGE` | Review the frozen profile and exact denials; do not infer live-record, scientific, policy, source-admission, or release authority. |
| STAC/Zarr array and multiscale metadata | 7-11 | The catalog-matrix schema is permissive and its root validator remains a placeholder. No current-main implementation was found for the packet's proposed array metadata block. | `CONFLICTED / DECISION-FIRST` | Verify the upstream profile and KFM catalog owner, then define one synthetic namespaced array-metadata profile before any catalog or store mutation. |
| Graph migration declaration, invariants, deltas, and recovery | 12-18 | The [graph migration README](../../../migrations/graph/README.md) already documents a proposed minimum packet and rollback pairing, but explicitly does not establish an active graph store, runner, payload ledger, or execution history. | `PARTIAL` | After profile ownership closes, validate a synthetic declaration-versus-observed-delta packet; do not execute Cypher or mutate a graph. |
| WZDx / ArcGIS / GTFS incident fusion | 19-28 | The [Roads / Rail / Trade lane](../../domains/roads-rail-trade/README.md) records WZDx source terms as needing verification. Current inspection did not establish admitted source descriptors, rights, a canonical incident contract, or source-conflict policy. | `CONFLICTED / DEFER` | Start later with a source-neutral snapshot-delta fixture that preserves `MISSING` as uncertain rather than cleared; no live fetch or promotion. |
| Deterministic lakeFS/DVC/LangGraph/OPA/Cosign run | 29-37 | The [pipeline root](../../../pipelines/README.md) already requires deterministic, no-network-by-default, receipt-aware, reversible behavior and separates pipeline output from release authority. Active implementation depth remains partial. | `CORROBORATIVE`; sample `REJECTED_AS_WRITTEN` | Reuse current RunReceipt and validation responsibilities. Do not import the packet's toolchain or workflow. |

[Back to top](#top)

## Candidate assay

| Candidate | Verified need | Repository fit | Deterministic proof | Authority / dependency burden | Intake result |
|---|---|---|---|---|---|
| Atmosphere calibration pedigree | High: current docs name the caveat and leave criteria proposed | High: established Atmosphere validator, fixture, test, and workflow roots | High: synthetic positive and exact-negative records | Moderate scientific review; no new dependency needed | **Selected and implemented as a bounded fixture profile** |
| STAC/Zarr array metadata | Medium: no matching implementation found | Medium: catalog schema and validator exist but are immature | High after profile choice | High upstream-version and catalog-authority burden | Decision-first |
| Graph migration declaration | Medium: documented contract is not executable | High responsibility-root fit | High with synthetic deltas | High store/profile/owner uncertainty | Hold for profile decision |
| Incident snapshot-delta | Medium: source terms are recorded but unadmitted | Medium domain fit | High with source-neutral fixtures | High rights, authority, safety, and event-policy burden | Defer |
| Deterministic replay receipt | Lower: current pipeline and receipt doctrine already carry much of the idea | High | High | Packet toolchain adds unnecessary supply-chain burden | Corroborative only |

### Selected follow-on boundary

**IMPLEMENTED IN THIS CHANGE / PROPOSED FOR MERGE:** a frozen, noncanonical
Atmosphere calibration-pedigree fixture profile under the existing validator,
fixture, test, documentation, and read-only workflow responsibilities.

A positive synthetic record should bind:

- raw-observation and reference-monitor evidence references without copying source payloads;
- source-descriptor references and generalized spatial support;
- exact fixture-local model, training, and specification identities plus full SHA-256 identity-string digests (not artifact-content or scientific-evidence hashes);
- co-location/training interval and declared deployment regime without adopting a universal duration;
- meteorological covariate names without claiming one scientifically sufficient model;
- held-out evaluation metadata, confidence posture, drift or out-of-distribution state, and explicit validity bounds;
- correction, caveat, limitation, review, and rollback metadata; and
- fixture-only governance with `promotion_eligible: false`.

Exact negative fixtures should deny:

1. peer consensus or a trust score presented as a reference anchor;
2. corrected or modeled output presented as a raw observation;
3. missing model, training, specification, or reference evidence identity;
4. an unbounded transfer claim outside the declared deployment regime;
5. a trust score or single validation metric granting promotion eligibility;
6. precise station coordinates on a public-safe fixture surface; and
7. missing correction caveats, confidence, limitations, or rollback identity.

Passing this profile proves only the declared synthetic shape and anti-collapse behavior. It does not prove scientific validity, reference-grade status, corrected concentration, source admission, policy approval, model fitness, public safety, release, or publication.

[Back to top](#top)

## Unsafe direct transfers

| Packet pattern | Why direct transfer is unsafe | Required correction |
|---|---|---|
| Trust score treated as truth, source authority, or promotion authority | Accuracy, stability, responsiveness, and consensus are model inputs, not evidence closure or accountable review. | Preserve trust as bounded assessment metadata subordinate to EvidenceBundle, policy, review, and release. |
| Fixed co-location duration, predictor ranking, model choice, clipping rule, or correction equation treated as canonical | Hardware, aerosol regime, climate, cadence, transfer distribution, and scientific evidence differ. | Require hardware- and regime-specific evidence, versioned decisions, uncertainty, and abstention. |
| Corrected PM2.5 collapsed into raw observation | It erases transform, model, evidence, and validity lineage. | Preserve raw and corrected characters plus model/specification identity and limitations. |
| Provisional STAC/Zarr fields copied into a canonical schema | The packet itself says standards are evolving, and current KFM catalog closure is immature. | Verify upstream specifications and choose a KFM profile through the owning contract/schema decision. |
| Packet graph paths, Cypher snippets, labels, cardinalities, or node limits copied directly | No active graph engine or relationship registry is established; generic invariants can be wrong for a domain. | Use the existing migration responsibility and contract-specific synthetic fixtures only after owner/profile review. |
| Tier A source alone or two-source agreement treated as confirmed or publishable | Source role, recency, and agreement do not establish evidence sufficiency, rights, policy, review, or release. | Preserve every observation and conflict; route promotion through KFM's governed gates. |
| Missing snapshot feature treated as deletion or clear | Feed churn and incomplete snapshots make absence ambiguous. | Emit an uncertain missing/probable-clear state with replayable observation history. |
| Packet deterministic-run workflow copied into CI | It uses unpinned downloads and floating actions, contains a hard-coded successful Cosign verdict, and introduces toolchain and publication behavior. | Reuse pinned repository tooling and existing no-network receipt/validation lanes. |
| Truncated identifiers or the sample seeded jitter used as proof of determinism | Short digests weaken collision resistance; the sample recreates the same seeded random value per record. | Use full accepted digests, canonical serialization, fixed inputs, and changed-input/replay negative tests. |

[Back to top](#top)

## Dependency-ordered continuation

### Wave 1 - bounded Atmosphere fixture evidence

Completed in this change:

1. reinspected current `main`, open pull requests, Atmosphere caveat docs, validator runtime, workflow, fixtures, tests, and generated-receipt conventions;
2. froze a profile-local calibration-pedigree shape with finite, non-echoing code/path findings;
3. added two synthetic positive controls, sixteen exact-negative pairs, parser bounds, identity-digest checks, determinism, CLI, and active no-network tests;
4. kept every live source, scientific model, precise coordinate, canonical threshold, Rego decision, release, and publication path inactive; and
5. documented rollback and paired the artifact set with a self-excluding provenance receipt.

### Wave 2 - decision-only profiles

After separately authorized evidence review:

- decide the KFM catalog owner and versioned STAC/Zarr array-metadata profile;
- decide the graph migration declaration and observed-delta profile; and
- define source-neutral incident observation/delta semantics, especially stale, missing, conflicting, corrected, and superseded states.

### Wave 3 - implementation behind gates

Live sensors, reference monitors, Zarr stores, graph stores, WZDx, ArcGIS, GTFS-Realtime, lakeFS, DVC, LangGraph, OPA, Cosign, pipelines, watchers, catalog writers, corrected public values, releases, and publication remain later work. Each requires accepted source identity and rights, contracts, schemas, policy, evidence, review, tests, correction, rollback, activation, and exact authorization.

[Back to top](#top)

## Out of scope

This change does not:

- commit or redistribute the PDF;
- verify the packet's external research, upstream standards, vendor APIs, source authority, rights, licenses, thresholds, or package versions;
- change an Atmosphere contract, canonical schema, scientific model, corrected observation, source descriptor, or Rego policy;
- evaluate live observations, select or validate a scientific correction, resolve synthetic evidence references, or authorize public release;
- create or mutate a STAC catalog, Zarr store, graph, incident stream, pipeline, policy, receipt family, proof, release, or publication artifact;
- install lakeFS, DVC, LangGraph, OPA, Cosign, Neo4j, ArcGIS, GTFS, or WZDx tooling;
- copy packet code, workflow YAML, generic paths, hard-coded trust tiers, automatic promotion rules, exact coordinates, credentials, or live payloads; or
- mark any proposal beyond the bounded fixture validator as implemented, accepted, scientifically validated, production-ready, released, deployed, or published.

[Back to top](#top)

## Validation and review boundary

Required checks for this source map:

- source filename, PDF title, digest, byte count, page count, and extracted-text counts match the attachment;
- visual review covers all five packet families;
- repository claims resolve to the pinned snapshot or remain labeled `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`;
- index and detailed register IDs, source identity, disposition, and follow-on recommendation agree;
- source map links resolve within the verified repository tree;
- the attachment is not added to Git;
- no external source, dependency, threshold, trust ranking, standard, schema, policy, model, pipeline, migration, release, or publication behavior is admitted;
- generated receipt artifact and truth-label keys exactly match the complete authored artifact set while excluding the receipt itself; and
- human review and hosted exact-head checks remain pending.

A clean Markdown, link, JSON, fixture, test, workflow, hash, or receipt check proves
only that the intake trace and frozen synthetic profile are structurally
reviewable, deterministic, and byte-bound. It does not establish scientific,
source, evidence, policy, regulatory, health, or release validity.

[Back to top](#top)

## Rollback and correction

Before merge, close the draft pull request and abandon the feature branch.

After a separately authorized merge:

1. use a reviewed corrective or revert pull request rather than rewriting history;
2. preserve the captured filename and digest when correcting interpretation;
3. update the source map, index, detailed register, and generated receipt together;
4. link to any later accepted destination without turning this source map into continuing authority; and
5. withdraw or narrow any candidate whose source interpretation, placement, standards posture, or repository-gap claim is disproved.

[Back to top](#top)
