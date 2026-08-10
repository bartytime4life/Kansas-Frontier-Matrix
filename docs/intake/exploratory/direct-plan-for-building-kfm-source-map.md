<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/direct-plan-for-building-kfm-source-map
title: Direct Plan for Building KFM - Governed Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; substantially-represented; end-to-end-proof-held
owners: OWNER_TBD - architecture steward; hydrology steward; evidence steward; release steward; apps steward; docs steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; intake; exploratory; architecture-reconciliation; privacy-minimized
truth_posture: cite-or-abstain; current-repository claims are pinned to the inspected snapshot
owning_root: docs/
responsibility: Preserve a privacy-minimized reconciliation of a private KFM build plan against current repository evidence without importing stale paths, treating component presence as an end-to-end release, or promoting the source into architecture authority.
source_class: connected private document
source_title: Direct plan for building KFM
source_version: UNKNOWN - no edition declared in the reviewed text
source_status: non-authoritative reconstruction-derived implementation plan
source_disclosure: privacy-minimized; source text, connector locator, private link, timestamps, digest, and file size omitted
repository: bartytime4life/Kansas-Frontier-Matrix
repository_snapshot: 8a671552785b773364f01d2e76d8ca6892a405ea
repository_verified_on: 2026-08-10
related:
  - ./README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - ../../adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md
  - ../../architecture/system-context.md
  - ../../domains/hydrology/THIN_SLICE.md
  - ../../../control_plane/root_registry.yaml
  - ../../../control_plane/object_family_register.yaml
  - ../../../contracts/evidence/evidence_ref.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../contracts/runtime/runtime_response_envelope.md
  - ../../../contracts/release/release_manifest.md
  - ../../../contracts/correction/correction_notice.md
  - ../../../apps/governed-api/README.md
  - ../../../apps/explorer-web/README.md
  - ../../../.github/workflows/hydrology-proof-slice.yml
tags: [kfm, intake, build-plan, hydrology, evidence, governed-api, explorer-web, release, rollback, reconciliation]
notes:
  - "The connected document was read in full for this triage. Source text and private connector metadata are deliberately excluded from the repository record."
  - "The source repeatedly attributes recommendations to an unnamed reconstruction study; that study was not independently identified or accepted through this source review."
  - "Current-main presence remains distinct from adoption, execution, deployment, release, publication, and end-to-end proof."
  - "This file creates no doctrine, ADR decision, contract, schema, policy, source, evidence, receipt, proof, release, dependency, deployment, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Direct Plan for Building KFM - governed source map

> **Outcome:** The source's authority-settlement, trust-object, governed hydrology,
> map-shell, correction, rollback, and bounded-AI responsibilities are
> substantially represented on current main. The remaining material gap is not
> another broad build wave: it is reproducible, same-candidate end-to-end proof
> that the existing hydrology, evidence, policy, release, API, drawer, and Focus
> surfaces compose without bypass. That proof remains `NEEDS VERIFICATION` and is
> not created by this documentation-only change.

> [!IMPORTANT]
> This source map records design lineage and current-repository corrections. It
> does not reproduce the private document, accept its unnamed reconstruction
> study as authority, authorize a hydrology source, or treat paths, tests,
> workflows, fixtures, and app components as proof of a deployed public release.

