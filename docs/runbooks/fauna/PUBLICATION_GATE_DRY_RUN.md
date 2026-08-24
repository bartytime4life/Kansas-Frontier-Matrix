<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/fauna/publication-gate-dry-run
title: Fauna — Publication Gate Dry-Run Runbook
type: runbook; operational-procedure; domain-lane; sensitive-domain; publication-denial; non-authoritative
version: v1.0.0
prior_version: PROPOSED scaffold
status: draft; repository-grounded; shared-synthetic-publication-denial-executable; fauna-candidate-absent; fauna-domain-dry-run-held; no-write; non-publisher
owners:
  - "@bartytime4life — verified GitHub review route only"
owner_status: >-
  Fauna, taxonomy, source, rights/stewardship, sensitivity/geoprivacy,
  evidence, policy, validation, independent-review, release, correction,
  rollback, public-surface, and operations assignments remain NEEDS
  VERIFICATION; CODEOWNERS routing does not create those authorities.
created: NEEDS VERIFICATION — the prior scaffold carried no creation date
updated: 2026-08-24
policy_label: public-review; fauna; publication-gate; dry-run; synthetic-denial; sensitive-location; fail-closed; no-release-authority; no-publication-authority
current_path: docs/runbooks/fauna/PUBLICATION_GATE_DRY_RUN.md
owning_root: docs/
responsibility: >-
  Document the exact bounded, no-write publication-gate rehearsal currently
  available to the Fauna lane; distinguish the shared synthetic denial profile
  from a candidate-specific Fauna dry run; and produce a public-safe review
  handoff without creating source admission, taxonomic authority, evidence,
  policy, review, promotion, release, deployment, or publication authority.
truth_posture: cite-or-abstain
truth_labels: [CONFIRMED, PROPOSED, UNKNOWN, NEEDS VERIFICATION, CONFLICTED, HOLD]
authority_class: explanatory operational documentation
canonical_relationship: same-path modernization; no new or parallel authority
path_posture: PLACE
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  content_inspection_commit: c3b39fb27fd7ca46c41f5b5133149f1d8cd73996
  branch_base_commit: c3b39fb27fd7ca46c41f5b5133149f1d8cd73996
  target_prior_blob: dff3b4a32ccbda552931775c67bf5aadcfad8c99
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  fauna_candidate_readme_blob: 653277efe3a44a96c29af481a73d7d90c41443ce
  fauna_proof_readme_blob: 70c2501e6d7c8ff4beeae7577fde9acd6b720b2e
  fauna_manifest_readme_blob: 9487abafcc0c4647618e3295efb3224b17eacd83
  fauna_published_readme_blob: 24a276f0e9b31ab5e7abc7dfe0b554c9dcba4029
  source_authority_register_blob: 32729857bc8eb5001acb37b8ee8e60bcb6e0dc50
  fauna_workflow_blob: 0edc73a77ee0ddb3193db2c0386ed6ac685b139a
  shared_dry_run_tool_blob: 5fed3a16aa0915b9233861048fc6a1e676e0ed8f
  shared_dry_run_test_blob: a5a427c20f52aa0303b334ce876781c6364a2d79
  promotion_gate_readme_blob: e729df0cc007e8cf0d9811afc25ec1f5ffbdffdd
  promotion_runbook_blob: e3c4ce643d77d887a8b74cc34f688c2d08613f5b
inspection_boundary: >-
  Current-session GitHub reads covered the target scaffold; accepted Directory
  Rules decision; CODEOWNERS; the Fauna candidate, proof, manifest, published,
  source-authority, promotion-policy, promotion-readiness, workflow, fixture,
  test, correction, withdrawal, and rollback boundaries; and the shared
  publication-denial executable and workflow. Repository-native commands were
  not run in a mounted checkout while this document was authored. No live or
  restricted Fauna source, animal occurrence, exact location, source credential,
  production policy evaluator, public carrier, release service, or lifecycle
  transition was exercised.
related:
  - ../README.md
  - ../RELEASE_DRY_RUN.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/fauna/README.md
  - ../../domains/fauna/RELEASE_INDEX.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ./EBD_DERIVATIVE_RELEASE.md
  - ./ROLLBACK_RUNBOOK.md
  - ../../../Makefile
  - ../../../.github/CODEOWNERS
  - ../../../.github/workflows/domain-fauna.yml
  - ../../../.github/workflows/release-dry-run.yml
  - ../../../control_plane/source_authority_register.yaml
  - ../../../release/candidates/fauna/README.md
  - ../../../release/manifests/fauna/README.md
  - ../../../data/proofs/fauna/README.md
  - ../../../data/published/fauna/README.md
  - ../../../policy/promotion/README.md
  - ../../../tools/release/README.md
  - ../../../tools/release/release_dry_run.py
  - ../../../tools/validators/promotion_gate/README.md
  - ../../../tests/release/test_publication_deny_dry_run.py
tags: [kfm, fauna, runbook, publication-gate, dry-run, denial, promotion, evidence, geoprivacy, review, release, rollback, fail-closed]
notes:
  - "v1.0.0 replaces the inventory-generated scaffold with a repository-grounded publication-gate rehearsal and review-handoff procedure."
  - "The implemented shared helper proves five synthetic publication-denial paths only; it does not accept or assemble a Fauna candidate."
  - "The domain-fauna workflow still records an explicit hold because no accepted Fauna release dry-run command or candidate-manifest contract exists."
  - "No child Fauna candidate dossier, Fauna proof artifact, Fauna manifest instance, or Fauna published carrier was present in the bounded direct-child inventories."
  - "This document changes no source, candidate, data, contract, schema, policy, fixture, validator, workflow, receipt, proof, review, decision, manifest, correction, withdrawal, rollback record, lifecycle state, deployment, or public surface."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna — Publication Gate Dry-Run Runbook

