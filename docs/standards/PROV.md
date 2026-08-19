<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standards-prov-v1
title: PROV — KFM Semantic Provenance Boundary
type: standard; semantic-provenance; repository-boundary
version: v2.0-draft
status: "draft; repository-grounded; profile-convergence-held; synthetic-closure-only; no-adoption; no-release; no-publication"
owners:
  - "@bartytime4life — verified GitHub review route through CODEOWNERS"
  - "NEEDS VERIFICATION — accountable provenance, evidence, catalog, policy, release, and independent-review stewardship"
created: 2026-05-14
updated: 2026-08-18
policy_label: "repository-facing; standards-guidance; provenance; release-gated"
owning_root: docs/
current_path: docs/standards/PROV.md
responsibility: >
  Explain W3C PROV, reconcile current KFM evidence, receipt, catalog,
  lineage, and supply-chain surfaces, disclose the bounded synthetic proof,
  and state what remains before KFM may claim adoption or conformance.
truth_posture: >
  CONFIRMED placement, CODEOWNERS route, PROV-O Recommendation, closed
  EvidenceBundle shape, fixture-only OpenLineage boundary, synthetic
  seven-record projection, placeholder catalog/prov lane, compatibility
  data/prov lane, and proposed ADR-0022 / PROPOSED KFM-wide PROV or PAV
  adoption, context, generic validator, released catalog, or public endpoint /
  CONFLICTED ownership across PROV.md, PROV-O.md, PROVENANCE.md, and PROV/README.md.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: ad143585aa3e0ad1da34111b07ac378f8ccdcb50
  target_prior_blob: e69e4e9ee9a9771d0ad33aecfbb7ce91bd60867f
  provenance_standard_blob: 84162bc67244a062638a960e01390a5de6d797e2
  evidence_bundle_schema_blob: cf5256831b63dca46a5f68b168441adcf68b8751
  synthetic_projection_blob: 2f2f90b67b64664b89ea4937febfc223c256b838
external_currentness:
  access_date: 2026-08-18
  prov_o: "W3C Recommendation dated 2013-04-30; namespace http://www.w3.org/ns/prov#"
  pav: "PAV documentation identifies version 2.3.1; KFM adoption is not established"
related:
  - ./README.md
  - ./PROV-O.md
  - ./PROVENANCE.md
  - ./PROV/README.md
  - ./OPENLINEAGE_FACETS.md
  - ./RUN_RECEIPT.md
  - ./EVIDENCE_BUNDLE.md
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - ../../contracts/evidence/evidence_bundle.md
  - ../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../contracts/runtime/run_receipt.md
  - ../../contracts/telemetry/openlineage_run_event_projection.md
  - ../../contracts/data/synthetic_release_catalog_closure_profile.md
  - ../../data/catalog/prov/README.md
  - ../../data/prov/README.md
tags: [kfm, standards, provenance, prov, prov-o, pav, evidence, lineage, catalog]
notes:
  - "Same-path documentation modernization only; no contract, schema, policy, validator, fixture, workflow, data, runtime, release, deployment, or publication changes."
  - "Legacy document ID, created date, H1 compatibility anchor, numbered anchors, object-family distinctions, and cite-or-abstain posture are retained."
  - "No canonical winner is selected among current PROV-family documentation surfaces."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="prov--w3c-provenance-in-kfm"></a>

# PROV — KFM Semantic Provenance Boundary

> **Operating rule.** Provenance describes relationships among entities, activities, and agents. It does not create source authority, evidence sufficiency, policy approval, review, release, publication, or public truth.

> [!IMPORTANT]
> **Human-readable guidance only.** W3C defines PROV semantics. KFM contracts define object meaning, schemas define shape, policy decides admissibility, validators prove bounded checks, and governed records decide release.

> [!CAUTION]
> **No adopted KFM-wide PROV profile was verified.** KFM has a bounded synthetic STAC/DCAT/PROV projection, but no verified generic context, RDF/OWL or PROV-N producer, semantic validator, claim-wide gate, released PROV catalog, or public endpoint.

