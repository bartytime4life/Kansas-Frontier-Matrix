<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/3cbf1956-c8bd-44a0-b624-82f3dfb22160
title: KFM Glossary
type: standard
version: v1.1
status: draft
owners: KFM Maintainers
created: 2026-03-04
updated: 2026-03-05
policy_label: public
related: []
tags: [kfm]
notes: [Shared definitions for KFM docs and system surfaces. Each entry includes status: CONFIRMED/PROPOSED/UNKNOWN.]
[/KFM_META_BLOCK_V2] -->

# KFM Glossary
Shared definitions for terms used across Kansas Frontier Matrix (KFM) docs, pipelines, policy, APIs, and UI.

> **Status:** active (draft)  
> **Owners:** KFM Maintainers (TODO: add GitHub handles / team)  
> **Policy label:** public  
>
> ![KFM Glossary badge](https://img.shields.io/badge/KFM-Glossary-blue)
> ![Status badge](https://img.shields.io/badge/Status-Draft-yellow)
> ![Policy badge](https://img.shields.io/badge/Policy-Public-success)
>
> **Quick links:** [How to use](#how-to-use-this-glossary) · [Conventions](#conventions) · [Abbreviations](#abbreviations) · [Glossary A–Z](#glossary-a-z) · [Contributing](#contributing) · [Sources](#sources)

---

## How to use this glossary

- Use these definitions in *governed docs* (standards, contracts, runbooks) and UI copy.
- If a term is overloaded in other domains, prefer the KFM definition **inside KFM**.
- When adding a new term, include:
  - **Status** (CONFIRMED / PROPOSED / UNKNOWN)
  - A crisp definition (1–3 sentences)
  - “See also” pointers to related terms

## Conventions

### Status meanings

- **CONFIRMED** — The meaning is explicitly described in KFM design/guide documents and treated as a stable semantic contract (even if not yet implemented everywhere).
- **PROPOSED** — The meaning appears as a recommended direction (e.g., blueprints/idea packs) but should be treated as changeable until ratified.
- **UNKNOWN** — The term is used but KFM meaning is ambiguous; it needs a defining spec link (or governance review).

### “Glossary ≠ implementation” guardrail

- This glossary defines **terms and intent**. It must not be used as proof that a module exists or is deployed.
- If a definition would imply specific code/repo structure, prefer wording like “**target module**”, “**intended surface**”, or mark it **UNKNOWN** until repo verification.

### Cross-references

- “See also” references are internal hyperlinks within this file.
- External standards (STAC/DCAT/PROV, etc.) are referenced conceptually; KFM profiles may further constrain them.

## Where this fits

> **Note:** This section describes intended repository placement and doc relationships. If your repo differs, update accordingly.

- **Recommended path:** `docs/glossary.md` (**UNKNOWN** until repo-verified)
- **Upstream (conceptual):** governance/policy docs, schema registries/profiles, ADRs
- **Downstream (conceptual):** Story Nodes, Focus Mode prompts/outputs, API contracts, pipeline specs, docs-lint rules

## Acceptable inputs

- New glossary entries for:
  - KFM-specific concepts (e.g., Promotion Contract, Trust membrane)
  - Standard acronyms used in KFM governance (e.g., SBOM, SLSA)
  - Data lifecycle zone terminology (RAW/WORK/QUARANTINE/PROCESSED/CATALOG/PUBLISHED)

## Exclusions

- **Do not** put policy decisions here (belongs in governance/policy docs).
- **Do not** define schemas here (belongs in `schemas/` / profile docs).
- **Do not** claim a module exists/works unless verified by:
  - a governed release note, **or**
  - a repo contract/test demonstrating it.

## Diagram

```mermaid
flowchart LR
  Upstream[Upstream sources] --> RAW[RAW zone]
  RAW --> WORK[WORK zone]
  WORK --> QUAR[QUARANTINE]
  WORK --> PROCESSED[PROCESSED zone]
  PROCESSED --> CATALOG[CATALOG triplet]
  CATALOG --> PUBLISHED[PUBLISHED surfaces]

  UI[UI clients] --> PEP[Governed API PEP]
  PEP --> PDP[Policy engine PDP]
  PEP --> ER[Evidence resolver]
  ER --> PEP
  PDP --> PEP
```

---

## Abbreviations

| Acronym | Expansion | Notes |
|---|---|---|
| CARE | Collective Benefit, Authority to Control, Responsibility, Ethics | Often paired with FAIR in KFM governance (“FAIR+CARE”). |
| CI | Continuous Integration | Promotion/publishing rules are designed to be enforceable as CI gates. |
| COG | Cloud Optimized GeoTIFF | Raster format optimized for HTTP range requests. |
| DCAT | Data Catalog Vocabulary | Dataset-level metadata surface in the KFM “triplet.” |
| JCS | JSON Canonicalization Scheme | Used for deterministic hashing (e.g., `spec_hash`). |
| OPA | Open Policy Agent | Policy engine; Rego language. |
| ORAS | OCI Registry As Storage | Used for pushing non-container artifacts to OCI registries. |
| PEP | Policy Enforcement Point | The gateway where policy is enforced (e.g., governed API). |
| PDP | Policy Decision Point | The component that produces allow/deny + obligations. |
| PMTiles | Portable Map Tiles | Single-file tile archive for fast distribution. |
| PROV | W3C Provenance model | Lineage surface in the KFM “triplet.” |
| SBOM | Software Bill of Materials | SPDX/CycloneDX are common formats. |
| SLSA | Supply-chain Levels for Software Artifacts | Used with attestations (often in-toto). |
| STAC | SpatioTemporal Asset Catalog | Asset-level metadata surface in the KFM “triplet.” |

---

## Glossary A–Z

### A

#### Acquisition manifest
- **Status:** CONFIRMED
- **Definition:** A record describing what was fetched/snapshotted from an upstream source, when, and under what terms. In KFM, acquisition manifests live with RAW artifacts as part of the auditable “truth path.”
- **See also:** [RAW zone](#raw-zone), [License snapshot](#license-snapshot)

#### Audit ref
- **Status:** CONFIRMED
- **Definition:** A stable reference to an audit-log/ledger entry associated with an action or output (e.g., a run receipt, a promotion manifest, or an EvidenceBundle). `audit_ref` exists so the UI/API can point to an auditable record without guessing.
- **See also:** [EvidenceBundle](#evidencebundle), [Run receipt](#run-receipt), [Promotion manifest](#promotion-manifest)

#### Allowlist
- **Status:** PROPOSED
- **Definition:** A set of explicitly permitted values (e.g., licenses, file types, domains, tool calls) used by policy checks. Anything not allowlisted is denied by default.
- **See also:** [Default-deny](#default-deny), [Fail-closed](#fail-closed)

---

### C

#### CARE
- **Status:** CONFIRMED
- **Definition:** CARE Principles for Indigenous Data Governance: **Collective Benefit, Authority to Control, Responsibility, Ethics**. In KFM, CARE appears as a governance lens alongside FAIR, especially when handling sensitive data and obligations.
- **See also:** [FAIR](#fair), [FAIR+CARE](#faircare), [Sensitivity classification](#sensitivity-classification)

#### Canonical layout
- **Status:** PROPOSED
- **Definition:** A documented object-storage path convention for storing RAW/WORK/PROCESSED/CATALOG artifacts so the “truth path” is navigable without depending on database state. The exact directory structure is a proposed contract and should be versioned if adopted.
- **See also:** [Truth path](#truth-path), [Projection store](#projection-store), [RAW zone](#raw-zone), [PROCESSED zone](#processed-zone)

#### Catalog triplet
- **Status:** CONFIRMED
- **Definition:** The cross-linked metadata surfaces that together describe a dataset version:
  - **DCAT** for dataset-level metadata,
  - **STAC** for asset-level spatiotemporal metadata,
  - **PROV** for lineage (how artifacts were produced).
  If the triplet is missing or inconsistent, promotion/publishing should fail.
- **See also:** [DCAT](#dcat), [STAC](#stac), [PROV](#prov), [Promotion Contract](#promotion-contract)

#### Citation handshake
- **Status:** PROPOSED
- **Definition:** A requirement that user-facing outputs (especially Focus Mode and Story publishing) include structured, resolvable citations to dataset versions and evidence artifacts (not just free-text references).
- **See also:** [Cite-or-abstain](#cite-or-abstain), [EvidenceRef](#evidenceref), [EvidenceBundle](#evidencebundle)

#### Cite-or-abstain
- **Status:** CONFIRMED
- **Definition:** A behavior rule: if the system cannot produce valid citations/evidence references for a factual claim, it must refuse or clearly mark the response as unknown rather than guessing.
- **See also:** [Focus Mode](#focus-mode), [Evidence resolver](#evidence-resolver), [Story Node](#story-node)

#### Conftest
- **Status:** PROPOSED
- **Definition:** A tool commonly used to run OPA/Rego policies against structured inputs during CI to enforce “policy as code.”
- **See also:** [OPA](#opa), [Policy engine](#policy-engine), [Policy regression suite](#policy-regression-suite)

---

### D

#### Data lifecycle zones
- **Status:** CONFIRMED
- **Definition:** KFM’s governed storage/promotion stages: **RAW → WORK/QUARANTINE → PROCESSED → CATALOG (triplet) → PUBLISHED**. These zones are treated as enforceable contract surfaces, not metaphor.
- **See also:** [RAW zone](#raw-zone), [WORK zone](#work-zone), [QUARANTINE](#quarantine), [PROCESSED zone](#processed-zone), [Catalog triplet](#catalog-triplet), [PUBLISHED surfaces](#published-surfaces), [Promotion Contract](#promotion-contract)

#### Dataset
- **Status:** CONFIRMED
- **Definition:** A named, versioned collection of artifacts + metadata representing a specific source/product in KFM. Datasets are promoted through lifecycle zones under the Promotion Contract.
- **See also:** [Dataset version](#dataset-version), [Promotion Contract](#promotion-contract)

#### Dataset ID
- **Status:** CONFIRMED
- **Definition:** A stable identifier for a dataset across time (slug or canonical ID). Dataset IDs group dataset versions.
- **See also:** [Dataset version](#dataset-version)

#### Dataset version
- **Status:** CONFIRMED
- **Definition:** An immutable, publishable “release unit” of a dataset that includes processed artifacts, validated catalogs, and run receipts. UI surfaces should show dataset version and freshness.
- **See also:** [PROCESSED zone](#processed-zone), [Run receipt](#run-receipt), [PUBLISHED surfaces](#published-surfaces), [Promotion manifest](#promotion-manifest)

#### DCAT
- **Status:** CONFIRMED
- **Definition:** W3C Data Catalog Vocabulary. In KFM, DCAT is the **dataset-level** surface of the catalog triplet (title/description/publisher/license/distributions), cross-linked to STAC and PROV and extended with KFM identity/policy fields.
- **See also:** [Catalog triplet](#catalog-triplet), [Policy label](#policy-label)

#### Default-deny
- **Status:** CONFIRMED
- **Definition:** A policy posture where the default is to deny access or deny an action unless explicitly allowed. Missing metadata, missing receipts, or ambiguous policy labels should cause denial rather than accidental exposure.
- **See also:** [Fail-closed](#fail-closed), [Policy label](#policy-label)

#### Digest
- **Status:** PROPOSED
- **Definition:** A cryptographic hash (commonly SHA-256) used as a content address for artifacts. In KFM, digests are used to verify integrity and to pin artifact references in catalogs/receipts/manifests.
- **See also:** [Digest-pinned distribution](#digest-pinned-distribution), [Integrity](#integrity)

#### Digest-pinned distribution
- **Status:** PROPOSED
- **Definition:** A distribution pattern where artifacts are referenced by immutable digests (not mutable tags/“latest”). This supports reproducibility and auditability.
- **See also:** [OCI artifact](#oci-artifact), [ORAS](#oras)

---

### E

#### Evidence
- **Status:** CONFIRMED
- **Definition:** The artifacts + metadata + lineage that justify a claim, query result, tile, or story statement. Evidence must be resolvable and governed.
- **See also:** [EvidenceRef](#evidenceref), [EvidenceBundle](#evidencebundle)

#### EvidenceBundle
- **Status:** CONFIRMED
- **Definition:** A structured, policy-filtered payload returned by the evidence resolver. It includes policy decision + obligations applied, license/attribution, provenance/run reference, artifact digests/links (policy-permitting), validation status, and an audit reference.
- **See also:** [Evidence resolver](#evidence-resolver), [EvidenceRef](#evidenceref), [Audit ref](#audit-ref)

#### Evidence drawer
- **Status:** CONFIRMED
- **Definition:** A shared UI component (Map/Story/Focus) that displays the EvidenceBundle for whatever the user is viewing (feature, tile, story paragraph, Focus answer), including license/attribution, freshness, provenance links, and obligations/redactions applied.
- **See also:** [Map Explorer](#map-explorer), [Story Mode](#story-mode), [Focus Mode](#focus-mode), [EvidenceBundle](#evidencebundle)

#### EvidenceRef
- **Status:** CONFIRMED
- **Definition:** A structured reference that can be resolved into an EvidenceBundle. EvidenceRefs must resolve without guessing; broken refs should fail promotion/publishing.
- **See also:** [Evidence resolver](#evidence-resolver), [Catalog triplet](#catalog-triplet)

#### Evidence resolver
- **Status:** CONFIRMED
- **Definition:** The service/endpoint that accepts an EvidenceRef, applies policy + redaction obligations, and returns an EvidenceBundle usable by the UI (target: resolvable in **≤ 2 calls**).
- **See also:** [Trust membrane](#trust-membrane), [Policy engine](#policy-engine)

#### Emergency deny
- **Status:** PROPOSED
- **Definition:** A kill-switch policy mechanism used to force denials (e.g., block promotions) to verify fail-closed behavior and to respond to incidents.
- **See also:** [Fail-closed](#fail-closed), [Policy regression suite](#policy-regression-suite)

---

### F

#### FAIR
- **Status:** PROPOSED
- **Definition:** Principles for making data Findable, Accessible, Interoperable, and Reusable. In KFM, FAIR is used as a governance lens for metadata quality and reuse readiness.
- **See also:** [FAIR+CARE](#faircare)

#### FAIR+CARE
- **Status:** PROPOSED
- **Definition:** A governance framing that combines FAIR principles with CARE principles. In KFM, it is used when discussing metadata quality **and** ethical obligations around sensitive data.
- **See also:** [CARE](#care)

#### Fail-closed
- **Status:** CONFIRMED
- **Definition:** A system design rule: when something is missing, invalid, or ambiguous, the system must deny or block rather than allow by accident. This applies to policy decisions, promotion gates, and evidence resolution.
- **See also:** [Default-deny](#default-deny), [Promotion gates](#promotion-gates)

#### Focus Mode
- **Status:** CONFIRMED
- **Definition:** A user-facing Q&A surface that produces evidence-led answers. Focus Mode must cite sources (EvidenceRefs/EvidenceBundles) for factual claims and abstain when it cannot.
- **See also:** [Cite-or-abstain](#cite-or-abstain), [Evidence drawer](#evidence-drawer)

---

### G

#### Gate
- **Status:** CONFIRMED
- **Definition:** A required check that must pass before a dataset version can be promoted/published (identity, licensing, sensitivity, triplet validity, QA thresholds, receipts).
- **See also:** [Promotion Contract](#promotion-contract), [Promotion gates](#promotion-gates)

#### GeoParquet
- **Status:** CONFIRMED
- **Definition:** A Parquet-based columnar format for geospatial features. In KFM, GeoParquet is an example of a PROCESSED-zone publishable artifact format.
- **See also:** [PROCESSED zone](#processed-zone)

---

### I

#### Integrity
- **Status:** PROPOSED
- **Definition:** The ability to verify that an artifact is complete and unmodified, typically via cryptographic checksums/digests recorded in catalogs and receipts.
- **See also:** [Digest](#digest), [Run receipt](#run-receipt)

---

### J

#### JCS
- **Status:** PROPOSED
- **Definition:** JSON Canonicalization Scheme; a deterministic canonical form for JSON so hashes can be stable. Used to compute `spec_hash`.
- **See also:** [Spec hash](#spec-hash)

---

### L

#### License snapshot
- **Status:** CONFIRMED
- **Definition:** A captured record of upstream licensing/terms at acquisition time, preserved alongside RAW artifacts so later audits can reconstruct what terms applied when data was fetched.
- **See also:** [Acquisition manifest](#acquisition-manifest)

#### Lineage
- **Status:** CONFIRMED
- **Definition:** The “how it was produced” chain linking inputs, activities, and outputs. In KFM, lineage is part of the catalog triplet via PROV and is surfaced in UI provenance panels.
- **See also:** [PROV](#prov), [Provenance](#provenance)

---

### M

#### Map Explorer
- **Status:** CONFIRMED
- **Definition:** The primary UI surface for exploring layers, time windows, and feature inspection. KFM’s UI trust surfaces include dataset version, freshness, license/attribution, policy badges, and an evidence drawer link.
- **See also:** [Evidence drawer](#evidence-drawer), [Trust membrane](#trust-membrane)

#### Materiality
- **Status:** PROPOSED
- **Definition:** A typed decision indicating whether a change is “publish candidate” material based on domain-appropriate diffs (to prevent noisy or meaningless promotions).
- **See also:** [Promotion gates](#promotion-gates), [Promotion manifest](#promotion-manifest)

---

### O

#### Obligation
- **Status:** CONFIRMED
- **Definition:** An action required by policy as a condition of allowing an output (e.g., applying redaction/generalization before serving). Obligations are enforced by policy gates and applied by the evidence resolver and publishing pipelines.
- **See also:** [Redaction](#redaction), [Policy engine](#policy-engine)

#### OCI artifact
- **Status:** PROPOSED
- **Definition:** A bundle stored in an OCI registry (not necessarily a container image) that can include datasets, catalogs, receipts, and attestations, addressed by digest for immutability.
- **See also:** [Digest-pinned distribution](#digest-pinned-distribution), [ORAS](#oras)

#### OPA
- **Status:** CONFIRMED
- **Definition:** Open Policy Agent; a policy engine that evaluates Rego rules to produce allow/deny decisions and obligations.
- **See also:** [Policy engine](#policy-engine)

#### ORAS
- **Status:** PROPOSED
- **Definition:** OCI Registry As Storage; tooling for pushing and pulling non-container artifacts (datasets, receipts, catalogs) to OCI registries.
- **See also:** [OCI artifact](#oci-artifact)

---

### P

#### PEP
- **Status:** CONFIRMED
- **Definition:** Policy Enforcement Point. In KFM, the governed API is the boundary that enforces policy for any access to storage/catalogs/evidence; UI and external clients must not bypass it.
- **See also:** [Trust membrane](#trust-membrane), [Policy engine](#policy-engine)

#### PDP
- **Status:** CONFIRMED
- **Definition:** Policy Decision Point. The component that evaluates policy (e.g., OPA/Rego) and returns allow/deny + obligations. Often paired with a PEP.
- **See also:** [PEP](#pep), [OPA](#opa)

#### Policy engine
- **Status:** CONFIRMED
- **Definition:** The runtime and CI component that evaluates policy-as-code to produce allow/deny decisions and obligations (e.g., redaction required). Semantics should match between CI and runtime where possible.
- **See also:** [Fail-closed](#fail-closed), [Obligation](#obligation)

#### Policy label
- **Status:** CONFIRMED
- **Definition:** A classification tag attached to datasets, artifacts, and outputs that drives access and redaction rules (e.g., public vs restricted). Policy labels must be visible in UI trust surfaces.
- **See also:** [Sensitivity classification](#sensitivity-classification)

#### Policy regression suite
- **Status:** PROPOSED
- **Definition:** A CI test pack that runs representative requests/fixtures through the policy engine and evidence resolver to detect policy regressions (e.g., default-deny, obligation correctness, and policy-safe errors).
- **See also:** [Fail-closed](#fail-closed), [Default-deny](#default-deny), [Evidence resolver](#evidence-resolver)

#### Projection store
- **Status:** CONFIRMED
- **Definition:** A derived database/index/cache built from promoted processed artifacts + catalogs (e.g., PostGIS tables, search indexes, tile caches). Projection stores are rebuildable and must never be treated as canonical truth.
- **See also:** [Canonical layout](#canonical-layout), [Rebuildable projection](#rebuildable-projection), [Truth path](#truth-path)

#### Promotion Contract
- **Status:** CONFIRMED
- **Definition:** The mechanism that turns governance intent into enforceable behavior by defining lifecycle zones and gates. Promotion is the act of moving dataset versions through zones into PUBLISHED surfaces only when all required artifacts exist and validate.
- **See also:** [Data lifecycle zones](#data-lifecycle-zones), [Promotion gates](#promotion-gates), [Promotion manifest](#promotion-manifest)

#### Promotion gates
- **Status:** CONFIRMED
- **Definition:** The minimum checks required for promotion/publishing (identity/versioning, licensing, sensitivity/obligations, catalog triplet validation, QA thresholds, run receipts/audit records, manifests).
- **See also:** [Run receipt](#run-receipt), [Catalog triplet](#catalog-triplet), [Promotion manifest](#promotion-manifest)

#### Promotion manifest
- **Status:** CONFIRMED
- **Definition:** An immutable record emitted when a dataset version is promoted/released. It references the dataset version ID, spec hash, artifacts + digests, catalogs + digests, QA result, policy decision, and approvals (if required). It exists so promotion can be audited and reconstructed.
- **See also:** [Run receipt](#run-receipt), [Catalog triplet](#catalog-triplet), [Audit ref](#audit-ref)

#### PROCESSED zone
- **Status:** CONFIRMED
- **Definition:** The zone containing publishable artifacts in KFM-approved formats with stable IDs and checksums. This is the “data product” layer that downstream projections and serving surfaces are built from.
- **See also:** [RAW zone](#raw-zone), [WORK zone](#work-zone), [PUBLISHED surfaces](#published-surfaces)

#### PROV
- **Status:** CONFIRMED
- **Definition:** The provenance/lineage surface of the KFM catalog triplet. PROV records the activities and agents that generated artifacts.
- **See also:** [Catalog triplet](#catalog-triplet), [Lineage](#lineage)

#### Provenance
- **Status:** CONFIRMED
- **Definition:** The provenance metadata that connects outputs to inputs and processes, enabling auditing and reproducibility. In KFM, provenance is surfaced through PROV plus run receipts and UI provenance panels.
- **See also:** [Run receipt](#run-receipt), [PROV](#prov)

#### PUBLISHED surfaces
- **Status:** CONFIRMED
- **Definition:** Governed runtime surfaces (API + UI) that may only serve promoted dataset versions that have processed artifacts, validated catalogs, run receipts, and policy labels.
- **See also:** [Trust membrane](#trust-membrane), [Promotion Contract](#promotion-contract)

---

### Q

#### QUARANTINE
- **Status:** CONFIRMED
- **Definition:** A holding state within WORK where artifacts fail validation, have unclear licensing, or have sensitivity concerns. Quarantined items are not promoted.
- **See also:** [WORK zone](#work-zone), [Fail-closed](#fail-closed)

---

### R

#### RAW zone
- **Status:** CONFIRMED
- **Definition:** Immutable acquisition storage: upstream payloads/snapshots plus checksums and minimal metadata (time fetched, source, license/terms snapshot). RAW is append-only; you supersede by new acquisitions.
- **See also:** [Acquisition manifest](#acquisition-manifest), [WORK zone](#work-zone)

#### Rebuildable projection
- **Status:** CONFIRMED
- **Definition:** A derived store that can be regenerated from canonical processed artifacts + catalogs (e.g., PostGIS tables, search indexes, graph edges, tile bundles). Projections are not the canonical truth.
- **See also:** [Projection store](#projection-store), [Canonical layout](#canonical-layout)

#### Redaction
- **Status:** CONFIRMED
- **Definition:** A first-class transformation that removes or generalizes sensitive information (geometry, fields, attributes) according to policy obligations before anything is served publicly.
- **See also:** [Obligation](#obligation), [Sensitivity classification](#sensitivity-classification)

#### Run manifest
- **Status:** PROPOSED
- **Definition:** A machine-readable record describing a pipeline run’s inputs, steps, outputs, and environment identifiers. Often paired with a run receipt.
- **See also:** [Run receipt](#run-receipt)

#### Run receipt
- **Status:** CONFIRMED
- **Definition:** A structured audit record capturing inputs, tooling versions, hashes/digests, and policy decisions for a run. Receipts are immutable and used as evidence during promotion/publishing.
- **See also:** [EvidenceBundle](#evidencebundle), [Promotion gates](#promotion-gates), [Audit ref](#audit-ref)

---

### S

#### SBOM
- **Status:** PROPOSED
- **Definition:** A Software Bill of Materials (e.g., SPDX or CycloneDX) describing dependencies for build/release artifacts; used to support supply-chain governance.
- **See also:** [SLSA](#slsa)

#### Sensitivity classification
- **Status:** CONFIRMED
- **Definition:** A classification describing whether data is public, restricted, or otherwise sensitive, and what obligations apply (redaction, generalization, access controls). Sensitivity must influence both CI promotion gates and runtime serving.
- **See also:** [Policy label](#policy-label), [Default-deny](#default-deny)

#### SLSA
- **Status:** PROPOSED
- **Definition:** Supply-chain Levels for Software Artifacts; used with attestations to document how artifacts were built and to reduce tampering risk.
- **See also:** [SBOM](#sbom)

#### Spec hash
- **Status:** PROPOSED
- **Definition:** A deterministic hash of a canonical pipeline spec used to identify “what was intended to run.” Typically computed by canonicalizing JSON (JCS) then hashing (SHA-256), producing an identifier like `jcs:sha256:<hex>`.
- **See also:** [JCS](#jcs), [Run receipt](#run-receipt)

#### Story Mode
- **Status:** CONFIRMED
- **Definition:** A UI surface focused on narrative experiences (“stories”) that must retain provenance, evidence, and policy visibility.
- **See also:** [Story Node](#story-node), [Evidence drawer](#evidence-drawer)

#### Story Node
- **Status:** CONFIRMED
- **Definition:** A versioned narrative artifact that binds narrative text to map state and resolvable citations. A Story Node typically includes a human-readable markdown file plus machine-readable sidecar metadata (map state, citations, policy/review fields). Publishing should be blocked if citations cannot be resolved via evidence resolution.
- **See also:** [EvidenceRef](#evidenceref), [Evidence resolver](#evidence-resolver), [PUBLISHED surfaces](#published-surfaces)

#### STAC
- **Status:** CONFIRMED
- **Definition:** The asset-level surface of the KFM catalog triplet, describing spatiotemporal artifacts (collections, items, assets) with links to distributions and checksums.
- **See also:** [Catalog triplet](#catalog-triplet)

---

### T

#### Trust membrane
- **Status:** CONFIRMED
- **Definition:** A non-bypassable boundary that prevents clients (UI/external) from directly accessing storage. All access must cross the governed API (PEP) where policy is evaluated and enforced.
- **See also:** [PEP](#pep), [Policy engine](#policy-engine)

#### Truth path
- **Status:** CONFIRMED
- **Definition:** The auditable chain linking RAW acquisition → WORK transforms → PROCESSED artifacts → catalog triplet → manifests/receipts → PUBLISHED serving. It is designed so audits and rebuilds can be performed without trusting a database as the source of truth.
- **See also:** [Data lifecycle zones](#data-lifecycle-zones), [Canonical layout](#canonical-layout), [Promotion Contract](#promotion-contract), [Projection store](#projection-store)

---

### W

#### WORK zone
- **Status:** CONFIRMED
- **Definition:** Intermediate transforms and QA where failures are isolated; artifacts may be rewritten. WORK includes normalization, reprojection, tiling jobs, QA reports, and candidate redactions/generalizations. QUARANTINE is the “fail state” within WORK.
- **See also:** [QUARANTINE](#quarantine), [PROCESSED zone](#processed-zone)

---

## Contributing

- Add terms alphabetically under the correct letter section.
- Keep definitions short; prefer KFM usage over generic textbook definitions.
- Do not claim a system behavior is implemented unless:
  - it is confirmed in a governed release note, **or**
  - the repo contains a verified contract/test demonstrating it.

### Definition of done for a glossary update

- [ ] Term is placed in correct A–Z location
- [ ] Status is set appropriately (CONFIRMED/PROPOSED/UNKNOWN)
- [ ] “See also” links exist where helpful
- [ ] No new broken links introduced

---

## Sources

This glossary aligns to the following KFM documents (titles/dates as captured in provided sources):

- **Kansas Frontier Matrix (KFM) — Architecture, Governance, and Delivery Plan** (Date: February 27, 2026)
- **Kansas Frontier Matrix (KFM) — Ultimate Blueprint (Draft)** (Generated 2026-02-20) and **Definitive Design & Governance Guide (vNext)** (included in the source snapshots bundle)
- **Kansas Frontier Matrix (KFM) — Data Source Integration Blueprint** (Version 1.0 — 2026-02-12)
- **New Ideas / idea packs** (used only for **PROPOSED** entries; do not treat as ratified standards)

> **TODO (repo hygiene):** replace any references to PDF-only sources with stable, repo-local Markdown equivalents once those docs are promoted into governed `docs/standards/` locations.

---

[Back to top](#kfm-glossary)
