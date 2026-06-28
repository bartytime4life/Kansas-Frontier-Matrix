<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/crosswalks/readme
name: Crosswalk Registry README
path: data/registry/crosswalks/README.md
type: data-registry-crosswalks-readme
version: v0.1.0
status: draft
owners:
  - <registry-steward>
  - <crosswalk-steward>
  - <source-steward>
  - <contract-steward>
  - <schema-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: internal-governance
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: crosswalk-registry-records
path_posture: existing-target-stub-replaced; parent-registry-stub-confirmed; exact-crosswalk-registry-layout-needs-verification
sensitivity_posture: registry-internal; no-public-path; source-role-preserving; evidence-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/
  - ../../receipts/
  - ../../proofs/
  - ../../catalog/
  - ../../../contracts/crosswalks/README.md
  - ../../../contracts/domains/flora/flora_taxon_crosswalk.md
  - ../../../docs/sources/catalog/CROSSWALKS.md
  - ../../../docs/architecture/directory-rules.md
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../tests/
  - ../../../fixtures/
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - crosswalks
  - mappings
  - authority-ids
  - taxonomy
  - source-fields
  - vocabulary
  - provenance
  - evidence
  - source-role
  - policy-aware
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/crosswalks/README.md`."
  - "Crosswalk registry records are mapping-state records. They do not define semantic meaning, machine schema shape, policy, validator behavior, proof, catalog closure, release decisions, or public claims."
  - "Semantic meaning for crosswalk families belongs in `contracts/crosswalks/` or domain contract paths. Documentation registers such as `docs/sources/catalog/CROSSWALKS.md` track authoring state; they are not registry records."
  - "Exact registry object names, schemas, validators, emitted examples, and CI enforcement remain NEEDS VERIFICATION until checked against implementation evidence."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Crosswalk Registry

Governed registry lane for crosswalk mapping records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Lane: crosswalks" src="https://img.shields.io/badge/lane-crosswalks-blue">
  <img alt="Boundary: not contract" src="https://img.shields.io/badge/boundary-not%20contract-critical">
  <img alt="Boundary: not release" src="https://img.shields.io/badge/boundary-not%20release-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Crosswalk boundary](#crosswalk-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested record shape](#suggested-record-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/crosswalks/` is a registry lane for governed mapping records. It is not the semantic-contract home, not the source payload home, not proof, not catalog closure, not policy approval, not validation output, not release authority, and not a public data surface.

---

## Scope

`data/registry/crosswalks/` stores registry records that track crosswalk mapping state across KFM object families, source systems, authority systems, names, identifiers, fields, vocabularies, and domain lanes.

A crosswalk registry record may answer bounded questions such as:

- Which source-native identifier maps to which KFM identity, candidate identity, authority identifier, vocabulary term, or relation?
- Which authority namespace, source descriptor, version, retrieval time, review state, evidence support, and policy posture support that mapping?
- Is the mapping exact, inferred, provisional, ambiguous, conflicted, stale, deprecated, denied, superseded, or withdrawn?
- Which downstream object families may rely on the mapping, and which must abstain or require review?
- What correction, supersession, rollback, redaction, or release-state constraints apply?

Crosswalk registry records are **mapping-state records**. They may point to contracts, schemas, policy, source descriptors, EvidenceBundle records, proof packs, validation receipts, catalog entries, release candidates, correction notices, and rollback cards. They do not replace any of those authority objects.

---

## Path posture

The requested lane is:

```text
data/registry/crosswalks/
```

Directory Rules place lifecycle data and emitted proof-family objects under `data/`, and explicitly name `registry` as a data-side phase that sits alongside raw, work, quarantine, processed, catalog, triplets, published, receipts, proofs, and rollback. Crosswalk registry records therefore belong under `data/registry/`, not under a new root.

The parent path exists but is currently a stub:

```text
data/registry/README.md
```

