<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/fauna/publication-gate-dry-run
title: Fauna — Publication Gate Dry-Run Runbook
type: runbook
version: v1.0.1
status: draft; repository-grounded; no-write; non-publisher
created: 2026-08-24
updated: 2026-08-24
last_reviewed: 2026-08-24
owner: "@bartytime4life — GitHub review routing only"
owner_status: functional Fauna, taxonomy, source, rights, sensitivity, evidence, policy, validation, release, correction, rollback, and independent-review assignments remain NEEDS VERIFICATION
truth_posture: cite-or-abstain
policy_label: public-review; fauna; publication-gate; dry-run; synthetic-denial; sensitive-location; fail-closed
current_path: docs/runbooks/fauna/PUBLICATION_GATE_DRY_RUN.md
owning_root: docs/
authority_class: explanatory operational documentation
path_posture: PLACE
repository: bartytime4life/Kansas-Frontier-Matrix
content_inspection_commit: c3b39fb27fd7ca46c41f5b5133149f1d8cd73996
prior_target_blob: dff3b4a32ccbda552931775c67bf5aadcfad8c99
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
release_effect: none
deployment_effect: none
publication_effect: none
source_activation_effect: none
related:
  - ../README.md
  - ../RELEASE_DRY_RUN.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/fauna/README.md
  - ../../domains/fauna/RELEASE_INDEX.md
  - ./NO_NETWORK_TEST_RUNBOOK.md
  - ./PROMOTION_RUNBOOK.md
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
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna — Publication Gate Dry-Run Runbook

> Run the repository's bounded publication-denial rehearsal, assess whether a specifically identified Fauna candidate is ready for a candidate-specific no-write rehearsal, and produce a public-safe review handoff without creating promotion, release, deployment, or publication state.

> [!IMPORTANT]
> The implemented `release-dry-run` command is a **shared synthetic publication-denial profile**. It does not accept a caller-selected Fauna candidate, assemble a release, resolve live evidence, evaluate production policy, authenticate reviewers, or publish anything.

> [!CAUTION]
> **Current Fauna result: `HOLD`.** At the inspected repository checkpoint, the Fauna candidate, proof, manifest, and published lanes contain no verified child trust object or public carrier; the source-authority projection is empty; promotion policy is inactive; and the domain workflow explicitly holds the Fauna proof and publication-dry-run capabilities.

> [!WARNING]
> Never place exact or reverse-engineerable animal locations in inputs, logs, workflow summaries, pull requests, screenshots, reports, exports, or handoff packets. Sensitive taxa, nests, dens, roosts, hibernacula, breeding or spawning sites, aggregations, telemetry paths, observer-linked records, private-land clues, and geoprivacy parameters fail closed.

