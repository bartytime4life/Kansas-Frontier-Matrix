<!-- [KFM_META_BLOCK_V2] doc_id: kfm://doc/TODO title: Ingest Receipt Contract type: standard version: v1 status: draft owners: TODO created: TODO updated: TODO policy_label: public related: [contracts/README.md, contracts/source/source_descriptor.md, schemas/contracts/v1/source/ingest_receipt.schema.json, data/receipts/README.md, data/receipts/ingest/README.md, policy/README.md, tools/validators/README.md] tags: [kfm, contracts, source, ingest, receipts] notes: [draft contract; companion schema, fixtures, validator, and policy checks still required] [/KFM_META_BLOCK_V2] -->

# Ingest Receipt Contract

One-line purpose: define the human-readable contract for KFM source-ingest receipts so every source-edge landing, skip, denial, quarantine, or error can be reconstructed without turning the receipt into source truth, release proof, or policy authority.

![status](https://img.shields.io/badge/status-draft-lightgrey)
![lane](https://img.shields.io/badge/lane-source--contracts-5319e7)
![object](https://img.shields.io/badge/object-IngestReceipt-0a60ff)
![posture](https://img.shields.io/badge/posture-receipt--not--proof-ffb000)
![schema](https://img.shields.io/badge/schema-companion--required-b60205)

> [!IMPORTANT]
> An `IngestReceipt` is process memory for a specific source-edge ingest event.
> It records what was attempted, what was observed, what landed or did not land, what policy-sensitive posture was known, and what handoff happened next.
>
> It is not a `SourceDescriptor`, not a raw archive, not an `EvidenceBundle`, not a `ValidationReport`, not a `ReleaseManifest`, and not publication proof.

---

## Quick jumps

- [Authority statement](#authority-statement)
- [Repo fit](#repo-fit)
- [Lifecycle position](#lifecycle-position)
- [Accepted inputs](#accepted-inputs)
- [Exclusions](#exclusions)
- [Receipt outcomes](#receipt-outcomes)
- [Required field groups](#required-field-groups)
- [Identity and hashing](#identity-and-hashing)
- [Sensitivity and redaction rules](#sensitivity-and-redaction-rules)
- [Minimal example](#minimal-example)
- [Validation expectations](#validation-expectations)
- [Compatibility and versioning](#compatibility-and-versioning)
- [Task list and definition of done](#task-list-and-definition-of-done)

---

## Authority statement

`contracts/source/ingest_receipt.md` is authoritative for the meaning, lifecycle role, required linkages, compatibility expectations, and review obligations of the `IngestReceipt` object family.

It does **not** own machine shape, emitted receipt storage, policy decisions, connector implementation, workflow orchestration, or release approval.

| Surface | Owns | Must not silently own |
|---|---|---|
| `contracts/source/ingest_receipt.md` | object meaning, field intent, lifecycle role, compatibility posture | JSON Schema enforcement, emitted receipt instances, policy decisions |
| `schemas/contracts/v1/source/ingest_receipt.schema.json` | machine-checkable shape | source authority, source rights, publication approval |
| `data/receipts/ingest/` | emitted ingest receipt instances, if this storage path is accepted | contract meaning, raw data, release proof |
| `data/raw/` | immutable source-native captures or capture manifests | contract definitions or policy decisions |
| `data/quarantine/` | held source material or candidate artifacts blocked by rights, sensitivity, validation, or uncertainty | public release or proof of truth |
| `policy/` | allow, deny, restrict, abstain, obligation, and publication-admissibility logic | schema definitions or emitted data storage |
| `tools/validators/` and `tests/` | executable checks and fixtures | semantic authority or release approval |

> [!WARNING]
> If an ingest receipt begins to act like a release proof, raw archive, source descriptor, policy decision, or EvidenceBundle, the boundary has slipped.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `contracts/source/ingest_receipt.md` |
| Object family | `IngestReceipt` |
| Authority class | human-readable contract |
| Storage target for emitted instances | `data/receipts/ingest/` or repo-accepted equivalent |
| Machine schema companion | `schemas/contracts/v1/source/ingest_receipt.schema.json` |
| Fixture companion | `schemas/tests/fixtures/source/ingest_receipt/` or repo-accepted equivalent |
| Validator companion | `tools/validators/` or repo-accepted equivalent |
| Policy adjacency | source-intake, rights, sensitivity, network, quarantine, and publication gates |
| Current maturity | draft contract; implementation and enforcement require verification |

---

## Lifecycle position

An ingest receipt belongs at the seam between source admission and lifecycle landing.

```mermaid
flowchart LR
    SD[SourceDescriptor / registry entry] --> PRE[Preflight and policy check]
    PRE --> ATTEMPT[Ingest attempt]
    ATTEMPT --> REC[IngestReceipt]
    ATTEMPT --> RAW[RAW capture or raw manifest]
    ATTEMPT --> QUAR[QUARANTINE hold]
    ATTEMPT --> SKIP[Skipped unchanged]
    ATTEMPT --> DENY[Denied before landing]
    ATTEMPT --> ERR[Error]

    REC -. links .-> SD
    REC -. links .-> RAW
    REC -. links .-> QUAR
    REC -. links .-> WORK[WORK handoff]
    REC -. supports .-> VAL[ValidationReport]
    VAL --> PROC[PROCESSED candidate]
    PROC --> CAT[CATALOG / TRIPLET]
    CAT --> REL[Release decision]

    REC -. must not replace .-> CAT
    REC -. must not replace .-> REL
