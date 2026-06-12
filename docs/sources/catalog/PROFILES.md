<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-profiles
title: Source catalog profiles register
type: register
version: v0.3
status: draft
owners: Docs steward · Source steward · Catalog profile owner
created: 2026-05-20
updated: 2026-06-12
policy_label: public
related:
  - docs/sources/catalog/README.md
  - docs/sources/catalog/CROSSWALKS.md
  - docs/sources/catalog/IDENTITY.md
  - docs/sources/catalog/GLOSSARY.md
  - docs/sources/catalog/OPEN-QUESTIONS.md
  - docs/sources/catalog/CARE-COMPLIANCE.md
  - docs/standards/STAC.md
  - docs/standards/DCAT.md
  - docs/standards/PROV.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/truth-posture.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/architecture/contract-schema-policy-split.md
  - schemas/contracts/v1/source/
tags: [kfm, docs, sources, catalog, register, profiles, stac, dcat, prov, provenance, care, attestation]
notes:
  - "v0.3 — optimized authority boundary. This file is a pointer register and catalog-lane coordination surface, not the authoritative source for external standard profile content, object meaning, machine-checkable schema shape, policy decisions, or release decisions."
  - "External standards profile content belongs in docs/standards/. KFM object meaning belongs in contracts/. Machine-checkable shape belongs in schemas/. Policy/admissibility decisions belong in policy/ and release/. This register points across those homes and records catalog-lane obligations."
  - "v0.3 downgrades unverified repo-path and sibling-link claims to NEEDS VERIFICATION unless supported by mounted-repo evidence, current repo scan, accepted ADR, or generated artifact."
  - "v0.3 retains the v0.2 doctrinal correction: type remains register, not profile."
  - "v0.3 keeps ADR-0014 for temporal vocabulary as NEEDS VERIFICATION. The six time-kinds vocabulary remains doctrine-supported; the specific ADR identifier must be reconciled against the active ADR ledger."
  - "Atlas anchors retained: KFM-P31-PROG-0004, KFM-P14-IDEA-0002, KFM-P14-PROG-0008, KFM-P7-PROG-0001, KFM-P10-PROG-0003, Pass-10 C4-01..05, C8-03, C15-01..03."
[/KFM_META_BLOCK_V2] -->

Source catalog profiles register

Pointer register for the external metadata-standard profiles the source-catalog lane relies on — STAC, DCAT, and PROV-O — plus the KFM-namespaced extension obligations that must be carried through catalog, evidence, policy, release, and UI surfaces.

Status: draft scaffold
Type: register, not profile
Last reviewed: 2026-06-12
Truth posture: doctrine-supported register · implementation paths NEEDS VERIFICATION unless separately confirmed

⸻

Quick jump

* Purpose
* Non-authority boundary
* Authority map
* Profiles register
* KFM-namespaced extension obligations
* Temporal vocabulary: six time-kinds
* Placement model
* Maintenance rules
* Validation checklist
* Open questions
* Related docs

⸻

Purpose

This register answers one operational question:

For each external metadata standard used by the source-catalog lane, where is the authoritative KFM profile, and which KFM extension obligations must travel with catalog records, evidence references, receipts, policy decisions, release manifests, and public UI payloads?

This file exists so catalog maintainers do not have to rediscover the same crosswalk every time a STAC Item, DCAT Dataset, PROV-O graph, EvidenceBundle, ReleaseManifest, or MapLibre layer payload is created.

It records:

1. Which external standards are in scope: STAC, DCAT, and PROV-O.
2. Where their authoritative KFM profile documents should live.
3. Which KFM extension obligations must be carried consistently.
4. Which claims are CONFIRMED doctrine, which are PROPOSED, and which require mounted-repo or ADR verification.
5. Which open questions block promotion from scaffold to stable register.

⸻

Non-authority boundary

This register is deliberately narrow.

It does not define external standards.
It points to the KFM profile docs under docs/standards/.

It does not define KFM object meaning.
Meaning belongs in contracts/.

It does not define machine-checkable JSON Schema shape.
Shape belongs in schemas/contracts/v1/....

