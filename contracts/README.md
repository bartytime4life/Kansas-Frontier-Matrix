<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<TODO-UUID>
title: Contracts
type: standard
version: v1
status: draft
owners: <TODO: verify owners / CODEOWNERS>
created: <TODO: YYYY-MM-DD>
updated: <TODO: YYYY-MM-DD>
policy_label: <TODO: verify public|restricted|internal|...>
related: [<TODO: verify related paths and kfm:// ids>]
tags: [kfm, contracts, schemas, verification]
notes: [Mounted workspace exposed PDFs only; repo tree, adjacent paths, owners, dates, and related links require direct verification before commit.]
[/KFM_META_BLOCK_V2] -->

# Contracts

Machine-readable contract backbone for KFM source intake, publication, runtime trust, and correction objects.

> [!IMPORTANT]
> **Status:** draft  
> **Owners:** `<TODO: verify owners / CODEOWNERS>`  
> ![status](https://img.shields.io/badge/status-draft-orange) ![scope](https://img.shields.io/badge/scope-contracts-blue) ![truth](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20PROPOSED%20%7C%20UNKNOWN-lightgrey) ![repo-state](https://img.shields.io/badge/repo%20state-unmounted%20in%20session-critical)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

> [!WARNING]
> This README is grounded in the mounted March 2026 KFM PDF corpus, not in a directly mounted repository checkout. `contracts/README.md` is the target file for this task, but adjacent repo paths, existing schemas, tests, and ownership markers remain **NEEDS VERIFICATION** until the actual repo tree is inspected.

## Scope

`contracts/` is the contract home for KFM’s typed, machine-validatable object layer: schemas, valid examples, invalid examples, and standards-profile artifacts that make doctrine executable rather than merely descriptive.

In corpus terms, this directory exists to make the following families diffable, reviewable, and testable:

- `source_descriptor`
- `ingest_receipt`
- `validation_report`
- `dataset_version`
- `catalog_closure`
- `decision_envelope`
- `review_record`
- `release_manifest`
- `projection_build_receipt`
- `evidence_bundle`
- `runtime_response_envelope`
- `correction_notice`

These contracts sit on the governed truth path and verification path. They should support fail-closed behavior, explicit lifecycle state, stable join keys, and visible correction without erasure.

[Back to top](#contracts)

## Repo fit

| Item | Value |
| --- | --- |
| Path | `contracts/README.md` |
| Directory role | Machine-readable contract layer for KFM artifact families |
| Upstream inputs | [Accepted inputs](#accepted-inputs): contract family definitions, standards pins, valid/invalid examples, and lifecycle/state obligations |
| Downstream consumers | [Exclusions](#exclusions), [Tables](#tables), and [Task list](#task-list): policy bundles, API descriptions, event schemas, fixtures, tests, runbooks, and runtime trust surfaces |
| Adjacent repo paths | **PROPOSED / NEEDS VERIFICATION:** `policy/`, `apis/`, `events/schemas/`, `fixtures/`, `tests/contracts/`, `tests/policy/`, `tests/e2e/`, `docs/runbooks/`, `observability/` |

**Why this directory exists**

The mounted KFM corpus repeatedly converges on the same rule: verification must be executable. That means schemas, valid and invalid examples, registries, resolvers, proof objects, and test harnesses need a durable home. This directory is that home for the contract layer itself.

## Accepted inputs

The following belong in `contracts/`:

- JSON Schema files for contract families
- valid example instances used by docs and tests
- invalid example instances used to prove fail-closed behavior
- standards/profile pins that affect contract publication and validation
- concise contract-local notes that explain required fields, join keys, and lifecycle/state expectations

### Minimum expectations for anything added here

- It is versioned.
- It is machine-validatable.
- It has at least one valid example.
- It has at least one invalid example.
- It names required fields explicitly.
- It supports traceability across release, runtime, review, and correction paths.

## Exclusions

The following do **not** belong in `contracts/` and should live elsewhere:

| Does **not** belong here | Goes instead | Why |
| --- | --- | --- |
| reason and obligation registries | `policy/` | Policy drift should not be hidden inside schema files |
| publication/runtime policy bundles | `policy/bundles/` | Policy needs its own versioned executable packaging |
| public API descriptions | `apis/public/` | Route contracts are adjacent to, but not the same as, object contracts |
| internal review/policy/runtime API descriptions | `apis/internal/` | Keeps internal surfaces typed without collapsing them into object schemas |
| event grammar for lifecycle/state transitions | `events/schemas/` | Events are a separate contract family |
| thin-slice dataset packages | `fixtures/` or `examples/thin_slice/` | Bounded end-to-end proof material should stay distinct from reusable contract specimens |
| schema/policy/e2e tests | `tests/contracts/`, `tests/policy/`, `tests/e2e/` | Keeps execution concerns separate from the contract source of truth |
| runbooks | `docs/runbooks/` | Docs should describe operational use, not replace typed contracts |
| telemetry contracts and join-key docs | `observability/` | Observability is adjacent, but not the same as schema definition |

> [!NOTE]
> The path names above are source-grounded **starter paths**, not confirmed mounted repo paths.

## Directory tree

**PROPOSED starter layout grounded in the mounted KFM corpus**

```text
contracts/
├─ README.md
├─ schemas/
│  ├─ source_descriptor.schema.json
│  ├─ ingest_receipt.schema.json
│  ├─ validation_report.schema.json
│  ├─ dataset_version.schema.json
│  ├─ catalog_closure.schema.json
│  ├─ decision_envelope.schema.json
│  ├─ review_record.schema.json
│  ├─ release_manifest.schema.json
│  ├─ projection_build_receipt.schema.json
│  ├─ evidence_bundle.schema.json
│  ├─ runtime_response_envelope.schema.json
│  └─ correction_notice.schema.json
├─ examples/
│  ├─ valid/
│  │  ├─ source_descriptor.min.json
│  │  ├─ ingest_receipt.min.json
│  │  ├─ validation_report.quarantine.json
│  │  ├─ dataset_version.min.json
│  │  ├─ catalog_closure.min.json
│  │  ├─ decision_envelope.allow_with_obligations.json
│  │  ├─ review_record.min.json
│  │  ├─ release_manifest.min.json
│  │  ├─ projection_build_receipt.min.json
│  │  ├─ evidence_bundle.min.json
│  │  ├─ runtime_response_envelope.answer.json
│  │  └─ correction_notice.supersede.json
│  └─ invalid/
│     └─ <at least one failing specimen per contract family>
└─ profiles/
   └─ standards_profile.yaml
```

## Quickstart

### 1) Add or update a contract schema

```bash
# Example only — adapt to the repo's actual validator and Python environment.
python -m jsonschema \
  -i contracts/examples/valid/source_descriptor.min.json \
  contracts/schemas/source_descriptor.schema.json
```

### 2) Prove that invalid fixtures fail

```bash
# Example only — failure is the expected result here.
python -m jsonschema \
  -i contracts/examples/invalid/source_descriptor.missing_dataset_id.json \
  contracts/schemas/source_descriptor.schema.json
```

### 3) Run the repo-local validation entrypoint

```bash
# Pseudocode — NEEDS VERIFICATION against the actual repo.
make validate-contracts
```

### 4) Keep profile pins explicit

If a contract depends on a new schema/profile pin, update `contracts/profiles/standards_profile.yaml` instead of leaving the assumption implicit.

## Usage

### Adding a new contract family

1. Choose the family only if it crosses a real lifecycle or trust boundary.
2. Add the schema in `contracts/schemas/`.
3. Add one valid example in `contracts/examples/valid/`.
4. Add one invalid example in `contracts/examples/invalid/`.
5. Record any new profile dependency in `contracts/profiles/standards_profile.yaml`.
6. Wire or update contract tests.
7. Confirm join keys, lifecycle state, and correction behavior are explicit.
8. Update adjacent docs and runbooks if operator behavior changes.

### Changing an existing contract

Use the smallest compatible change that preserves reviewability:

- add fields before renaming fields
- prefer versioned expansion over silent semantic drift
- keep correction and supersession traceable
- do not move policy logic into free-text comments or UI-only conditionals
- do not let examples drift from schemas

### Review questions

Before merging a contract change, ask:

- What transition does this contract govern?
- What breaks if this object is malformed?
- Which join keys depend on it?
- Which negative outcome must remain first-class?
- Does it change what the user can see, export, or trust?
- Does it change correction, review, or runtime behavior?

## Diagram

```mermaid
flowchart LR
    SD[source_descriptor] --> IR[ingest_receipt]
    IR --> VR[validation_report]
    VR --> DV[dataset_version]
    DV --> CC[catalog_closure]
    CC --> DE[decision_envelope]
    DE --> RR[review_record]
    RR --> RM[release_manifest]
    RM --> PBR[projection_build_receipt]
    RM --> EB[evidence_bundle]
    EB --> RRE[runtime_response_envelope]
    RM --> CN[correction_notice]

    subgraph contracts["contracts/"]
      S[schemas/]
      V[examples/valid/]
      I[examples/invalid/]
      P[profiles/standards_profile.yaml]
    end

    S -. validates .-> SD
    S -. validates .-> IR
    S -. validates .-> VR
    S -. validates .-> DV
    S -. validates .-> CC
    S -. validates .-> DE
    S -. validates .-> RR
    S -. validates .-> RM
    S -. validates .-> PBR
    S -. validates .-> EB
    S -. validates .-> RRE
    S -. validates .-> CN
    V -. canonical passing specimens .-> S
    I -. negative-path fixtures .-> S
    P -. explicit standards pins .-> S
```

## Tables

### First-wave contract matrix

| Contract family | Operational role | First schema file | First valid example | Must exist before |
| --- | --- | --- | --- | --- |
| `source_descriptor` | source access contract | `schemas/source_descriptor.schema.json` | `examples/valid/source_descriptor.min.json` | governed ingestion |
| `ingest_receipt` | acquisition attempt memory | `schemas/ingest_receipt.schema.json` | `examples/valid/ingest_receipt.min.json` | replayable intake |
| `validation_report` | structural / spatial / temporal / policy QA | `schemas/validation_report.schema.json` | `examples/valid/validation_report.quarantine.json` | canonical write or quarantine |
| `dataset_version` | immutable candidate / released subject set | `schemas/dataset_version.schema.json` | `examples/valid/dataset_version.min.json` | catalog closure |
| `catalog_closure` | DCAT + STAC + PROV closure | `schemas/catalog_closure.schema.json` | `examples/valid/catalog_closure.min.json` | release assembly |
| `decision_envelope` | machine-readable policy outcome | `schemas/decision_envelope.schema.json` | `examples/valid/decision_envelope.allow_with_obligations.json` | promotion or runtime admissibility |
| `review_record` | independent approval memory | `schemas/review_record.schema.json` | `examples/valid/review_record.min.json` | policy-significant transition |
| `release_manifest` | one governed release object | `schemas/release_manifest.schema.json` | `examples/valid/release_manifest.min.json` | public or restricted publication |
| `projection_build_receipt` | proof that a derivative came from a release | `schemas/projection_build_receipt.schema.json` | `examples/valid/projection_build_receipt.min.json` | derived visibility |
| `evidence_bundle` | human-inspectable trust object | `schemas/evidence_bundle.schema.json` | `examples/valid/evidence_bundle.min.json` | claim, feature, story, or answer support |
| `runtime_response_envelope` | request-time accountability | `schemas/runtime_response_envelope.schema.json` | `examples/valid/runtime_response_envelope.answer.json` | governed runtime |
| `correction_notice` | lineage-preserving post-publication change | `schemas/correction_notice.schema.json` | `examples/valid/correction_notice.supersede.json` | visible correction workflow |

### Profile pins that affect this directory

| Profile area | Current baseline in corpus | Why this matters here |
| --- | --- | --- |
| JSON Schema | Draft 2020-12 | default `$schema` base for machine-validated object files |
| OpenAPI | 3.2.0 | adjacent route/publication contract pin; kept outside `contracts/`, but referenced by the overall standards profile |
| DCAT 3 | active profile | catalog-facing portion of `catalog_closure` |
| STAC | active profile | spatiotemporal asset/catalog portion of `catalog_closure` |
| PROV-O / PROV | active profile | lineage/provenance portion of `catalog_closure`, release evidence, and bundle linkage |
| WCAG 2.2 | active accessibility baseline | trust-visible surfaces consuming contract outputs should not hide state or evidence cues |
| OpenTelemetry semconv | explicit pin recommended | join keys and audit reconstruction need stable naming if surfaced into contract-adjacent docs |

### Required cross-contract join keys

| Join key | Why it matters |
| --- | --- |
| `release_id` | binds publication state to visible derivatives and runtime scope |
| `dataset_version_id` | ties canonical subject sets to release and correction paths |
| `decision_id` | joins policy outcomes to review, runtime, and correction objects |
| `review_id` | makes separation of duty inspectable |
| `bundle_id` or stable evidence ref | keeps evidence operational instead of decorative |
| `projection_id` | binds derived layers to release truth and freshness checks |
| `audit_ref` | lets runtime, traces, incidents, and support actions converge |

## Task list

### Definition of done for any contract added here

- [ ] schema file exists
- [ ] at least one valid fixture exists
- [ ] at least one invalid fixture exists
- [ ] required fields are explicit
- [ ] lifecycle state is explicit
- [ ] correction/supersession path is explicit
- [ ] join keys are explicit
- [ ] examples match current schema
- [ ] policy dependencies are referenced, not buried in prose
- [ ] adjacent tests are updated
- [ ] adjacent docs/runbooks are updated if operator behavior changed

### Review gates

- [ ] no free-text-only decision logic where codes or enums are required
- [ ] no client-visible trust behavior depends on undocumented fields
- [ ] no contract change silently broadens publication, export, or runtime answer scope
- [ ] no invalid fixture now passes unexpectedly
- [ ] no valid fixture now fails unexpectedly
- [ ] no change weakens audit reconstruction or correction lineage

## FAQ

### Why keep invalid examples?

Because KFM’s verification posture is fail-closed. A passing happy-path example proves almost nothing by itself; an invalid fixture proves that the schema and test harness reject bad structure on purpose.

### Why are reason and obligation registries excluded from this directory?

Because they are policy artifacts, not merely structural artifacts. The corpus treats them as executable review/runtime logic that should remain versioned and auditable in `policy/`, not buried in object schemas.

### Why are literal endpoint paths absent?

Because the mounted corpus repeatedly prefers **route classes** over unverified literal paths. This README stays honest about that boundary.

### Why is this README still useful if the repo tree was not mounted?

Because the contract families, starter layout, and verification expectations are strongly convergent across the mounted KFM doctrine and realization overlays. What remains unverified is path reality, not the contract-layer role.

## Appendix

<details>
<summary><strong>Evidence basis and current-session limits</strong></summary>

This README was grounded primarily in the mounted March 2026 KFM corpus, especially the contract/artifact realization deepening pass, the verification doctrine, the canonical master-reference packages, the governed delivery doctrine, and the phase-one runtime note.

Directly grounded points used here include:

- the first-wave contract families
- the proposed `contracts/schemas/`, `contracts/examples/valid/`, and `contracts/examples/invalid/` layout
- the standards-profile artifact under `contracts/profiles/`
- the separation of contracts from policy bundles, OpenAPI descriptions, event contracts, fixtures, tests, and runbooks
- the requirement for valid and invalid fixtures
- the use of stable join keys such as `release_id`, `dataset_version_id`, `decision_id`, `review_id`, `bundle_id`, `projection_id`, and `audit_ref`

Current-session constraint:

- the mounted workspace exposed PDFs only
- no repo tree, existing `contracts/` directory, schemas, tests, workflow files, manifests, or CODEOWNERS entries were directly verified

Interpretation rule:

- treat directory shape outside `contracts/README.md` as **PROPOSED starter layout**
- ratify relative paths, owners, dates, policy label, and related links against the mounted repo before commit

</details>

<details>
<summary><strong>Likely next files after this README</strong></summary>

High-leverage next artifacts, in order:

1. `contracts/schemas/source_descriptor.schema.json`
2. `contracts/schemas/dataset_version.schema.json`
3. `contracts/schemas/decision_envelope.schema.json`
4. `contracts/schemas/release_manifest.schema.json`
5. `contracts/schemas/evidence_bundle.schema.json`
6. `contracts/schemas/runtime_response_envelope.schema.json`
7. `contracts/schemas/correction_notice.schema.json`
8. one valid and one invalid specimen per contract family
9. `contracts/profiles/standards_profile.yaml`

</details>

[Back to top](#contracts)