**Quick links:** [Source boundary](#source-boundary-and-review-method) ·
[Placement](#directory-rules-and-authority-basis) ·
[Reconciliation](#repository-grounded-reconciliation) ·
[Residual gap](#retained-non-duplicate-gap) ·
[Unsafe transfers](#unsafe-direct-transfers) ·
[Validation](#validation-and-review-boundary) ·
[Rollback](#rollback-and-correction)

## Source boundary and review method

### Privacy-minimized source identity

| Field | Bounded value |
|---|---|
| Supplied title | *Direct plan for building KFM* |
| Declared edition | `UNKNOWN` - no edition was declared in the reviewed text |
| Source posture | Reconstruction-derived implementation plan; non-authoritative input |
| Repository comparison | `main@8a671552785b773364f01d2e76d8ca6892a405ea`, inspected `2026-08-10` |
| Private material | Source text, Drive locator, private link, connector timestamps, digest, and file size intentionally omitted |

This pass:

1. read the connected document in full, including its target state, seven build
   phases, minimum test list, and proposed first three pull requests;
2. treated its path, maturity, runtime, test, deployment, and release statements
   as dated claims requiring current verification;
3. searched current GitHub code, pull requests, commits, and branches for exact
   title or intended source-map collisions;
4. inspected accepted Directory Rules, path decisions, responsibility roots,
   control-plane projections, trust-object families, hydrology thin-slice
   surfaces, apps, fixtures, validators, tests, and workflows on current main;
5. separated presence from adoption, execution, end-to-end composition,
   deployment, release, publication, and public fitness; and
6. retained only the source-specific reconciliation and an explicit evidence
   threshold for future work.

[Back to top](#top)

## Directory Rules and authority basis

Accepted [Directory Rules v2](../../doctrine/directory-rules.md), adopted through
[ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md), place an
artifact by its single authority owner and return `HOLD` when ownership or
authority is unresolved. The [exploratory intake README](./README.md) defines
this lane as a noncanonical waiting room for source reconciliation, current-
repository correction, routing, and rejection without accidental promotion.

Path decision for this file:

```yaml
path_decision:
  artifact: direct-plan-for-building-kfm-source-map
  proposed_path: docs/intake/exploratory/direct-plan-for-building-kfm-source-map.md
  artifact_kind: human_document
  authority_owner: documentation_intake
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: global
  scope_id: kfm-build-plan-lineage
  exposure: public
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/intake/exploratory/README.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-PLACE-001
    - DIR-PLACE-005
  outcome: PLACE
```

The file does not belong under architecture or doctrine because the source
cannot adopt system authority. It does not belong under contracts, schemas, or
policy because it defines no object meaning, machine shape, or normative rule.
It does not belong under data or release because it is neither lifecycle input
nor a promotion, correction, withdrawal, rollback, or publication decision.

[Back to top](#top)

## Repository-grounded reconciliation

Disposition terms:

- `REPRESENTED` - current main contains a repository-native surface for the
  responsibility.
- `CORROBORATIVE` - the source reinforces a governing boundary without adding a
  distinct owner or object.
- `NARROWED` - current evidence supports a smaller claim than the source makes.
- `HOLD` - a continuation is plausible, but its evidence or authority gate is
  unresolved.
- `REJECT_AS_PARALLEL` - direct transfer would duplicate current authority.
- `NEEDS VERIFICATION` - a concrete runtime, hosted, or same-candidate check was
  not proved by this pass.

| Source contribution | Current-main evidence | Disposition | Boundary |
|---|---|---|---|
| Freeze schema, API, browser-shell, compatibility-root, and control-plane authority before feature work | Accepted [schema-home](../../adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md), [governed-API](../../adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md), and [Explorer Web](../../adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md) decisions are present with root and object-family projections. | `REPRESENTED` | The source's example `ADR-0001-schema-home.md`, underscore API spelling, and multi-shell choice list are dated proposals, not current paths. |
| Preserve responsibility roots and the governed lifecycle; deny direct public access to internal or sensitive material | Current [system context](../../architecture/system-context.md) and Directory Rules retain the trust membrane, finite outcomes, lifecycle, sensitivity, correction, and rollback boundaries. | `CORROBORATIVE` | Repetition in an intake plan adds no doctrine or policy authority. |
| Build the named trust-object wave before domain scale | EvidenceRef, EvidenceBundle, runtime response, policy, promotion, release, layer, review, correction, and rollback families have contract/schema/fixture/validator/test surfaces on current main. | `REPRESENTED / NARROWED` | Presence and local fixture coverage do not prove every family is mature, uniquely placed, integrated, or operational. The [CorrectionNotice contract](../../../contracts/correction/correction_notice.md), for example, records placeholder and placement holds. |
| Prove one public-safe hydrology lane through source admission, evidence resolution, release, map, drawer, and bounded Focus outcomes | Hydrology documentation, public-safe fixtures, a thin-slice workflow, governed API, Explorer hydrology surfaces, Evidence Drawer, and Focus components are present. | `REPRESENTED / NEEDS VERIFICATION` | No same-candidate execution receipt, deployed public route, admitted live source, released PMTiles carrier, or production publication was proved in this pass. |
| Complete the governed map shell with time, visible negative states, and accessibility | Explorer Web contains map-runtime, time-banner, drawer, Focus, trust-header, citation, and browser-test surfaces. | `REPRESENTED / NEEDS VERIFICATION` | File and test presence do not prove deployment, assistive-technology conformance, current browser-matrix results, or release-bound data flow. |
| Close catalog, proof, promotion, correction, withdrawal, and rollback before scaling domains | Catalog, proof, promotion, release, correction, rollback contracts, schemas, fixtures, runbooks, and workflows are present in their responsibility roots. | `REPRESENTED / PARTIAL` | Current surfaces retain explicit owner, schema, validator, integration, and operational holds; a broad completion claim would overstate the evidence. |
| Expand soil, habitat, ecological, atmosphere, geology, infrastructure, hazards, and people/DNA/land lanes in a fixed order | Domain documentation, contracts, schemas, fixtures, and UI surfaces exist across multiple named lanes. | `REJECT_AS_SEQUENCE_AUTHORITY` | A private plan cannot set current portfolio priority. Each domain remains subject to its own rights, sovereignty, sensitivity, evidence, policy, steward, release, and rollback gates. |
| Add review console and provider-neutral AI only after evidence closure works | Read-only review and governed-AI surfaces are present, while system doctrine keeps AI subordinate to EvidenceBundle and governed finite outcomes. | `CORROBORATIVE / HOLD` | Provider admission, live model access, citation closure, reviewer authority, deployment, and public AI readiness remain separate decisions and evidence burdens. |
| Implement the source's minimum test suite | Current main contains extensive contract, domain, API, UI, release, rollback, citation, sensitivity, identity, and reproducibility tests and workflows. | `REPRESENTED / NEEDS VERIFICATION` | This pass did not claim exhaustive coverage, current ruleset coupling, or all-workflow health from repository presence alone. |
| Execute the source's first three pull requests as one roadmap | Their authority settlement, trust-object, and hydrology responsibilities have since been distributed across many repository-native changes. | `REJECT_AS_PARALLEL` | Replaying the three broad PRs would overwrite lineage, collapse owners, and count existing work as new implementation. |

The source uses accurate KFM vocabulary and preserves useful sequencing
principles, but it is a dated synthesis. Its unnamed reconstruction study,
example paths, and completion language do not outrank current accepted decisions
or exact repository evidence.

[Back to top](#top)

## Retained non-duplicate gap

The distinct gap is a **same-candidate hydrology trust-path proof**, not a new
object family or a second architecture plan. Future work should begin only when
one immutable public-safe candidate can be followed through existing owners and
produce inspectable evidence for all of these checks:

1. a governed SourceDescriptor and rights/sensitivity posture bind the candidate
   without embedding private or precise sensitive data;
2. every public claim resolves an EvidenceRef to an EvidenceBundle at the same
   candidate identity and release boundary;
3. validation, policy, review, promotion, release, correction, and rollback refs
   are internally consistent and independently reviewable;
4. the released carrier digest and layer manifest are the exact artifacts
   admitted by the governed API and Explorer runtime;
5. click-to-drawer renders only the public-safe projection and exposes stale,
   withheld, restricted, correction, and rollback state where applicable;
6. Focus returns only finite `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` outcomes,
   with `ANSWER` impossible when citation-safe support is absent;
7. public clients cannot retrieve internal lifecycle paths, raw evidence payloads,
   model-provider details, or steward-only diagnostics; and
8. a deterministic rollback or withdrawal drill targets the same release and
   leaves an auditable receipt.

Until one exact execution binds those claims, the truthful state is `NEEDS
VERIFICATION`. Separate passing component tests must not be aggregated into an
end-to-end release claim by prose.

[Back to top](#top)

## Unsafe direct transfers

| Source pattern | Why direct transfer is unsafe | Required correction |
|---|---|---|
| Copy the plan into architecture as the current build authority | It would create a second broad architecture spine and import dated path and maturity assertions. | Preserve this intake map; update only responsibility-specific current docs when verified behavior changes. |
| Create or rename paths exactly as the source lists them | Accepted ADRs and current responsibility roots already settle several names differently. | Use the adopted Directory Rules, accepted ADRs, root registry, and exact current consumers. |
| Treat the object-family list as evidence that every family is complete | Several families retain draft, owner, placeholder, placement, integration, or operational holds. | Inspect each owning contract, schema, validator, fixture, workflow, and consumer before claiming maturity. |
| Treat hydrology files and green component tests as a public release | Presence and isolated validation do not prove live source admission, same-candidate composition, release, deployment, or public safety. | Require pinned end-to-end evidence and release/rollback receipts. |
| Use real sensitive locations, living-person, DNA, archaeology, rare-species, or infrastructure data to make the proof realistic | Precision and realism can increase disclosure risk without improving contract proof. | Use synthetic or public-safe minimized fixtures and preserve deny, quarantine, redaction, generalization, and staged-access outcomes. |
| Make AI or the map the root truth surface | Both are downstream carriers and can overstate evidence if they bypass the governed API. | Resolve EvidenceBundle, policy, review, and release state before interpretation or rendering. |
| Recreate the broad first-three-PR sequence | Current main already distributes those responsibilities across accepted decisions and owners. | Open only a responsibility-specific change after an exact residual gap and collision check. |

[Back to top](#top)

## Recommended next bounded action

**No new implementation object is justified by this source alone.**

This source map is the complete bounded adaptation for the inspected snapshot.
A follow-on change should begin only from reproducible evidence of a broken or
missing link in the same-candidate hydrology path, such as:

1. an existing hydrology candidate whose EvidenceRef cannot resolve through the
   governed API without an internal-path leak;
2. a released carrier whose digest or layer-manifest identity diverges between
   release, API, and Explorer admission;
3. a finite-outcome or citation validator that accepts `ANSWER` without
   candidate-bound support; or
4. a rollback drill that cannot restore or withdraw the exact release under
   test.

Any follow-on must extend the existing owner, use synthetic or independently
cleared data, keep every negative state explicit, include validation and
rollback, and remain separate from this intake record.

[Back to top](#top)

## Validation and review boundary

This source map is complete only if:

- the connected document was read in full;
- source text and private Drive metadata are absent;
- current-repository conclusions remain pinned to
  `main@8a671552785b773364f01d2e76d8ca6892a405ea`;
- every linked current-main path resolves;
- current object, hydrology, API, UI, release, correction, and rollback families
  are not counted again as new implementation;
- stale example paths and the unnamed reconstruction-study dependency remain
  explicit;
- presence is not upgraded into end-to-end execution, deployment, release,
  publication, accessibility, or public-fitness proof;
- sensitive and private material is not copied into the repository;
- no doctrine, ADR, contract, schema, policy, source, evidence, lifecycle,
  receipt, proof, release, dependency, deployment, or publication state changes;
  and
- human review confirms the no-new-object and same-candidate-proof dispositions.

[Back to top](#top)

## Rollback and correction

Before merge, close the draft pull request and abandon its isolated branch.
After an authorized merge, revert this single additive documentation file. No
source, lifecycle state, runtime, release, deployment, or public artifact
requires restoration.

If a repository path, implementation fact, source interpretation, privacy
boundary, or responsibility classification proves wrong:

1. preserve this source map as dated lineage;
2. append a correction or superseding map instead of converting the source into
   authority;
3. re-run current-main, exact-path, code, branch, pull-request, and consumer
   checks;
4. update only the affected disposition and verification need; and
5. route behavior changes through their owning contract, schema, policy,
   fixture, validator, test, workflow, receipt, review, release, correction, and
   rollback surfaces.

[Back to top](#top)
