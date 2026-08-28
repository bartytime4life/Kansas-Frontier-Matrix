<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/new-ideas-5-source-map
title: New Ideas 5 - Governed Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; repository-grounded
owners: OWNER_TBD - Intake steward; docs steward; affected subsystem stewards
created: 2026-07-29
updated: 2026-07-29
policy_label: public; intake; exploratory; cite-or-abstain
owning_root: docs/
responsibility: Preserve a bounded, reviewable map from the New Ideas 5 packet to current KFM repository evidence, conflicts, candidate responsibility roots, blockers, and next actions without promoting packet prose into authority.
source_evidence:
  captured_filename: New Ideas 5.pdf
  capture_date: 2026-07-29
  source_date: NEEDS_VERIFICATION
  sha256: 094200ad69f3843d856fce782806f4090c31263567d533d0b425468730d1c91d
  byte_count: 10558510
  page_count: 944
  extracted_text_lines: 42903
  extracted_text_words: 156005
  extracted_text_bytes: 1388783
repository_evidence:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: c5e37844bc18aa129466415c5bb99389c1eb1424
related:
  - ../README.md
  - ../NEW_IDEAS_INDEX.md
  - ../new-ideas-register.md
  - ../canonicalization-policy.md
  - ./README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, new-ideas, source-map, catalog, stac, maplibre, cesium, hydrology, provenance, pipelines, atmosphere, soil, geology, knowledge-graph, ai]
notes:
  - "The PDF is not committed by this change. Its filename and digest preserve attachment identity for later reconciliation."
  - "Page references identify locations in the supplied packet; they do not make packet claims current, correct, accepted, implemented, or publishable."
  - "No code, workflow, dependency, source descriptor, data object, receipt, proof, release object, or public artifact is created by this intake map."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# New Ideas 5 - governed source map

> **Outcome:** The 944-page packet is captured as one exploratory source and reduced to a dependency-aware candidate map. Nothing in this file promotes packet prose into doctrine, architecture, source authority, contract, schema, policy, implementation, proof, release, deployment, or publication.

> [!IMPORTANT]
> `New Ideas 5.pdf` is evidence that an idea was proposed. It is not evidence that an external fact is current, a repository path is correct, a dependency is approved, a source is admissible, a workflow is safe, or a feature is implemented.

