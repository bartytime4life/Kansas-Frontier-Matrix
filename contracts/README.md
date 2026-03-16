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
notes: [PDF corpus only in current session; repo tree, owners, dates, adjacent paths, and related links require direct verification before commit.]
[/KFM_META_BLOCK_V2] -->

# Contracts

Machine-readable contract backbone for KFM source intake, publication, runtime trust, and correction objects.

> [!IMPORTANT]
> **Status:** `<TODO: verify experimental|active|stable|deprecated>` · **Doc status:** `draft`  
> **Owners:** `<TODO: verify owners / CODEOWNERS>`  
> **Path:** `contracts/README.md`  
> ![doc status](https://img.shields.io/badge/doc%20status-draft-orange) ![scope](https://img.shields.io/badge/scope-contracts-blue) ![truth](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20PROPOSED%20%7C%20UNKNOWN-lightgrey) ![workspace](https://img.shields.io/badge/workspace-PDF%20corpus%20only-critical)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

> [!WARNING]
> This README is grounded in the mounted March 2026 KFM PDF corpus, not in a directly mounted repository checkout. `contracts/README.md` is the requested target path, but adjacent repo paths, existing schemas, tests, ownership markers, and CI entrypoints remain **NEEDS VERIFICATION** until the actual repo tree is inspected.

## Scope

`contracts/` is the contract home for KFM’s typed, machine-validatable object layer: schemas, valid examples, invalid examples, and standards-profile artifacts that make doctrine executable rather than merely descriptive.

In KFM terms, this directory exists so source onboarding, evidence movement, release assembly, runtime trust, and visible correction all speak the same object grammar. The mounted corpus is consistent on the core requirement: contracts are part of trust, not a secondary convenience. They should support fail-closed behavior, stable join keys, explicit time carriage, and lineage-preserving correction.

### Truth posture used in this README

| Label | Used for here |
| --- | --- |
| **CONFIRMED** | Contract families, need for machine-readable schemas, valid and invalid fixtures, stable join keys, reason/obligation registries, and standards-profile pinning as corpus-supported requirements or recommendations |
| **PROPOSED** | Starter directory tree, adjacent repo paths beyond the target file, example validator commands, and the exact first-wave publication order where the mounted corpus stops at design guidance |
| **UNKNOWN / NEEDS VERIFICATION** | Mounted repo layout, existing schema inventory, CODEOWNERS, current CI jobs, local validator entrypoints, and whether any of the proposed paths already exist |

## Repo fit

| Item | Value |
| --- | --- |
| Path | `contracts/README.md` |
| Directory role | Machine-readable contract layer for KFM artifact families |
| Upstream inputs | [Accepted inputs](#accepted-inputs): contract-family definitions, standards pins, valid/invalid specimens, and lifecycle/state obligations |
| Downstream consumers | Policy bundles, API descriptions, event schemas, fixtures, tests, runbooks, observability joins, and governed runtime trust surfaces |
| Adjacent repo paths | **PROPOSED / NEEDS VERIFICATION:** `policy/`, `apis/public/`, `apis/internal/`, `events/schemas/`, `fixtures/`, `tests/contracts/`, `tests/policy/`, `tests/e2e/`, `docs/runbooks/`, `docs/adr/`, `observability/`, `deployment/` |

## Accepted inputs

The following belong in `contracts/`:

- JSON Schema files for contract families
- valid example instances used by docs and tests
- invalid example instances used to prove fail-closed behavior
- standards-profile artifacts or pins that affect contract publication and validation
- concise contract-local notes that explain required fields, join keys, lifecycle states, and correction behavior

### Minimum bar for anything added here

- It is versioned.
- It is machine-validatable.
- It has at least one valid example.
- It has at least one invalid example.
- Required fields are explicit.
- Time basis, join keys, and lineage hooks are explicit.
- Negative states are first-class rather than implied away.

## Exclusions

The following do **not** belong in `contracts/` and should live elsewhere:

| Does **not** belong here | Goes instead | Why |
| --- | --- | --- |
| versioned publication/runtime policy bundles | `policy/bundles/` | Policy should stay executable and reviewable, not hidden in schema prose |
| reason, obligation, and reviewer-role registries | `policy/reason_codes.json`, `policy/obligation_codes.json`, `policy/reviewer_roles.json` | Prevents free-text drift in policy-significant decisions |
| public read-surface API descriptions | `apis/public/` | Route contracts are adjacent to object contracts, not the same thing |
| internal review/policy/runtime API descriptions | `apis/internal/` | Keeps internal surfaces typed without collapsing them into object schemas |
| lifecycle/state transition event grammar | `events/schemas/` | Events are their own contract family |
| bounded thin-slice packages and correction drills | `fixtures/thin_slice/`, `fixtures/correction_drills/` | Keeps end-to-end proof material distinct from reusable contract specimens |
| schema, policy, and e2e tests | `tests/contracts/`, `tests/policy/`, `tests/e2e/` | Execution belongs in tests, not in the source-of-truth contract directory |
| runbooks and ADRs | `docs/runbooks/`, `docs/adr/` | Narrative operational guidance should not replace machine-readable contracts |
| telemetry join-key docs and alert contracts | `observability/` | Observability is adjacent evidence, not the schema definition layer |
| deployment manifests and rollout notes | `deployment/` | Deployment posture should remain reviewable without hiding contract sources |

> [!NOTE]
> The path names above are corpus-grounded starter paths, not confirmed mounted repo paths.

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

### 1) Validate a happy-path example

```bash
# Illustrative only — verify the repo's actual Python environment and validator entrypoint.
python -m jsonschema \
  -i contracts/examples/valid/source_descriptor.min.json \
  contracts/schemas/source_descriptor.schema.json
```

### 2) Prove that an invalid fixture fails

```bash
# Illustrative only — replace <failing-specimen>.json with a real failing fixture from the repo.
python -m jsonschema \
  -i contracts/examples/invalid/<failing-specimen>.json \
  contracts/schemas/source_descriptor.schema.json
```

### 3) Keep standards pins explicit

If a contract depends on a new external profile or version pin, update `contracts/profiles/standards_profile.yaml` instead of leaving the assumption implicit.

### 4) Run the repo-local contract gate

```bash
# Pseudocode — verify the real entrypoint once the repo tree is mounted.
<contract-test-command>
```

### Illustrative minimal schema skeleton

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "kfm://schema/runtime_response_envelope/v1",
  "title": "runtime_response_envelope",
  "type": "object",
  "required": [
    "schema_version",
    "object_type",
    "audit_ref",
    "request_id",
    "evaluated_at",
    "surface_class",
    "surface_state",
    "result"
  ]
}
```

> [!TIP]
> The mounted corpus is explicit that the value is not the literal filename or URI syntax by itself. The value is making the contract explicit enough to validate, diff, test, and review.

## Usage

### Adding a new contract family

1. Add it only if it governs a real lifecycle or trust boundary.
2. Create the schema in `contracts/schemas/`.
3. Add one valid example in `contracts/examples/valid/`.
4. Add one invalid example in `contracts/examples/invalid/`.
5. Record any new standards pin in `contracts/profiles/standards_profile.yaml`.
6. Wire or update contract tests.
7. Confirm join keys, clock fields, lifecycle state, and correction behavior are explicit.
8. Update adjacent docs or runbooks if operator behavior changes.

### Changing an existing contract

Use the smallest compatible change that preserves reviewability:

- add fields before renaming fields
- prefer versioned expansion over silent semantic drift
- keep correction and supersession traceable
- do not bury decision logic in free-text comments or UI-only conditionals
- do not let examples drift from schemas
- do not let derived-layer convenience rewrite authoritative object meaning

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

### Contract family starter map

| Contract family | Operational role | First schema file | First valid example | Must exist before |
| --- | --- | --- | --- | --- |
| `source_descriptor` | source access contract | `schemas/source_descriptor.schema.json` | `examples/valid/source_descriptor.min.json` | governed ingestion |
| `ingest_receipt` | acquisition attempt memory | `schemas/ingest_receipt.schema.json` | `examples/valid/ingest_receipt.min.json` | replayable intake |
| `validation_report` | structural, spatial, temporal, and policy QA | `schemas/validation_report.schema.json` | `examples/valid/validation_report.quarantine.json` | canonical write or quarantine |
| `dataset_version` | immutable candidate or released subject set | `schemas/dataset_version.schema.json` | `examples/valid/dataset_version.min.json` | catalog closure |
| `catalog_closure` | outward DCAT + STAC + PROV closure | `schemas/catalog_closure.schema.json` | `examples/valid/catalog_closure.min.json` | release assembly |
| `decision_envelope` | machine-readable policy outcome | `schemas/decision_envelope.schema.json` | `examples/valid/decision_envelope.allow_with_obligations.json` | promotion or runtime admissibility |
| `review_record` | independent approval memory | `schemas/review_record.schema.json` | `examples/valid/review_record.min.json` | policy-significant transition |
| `release_manifest` | one governed release object | `schemas/release_manifest.schema.json` | `examples/valid/release_manifest.min.json` | public or restricted publication |
| `projection_build_receipt` | proof that a derivative came from a release | `schemas/projection_build_receipt.schema.json` | `examples/valid/projection_build_receipt.min.json` | derived visibility |
| `evidence_bundle` | human-inspectable trust object | `schemas/evidence_bundle.schema.json` | `examples/valid/evidence_bundle.min.json` | claim, feature, story, export preview, or answer support |
| `runtime_response_envelope` | request-time accountability | `schemas/runtime_response_envelope.schema.json` | `examples/valid/runtime_response_envelope.answer.json` | governed runtime |
| `correction_notice` | lineage-preserving post-publication change | `schemas/correction_notice.schema.json` | `examples/valid/correction_notice.supersede.json` | visible correction workflow |

> [!NOTE]
> The mounted corpus often treats the release family as `release_manifest / release_proof_pack`. This README keeps `release_manifest.schema.json` as the starter file because that is the repeatedly named first-wave schema entry.

<details>
<summary><strong>Minimum semantic burden by contract family</strong></summary>

| Contract family | Must include at least |
| --- | --- |
| `source_descriptor` | identity; owner or steward; access mode; rights posture; support; cadence; validation plan; publication intent |
| `ingest_receipt` | source reference; fetch time; integrity checks; result; output pointers |
| `validation_report` | checklist; severity; reason codes; subject refs |
| `dataset_version` | stable ID; version ID; support; time semantics; provenance links |
| `catalog_closure` | STAC/DCAT/PROV refs; identifiers; release linkage; outward profile refs |
| `decision_envelope` | subject; action; lane; result; reason codes; obligation codes; policy basis; `audit_ref`; effective window |
| `review_record` | reviewer role; decision; timestamp; refs; comments |
| `release_manifest` | version refs; catalog refs; decision refs; docs/accessibility gate; rollback/correction posture; profile versions; bundle plan |
| `projection_build_receipt` | release ref; projection type; surface class; build time; freshness basis; stale-after policy |
| `evidence_bundle` | bundle ID; source basis; dataset refs; lineage summary; preview policy; transform receipts; rights/sensitivity state; `audit_ref` |
| `runtime_response_envelope` | schema version; object type; `audit_ref`; `request_id`; evaluated-at time; surface class; surface state; result; citations check; decision ref |
| `correction_notice` | affected releases; replacement releases; affected surface classes; rebuild refs; cause; public note |

</details>

### Corpus-supported standards publication profile

| Concern | Profile to pin explicitly | How it affects `contracts/` |
| --- | --- | --- |
| JSON object schemas | JSON Schema Draft 2020-12 | default basis for machine-readable envelopes, examples, invalid fixtures, and schema-aware docs |
| Public API descriptions | OpenAPI 3.2.0 | adjacent API contract pin; document explicitly even if the files live outside `contracts/` |
| Dataset and release catalogs | DCAT 3 | outward catalog metadata referenced by `catalog_closure` and release artifacts |
| Outward provenance | PROV-O | lineage vocabulary referenced by `catalog_closure`, release evidence, and correction linkage |
| Spatiotemporal collections and assets | STAC core / catalog / collection / item family | outward spatiotemporal description linked from `catalog_closure` |
| Feature read routes | OGC API - Features 1.0/1.0.1 | adjacent standards-aligned route family for authoritative reads |
| Map and tile portrayal | OGC API - Maps 1.0 and OGC API - Tiles 1.0 | adjacent outward portrayal routes; still subordinate to release linkage and surface-state rules |
| Catalog search routes | OGC API - Records 1.0 | optional outward catalog/discovery route where KFM exposes interoperable record search |
| Accessibility baseline | WCAG 2.2 | public trust surfaces that consume contract outputs must remain accessible and state-explicit |
| Release integrity | OCI image-spec 1.1.1 + Sigstore/Cosign | optional artifact packaging, signing, and attestation family when release-integrity evidence is needed |
| Observability semantics | OpenTelemetry semantic conventions | stable core semantic conventions for logs, traces, metrics, and resources; exact adopted categories should be version-pinned |

### Required cross-contract join keys

| Join key | Why it matters |
| --- | --- |
| `release_id` | binds publication state to visible derivatives and runtime scope |
| `dataset_version_id` | ties canonical subject sets to release and correction paths |
| `decision_id` | joins policy outcomes to review, runtime, and correction objects |
| `review_id` | makes separation of duty inspectable |
| `bundle_id` or stable `EvidenceRef` | keeps evidence operational instead of decorative |
| `projection_id` | binds derived layers to release truth and freshness checks |
| `request_id` | distinguishes one governed response from another in runtime traces |
| `audit_ref` | lets runtime, traces, incidents, and support actions converge |
| `notice_id` | preserves correction lineage under supersession or withdrawal |

### Runtime outcomes these contracts must preserve

| Outcome class | Meaning | Typical trust-visible state |
| --- | --- | --- |
| `ANSWER` | admissible published scope resolved with inspectable evidence and audit linkage | normal published state with citations, release scope, and freshness visible |
| `ABSTAIN` | support is partial, missing, stale, or insufficiently scoped | calm failure banner; narrowed scope or evidence-needed guidance |
| `DENY` | policy, rights, sensitivity, or approval state blocks release or response | policy-visible denial state; no silent omission |
| `ERROR` | trustworthy service is currently impossible and cannot safely downgrade to abstain or deny | operational error state with `audit_ref` and correction or rollback path where applicable |

## Task list

### Definition of done for any contract added here

- [ ] schema file exists
- [ ] at least one valid fixture exists
- [ ] at least one invalid fixture exists
- [ ] required fields are explicit
- [ ] time basis is explicit
- [ ] lifecycle state is explicit
- [ ] correction or supersession path is explicit
- [ ] join keys are explicit
- [ ] examples match the current schema
- [ ] policy dependencies are referenced, not buried in prose
- [ ] adjacent tests are updated
- [ ] adjacent docs or runbooks are updated if operator behavior changed

### Review gates

- [ ] no free-text-only decision logic where reason or obligation codes are required
- [ ] no client-visible trust behavior depends on undocumented fields
- [ ] no contract change silently broadens publication, export, or runtime answer scope
- [ ] no invalid fixture now passes unexpectedly
- [ ] no valid fixture now fails unexpectedly
- [ ] no change weakens audit reconstruction or correction lineage
- [ ] no schema, example, or docs drift leaves `contracts/` out of sync with runtime trust surfaces

## FAQ

### Why keep invalid examples?

Because KFM’s verification posture is fail-closed. A happy-path specimen proves almost nothing by itself; an invalid fixture proves that the schema and test harness reject bad structure on purpose.

### Why are policy registries excluded from this directory?

Because the mounted corpus treats reason codes, obligation codes, and reviewer-role maps as executable policy artifacts, not just structural metadata. Keeping them in `policy/` makes them versionable, reviewable, and reusable across release and runtime decisions.

### Why start with a small first schema wave?

Because the corpus repeatedly prefers a modest, high-leverage first wave over contract sprawl: get the highest-trust objects explicit enough to validate, diff, test, and exercise end to end, then grow from a governed thin slice.

### Why are literal endpoint paths absent?

Because the mounted corpus repeatedly shifts emphasis from unverified literal routes toward route classes and trust obligations. This README stays honest about that boundary.

### Why is this README still useful if the repo tree was not mounted?

Because the contract families, schema wave, fixture rules, join keys, and standards-profile expectations converge strongly across the mounted March 2026 KFM doctrine and realization overlays. What remains unverified is path reality, not the contract-layer role.

## Appendix

<details>
<summary><strong>Evidence basis and current-session limits</strong></summary>

This README is grounded primarily in the mounted March 2026 KFM contract, verification, and canonical-manual overlays. The strongest direct inputs for this file were the contract/artifact realization deepening pass, the verification doctrine, the unified governed-delivery doctrine, and the March 14 canonical master-manual passes that repeat the same starter schema wave, valid/invalid fixture requirement, standards-profile pins, route-class discipline, stable join keys, and transition-oriented verification posture.

Current-session constraint:

- the mounted workspace exposed PDF artifacts only
- no repo checkout, `.git` metadata, schema files, example fixtures, CODEOWNERS entries, tests, workflow files, deployment manifests, or runtime logs were directly verified

Interpretation rule:

- treat directory shape outside `contracts/README.md` as a **PROPOSED starter layout**
- ratify owners, dates, policy label, related links, adjacent paths, and local validator entrypoints against the mounted repo before commit

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
