<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<UUID_NEEDS_VERIFICATION>
title: Contracts
type: standard
version: v1
status: draft
owners: <OWNER_NEEDS_VERIFICATION>
created: <DATE_NEEDS_VERIFICATION>
updated: <DATE_NEEDS_VERIFICATION>
policy_label: <POLICY_LABEL_NEEDS_VERIFICATION>
related: [<RELATED_PATHS_NEEDS_VERIFICATION>]
tags: [kfm, contracts, schemas, proof-objects]
notes: [Root contracts lane aligned to the user-requested path and doctrinal starter paths; owners, dates, and exact mounted inventory need verification]
[/KFM_META_BLOCK_V2] -->

# Contracts

Machine-checkable contract lane for KFM’s shared schemas, proof objects, and contract-first release rules.

> **Status:** experimental  
> **Owners:** `<OWNER_NEEDS_VERIFICATION>`  
> ![Status: experimental](https://img.shields.io/badge/status-experimental-ffb000) ![Contracts: starter wave](https://img.shields.io/badge/contracts-starter_wave-5319e7) ![Evidence: PDF grounded](https://img.shields.io/badge/evidence-pdf--grounded-0a60ff) ![Proof quartet: required](https://img.shields.io/badge/proof_quartet-required-2ea44f) ![Schema profile: JSON Schema 2020-12](https://img.shields.io/badge/json_schema-2020--12-6e7781)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Quickstart](#quickstart) · [Diagram](#diagram) · [Starter schema wave](#starter-schema-wave) · [Versioning rules](#versioning-rules) · [Validation and gates](#validation-and-gates) · [FAQ](#faq)

> [!IMPORTANT]
> This directory should function as KFM’s **canonical contract lane**: the place where recurring proof objects become explicit enough to validate, diff, test, and govern.

> [!WARNING]
> Current-session evidence for this task was **PDF-rich only**. Treat exact mounted file inventory under `contracts/` as **NEEDS VERIFICATION** unless a path is explicitly listed below as a documented starter path or is directly surfaced in the repository.

## Scope

KFM’s doctrine is already strong. What this lane adds is **artifactization**: contracts that stop critical behavior from remaining prose-only.

This directory exists to make KFM’s recurring proof objects:

- machine-checkable
- versionable
- fixture-testable
- policy-gateable
- reviewable in the same stream as the code and docs they affect

### Why contracts first

Contracts matter here for three reasons:

1. They keep doctrine from dissolving into free-text interpretation.
2. They make proof objects testable before promotion.
3. They give runtime trust surfaces stable payloads instead of improvised JSON.

### Status vocabulary used here

| Label | Meaning in this README |
| --- | --- |
| **CONFIRMED** | Directly supported by the attached KFM manuals or attached repo-native Markdown examples |
| **INFERRED** | Small structural completion that fits the stronger source base but is not directly surfaced as mounted repo fact |
| **PROPOSED** | Recommended starter rule, file shape, or subtree convention |
| **UNKNOWN** | Not verified strongly enough in the current session |
| **NEEDS VERIFICATION** | Review flag for ownership, dates, exact inventory, or mounted enforcement |

## Repo fit

| Path | Role | Relationship |
| --- | --- | --- |
| `contracts/README.md` | contracts subtree hub | this file |
| [`../README.md`](../README.md) | repository/root orientation | upstream context for project identity and navigation (**NEEDS VERIFICATION**) |
| `./source/` | source-intake contract lane | **PROPOSED** starter subtree |
| `./core/` | authoritative core object lane | **PROPOSED** starter subtree |
| `./policy/` | policy-result and decision-object lane | **PROPOSED** starter subtree |
| `./release/` | release-bearing contract lane | **PROPOSED** starter subtree |
| `./runtime/` | runtime trust-object lane | **PROPOSED** starter subtree |
| `./correction/` | correction and supersession lane | **PROPOSED** starter subtree |
| `./profiles/` | standards-profile and compatibility lane | **PROPOSED** starter subtree |

## Accepted inputs

Place material here when its primary job is to define **shape, semantics, or compatibility** for a governed object:

- JSON Schema or equivalent contract definitions for KFM object families
- typed-model exports when the repo treats generated JSON Schema as the publishable contract surface
- standards-profile files that pin external vocabularies or compatibility decisions
- contract-local notes about required fields, compatibility, and migration behavior
- valid and invalid examples only when they are used to test the contract itself

## Exclusions

Do **not** place the following here:

- free-form policy bundles, reason-code governance, or reviewer-role registries when they are owned by the policy lane
- lane-specific research notes, spikes, or design ideation
- emitted runtime instances from actual runs such as concrete `run_receipt.json`, `release_manifest.json`, or `correction_notice.json` files
- domain-facing docs, runbooks, or shell behavior notes unless they are explaining a contract boundary
- ad hoc examples that bypass the schema, fixtures, or validation path

## Directory tree

```text
contracts/
├── README.md
├── source/       # PROPOSED starter lane
├── core/         # PROPOSED starter lane
├── policy/       # PROPOSED starter lane
├── release/      # PROPOSED starter lane
├── runtime/      # PROPOSED starter lane
├── correction/   # PROPOSED starter lane
└── profiles/     # PROPOSED starter lane
```

> [!NOTE]
> The tree above is a **starter routing shape**, not a claim that every directory already exists in the mounted repo.

## Quickstart

### Add a new schema

1. Choose the nearest contract family before naming files.
2. Place the schema in the narrowest matching lane under `contracts/`.
3. Add at least one valid and one invalid fixture.
4. Record compatibility impact: breaking, non-breaking, or **NEEDS VERIFICATION**.
5. Wire or update schema tests and policy gates before merge.
6. Update this README if the subtree shape or family map changes.

### Minimal starter shape

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "kfm://contracts/source/source_descriptor.schema.json",
  "title": "SourceDescriptor",
  "type": "object",
  "required": [
    "source_id",
    "owner",
    "access_mode",
    "rights_posture",
    "cadence",
    "validation_plan",
    "publication_intent"
  ],
  "properties": {
    "source_id": { "type": "string" },
    "owner": { "type": "string" },
    "access_mode": { "type": "string" },
    "rights_posture": { "type": "string" },
    "cadence": { "type": "string" },
    "validation_plan": { "type": "string" },
    "publication_intent": { "type": "string" }
  },
  "additionalProperties": false
}
```

> [!NOTE]
> The example above is an **illustrative starter skeleton**. Use mounted repo conventions if a stronger local template, typed-model source of truth, or naming pattern already exists.

## Usage

### Typed flow pattern

When contracts are backed by typed models, keep every hop explicit and fail-closed.

```python
# illustrative pattern
item = ContractModel.model_validate(payload)   # typed in
out = transform(item)
serialized = out.model_dump()
ContractModel.model_validate(serialized)       # re-validate before write
```

### Where fixtures should help

Use fixtures to prove:

- valid minimum payloads
- invalid required-field failures
- version-compatibility boundaries
- reason/obligation grammar integrity
- runtime negative outcomes where a contract is outward-facing

### When to update this README

Update this file when any of the following changes:

- the verified contract family inventory changes
- a starter path becomes directly confirmed or gets superseded
- the versioning policy becomes repo-local and explicit
- adjacent lanes change routing boundaries
- the proof quartet or release/correction expectations change

## Diagram

```mermaid
flowchart LR
    A[SourceDescriptor] --> B[IngestReceipt]
    B --> C[ValidationReport]
    C --> D[DatasetVersion]
    D --> E[CatalogClosure]
    E --> F[DecisionEnvelope / ReviewRecord]
    F --> G[ReleaseManifest]
    G --> H[ProjectionBuildReceipt]
    G --> I[EvidenceBundle]
    I --> J[RuntimeResponseEnvelope]
    J --> K[ANSWER | ABSTAIN | DENY | ERROR]
    G --> L[CorrectionNotice]
