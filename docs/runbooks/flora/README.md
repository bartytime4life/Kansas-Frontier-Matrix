<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/flora/readme
title: Flora Runbooks · Lane Boundary and Navigation
type: readme
version: v1.0
status: draft; repository-grounded; documentation-only; proposal-era-children; sensitive-domain; non-authoritative; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: "Flora, taxonomy, source, rights, stewardship, sensitivity/geoprivacy, evidence, policy, validation, review, release, correction, rollback, operations, and independent-review assignments remain NEEDS VERIFICATION; CODEOWNERS routing does not create those authorities."
created: 2026-08-24
updated: 2026-08-24
policy_label: public-review; flora; runbook-index; proposal-era-children; sensitive-location; fail-closed; non-release
current_path: docs/runbooks/flora/README.md
owning_root: docs/
responsibility: "Define the human-facing Flora runbook lane boundary, disclose current child maturity, and route operators to the narrowest applicable procedure without granting taxonomy, source, rights, sensitivity, evidence, policy, review, lifecycle, release, deployment, promotion, rollback-execution, or publication authority."
truth_posture: cite-or-abstain
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 35bb62209569f63af78c6fefe4c85015d3bdceb1
  prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  child_count: 4
  substantive_proposal_era_children: 4
  bounded_workflow_blob: 3fe6b1ba8150960692b6b2fc764c6aa31d09565c
  bounded_validator_blob: 17933f997f7cb1219e3057ea74bf2c077dc45386
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  policy_gate_register_blob: bc8185b4762a947c742cf54a7ea4f2bf80670e21
  flora_source_placeholder_blob: 4cf877d234542990be382913d0ab0917f8fb3398
  flora_release_candidate_index_blob: 15a08f9fb2cdd33041d3a3f3e3c844f26a7a0998
related:
  - ../README.md
  - ../../domains/flora/README.md
  - ../../domains/flora/SENSITIVITY.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-flora.yml
  - ../../../tools/validators/domains/flora/validate_public_safe_fixture.py
  - ../../../tests/domains/flora/test_flora_smoke.py
  - ../../../fixtures/domains/flora/
  - ../../../data/registry/sources/flora/README.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../control_plane/policy_gate_register.yaml
  - ../../../policy/domains/flora/flora_publication_gate.rego
  - ../../../release/candidates/flora/README.md
tags: [kfm, runbooks, flora, taxonomy, occurrence, rare-plants, geoprivacy, rights, navigation, boundary, proposal-era, hold]
notes:
  - "Replaces the prior one-byte placeholder with a lane boundary and navigation contract only."
  - "All four direct child procedures are substantive proposal-era drafts written from a no-mounted-repository posture; current paths, commands, actors, policy bindings, and terminal claims require reconciliation before operational reliance."
  - "One bounded deterministic public-safe Flora fixture validator is executable; proof production and release dry-run jobs remain explicit holds."
  - "The flat sibling Flora runbook files remain proposal scaffolds and are disclosed as topology/identity drift, not treated as canonical procedure children."
  - "Document length, path presence, workflow success, pull-request state, and merge state are inventory evidence, not botanical, sensitivity, release, or publication evidence."
  - "This README changes no contract, schema, policy, fixture, validator, workflow, source record, evidence object, lifecycle object, review record, release object, runtime, deployment, promotion, rollback execution, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Runbooks

> Human-facing navigation for testing, refreshing, assessing, containing, and preparing governed handoffs for the Flora lane. These documents explain procedures; they do not create botanical authority or operational state.

> [!IMPORTANT]
> A runbook, schema-valid fixture, passing validator, green workflow, review note, pull request, or merge is not source admission, taxonomic endorsement, an `EvidenceBundle`, rights clearance, sensitivity approval, policy approval, lifecycle promotion, release authorization, deployment, rollback execution, or publication.

