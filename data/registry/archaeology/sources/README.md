<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/archaeology/sources/readme
name: Archaeology Source Registry README
path: data/registry/archaeology/sources/README.md
type: data-registry-domain-sources-readme
version: v0.2.0
status: draft
owners:
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
registry_scope: archaeology-source-descriptors
path_posture: existing-requested-path-replaced; registry-path-order-conflict-needs-verification; source-descriptor-instance-lane-not-source-payload-lane
sensitivity_posture: restricted-by-default; protected-location-deny-default; cultural-review-required; steward-review-required; rights-and-current-terms-required-before-activation; public-output-blocked-until-redaction-review-release
related:
  - ../../README.md
  - ../README.md
  - ../../../raw/archaeology/README.md
  - ../../../work/archaeology/README.md
  - ../../../quarantine/archaeology/README.md
  - ../../../processed/archaeology/README.md
  - ../../../receipts/README.md
  - ../../../receipts/validation/README.md
  - ../../../proofs/README.md
  - ../../../catalog/README.md
  - ../../../../docs/domains/archaeology/SOURCE_REGISTRY.md
  - ../../../../docs/domains/archaeology/SOURCES.md
  - ../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../docs/domains/archaeology/RELEASE_INDEX.md
  - ../../../../docs/architecture/directory-rules.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../docs/registers/SOURCE_AUTHORITY.md
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/domains/archaeology/
tags:
  - kfm
  - data
  - registry
  - archaeology
  - sources
  - source-descriptor
  - source-role
  - cultural-review
  - steward-review
  - sovereignty
  - rights
  - sensitivity
  - quarantine
  - protected-location-deny
  - cite-or-abstain
notes:
  - "This README replaces the short placeholder at `data/registry/archaeology/sources/README.md`."
  - "Archaeology documentation names both `data/registry/sources/archaeology/*.yaml` and `data/registry/archaeology/sources/` as machine/source-descriptor homes. The lane-order conflict remains NEEDS VERIFICATION until an ADR or registry migration resolves it."
  - "This directory is for source registry/source descriptor records only. It is not raw source data, not a site inventory, not a receipt lane, not proof, not release, and not public output."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Source Registry

