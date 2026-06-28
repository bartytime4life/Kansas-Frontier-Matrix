<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/archaeology/readme
name: Archaeology Registry README
path: data/registry/archaeology/README.md
type: data-registry-domain-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <archaeology-source-steward>
  - <archaeology-domain-steward>
  - <sensitivity-reviewer>
  - <rights-holder-representative>
  - <cultural-review-steward>
  - <policy-steward>
  - <validation-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: archaeology-domain-registry-parent
path_posture: existing-parent-stub-replaced; child-sources-lane-confirmed; registry-path-order-conflict-needs-verification
sensitivity_posture: restricted-by-default; protected-location-deny-default; cultural-review-required; steward-review-required; rights-and-current-terms-required-before-activation; public-output-blocked-until-redaction-review-release
related:
  - ../README.md
  - sources/README.md
  - ../../raw/archaeology/README.md
  - ../../work/archaeology/README.md
  - ../../quarantine/archaeology/README.md
  - ../../processed/archaeology/README.md
  - ../../receipts/README.md
  - ../../receipts/validation/README.md
  - ../../proofs/README.md
  - ../../catalog/README.md
  - ../../../docs/domains/archaeology/SOURCE_REGISTRY.md
  - ../../../docs/domains/archaeology/SOURCES.md
  - ../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../docs/domains/archaeology/RELEASE_INDEX.md
  - ../../../docs/architecture/directory-rules.md
  - ../../../docs/architecture/source-roles.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../docs/registers/SOURCE_AUTHORITY.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/domains/archaeology/
tags:
  - kfm
  - data
  - registry
  - archaeology
  - source-descriptor
  - admission-control
  - source-role
  - cultural-review
  - steward-review
  - rights
  - sensitivity
  - quarantine
  - protected-location-deny
  - cite-or-abstain
notes:
  - "This README replaces the greenfield stub at `data/registry/archaeology/README.md`."
  - "The confirmed child lane during this edit is `sources/`."
  - "Archaeology docs show a registry path-order conflict between `data/registry/archaeology/sources/` and `data/registry/sources/archaeology/`. This README documents the existing parent lane without resolving that conflict."
  - "This directory is for Archaeology registry routing and local registry records only. It is not raw source data, receipts, proofs, catalog output, release state, policy source, or public Archaeology truth."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Registry