It does not decide allow, deny, restrict, redact, delay, or publish.
Admissibility and release decisions belong in policy/ and release/.

It does not prove current implementation.
Any route name, file existence, validator behavior, CI enforcement, release artifact, or runtime behavior is NEEDS VERIFICATION unless confirmed by mounted-repo evidence, generated receipts, logs, tests, dashboards, or accepted ADRs.

This file is a coordination register. It keeps the catalog lane aligned with the standards lane, schema lane, policy lane, evidence lane, release lane, and public UI lane.

⸻

Authority map

Concern	Canonical owner	This file’s role	Status
External profile prose for STAC, DCAT, PROV-O	docs/standards/	Points to profile docs	CONFIRMED doctrine / file existence NEEDS VERIFICATION
KFM object meaning	contracts/	Points to contract owner	CONFIRMED doctrine
Machine-checkable object shape	schemas/contracts/v1/...	Points to schema owner	CONFIRMED doctrine
Source identity, rights, sensitivity	data/registry/ + source descriptors + policy review	Records catalog dependency	CONFIRMED doctrine / specific paths NEEDS VERIFICATION
Policy decisions	policy/	Records required policy linkage	CONFIRMED doctrine
Release, rollback, correction	release/	Records required release linkage	CONFIRMED doctrine
STAC/DCAT/PROV catalog outputs	data/catalog/... lifecycle lane	Records expected catalog lanes	CONFIRMED lifecycle phase / specific folder shape NEEDS VERIFICATION
EvidenceBundle and receipts	evidence/proof/receipt homes per accepted repo convention	Records required references	CONFIRMED doctrine / exact homes NEEDS VERIFICATION
Public MapLibre/UI payloads	governed API + released artifacts	Records downstream obligations	CONFIRMED doctrine / implementation UNKNOWN

Placement correction inherited from v0.2

Earlier versions risked treating this file as a profile. That was corrected.

This document is a register in the source-catalog docs lane. External standards profile content belongs in docs/standards/. KFM object contracts and schemas remain under their own governance roots.

⸻

Profiles register

The catalog lane relies on three external standards. Each profile below is a pointer entry, not a full profile definition.

1. KFM-STAC profile

Field	Register value	Status
Base standard	STAC	CONFIRMED external standard dependency
Intended version pin	STAC 1.1.x	PROPOSED / NEEDS VERIFICATION
Authoritative KFM profile doc	docs/standards/STAC.md	PROPOSED file / placement doctrine-supported
Machine-readable schema home	schemas/contracts/v1/catalog/stac/... or accepted repo equivalent	PROPOSED / NEEDS ADR or repo verification
Catalog output lane	data/catalog/stac/...	PROPOSED path / lifecycle phase supported
Collection ID convention	kfm-<org>-<product>	PROPOSED / verify against IDENTITY.md
Item identity	deterministic identity from source identity + spec_hash	PROPOSED / doctrine-supported
Required external extensions	projection, processing, file	PROPOSED / verify against STAC profile
KFM extension obligations	kfm:provenance, kfm:care when applicable, attestation link	PROPOSED register obligation
Required public posture	STAC is catalog metadata, not publication approval	CONFIRMED doctrine

Minimum profile coverage expected in docs/standards/STAC.md:

* version pin and migration rule;
* conformance classes;
* extension list;
* Collection ID rules;
* Item identity and spec_hash rules;
* asset role vocabulary;
* MIME/media-type policy;
* file:checksum and per-asset integrity;
* kfm:provenance carriage;
* kfm:care carriage where applicable;
* attestation link relation posture;
* validation fixtures and expected failure cases.

2. KFM-DCAT profile

Field	Register value	Status
Base standard	W3C DCAT	CONFIRMED external standard dependency
Intended version pin	DCAT 3	PROPOSED / NEEDS VERIFICATION
Authoritative KFM profile doc	docs/standards/DCAT.md	PROPOSED file / placement doctrine-supported
Machine-readable schema home	schemas/contracts/v1/catalog/dcat/... or accepted repo equivalent	PROPOSED / NEEDS ADR or repo verification
Catalog output lane	data/catalog/dcat/...	PROPOSED path / lifecycle phase supported
Core model	Dataset → Distribution(s)	CONFIRMED standard pattern / KFM mapping PROPOSED
Distribution obligations	checksum, byte size, media type, version, license, rights holder, provenance links	PROPOSED
KFM extension obligations	kfm:care at Dataset level where applicable; provenance at Dataset or Distribution level per profile	PROPOSED / NEEDS VERIFICATION
Required public posture	DCAT is harvest/discovery metadata, not publication approval	CONFIRMED doctrine