**Navigation:** [Purpose](#purpose-and-terminal-boundary) · [Authority](#authority-and-placement) · [Posture](#current-repository-posture) · [Safety](#no-network-no-write-and-sensitive-data-contract) · [Preflight](#preflight-and-stop-conditions) · [Commands](#current-command-map) · [Shared profile](#shared-publication-denial-profile) · [Procedure](#operator-procedure) · [Fauna gates](#fauna-candidate-publication-gates) · [Matrix](#current-closure-matrix) · [CI](#hosted-ci-and-held-job-interpretation) · [Handoff](#public-safe-review-handoff) · [Graduation](#graduation-criteria) · [Recovery](#correction-withdrawal-and-rollback) · [Evidence](#evidence-basis) · [Checklist](#operator-checklist)

---

<a id="purpose-and-terminal-boundary"></a>

## Purpose and terminal boundary

This runbook separates two operations:

1. **Shared synthetic denial rehearsal** — execute the repository-controlled five-case profile and verify that unsafe or unsupported packet mutations remain blocked.
2. **Candidate-specific Fauna assessment** — determine whether one named Fauna candidate has enough accepted support to enter a future no-write publication-gate rehearsal.

At the inspected checkpoint, operation 1 is executable. Operation 2 stops at `HOLD` because no verified child Fauna candidate dossier or accepted candidate-specific dry-run contract exists.

The governing lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This runbook does not execute that lifecycle. It rehearses denial behavior and assesses readiness to rehearse a transition.

### In scope

- freeze the exact repository revision and target scope;
- verify that the shared helper remains synthetic, deterministic, no-network, no-write, and non-authoritative;
- run and interpret the shared denial, generic A–G readiness, and Fauna fixture-safety profiles;
- inventory Fauna candidate, proof, manifest, and published lanes without opening protected payloads;
- assess candidate identity, source, taxonomy, evidence, rights, sensitivity, geoprivacy, validation, policy, review, correction, withdrawal, rollback, and public-carrier closure;
- report hosted checks at the exact head and distinguish held jobs from implemented capabilities; and
- prepare a public-safe review handoff.

### Out of scope

- live source access, source admission, source activation, connector execution, credential use, or data retrieval;
- validation of real occurrence, range, migration, mortality, disease, conservation, telemetry, or sensitive-site records;
- choosing or executing a production geoprivacy transform;
- resolving a real `EvidenceRef` to an authoritative `EvidenceBundle`;
- treating the inactive promotion Rego stubs as production policy;
- authenticating a reviewer, steward, rights holder, or release authority;
- creating a candidate, receipt, proof, review, decision, manifest, signature, correction, withdrawal, rollback card, or published carrier;
- writing to lifecycle, release, cache, deployment, or public-serving surfaces; and
- promotion, release, deployment, publication, correction execution, withdrawal execution, or rollback execution.

### Maximum current result

```text
shared synthetic denial profile: PASS | ABSTAIN | DENY | ERROR
candidate-specific Fauna gate:    HOLD | DENY | ABSTAIN | ERROR
review handoff:                   READY only when explicitly supported
lifecycle and public state:       UNCHANGED
```

`READY` means ready for accountable review only. It is not `APPROVE`, `PROMOTED`, `RELEASED`, or `PUBLISHED`.

[Back to top](#top)

---

<a id="authority-and-placement"></a>

## Authority and placement

### Directory Rules result

**`PLACE` — confirmed for this same-path update.**

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts [Directory Rules v2](../../doctrine/directory-rules.md). This tracked file is a human operational procedure under `docs/runbooks/fauna/`. The update creates no new root, schema home, policy home, release home, proof home, alias, mirror, or publication path.

| Responsibility | Owning surface | This runbook's role |
|---|---|---|
| Human procedure | `docs/runbooks/fauna/` | Explain bounded execution and handoff |
| Fauna meaning and sensitivity | `docs/domains/fauna/`, domain contracts | Cite; do not redefine |
| Machine shape | `schemas/` | Do not invent or amend |
| Source admission and rights | source registry and policy authorities | Require accepted references |
| Evidence and proof | evidence and `data/proofs/` authorities | Require resolution; do not manufacture |
| Policy | `policy/` | Record current posture; do not replace evaluation with prose |
| Validators and tests | `tools/validators/`, `tests/`, `fixtures/` | Document exact entry points and limits |
| Decisions and manifests | `release/` | Require governed records; do not create |
| Public-safe carriers | `data/published/` | Inventory only; no writes |
| Public consumption | governed APIs and released artifacts | Outside this procedure |

The local `docs/runbooks/fauna/README.md` remains a placeholder at the inspection checkpoint. This runbook does not substitute for that missing lane-boundary and navigation contract.

### Current implementation outranks proposal-era mechanics

The cross-domain [Release Dry-Run Runbook](../RELEASE_DRY_RUN.md) remains planning lineage. For current executable behavior, prefer:

1. [`tools/release/release_dry_run.py`](../../../tools/release/release_dry_run.py);
2. [`tests/release/test_publication_deny_dry_run.py`](../../../tests/release/test_publication_deny_dry_run.py);
3. the exact [`Makefile`](../../../Makefile) targets;
4. [`.github/workflows/release-dry-run.yml`](../../../.github/workflows/release-dry-run.yml); and
5. [`.github/workflows/domain-fauna.yml`](../../../.github/workflows/domain-fauna.yml).

When those surfaces and this document disagree, stop and correct the documentation or implementation in a separate reviewable change. Do not choose the wording that permits publication.

[Back to top](#top)

---

<a id="current-repository-posture"></a>

## Current repository posture

The following conclusions are bounded to `main@c3b39fb27fd7ca46c41f5b5133149f1d8cd73996`.

| Surface | Status | Safe conclusion |
|---|---|---|
| Prior target | **Confirmed scaffold** | The prior file asked for authoritative content but provided no executable procedure. |
| Fauna candidate lane | **Empty of verified child dossiers** | Direct-child inventory contains only guidance. No active candidate is established. |
| Fauna proof lane | **Guidance only** | No Fauna proof artifact is established. |
| Fauna manifest lane | **Guidance only / conflicted topology** | No Fauna manifest instance is established; singular/plural manifest responsibility remains unresolved. |
| Fauna published lane | **Guidance only** | No Fauna public carrier is established. |
| Source-authority projection | **Proposed, absent, empty** | `entries: []`; it neither admits nor activates sources. |
| Shared denial helper | **Executable, synthetic** | Replays five fixed mutations over a repository-controlled synthetic packet. It accepts no caller candidate. |
| Shared denial tests | **Executable** | Check exact polarity, reason codes, no authority claims, deterministic output, no-network behavior, and no file emission. |
| Generic A–G validator | **Executable, bounded** | `PASS` means `APPROVE_READY` for review only; references and authority are not authenticated. |
| Promotion policy | **Proposed and inactive** | Local Rego files are no-op stubs and are not the operative gate. |
| Fauna fixture suite | **Executable, synthetic** | Tests public-safe fixture hygiene; fixtures are ineligible for promotion and publication. |
| Fauna proof producer | **Workflow hold** | No accepted producer or deterministic proof command is wired. |
| Fauna publication dry run | **Workflow hold** | No accepted Fauna candidate-manifest contract or domain command is wired. |
| Review route | **Routing only** | CODEOWNERS routes GitHub review to `@bartytime4life`; functional authority and independence are unverified. |
| Release, deployment, publication | **Not established** | No inspected surface creates those effects for Fauna. |

### Bounded determination

```text
shared synthetic denial profile     = IMPLEMENTED / BOUNDED
generic declared-readiness profile  = IMPLEMENTED / BOUNDED
Fauna fixture-safety profile        = IMPLEMENTED / BOUNDED
Fauna candidate dossier             = ABSENT
Fauna candidate proof               = ABSENT
Fauna candidate manifest            = ABSENT
Fauna candidate-specific dry run    = HOLD
Fauna release or publication        = NOT ESTABLISHED
```

Repository-native commands were not run in a mounted checkout while this revision was authored. Commands below are documented entry points, not claimed local passes.

[Back to top](#top)

---

<a id="no-network-no-write-and-sensitive-data-contract"></a>

## No-network, no-write, and sensitive-data contract

### Shared profile

| Requirement | Required posture | Failure posture |
|---|---|---|
| Inputs | Fixed repository-controlled synthetic packet and mutations | Stop on caller-controlled candidate content |
| Network | No DNS, socket, API, source, tile, model, registry, or external policy request | `DENY` and stop |
| Credentials | No source token, cloud credential, signing key, private endpoint, or unrelated secret | `DENY` and stop |
| Writes | No candidate, receipt, proof, decision, manifest, rollback, release, or published artifact | `ERROR` and investigate |
| Output | Deterministic JSON to stdout plus bounded test output | `ERROR` on nondeterminism or file emission |
| Authority | Every authority, decision, assembly, and publication field remains false | `DENY` on an authority claim |
| Sensitive data | No real or reconstructable Fauna detail | Quarantine and notify authorized reviewers |

### Future candidate-specific profile

A candidate-specific Fauna dry run must additionally:

- name one accepted candidate and immutable artifact set;
- consume only public-safe packet metadata or governed references;
- never print protected values, exact coordinates, transform parameters, observer identities, private-land clues, or restricted source rows;
- resolve support through governed interfaces rather than direct canonical-store access;
- bind every finding to candidate, revision, policy version, validator profile, review context, and evaluation time;
- produce review support without writing release or public state; and
- fail closed when rights, sensitivity, stewardship, evidence, policy, review, correction, withdrawal, or rollback support is incomplete.

Environment variables express intent but are not a network sandbox. Use an isolated checkout and remove unrelated credentials. Do not run in a worktree containing unreviewed restricted Fauna payloads.

[Back to top](#top)

---

<a id="preflight-and-stop-conditions"></a>

## Preflight and stop conditions

### Freeze before execution

Record:

- repository, branch, and exact 40-hex commit;
- clean or dirty worktree status;
- candidate ID, or `NOT_ESTABLISHED`;
- helper, test, workflow, and validator revision;
- candidate, proof, manifest, and published lane counts;
- source-authority and policy posture;
- requested terminal boundary;
- verified reviewers and assignments; and
- overlapping pull request, migration, correction, withdrawal, or rollback work.

### Count-only inventory

Do not print payload contents. Exclude guidance files:

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

A nonzero count is not permission to open or expose a file. Determine access, sensitivity, ownership, and review posture first.

### Mandatory stop conditions

Stop candidate-specific evaluation when any condition applies:

1. no candidate exists;
2. frozen governing bytes changed;
3. overlapping work owns the same surface;
4. an input contains or may reveal protected animal, observer, telemetry, private-land, access, or site detail;
5. source identity, role, approved use, rights, or redistribution is unresolved;
6. taxonomic identity or a material crosswalk conflict is unresolved;
7. EvidenceRefs do not resolve to accepted EvidenceBundles;
8. public-safe transform, caveats, reconstruction risk, or transform proof is unresolved;
9. promotion policy is inactive or no accepted evaluator/result is bound;
10. required review, authority interval, or separation of duties is absent;
11. manifest placement or release vocabulary is ambiguous;
12. correction, withdrawal, cache invalidation, or rollback support is missing;
13. a command requires network, credentials, signing authority, deployment access, or mutable external state;
14. a workflow is green only because it successfully confirmed a hold; or
15. the result cannot be reported without exposing protected detail.

A correct `HOLD`, `DENY`, or `ABSTAIN` is preferable to an unsupported pass.

[Back to top](#top)

---

<a id="current-command-map"></a>

## Current command map

Run from repository root at the frozen revision.

### Shared synthetic publication-denial profile

```bash
KFM_NO_NETWORK=1 \
PYTHONHASHSEED=0 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
TZ=UTC \
make release-dry-run
```

This invokes the helper and its bounded unittest profile.

### Generic A–G declared-readiness fixtures

```bash
KFM_NO_NETWORK=1 \
PYTHONHASHSEED=0 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
TZ=UTC \
make publish-check
```

This validates fixture-only `ReviewRecord` and A–G readiness matrices. It does not evaluate the inactive promotion Rego stubs, resolve live evidence, authenticate actors, or create a decision.

### Synthetic Fauna fixture-safety suite

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

This validates synthetic fixture hygiene only.

### Registry-driven release-adjacent profile

```bash
KFM_NO_NETWORK=1 \
PYTHONHASHSEED=0 \
PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1 \
TZ=UTC \
make validator-release-profile
```

Treat this as release-adjacent fixture validation, not a candidate release gate.

### Commands not currently established

```text
fauna-release-dry-run
release-dry-run-fauna
```

Do not invent an alias, candidate path, shell script, or workflow invocation to make the documentation appear complete. A candidate-specific tool requires its own reviewed implementation slice.

[Back to top](#top)

---

<a id="shared-publication-denial-profile"></a>

## Shared publication-denial profile

The helper loads a repository-controlled synthetic promotion packet, copies it in memory, applies one negative mutation per case, invokes the bounded validator, and compares the observed result with the exact expected status and reason code.

| Case | Mutation | Expected status | Exact reason code | Publication posture |
|---|---|---|---|---|
| `evidence_missing` | clear `evidence_refs` | `ABSTAIN` | `PG_F_EVIDENCE_REF_MISSING` | denied |
| `policy_denied` | set declared policy evaluation to `DENY` | `DENY` | `PG_E_POLICY_DENY` | denied |
| `integrity_mismatch` | replace receipt output digest set | `DENY` | `PG_B_ARTIFACT_SET_MISMATCH` | denied |
| `rights_or_sensitivity_not_public_safe` | replace public-safe labels with `restricted` | `DENY` | `PG_E_PUBLIC_SAFE_LABEL_INVALID` | denied |
| `review_absent` | remove declared review | `DENY` | `PG_G_REVIEW_INVALID` | denied |

The suite passes only when:

- all five cases have exact expected statuses and sorted reason codes;
- readiness remains `BLOCKED` for every case;
- authority, decision, network, publication, and candidate-assembly claims remain false;
- repeated CLI executions emit byte-identical stdout; and
- repository file inventory is unchanged.

### What a pass proves

- the fixed synthetic mutations still trigger the expected bounded findings;
- the helper and tests executed at the tested revision;
- the tested path is deterministic under the supplied environment;
- the patched network entry point was not used; and
- no repository file was emitted.

### What a pass does not prove

- that a Fauna candidate exists;
- source admission, taxonomic truth, rights, or geoprivacy approval;
- EvidenceRef resolution;
- production policy evaluation;
- reviewer authenticity or independence;
- manifest, correction, withdrawal, or rollback validity;
- public-surface safety;
- promotion, release, deployment, publication, correction, withdrawal, or rollback; or
- required-check enforcement in repository settings.

The evidence-missing case returns `ABSTAIN`, not a policy denial. Publication remains blocked because cite-or-abstain forbids unsupported consequential claims. Do not translate `ABSTAIN` into warning-only or nearly ready.

[Back to top](#top)

---

<a id="operator-procedure"></a>

## Operator procedure

### 1. Freeze revision and scope

```bash
git rev-parse HEAD
git branch --show-current
git status --short
```

Record:

```text
candidate_id: NOT_ESTABLISHED
requested_boundary: CATALOG/TRIPLET -> PUBLISHED rehearsal
network_allowed: false
release_state_mutation_allowed: false
public_state_mutation_allowed: false
```

Replace `NOT_ESTABLISHED` only after a verified child candidate exists and its identifier is safe for the audience.

### 2. Inventory without opening payloads

Run the count-only inventory. At the inspected checkpoint, the expected non-guidance counts are zero. A changed count triggers review, not automatic progression.

### 3. Verify implementation boundaries

Confirm that:

- the helper still loads the fixed synthetic baseline;
- its case set remains the five documented mutations;
- all authority and publication fields remain false;
- tests still enforce no-network behavior, deterministic output, and no file emission;
- the Make target invokes only the bounded helper and tests;
- the shared workflow has read-only contents permission and no release or deployment secret;
- the Fauna workflow still marks proof and candidate-specific dry run as holds; and
- no new candidate-specific target appeared without a reviewed contract and tests.

Stop when an assumption changed.

### 4. Run the shared denial profile

Execute `make release-dry-run` and require:

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

Do not copy the synthetic packet or its pass status into a Fauna candidate record.

### 5. Run generic readiness fixtures

Execute `make publish-check`. Interpret success as fixture-only declared readiness, not authenticated support or transition authority.

### 6. Run Fauna fixture safety

Execute the exact Fauna unittest command. Confirm positive and negative fixture polarity without treating fixture success as candidate readiness.

### 7. Apply the candidate closure matrix

Because no candidate exists at the inspected checkpoint, stop at:

```text
outcome: HOLD
reason: no verified child Fauna candidate dossier
next authority: accountable candidate commissioning and review
public effect: none
```

Do not substitute a synthetic fixture, planning example, source template, or range product.

### 8. Inspect hosted exact-head evidence

Bind every workflow result to the exact pull-request head. Separate:

- documentation checks;
- shared denial checks;
- generic readiness fixtures;
- Fauna fixture checks;
- explicit hold jobs;
- introduced failures;
- inherited or concurrent failures; and
- repository-settings enforcement, which requires separate evidence.

### 9. Prepare the public-safe handoff

Use the template below. Include no protected values.

### 10. Stop

Do not create or mutate candidate, evidence, proof, decision, receipt, manifest, correction, withdrawal, rollback, public carrier, API, map, tile, cache, search, graph, export, deployment, release, promotion, or publication state.

[Back to top](#top)

---

<a id="fauna-candidate-publication-gates"></a>

## Fauna candidate publication gates

A future candidate-specific dry run must preserve these distinctions.

### Candidate and object family

- Name one candidate, immutable artifact set, specification hash, domain scope, audience, and requested boundary.
- Identify taxon, crosswalk, conservation status, occurrence, restricted occurrence, public occurrence, range, seasonal range, migration context, sensitive site, mortality, disease, invasive-species, and transform-support objects explicitly.
- Do not let a product name or folder imply canonical ownership.

### Taxonomy

- Bind names to taxon concepts and source authority, not strings alone.
- Preserve accepted, synonym, provisional, unresolved, split, lump, and conflict posture.
- Record taxonomic version and crosswalk limits.
- Abstain from species-level claims when support is broader.

### Source, rights, and stewardship

- Require accepted source descriptors and approved uses.
- Keep observation, specimen, citizen-science, model, aggregate, administrative, regulatory, contextual, and synthetic roles distinct.
- Verify access, redistribution, citation, retention, derivative, audience, and revocation obligations.
- API access or discoverability does not establish public-use permission.

### Occurrence, range, season, and migration

- occurrence supports a bounded observation, not general range;
- range does not prove presence at a point or time;
- seasonal range does not prove year-round presence;
- migration context must not reveal or predict an individual path; and
- non-detection is not absence unless sampling design supports the inference.

### Sensitivity and geoprivacy

- Transform before rendering or delivery; client-side hiding is not a safe transform.
- Review coordinates, centroids, boxes, tiles, feature IDs, source-layer names, counts, timestamps, URLs, logs, caches, screenshots, exports, and cross-domain joins.
- Bind the public derivative to transform identity, digests, audience, caveats, evidence, policy, and review without exposing protected parameters.
- Test reverse inference, differencing, repeated queries, temporal correlation, private-land, access-road, imagery, and habitat joins.

### Evidence and scientific support

- Resolve every consequential EvidenceRef to an accepted EvidenceBundle.
- Preserve support type, spatial and temporal scope, source role, uncertainty, caveats, and contradiction state.
- Do not treat a receipt, summary, model, index, tile, graph, or generated answer as root evidence.
- Keep suitability, predicted occupancy, interpolated density, observed count, effort, mortality, disease, and population trend distinct.

### Validation and integrity

- Bind candidate, artifacts, receipts, proofs, manifest, and public carrier by deterministic identity and digest.
- Validate schema, geometry/CRS, time, taxonomy, source role, evidence closure, rights, sensitivity, field allowlists, transform support, and reconstruction risk.
- Include negative fixtures for exact-location leakage, encoded clues, missing source identity, taxonomy conflict, evidence gap, rights gap, policy gap, review gap, correction gap, and rollback gap.
- Diagnostics must not echo protected values.

### Policy, review, and release support

- Use an accepted policy source, bundle, evaluator, entry point, input contract, result normalization, version, and digest.
- Missing context, unknown labels, evaluator failure, inactive stubs, and unbound policy never default to allow.
- Authenticate subject, reviewer, assignment, scope, authority interval, obligations, and supersession state.
- Prevent self-review when materiality requires separation.
- Resolve the canonical manifest lane before creating an instance.
- Bind included artifacts, evidence, proof, receipts, policy, reviews, decisions, signatures, correction, withdrawal, rollback, changelog, and public-carrier identity.

### Public clients and governed AI

- Standard clients consume governed APIs or released public-safe artifacts only.
- Evidence Drawer and Focus Mode expose evidence, time, policy, release, stale, correction, and withheld/denied context appropriate to the audience.
- AI may interpret released evidence; it cannot infer protected coordinates, expand beyond EvidenceBundle scope, or approve release.
- A polished map, popup, dashboard, report, story, export, or answer cannot compensate for an unresolved gate.

[Back to top](#top)

---

<a id="current-closure-matrix"></a>

## Current closure matrix

| Closure area | Current status | Reason | Required before candidate-specific dry run |
|---|---|---|---|
| Candidate and artifact set | **HOLD** | No verified child dossier | Accepted child candidate with immutable public-safe pointers |
| Source admission | **HOLD** | Empty authority projection; no candidate source set | Accepted descriptors, roles, rights, purpose, and cadence |
| Taxonomy | **HOLD** | No candidate taxon packet | Reviewed concepts, versions, conflicts, and limitations |
| Evidence and proof | **HOLD** | No Fauna proof or candidate EvidenceBundle closure | Resolvable EvidenceRefs and accepted proof support |
| Rights and stewardship | **HOLD** | No candidate-specific decision | Current approved-use, redistribution, stewardship, and audience decisions |
| Sensitivity and geoprivacy | **HOLD** | No transform or review packet | Transform proof, reconstruction review, caveats, and decision |
| Candidate validation | **HOLD** | Existing Fauna suite is synthetic fixture hygiene only | Candidate-bound profile, fixtures, tests, and findings |
| Generic A–G validation | **PARTIAL / BOUNDED** | Declared-packet validator exists | Candidate-specific accepted input and support resolution |
| Promotion policy | **HOLD** | Rego stubs inactive; no evaluator binding | Accepted fail-closed bundle, evaluator, input, output, and consumer |
| Accountable review | **HOLD** | Only GitHub routing verified | Assignments, independence, scope, obligations, and review records |
| Decision and receipt | **HOLD** | No Fauna instance | Governed candidate-bound records after review |
| Release manifest | **HOLD / CONFLICTED** | No instance; topology unresolved | Accepted canonical lane and candidate-bound manifest |
| Correction and withdrawal | **HOLD** | No candidate-specific closure | Accepted correction, supersession, withdrawal, notice, and propagation plan |
| Rollback | **HOLD** | No candidate target or drill | Candidate-bound target, card, and bounded rehearsal |
| Public carrier | **HOLD** | No direct-child carrier | Release-authorized public-safe carrier with digest and support bindings |
| Governed API, map, export, AI | **HOLD / UNKNOWN** | No candidate release binding | End-to-end consumption and invalidation evidence |
| Release, deployment, publication | **NOT ESTABLISHED** | No accountable decision or transition evidence | Separate authorized transitions after every gate closes |

Current human-facing outcome:

```text
outcome: HOLD
primary_reason: FAUNA_CANDIDATE_NOT_ESTABLISHED
public_state_changed: false
release_state_changed: false
source_activation_changed: false
```

These explanatory labels are not accepted wire-level enums. Do not serialize them into a governed record unless an accepted contract defines them.

[Back to top](#top)

---

<a id="hosted-ci-and-held-job-interpretation"></a>

## Hosted CI and held-job interpretation

| Workflow | A success can show | A success cannot show |
|---|---|---|
| `release-dry-run` | Shared denial, bounded A–G fixtures, and synthetic rollback support completed at exact head | Candidate assembly, live policy, evidence authentication, release, or publication |
| `promotion-gate` | Fixture-only review and readiness profile completed | Authenticated reviewer, accepted policy, decision, or transition |
| `domain-fauna` | Synthetic fixture suite completed and hold assertions remained true | Fauna proof, domain dry run, source admission, or real-data safety |
| Documentation checks | Current docs checks passed by their definitions | Scientific truth, rights, sensitivity, release authority, or operations |

### Exact-head rule

Report:

- PR number and exact head SHA;
- workflow/run/job identity;
- status and conclusion;
- changed-area relevance;
- introduced, inherited, concurrent, or unresolved failure classification;
- whether a successful job confirmed a hold; and
- whether all runs settled.

A check from an older head becomes stale when the branch moves.

### Held-success rule

A successful Fauna publication-dry-run hold job means the workflow confirmed that no accepted candidate-specific command and contract appeared. It does **not** mean a Fauna publication dry run ran.

A successful Fauna proof hold job means the workflow confirmed that no accepted proof producer and artifact appeared. It does **not** mean a proof was built.

A workflow appearing on a PR does not prove it is required by a ruleset. Required-check coupling and branch protection need separate current evidence.

[Back to top](#top)

---

<a id="public-safe-review-handoff"></a>

## Public-safe review handoff

Include only:

- repository and exact revision;
- command/profile and relevant blob identities;
- candidate ID or `NOT_ESTABLISHED`;
- requested lifecycle boundary and audience;
- count-only lane inventory;
- public-safe source, taxon, EvidenceRef, and EvidenceBundle IDs and statuses;
- rights, sensitivity, geoprivacy, policy, validation, review, correction, withdrawal, and rollback status;
- exact shared statuses and public-safe reason codes;
- exact-head hosted checks;
- introduced versus inherited failures;
- finite handoff outcome;
- next verified authority; and
- explicit non-effects.

```markdown
## Fauna publication-gate dry-run handoff

- Repository: `bartytime4life/Kansas-Frontier-Matrix`
- Exact revision: `<40-hex SHA>`
- Candidate: `NOT_ESTABLISHED` or `<public-safe candidate ID>`
- Requested boundary: `CATALOG/TRIPLET -> PUBLISHED rehearsal`
- Shared denial profile: `PASS | ABSTAIN | DENY | ERROR`
- Generic A–G fixtures: `PASS | ABSTAIN | DENY | ERROR`
- Fauna fixture-safety profile: `PASS | FAIL | ERROR`
- Candidate-specific result: `HOLD | DENY | ABSTAIN | ERROR | REVIEW HANDOFF READY`
- Candidate/proof/manifest/published counts: `<count-only>`
- Source admission: `<status and public-safe IDs>`
- Taxonomy: `<status and public-safe IDs>`
- Evidence/proof: `<status and public-safe IDs>`
- Rights/stewardship: `<status>`
- Sensitivity/geoprivacy: `<status>`
- Policy: `<status and accepted evaluator ID, if any>`
- Review/separation: `<status>`
- Correction/withdrawal/rollback: `<status>`
- Exact-head checks: `<status summary>`
- Introduced failures: `<none or bounded list>`
- Inherited/concurrent failures: `<none or bounded list>`
- Outcome: `<finite classification>`
- Next accountable authority: `<verified assignment or NEEDS VERIFICATION>`
- Public state changed: `false`
- Release state changed: `false`
- Source activation changed: `false`
```

Do not include coordinates, protected site clues, transform thresholds or secrets, source rows, observer identities, private-land/access detail, restricted URLs, credentials, unredacted logs, or language enabling reverse inference.

Current handoff:

```text
candidate: NOT_ESTABLISHED
candidate-specific dry run: HOLD
review handoff ready: no
release/deployment/publication effect: none
```

[Back to top](#top)

---

<a id="graduation-criteria"></a>

## Graduation criteria

Do not remove the workflow hold because this document is complete. Graduate the candidate-specific Fauna dry-run lane only through a separate implementation that establishes:

1. an accepted candidate and no-write input/output contract;
2. verified homes for candidate, proof, decision, receipt, manifest, correction, withdrawal, and rollback families;
3. one explicitly non-releasable public-safe synthetic candidate fixture;
4. negative fixtures for source, taxonomy, evidence, rights, sensitivity, reconstruction, transform, policy, review, integrity, correction, and rollback failures;
5. accepted source descriptors and approved uses;
6. taxon concept, authority/version, crosswalk, conflict, and uncertainty closure;
7. resolvable fixture EvidenceRefs and bounded EvidenceBundles;
8. geoprivacy contract, proof/receipt binding, safe diagnostics, and reverse-inference tests;
9. accepted fail-closed policy bundle, evaluator, entry point, input/output contract, and consumer;
10. review and assignment shapes that keep synthetic proof separate from production authority;
11. accepted manifest, decision, receipt, correction, withdrawal, and rollback contracts;
12. tests proving no lifecycle, release, cache, API, map, tile, index, graph, export, or published mutation;
13. deterministic no-network execution with explicit guards;
14. stable safe reason codes without protected values;
15. least-privilege workflow permissions, pinned actions, timeouts, and explicit non-effects;
16. synchronized runbook, workflow, tool, test, index, and register documentation;
17. exact-head changed-area validation and transparent implementation rollback; and
18. accountable domain, source/rights, taxonomy, sensitivity, evidence, policy, validation, independent-review, release, correction, and rollback assignments.

The first graduated command must still stop before release and publication.

[Back to top](#top)

---

<a id="correction-withdrawal-and-rollback"></a>

## Correction, withdrawal, and rollback

### Dry-run correction

When helper behavior, fixtures, reason codes, or workflows change:

1. freeze old and new exact revisions;
2. identify the contract change;
3. rerun all five negative cases;
4. compare deterministic output and exact codes;
5. update tests and this runbook in the same coherent boundary when intentional;
6. preserve prior receipts and exact-tree references;
7. do not rewrite old evidence to match new code; and
8. record unresolved compatibility as `HOLD` or `CONFLICTED`.

A future candidate dry run routes incorrect source, taxonomy, evidence, transform, rights, policy, or validation support back to its owning lane. It must not repair canonical or restricted data inside release tooling.

### Public correction and withdrawal

No current Fauna public carrier was established by the bounded inventory, so this procedure cannot execute public correction or withdrawal.

For a future release:

- retain immutable original history;
- issue correction or withdrawal through accepted release-family authority;
- publish an audience-appropriate notice;
- invalidate or supersede governed API, tile, cache, search, graph, export, screenshot, and AI-facing derivatives;
- bind successor or withdrawal state to evidence, review, decision, and rollback records; and
- verify public surfaces rather than assuming repository changes propagated.

### Rollback boundary

Synthetic rollback-card checks do not execute rollback. Candidate-specific rollback readiness requires a stable prior target, enumerated consumers, explicit correction/withdrawal relationships, bounded cache/index/tile/API invalidation, protected-data preservation, successful rehearsal, and accountable review.

### This document's rollback

Before merge, close or abandon the draft PR and leave `main` unchanged. After merge, use a transparent revert of the actual merge commit or a reviewed forward correction. Do not rewrite shared history.

Reverting this Markdown file would not withdraw a source, undo a lifecycle transition, roll back a release, invalidate a public carrier, or change deployment state because this documentation change creates none of those effects.

[Back to top](#top)

---

<a id="evidence-basis"></a>

## Evidence basis

| Surface | Use | Limitation |
|---|---|---|
| [Directory Rules](../../doctrine/directory-rules.md) and [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Placement and responsibility separation | No runtime proof |
| [CODEOWNERS](../../../.github/CODEOWNERS) | GitHub review routing | Not substantive authority or completed review |
| [Fauna candidate README](../../../release/candidates/fauna/README.md) and bounded inventory | Candidate-lane boundary and absent child dossier | Does not cover external or restricted systems |
| [Fauna proof README](../../../data/proofs/fauna/README.md) and bounded inventory | Proof-lane boundary and absent artifact | README is not proof |
| [Fauna manifest README](../../../release/manifests/fauna/README.md) and bounded inventory | Manifest guidance and topology conflict | No instance or accepted canonical lane |
| [Fauna published README](../../../data/published/fauna/README.md) and bounded inventory | Public-carrier boundary and absent carrier | Folder presence is not publication |
| [Source-authority projection](../../../control_plane/source_authority_register.yaml) | Empty current projection posture | Does not admit or activate sources |
| [Shared helper](../../../tools/release/release_dry_run.py) | Exact five-case implementation | Synthetic baseline only |
| [Shared tests](../../../tests/release/test_publication_deny_dry_run.py) | Polarity, code, no-network, determinism, and no-emission assertions | Bounded Python test surface |
| [Promotion-gate README](../../../tools/validators/promotion_gate/README.md) | A–G checks, finite results, and limits | Declared context only; no live authority |
| [Promotion policy README](../../../policy/promotion/README.md) | Inactive policy posture | No production policy evaluation |
| [Fauna workflow](../../../.github/workflows/domain-fauna.yml) | Synthetic validation and explicit holds | Workflow success is not release |
| [Release-dry-run workflow](../../../.github/workflows/release-dry-run.yml) | Read-only orchestration | No real candidate or publication |
| [Fauna Promotion Runbook](./PROMOTION_RUNBOOK.md) | Current promotion-readiness boundary | Documentation cannot create authority |
| [Fauna No-Network Runbook](./NO_NETWORK_TEST_RUNBOOK.md) | Synthetic fixture procedure | Fixture hygiene only |
| [Fauna Release Index](../../domains/fauna/RELEASE_INDEX.md) | Navigation lineage and vocabulary conflicts | Illustrative IDs are not releases |

### Evidence limits

- Git-tree presence proves bytes at a revision, not scientific correctness, legal permission, release, deployment, or publication.
- Direct-child inventories are bounded to inspected paths and revision.
- Connector-only authoring did not execute repository-native commands locally.
- No live source, protected payload, production policy engine, reviewer-authority service, release service, public API, map, tile server, cache, or deployment was exercised.
- Operational state beyond visible repository evidence remains `UNKNOWN` or `NEEDS VERIFICATION`.

The `created` date in this file records creation of the substantive v1.0 runbook. The creation date of the prior inventory-generated scaffold remains unknown.

[Back to top](#top)

---

<a id="operator-checklist"></a>

## Operator checklist

### Freeze and safety

- [ ] Exact repository and head recorded.
- [ ] Branch and worktree status recorded.
- [ ] Candidate ID recorded or `NOT_ESTABLISHED`.
- [ ] Active overlap checked.
- [ ] No restricted or uncommitted sensitive payload present.
- [ ] No source credential, network, signing, deployment, or public-write dependency.
- [ ] Count-only inventory used.

### Shared validation

- [ ] `make release-dry-run` ran at the exact revision.
- [ ] Five cases observed.
- [ ] Exact statuses and reason codes matched.
- [ ] Every publication outcome remained denied.
- [ ] Every readiness remained `BLOCKED`.
- [ ] Authority, decision, network, publication, and assembly fields remained false.
- [ ] Determinism and no-emission tests passed.

### Generic and Fauna fixtures

- [ ] `make publish-check` interpreted as fixture-only declared readiness.
- [ ] Fauna fixture-safety suite ran.
- [ ] Positive and negative fixture polarity remained exact.
- [ ] Synthetic success was not translated into candidate readiness.
- [ ] Proof and dry-run jobs were reported as holds when applicable.

### Candidate closure

- [ ] Candidate and immutable artifact set exist.
- [ ] Source admission and approved use are accepted.
- [ ] Taxonomy packet is reviewed.
- [ ] EvidenceRefs resolve to accepted EvidenceBundles.
- [ ] Rights and stewardship decisions are current.
- [ ] Geoprivacy transform and reconstruction review are accepted.
- [ ] Candidate validation is deterministic and negative-tested.
- [ ] Promotion policy is active, accepted, and bound.
- [ ] Required reviewers and separation are authenticated.
- [ ] Manifest lane and vocabulary are unambiguous.
- [ ] Correction, withdrawal, and rollback are closed.
- [ ] Public carrier and consumers are identified and reversible.

### Handoff

- [ ] Exact-head hosted status recorded.
- [ ] Introduced and inherited failures separated.
- [ ] Public-safe reason codes only.
- [ ] No protected values exposed.
- [ ] Finite outcome and next accountable authority recorded.
- [ ] Public, release, deployment, and source-activation state unchanged.

At the inspected checkpoint, the checklist stops at **candidate closure: candidate not established**, and the final outcome is **HOLD**.

[Back to top](#top)