Because the parent registry README has not yet been expanded, this child README documents only the crosswalk registry lane. It does not claim final authority over every future `data/registry/` child.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping-state records and indexes. |
| Source descriptors and source-role inputs | `data/registry/sources/` or accepted source registry lane | Source identity, rights, cadence, role, access, and authority limits. |
| Crosswalk semantic meaning | `contracts/crosswalks/` and domain contract paths | Defines what mapping objects mean. |
| Machine-checkable shape | `schemas/contracts/v1/` | Defines enforceable schema shape. |
| Policy/admissibility/release rules | `policy/` | Decides allowed use, exposure, and gate behavior. |
| Validator code | `tools/`, `packages/`, `pipelines/` | Produces checks; not stored as registry state. |
| Validation receipts | `data/receipts/validation/` | Process memory for validation runs. |
| Evidence and proof | `data/proofs/` | EvidenceBundle closure, proof packs, signatures, and integrity support. |
| Catalog/discovery records | `data/catalog/` | STAC/DCAT/PROV/catalog closure and discovery state. |
| Release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and manifest decisions. |
| Public clients | governed APIs and released artifacts | Public clients do not read registry internals directly. |

---

## Crosswalk boundary

| Rule | Handling |
|---|---|
| Crosswalk row is a claim | Treat every consequential mapping as evidence-bound, reviewable, correctable, and rollback-aware. |
| Preserve source-native values | Do not erase source names, IDs, fields, vocabularies, statuses, or authority versions after normalization. |
| Preserve source role | A crosswalk must not upgrade an observed, modeled, regulatory, aggregate, administrative, candidate, synthetic, or contextual source role. |
| Preserve authority namespace | External authority identifiers must remain namespaced and versioned where possible. |
| Preserve temporal context | Store source time, authority version time, retrieval time, review time, release time, and supersession time when relevant. |
| Fail closed on uncertainty | Missing anchors, stale authority state, ambiguous mappings, conflicts, rights gaps, sensitivity gaps, or evidence gaps should produce `ABSTAIN`, `HOLD`, `DENY`, `CONFLICT`, or `NEEDS_REVIEW`, not silent normalization. |
| Registry is not proof | EvidenceBundle and proof closure remain separate. |
| Registry is not release | Public release requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |

---

## Accepted material

Accepted content in this lane is limited to registry records and registry-local sidecars for crosswalk state:

- authority-ID crosswalk records;
- source-field to canonical-field crosswalk records;
- taxonomy or name crosswalk records;
- vocabulary and controlled-term crosswalk records;
- domain-to-domain relation crosswalk records;
- public-safe derived mapping records after policy/review gates;
- conflict, ambiguity, denial, supersession, withdrawal, correction, and rollback mapping records;
- local indexes that help stewards find crosswalk records without becoming proof, catalog, release, public API, public UI, or generated-answer authority;
- checksums, manifests, and signatures for registry state where applicable;
- README files that document registry boundaries.

Each consequential record should reference the relevant source descriptor, contract, schema, policy, evidence/proof, validation receipt, review record, catalog/release candidate, correction notice, or rollback card by stable ID or path rather than embedding those authority objects.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw source payloads, source-native full extracts, restricted tables, private identifiers, tokens, or credentials | `data/raw/`, `data/work/`, `data/quarantine/`, or governed secret/restricted storage as applicable |
| Semantic crosswalk contract documents | `contracts/crosswalks/` or `contracts/domains/<domain>/...` |
| JSON Schema or machine contract shape | `schemas/contracts/v1/...` |
| Policy rules, rights rules, sensitivity rules, access-control rules, or release rules | `policy/` |
| Validator code, resolver code, pipelines, or transformation logic | `tools/`, `packages/`, `pipelines/`, or `connectors/` as appropriate |
| Fixtures and tests | `fixtures/` and `tests/` |
| Validation receipts or run receipts | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/catalog/discovery records | `data/catalog/` |
| Published artifacts, map layers, tiles, reports, public dashboards, or public API payloads | `data/published/`, governed app/API roots, and `release/` after promotion |
| Release manifests, promotion decisions, rollback cards, correction notices, withdrawal notices, supersession notices | `release/` |
| Documentation-only crosswalk registers | `docs/` lanes such as `docs/sources/catalog/CROSSWALKS.md` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance. It is not proof that these child folders or payloads exist.