Minimum profile coverage expected in docs/standards/DCAT.md:

* Dataset and Distribution mapping;
* version and release mapping;
* license and rights-holder rules;
* DOI or persistent identifier posture;
* EvidenceBundle and ReleaseManifest references;
* STAC → DCAT JSON-LD mapping;
* distribution checksums and byte sizes;
* kfm:care exposure rule;
* policy and sensitivity warning fields;
* harvest and correction timestamps.

3. KFM-PROV profile

Field	Register value	Status
Base standard	W3C PROV-O	CONFIRMED external standard dependency
Adjacent vocabulary	PAV where useful	PROPOSED / NEEDS VERIFICATION
Intended version pin	PROV-O 1.0	PROPOSED / NEEDS VERIFICATION
Authoritative KFM profile doc	docs/standards/PROV.md	PROPOSED file / placement doctrine-supported
Machine-readable schema home	schemas/contracts/v1/catalog/prov/... or accepted repo equivalent	PROPOSED / NEEDS ADR or repo verification
Catalog output lane	data/catalog/prov/...	PROPOSED path / lifecycle phase supported
Core mapping	RunReceipt → Activity; EvidenceBundle → Entity; tool/operator/system → Agent	PROPOSED / doctrine-supported
Key relations	prov:used, prov:generated, prov:wasAssociatedWith, prov:wasAttributedTo, prov:wasGeneratedBy	PROPOSED
Serialization	JSON-LD	PROPOSED
Canonicalization	JCS by default for KFM object hashing; URDNA2015 reserved for RDF semantic equivalence	PROPOSED / NEEDS ADR
Required public posture	PROV lineage explains evidence flow; it does not override policy or release state	CONFIRMED doctrine

Minimum profile coverage expected in docs/standards/PROV.md:

* KFM object-family mapping;
* activity/entity/agent identity;
* JSON-LD context strategy;
* canonicalization and hash discipline;
* relation vocabulary;
* time-kind mapping;
* EvidenceBundle, RunReceipt, AIReceipt, ReleaseManifest, and CorrectionNotice linkage;
* Neo4j/triplet projection constraints;
* round-trip checks between STAC/DCAT/PROV.

⸻

KFM-namespaced extension obligations

The following are KFM-specific extension obligations. This register records their catalog-lane carriage requirements, but their meaning, schema, and policy effects must be defined in the appropriate authority roots.

Extension ownership table

Extension	Catalog carriage	Meaning owner	Shape owner	Policy owner	Status
kfm:provenance	STAC Item properties; DCAT Distribution or Dataset; PROV linkage	contracts/	schemas/contracts/v1/...	policy/ + release/	PROPOSED / doctrine-supported
kfm:care	STAC properties and DCAT Dataset where applicable	contracts/	schemas/contracts/v1/...	policy/sensitivity/ or accepted equivalent	PROPOSED / default-deny doctrine-supported
KFM attestation link relation	STAC links[]; DCAT distribution relation; release/proof linkage	contracts/	schemas/contracts/v1/...	release/ + proof policy	PROPOSED / rel registration NEEDS VERIFICATION

kfm:provenance carriage obligation

When a catalog object depends on evidence or emitted artifacts, it should carry or resolve to the following provenance fields.

Field	Expected value	Register posture
spec_hash	canonical hash of the record or governed artifact	PROPOSED
evidence_bundle_ref	resolvable EvidenceBundle URI	PROPOSED
run_record_ref	RunReceipt or pipeline run record URI	PROPOSED
audit_ref	audit/proof/attestation reference	PROPOSED
policy_digest	digest of policy bundle used for decision or promotion	PROPOSED
per-asset checksum	file:checksum or asset-specific checksum field	PROPOSED