| Field | Current result |
|---|---|
| Snapshot | `main@ad143585aa3e0ad1da34111b07ac378f8ccdcb50` |
| Placement | **PLACE** at `docs/standards/PROV.md` |
| Review | `@bartytime4life`; specialist stewardship **NEEDS VERIFICATION** |
| Upstream | PROV-O W3C Recommendation, 2013-04-30; `http://www.w3.org/ns/prov#` |
| KFM profile | **NOT ESTABLISHED** |
| Executable proof | Deterministic, no-network, synthetic seven-record closure |
| EvidenceBundle | Closed ten-field schema; no PROV/PAV properties |
| Catalog | `data/catalog/prov/` placeholder; `data/prov/` compatibility lane |
| Governance | ADR-0022 proposed |
| Release/public effect | None |

<a id="quick-jump"></a>

**Navigation:** [Status](#0-current-repository-status-and-authority) · [Scope](#1-purpose--scope) · [Vocabulary](#2-vocabulary-stack) · [Mapping](#3-kfm--prov-mapping) · [Profile](#4-required-predicates-no-rename-rule) · [Evidence](#5-prov-in-the-evidencebundle) · [Catalog](#6-prov-in-artifacts-and-release-manifests) · [CRM](#7-prov-o-vs-cidoc-crm-e13) · [Adjacent](#8-prov-vs-openlineage-vs-slsa) · [Identity/time](#9-bitemporal--identity-rules) · [Validation](#10-validation-gates) · [Anti-patterns](#11-anti-patterns) · [Open work](#12-open-questions) · [References](#13-references)

---

<a id="0-current-repository-status-and-authority"></a>

## 0. Current repository status and authority

| Surface | CONFIRMED state | Does not establish |
|---|---|---|
| [`PROV.md`](./PROV.md), [`PROV-O.md`](./PROV-O.md), [`PROV/README.md`](./PROV/README.md) | Overlapping guidance and explicit conflict | Canonical profile |
| [`PROVENANCE.md`](./PROVENANCE.md) | Supply-chain/build provenance | Semantic PROV |
| [`EvidenceBundle`](../../contracts/evidence/evidence_bundle.md) and [schema](../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) | Proposed closed evidence object | PROV/PAV, policy, release |
| [`RunReceipt`](../../contracts/runtime/run_receipt.md) | Proposed immutable run output | A PROV Activity |
| [`OpenLineage projection`](../../contracts/telemetry/openlineage_run_event_projection.md) | Fixture-only no-network projection | Telemetry publication or PROV |
| [`Synthetic closure`](../../contracts/data/synthetic_release_catalog_closure_profile.md) | Seven-record STAC/DCAT/PROV agreement proof | RDF/OWL/JSON-LD or production release |
| [`data/catalog/prov/`](../../data/catalog/prov/README.md), [`data/prov/`](../../data/prov/README.md) | Placeholder and compatibility lanes | Released catalog/public endpoint |
| [`ADR-0022`](../adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) | Proposed | Adopted authority |

Specifications define PROV; contracts/schemas define KFM objects; evidence/policy support claims; validators prove bounded checks; review/release records govern transitions. This page owns none of those authorities.

---

<a id="1-purpose--scope"></a>

## 1. Purpose & scope

This page summarizes PROV-O, reconciles KFM object families, documents the synthetic proof, removes unsupported adoption claims, and states future evidence needs.

It does **not** select a canonical profile page, accept ADR-0022, mint ontology terms, change contracts/schemas, create validators/catalog records, activate graph stores/connectors, or authorize release, promotion, or publication.

---

<a id="2-vocabulary-stack"></a>

## 2. Vocabulary stack

| Class | Upstream role | KFM caution |
|---|---|---|
| `prov:Entity` | A thing with fixed aspects | A KFM artifact is not automatically an Entity |
| `prov:Activity` | Something occurring over time | A RunReceipt may evidence, but is not automatically, an Activity |
| `prov:Agent` | Something bearing responsibility | People/services/tools need role and privacy rules |

Common relations include `prov:used`, `prov:wasGeneratedBy`, `prov:wasDerivedFrom`, `prov:wasAssociatedWith`, `prov:wasAttributedTo`, and `prov:wasInformedBy`. This is upstream vocabulary, not a KFM-required subset.

PAV is separate authoring/versioning vocabulary (`http://purl.org/pav/`, documented version `2.3.1`). KFM has no verified PAV subset, context, schema, validator, migration, or producer/consumer contract.

> [!WARNING]
> A prefix is not adoption. A `prov:` key in JSON does not prove JSON-LD, RDF, valid PROV, accepted KFM shape, or release eligibility. Do not mint KFM terms inside `prov:` or `pav:`.

---

<a id="3-kfm--prov-mapping"></a>

## 3. KFM ↔ PROV mapping

These are **candidates**, not current requirements.

| KFM surface | Candidate role | Closure needed |
|---|---|---|
| Artifact/source | `prov:Entity` | Identity, digest, rights, sensitivity, lifecycle |
| Processing run | `prov:Activity` | ID, time, input/output and receipt binding |
| Human/service/tool | `prov:Agent` | Role, privacy, accountability |
| Run → input | `prov:used` | Resolved immutable input |
| Artifact → run | `prov:wasGeneratedBy` | Exact output/correction binding |
| Artifact → source | `prov:wasDerivedFrom` | Complete producing activity |
| Run/artifact → party | association or attribution | Distinct roles; no signature/approval collapse |

The prior page required every claim to carry `prov:wasGeneratedBy` and resolve to a RunReceipt. No current contract, schema, policy, validator, fixtures, or required workflow was verified as enforcing that rule. EvidenceRef → EvidenceBundle and policy boundaries remain authoritative.

---

<a id="4-required-predicates-no-rename-rule"></a>

## 4. Predicate and profile discipline

When KFM uses a PROV term, preserve the canonical W3C IRI and meaning. That does **not** establish the prior global fixed-subset/no-rename rule.

Adoption needs profile ownership/versioning, exact terms and constraints, serialization/context, identity/time, evidence/receipt/review/release bindings, rights/sensitivity, deterministic fixtures, producer/consumer negotiation, migration/replay, correction/withdrawal/rollback, and a governed public route.

---

<a id="5-prov-in-the-evidencebundle"></a>

## 5. PROV and EvidenceBundle

The closed EvidenceBundle schema requires `bundle_id`, `claim_scope`, `evidence_refs`, `source_records`, `citations`, `rights`, `sensitivity`, `transforms`, `checksums`, and `spec_hash`. It has no `@context`, `@graph`, `prov:*`, or `pav:*` field.

> [!IMPORTANT]
> An embedded PROV graph requires a versioned contract/schema change, validators, fixtures, compatibility analysis, and consumer migration. Documentation cannot add it.

A future design could reference or embed a versioned PROV artifact, or remain catalog-only. This page selects none. PROV describes lineage; it does not prove evidence, rights, sensitivity handling, policy, review, release, or publication.

---

<a id="6-prov-in-artifacts-and-release-manifests"></a>

## 6. PROV in catalog and release surfaces

The synthetic validator builds STAC Collection/Item, DCAT Dataset/Distribution, and PROV Entity/Activity/Agent records. They agree on identity, digest, extent, interval, source role, license, sensitivity, state, correction, rollback, and authored time.

Authority flags deny evidence grants, policy decisions, review approval, release authorization, publication, network use, and lifecycle writes.

This proves deterministic synthetic agreement and drift rejection—not RDF, OWL, PROV-N, JSON-LD, generic constraints, real data, live writes, public serving, or adoption. The `profile: "PROV"` record is a KFM projection, not a W3C RDF class.

---

<a id="7-prov-o-vs-cidoc-crm-e13"></a>

## 7. PROV-O and CIDOC CRM E13

The prior machine-versus-scholar split is unaccepted. No KFM mapping, examples, schema, or validator was verified. Future work must cover machine lineage, curatorial attribution, hybrid records, and correction without replacing E13 semantics.

---

<a id="8-prov-vs-openlineage-vs-slsa"></a>

## 8. PROV, OpenLineage, receipts, and supply-chain provenance

| Family | Current role | Does not prove |
|---|---|---|
| PROV | Semantic model plus synthetic projection | Evidence, policy, signatures, release |
| RunReceipt | Proposed immutable run output | Semantic PROV/truth |
| OpenLineage | Fixture-only operational projection | Telemetry delivery/PROV translation |
| Supply-chain provenance | Build attestations in [`PROVENANCE.md`](./PROVENANCE.md) | Domain evidence |
| EvidenceBundle | Proposed closed evidence object | Runtime or semantic graph |
| Release/correction/rollback | Govern transitions | Vocabulary conformance |

No generic translation was verified. Any mapping must be versioned, deterministic, loss-aware, tested, and explicit about omissions. Storage is not authority.

---

<a id="9-bitemporal--identity-rules"></a>

## 9. Identity, time, and canonicalization

No generic PROV identifier grammar was verified. Define IRIs, aliases, blank nodes, correction identity, dereference, collision, replay, and cross-profile rules before consumers stabilize.

Current checksums/spec hashes use `sha256:` plus 64 lowercase hexadecimal characters. JCS is a JSON canonicalization method, not part of the digest prefix. RDF canonicalization is separate.

Keep source/event, observation, validity, publication, retrieval, activity, catalog, review/release, and correction/withdrawal times distinct. No generic mapping of all facets to PROV time properties exists.

---

<a id="10-validation-gates"></a>

## 10. Validation and adoption gates

```bash
python tools/validators/catalog_closure/validate_synthetic_release_catalog_closure.py --fixtures
python tools/validators/validate_evidence_bundle.py
```

The first is not a generic PROV validator; the second validates only EvidenceBundle shape.

Adoption gates must close for authority, vocabulary, serialization, constraints, identity, evidence binding, time, rights/sensitivity, producers, consumers, catalog, release, correction, migration, and rollback. Negative fixtures must prove fail-closed malformed, missing, ambiguous, mismatched, restricted, temporal, correction, and legacy cases.

This page's checks cover metadata YAML, one H1, heading order, compatibility anchors, fences, fragments, relative links, placeholders/status claims, preserved identity, and no unrelated files. `docs-build` is a read-only readiness hold, not semantic/release/publication proof.

---

## 11. Illustrative semantic shape

```json
{
  "@context": { "prov": "http://www.w3.org/ns/prov#" },
  "@graph": [
    {
      "@id": "urn:example:artifact:alpha",
      "@type": "prov:Entity",
      "prov:wasGeneratedBy": { "@id": "urn:example:activity:build-alpha" }
    },
    {
      "@id": "urn:example:activity:build-alpha",
      "@type": "prov:Activity",
      "prov:used": { "@id": "urn:example:source:alpha" }
    }
  ]
}
```

Illustrative only: no KFM context, evidence binding, canonicalization, release, correction, or conformance is claimed.

---

## 12. Rights, sensitivity, correction, and rollback

Provenance can expose people, signers, topology, restricted sources, private endpoints, reviewers, parameters, or harmful precision. A profile must resolve rights/sensitivity, minimize disclosure, fail closed, prevent internal paths becoming public URLs, and use governed public routes.

Correction must preserve identities, derivation, attribution, supersession/withdrawal, public effects, and history. PROV may describe change; governed correction/rollback remains separate. Before merge, abandon/close the branch or PR; after merge, revert or forward-fix transparently.

---

<a id="11-anti-patterns"></a>

## 13. Anti-patterns

- Calling this page canonical.
- Adding PROV/PAV fields to a closed schema without versioning.
- Treating `profile: "PROV"` as RDF/PROV-O conformance.
- Using unverified contexts or minting KFM terms in external namespaces.
- Collapsing PROV, RunReceipt, OpenLineage, EvidenceBundle, or attestations.
- Inferring truth from lineage or authority from storage.
- Collapsing distinct times or exposing identities/precision by default.
- Treating validators, PRs, signatures, or projections as release.
- Hand-editing generated projections or creating parallel authority.

---

<a id="12-open-questions"></a>

## 14. Open questions

| Topic | Required follow-up |
|---|---|
| Profile owner and canonical page | Maintainer decision preserving supply-chain/compatibility boundaries |
| Serialization, terms, constraints | Versioned contract, context/shape, parser and negative fixtures |
| EvidenceBundle/RunReceipt binding | One versioned identity/resolution design |
| OpenLineage and CRM E13 mappings | Loss-aware field mapping and hybrid cases |
| Identity, time, canonicalization | Stable grammar and correction fixtures |
| Restricted identities/precision | Policy-backed public/private projection |
| ADR-0022 and catalog adoption | Maintainer review without fixture-as-adoption |
| Persisted consumers and migration | Inventory, compatibility, rollback |
| Release/correction bindings | Dependency-closed design and rehearsal |

No unresolved item authorizes speculative implementation.

---

## 15. Material-change ledger

| Prior element | Disposition |
|---|---|
| ID, date, path, H1 and numbered fragments | **KEEP / COMPATIBILITY** |
| PROV/PAV vocabulary and KFM mapping | **CLARIFY / REPAIR** as upstream and candidates |
| Universal generator edge/fixed subset | **REMOVE / CLARIFY**; no enforcement |
| Embedded EvidenceBundle graph | **REMOVE WITH EVIDENCE** |
| Digest/context examples | **REPAIR** |
| Catalog mapping | **ENRICH** with synthetic proof |
| Adjacent families, time, rights, correction | **KEEP / ENRICH** |
| Briefing references, fake URLs, unmounted caveats | **REMOVE WITH EVIDENCE** |
| Four-surface conflict | **SURFACE CONFLICT**; no rename/winner |

---

<a id="13-references"></a>

## 16. References

**Upstream:** [PROV-O](https://www.w3.org/TR/prov-o/) · [PROV Overview](https://www.w3.org/TR/prov-overview/) · [PROV-DM](https://www.w3.org/TR/prov-dm/) · [PROV Constraints](https://www.w3.org/TR/prov-constraints/) · [PROV-N](https://www.w3.org/TR/prov-n/) · [PAV](https://pav-ontology.github.io/pav/)

**Repository:** [`PROV/README.md`](./PROV/README.md) · [`PROV-O.md`](./PROV-O.md) · [`PROVENANCE.md`](./PROVENANCE.md) · [`OPENLINEAGE_FACETS.md`](./OPENLINEAGE_FACETS.md) · [`RUN_RECEIPT.md`](./RUN_RECEIPT.md) · [`EVIDENCE_BUNDLE.md`](./EVIDENCE_BUNDLE.md) · [EvidenceBundle](../../contracts/evidence/evidence_bundle.md) and [schema](../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) · [RunReceipt](../../contracts/runtime/run_receipt.md) · [OpenLineage](../../contracts/telemetry/openlineage_run_event_projection.md) · [synthetic closure](../../contracts/data/synthetic_release_catalog_closure_profile.md), [projection](../../tools/validators/catalog_closure/_synthetic_release_catalog_closure_projection.py), and [validator](../../tools/validators/catalog_closure/validate_synthetic_release_catalog_closure.py) · [`data/catalog/prov/`](../../data/catalog/prov/README.md) · [`data/prov/`](../../data/prov/README.md) · [ADR-0022](../adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md)

<a id="related-docs"></a>

## Related docs

[`STAC.md`](./STAC.md) · [`DCAT.md`](./DCAT.md) · [`SIGNING.md`](./SIGNING.md) · [`lifecycle-law.md`](../doctrine/lifecycle-law.md) · [`trust-membrane.md`](../doctrine/trust-membrane.md) · [`directory-rules.md`](../doctrine/directory-rules.md)

---

*Last updated: 2026-08-18 · Status: draft, repository-grounded, no adopted PROV profile · [Back to top](#top)*
