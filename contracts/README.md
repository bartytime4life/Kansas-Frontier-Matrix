<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS_VERIFICATION_UUID>
title: Contracts
type: standard
version: v1
status: draft
owners: @bartytime4life
created: <NEEDS_VERIFICATION_YYYY-MM-DD>
updated: <NEEDS_VERIFICATION_YYYY-MM-DD>
policy_label: <NEEDS_VERIFICATION_POLICY_LABEL>
related: [../README.md, ../schemas/README.md, ../policy/README.md, ../tests/README.md, ../docs/standards/README.md, ../.github/workflows/README.md, ../.github/CODEOWNERS, ../.github/PULL_REQUEST_TEMPLATE.md]
tags: [kfm, contracts, trust-objects, json-schema, validation]
notes: [Current public main confirms /contracts/ ownership and README-only tree visibility; doc_id, created, updated, and policy_label need commit-time verification.]
[/KFM_META_BLOCK_V2] -->

# Contracts

Machine-readable contract backbone for KFM source admission, policy mediation, release proof, runtime trust, and correction lineage.

> [!IMPORTANT]
> **Status:** `experimental` *(INFERRED from sibling README surfaces on current public `main`; verify if the checked-out branch differs)*  
> **Doc status:** `draft`  
> **Owners:** `@bartytime4life` *(current public `CODEOWNERS` owner for `/contracts/`)*  
> **Path:** `contracts/README.md`  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![doc](https://img.shields.io/badge/doc-draft-lightgrey) ![owners](https://img.shields.io/badge/owners-%40bartytime4life-blue) ![scope](https://img.shields.io/badge/scope-contracts-0969da) ![truth](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20INFERRED%20%7C%20PROPOSED-lightgrey) ![schema authority](https://img.shields.io/badge/schema%20authority-pending-red) ![public tree](https://img.shields.io/badge/public%20tree-README--only-lightgrey)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)  
> **Repo fit:** path `contracts/README.md` · upstream [`../README.md`](../README.md), [`../schemas/README.md`](../schemas/README.md), [`../policy/README.md`](../policy/README.md), [`../tests/README.md`](../tests/README.md), [`../docs/standards/README.md`](../docs/standards/README.md), [`../.github/workflows/README.md`](../.github/workflows/README.md) · control surfaces [`../.github/CODEOWNERS`](../.github/CODEOWNERS), [`../.github/PULL_REQUEST_TEMPLATE.md`](../.github/PULL_REQUEST_TEMPLATE.md) · downstream governed APIs, release assembly, `EvidenceBundle` resolution, `RuntimeResponseEnvelope` emitters, correction lineage, and the hydrology-first thin slice

> [!NOTE]
> Current public `main` now confirms `contracts/` contains `README.md` only. Treat this directory as a real boundary surface, not as an already-materialized contract registry.

> [!WARNING]
> The March 2026 KFM corpus is stronger on doctrine than the current public tree is on mounted machine artifacts. This README therefore distinguishes **current public repo evidence** from **PROPOSED starter structure** and keeps schema-home authority explicitly **UNKNOWN / NEEDS VERIFICATION** until the repo resolves it.

## Scope

`contracts/` is where KFM stops speaking only in doctrine and starts publishing typed trust objects.

In KFM, contracts are not ornamental API notes. They are the machine-readable edge of the governed truth path: the object shapes that make source admission, validation, policy decisions, release readiness, runtime evidence, and correction lineage testable instead of merely persuasive.

### Truth posture used in this README

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Directly supported by March 2026 KFM doctrine or by current public repo evidence inspected for this revision |
| **INFERRED** | Conservative completion drawn from adjacent repo surfaces or repeated KFM practice, but not explicitly stated in the current `contracts/README.md` |
| **PROPOSED** | Doctrine-consistent starter layout, schema path, fixture layout, validator pattern, or route-family shape not yet proven as mounted implementation |
| **UNKNOWN / NEEDS VERIFICATION** | Branch-specific details, authoritative schema-home ADR, real machine-readable inventory, fixture density, workflow YAML, mounted policy bundles, and exact runtime emitters not yet re-verified on the checked-out branch |

### What this directory is for

`contracts/` should answer questions like these:

- What object must exist before a source is admitted?
- What fields make a policy decision reconstructable?
- What release object proves publication readiness?
- What runtime envelope makes an answer accountable?
- What correction object prevents silent overwrite?

### Why this matters in KFM

KFM doctrine is explicit that trust changes state through governed transitions, not through casual file movement, smooth UI presentation, or implied enforcement. That means named, typed, diffable, testable objects are part of the operating system of trust.

Without machine-checkable contracts, KFM can stay architecturally strong while remaining operationally under-enforced.

[Back to top](#contracts)

## Repo fit

| Item | Value |
|---|---|
| **Path** | `contracts/README.md` |
| **Directory role** | Contract publication and machine-readable trust-object reference surface |
| **Upstream constraints** | [`../schemas/README.md`](../schemas/README.md) · [`../policy/README.md`](../policy/README.md) · [`../tests/README.md`](../tests/README.md) · [`../docs/standards/README.md`](../docs/standards/README.md) · [`../.github/workflows/README.md`](../.github/workflows/README.md) |
| **Downstream consumers** | Governed APIs, release assembly, policy mediation, `EvidenceBundle` resolution, `RuntimeResponseEnvelope` emitters, correction lineage, and the hydrology-first thin slice |
| **Current repo signal** | `contracts/` and `schemas/` both exist as schema/contract documentation surfaces; `docs/standards/README.md` currently routes “API endpoint schemas and machine contracts” toward `../contracts/`; one authoritative schema home still needs explicit resolution |
| **Trust rule** | Contracts define shapes and minimum semantics; contracts alone do **not** grant publication, approval, or runtime permission |

### Current verified snapshot

| Area | Status | What that means here |
|---|---|---|
| `contracts/README.md` as a repo documentation surface | **CONFIRMED** | The contracts lane exists as a real directory README |
| Current visible `contracts/` inventory | **CONFIRMED** | Current public `main` shows `README.md` only inside `contracts/`; no checked-in machine-readable contract files are visible in this directory from the public tree |
| `schemas/README.md` as a parallel documentation surface | **CONFIRMED** | Authority is currently ambiguous across two top-level documentation surfaces |
| Current visible `schemas/` inventory | **CONFIRMED** | Current public `main` shows `README.md` only inside `schemas/` |
| Current visible `.github/workflows/` inventory | **CONFIRMED** | Current public `main` shows `README.md` only inside `.github/workflows/` |
| `/contracts/` ownership in `CODEOWNERS` | **CONFIRMED** | Current public `CODEOWNERS` routes `/contracts/` to `@bartytime4life` |
| PR truth/evidence checklist | **CONFIRMED** | The repo’s PR template requires honest truth labels plus linked evidence / proof / validation material |
| Standards routing toward `contracts/` | **CONFIRMED** | `docs/standards/README.md` keeps standards separate while treating machine contracts as an adjacent governed surface, and `schemas/README.md` points readers toward the contract lane while warning against parallel authority |
| Authoritative schema home | **UNKNOWN / NEEDS VERIFICATION** | An ADR or equivalent decision should make one home canonical before CI gates depend on it |
| Real machine-readable contract inventory | **UNKNOWN / NEEDS VERIFICATION** | The current public `contracts/` tree does not yet prove a checked-in schema registry or versioned contract lattice |
| Valid / invalid contract fixtures | **PROPOSED** | Doctrine and repo-grounded planning pressure call for them, but they are not yet evidenced as mounted artifacts here |
| Merge-blocking validator workflow | **PROPOSED** | The repo surface documents workflow doctrine, but current public `main` does not expose a checked-in contracts gate YAML |

> [!NOTE]
> The March 2026 corpus is strong on **which** contract families KFM needs. It is still cautious on **where** the final authoritative machine-contract home will settle. This README uses a versioned `contracts/v1/` publication shape as the default starter pattern because it is the clearest current repo-native next move, but that pathing remains **PROPOSED** until authority is resolved explicitly.

[Back to top](#contracts)

## Accepted inputs

The following belong in `contracts/`:

| Belongs here | Why it belongs here |
|---|---|
| Versioned JSON Schema files for trust-bearing objects | They make KFM object families explicit enough to validate, diff, gate, and evolve |
| Shared header/profile schema(s) | They stabilize common fields, version grammar, and minimum contract identity |
| Contract-local migration notes | They keep additive evolution and breaking-change handling explicit |
| Vocabulary registries for reasons / obligations / reviewer roles | Only if the authoritative-home decision assigns shared vocab ownership here |
| Companion examples or excerpts tied to schema publication | Useful when they clarify semantics without replacing test fixtures as the authoritative validation surface |
| OpenAPI starter fragments for governed route families | Only when this directory is the agreed publication home for boundary contracts, not merely narrative route notes |

### Minimum bar for anything added here

- It has a clear lifecycle seam.
- It is versioned.
- It is machine-validatable.
- It has at least one valid example.
- It has at least one invalid example.
- Required fields are explicit.
- Time basis is explicit.
- Rights or sensitivity posture is explicit where relevant.
- Correction or supersession behavior is explicit where relevant.
- At least one named gate, test, or drill is intended to exercise it.

[Back to top](#contracts)

## Exclusions

The following do **not** belong in `contracts/` as source-of-truth assets:

| Does **not** belong here | Goes instead | Why |
|---|---|---|
| Executable policy bundles and Rego logic | [`../policy/`](../policy/) | Policy should stay executable and separately reviewable |
| Workflow YAML and merge-gate wiring | [`../.github/workflows/`](../.github/workflows/) | CI wiring enforces contracts but is not itself the contract layer |
| Runtime or service implementation code | service / app / package surfaces | Emitters, resolvers, and handlers should consume contracts, not live inside them |
| Canonical or derived data artifacts | `../data/` or equivalent lifecycle zones | Contracts describe objects; they are not the objects themselves |
| Release proof artifacts themselves | release / proof or published stores | `ReleaseManifest` schema belongs here; emitted release evidence does not |
| UI payload renderers and shell state logic | app / shell packages | The contract surface should stay transport- and renderer-independent |
| Exploratory notebooks and ad hoc test scraps | notebooks / scratch / examples | Trust-bearing law should not be hidden in ephemeral work areas |

### Contract / schema authority hazard

A strong exclusion rule for this README is **parallel schema law**.

If `contracts/` and `schemas/` both evolve as authoritative homes, CI can validate one tree while code, docs, review logic, or runtime expectations silently drift against the other. Until the repo resolves that split, any new contract work should be accompanied by an explicit authority note and a migration plan.

[Back to top](#contracts)

## Directory tree

### Current confirmed public-main snapshot

```text
repo-root/
├─ contracts/
│  └─ README.md
├─ schemas/
│  └─ README.md
├─ policy/
│  └─ README.md
├─ tests/
│  └─ README.md
└─ .github/
   └─ workflows/
      └─ README.md
```

### Starter target shape after the authority ADR (**PROPOSED**)

```text
contracts/
├─ README.md
├─ v1/
│  ├─ common/
│  │  └─ header_profile.schema.json
│  ├─ policy/
│  │  └─ decision_envelope.schema.json
│  ├─ evidence/
│  │  └─ evidence_bundle.schema.json
│  ├─ runtime/
│  │  └─ runtime_response_envelope.schema.json
│  ├─ correction/
│  │  └─ correction_notice.schema.json
│  ├─ release/
│  │  └─ release_manifest.schema.json
│  ├─ source/
│  │  └─ source_descriptor.schema.json
│  └─ data/
│     └─ dataset_version.schema.json
└─ vocab/
   ├─ reason_codes.json
   ├─ obligation_codes.json
   └─ reviewer_roles.json
```

### Companion fixture location recommended by current evidence (**PROPOSED**)

```text
tests/
└─ fixtures/
   └─ contracts/
      └─ v1/
         ├─ valid/
         └─ invalid/
```

[Back to top](#contracts)

## Quickstart

The safest path here is **inspection first**, not assumption first.

### 1) Inspect the visible tree and adjacent governed surfaces

```bash
# inspect the visible contracts lane
find contracts -maxdepth 3 -type f 2>/dev/null | sort

# inspect sibling schema and workflow lanes
find schemas -maxdepth 2 -type f 2>/dev/null | sort
find .github/workflows -maxdepth 2 -type f 2>/dev/null | sort

# inspect ownership and review boundaries
sed -n '1,200p' .github/CODEOWNERS 2>/dev/null || true
sed -n '1,240p' .github/PULL_REQUEST_TEMPLATE.md 2>/dev/null || true

# inspect adjacent documentation surfaces
sed -n '1,220p' contracts/README.md 2>/dev/null || true
sed -n '1,220p' schemas/README.md 2>/dev/null || true
sed -n '1,220p' policy/README.md 2>/dev/null || true
sed -n '1,220p' tests/README.md 2>/dev/null || true
sed -n '1,220p' docs/standards/README.md 2>/dev/null || true

# inspect likely contract vocabulary without guessing a runtime package
grep -RIn "DecisionEnvelope\|EvidenceBundle\|RuntimeResponseEnvelope\|CorrectionNotice\|ReleaseManifest" \
  contracts schemas policy tests docs 2>/dev/null || true
```

### 2) Resolve schema-home authority first

Before adding a merge-blocking validator, declare **one** authoritative schema home.

That decision should do three things:

1. name the canonical publication path,
2. mark the non-authoritative sibling surface clearly, and
3. update this README, sibling docs, and CI references together.

### 3) Add the smallest first contract wave

Recommended **Wave 01**:

- `DecisionEnvelope`
- `EvidenceBundle`
- `RuntimeResponseEnvelope`
- `CorrectionNotice`
- `ReleaseManifest`

Recommended **Wave 01.5**:

- `SourceDescriptor`
- `DatasetVersion`

### 4) Add valid and invalid fixtures immediately

```bash
# Illustrative only — verify the repo's real validator entrypoint before commit.
python -m jsonschema \
  -i tests/fixtures/contracts/v1/valid/runtime_response_envelope.min.json \
  contracts/v1/runtime/runtime_response_envelope.schema.json
```

```bash
# Illustrative only — invalid fixtures should fail the build on purpose.
python -m jsonschema \
  -i tests/fixtures/contracts/v1/invalid/runtime_response_envelope.missing_citations.json \
  contracts/v1/runtime/runtime_response_envelope.schema.json
```

### 5) Wire one deterministic merge gate

```text
PSEUDOCODE ONLY
---------------
<contracts-validator-command>
  -> validates Wave 01 schemas
  -> validates valid fixtures
  -> confirms invalid fixtures fail
  -> exits non-zero on any drift
```

### 6) Keep negative outcomes first-class

For KFM, the following are not embarrassing edge cases:

- `ABSTAIN`
- `DENY`
- `ERROR`
- `STALE-VISIBLE`
- `GENERALIZED`
- `SUPERSEDED`
- `WITHDRAWN`
- `CORRECTION-PENDING`

If a contract wave cannot express and test those states where relevant, it is incomplete.

[Back to top](#contracts)

## Usage

### Add a new contract family safely

1. Add it only if it governs a real lifecycle step, trust seam, or visible state.
2. Place it in the most specific contract family path available.
3. Define minimum identifiers, timestamps, rights/sensitivity fields, and review/policy linkage where relevant.
4. Add one valid and one invalid fixture.
5. Add or update the corresponding registry values if the object depends on reason/obligation/role vocab.
6. Update adjacent docs and route-family notes if boundary behavior changes.
7. Add or extend a gate, drill, or test that proves the object matters operationally.

### Change an existing contract safely

- Prefer additive evolution by default.
- Add fields before renaming them.
- Version meaning changes explicitly.
- Keep old fixtures interpretable long enough to preserve audit history.
- Do not let runtime code depend on undocumented fields.
- Do not let a convenience DTO quietly replace the public contract.

### Keep transport separate from contract law

A route may change. A service may move. A framework may be replaced.

The trust-bearing object role should survive those changes. That is why KFM repeatedly treats filenames, DTOs, and route names as less important than stable object semantics.

[Back to top](#contracts)

## Diagram

```mermaid
flowchart LR
    A[SourceDescriptor] --> B[IngestReceipt]
    B --> C[ValidationReport]
    C --> D[DatasetVersion]
    D --> E[CatalogClosure]
    E --> F[DecisionEnvelope]
    F --> G[ReviewRecord]
    G --> H[ReleaseManifest / ReleaseProofPack]
    H --> I[ProjectionBuildReceipt]
    H --> J[EvidenceBundle]
    J --> K[RuntimeResponseEnvelope]
    H --> L[CorrectionNotice]

    M[policy bundles / vocab registries] -. shapes decisions .-> F
    N[tests / fixtures] -. validate .-> A
    N -. validate .-> K
    O[workflow gate] -. blocks invalid objects .-> K
    P[UI shell / Evidence Drawer / Focus] -. consumes governed outputs .-> J
    P -. consumes governed outputs .-> K
    L -. propagates lineage .-> P
```

[Back to top](#contracts)

## Tables

### Contract family registry

| Contract family | Minimum purpose | Fail-closed consequence | First-wave priority |
|---|---|---|---|
| `SourceDescriptor` | Declare the governed intake contract for a source family, endpoint, archive, or acquisition pattern | No governed admission; reject, hold, or quarantine | Wave 01.5 |
| `IngestReceipt` | Prove what was fetched, when, from where, and with what integrity result | Hold or quarantine; replay cannot be trusted | Later / adjacent |
| `ValidationReport` | Record structural, spatial, temporal, unit, and policy-adjacent checks | Return to quarantine or block canonical write | Later / adjacent |
| `DatasetVersion` | Carry an authoritative candidate or promoted subject set | No authoritative write; remain in governed processing | Wave 01.5 |
| `CatalogClosure` | Publish outward discoverability, lineage, and rights/review closure | No releasable scope | Later / adjacent |
| `DecisionEnvelope` | Express a machine-readable policy result | Deny, hold, generalize, or require review instead of publishing by convenience | Wave 01 |
| `ReviewRecord` | Capture human approval, denial, escalation, or note | Require second review or no publication | Later / adjacent |
| `ReleaseManifest` | Assemble the public-safe release inventory and promotion metadata | Deployment cannot stand in for release | Wave 01 |
| `ReleaseProofPack` | Bundle proof that a release is publishable | Release remains candidate or blocked | Later / adjacent |
| `ProjectionBuildReceipt` | Prove a derived tile, export, search, graph, or scene artifact came from a known release | Block, rebuild, mark stale-visible, or withdraw output | Later / adjacent |
| `EvidenceBundle` | Package inspectable support for a claim, feature, story node, export preview, or answer | `ABSTAIN`, `DENY`, or `ERROR` rather than bluffing | Wave 01 |
| `RuntimeResponseEnvelope` | Make runtime outcomes accountable and finite | No uncited answer; no silent fifth outcome | Wave 01 |
| `CorrectionNotice` | Preserve visible lineage under rollback, supersession, withdrawal, narrowing, or corrected republication | No silent overwrite or invisible narrowing | Wave 01 |

### First schema wave and fixture plan

| Wave | Proposed path | Why it lands early |
|---|---|---|
| Wave 01 | `contracts/v1/common/header_profile.schema.json` | Shared minimum grammar makes later families more coherent |
| Wave 01 | `contracts/v1/policy/decision_envelope.schema.json` | Turns deny-by-default policy into machine-readable structure |
| Wave 01 | `contracts/v1/evidence/evidence_bundle.schema.json` | Makes evidence drill-through explicit and reusable |
| Wave 01 | `contracts/v1/runtime/runtime_response_envelope.schema.json` | Enforces finite runtime outcomes and cite-or-abstain |
| Wave 01 | `contracts/v1/correction/correction_notice.schema.json` | Prevents silent overwrite and anchors correction lineage |
| Wave 01 | `contracts/v1/release/release_manifest.schema.json` | Keeps publication as a governed state transition |
| Wave 01.5 | `contracts/v1/source/source_descriptor.schema.json` | Starts making source admission contract-governed |
| Wave 01.5 | `contracts/v1/data/dataset_version.schema.json` | Begins anchoring canonical truth and stable version identity |
| Companion | `tests/fixtures/contracts/v1/valid/*` | Proves happy-path structure intentionally |
| Companion | `tests/fixtures/contracts/v1/invalid/*` | Proves fail-closed rejection intentionally |
| Companion | `contracts/vocab/reason_codes.json` | Stabilizes decision grammar |
| Companion | `contracts/vocab/obligation_codes.json` | Stabilizes obligations without free-text drift |
| Companion | `contracts/vocab/reviewer_roles.json` | Stabilizes review vocabulary and separation-of-duty semantics |

### Route-family touchpoints that contracts must support

| Route family | Primary objects | Visible fail-closed behavior |
|---|---|---|
| Catalog / discovery | `CatalogClosure`, `ReleaseManifest` | restricted preview, empty result with reason, or `ERROR`; never leak unpublished scope |
| Map / tile / vector delivery | `ReleaseManifest`, `ProjectionBuildReceipt` | `404/410`, stale-visible state, or `ERROR`; never synthesize truth from cache alone |
| Dossier / story / Focus read surfaces | `EvidenceBundle`, `RuntimeResponseEnvelope`, `ReleaseManifest` | `ABSTAIN`, `DENY`, or `ERROR` with visible reason blocks; no detached chat fallback |
| Evidence resolution | `EvidenceBundle`, `DecisionEnvelope`, `ReviewRecord` | deny, generalize, or error rather than leak hidden items or unfiltered citations |
| Correction lineage lookup | `CorrectionNotice`, `ReleaseManifest`, `ProjectionBuildReceipt`, `RuntimeResponseEnvelope` | superseded / withdrawn / correction-pending state; never silently replace history |
| Release / proof inspection | `ReleaseManifest`, `ReleaseProofPack`, `ProjectionBuildReceipt` | no publication or restricted proof summary when release is absent, candidate-only, or withdrawn |
| Review / steward workflows | `ReviewRecord`, `DecisionEnvelope`, `CatalogClosure`, `ReleaseManifest` | hold or require second review; no silent administrative bypass |

[Back to top](#contracts)

## Task list & definition of done

### First enforceable slice

- [ ] One ADR declares the single authoritative schema home.
- [ ] Wave 01 contract files exist as real machine-readable artifacts.
- [ ] `reason_codes.json`, `obligation_codes.json`, and `reviewer_roles.json` exist if this directory owns shared vocab.
- [ ] Each Wave 01 contract has at least one valid and one invalid fixture.
- [ ] A deterministic validator command exists and is documented.
- [ ] One merge-blocking workflow gate runs that validator without skip-risk.
- [ ] `contracts/README.md` and `schemas/README.md` no longer imply competing authority.
- [ ] Runtime contracts prove finite outcomes and citation requirements.
- [ ] Correction contracts prove visible lineage under supersession or withdrawal.
- [ ] Docs, fixtures, and validator output stay in sync.

### Review gates

- [ ] No new contract silently broadens public-safe scope.
- [ ] No field appears in runtime or review payloads without contract coverage.
- [ ] No free-text-only decision logic is introduced where registries are required.
- [ ] No invalid fixture unexpectedly passes.
- [ ] No valid fixture unexpectedly fails.
- [ ] No change weakens release linkage, correction lineage, or audit reconstruction.
- [ ] No `UNKNOWN` is silently promoted to implementation fact.

[Back to top](#contracts)

## FAQ

### Why does this README talk about both `contracts/` and `schemas/`?

Because current public repo evidence points to both as documentation surfaces. That is useful as a warning signal and dangerous as long-term authority practice. This README keeps the conflict visible instead of pretending it is already resolved.

### Why start with `RuntimeResponseEnvelope` and `CorrectionNotice`?

Because they touch the public trust seam fastest: outward answers must be finite, cited, and accountable, and published meaning must change visibly rather than by silent overwrite.

### Why are invalid fixtures mandatory?

Because KFM is fail-closed by design. A valid fixture proves the happy path; an invalid fixture proves the system rejects bad structure on purpose.

### Why is hydrology mentioned in a contracts README?

Because the corpus repeatedly treats hydrology as the strongest first governed thin slice, and that slice exercises the exact contract chain this directory is supposed to define.

[Back to top](#contracts)

## Appendix

<details>
<summary><strong>Evidence basis, verification backlog, and merge-time fill items</strong></summary>

### Evidence basis used for this README

This README is grounded in three layers that should be read together:

1. **The current public repo surface** describing what public `main` exposes around `contracts/`, `schemas/`, `.github/workflows/`, ownership, and review discipline.
2. **The uploaded current draft** of `contracts/README.md`, which already provided the section order, first-wave contract set, fail-closed posture, and route-family framing.
3. **March 2026 KFM doctrine and repo-grounded synthesis**, which define the contract families, fail-closed semantics, route families, proof objects, hydrology-first sequencing, and correction burden.

Where those layers differ, this README prefers the stronger truth posture:

- current public repo evidence determines what can be stated as visible now,
- uploaded draft content determines what should be preserved and improved in place,
- attached doctrine determines what KFM still needs even when the current tree is thinner.

### Pre-merge verification backlog

Before committing this README as authoritative repo documentation, verify at least:

1. the actual `contracts/` tree in the checked-out branch,
2. whether `schemas/` is being retained, demoted, or removed,
3. whether any real `.schema.json` files already exist under another path,
4. where fixtures actually live,
5. whether policy registries already exist, and under what names,
6. whether `.github/workflows/` now contains a real merge-blocking contracts gate,
7. whether `contracts/v1/` or another layout is the repo’s preferred publication path,
8. commit-time values for `doc_id`, `created`, `updated`, and `policy_label`,
9. whether the checked-out branch wants `experimental` retained as the surface-status label.

### Why this file still prefers a small first wave

The corpus consistently prefers a small, enforceable artifact wave over a large but weakly tested schema universe. That is why this README recommends:

- a single authoritative schema home,
- a minimal Wave 01,
- valid and invalid fixtures,
- a deterministic validator command,
- one merge-blocking workflow,
- and one correction drill.

That sequence makes the trust doctrine executable without pretending the whole platform is already mounted.

</details>

[Back to top](#contracts)
