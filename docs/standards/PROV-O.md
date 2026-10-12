<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standards/prov-o
title: PROV-O — KFM Semantic Provenance Boundary
type: "standard; interoperability guidance; conformance readiness"
version: v2.0-draft
status: "draft; repository-grounded; no adopted KFM PROV-O profile; no generic validator; no release or publication"
owners:
  - "@bartytime4life — CODEOWNERS review route"
  - "NEEDS VERIFICATION — semantic-profile owner and independent reviewer"
created: 2026-05-14
updated: 2026-08-18
policy_label: "provenance; evidence-boundary; fail-closed"
owning_root: docs/
current_path: docs/standards/PROV-O.md
responsibility: >
  Explain W3C PROV-O/PAV interoperability, reconcile current provenance-shaped
  KFM surfaces, and bound every profile, conformance, release, and publication claim.
truth_posture: >
  CONFIRMED same-path placement and pinned repository shapes; PROPOSED future
  namespace, context, mappings, shapes, validators, fixtures, policy effects,
  and producer/consumer integration; UNKNOWN production RDF records and publication.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3ddf171cd7c4a5b4dbbeec3127e9721411c2c8eb
  target_prior_blob: 919452dbd8abe1ff1079a7235d43b211de6fae54
  directory_rules: docs/doctrine/directory-rules.md
  review_route: .github/CODEOWNERS
external_currentness:
  prov_o: "W3C Recommendation, 2013-04-30; http://www.w3.org/ns/prov#"
  rdf_dataset_canonicalization: "W3C Recommendation, 2024-05-21; RDFC-1.0"
  pav: "PAV 2.3.1 community ontology; optional unless adopted"
related:
  - ./README.md
  - ./PROV.md
  - ./PROV/README.md
  - ./CANONICALIZATION.md
  - ./OPENLINEAGE_FACETS.md
  - ./EVIDENCE_BUNDLE.md
  - ./RUN_RECEIPT.md
  - ../architecture/contract-schema-policy-split.md
  - ../../contracts/evidence/evidence_bundle.md
  - ../../contracts/runtime/run_receipt.md
notes:
  - "Same-path documentation modernization only; no contract, schema, policy, validator, runtime, workflow, dependency, release, deployment, or publication change."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="prov-o--kfm-provenance-vocabulary-conformance"></a>

# PROV-O — KFM Semantic Provenance Boundary

> **Operating rule.** PROV-O can describe how an entity came to exist. It does not establish source authority, factual correctness, rights, sensitivity clearance, policy approval, release, or publication.

> [!CAUTION]
> The pinned repository evidence establishes no canonical KFM PROV-O application profile, namespace, JSON-LD context, generic graph validator, production producer/consumer inventory, governed release, or public publication.

> [!WARNING]
> Current EvidenceBundle and RunReceipt schemas are closed JSON shapes. Do not insert `@context`, `@graph`, `prov:*`, or `pav:*` members without a versioned contract/schema migration.

| Boundary | Current result |
|---|---|
| Placement | **PLACE** at existing `docs/standards/PROV-O.md` |
| Upstream | W3C PROV-O; namespace `http://www.w3.org/ns/prov#` |
| KFM profile | **NOT ESTABLISHED** |
| Release/public effect | None |

<a id="contents"></a>

## Contents