Required guardrail:

A catalog record carrying kfm:provenance must not imply public release. It only records provenance linkage. Public release still depends on validation, policy, review, release manifest, correction path, and rollback target.

kfm:care carriage obligation

When a source, dataset, feature, layer, or evidence bundle carries Indigenous, cultural, community, stewardship, consent, or authority-to-control concerns, catalog records must preserve that signal without exposing restricted details.

Expected fields:

Field	Meaning	Publication posture
steward_org	community, nation, organization, or steward body	restrict/redact if sensitive
authority_to_control	asserted authority/control interest	non-empty triggers default-deny review
consent	ConsentSidecar or consent record reference	never infer consent from absence
obligations	stewardship or use obligations	preserve through release
benefit_commitments	benefit-sharing or return obligations	preserve through release
access_tier	public, staged, restricted, denied, or steward-review	policy-owned
redaction_reason	reason exact data is withheld/generalized	required when transformed

Required guardrail:

kfm:care is not decorative metadata. If it indicates authority-to-control, cultural sensitivity, consent requirements, or community obligations, publication must fail closed until policy and review state permit release.

KFM attestation link relation

A catalog object may include a KFM attestation link relation that points to an EvidenceBundle, proof bundle, DSSE/cosign-style attestation, or ReleaseManifest entry.

Proposed STAC link shape:

{
  "rel": "kfm:attestation",
  "href": "kfm://evidence/<digest-or-id>",
  "type": "application/json",
  "title": "KFM attestation and evidence bundle"
}

Notes:

* rel: "attestation" without a namespace is NEEDS VERIFICATION against upstream STAC link relation registration.
* Until registration is confirmed, prefer kfm:attestation.
* The namespace prefix itself remains open under the namespace-pin question.
* The link must not bypass evidence, policy, review, or release checks.

Namespace pin

Current provisional namespace: kfm:.

Open alternative: ks-kfm:.

The final namespace decision affects:

* STAC extension fields;
* DCAT JSON-LD context;
* PROV JSON-LD context;
* schema property names;
* validators;
* public API payloads;
* layer manifests;
* Evidence Drawer fields;
* Focus Mode citations;
* docs examples;
* released catalog records.

No mass rename should occur without an accepted ADR and migration plan.

⸻

Temporal vocabulary: six time-kinds

KFM keeps six time-kinds distinct where material.

#	Time-kind	What it pins	Example
1	source time	When the publisher/source recorded or issued the data	date on agency source record
2	observed time	When the real-world event, condition, or measurement occurred	stream gauge measurement time
3	valid time	Interval during which the assertion applies	regulatory boundary effective dates
4	retrieval time	When KFM fetched or received the artifact	connector fetch receipt timestamp
5	release time	When KFM released the derived artifact	ReleaseManifest timestamp
6	correction time	When a correction notice was issued	CorrectionNotice timestamp

Required rule:

These time-kinds are not interchangeable. Collapsing them weakens evidence, rollback, correction, source drift detection, temporal filtering, and public explanation.

Register posture:

* The six time-kinds are doctrine-supported.
* The specific historical reference to ADR-0014 remains NEEDS VERIFICATION.
* A future accepted ADR should pin field names, JSON-LD mappings, STAC/DCAT/PROV placement, and UI vocabulary.

Recommended carriage by profile:

Time-kind	STAC	DCAT	PROV-O	KFM receipt/release object
source	source-specific property or provider metadata	issued/modified/source note	Entity attribution metadata	SourceDescriptor / RetrievalReceipt
observed	datetime, start_datetime, end_datetime	temporal coverage	Entity time or qualified relation	Observation record
valid	temporal interval properties	temporal coverage	validity interval extension	Assertion / rule record
retrieval	kfm:provenance.run_record_ref	harvest metadata	Activity time	RunReceipt
release	linked ReleaseManifest	distribution issued date	generated activity time	ReleaseManifest
correction	linked CorrectionNotice	modified/correction note	invalidation/revision relation	CorrectionNotice

⸻

Placement model