```

## Reference tables

### Contract families

The recurring family below is doctrinally stable enough to document now, even though exact mounted schema coverage remains incomplete.

| Family | Primary job | Must include at least |
| --- | --- | --- |
| `SourceDescriptor` | Declare the intake contract for a source or endpoint | identity, owner/steward, access mode, rights posture, support, cadence, validation plan, publication intent |
| `IngestReceipt` | Prove that a fetch and landing event occurred | source reference, fetch time, integrity checks, result, output pointers |
| `ValidationReport` | Record what checks passed, failed, or quarantined | check list, severity, reason codes, subject refs |
| `DatasetVersion` | Carry an authoritative candidate or promoted subject set | stable ID, version ID, support, time semantics, provenance links |
| `CatalogClosure` | Publish outward metadata closure and lineage linkage | STAC/DCAT/PROV refs, identifiers, release linkage, outward profile refs |
| `DecisionEnvelope` | Express a policy result machine-readably | subject, action, lane, result, reason codes, obligation codes, policy basis, `audit_ref`, effective window |
| `ReviewRecord` | Capture human approval, denial, escalation, or note | reviewer role, decision, timestamp, refs, comments |
| `ReleaseManifest` / `ReleaseProofPack` | Assemble a public-safe release and its proof | version refs, catalog refs, decision refs, docs/accessibility gate, rollback/correction posture, profile versions, bundle plan |
| `ProjectionBuildReceipt` | Prove a derived layer was built from a known release scope | release ref, projection type, surface class, build time, freshness basis, stale-after policy |
| `EvidenceBundle` | Package support for a claim, feature, story, export preview, or answer | bundle ID, source basis, dataset refs, lineage summary, preview policy, transform receipts, rights/sensitivity state, `audit_ref` |
| `RuntimeResponseEnvelope` | Make runtime outcomes accountable | schema version, object type, `audit_ref`, request ID, evaluated-at time, surface class, surface state, result, citation check, decision ref |
| `CorrectionNotice` | Preserve visible lineage under change | affected releases, replacement releases, affected surface classes, rebuild refs, cause, public note |

### Proof quartet

KFM’s minimum machine-checkable proof center is small on purpose.

| Carrier | Why it matters | Minimum expectation |
| --- | --- | --- |
| `spec_hash` | stable identity for an input or spec basis | deterministic and reproducible across reruns |
| `run_receipt` | common audit object for one run | inputs, outputs, timestamps, `spec_hash`, artifact refs, policy/attestation refs |
| `ai_receipt` | model-mediated audit object where AI participates | model/runtime ID, allowed prompt/seed refs, inputs, outputs, policy context, artifact refs |
| attestation refs | integrity and origin verification | verifiable link from contract-bearing artifact to signed proof |

> [!IMPORTANT]
> A change that weakens the proof quartet is not a cosmetic change. It is a trust-surface change.

### Starter schema wave

The corpus names a deliberately small first wave. Family purpose is **CONFIRMED**. Exact mounted file presence still needs direct repo verification.

| Starter filename | Family | Why it belongs in the first wave | Status |
| --- | --- | --- | --- |
| `source/source_descriptor.schema.json` | `SourceDescriptor` | source intake cannot stay implicit | **PROPOSED** starter path |
| `core/dataset_version.schema.json` | `DatasetVersion` | authoritative versioning needs a canonical carrier | **PROPOSED** starter path |
| `policy/decision_envelope.schema.json` | `DecisionEnvelope` | policy results must be machine-readable | **PROPOSED** starter path |
| `release/release_manifest.schema.json` | `ReleaseManifest` | releases need inspectable scope and rollback posture | **PROPOSED** starter path |
| `runtime/evidence_bundle.schema.json` | `EvidenceBundle` | every consequential claim needs resolvable support | **PROPOSED** starter path |
| `runtime/runtime_response_envelope.schema.json` | `RuntimeResponseEnvelope` | runtime outcomes must stay inspectable | **PROPOSED** starter path |
| `correction/correction_notice.schema.json` | `CorrectionNotice` | supersession must remain visible | **PROPOSED** starter path |
| `runtime/run_receipt.schema.json` | `run_receipt` | common run audit carrier | family **CONFIRMED**; lane placement **NEEDS VERIFICATION** |
| `runtime/ai_receipt.schema.json` | `ai_receipt` | model-mediated audit carrier | family **CONFIRMED**; lane placement **NEEDS VERIFICATION** |
| `profiles/standards_profile.yaml` | standards profile | keeps external vocabularies and profile versions pinned | **PROPOSED** starter path |

### Standards profile

External standards matter here, but they do **not** replace KFM’s own contract family.

| Standard | Use in this lane |
| --- | --- |
| JSON Schema Draft 2020-12 | machine-validatable contract files, valid/invalid fixtures, contract-profile language |
| STAC 1.1.x | outward spatiotemporal asset description and scene/package discovery vocabulary |
| DCAT 3 | outward dataset and distribution catalog metadata |
| PROV-O | outward lineage vocabulary for activities, entities, agents, and causal relations |

### Versioning rules

Until a repo-local contract versioning policy is directly surfaced, use the following **PROPOSED starter rules**.

| Change type | Treat as | Suggested version move |
| --- | --- | --- |
| Remove a field, rename a field, or change field meaning | breaking | major |
| Narrow an enum or turn optional into required | breaking | major |
| Change units, time semantics, result grammar, or correction behavior | breaking | major |
| Add an optional field with safe default semantics | non-breaking | minor |
| Add new valid/invalid fixtures without semantic change | non-breaking | patch |
| Clarify docs, descriptions, examples, or comments only | non-breaking | patch |
| Add a new reason/obligation code that consumers must actively handle | usually breaking | major or explicit compatibility note |

#### Compatibility guardrails

- Keep a visible schema version in the contract or its package metadata.
- Never silently change the meaning of an existing reason or obligation code.
- If a contract change alters release, correction, or runtime behavior, update the contract, fixtures, and the relevant runbook in the same review stream.
- If a change affects user-visible runtime outcomes, provide both positive and negative example payloads.

## Validation and gates

KFM’s contract lane is only real if it is executable.

| Gate | Why it exists | Status |
| --- | --- | --- |
| Schema export or lint | keeps publishable contract shape current | **PROPOSED** starter gate |
| Valid/invalid fixture tests | proves the schema can fail closed | doctrinally **CONFIRMED**; exact harness **NEEDS VERIFICATION** |
| Conftest / OPA gate | blocks unapproved contract drift | **PROPOSED** starter gate |
| Docs gate | prevents behavior drift between contracts and maintainer/public docs | requirement **CONFIRMED**; exact wiring **NEEDS VERIFICATION** |
| Runtime negative-path samples | proves `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` behave visibly | **CONFIRMED** requirement |

### Illustrative starter commands

```bash
# Starter wiring only — adjust to the mounted repo paths
python -m pytest -q tests/schema_validation
conftest test policy/ --all-namespaces
```

## Task list / definition of done

- [ ] schema file added or updated in the correct family lane
- [ ] valid fixture and invalid fixture included
- [ ] compatibility impact written down
- [ ] tests or validators updated in the same change
- [ ] policy consequences updated if reason/obligation or release behavior changed
- [ ] documentation updated if outward behavior changed
- [ ] correction or rollback implications noted when applicable

## FAQ

### Why does this directory emphasize structure more than implementation claims?

Because the strongest current evidence is doctrinal and architectural, not a directly mounted repo inventory. This README therefore prioritizes **routing, families, and guardrails** over bluffing maturity.

### Are concrete `run_receipt.json` and `release_manifest.json` files stored here?

Not by default. This lane is for **contract definitions**. Concrete emitted instances belong in the run, release, or evidence lane that owns the actual event.

### Are external standards enough by themselves?

No. JSON Schema, STAC, DCAT, and PROV help with validation and outward vocabulary, but KFM still needs its own object family for policy decisions, runtime envelopes, correction lineage, and release proof.

### Do negative outcomes need contracts too?

Yes. `ABSTAIN`, `DENY`, and `ERROR` are first-class outcomes, not embarrassing edge cases.

### Is this exact subtree already mounted in the repo?

**NEEDS VERIFICATION.** The family map is strong. The exact mounted inventory must still be checked against the live repository.

## Appendix

<details>
<summary><strong>Starter reason and obligation codes</strong></summary>

These are useful starter examples for policy-linked contracts:

| Type | Example code | Typical meaning |
| --- | --- | --- |
| reason | `rights.unknown` | rights or redistribution posture is unresolved |
| reason | `sensitivity.exact_location` | exact location is too sensitive for the requested audience |
| reason | `validation.schema_failed` | required schema or semantic validation failed |
| reason | `runtime.evidence_missing` | no reconstructible evidence path exists for the outward claim |
| reason | `runtime.citation_failed` | evidence was retrieved but user-visible claims failed citation verification |
| obligation | `generalize` | serve only a generalized representation for this audience |
| obligation | `withhold` | do not publish or render the object on the requested surface |
| obligation | `review_required` | escalate to steward or reviewer lane before promotion or outward use |
| obligation | `correction_notice` | publish visible correction state across affected surfaces |
| obligation | `rebuild_projection` | rebuild derived delivery from corrected release scope |
| obligation | `cite` | attach inspectable evidence or fail closed |
| obligation | `log_audit` | emit audit linkage and decision trace |

</details>

<details>
<summary><strong>Starter review questions</strong></summary>

Before merging a contract change, check the following:

- Does the family name still match the object’s real job?
- Would an older consumer misread this payload?
- Does a required field imply a breaking change?
- Did fixtures prove both acceptance and rejection behavior?
- If the contract touches runtime or release behavior, was a negative-path example updated too?

</details>

[Back to top](#contracts)