Source descriptor instance lane for Archaeology-domain source admission and activation records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data registry" src="https://img.shields.io/badge/root-data%2Fregistry-blue">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-7a3e3e">
  <img alt="Protected locations: deny" src="https://img.shields.io/badge/protected%20locations-DENY-critical">
  <img alt="Cultural review: required" src="https://img.shields.io/badge/cultural%20review-required-purple">
  <img alt="Path posture: needs verification" src="https://img.shields.io/badge/path-NEEDS%20VERIFICATION-orange">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Source descriptor boundary](#source-descriptor-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Source families](#source-families) · [Suggested descriptor fields](#suggested-descriptor-fields) · [Activation states](#activation-states) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/archaeology/sources/` is a registry lane for Archaeology source descriptor records and source activation posture. It is not raw source storage, not a bibliography, not a receipt lane, not proof, not release, not policy source, and not public Archaeology truth.

> [!WARNING]
> Archaeology is a sensitive-domain lane. Protected locations and culturally restricted source details are denied by default unless governed review, sensitivity transformation, redaction receipt, release authority, and rights or cultural authority all resolve.

---

## Scope

This directory is for Archaeology-domain source registry records: compact, reviewable source descriptors that decide whether a source is admitted, restricted, quarantined, denied, retired, or pending cultural/steward review before any connector, watcher, pipeline, validator, AI surface, map layer, or release candidate may rely on it.

A source registry record should answer:

- What source family, publisher, steward, institution, community authority, or repository is being admitted?
- What stable source identity, authority crosswalk, and source role applies?
- What rights, attribution, redistribution, access, embargo, consent, revocation, and terms posture applies?
- What sensitivity class, cultural review state, and public-release class applies?
- What cadence, freshness, stale-state, HTTP-validator, manifest-checksum, or watcher expectation applies?
- Which raw/work/quarantine/processed lanes may receive payloads from this source?
- Which policies, schemas, validators, receipts, proofs, catalog records, release gates, correction notices, and rollback targets must reference this descriptor?

This lane stores **registry control records**, not archaeological payloads or source-native files.

---

## Path posture

The requested and currently existing path is:

```text
data/registry/archaeology/sources/
```

Archaeology documentation also points to this alternate machine-registry pattern:

```text
data/registry/sources/archaeology/
```

That is a real lane-order conflict. This README documents the existing requested path without resolving the conflict. Until accepted registry-layout governance, ADR review, or a migration note settles the convention, treat this path as **NEEDS VERIFICATION** for canonical placement while still using it safely as a README-controlled registry lane.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/registry/archaeology/sources/` |
| Responsibility root | `data/` |
| Artifact family | registry |
| Domain lane | archaeology |
| Record type | SourceDescriptor / SourceActivationDecision support |
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

## Source descriptor boundary

| Rule | Handling |
|---|---|
| Registry is admission control | A descriptor controls whether a source may shape Archaeology claims or candidate objects. |
| Descriptor is not source data | Source payloads go to lifecycle data lanes, not this directory. |
| Source role is fixed at admission | An observed, administrative, regulatory, modeled, aggregate, candidate, or synthetic source role must not be silently upgraded downstream. |
| Rights fail closed | Current terms, attribution, redistribution, embargo, access, consent, revocation, and review obligations must resolve before activation. |
| Sensitivity fails closed | Protected cultural-resource information requires denial, quarantine, restriction, redaction, or steward review. |
| Watchers are non-publishers | Source-health probes and conditional fetches can support admission; they cannot publish or activate a source by themselves. |
| Registry is not catalog | Discovery records such as STAC/DCAT/PROV belong under `data/catalog/`. |
| Registry is not proof | EvidenceBundle, ProofPack, citation validation, integrity proof, and review proof support belong under `data/proofs/` or the accepted proof lane. |
| Registry is not release | ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, and signatures belong under `release/`. |

---

## Accepted material

Accepted content is limited to source-registry records and source-descriptor-local sidecars:

- one descriptor file per Archaeology source family, institution, steward-mediated feed, archive, controlled API, or source endpoint;
- descriptor indexes that point to source descriptor records without becoming catalog or proof records;
- source identity, steward authority, cultural authority, publisher, maintainer, access method, stable identifiers, authority crosswalks, endpoint references, version/cadence expectations, watcher strategy, stale-state rules, and activation posture;
- `source_role`, source-role anti-collapse notes, and authority/candidate status;
- rights, attribution, redistribution, embargo, access, rate-limit, consent, revocation, and steward-review posture;
- sensitivity, cultural review, public-release class, redaction requirements, aggregation/generalization requirements, quarantine triggers, and denial reasons;
- references to policies, schemas, validators, receipts, proof requirements, catalog expectations, release gates, correction notices, rollback targets, and review records;
- local README files that help stewards inspect registry posture without becoming source data, proof, catalog, release, policy, public output, location authority, or generated-answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw archaeology source payloads, downloaded packages, or source-native files | `data/raw/archaeology/` or governed restricted storage; unresolved/sensitive records go to `data/quarantine/archaeology/` |
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

## Source families

The human-facing Archaeology source documents identify eight source families. This registry lane should hold machine-adjacent descriptors for those families, not duplicate the full narrative catalogue.

Starter descriptor filenames should use stable, lowercase slugs. Examples:

```text
data/registry/archaeology/sources/
├── README.md
├── state-site-inventory.source.json
├── public-register-listings.source.json
├── field-survey-forms.source.json
├── excavation-records.source.json
├── collection-repository-records.source.json
├── lab-reports.source.json
├── historic-records.source.json
└── oral-history-cultural-knowledge.source.json
```

> [!NOTE]
> The filename examples are proposed registry hygiene. Do not treat them as proof that descriptor payloads already exist, that rights have been cleared, or that any archaeology source may be ingested.

---

## Suggested descriptor fields

The exact schema remains **NEEDS VERIFICATION** until accepted source descriptor schema evidence is checked. Archaeology source descriptors should be structured enough for policy, cultural review, validation, receipts, proof assembly, catalog closure, correction, rollback, and release review.

| Field | Purpose |
|---|---|
| `id` | Stable source descriptor identity. |
| `source_family` | Source family name. |
| `publisher_or_authority` | Source publisher, steward, institution, agency, repository, cultural authority, or knowledge-holder authority. |
| `source_role` | Primary source role at admission; must not be silently upgraded downstream. |
| `secondary_roles` | Permitted secondary roles, if any. |
| `domain` | `archaeology`. |
| `access_method` | Restricted API, file drop, steward-mediated review, harvested public record, agreement-governed access, archive request, manual upload, or connector strategy. |
| `endpoint_refs` | URLs, accession systems, API identifiers, archive IDs, or source refs, without secrets or restricted access tokens. |
| `rights_posture` | Terms, attribution, redistribution, embargo, access, consent, and revocation posture. |
| `sensitivity_posture` | Protected cultural-resource, restricted-location, restricted-knowledge, aggregate-only, or public-safe posture. |
| `stewardship` | Required steward or cultural-review authority. |
| `freshness` | Cadence, retrieval expectations, stale-state rules, HTTP validators, manifest checksum expectations, and source-vintage rules. |
| `geography` | Spatial scope and precision posture without exposing restricted details. |
| `time_support` | Observed/source/retrieval/valid/release/correction time expectations. |
| `policy_refs` | Relevant source, rights, sensitivity, cultural review, access, or release policies. |
| `schema_refs` | Source descriptor and domain schemas that apply. |
| `validator_refs` | Validators or fixture packs expected before activation. |
| `receipt_expectations` | Receipts expected from watchers, validators, redactors, transforms, review, or release dry runs. |
| `proof_requirements` | Evidence/proof/review closure required before claims or public layers depend on the source. |
| `activation_status` | Current finite state such as `candidate`, `active`, `restricted`, `quarantined`, `denied`, `retired`, or `superseded`. |
| `review_refs` | Steward, cultural, rights, sensitivity, policy, and release review references. |
| `correction_refs` | Correction, withdrawal, supersession, rollback, or revocation references when applicable. |

---

## Activation states

| State | Meaning | Allowed downstream use |
|---|---|---|
| `candidate` | Descriptor is being drafted or reviewed. | No ingestion beyond fixtures or controlled review. |
| `active` | Rights, source role, sensitivity, stewardship, cultural review, cadence, and policy posture are sufficiently resolved for governed intake. | Connector/watcher may emit to approved lifecycle lanes, subject to restrictions. |
| `restricted` | Source may be used only under named restrictions, agreement, steward approval, cultural authority, or reviewer-only access. | Restricted processing only; no public release without additional gates. |
| `quarantined` | Source has unresolved rights, sensitivity, integrity, identity, cultural review, stewardship, or terms risk. | No promotion; quarantine-only handling. |
| `denied` | Source must not shape KFM claims. | No intake or downstream use. |
| `retired` | Source is no longer active but historical references may remain. | Historical audit only; no new intake. |
| `superseded` | Source descriptor has been replaced by a newer descriptor. | Use successor for new work; preserve old descriptor for audit. |

---

## Required checks before use

- [ ] Confirm the descriptor belongs in the Archaeology source registry lane and not in raw/work/quarantine/processed/published data.
- [ ] Resolve the lane-order conflict before treating this path as canonical across the repository.
- [ ] Confirm descriptor identity, publisher/authority, source family, access method, and source role.
- [ ] Confirm rights, attribution, redistribution, terms, embargo, access limits, consent, revocation, and review obligations from current source or steward documentation.
- [ ] Confirm sensitivity posture and cultural/steward review requirements before activation.
- [ ] Confirm watcher cadence, HTTP validators, freshness, stale-state rules, source-vintage rules, and correction/supersession handling.
- [ ] Confirm source role is preserved and not silently upgraded by validation, aggregation, modeling, AI interpretation, or promotion.
- [ ] Confirm policies, schemas, validators, receipts, proof requirements, catalog expectations, release gates, correction references, and rollback targets are referenced.
- [ ] Confirm no credentials, secrets, restricted identifiers, protected location details, or source payloads are stored in the descriptor README or local indexes.
- [ ] Confirm public clients and generated answer surfaces do not read this registry lane directly.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the short placeholder at `data/registry/archaeology/sources/README.md`. | CONFIRMED authored |
| The target path existed in the live repository before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/archaeology/README.md` exists but is still a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| Archaeology source-registry documentation exists at `docs/domains/archaeology/SOURCE_REGISTRY.md`. | CONFIRMED by GitHub contents API during this edit |
| Archaeology source-family documentation exists at `docs/domains/archaeology/SOURCES.md`. | CONFIRMED by GitHub contents API during this edit |
| Archaeology docs identify both `data/registry/sources/archaeology/*.yaml` and `data/registry/archaeology/sources/` patterns. | CONFIRMED from repo documentation |
| Emitted source descriptor payloads exist in this folder. | UNKNOWN |
| The canonical machine schema for Archaeology source descriptors is fully enforced. | NEEDS VERIFICATION |
| This README grants public access, activates any source, or authorizes protected-location exposure. | DENY |

---

## Maintainer note

A source descriptor is the admission control record for a source. In Archaeology, admission is inseparable from sensitivity, cultural review, rights, stewardship, and protected-location denial. Keep the chain explicit:

```text
source descriptor -> governed intake or quarantine -> receipt -> proof/review/catalog/release checks -> governed public-safe surface
```

Never collapse it into:

```text
source descriptor -> public Archaeology truth
```