```text
data/registry/crosswalks/
├── README.md
├── taxonomy/
│   ├── README.md
│   └── index.local.json
├── authority_ids/
│   ├── README.md
│   └── index.local.json
├── source_fields/
│   ├── README.md
│   └── index.local.json
├── vocabularies/
│   ├── README.md
│   └── index.local.json
├── cross_domain_relations/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

Child lane names should be reviewed before hardening. If an accepted ADR or registry contract chooses a different pattern, migrate with a manifest, redirect note, rollback target, and preserved history.

---

## Suggested record shape

The exact schema remains **NEEDS VERIFICATION**. A crosswalk registry record should be structured enough for inspection, validation, correction, and rollback.

```json
{
  "id": "kfm-crosswalk:<family>:<stable-id>",
  "record_type": "crosswalk_registry_record",
  "family": "taxonomy | authority_id | source_field | vocabulary | cross_domain_relation | other",
  "status": "active | candidate | provisional | conflicted | denied | deprecated | superseded | withdrawn",
  "source_side": {
    "source_descriptor_ref": "kfm://source/...",
    "namespace": "source-native namespace",
    "identifier": "source-native identifier",
    "label": "source-native label",
    "version": "source or authority version",
    "observed_at": "YYYY-MM-DD or timestamp"
  },
  "target_side": {
    "namespace": "kfm or external authority namespace",
    "identifier": "target identifier or candidate id",
    "label": "target label",
    "version": "target authority version"
  },
  "relationship": "exact | synonym | broader | narrower | equivalent | related | inferred | ambiguous | rejected | denied",
  "source_role": "observed | regulatory | modeled | aggregate | administrative | candidate | synthetic | context | restricted",
  "evidence_refs": [],
  "proof_refs": [],
  "validation_receipt_refs": [],
  "policy_refs": [],
  "review_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "release_refs": [],
  "sensitivity_posture": "public-safe | restricted | redacted | generalized | denied | needs-review",
  "outcome": "ALLOW | HOLD | ABSTAIN | DENY | CONFLICT | NEEDS_REVIEW",
  "reason_codes": [],
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing shape sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflow are verified.

---

## Required checks before use

- [ ] Confirm the crosswalk record belongs under `data/registry/crosswalks/` rather than a contract, schema, policy, source, proof, catalog, receipt, or release root.
- [ ] Confirm the mapping preserves source-native identifiers, labels, field names, authority namespaces, authority versions, and source-role posture.
- [ ] Confirm the mapping relationship type is explicit and does not silently convert candidate, ambiguous, stale, conflicted, or denied mappings into accepted mappings.
- [ ] Confirm EvidenceRef/EvidenceBundle support exists for consequential mappings.
- [ ] Confirm rights, sensitivity, geoprivacy, cultural, living-person, rare-species, archaeology, infrastructure, and precise-location risks are handled before downstream exposure.
- [ ] Confirm validation receipts are present when the record supports release-candidate or public-safe use.
- [ ] Confirm proof/catalog/release states remain separate and are referenced, not embedded.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths are recorded for mappings that can change.
- [ ] Confirm no public client, map layer, generated answer, vector index, graph edge, report, or dashboard treats this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/crosswalks/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| `contracts/crosswalks/README.md` exists and defines semantic-contract boundaries for crosswalks. | CONFIRMED by GitHub contents API during this edit |
| `docs/sources/catalog/CROSSWALKS.md` exists as a documentation register, not the crosswalk records themselves. | CONFIRMED by GitHub contents API during this edit |
| `contracts/domains/flora/flora_taxon_crosswalk.md` exists as a Flora crosswalk semantic contract. | CONFIRMED by GitHub contents API during this edit |
| Emitted crosswalk registry records currently exist under this lane. | UNKNOWN |
| A canonical crosswalk registry schema is fully enforced. | NEEDS VERIFICATION |
| CI validates crosswalk registry records. | UNKNOWN |
| This README grants public access to registry internals. | DENY |

---

## Maintainer note

Crosswalk registries are useful only when they preserve ambiguity, source role, evidence, authority boundaries, correction state, and rollback state. The safe chain is:

```text
source-native value -> crosswalk registry record -> validation/proof/policy/review -> catalog/release -> governed public surface
```

Never collapse it into:

```text
source-native value -> normalized label -> public truth
```