flowchart LR
  subgraph Doctrine["Doctrine and authority"]
    DR["docs/doctrine/directory-rules.md"]
    SPLIT["contract-schema-policy split"]
    LIFE["lifecycle law"]
  end
  subgraph Standards["External profile docs"]
    STAC["docs/standards/STAC.md"]
    DCAT["docs/standards/DCAT.md"]
    PROV["docs/standards/PROV.md"]
  end
  subgraph Register["This register"]
    REG["docs/sources/catalog/PROFILES.md"]
    EXT["extension obligations"]
    TIME["six time-kinds"]
    OPEN["open questions"]
  end
  subgraph AuthorityRoots["Authority roots"]
    CONTRACTS["contracts/"]
    SCHEMAS["schemas/contracts/v1/"]
    POLICY["policy/"]
    RELEASE["release/"]
  end
  subgraph DataLifecycle["Catalog lifecycle outputs"]
    CSTAC["data/catalog/stac/"]
    CDCAT["data/catalog/dcat/"]
    CPROV["data/catalog/prov/"]
  end
  DR --> Register
  DR --> Standards
  SPLIT --> AuthorityRoots
  LIFE --> DataLifecycle
  REG --> STAC
  REG --> DCAT
  REG --> PROV
  REG --> EXT
  REG --> TIME
  REG --> OPEN
  EXT --> CONTRACTS
  EXT --> SCHEMAS
  EXT --> POLICY
  EXT --> RELEASE
  STAC --> CSTAC
  DCAT --> CDCAT
  PROV --> CPROV
  CONTRACTS -. meaning .-> EXT
  SCHEMAS -. shape .-> EXT
  POLICY -. admissibility .-> EXT
  RELEASE -. publication state .-> EXT

Interpretation:

* docs/standards/ owns external profile prose.
* This register points at those profiles.
* This register records cross-profile catalog obligations.
* contracts/, schemas/, policy/, and release/ remain the authority roots for meaning, shape, decisions, and publication state.
* data/catalog/... carries lifecycle outputs after validation and promotion gates.

⸻

Maintenance rules

This register must be updated whenever one of the following changes lands.

Trigger	Required update
STAC, DCAT, or PROV version pin changes	Update profile row, add migration note, link accepted ADR or drift entry
docs/standards/STAC.md, DCAT.md, or PROV.md lands or moves	Update profile status and related links
kfm:provenance field changes	Update extension obligation table; link contract/schema/policy changes
kfm:care field changes	Coordinate with CARE-COMPLIANCE.md; update policy linkage
namespace pin resolves	Replace provisional prefix; add migration checklist
attestation rel is registered upstream	Update link relation rule and validator expectation
six time-kinds ADR lands	Replace ADR NEEDS VERIFICATION note with accepted ADR reference
schema home changes	Do not edit this file alone; require ADR and update schema-home references
policy gate changes	Update policy owner references and validation checklist
catalog output lanes move	Record drift, ADR, migration, and rollback path

Version rule:

* Keep v0.x while namespace pin, profile doc existence, and ADR references remain unresolved.
* Move to v1.0 only after:
    * the three standards profile docs exist and are reviewed;
    * namespace pin is accepted;
    * attestation relation posture is accepted;
    * the schema/contract/policy split is reflected in actual files;
    * validators and fixtures exist for at least one STAC, one DCAT, and one PROV example.

⸻

Validation checklist

Before promoting this register beyond draft, run or complete the following checks.

Check	Expected result	Status
Confirm docs/standards/STAC.md exists	profile doc present and reviewed	NEEDS VERIFICATION
Confirm docs/standards/DCAT.md exists	profile doc present and reviewed	NEEDS VERIFICATION
Confirm docs/standards/PROV.md exists	profile doc present and reviewed	NEEDS VERIFICATION
Confirm PROV.md vs PROVENANCE.md naming	one canonical name or ADR	NEEDS VERIFICATION
Confirm source catalog sibling links	README, CROSSWALKS, IDENTITY, GLOSSARY, OPEN-QUESTIONS, CARE-COMPLIANCE	NEEDS VERIFICATION
Confirm schema homes for catalog profiles	under accepted schema root	NEEDS VERIFICATION
Confirm source descriptor schema home	under accepted source schema root	NEEDS VERIFICATION
Confirm kfm:provenance fixture	valid and invalid fixture present	NEEDS VERIFICATION
Confirm kfm:care fixture	default-deny case present	NEEDS VERIFICATION
Confirm attestation fixture	link relation and evidence resolution tested	NEEDS VERIFICATION
Confirm six time-kind fixture	source/observed/valid/retrieval/release/correction distinction tested	NEEDS VERIFICATION
Confirm STAC → DCAT mapping fixture	JSON-LD output validates	NEEDS VERIFICATION
Confirm STAC/DCAT/PROV round trip	no evidence or release reference lost	NEEDS VERIFICATION
Confirm no public UI bypass	public payload resolves through governed API and released artifacts	NEEDS VERIFICATION