> **Run the repository's bounded publication-denial rehearsal, evaluate the Fauna lane's candidate-specific publication prerequisites, and produce a public-safe review handoff—without assembling a release, weakening sensitive-location controls, or implying that a green check is promotion, release, deployment, or publication.**

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#current-repository-posture)
[![Shared denial profile: executable](https://img.shields.io/badge/shared%20denial%20profile-executable-1f883d?style=flat-square)](#shared-publication-denial-profile)
[![Fauna candidate: absent](https://img.shields.io/badge/Fauna%20candidate-NOT__ESTABLISHED-critical?style=flat-square)](#current-repository-posture)
[![Fauna dry run: hold](https://img.shields.io/badge/Fauna%20dry%20run-HOLD-d4a72c?style=flat-square)](#current-fauna-publication-closure-matrix)
[![Network: denied](https://img.shields.io/badge/network-denied-1f883d?style=flat-square)](#no-network-and-no-write-contract)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-boundary-and-review-handoff)

> [!IMPORTANT]
> **The currently implemented command is a shared synthetic publication-denial profile, not a Fauna candidate dry run.** It starts from a repository-controlled synthetic promotion packet, applies five negative mutations, verifies that publication remains blocked, writes no file, and accepts no caller-controlled candidate content.

> [!CAUTION]
> **Current Fauna publication-gate result: `HOLD`.** The Fauna candidate lane has no verified child dossier; the Fauna proof lane has no proof artifact; the Fauna manifest lane has no manifest instance; the central source-authority projection is empty; promotion policy is inactive; and the domain workflow explicitly records that no accepted Fauna release dry-run command or candidate-manifest contract exists.

> [!WARNING]
> **Never place exact or reverse-engineerable animal locations in dry-run inputs, logs, reports, pull requests, screenshots, workflow summaries, or handoff packets.** Sensitive taxa, nests, dens, roosts, hibernacula, spawning or breeding sites, aggregation sites, telemetry paths, private-land joins, access clues, observer-linked detail, steward-controlled records, and geoprivacy transform parameters fail closed.

**Quick navigation:** [Purpose](#purpose-scope-and-terminal-boundary) · [Placement](#authority-placement-and-document-precedence) · [Posture](#current-repository-posture) · [Terms](#terms-and-anti-collapse-rules) · [Roles](#roles-and-separation-of-duties) · [Contract](#no-network-and-no-write-contract) · [Preflight](#preflight-and-mandatory-stop-conditions) · [Commands](#current-executable-command-map) · [Shared profile](#shared-publication-denial-profile) · [Procedure](#operator-procedure) · [Fauna gates](#fauna-specific-publication-gates) · [Matrix](#current-fauna-publication-closure-matrix) · [Outcomes](#finite-outcomes-and-reason-code-boundary) · [Handoff](#authority-boundary-and-review-handoff) · [CI](#hosted-ci-and-exact-head-interpretation) · [Recovery](#correction-withdrawal-and-rollback-boundary) · [Graduation](#graduation-criteria-for-a-candidate-specific-fauna-dry-run) · [Open work](#open-verification-register) · [Evidence](#evidence-basis) · [Document rollback](#document-change-rollback) · [Checklist](#appendix-a-operator-checklist)

---

<a id="purpose-scope-and-terminal-boundary"></a>

## Purpose, scope, and terminal boundary

Use this runbook for two separate operations that must remain visibly distinct:

1. **Execute the shared synthetic publication-denial profile** to prove that five known unsafe or unsupported packet mutations remain blocked at an exact repository revision.
2. **Assess whether one specifically identified Fauna candidate has the support required for a candidate-specific no-write publication-gate rehearsal.**

At the current repository checkpoint, operation 1 is executable and operation 2 stops at `HOLD` because no Fauna candidate dossier or accepted domain dry-run contract exists.

The KFM lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This runbook does not execute that lifecycle. It documents a rehearsal and a fail-closed assessment of readiness to rehearse.

### In scope

- freezing the exact repository revision and target scope;
- verifying that the shared helper, tests, and workflow remain synthetic, deterministic, no-network, and no-write;
- running `make release-dry-run` and interpreting only its declared five-case result;
- running the generic bounded A–G readiness fixtures through `make publish-check`;
- running the accepted synthetic Fauna fixture-safety suite;
- inventorying candidate, proof, manifest, and published Fauna lanes without reading protected payloads;
- assessing source, taxonomy, evidence, rights, sensitivity, geoprivacy, validation, policy, review, correction, withdrawal, rollback, and public-carrier closure;
- reporting exact-head hosted results without treating held jobs as implemented release machinery; and
- preparing a public-safe review handoff.

### Out of scope

- live source access, connector execution, source admission, source activation, or credential use;
- validation of real animal occurrence, range, migration, mortality, disease, conservation, telemetry, or sensitive-site records;
- choosing or executing a production geoprivacy transform;
- resolving a real `EvidenceRef` to an authoritative `EvidenceBundle`;
- evaluating the inactive promotion Rego stubs as production policy;
- authenticating a reviewer, stewardship assignment, rights-holder decision, or release authority;
- assembling a Fauna candidate, `PromotionDecision`, `PromotionReceipt`, `ReleaseManifest`, proof, signature, rollback card, correction notice, or withdrawal notice;
- writing to any lifecycle, receipt, proof, release, cache, deployment, or public-serving surface; and
- promotion, release, deployment, publication, correction execution, withdrawal execution, or rollback execution.

### Terminal boundary

The maximum current result is:

```text
shared synthetic denial profile: PASS | ABSTAIN | DENY | ERROR
Fauna candidate-specific gate:   HOLD | DENY | ABSTAIN | ERROR
review handoff:                  READY only when explicitly supported
public or lifecycle state:       UNCHANGED
```

`READY` means ready for accountable review only. It is not `APPROVE`, `PROMOTED`, `RELEASED`, or `PUBLISHED`.

[Back to top](#top)

---

<a id="authority-placement-and-document-precedence"></a>

## Authority, placement, and document precedence

### Directory Rules result

**`PLACE` — CONFIRMED for this same-path update.**

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). This tracked file is a human operational procedure under `docs/runbooks/`, with `fauna` as a domain segment. The update creates no new root, lane, alias, mirror, schema home, policy home, release home, proof home, or publication path.

| Responsibility | Owning surface | This runbook's role |
|---|---|---|
| Human operating procedure | `docs/runbooks/fauna/` | Explain exact bounded execution and handoff |
| Fauna meaning and sensitivity intent | `docs/domains/fauna/`, `contracts/domains/fauna/` | Cite; do not redefine |
| Machine shape | `schemas/` | Do not invent or amend |
| Source admission and rights | source registry and policy authorities | Require accepted pointers |
| Evidence and proof | `data/proofs/` and evidence authorities | Require resolution; do not manufacture |
| Policy source | `policy/` | Record current state; do not evaluate by prose |
| Validators and tests | `tools/validators/`, `tests/`, `fixtures/` | Document exact bounded entry points |
| Release decisions and manifests | `release/` | Require governed records; do not create |
| Published public-safe carriers | `data/published/` | Inspect public-safe inventory only; no writes |
| Public clients | governed APIs and released artifacts | Outside this procedure |

The local [`docs/runbooks/fauna/README.md`](./README.md) remains a one-byte placeholder at the evidence checkpoint. This runbook does not substitute for that missing local lane boundary. The parent [runbook index](../README.md) and accepted responsibility-root rules remain the broader navigation and authority surfaces.

### Current behavior outranks proposal-era prose

The broad [Release Dry-Run Runbook](../RELEASE_DRY_RUN.md) remains useful as planning lineage, but its proposal-era statements about assembling candidate outputs, producing decisions, or drafting manifests do not describe the current implemented helper. For current behavior, prefer:

1. [`tools/release/release_dry_run.py`](../../../tools/release/release_dry_run.py);
2. [`tests/release/test_publication_deny_dry_run.py`](../../../tests/release/test_publication_deny_dry_run.py);
3. the exact [`Makefile`](../../../Makefile) targets;
4. [`.github/workflows/release-dry-run.yml`](../../../.github/workflows/release-dry-run.yml); and
5. [`.github/workflows/domain-fauna.yml`](../../../.github/workflows/domain-fauna.yml).

If those surfaces disagree with this runbook, stop and update the documentation rather than selecting whichever wording permits publication.

[Back to top](#top)

---

<a id="current-repository-posture"></a>

## Current repository posture

The following conclusions are bounded to `main@c3b39fb27fd7ca46c41f5b5133149f1d8cd73996`.

| Surface | Status | Safe conclusion |
|---|---|---|
| This target | **CONFIRMED prior scaffold** | The prior 660-byte file says to fill in authoritative content. It contains no executable procedure. |
| Directory governance | **CONFIRMED / accepted** | `docs/runbooks/fauna/` is the correct same-path human procedure lane. |
| Fauna candidate lane | **CONFIRMED / empty of child dossiers** | Direct-child inventory contains only the parent README. No active candidate is established. |
| Fauna proof lane | **CONFIRMED / guidance only** | Direct-child inventory contains README plus `.gitkeep`; no Fauna proof artifact is established. |
| Fauna manifest lane | **CONFIRMED / guidance only** | Direct-child inventory contains README plus `.gitkeep`; no Fauna manifest instance is established. The singular/plural manifest-home question remains unresolved. |
| Fauna published lane | **CONFIRMED / guidance only** | Direct-child inventory contains README plus `.gitkeep`; no Fauna published carrier is established. |
| Source-authority projection | **CONFIRMED / empty and non-authoritative** | Status is `PROPOSED`, implementation is `ABSENT`, completeness is `empty`, and `entries: []`. |
| Shared publication-denial helper | **CONFIRMED executable / synthetic** | Five negative mutations are replayed over one repository-controlled synthetic packet. No caller candidate is accepted. |
| Shared denial tests | **CONFIRMED executable** | Exact case polarity, no-authority claims, no-network behavior, deterministic output, and no file emission are tested. |
| Generic A–G readiness validator | **CONFIRMED executable / bounded** | `PASS` means only `APPROVE_READY` over declared synthetic closure. References and authority are not authenticated. |
| Promotion policy | **CONFIRMED proposed and inactive** | Two local Rego files are no-op stubs, have no operative denial body, and are not executed by the promotion workflow. |
| Fauna fixture suite | **CONFIRMED executable / synthetic** | Two positive and five negative public-safe fixtures test bounded hygiene. They are ineligible for promotion and publication. |
| Fauna proof producer | **CONFIRMED workflow hold** | No accepted Fauna proof producer or deterministic proof command is wired. |
| Fauna publication dry run | **CONFIRMED workflow hold** | No accepted Fauna release dry-run command or candidate-manifest contract is wired. |
| Review route | **CONFIRMED routing only** | CODEOWNERS routes to `@bartytime4life`; functional authority and independence remain unverified. |
| Release, deployment, publication | **NOT ESTABLISHED** | No current inspected surface creates those effects for Fauna. |

### Current bounded determination

```text
shared synthetic publication-denial profile = IMPLEMENTED / BOUNDED
generic declared readiness profile          = IMPLEMENTED / BOUNDED
Fauna fixture-safety profile                 = IMPLEMENTED / BOUNDED
Fauna candidate dossier                      = ABSENT
Fauna candidate proof                        = ABSENT
Fauna candidate manifest                     = ABSENT
Fauna domain publication dry run             = HOLD
Fauna release or publication                 = NOT ESTABLISHED
```

Repository-native commands were not run in a mounted checkout while this documentation revision was authored. Commands below are therefore documented entry points, not reported execution results for this revision.

[Back to top](#top)

---

<a id="terms-and-anti-collapse-rules"></a>

## Terms and anti-collapse rules

| Term | Meaning in this runbook | Must not be collapsed into |
|---|---|---|
| **Shared publication-denial profile** | Synthetic helper that proves five unsafe mutations remain blocked | Candidate-specific Fauna validation |
| **Generic promotion readiness** | A–G declared-packet validator; `PASS` means `APPROVE_READY` | Promotion decision, release approval, or publication |
| **Fauna fixture-safety profile** | Synthetic public-safe fixture hygiene | Real taxonomy, source admission, evidence, or geoprivacy approval |
| **Fauna publication-gate dry run** | A future candidate-specific no-write rehearsal over accepted Fauna support | The shared synthetic helper |
| **Promotion** | Governed lifecycle transition | File move, PR, merge, workflow result, badge, or deployment |
| **Release** | Accountable release-family decision and bound records | Schema-valid manifest-shaped file |
| **Publication** | Authorized exposure of a released public-safe carrier | Presence under `data/published/`, map visibility, or public URL |
| **Receipt** | Process memory about what ran | Proof, decision, or authority |
| **Proof** | Support for a bounded claim or gate | Receipt, catalog, or release record |
| **Manifest** | Release-governance record binding included artifacts and support | Payload, proof, or decision by itself |
| **Rollback card** | Governed rollback decision/support record | Executed rollback or restored public state |
| **Workflow success** | Exact workflow completed according to its current definition | All functional holds graduated |

### Core anti-collapse rules

- A `PASS` from `make release-dry-run` means the **denial controls worked**, not that a release is ready.
- The `evidence_missing` case returns `ABSTAIN`, yet its publication outcome remains denied. Insufficient support is not a soft pass.
- A `PASS` from `make publish-check` means declared synthetic closure is `APPROVE_READY` for review only.
- A green `domain-fauna` workflow includes explicit proof and publication-dry-run hold jobs. Green does not mean those capabilities exist.
- A source descriptor-shaped file is not source admission.
- A taxon identifier is not a verified identification.
- A range polygon is not an occurrence observation.
- A model surface is not an observation.
- An aggregate is not an individual location.
- A regulatory status is not evidence of current presence.
- A hidden map field is not a safe transform.
- A generalized public carrier is not canonical restricted truth.
- Generated language, map pixels, tiles, screenshots, dashboards, indexes, graph projections, and AI answers are not release authority.

[Back to top](#top)

---

<a id="roles-and-separation-of-duties"></a>

## Roles and separation of duties

Only the GitHub review route is verified. Every functional role below remains **NEEDS VERIFICATION** until an accepted assignment and current authority interval are available.

| Role | Publication-gate responsibility | Current status |
|---|---|---|
| Operator | Freeze revision, run bounded commands, preserve logs, stop on holds | Assignment unknown |
| Fauna domain steward | Confirm domain scope and object-family ownership | Assignment unknown |
| Taxonomy reviewer | Resolve accepted-name, concept, crosswalk, and conflict posture | Assignment unknown |
| Source and rights reviewer | Verify source identity, role, access terms, redistribution, and approved use | Assignment unknown |
| Sensitivity/geoprivacy reviewer | Review harmful precision, transform, reconstruction, and audience posture | Assignment unknown |
| Evidence steward | Verify EvidenceRef resolution and support limitations | Assignment unknown |
| Policy steward | Verify accepted policy source, bundle, evaluator, and result | Assignment unknown |
| Validation owner | Confirm validator scope, fixtures, exact revision, and finding interpretation | Assignment unknown |
| Independent reviewer | Review the candidate without collapsing author and approver | Assignment unknown |
| Release authority | Decide release-family state after all support closes | Assignment unknown |
| Correction/withdrawal owner | Ensure correction, supersession, withdrawal, and notice paths exist | Assignment unknown |
| Rollback owner | Verify rollback target and bounded restoration plan | Assignment unknown |
| Public-surface/operations owner | Verify governed API, map, export, cache, and monitoring effects | Assignment unknown |
| GitHub reviewer | Review repository changes routed through CODEOWNERS | `@bartytime4life` routing confirmed |

> [!IMPORTANT]
> CODEOWNERS routing does not prove taxonomic qualification, rights-holder authority, sensitivity stewardship, reviewer independence, release approval, or publication authority.

No person may infer a missing role from a filename, account ownership, prior comment, workflow actor, or generated receipt.

[Back to top](#top)

---

<a id="no-network-and-no-write-contract"></a>

## No-network and no-write contract

### Shared profile contract

| Requirement | Required posture | Failure posture |
|---|---|---|
| Inputs | Repository-controlled synthetic baseline and five fixed mutations only | `ERROR` or stop on caller-controlled candidate input |
| Network | No source, DNS, socket, API, tile, registry, model, or external policy request | `DENY` and stop |
| Credentials | No source token, cloud credential, private endpoint, signing key, or unrelated secret | `DENY` and stop |
| Writes | No candidate, decision, receipt, proof, manifest, rollback card, release, or published artifact | `ERROR` and investigate |
| Output | Deterministic JSON to stdout plus test output | `ERROR` on nondeterminism or file emission |
| Authority | Every authority/publication field remains false | `DENY` on authority claim |
| Case closure | All five cases match exact status and reason-code expectations and remain `BLOCKED` | `FAIL` |
| Sensitive data | No real or reconstructable Fauna detail | `DENY`, quarantine the test material, and notify authorized reviewers |

### Candidate-specific Fauna contract

A future Fauna dry run must additionally:

- use one explicit accepted candidate and immutable artifact identity;
- read only public-safe packet metadata or governed references;
- never print protected values, exact coordinates, transform parameters, observer identities, private-land clues, or restricted source rows;
- resolve support through governed interfaces rather than direct canonical-store access;
- bind every finding to an exact candidate, revision, policy version, validator profile, review context, and evaluation time;
- produce review support without writing release or public state; and
- fail closed when rights, sensitivity, stewardship, evidence, policy, review, correction, withdrawal, or rollback support is missing.

### Environment

Use an isolated checkout at an exact revision. Remove unrelated source credentials from the environment. The accepted commands set deterministic and no-network intent variables, but environment variables alone are not a network sandbox. The shared test suite provides the bounded socket guard described by its implementation; production-grade isolation remains separate work.

Do not run this procedure in a checkout that contains unreviewed restricted Fauna payloads or uncommitted sensitive files.

[Back to top](#top)

---

<a id="preflight-and-mandatory-stop-conditions"></a>

## Preflight and mandatory stop conditions

### Freeze before execution

Record:

- repository and exact commit SHA;
- branch and worktree status;
- candidate identity, or `NOT_ESTABLISHED`;
- shared helper and test blobs;
- promotion-gate validator profile;
- Fauna fixture profile;
- candidate/proof/manifest/published lane counts;
- policy and source-authority status;
- requested terminal boundary;
- current reviewers and verified assignments;
- any overlapping branch, pull request, migration, or correction work.

### Safe count-only inventory

Do not print candidate or artifact contents. Use a count-only inventory that excludes README and `.gitkeep` guidance files:

```bash
python - <<'PY'
from pathlib import Path

lanes = {
    "candidate_payloads": Path("release/candidates/fauna"),
    "proof_payloads": Path("data/proofs/fauna"),
    "manifest_payloads": Path("release/manifests/fauna"),
    "published_payloads": Path("data/published/fauna"),
}

for label, root in lanes.items():
    files = [
        path
        for path in root.rglob("*")
        if path.is_file() and path.name not in {"README.md", ".gitkeep"}
    ]
    print(f"{label}={len(files)}")
PY
```

A nonzero count is not permission to inspect or expose a file. Stop and determine its access, sensitivity, ownership, and review posture first.

### Mandatory stop conditions

Stop before candidate-specific evaluation when any condition applies:

1. **No candidate exists.** Record `HOLD: candidate not established`. Running the shared synthetic profile remains allowed, but it cannot stand in for the absent candidate.
2. **The target or governing bytes changed after the freeze.** Re-read and reconcile before continuing.
3. **An overlapping pull request, migration, correction, withdrawal, or rollback owns the same surface.**
4. **Any input contains or may reveal protected location, observer, private-land, telemetry, collection, or steward-controlled detail.**
5. **Source identity, approved use, rights, redistribution, or source role is unresolved.**
6. **Taxonomic identity or crosswalk conflict is unresolved and material to the output.**
7. **EvidenceRefs do not resolve to accepted EvidenceBundles, or support scope is insufficient.**
8. **The public-safe transform, caveats, reconstruction risk, or transform proof is unresolved.**
9. **Promotion policy remains inactive or no accepted evaluator/result is bound to the candidate.**
10. **Required review or separation of duties is absent, expired, superseded, or unauthenticated.**
11. **Manifest placement or release-state vocabulary conflict prevents an unambiguous record.**
12. **Correction, withdrawal, supersession, cache invalidation, or rollback support is missing.**
13. **A command requires network, credentials, public writes, release secrets, signing authority, deployment access, or mutable external state.**
14. **A workflow is green only because a readiness hold is implemented as a successful inspection job.**
15. **The operator cannot report the result without exposing sensitive detail.**

A correct `HOLD`, `DENY`, or `ABSTAIN` is preferable to a persuasive but unsupported pass.

[Back to top](#top)

---

<a id="current-executable-command-map"></a>

## Current executable command map

Run from repository root at the frozen revision.

### 1. Shared synthetic publication-denial profile

```bash
KFM_NO_NETWORK=1 \
PYTHONHASHSEED=0 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
TZ=UTC \
make release-dry-run
```

Equivalent implementation entry points:

```bash
KFM_NO_NETWORK=1 \
PYTHONHASHSEED=0 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
TZ=UTC \
python tools/release/release_dry_run.py --pretty

KFM_NO_NETWORK=1 \
PYTHONHASHSEED=0 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
TZ=UTC \
python -m unittest -q tests.release.test_publication_deny_dry_run
```

### 2. Generic A–G declared-readiness fixtures

```bash
KFM_NO_NETWORK=1 \
PYTHONHASHSEED=0 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
TZ=UTC \
make publish-check
```

This runs fixture-only `ReviewRecord` and promotion-gate validation. It does not evaluate the inactive promotion Rego stubs, resolve live evidence, authenticate actors, or create a decision.

### 3. Accepted synthetic Fauna fixture-safety suite

```bash
KFM_NO_NETWORK=1 \
PYTHONHASHSEED=0 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
TZ=UTC \
python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_fauna_smoke.py' \
  --verbose
```

This suite validates synthetic fixture hygiene only.

### 4. Registry-driven release-adjacent profile

```bash
KFM_NO_NETWORK=1 \
PYTHONHASHSEED=0 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
TZ=UTC \
make validator-release-profile
```

Treat the selected validator set as release-adjacent fixture validation only. It is not a substitute for the explicit commands above and has no release effect.

### Commands that do not exist

At the evidence checkpoint, neither of these accepted Make targets exists:

```text
fauna-release-dry-run
release-dry-run-fauna
```

Do not invent an alias, shell script, candidate path, or workflow invocation in order to make the documentation appear complete. Wiring a candidate-specific tool requires its own reviewed implementation slice.

[Back to top](#top)

---

<a id="shared-publication-denial-profile"></a>

## Shared publication-denial profile

The shared helper loads `fixtures/release/promotion_gate/valid/pass__complete_candidate.json`, copies it in memory, applies exactly one negative mutation per case, invokes the bounded promotion-gate validator, and compares the observed result with the exact expected status and reason codes.

| Case | Mutation | Expected status | Exact reason code | Publication effect |
|---|---|---|---|---|
| `evidence_missing` | Clear `evidence_refs` | `ABSTAIN` | `PG_F_EVIDENCE_REF_MISSING` | Denied |
| `policy_denied` | Set declared policy evaluation to `DENY` | `DENY` | `PG_E_POLICY_DENY` | Denied |
| `integrity_mismatch` | Replace receipt output digest set | `DENY` | `PG_B_ARTIFACT_SET_MISMATCH` | Denied |
| `rights_or_sensitivity_not_public_safe` | Replace public-safe labels with `restricted` | `DENY` | `PG_E_PUBLIC_SAFE_LABEL_INVALID` | Denied |
| `review_absent` | Remove declared review | `DENY` | `PG_G_REVIEW_INVALID` | Denied |

The suite passes only when:

- every case has the exact expected status;
- the exact sorted reason-code tuple matches;
- readiness is `BLOCKED` for every case;
- the report contains five cases;
- no authority, decision, publication, network use, or release-candidate assembly is claimed;
- two CLI executions produce byte-identical stdout; and
- the repository file inventory is unchanged.

### Interpretation

A successful run proves:

- the fixed synthetic negative mutations still trigger their expected bounded findings;
- the helper and tests executed at the tested revision;
- the helper is deterministic under the tested environment;
- its tested code path does not use the patched network entry point; and
- its execution emits no repository file.

A successful run does **not** prove:

- that a Fauna candidate exists;
- source admission, rights, sensitivity, or taxonomic truth;
- that an EvidenceRef resolves;
- that current policy was actually evaluated;
- that a reviewer or assignment is authentic;
- that a real manifest, correction path, or rollback target is valid;
- public-surface safety;
- promotion, release, deployment, publication, withdrawal, correction, or rollback; or
- required-check enforcement in repository settings.

### Why `ABSTAIN` still denies publication

The evidence-missing case is not a policy denial. It is an evidence insufficiency outcome. The helper nevertheless records `publication_outcome: DENIED` because cite-or-abstain forbids publication of an unsupported consequential claim. Do not rewrite `ABSTAIN` as `PASS`, `WARN`, or “nearly ready.”

[Back to top](#top)

---

<a id="operator-procedure"></a>

## Operator procedure

### Step 1 — freeze identity and scope

Record the exact SHA and clean/dirty state:

```bash
git rev-parse HEAD
git branch --show-current
git status --short
```

Do not continue from a dirty checkout containing unknown or sensitive files.

Record:

```text
candidate_id: NOT_ESTABLISHED
requested_boundary: CATALOG/TRIPLET -> PUBLISHED rehearsal
public_state_mutation_allowed: false
release_state_mutation_allowed: false
network_allowed: false
```

Replace `NOT_ESTABLISHED` only after a verified child candidate dossier exists and its identifier can be disclosed safely.

### Step 2 — inventory without opening payloads

Run the count-only inventory in [Preflight](#preflight-and-mandatory-stop-conditions).

At the current checkpoint, the expected non-guidance counts are all zero. Any change triggers review; it does not automatically advance the procedure.

### Step 3 — verify current implementation boundaries

Confirm:

- `tools/release/release_dry_run.py` still loads the fixed synthetic baseline;
- its `CASES` set remains the five documented cases;
- the report still declares all authority/publication/assembly fields false;
- `tests/release/test_publication_deny_dry_run.py` still checks no-network, deterministic output, and no file emission;
- the `Makefile` target still invokes only the bounded helper and test;
- the shared workflow has read-only contents permission and no release/deployment secret;
- the Fauna workflow still marks proof and publication-dry-run jobs as holds; and
- no candidate-specific target appeared without a reviewed contract and tests.

If any assumption changed, stop and update this runbook or the implementation as a separate coherent change.

### Step 4 — run the shared synthetic denial profile

Execute `make release-dry-run`.

Required interpretation:

```text
dry_run_status=PASS
case_count=5
every publication_outcome=DENIED
every readiness=BLOCKED
authority_created=false
decision_created=false
network_used=false
publication_created=false
release_candidate_assembled=false
```

Do not copy the synthetic packet or its `PASS` status into a Fauna candidate record.

### Step 5 — run generic declared-readiness fixtures

Execute `make publish-check`.

A pass proves only that the current fixture-only review and A–G matrices pass their bounded tests. It does not authenticate a source, EvidenceBundle, policy result, reviewer, assignment, rollback target, or public surface.

### Step 6 — run the accepted Fauna fixture-safety suite

Execute the exact Fauna unittest command.

Required interpretation:

- accepted positive synthetic fixtures have no findings;
- negative fixtures fail closed with the suite's exact expected findings;
- the sensitive-withheld fixture preserves its fixture-only transform reference, matching geoprivacy state, and withholding caveat;
- no live Fauna data were tested; and
- no candidate, proof, release, or publication was produced.

### Step 7 — evaluate the candidate-specific matrix

Use [Current Fauna publication closure matrix](#current-fauna-publication-closure-matrix).

Because no candidate exists at the current checkpoint, stop at:

```text
HOLD
reason: no verified child Fauna candidate dossier
next authority: accountable Fauna candidate commissioning and review
public effect: none
```

Do not continue by substituting a synthetic fixture, a planning example from the release index, or an eBird/GBIF source template.

### Step 8 — inspect hosted exact-head evidence

For a pull request, bind every workflow result to the exact head SHA.

Distinguish:

- direct changed-area documentation checks;
- shared synthetic publication-denial checks;
- generic promotion-readiness fixture checks;
- Fauna fixture-safety checks;
- explicit hold jobs;
- inherited or concurrent repository failures; and
- repository-settings enforcement, which remains separate evidence.

### Step 9 — prepare a public-safe review handoff

Use the template below. Include no protected values.

The current correct handoff is `HOLD`, not `REVIEW_HANDOFF_READY`.

### Step 10 — stop

Do not:

- create a candidate, decision, receipt, proof, manifest, signature, correction, withdrawal, rollback, or publication record;
- copy files to `data/published/fauna/`;
- update a governed API catalog, map layer, tile source, cache, search index, graph, export, or AI context;
- request release or deployment authority; or
- treat a merge as lifecycle progression.

[Back to top](#top)

---

<a id="fauna-specific-publication-gates"></a>

## Fauna-specific publication gates

A future candidate-specific dry run must preserve the following distinctions and fail closed when support is missing.

### Candidate identity and object family

- Name one candidate, immutable artifact set, specification hash, domain scope, audience, and requested boundary.
- Identify whether each included object is a taxon, crosswalk, conservation status, occurrence, restricted occurrence, public occurrence, range, seasonal range, migration context, sensitive site, mortality observation, disease observation, invasive-species record, or redaction/generalization support.
- Do not add an object family by implication or allow a view/product name to become canonical domain ownership.

### Taxonomy

- Bind names to a taxon concept and source authority, not a string alone.
- Preserve accepted, synonym, provisional, unresolved, split, lump, and conflict posture.
- Record the taxonomic time/version and crosswalk limitations.
- Abstain from species-level claims when the evidence supports only a broader concept.

### Source identity, role, rights, and stewardship

- Require an accepted source descriptor and approved use for every input.
- Keep observed, specimen, citizen-science, modeled, aggregate, administrative, regulatory, contextual, and synthetic roles distinct.
- Verify access terms, redistribution, citation, retention, derivative, audience, and revocation obligations.
- Do not inherit public-use permission from discoverability or API access.

### Occurrence, range, season, and migration

- An occurrence record supports a bounded observation, not general range.
- A range polygon does not prove presence at a point or time.
- Seasonal range does not prove year-round presence.
- Migration context does not reveal or predict an individual path.
- Non-detection is not absence unless the sampling design supports that inference.

### Rights, sensitivity, and geoprivacy

- Deny exact or reconstructable sensitive location exposure.
- Review direct coordinates, centroids, bounding boxes, tiles, feature IDs, source-layer names, counts, timestamps, labels, URLs, caches, screenshots, logs, exports, and cross-domain joins.
- Transform before rendering or delivery; client-side hiding is not a safe transform.
- Bind the public derivative to the transform identity, input/output digests, audience, caveats, evidence, policy, and review without disclosing protected parameters.
- Test reverse inference, differencing, repeated-query, temporal-correlation, private-land, road/access, imagery, and habitat joins.

### Evidence and scientific support

- Resolve every consequential EvidenceRef to an accepted EvidenceBundle.
- Preserve support type, spatial scope, temporal scope, source role, uncertainty, caveats, and contradiction state.
- Do not treat a receipt, summary, model, index, tile, or graph projection as evidence truth.
- Keep modeled suitability, predicted occupancy, interpolated density, observed count, checklist effort, mortality, disease, and population trend separate.

### Validation and integrity

- Bind candidate, artifacts, manifest, receipts, proofs, and public carriers by deterministic identity and digest.
- Validate geometry/CRS, time, schema, taxonomy, source role, evidence closure, rights, sensitivity, field allowlists, transform support, and public-carrier reconstruction risk.
- Include negative fixtures for exact-location leakage, encoded clues, missing source identity, unresolved taxonomy, evidence gaps, rights gaps, policy gaps, review gaps, correction gaps, and rollback gaps.
- A validator must not echo protected values in diagnostics.

### Policy

- Use an accepted policy source, bundle, evaluator, entry point, input contract, result normalization, and version/digest.
- Treat missing context, unknown labels, evaluator failure, inactive stubs, and unbound policy as `HOLD`, `ABSTAIN`, `DENY`, or `ERROR` according to the accepted contract—not allow.
- Policy output is one input to review and release; it does not decide truth or apply a transition.

### Review and separation

- Authenticate subject, reviewer, assignment, scope, authority interval, review time, validity interval, obligations, and supersession state.
- Prevent self-review where materiality requires separation.
- Require source/rights, taxonomy, sensitivity/geoprivacy, evidence, policy, validation, and release review appropriate to consequence.
- Do not substitute CODEOWNERS routing or a PR approval for a substantive review record.

### Release, correction, withdrawal, and rollback

- Resolve the canonical manifest lane before creating an instance.
- Bind included artifacts, decisions, evidence/proof, receipts, policy, reviews, signatures, correction path, withdrawal path, rollback target, changelog, and public-carrier identity.
- Prove that public caches, tiles, indexes, graphs, exports, screenshots, and AI-facing summaries can be invalidated or superseded safely.
- Preserve immutable history; do not silently overwrite or delete prior public state.

### Public clients and governed AI

- Standard clients consume governed APIs or released public-safe artifacts only.
- Evidence Drawer and Focus Mode must show bounded evidence, time, policy, release, stale, correction, and withheld/denied context appropriate to the audience.
- AI may interpret released evidence; it cannot infer protected coordinates, expand beyond EvidenceBundle scope, or approve release.
- An attractive map, popup, dashboard, report, story, or answer cannot compensate for an unresolved gate.

[Back to top](#top)

---

<a id="current-fauna-publication-closure-matrix"></a>

## Current Fauna publication closure matrix

This matrix describes the bounded checkpoint, not a permanent judgment.

| Closure area | Current status | Evidence-based reason | Required before candidate-specific dry run |
|---|---|---|---|
| Candidate identity and artifact set | **HOLD** | No verified child dossier under `release/candidates/fauna/` | Accepted child candidate with immutable public-safe pointers |
| Source admission and approved use | **HOLD** | Central authority projection is empty; candidate source set absent | Accepted source descriptors, rights, purpose, role, and cadence |
| Taxonomy packet | **HOLD** | No candidate taxon scope or crosswalk packet | Reviewed taxon concepts, versions, conflicts, and limitations |
| Evidence and proof | **HOLD** | No Fauna proof artifact; no candidate EvidenceBundle closure | Resolvable candidate EvidenceRefs and accepted proof support |
| Rights and stewardship | **HOLD** | No candidate-specific decision | Current approved-use, redistribution, stewardship, and audience decisions |
| Sensitivity and geoprivacy | **HOLD** | No candidate transform/review packet | Public-safe transform proof, reconstruction review, caveats, and reviewer decision |
| Candidate-specific validation | **HOLD** | Current executable Fauna suite is synthetic fixture hygiene only | Candidate-bound validator profile, fixtures, tests, and exact findings |
| Generic readiness validation | **PARTIAL / BOUNDED** | A–G fixture validator exists; authenticity and authority are unresolved | Candidate-specific accepted input and support resolution |
| Promotion policy | **HOLD** | Promotion Rego stubs are inactive and no evaluator binding exists | Accepted fail-closed policy bundle, evaluator, input, output, and consumer |
| Accountable review | **HOLD** | Only GitHub review routing is verified | Current assignments, independence, scope, obligations, and review records |
| Promotion decision/receipt | **HOLD** | No Fauna instance; reusable families remain proposed/fixture-first | Governed, authenticated, candidate-bound records after review |
| Release manifest | **HOLD / CONFLICTED** | No Fauna instance; singular/plural manifest topology unresolved | Accepted canonical lane and candidate-bound manifest |
| Correction and withdrawal | **HOLD** | No candidate-specific closure | Accepted correction, supersession, withdrawal, notice, and propagation plan |
| Rollback | **HOLD** | No candidate rollback target or executed drill | Candidate-bound rollback card/target and bounded rehearsal |
| Public carrier | **HOLD** | No Fauna published artifact in direct-child inventory | Release-authorized public-safe carrier with digest and support bindings |
| Governed API/map/export/AI | **HOLD / UNKNOWN** | No candidate release binding or public-surface proof | End-to-end public-safe consumption and invalidation evidence |
| Release, deployment, publication | **NOT ESTABLISHED** | No accountable decision or transition evidence | Separate authorized transitions after all gates close |

### Current outcome

```text
outcome: HOLD
primary_reason: FAUNA_CANDIDATE_NOT_ESTABLISHED
secondary_reasons:
  - source admission not closed
  - proof/evidence closure absent
  - rights and geoprivacy review absent
  - promotion policy inactive
  - accountable review absent
  - manifest topology unresolved
  - correction/withdrawal/rollback closure absent
public_state_changed: false
release_state_changed: false
```

The identifiers in this example are **runbook-local explanatory labels**, not accepted wire-level enums. Do not serialize them into a governed record unless an accepted contract defines them.

[Back to top](#top)

---

<a id="finite-outcomes-and-reason-code-boundary"></a>

## Finite outcomes and reason-code boundary

### Shared helper outcomes

These are implemented in the shared helper or promotion-gate validator:

| Outcome | Meaning | Publication posture |
|---|---|---|
| `PASS` | All five expected denial cases matched exactly | No publication; proves synthetic blocking profile only |
| `ABSTAIN` | Support is insufficient without a contradictory unsafe claim | Publication remains blocked |
| `DENY` | Mandatory or unsafe condition blocks readiness | Publication remains blocked |
| `ERROR` | Input or evaluation could not complete safely | Publication remains blocked |

Exact shared reason codes used by this runbook:

- `PG_F_EVIDENCE_REF_MISSING`
- `PG_E_POLICY_DENY`
- `PG_B_ARTIFACT_SET_MISMATCH`
- `PG_E_PUBLIC_SAFE_LABEL_INVALID`
- `PG_G_REVIEW_INVALID`

### Fauna handoff outcomes

Use these human-facing classifications without presenting them as schema enums:

| Classification | Use |
|---|---|
| **HOLD** | A named prerequisite is missing, unresolved, stale, conflicted, or unassigned |
| **DENY** | Exposure or use is prohibited by accepted rights, sensitivity, policy, or authority |
| **ABSTAIN** | Evidence is insufficient to make the requested consequential claim |
| **ERROR** | The rehearsal could not be completed safely or deterministically |
| **REVIEW HANDOFF READY** | The public-safe packet is complete enough for accountable review; no release effect |
| **NO ACTION** | No candidate-specific action is authorized or required |

At the current checkpoint, the correct classification is **HOLD**.

Do not use `ALLOW`, `APPROVE`, `PUBLISHED`, `RELEASED`, or `PROMOTED` as a dry-run conclusion.

[Back to top](#top)

---

<a id="authority-boundary-and-review-handoff"></a>

## Authority boundary and review handoff

### Handoff requirements

A public-safe handoff should include only:

- repository and exact commit;
- command/profile identities and relevant blobs;
- candidate ID or `NOT_ESTABLISHED`;
- requested lifecycle boundary and audience;
- count-only candidate/proof/manifest/published inventory;
- source descriptor IDs and status, without protected credentials or rows;
- taxon concept IDs and conflict posture;
- EvidenceRef/EvidenceBundle IDs and resolution status;
- rights, sensitivity, geoprivacy, policy, validation, review, correction, withdrawal, and rollback status;
- exact shared helper statuses and public-safe reason codes;
- hosted exact-head workflow statuses;
- introduced versus inherited failures;
- current finite handoff outcome;
- required next authority; and
- explicit non-effects.

### Handoff template

```markdown
## Fauna publication-gate dry-run handoff

- Repository: `bartytime4life/Kansas-Frontier-Matrix`
- Exact revision: `<40-hex SHA>`
- Candidate: `NOT_ESTABLISHED` or `<public-safe candidate ID>`
- Requested boundary: `CATALOG/TRIPLET -> PUBLISHED rehearsal`
- Audience: `<public-safe audience class or UNKNOWN>`
- Shared denial profile: `PASS | ABSTAIN | DENY | ERROR`
- Generic A–G fixtures: `PASS | ABSTAIN | DENY | ERROR`
- Fauna fixture-safety profile: `PASS | FAIL | ERROR`
- Candidate-specific Fauna dry run: `HOLD | DENY | ABSTAIN | ERROR | REVIEW HANDOFF READY`
- Candidate/proof/manifest/published payload counts: `<count-only>`
- Source admission: `<status and public-safe IDs>`
- Taxonomy: `<status and public-safe IDs>`
- Evidence/proof: `<status and public-safe IDs>`
- Rights/stewardship: `<status>`
- Sensitivity/geoprivacy: `<status>`
- Policy: `<status and accepted evaluator identity, if any>`
- Review/separation: `<status>`
- Correction/withdrawal/rollback: `<status>`
- Exact-head hosted checks: `<status summary>`
- Introduced failures: `<none or bounded list>`
- Inherited/concurrent failures: `<none or bounded list>`
- Outcome: `<finite handoff classification>`
- Next accountable authority: `<verified assignment or NEEDS VERIFICATION>`
- Public state changed: `false`
- Release state changed: `false`
- Source activation changed: `false`
```

### Current handoff

```text
candidate: NOT_ESTABLISHED
shared denial profile: available
candidate-specific Fauna dry run: HOLD
review handoff ready: no
next action: commission and review a bounded candidate-specific implementation slice
release/deployment/publication effect: none
```

### Sensitive reporting rule

Report categories, counts, IDs safe for the review audience, and public-safe reason codes. Do not report:

- coordinates or precision;
- source-row contents;
- protected site or taxon clues;
- transform thresholds, salts, seeds, secret grids, or reversible mappings;
- observer names or contact details;
- private-land/access details;
- restricted URLs, credentials, tokens, or storage paths;
- unredacted diffs, logs, screenshots, or exports; or
- language that enables reverse inference.

When a reviewer needs protected detail, route it through the accepted restricted review environment. Do not move it into GitHub to simplify review.

[Back to top](#top)

---

<a id="hosted-ci-and-exact-head-interpretation"></a>

## Hosted CI and exact-head interpretation

### Relevant workflows

| Workflow | What a success can show | What it cannot show |
|---|---|---|
| `release-dry-run` | Shared synthetic denial, bounded A–G fixtures, and rollback-card fixture/rehearsal checks completed at exact head | Candidate assembly, live policy, evidence authentication, release, or publication |
| `promotion-gate` | Fixture-only review and A–G readiness profile completed | Authenticated reviewer, accepted policy, real decision, or transition |
| `domain-fauna` | Synthetic fixture suite completed and current proof/dry-run hold assertions remained true | Fauna proof, domain dry run, source admission, or public safety of real data |
| `domain-fauna` held jobs | Repository still lacks the capabilities the hold checks are designed to detect | Functional proof or release machinery |
| Documentation checks | Markdown, metadata, links, or docs build passed according to each workflow | Scientific truth, rights, sensitivity, release authority, or operations |

### Exact-head rule

Always report:

- pull-request number;
- exact head SHA;
- check name and run/job identity;
- status and conclusion;
- whether the workflow tested the changed path;
- whether the failure is introduced, inherited, concurrent, or unresolved;
- whether a hold job passed by confirming absence; and
- whether all runs settled.

A workflow pass at an older head is stale after the branch moves.

### Held-success rule

A successful `publish-dry-run-fauna` job currently means:

> The workflow confirmed that no child candidate record and no accepted Fauna dry-run target had appeared, then emitted the documented hold.

It does **not** mean the Fauna publication dry run ran.

A successful `build-proof-fauna` job currently means:

> The workflow confirmed that no accepted Fauna proof producer/artifact had appeared, then emitted the documented hold.

It does **not** mean a Fauna proof was built.

### Required-check rule

A workflow appearing on a pull request does not prove it is required by repository rulesets. Required-check coupling, branch protection, merge policy, and administrative enforcement require separate current evidence.

[Back to top](#top)

---

<a id="correction-withdrawal-and-rollback-boundary"></a>

## Correction, withdrawal, and rollback boundary

### Dry-run correction

When the shared helper, fixtures, reason codes, or workflow change:

1. freeze the old and new exact revisions;
2. identify the contract or behavior change;
3. rerun all five negative cases;
4. compare deterministic output and reason codes;
5. update tests and this runbook in the same coherent review boundary when the behavior intentionally changed;
6. preserve prior generated authoring receipts and exact-tree references;
7. do not rewrite old evidence to make it match new code; and
8. record unresolved compatibility as `HOLD` or `CONFLICTED`.

### Candidate correction

A future candidate dry run must route incorrect source, taxonomic, evidence, transform, rights, policy, or validation support back to its owning lane. Do not repair canonical or restricted data inside a release-support tool.

### Public correction and withdrawal

No current Fauna public carrier was established by the bounded inventory. Therefore this procedure cannot execute a public correction or withdrawal.

If a future release exists:

- issue a correction or withdrawal through the accepted release-family lane;
- retain the original release and immutable lineage;
- publish an audience-appropriate notice;
- invalidate or supersede governed API, tile, cache, search, graph, export, screenshot, and AI-facing derivatives;
- bind the successor or withdrawal to evidence, review, decision, and rollback records; and
- verify public surfaces rather than assuming a repository change propagated.

### Rollback

The shared workflow's rollback-card checks are synthetic fixture/rehearsal evidence only. They do not execute rollback.

A candidate-specific Fauna dry run must not claim rollback readiness until:

- the prior public-safe target is stable and available;
- affected carriers and consumers are enumerated;
- correction and withdrawal relationships are explicit;
- cache/index/tile/API invalidation is bounded;
- protected source material remains protected;
- a deterministic or otherwise auditable rehearsal succeeds; and
- accountable reviewers accept the result.

[Back to top](#top)

---

<a id="graduation-criteria-for-a-candidate-specific-fauna-dry-run"></a>

## Graduation criteria for a candidate-specific Fauna dry run

Do not remove the workflow hold merely because this runbook is complete.

Graduate the Fauna domain dry-run lane only through a separate reviewable implementation that establishes:

1. **Candidate contract** — accepted candidate identity, artifact, manifest, lifecycle boundary, audience, and no-write semantics.
2. **Directory placement** — verified homes for candidate, manifest, decision, receipt, proof, correction, withdrawal, and rollback families; resolve singular/plural manifest conflict or record an accepted migration.
3. **Accepted candidate fixture** — one public-safe synthetic Fauna candidate that cannot expose protected locations and is explicitly non-releasable.
4. **Negative matrix** — missing source, taxonomy conflict, evidence gap, rights gap, sensitive precision, reconstruction clue, transform gap, policy gap, review gap, integrity mismatch, correction gap, and rollback gap.
5. **Source closure** — accepted descriptors, roles, terms, rights, cadence, and purpose binding.
6. **Taxonomy closure** — concept identity, authority/version, crosswalk, conflict, and uncertainty.
7. **Evidence closure** — resolvable fixture EvidenceRefs and bounded EvidenceBundles without promoting fixture data.
8. **Geoprivacy closure** — public-safe transform contract, proof/receipt binding, diagnostics redaction, and reverse-inference tests.
9. **Policy closure** — accepted fail-closed rule source, bundle, evaluator, entry point, input/output contract, tests, and governed consumer.
10. **Review closure** — fixture-only authenticated-shape profile plus a production authority/assignment route kept separate from synthetic proof.
11. **Release support** — accepted manifest, decision, receipt, correction, withdrawal, and rollback contracts and candidate-bound validation.
12. **No-write enforcement** — tests prove no lifecycle, release, cache, API, map, tile, index, graph, export, or published mutation.
13. **No-network enforcement** — deterministic fixture execution with explicit guards; any dependency installation remains outside the validated domain logic.
14. **Sensitive diagnostics** — findings contain stable codes and safe paths only, never protected values.
15. **Workflow hardening** — least permissions, pinned actions, no release/deployment secrets, exact job summaries, concurrency, timeouts, and explicit non-effects.
16. **Documentation** — update this runbook, the Fauna workflow, tool/test READMEs, candidate index, and relevant registers together.
17. **Validation and rollback** — changed-area tests, exact-head CI, and a transparent rollback plan for the implementation itself.
18. **Human authority** — accountable domain, source/rights, sensitivity, evidence, policy, validation, independent-review, release, correction, and rollback assignments.

The first graduated command should still stop before release and publication.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| Item | Status | Verification required |
|---|---|---|
| Fauna runbook-lane README | **HOLD** | Replace one-byte placeholder with a reviewed local boundary/navigation contract |
| Fauna child candidate dossier | **ABSENT** | Commission and verify one bounded public-safe candidate |
| Fauna proof producer and artifact | **HOLD** | Accepted proof contract, producer, fixtures, validator, and release binding |
| Fauna candidate-specific dry-run tool | **HOLD** | Accepted input/output contract, implementation, tests, and workflow |
| Canonical Fauna manifest home | **CONFLICTED** | Decide singular/plural lane responsibilities before instance creation |
| Source-authority register | **PROPOSED / empty** | Accepted owner, schema, entries, and admission integration |
| Candidate source set and rights | **UNKNOWN / HOLD** | Accepted source descriptors and current approved-use records |
| Taxonomy authority and review | **NEEDS VERIFICATION** | Verified concepts, crosswalks, assignments, and review |
| Promotion policy | **INACTIVE** | Operative fail-closed rules, tests, bundle, evaluator, and consumer |
| Fauna sensitivity/geoprivacy policy | **NEEDS VERIFICATION / HOLD** | Accepted transform and reconstruction-risk enforcement |
| EvidenceRef resolution | **HOLD** | Candidate-bound EvidenceBundle resolution and proof linkage |
| Accountable reviewers | **NEEDS VERIFICATION** | Current assignments, scopes, authority intervals, and independence |
| PromotionDecision/Receipt | **PROPOSED / no Fauna instance** | Candidate-bound authenticated records after review |
| Correction/withdrawal topology | **NEEDS VERIFICATION** | Accepted homes, contracts, propagation, and notices |
| Rollback target and drill | **HOLD** | Candidate-bound target, card, rehearsal, and public-surface validation |
| Published Fauna carrier | **NOT ESTABLISHED** | Separate release-authorized public-safe artifact and manifest binding |
| Governed API/map/export/AI behavior | **UNKNOWN / HOLD** | End-to-end released-carrier proof and correction/rollback propagation |
| Required-check/ruleset coupling | **NEEDS VERIFICATION** | Current GitHub ruleset and exact required-check evidence |
| Independent operational ownership | **NEEDS VERIFICATION** | Named and accepted owners beyond CODEOWNERS routing |

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

| Repository surface | Use in this runbook | Limitation |
|---|---|---|
| [Directory Rules v2](../../doctrine/directory-rules.md) and [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Same-path placement and responsibility separation | Does not prove runtime behavior |
| [CODEOWNERS](../../../.github/CODEOWNERS) | Verified GitHub review route | Not substantive authority or review completion |
| [Fauna candidate README](../../../release/candidates/fauna/README.md) and direct-child inventory | Candidate-lane boundary and no verified child dossier | Differently named, external, restricted, generated, or historical material remains outside the bounded inventory |
| [Fauna proof README](../../../data/proofs/fauna/README.md) and direct-child inventory | Proof-lane boundary and absence of proof artifact | README is not proof |
| [Fauna manifest README](../../../release/manifests/fauna/README.md) and direct-child inventory | Manifest guidance and topology conflict | No manifest instance or accepted canonical lane |
| [Fauna published README](../../../data/published/fauna/README.md) and direct-child inventory | Public-carrier boundary and absence of carrier | Folder/README presence is not publication |
| [Source-authority register](../../../control_plane/source_authority_register.yaml) | Current empty projection posture | Does not admit or activate sources |
| [Shared dry-run tool](../../../tools/release/release_dry_run.py) | Exact five-case implementation | Synthetic baseline only; accepts no caller candidate |
| [Shared dry-run tests](../../../tests/release/test_publication_deny_dry_run.py) | Exact case, no-network, determinism, and no-emission assertions | Bounded Python test surface only |
| [Release tooling README](../../../tools/release/README.md) | Tooling versus release-authority boundary | Draft explanatory surface |
| [Promotion-gate README](../../../tools/validators/promotion_gate/README.md) | A–G checks, finite results, and limitations | Declared context only; no live resolution or authority |
| [Promotion policy README](../../../policy/promotion/README.md) | Inactive no-op policy posture | Does not provide production policy |
| [Fauna workflow](../../../.github/workflows/domain-fauna.yml) | Exact synthetic validation and explicit proof/dry-run holds | Workflow success is not release |
| [Shared release-dry-run workflow](../../../.github/workflows/release-dry-run.yml) | Read-only orchestration and bounded synthetic checks | No real candidate or publication |
| [Fauna Promotion Runbook](./PROMOTION_RUNBOOK.md) | Current promotion-readiness boundary and holds | Documentation cannot create transition authority |
| [Fauna No-Network Test Runbook](./NO_NETWORK_TEST_RUNBOOK.md) | Accepted synthetic fixture procedure | Fixture hygiene only |
| [Fauna Release Index](../../domains/fauna/RELEASE_INDEX.md) | Human release-navigation lineage and open vocabulary conflicts | Illustrative IDs are not releases |
| [Proposal-era Release Dry-Run Runbook](../RELEASE_DRY_RUN.md) | Planning lineage | Current implementation files outrank its unverified broad mechanics |

### Evidence limits

- Git tree presence proves bytes at a revision, not scientific correctness, legal permission, release, deployment, or publication.
- Direct-child inventories are bounded to the inspected paths and revision.
- Connector-only authoring did not execute repository-native commands locally.
- No live source, protected payload, policy engine, reviewer authority service, release service, public API, map, tile server, cache, or deployment was exercised.
- Current operational state outside visible repository evidence remains `UNKNOWN` or `NEEDS VERIFICATION`.

[Back to top](#top)

---

<a id="document-change-rollback"></a>

## Document change rollback

This change replaces one same-path Markdown scaffold. It creates no executable or public effect.

Before merge:

- close or abandon the draft pull request;
- delete or retain the feature branch according to repository practice; and
- leave `main` unchanged.

After merge:

- revert the actual merge commit through a reviewed pull request, or
- apply a reviewed forward correction.

Do not rewrite shared history.

Reverting this document would restore the prior scaffold. It would not withdraw a Fauna source, undo a lifecycle transition, roll back a release, invalidate a public carrier, or change deployment state because this documentation change creates none of those effects.

[Back to top](#top)

---

<a id="appendix-a-operator-checklist"></a>

## Appendix A — operator checklist

### Freeze

- [ ] Exact repository and 40-hex commit recorded.
- [ ] Branch and worktree status recorded.
- [ ] Target and governing blobs frozen.
- [ ] Candidate ID recorded, or explicitly `NOT_ESTABLISHED`.
- [ ] Requested boundary and audience recorded.
- [ ] Active overlapping work checked.
- [ ] No restricted or uncommitted sensitive payload is present.

### Safety

- [ ] No source credentials exposed.
- [ ] No network access required by validated logic.
- [ ] No protected location or observer detail in inputs or logs.
- [ ] No geoprivacy transform parameters exposed.
- [ ] No lifecycle, release, cache, deployment, or public write authorized.
- [ ] Count-only lane inventory used.

### Shared validation

- [ ] `make release-dry-run` ran at exact revision.
- [ ] Five cases observed.
- [ ] Every publication outcome remained denied.
- [ ] Exact expected reason codes matched.
- [ ] Every case readiness remained `BLOCKED`.
- [ ] Authority, decision, publication, network, and assembly fields remained false.
- [ ] Deterministic/no-emission tests passed.

### Generic and Fauna validation

- [ ] `make publish-check` interpreted as fixture-only declared readiness.
- [ ] Accepted Fauna fixture suite ran.
- [ ] Positive/negative fixture polarity remained exact.
- [ ] Synthetic pass was not translated into candidate readiness.
- [ ] Domain proof and dry-run hold jobs were reported as holds.

### Candidate-specific closure

- [ ] Candidate exists and identity is stable.
- [ ] Artifact set and digests are immutable.
- [ ] Source admission and approved use are accepted.
- [ ] Taxonomy packet is reviewed.
- [ ] EvidenceRefs resolve to accepted EvidenceBundles.
- [ ] Rights/stewardship decisions are current.
- [ ] Sensitivity/geoprivacy transform and reconstruction review are accepted.
- [ ] Candidate-specific validation is deterministic and negative-tested.
- [ ] Promotion policy is active, accepted, and bound.
- [ ] Required reviewers and separation are authenticated.
- [ ] Manifest lane and vocabulary are unambiguous.
- [ ] Correction, withdrawal, and rollback are closed.
- [ ] Public carrier and consumers are identified and reversible.

### Handoff

- [ ] Exact-head hosted status recorded.
- [ ] Introduced and inherited failures separated.
- [ ] Public-safe reason codes only.
- [ ] No protected values in the handoff.
- [ ] Finite outcome recorded.
- [ ] Next accountable authority verified or marked `NEEDS VERIFICATION`.
- [ ] Public state unchanged.
- [ ] Release state unchanged.
- [ ] Source activation unchanged.

At the current checkpoint, the checklist must stop at **candidate-specific closure: candidate does not exist**, and the final outcome is **HOLD**.

[Back to top](#top)