> [!WARNING]
> Exact or reverse-engineerable locations of rare, protected, threatened, culturally significant, or steward-controlled plants fail closed. Private-land joins, collector- or observer-linked details, culturally sensitive plant knowledge, access or collection directions, and geoprivacy transform parameters must not appear in public fixtures, logs, issues, pull requests, screenshots, maps, exports, or generated answers.

> [!CAUTION]
> All four direct child runbooks are substantive but proposal-era. They were authored from a no-mounted-repository posture and contain proposed paths, placeholder actors, illustrative commands, and unverified lifecycle-wide claims. The current repository establishes one bounded synthetic public-safe fixture validator; Flora proof production, live source work, release dry runs, operational promotion, rollback execution, and publication remain held or unverified.

## Lane boundary

Accepted Directory Rules place human operational procedures under `docs/runbooks/`; Flora remains a domain segment inside that responsibility root. Completing this existing README is therefore a same-path documentation update, not a new schema, source registry, policy, evidence, release, or public-serving authority.

This directory owns human procedures for Flora work. It does not own object meaning, machine shape, source admission, taxonomic authority, rights, sensitivity classification, evidence, policy, human review decisions, lifecycle transitions, release state, runtime behavior, or public carriers. Those remain with their accepted doctrine and ADRs, contracts, schemas, registries, policy, evidence, review, release, application, pipeline, fixture, test, and validator surfaces.

Flora procedures may address plant taxonomy, specimen and occurrence evidence, rare or protected plants, culturally sensitive plant knowledge, vegetation communities, invasive plants, phenology, restoration records, and public-safe botanical derivatives. They may link to Habitat, Fauna, Soil, Agriculture, Hydrology, Hazards, or other lanes, but they do not absorb those lanes' truth, policy, or release authority.

The lane preserves these distinctions:

- a taxon concept or synonym mapping is not an occurrence, specimen, legal status, conservation status, range, distribution model, vegetation community, or release decision;
- a specimen or collection record is not proof of current presence, absence, population size, range extent, habitat suitability, or safe public access;
- an occurrence is not a range polygon, area-of-occupancy estimate, vegetation-index result, modeled distribution, restoration outcome, or regulatory determination;
- taxonomic backbones, herbaria, community observations, agency records, remote-sensing products, modeled surfaces, and contextual sources retain distinct source roles;
- upstream obscured or generalized coordinates must not be de-obscured, reverse engineered, or upgraded through a join;
- public-safe and restricted botanical records remain distinct object and exposure families;
- style hiding, client filtering, tile clipping, or omission from a popup is not a governed redaction or geoprivacy transform;
- maps, tiles, dashboards, indexes, summaries, and generated language remain downstream carriers subordinate to resolvable evidence and accepted policy.

Missing authority or support fails closed with the outcome owned by the selected procedure. Do not infer permission from a public URL, tracked path, plausible filename, document length, validator pass, merge, or absence of an explicit denial.

## Choose the narrowest procedure