⸻

Open questions

Canonical numbering lives in docs/sources/catalog/OPEN-QUESTIONS.md. IDs below are retained as register-local references until confirmed there.

ID	Question	Status
OPEN-DSC-03	Namespace pin: kfm: vs ks-kfm:	OPEN
OPEN-DSC-05	STAC vs DCAT disposition for spatiotemporal datasets that can fit either model	NEEDS VERIFICATION
OPEN-DSC-06	Pointer register placement: keep this file in docs/sources/catalog/ while profiles live in docs/standards/?	OPEN
OPEN-DSC-12-NV	Reconcile ADR-0014 temporal-vocabulary reference against active ADR ledger	NEEDS VERIFICATION
OPEN-DSC-29	STAC version-pin migration: all-at-once or per-Collection migration?	PROPOSED ALLOCATION
OPEN-DSC-30	Asset-role and MIME/media-type enumeration: prose only, schema artifact, or both?	PROPOSED ALLOCATION
OPEN-DSC-31	KFM attestation rel: upstream registration, KFM-local namespace, or both?	PROPOSED ALLOCATION
OPEN-DSC-32	PROV-O ↔ CIDOC CRM / CIDOC E13 boundary for cultural-heritage lineage	PROPOSED ALLOCATION
OPEN-DSC-33	Which catalog fields must be mirrored into public API payloads versus only resolvable through Evidence Drawer?	PROPOSED ALLOCATION
OPEN-DSC-34	Which KFM extension obligations are mandatory for context-only layers?	PROPOSED ALLOCATION

Allocation warning:

Proposed IDs must not be treated as canonical until entered into OPEN-QUESTIONS.md and checked for collisions.

⸻

Related docs

* docs/sources/catalog/README.md — catalog lane overview
* docs/sources/catalog/CROSSWALKS.md — cross-format mapping register
* docs/sources/catalog/IDENTITY.md — source, collection, item, namespace, and promotion identity guidance
* docs/sources/catalog/GLOSSARY.md — catalog vocabulary
* docs/sources/catalog/CARE-COMPLIANCE.md — CARE and stewardship surfacing rules
* docs/sources/catalog/OPEN-QUESTIONS.md — canonical OPEN-DSC-* register
* docs/standards/STAC.md — KFM-STAC profile
* docs/standards/DCAT.md — KFM-DCAT profile
* docs/standards/PROV.md — KFM-PROV profile
* docs/standards/ISO-19115.md — adjacent profile / crosswalk target
* docs/standards/OGC-API-TILES.md — adjacent tile-service profile
* docs/standards/PMTILES.md — adjacent artifact/profile consumer
* contracts/ — object-family meaning
* schemas/contracts/v1/ — machine-checkable shapes
* policy/ — allow/deny/restrict/abstain controls
* release/ — release, correction, rollback, and publication state
* data/catalog/ — lifecycle catalog outputs
* docs/doctrine/directory-rules.md — placement authority
* docs/registers/DRIFT_REGISTER.md — drift tracking
* docs/adr/ — accepted and proposed architecture decisions

⸻

Final status

Document status: draft register, v0.3
Primary correction: authority boundary clarified
Primary remaining blockers: repo verification, profile doc existence, namespace pin, attestation rel posture, schema fixture coverage, temporal ADR reconciliation
Publication posture: public docs scaffold only; not a release artifact, not implementation proof, not profile authority, not policy authority

Back to top