**Quick links:** [Source identity](#source-identity-and-review-method) · [Placement](#directory-rules-and-authority-basis) · [Candidate map](#repository-grounded-candidate-map) · [Conflicts](#conflicts-and-unsafe-direct-transfers) · [Sequence](#dependency-ordered-continuation) · [Validation](#validation-and-review-boundary) · [Rollback](#rollback-and-correction)

## Source identity and review method

### Confirmed attachment facts

| Field | Confirmed value |
|---|---|
| Captured filename | `New Ideas 5.pdf` |
| PDF title metadata | `New Ideas 5` |
| Capture and triage date | `2026-07-29` |
| Source authoring date | `NEEDS VERIFICATION` - neither the filename nor inspected PDF metadata supplies a reliable authoring date |
| SHA-256 | `094200ad69f3843d856fce782806f4090c31263567d533d0b425468730d1c91d` |
| Byte count | `10,558,510` |
| Page count | `944` |
| Extracted text | `42,903` lines; `156,005` words; `1,388,783` bytes |
| Repository comparison base | `main@c5e37844bc18aa129466415c5bb99389c1eb1424` |

### Review method and limits

This first pass:

1. extracted the full text and retained page boundaries;
2. visually inspected the opening 3D proposal and representative catalog-QA and NWIS pages;
3. scanned all page-leading text for recurring catalog, renderer, governance, validation, provenance, pipeline, domain, graph, AI, and security themes;
4. read representative implementation-heavy sections;
5. compared high-signal proposals with current repository paths, contracts, ADRs, validators, tests, workflows, and lane READMEs; and
6. classified each selected cluster by repository fit and dependency burden.

This is a **bounded triage**, not a sentence-by-sentence verification of all 156,005 words. Ideas not listed below remain `CAPTURED / EXPLORATORY` rather than silently rejected or accepted.

The packet contains many implementation-looking code and workflow fragments. Those fragments were treated as untrusted proposal text. They were not executed, copied into repository code, or used as authority.

[Back to top](#top)

## Directory Rules and authority basis

The accepted [Directory Rules v2](../../doctrine/directory-rules.md), adopted through [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), require placement by responsibility root rather than packet topic or suggested path.

That produces the following routing rules:

| Packet material | Correct responsibility |
|---|---|
| Exploratory packet identity, clustering, and disposition | `docs/intake/` |
| Durable renderer or system choice | `docs/adr/` plus the affected architecture lane |
| Human-readable object meaning | `contracts/` |
| Machine-checkable shape | `schemas/` |
| Allow, deny, restrict, abstain, or obligation behavior | `policy/` |
| Executable validators and build helpers | `tools/` |
| Pipeline implementation and declarative profiles | `pipelines/` and `pipeline_specs/` |
| Source identity, rights, cadence, and activation posture | source documentation and `data/registry/` |
| Lifecycle data and catalog projections | the matching `data/` phase |
| Release, correction, withdrawal, and rollback authority | `release/` and its governed companions |

The packet's older paths such as `src/pipelines/...`, `tools/validation/...`, generic `web/`, and data-local output trees are not carried forward as current KFM locations. Current repository topology and accepted Directory Rules control placement.

[Back to top](#top)

## Repository-grounded candidate map

Disposition terms:

- `CORROBORATIVE` - reinforces a direction already represented by stronger repository surfaces.
- `REPO_VERIFY` - useful pressure tied to a confirmed repository gap, but not yet safe to implement.
- `CONFLICTED` - disagrees with, bypasses, or depends on an unresolved repository decision.
- `DEFERRED` - viable only after external facts, source rights, contracts, policies, or upstream dependencies close.
- `REJECTED_AS_WRITTEN` - the direct packet transfer would violate current boundaries; a narrower reformulation may remain useful.

| Candidate cluster | Packet location | Repository evidence at the pinned base | Disposition | Candidate owner and smallest safe next action |
|---|---|---|---|---|
| Cesium + MapLibre dual-renderer Story Node | pp. 1-4 | [ADR-0007](<../../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>) is still proposed and requires a separately accepted exception for a peer renderer. `packages/cesium/` is absent at the checked path; [`packages/maplibre/`](../../../packages/maplibre/README.md) remains a scaffold. | `CONFLICTED`; direct transfer `REJECTED_AS_WRITTEN` | `docs/adr/` + renderer architecture. Reconcile ADR-0007 and the missing/overstated 3D architecture surfaces before selecting any peer renderer, package, camera handoff, or public demo. |
| Projection extension mapping and fast STAC catalog QA | pp. 5-11 | [`tools/validators/catalog/`](../../../tools/validators/catalog/README.md) is README-led; the top-level CatalogMatrix validator remains a stub; the accepted STAC profile and CatalogMatrix homes are unresolved; the only discovered `collection.json` is explicitly a placeholder rather than a STAC Collection. | `REPO_VERIFY`; high-value candidate, not implementation-ready | Catalog contract/schema/validator owners. First freeze the record-local profile, placeholder disposition, offline link semantics, finite outcomes, and separation from [`catalog_closure/`](../../../tools/validators/catalog_closure/README.md). Default CI must not depend on live `HEAD`/`GET` requests. |
| Keyless signing, SLSA, SBOM, and attestation references | pp. 12, 65-75, 201-213 | [`tools/attest/`](../../../tools/attest/README.md), attestation validators, a PMTiles-attestation workflow, and release/attestation lanes already exist. Their presence does not prove accepted signing identity, production use, transparency-log policy, or release closure. | `CORROBORATIVE / REPO_VERIFY` | Supply-chain and release owners. Inventory current executable behavior and gaps before adding another workflow or schema family; retain signing evidence as distinct from KFM semantic evidence and release approval. |
| USGS NWIS watcher with normalization, freshness, kill switch, and rollback | pp. 13-21 | KFM already has USGS Water Data connector, pipeline-spec, hydrology pipeline, normalizer tests, watcher/tooling docs, and [`nwis-water.md`](../../sources/catalog/usgs/nwis-water.md). The packet's legacy `waterservices.usgs.gov` assumptions and 2026/2027 phase-out claims remain version-sensitive. | `CORROBORATIVE / DEFERRED` | Hydrology source and connector owners. Verify current official endpoints, terms, cadence, parameter semantics, and cutover status; then close one existing connector/pipeline gap rather than creating `src/pipelines/hydrology/nwis_watcher/`. |
| Dependency DAGs, canary partitions, backpressure, WAL/outbox, kill switches, and rollback-first pipeline patterns | pp. 22-30, 47-64 | Current KFM doctrine already requires fail-closed promotion, receipts, watcher-as-non-publisher, correction, and rollback. Concrete orchestrators, queue semantics, telemetry, and transactional guarantees vary by lane and are not established by packet prose. | `CORROBORATIVE / DEFERRED` | Pipeline, runtime, and control-plane owners. Select one current pipeline with a confirmed failure mode and add the smallest contract-test-tool co-change; do not introduce a second orchestration authority. |
| Air-quality fusion using CAMS, HRRR-Smoke, AQS, PurpleAir, NowCast, bias correction, and EnKF | pp. 31-38, 83-85, 113-118 | Atmosphere contracts, PM2.5 schemas, HRRR-Smoke connector docs, AOD-not-PM2.5 policy tests, source records, and a placeholder PM2.5 catalog object exist. Live source roles, rights, calibration authority, model validation, and fused-product release semantics remain unresolved. | `DEFERRED` | Atmosphere, source, model, policy, and sensitivity owners. Define observation-versus-model roles and a synthetic no-network fusion contract before any live fetch, calibration claim, or public layer. |
| Deterministic soil/geology GeoParquet, COG, PMTiles, identity, and scale guardrails | pp. 39-43, 76-82, 163-178 | Soil and geology packages, domain schemas, validators, lifecycle lanes, and source docs already exist, with known placeholder and authority gaps. Packet paths and hard-coded scale/CRS choices are not current policy. | `CORROBORATIVE / REPO_VERIFY` | Soil/geology, geo, catalog, and policy owners. Choose one existing placeholder validator or missing fixture with an accepted contract and implement a no-network bounded slice. |
| Reproducible experiments, seeds, model cards, metrics, and promotion checks | pp. 86-90, 154-162, 179-183 | Model-card and reproducibility documentation/policy surfaces exist in selected lanes; no packet-wide experiment root or promotion policy is established by current evidence. | `CORROBORATIVE / DEFERRED` | Runtime/model, evidence, policy, and provenance owners. Inventory existing experiment/model object families before proposing a canonical contract or storage path. |
| Knowledge-graph summaries, Neo4j constraints, DRIFT/LlamaIndex retrieval, and AI synthesis | pp. 192-196, 234-237, 702, 724-727 | Current repository search found graph/triplet doctrine and drift registers, but did not establish the packet's named Neo4j/DRIFT runtime, retrieval stack, or public consumer. AI remains evidence-subordinate and public clients remain behind governed APIs. | `DEFERRED`; runtime transfer `REJECTED_AS_WRITTEN` | Graph, triplet, governed-AI, security, and API owners. Begin with a contract-level retrieval envelope and synthetic evidence-resolution test only after a current consumer and canonical graph boundary are verified. |
| SPDX/license guard and dependency/license automation | pp. 238 onward | Current dependency scanning and repository license surfaces exist, but a header-count heuristic or network-fetched tool is not license compliance proof. | `REPO_VERIFY` | Supply-chain and legal/rights owners. Define accepted license evidence, exemptions, generated/vendor handling, deterministic fixtures, and false-positive posture before adding a blocking check. |

### Highest-confidence conclusions

1. **The packet should not be implemented as a directory tree.** Several suggested paths conflict with current responsibility roots.
2. **The catalog-QA proposal identifies a real gap, but its direct implementation is unsafe.** It assumes a profile, treats live network reachability as validation, and would encounter a confirmed placeholder `collection.json`.
3. **The NWIS proposal is mostly corroborative.** Current KFM already has stronger hydrology placement and object-role boundaries; the useful delta is current endpoint/cutover verification.
4. **The dual-renderer proposal requires a decision, not a demo branch.** It cannot bypass the unresolved renderer ADR and package-admission burden.
5. **Supply-chain, provenance, watcher, pipeline, soil/geology, and atmosphere ideas should extend existing lanes.** Creating packet-named parallel homes would increase drift.

[Back to top](#top)

## Conflicts and unsafe direct transfers

| Packet pattern | Why direct transfer is unsafe | Required correction |
|---|---|---|
| "Drop-in" or "ready to commit" label | Presentation is not repository fit, dependency closure, review, or authorization. | Re-derive the change from current repo evidence and freeze an exact bounded scope. |
| `tools/validation/...` | Current executable validator responsibility is under `tools/validators/...`; record-local and closure validation are separate. | Route through the existing validator topology. |
| `src/pipelines/...` | Current pipelines live under the `pipelines/` responsibility root with domain and spec lanes. | Extend the existing hydrology lane after source and contract gates. |
| Generic `web/` demo | `web/` is a compatibility surface; Explorer Web is the current canonical shell direction. | Use current app/package boundaries only after renderer and governed-input decisions. |
| Live link checks in default catalog CI | Network volatility can turn availability into false semantic failure and violates the catalog lane's no-network default. | Validate local link shape and closure deterministically; isolate any live probe as non-authoritative evidence. |
| Hard-coded external versions, endpoints, licenses, or service maturity | These facts can change and were not reverified in this intake run. | Mark `NEEDS VERIFICATION` and check primary sources in the implementing run. |
| Example coordinates, station IDs, thresholds, or claims | Examples may be synthetic, stale, sensitive, or policy-significant. | Use explicitly synthetic fixtures unless an admitted source and policy permit real data. |
| Successful signature, schema, render, model, or link result | Each proves only its declared check, not truth, evidence closure, policy approval, release, or publication. | Preserve separate validation, evidence, policy, review, and release objects. |

[Back to top](#top)

## Dependency-ordered continuation

### Wave 1 - decisions and repository verification

1. Reconcile the role of `NEW_IDEAS_INDEX.md` and `new-ideas-register.md` without creating another intake authority.
2. Resolve the record-local STAC profile and placeholder `collection.json` disposition before catalog-QA code.
3. Reconcile ADR-0007 and current renderer architecture before any Cesium or peer-renderer work.
4. Reverify current USGS Water Data endpoint/cutover facts from official sources before connector changes.
5. Inventory current attestation and license-check behavior before adding supply-chain workflows.

### Wave 2 - bounded offline implementation

After Wave 1 closes the applicable gate, admit at most one dependency-closed slice:

- a deterministic no-network catalog-record readiness validator with synthetic valid/invalid fixtures;
- one existing hydrology connector or normalizer gap with no live-source activation;
- one soil/geology contract-validator-fixture gap;
- one attestation-reference or license-readiness checker with finite outcomes; or
- one renderer-decision documentation reconciliation with no runtime dependency.

### Wave 3 - live adapters and public behavior

Live source calls, model fusion, graph retrieval, peer rendering, deployment, release, and publication remain later work. They require admitted sources, current external verification, rights and sensitivity review, evidence closure, policy decisions, tested correction, rollback, and separate authorization.

### Recommended next bounded action

**PROPOSED:** inspect the current catalog contract/profile and the placeholder atmosphere `collection.json`, then freeze a decision-only packet for record-local STAC readiness. Do not implement the PDF's networked quick gate until profile ownership, placeholder handling, local link semantics, finite outcomes, fixtures, and CI significance are explicit.

[Back to top](#top)

## Out of scope

This intake change does not:

- commit or redistribute the PDF;
- verify every external citation or product claim in the packet;
- accept or reject ADR-0007;
- select Cesium, MapLibre, a plugin, an orchestrator, graph database, AI framework, model, source, endpoint, package version, or license;
- add source descriptors or activate sources;
- add or modify code, tests, fixtures, workflows, dependencies, data, receipts, proofs, release objects, deployments, or public artifacts;
- claim that a suggested example is real, current, public-safe, or authorized; or
- grant authority to any candidate destination.

[Back to top](#top)

## Validation and review boundary

Required review checks for this source map:

- source filename, digest, byte count, page count, and extracted-text counts match the inspected attachment;
- every repository claim resolves to the pinned base or is narrowed to `NEEDS VERIFICATION`;
- every proposed destination uses an existing responsibility root;
- no packet code or sensitive payload is copied;
- links resolve at the pinned base;
- candidate status does not imply promotion;
- the recommended next action is bounded, reversible, and non-authorizing; and
- any future implementation starts with a fresh base/path/operation authorization.

A passing Markdown, link, or repository test proves only that this intake artifact is structurally reviewable. It does not validate the packet's external facts or candidates.

[Back to top](#top)

## Rollback and correction

Before merge, close the draft PR and abandon its branch.

After any separately authorized merge:

1. use a reviewed corrective or revert PR rather than rewriting shared history;
2. preserve the packet identity and prior classification as lineage;
3. update the [New Ideas Index](../NEW_IDEAS_INDEX.md) and [New Ideas Register](../new-ideas-register.md) together when a candidate is promoted, deferred, rejected, or superseded; and
4. add a forward link to the accepted destination without turning this exploratory source map into continuing authority.

[Back to top](#top)