| Need | Procedure | Current terminal boundary |
|---|---|---|
| Run deterministic checks without network access | [`NO_NETWORK_TEST_RUNBOOK.md`](NO_NETWORK_TEST_RUNBOOK.md) | Proposal-era procedure; use the verified public-safe fixture validator only for bounded synthetic conformance |
| Refresh an already admitted Flora source | [`SOURCE_REFRESH_RUNBOOK.md`](SOURCE_REFRESH_RUNBOOK.md) | Proposal-era review-handoff design; no source admission, activation, schedule, or live fetch |
| Assess promotion readiness | [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) | Proposal-era lifecycle guidance; no verified Flora candidate, active policy binding, proof packet, transition, or release |
| Plan rollback of an already published Flora release | [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | Proposal-era guidance; no verified prior Flora release or operational rollback target is established |

If more than one procedure appears applicable, preserve the boundaries between them. Fixture validation does not resolve taxonomy, rights, or sensitivity. Source refresh does not admit a source or promote its payload. Promotion readiness does not release. A rollback plan does not mutate public state. Where no safe prior published release exists, use a governed withdrawal or hold posture rather than inventing a rollback target.

## Current child maturity

The labels below describe the four direct child documents at `main@35bb62209569f63af78c6fefe4c85015d3bdceb1`. They do not prove that a live source, qualified actor, accepted policy, evidence bundle, released artifact, deployed consumer, or public carrier exists.

| Procedure | Current document maturity | Verified limit |
|---|---|---|
| [`NO_NETWORK_TEST_RUNBOOK.md`](NO_NETWORK_TEST_RUNBOOK.md) | Substantive proposal-era draft | Correctly emphasizes deterministic, no-network, fail-closed Flora testing, but its broad object inventory, paths, commands, enforcement mechanisms, and CI claims are proposed and do not describe the one current executable profile precisely |
| [`PROMOTION_RUNBOOK.md`](PROMOTION_RUNBOOK.md) | Substantive proposal-era draft | Defines useful Flora gate pressure, but placeholder owners, speculative paths, lifecycle-wide A–G claims, auto-merge language, signing/tooling assumptions, and release semantics require current repository reconciliation |
| [`ROLLBACK_RUNBOOK.md`](ROLLBACK_RUNBOOK.md) | Substantive proposal-era draft | Preserves correction and sensitivity-containment principles, but assumes a published Flora release, prior target, release topology, executors, and paths not established by current evidence |
| [`SOURCE_REFRESH_RUNBOOK.md`](SOURCE_REFRESH_RUNBOOK.md) | Substantive proposal-era draft | Preserves watcher-as-non-publisher and quarantine principles, but named source homes, roles, cadences, endpoints, commands, actors, and live refresh flow remain proposed or conflicted |

Document length is not maturity evidence. Each child must be reconciled separately before its commands or implementation claims are used operationally.

## Current repository evidence

| Surface | CONFIRMED observation at the pinned revision | Bounded conclusion |
|---|---|---|
| This README | Existing tracked file contained only a newline | The local Flora runbook boundary was absent in substance |
| Direct procedure packet | Four tracked long-form procedure files plus this README | A stable four-procedure documentation packet exists |
| [`domain-flora` workflow](../../../.github/workflows/domain-flora.yml) | Runs one deterministic, standard-library, no-network public-safe fixture suite; proof and release dry-run jobs are explicit holds | A successful job proves only the frozen synthetic fixture profile |
| [Flora validator](../../../tools/validators/domains/flora/validate_public_safe_fixture.py) | Requires fixture-only references, generalized fixture support, no release eligibility, and rejects sensitive location fields, coordinate-like values, external references, private-land joins, cultural knowledge, and transform secrets | The validator is a safety-oriented fixture gate, not botanical, source, rights, policy, stewardship, evidence, or release validation |
| [Flora tests](../../../tests/domains/flora/test_flora_smoke.py) | Freeze one positive fixture and six exact negative fixtures; block socket, DNS, and URL access; require stable reason codes and paths without echoing candidate values | The test surface is deterministic and bounded; it does not prove a live Flora pipeline |
| [Source-authority projection](../../../control_plane/source_authority_register.yaml) | `implementation_status: ABSENT`, `completeness: empty`, and `entries: []` | No source is activated or admitted by the central projection |
| [Flora source registry](../../../data/registry/sources/flora/README.md) | Contains a detailed draft README and one `usda_plants.yaml` placeholder; the README records a subtype-first/domain-first topology conflict | No admitted Flora source descriptor or live source authority is established by the inspected lane |
| `usda_plants.yaml` | Declares `status: PROPOSED` and identifies itself as a placeholder created from documentation inventory | It is not source admission, endpoint verification, rights clearance, or botanical evidence |
| [Policy-gate projection](../../../control_plane/policy_gate_register.yaml) | `implementation_status: ABSENT`, `completeness: empty`, and `entries: []` | No active Flora policy binding or policy approval is established |
| [Flora publication policy](../../../policy/domains/flora/flora_publication_gate.rego) | A generated `PROPOSED scaffold` with `default allow := false` | It is fail-closed placeholder code, not an accepted operational evaluator |
| [Flora candidate lane](../../../release/candidates/flora/README.md) | Bounded inventory establishes no child candidate dossier, approved manifest, or published Flora release | Operational promotion, release, and rollback remain unproved |
| CODEOWNERS | Default GitHub review route is `@bartytime4life`; no Flora runbook-specific rule exists | Review routing exists; accountable stewardship, rights-holder or community authority, release authority, and independent approval remain unverified |
| Flat sibling files | [`flora_SOURCE_REFRESH.md`](../flora_SOURCE_REFRESH.md) and [`flora_BACKBONE_ROTATION.md`](../flora_BACKBONE_ROTATION.md) are proposal scaffolds outside this direct child lane | They are drift/lineage signals, not parallel canonical procedure authority |
| Live sources, proof, release, deployment, publication | Not established by this directory or the inspected bounded controls | `HOLD`, `UNKNOWN`, or `NEEDS VERIFICATION` until owning surfaces provide exact-revision evidence |

### What the current executable slice proves

The current `flora-public-safe-fixture` profile can prove that one synthetic candidate:

- contains only fixture-scoped source, taxon, evidence, redaction, and review references;
- carries generalized fixture support without exact, reverse-engineerable, or private-land location detail;
- carries no external URL, coordinate-like value, WKT, access route, collection route, or hidden transform parameter;
- remains explicitly `not_released` and `promotion_eligible: false`;
- produces deterministic, sorted, machine-readable findings for the accepted negative fixtures; and
- completes without network access.

It cannot prove plant identity, occurrence truth, absence, range, abundance, source authority, rights, sensitivity clearance, stewardship approval, a real geoprivacy transform, EvidenceBundle closure, proof construction, candidate readiness, release safety, deployment, or publication.

## Authority and handoff rules

1. Pin the repository revision and identify the exact taxon assertion, object family, source or source product, source role, geography, time scope, sensitivity scope, intended consumer, and requested terminal boundary.
2. Read the selected child's status, evidence boundary, preconditions, stop conditions, outcome vocabulary, and rollback section before using any command or path.
3. Re-resolve every named contract, schema, source record, policy, fixture, validator, evidence object, review record, candidate, release object, and executable entry point from its owning root at the pinned revision.
4. Keep exact or reconstructable sensitive detail and transform secrets out of public channels. A generalized display without a traceable transform and review is not public-safe proof.
5. Use only verified actors and environments. `@bartytime4life` is the verified GitHub route; accountable Flora, taxonomy, source-rights, sensitivity, stewardship, community/sovereignty, evidence, policy, release, rollback, operations, and independent-review assignments remain to be verified where required.
6. Preserve each producer's bounded outcome vocabulary. A current Flora fixture `PASS` means profile conformance only; it does not mean `ALLOW`, `ANSWER`, `APPROVE`, `PROMOTE`, `RELEASE`, or `PUBLISH`.
7. Keep review, merge, source activation, lifecycle transition, release, deployment, promotion, rollback execution, and publication as separate events with separate evidence.
8. When rights, sensitivity, taxonomic identity, source role, or evidence support is unresolved, retain the object in `WORK`, route it to `QUARANTINE`, abstain, restrict, or deny according to the owning controls; do not upgrade uncertainty through prose.

Stop and create a public-safe review handoff when a named path or command does not match the pinned repository; an actor or authority is unresolved; a source descriptor is absent or only a placeholder; taxonomy would be silently reconciled; occurrence, specimen, range, model, vegetation, legal-status, or source roles would collapse; sensitive precision or cultural knowledge could leak; a public-safe transform lacks a traceable receipt and review; or a rollback target has not been independently rechecked under current rights and sensitivity controls.

## Open verification

| Item | Current posture | Smallest truthful next step |
|---|---|---|
| No-network procedure | `PARTIAL / PROPOSAL-ERA` | Reconcile it to the exact `flora-public-safe-fixture` validator, one positive fixture, six negative fixtures, current workflow, and explicit proof/release holds |
| Source-refresh procedure | `PARTIAL / PROPOSAL-ERA` | Reconcile source identity, registry topology, placeholder descriptors, admission prerequisites, no-network replay, quarantine, and live-network graduation without activating a source |
| Promotion procedure | `PARTIAL / PROPOSAL-ERA` | Replace speculative A–G, auto-merge, signing, path, and release claims with current bounded readiness controls and explicit candidate/policy/proof/release holds |
| Rollback procedure | `PARTIAL / PROPOSAL-ERA` | Reconcile it to the current empty candidate inventory, shared rollback objects if present, first-release withdrawal/hold behavior, and operational-executor holds |
| Source registry topology | `CONFLICTED / NEEDS VERIFICATION` | Select one canonical descriptor lane or create an accepted migration/compatibility decision; do not maintain divergent subtype-first and domain-first records |
| Source admission | `HOLD / NOT ESTABLISHED` | Replace placeholders only through a governed SourceDescriptor admission review with rights, role, sensitivity, cadence, endpoint, and authority evidence |
| Flora policy | `SCAFFOLD / NOT ACTIVE` | Define and review accepted Flora policy semantics, fixtures, evaluator binding, version/digest, negative tests, and fail-safe runtime behavior |
| Proof and release | `WORKFLOW HOLD` | Establish immutable candidate identity, EvidenceBundle and citation closure, public-safe transform support, review, correction, withdrawal, rollback, and safe dry-run execution before graduation |
| Sensitivity documentation | `CONFLICTED` | Reconcile overlapping Flora sensitivity documents through the owning governance path without silently creating a second authority |
| Flat sibling scaffolds | `DRIFT / LINEAGE` | Inventory consumers and choose migrate, redirect, retain, or retire through a separate reviewed change; do not rename or delete them in this README update |
| Parent runbook index | `STALE` | Recompute the parent inventory only after current lane updates settle; keep this Flora change one-file and local |
| Accountable roles | `NEEDS VERIFICATION` | Record verified scope, authority, separation, community or rights-holder obligations, and revocation for each required Flora role |
| Live Flora operations | `HOLD / UNKNOWN` | Require admitted sources, executable connectors, version-pinned taxonomy, rights and sensitivity closure, evidence, policy, review, release topology, correction, rollback, monitoring, and current runtime evidence |

## Related surfaces

- Parent runbook index: [`docs/runbooks/README.md`](../README.md)
- Flora domain boundary: [`docs/domains/flora/README.md`](../../domains/flora/README.md)
- Flora sensitivity documentation: [`docs/domains/flora/SENSITIVITY.md`](../../domains/flora/SENSITIVITY.md)
- Directory Rules: [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)
- Accepted placement decision: [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- Flora workflow: [`.github/workflows/domain-flora.yml`](../../../.github/workflows/domain-flora.yml)
- Bounded validator: [`tools/validators/domains/flora/validate_public_safe_fixture.py`](../../../tools/validators/domains/flora/validate_public_safe_fixture.py)
- Focused tests: [`tests/domains/flora/test_flora_smoke.py`](../../../tests/domains/flora/test_flora_smoke.py)
- Flora source registry: [`data/registry/sources/flora/README.md`](../../../data/registry/sources/flora/README.md)
- Flora candidate lane: [`release/candidates/flora/README.md`](../../../release/candidates/flora/README.md)

## Maintenance and document rollback

Update this README when a direct child is added, removed, renamed, materially re-scoped, or reconciled to current repository evidence; when taxonomy, source-role, rights, sensitivity, geoprivacy, evidence, policy, release, correction, or rollback boundaries change; or when accountable authority, executable validation, live-source, runtime, deployment, promotion, or publication evidence changes.

This is a documentation-only change. Before merge, close or abandon its draft pull request. After merge, revert the documentation commit or submit a smaller reviewed forward correction. Blob `8b137891791fe96927ad78e64b0aad7bded08bdc` restores the prior one-byte file, but reverting this README would not change source, taxonomy, evidence, policy, lifecycle, release, runtime, rollback, or public state.

[Back to top](#top)