Domain parent lane for Archaeology registry records and source-admission routing.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data registry" src="https://img.shields.io/badge/root-data%2Fregistry-blue">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-7a3e3e">
  <img alt="Protected locations: deny" src="https://img.shields.io/badge/protected%20locations-DENY-critical">
  <img alt="Cultural review: required" src="https://img.shields.io/badge/cultural%20review-required-purple">
  <img alt="Path posture: needs verification" src="https://img.shields.io/badge/path-NEEDS%20VERIFICATION-orange">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Registry boundary](#registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/archaeology/` is a registry parent lane. It may route Archaeology source descriptors and future Archaeology registry records, but it is not raw source storage, not a source catalog profile, not a receipt lane, not proof, not release, not policy source, and not public Archaeology truth.

> [!WARNING]
> Archaeology is a sensitive-domain lane. Protected locations and culturally restricted source details are denied by default unless governed review, sensitivity transformation, redaction receipt, release authority, and rights or cultural authority all resolve.

---

## Scope

This directory is the Archaeology-domain parent lane under `data/registry/`. It exists to organize registry records that control whether Archaeology sources, descriptors, authorities, activation states, and related registry objects may shape downstream KFM work.

At this maturity level, the confirmed child lane is:

```text
data/registry/archaeology/sources/
```

That child lane is for Archaeology source descriptor and activation records. This parent README routes maintainers to the correct responsibility homes and prevents registry material from being confused with raw payloads, receipts, proofs, catalogs, release decisions, policy source, or public artifacts.

A registry record in this branch should help answer:

- Which Archaeology source or registry object is being admitted or controlled?
- What stable identity, source role, rights posture, and access posture applies?
- What sensitivity, cultural review, public-release, cadence, and stale-state posture applies?
- Which policies, schemas, validators, receipts, proofs, catalogs, release gates, corrections, and rollback hooks must reference the registry record?
- What is the current finite activation state: candidate, active, restricted, quarantined, denied, retired, or superseded?

---

## Path posture

The requested and currently existing parent path is:

```text
data/registry/archaeology/
```

The confirmed child path is:

```text
data/registry/archaeology/sources/
```

Archaeology documentation also points to this alternate machine-registry pattern:

```text
data/registry/sources/archaeology/
```

This is an unresolved path-order conflict. This README documents the existing requested parent lane and its confirmed child lane without declaring final canonical placement. Treat this branch as **NEEDS VERIFICATION** for canonical registry layout until an ADR, migration note, or accepted Directory Rules update resolves the registry ordering convention.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/registry/archaeology/` |
| Responsibility root | `data/` |
| Artifact family | registry |
| Domain lane | archaeology |
| Confirmed child lane | `sources/` |
| Current child purpose | SourceDescriptor / SourceActivationDecision support records |
| Human-facing source registry docs | `docs/domains/archaeology/SOURCE_REGISTRY.md` and `docs/domains/archaeology/SOURCES.md` |
| Cross-domain authority register | `docs/registers/SOURCE_AUTHORITY.md` and `control_plane/source_authority_register.yaml`, where accepted |
| Schema authority | `schemas/contracts/v1/source/`, subject to accepted schema-home ADRs |
| Policy authority | `policy/domains/archaeology/`, sensitivity/cultural-review policy roots, and cross-domain policy roots |
| Payload lanes | `data/raw/archaeology/`, `data/work/archaeology/`, `data/quarantine/archaeology/`, `data/processed/archaeology/`, and `data/published/` after release |
| Receipt authority | `data/receipts/`, not this registry lane |
| Proof authority | `data/proofs/`, not this registry lane |
| Catalog authority | `data/catalog/`, not this registry lane |
| Release authority | `release/`, not this registry lane |
| Public access posture | No direct public path. Public clients use governed APIs and released, redacted, policy-safe artifacts only. |

---

## Confirmed child lanes

The child lane below was confirmed by a current GitHub read while replacing this parent stub. This confirms README/path evidence only. It does **not** prove emitted descriptor payloads, canonical schema enforcement, validators, fixtures, CI enforcement, policy enforcement, connector activation, release integration, correction hooks, rollback hooks, or public-safe summaries.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`sources/`](sources/README.md) | CONFIRMED README | Archaeology source descriptor and activation records for source admission, source-role preservation, rights posture, sensitivity posture, cultural/steward review, cadence, stale-state, and downstream gate references. | Not raw source data, not receipts, not proofs, not catalog records, not release manifests, not policy source, and not public Archaeology truth. |

---

## Registry boundary

| Rule | Handling |
|---|---|
| Registry is admission control | It controls whether sources and registry objects may shape downstream Archaeology work. |
| Registry is not source data | Acquired payloads go to lifecycle data lanes, not this directory. |
| Registry is not documentation-only | Human-facing docs explain; registry records should be machine-adjacent and gateable. |
| Source role is preserved | Source role is fixed at admission and must not be silently upgraded by validation, AI interpretation, aggregation, or promotion. |
| Rights fail closed | Terms, attribution, redistribution, access constraints, consent, revocation, and review obligations must resolve before activation. |
| Sensitivity fails closed | Protected cultural-resource information requires denial, quarantine, restriction, redaction, or steward review. |
| Registry is not receipt | Run, validation, redaction, telemetry, AI, aggregation, correction, rollback, and release-support receipts live under `data/receipts/`. |
| Registry is not proof | EvidenceBundle, ProofPack, citation validation, integrity proof, and review proof support live under `data/proofs/`. |
| Registry is not catalog | Discovery records such as STAC/DCAT/PROV live under `data/catalog/`. |
| Registry is not release | ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, and signatures live under `release/`. |

---

## Accepted material

Accepted content is limited to Archaeology registry records and registry-local sidecars:

- README files that route Archaeology registry material without becoming source truth;
- source descriptor and source activation support records under the confirmed `sources/` child lane;
- local registry indexes that point to source descriptors without becoming catalog or proof records;
- source identity, authority, steward, publisher, access method, stable identifiers, authority crosswalks, endpoint references, cadence expectations, watcher strategy, stale-state rules, and activation posture;
- `source_role` and anti-collapse notes;
- rights, attribution, redistribution, access, embargo, consent, revocation, and steward-review posture;
- sensitivity, cultural review, public-release class, redaction requirements, aggregation/generalization requirements, quarantine triggers, and denial reasons;
- references to policies, schemas, validators, receipts, proof requirements, catalog expectations, release gates, correction notices, rollback targets, and review records.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Archaeology source payloads, downloaded packages, or source-native files | `data/raw/archaeology/` or governed restricted storage; unresolved/sensitive records go to `data/quarantine/archaeology/` |
| Protected cultural-resource details or restricted location details | Do not expose in README/index text; use governed restricted or quarantine handling only |
| Work-in-progress transforms, scratch outputs, unresolved candidates, or derived experiments | `data/work/archaeology/` |
| Processed Archaeology objects or public-safe derivatives | `data/processed/archaeology/` after gates; `data/published/` only after release |
| Source catalog profiles and human source documentation | `docs/sources/catalog/` and `docs/domains/archaeology/` |
| EvidenceBundle, ProofPack, CatalogMatrix, citation validation, review proof support, or integrity proof | `data/proofs/` |
| STAC, DCAT, PROV, discovery records, or public catalog exports | `data/catalog/` |
| RunReceipt, validation receipt, redaction receipt, aggregation receipt, AI receipt, telemetry receipt, watcher receipt, or EventRunReceipt | `data/receipts/` |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, release signature, or release changelog | `release/` |
| Policy source, Rego files, source-role policies, sensitivity policies, cultural review policies, or access-control rules | `policy/` |
| Semantic contracts and machine schemas | `contracts/` and `schemas/` |
| Connector code, watcher code, packages, fixtures, tests, or CI workflows | `connectors/`, `tools/`, `packages/`, `fixtures/`, `tests/`, `.github/workflows/` |
| Public map/API/UI payloads, graph edges, vector-index content, reports, dashboards, or generated answer text | governed public outputs only after evidence, policy, validation, review, redaction, release, correction, and rollback gates close |

---

## Suggested directory shape

The following map is documentation guidance, not proof that payloads exist beyond the README paths verified in this edit.

```text
data/registry/archaeology/
├── README.md
├── sources/
│   ├── README.md
│   ├── state-site-inventory.source.json
│   ├── public-register-listings.source.json
│   ├── field-survey-forms.source.json
│   ├── excavation-records.source.json
│   ├── collection-repository-records.source.json
│   ├── lab-reports.source.json
│   ├── historic-records.source.json
│   └── oral-history-cultural-knowledge.source.json
└── index.local.json
```

`index.local.json` is optional and registry-local only. It is not a proof index, catalog record, release manifest, public-layer pointer, search index, vector index, map source, policy authority, source truth, or generated-answer source.

---

## Required checks before use

- [ ] Confirm the registry record belongs in the Archaeology registry lane and not in raw/work/quarantine/processed/published data.
- [ ] Resolve the registry path-order conflict before treating this path as canonical across the repository.
- [ ] Confirm descriptor identity, publisher/authority, source family, access method, and source role.
- [ ] Confirm rights, attribution, redistribution, terms, embargo, access limits, consent, revocation, and review obligations from current source or steward documentation.
- [ ] Confirm sensitivity posture and cultural/steward review requirements before activation.
- [ ] Confirm watcher cadence, HTTP validators, freshness, stale-state rules, source-vintage rules, and correction/supersession handling.
- [ ] Confirm source role is preserved and not silently upgraded by validation, aggregation, modeling, AI interpretation, or promotion.
- [ ] Confirm policies, schemas, validators, receipts, proof requirements, catalog expectations, release gates, correction references, and rollback targets are referenced.
- [ ] Confirm no credentials, secrets, restricted identifiers, protected location details, or source payloads are stored in README or local indexes.
- [ ] Confirm public clients and generated answer surfaces do not read this registry lane directly.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/archaeology/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/archaeology/sources/README.md` exists and defines the Archaeology source descriptor child lane. | CONFIRMED by GitHub contents API during this edit |
| Archaeology source-registry documentation exists at `docs/domains/archaeology/SOURCE_REGISTRY.md`. | CONFIRMED by GitHub contents API during this edit |
| Archaeology source-family documentation exists at `docs/domains/archaeology/SOURCES.md`. | CONFIRMED by GitHub contents API during this edit |
| Archaeology docs identify both `data/registry/sources/archaeology/*.yaml` and `data/registry/archaeology/sources/` patterns. | CONFIRMED from repo documentation |
| Emitted source descriptor payloads exist under this parent lane. | UNKNOWN |
| The canonical machine schema for Archaeology source descriptors is fully enforced. | NEEDS VERIFICATION |
| This README grants public access, activates any source, or authorizes protected-location exposure. | DENY |

---

## Maintainer note

This parent lane keeps Archaeology registry material organized without turning registry records into data, receipts, proofs, catalog records, release decisions, policy, or public truth. Keep the chain explicit:

```text
registry record -> governed intake or quarantine -> receipt -> proof/review/catalog/release checks -> governed public-safe surface
```

Never collapse it into:

```text
registry record -> public Archaeology truth
```