1. [Purpose](#section-1-purpose)
2. [Why PROV-O in KFM](#section-2-why-prov-o-in-kfm)
3. [Authority and scope](#section-3-authority-and-scope)
4. [Starting-point terms](#section-4-starting-point-terms)
5. [KFM application profile](#section-5-kfm-application-profile)
6. [Predicate stability rule](#section-6-predicate-stability-rule)
7. [Worked JSON-LD example](#section-7-worked-json-ld-example)
8. [PROV-O ↔ RunReceipt round-trip](#section-8-prov-o-runreceipt-round-trip)
9. [PROV-O vs CIDOC-CRM E13 — demarcation](#section-9-prov-o-vs-cidoc-crm-e13-demarcation)
10. [Canonicalization](#section-10-canonicalization)
11. [Policy gates and validation](#section-11-policy-gates-and-validation)
12. [OpenLineage → PROV-O semantics](#section-12-openlineage-prov-o-semantics)
13. [Open questions and verification backlog](#section-13-open-questions-and-verification-backlog)
14. [Related docs](#section-14-related-docs)
15. [Appendix A — Mapping tables](#appendix-a-mapping-tables)
16. [Appendix B — Negative-state fixtures](#appendix-b-negative-state-fixtures)

---

<a id="section-1-purpose"></a>

## 1. Purpose

This page is human-readable interoperability guidance. Contracts define KFM object meaning, schemas define machine shape, policy decides admissibility, validators prove only declared checks, and governed release records decide release. This page adopts none of those authorities and activates no source, dependency, runtime, release, or publication.

[Back to contents](#contents)

---

<a id="section-2-why-prov-o-in-kfm"></a>

## 2. Why PROV-O in KFM

PROV-O supplies shared terms for Entity, Activity, Agent, generation, use, derivation, association, attribution, and activity time. These can connect KFM object families without merging their authority. A valid graph can still describe false, stale, sensitive, disallowed, or unreleased material; EvidenceBundle resolution and governed policy/release decisions remain necessary.

[Back to contents](#contents)

---

<a id="section-3-authority-and-scope"></a>

## 3. Authority and scope

| Question | Authority |
|---|---|
| Official PROV meaning | W3C PROV-O / PROV-DM / PROV-CONSTRAINTS |
| KFM object meaning/shape | `contracts/` / `schemas/contracts/v1/` |
| Allowed vocabulary combination | Future accepted profile/shape and validator |
| Admissibility | `policy/` and accountable review |
| Release/publication | Exact governed release, correction, and rollback evidence |

PAV 2.3.1 is an optional community ontology, not a W3C Recommendation or current KFM requirement. Semantic IRIs, KFM IDs, repository paths, digests, EvidenceRefs, and release/correction IDs remain distinct.

[Back to contents](#contents)

---

<a id="section-4-starting-point-terms"></a>

## 4. Starting-point terms

| Term | Direction or kind | Bounded meaning |
|---|---|---|
| `prov:Entity` / `Activity` / `Agent` | classes | Thing, occurrence, and responsibility-bearing actor |
| `prov:wasGeneratedBy` | Entity → Activity | Activity that generated an entity |
| `prov:generated` / `used` | Activity → Entity | Output / input |
| `prov:wasDerivedFrom` | Entity → Entity | Derivative lineage |
| `prov:wasAssociatedWith` | Activity → Agent | Activity-agent association |
| `prov:wasAttributedTo` | Entity → Agent | Entity attribution |
| `prov:wasInformedBy` | Activity → Activity | Activity influence/order |
| `prov:startedAtTime` / `endedAtTime` | Activity → literal | Execution interval |

Do not collapse observation-valid, upstream publication, retrieval, activity, receipt, review, release, correction, or withdrawal time.

[Back to contents](#contents)

---

<a id="section-5-kfm-application-profile"></a>

## 5. KFM application profile

**Current disposition: HOLD.** The proposed `CatalogTrustExtension` uses exact JSON keys such as `kfm:run_receipt_ref` and `kfm:proof_ref`; the proposed `RemoteSensingLineageActivity` contains a custom `prov_activity` object. Similar names do not make those fields official RDF predicates or prove graph conformance.

A future profile must version namespace/context, serialization, node kinds, direction, cardinality, identifiers, reference closure, time, rights/sensitivity, correction/rollback, producer/consumer compatibility, and validator outcomes. Maturity remains: documented → proposed → validated → integrated → governed → release-eligible → released → published.

[Back to contents](#contents)

---

<a id="section-6-predicate-stability-rule"></a>

## 6. Predicate stability rule

Official IRIs retain W3C meaning and direction. Do not mint aliases for official terms, reverse `prov:used` or `prov:wasGeneratedBy`, treat `prov:Agent` as accountable approval, or treat `prov:wasDerivedFrom` as proof of truth or rights. Extensions require an accepted namespace, stable definition, shape constraints, fixtures, compatibility rules, and public-safety boundaries.

[Back to contents](#contents)

---

<a id="section-7-worked-json-ld-example"></a>

## 7. Worked JSON-LD example

This is **illustrative proposed-profile material**, not a current EvidenceBundle, RunReceipt, accepted context, or release artifact. `example.invalid` is intentionally non-resolving.

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "https://example.invalid/kfm/profile/v1#"
  },
  "@graph": [
    {
      "@id": "urn:example:entity:derived",
      "@type": "prov:Entity",
      "prov:wasGeneratedBy": {"@id": "urn:example:activity:run"},
      "prov:wasDerivedFrom": {"@id": "urn:example:entity:source"}
    },
    {
      "@id": "urn:example:activity:run",
      "@type": "prov:Activity",
      "prov:used": {"@id": "urn:example:entity:source"},
      "kfm:runReceipt": {"@id": "urn:example:receipt:run"}
    }
  ]
}
```

It demonstrates direction and distinct IDs only, not schema validity, canonicalization, rights, policy, release, or publication.

[Back to contents](#contents)

---

<a id="section-8-prov-o-runreceipt-round-trip"></a>

## 8. PROV-O ↔ RunReceipt round-trip

No universal round-trip is established. A future profile may choose a direct semantic reference, receipt backlink, deterministic Activity IRI, or separate projection artifact. Each requires versioned mapping, identity/digest boundaries, reference closure, temporal agreement, correction traversal, and finite outcomes such as `PASS`, `ABSTAIN`, `DENY`, `QUARANTINE`, `ERROR`, and `NOT_APPLICABLE`.

[Back to contents](#contents)

---

<a id="section-9-prov-o-vs-cidoc-crm-e13-demarcation"></a>

## 9. PROV-O vs CIDOC-CRM E13 — demarcation

PROV-O emphasizes execution and derivation lineage. CIDOC CRM E13 emphasizes an act of attribute assignment in cultural-heritage modeling. Neither replaces the other, source authority, EvidenceBundle closure, review, or release. Any crosswalk must document identifiers, direction, cardinality, loss, round-trip behavior, and abstention.

[Back to contents](#contents)

---

<a id="section-10-canonicalization"></a>

## 10. Canonicalization

[`CANONICALIZATION.md`](./CANONICALIZATION.md) records current JSON canonicalization evidence; that does not bind RDF semantic identity. A future RDF profile must pin graph boundaries, algorithm/version, blank-node and order-variance fixtures, equivalence/non-equivalence tests, toolchain identity, no-network reproducibility, migration/correction/rollback, and signature coverage. Evaluate W3C RDF Dataset Canonicalization 1.0 rather than silently carrying the older `URDNA2015` label forward.

[Back to contents](#contents)

---

<a id="section-11-policy-gates-and-validation"></a>

## 11. Policy gates and validation

Current evidence is bounded to proposed closed JSON schemas, exact proposed trust fields, a custom proposed lineage projection, and deterministic synthetic closure code—not a generic RDF/OWL, JSON-LD, SHACL, ShEx, or production PROV-O validator.

Future validation should cover syntax, pinned local context, vocabulary, node kinds/direction/cardinality, identity/digest boundaries, reference closure, time separation, rights/sensitivity/consent/sovereignty, correction/rollback, and policy effects. Tests remain no-network. Fail closed on mutable context, reversed predicates, silent aliases, unresolved required evidence, receipt/activity mismatch, ambiguous digest boundary, broken correction, restricted precision, or remote-context dereferencing.

[Back to contents](#contents)

---

<a id="section-12-openlineage-prov-o-semantics"></a>

## 12. OpenLineage → PROV-O semantics

[`OPENLINEAGE_FACETS.md`](./OPENLINEAGE_FACETS.md) describes an inactive fixture-first profile, not a verified live exporter. A future derived projection may map Run to `prov:Activity`, datasets to used/generated Entities, and producer software to `prov:SoftwareAgent`. Record source profile, mapping version, transformed/dropped fields, unresolved IDs, digest, correction behavior, and reverse-reconstruction limits.

[Back to contents](#contents)

---

<a id="section-13-open-questions-and-verification-backlog"></a>

## 13. Open questions and verification backlog

Unresolved: owner, namespace/context, serialization, shape language, EvidenceBundle route, RunReceipt mapping, canonicalization boundary, PAV adoption, CIDOC crosswalk, OpenLineage loss, policy effects, independent review, producer/consumer inventory, migration/correction/rollback, and sensitive-graph generalization.

The smallest next slice is one rights-safe synthetic object family with a real intended consumer, one versioned mapping/shape, deterministic positive and fail-closed fixtures, no-network validation, exact non-effects, preserved compatibility, and release/publication left inactive. Keep the profile on **HOLD** until authority resolves.

[Back to contents](#contents)

---

<a id="section-14-related-docs"></a>

## 14. Related docs

- [`docs/standards/README.md`](./README.md)
- [`docs/standards/PROV.md`](./PROV.md)
- [`docs/standards/PROV/README.md`](./PROV/README.md)
- [`docs/standards/EVIDENCE_BUNDLE.md`](./EVIDENCE_BUNDLE.md)
- [`docs/standards/RUN_RECEIPT.md`](./RUN_RECEIPT.md)
- [`EvidenceBundle` contract](../../contracts/evidence/evidence_bundle.md)
- [`RunReceipt` contract](../../contracts/runtime/run_receipt.md)
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)
- [W3C PROV-CONSTRAINTS](https://www.w3.org/TR/prov-constraints/)
- [W3C RDF Dataset Canonicalization 1.0](https://www.w3.org/TR/rdf-canon/)
- [PAV ontology](https://pav-ontology.github.io/pav/)

[Back to contents](#contents)

---

<a id="appendix-a-mapping-tables"></a>

## Appendix A — Mapping tables

| Official term | Candidate KFM use | Not equivalent to |
|---|---|---|
| `prov:Entity` | Input/output/artifact/projection | EvidenceBundle truth or release approval |
| `prov:Activity` | Transform/acquisition/validation/correction | RunReceipt without a versioned mapping |
| `prov:Agent` | Software/person/organization | Accountable reviewer role |
| `prov:wasGeneratedBy` / `used` | Output/input relation | Receipt or `inputs[]` without mapping |
| `prov:wasDerivedFrom` | Derivative lineage | Proof of truth or rights |
| `prov:wasAssociatedWith` | Activity-agent relation | Approval/signature verification |
| activity time | Execution interval | Observation, publication, release, or withdrawal time |

Current KFM field names remain contract/schema fields, not accepted RDF predicates, until a profile maps them.

[Back to contents](#contents)

---

<a id="appendix-b-negative-state-fixtures"></a>

## Appendix B — Negative-state fixtures

| Fixture | Expected bounded result |
|---|---|
| Unknown/mutable context | `ABSTAIN` or profile `FAIL` |
| Reversed predicate / silent alias / wrong node kind | profile `FAIL` |
| Required receipt unresolved | `ABSTAIN`, `DENY`, or `QUARANTINE` |
| Receipt/activity mismatch | `QUARANTINE` |
| Missing digest algorithm/graph boundary | `ABSTAIN` |
| Activity time reused as observation/release time | profile `FAIL` |
| Software Agent treated as approval | `DENY` |
| Broken correction lineage | `FAIL` or `QUARANTINE` |
| Restricted public precision | `DENY` |
| Arbitrary remote-context retrieval | `ERROR`; no request |
| JSON-LD injected into current closed objects | schema `FAIL` |

Before changing “no adopted profile,” verify accountable ownership, accepted identity/context/version, graph boundary, aligned contract/schema/shape authority, deterministic fixtures and validator, at least one real producer and consumer, rights/sensitivity tests, correction/migration/rollback, governed release criteria, and actual publication evidence before any publication claim.

[Back to contents](#contents)
