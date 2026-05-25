<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standard/release-manifest-conformance
title: ReleaseManifest — External Standards Conformance Dossier
type: standard
version: v1
status: draft
owners: <TBD: docs steward + release/governance lead>
created: 2026-05-24
updated: 2026-05-24
policy_label: public
related: [
  contracts/v1/release/,
  schemas/contracts/v1/release/,
  policy/release/,
  release/,
  docs/standards/EVIDENCE_BUNDLE.md,
  docs/standards/PROV/README.md,
  docs/standards/DUO_PROFILE.md,
  docs/standards/MAP_TRUST_STATES.md,
  docs/standards/SIGNING.md,
  docs/standards/CANONICALIZATION.md,
  docs/standards/PMTILES.md,
  docs/standards/ISO-19115.md,
  docs/architecture/contract-schema-policy-split.md,
  docs/doctrine/lifecycle-law.md,
  docs/doctrine/trust-membrane.md
]
tags: [kfm, standard, release-manifest, conformance, jcs, merkle, slsa, dsse, cosign, oci, stac, dcat, governance, rollback]
notes: [
  "Topical standards document (UPPERCASE_WITH_UNDERSCORES) per Directory Rules §6.1.a — names a KFM-coined object's external-standards conformance posture, not the object's meaning.",
  "Object meaning is owned by contracts/v1/release/; machine shape by schemas/contracts/v1/release/; admissibility by policy/release/; release decisions by release/. This file does NOT redefine those.",
  "Placement parallels docs/standards/EVIDENCE_BUNDLE.md; see §2 Scope Guardrail and Appendix B Placement Rationale."
]
[/KFM_META_BLOCK_V2] -->

# ReleaseManifest — External Standards Conformance Dossier

> A single place to answer the question *"which external standards does a KFM `ReleaseManifest` conform to, and how does an external consumer verify a KFM release end-to-end?"* — without redefining the manifest itself.

[![status: draft](https://img.shields.io/badge/status-draft-orange)](#)
[![type: topical standards document](https://img.shields.io/badge/type-topical--standards--document-informational)](#)
[![scope: external conformance only](https://img.shields.io/badge/scope-external%20conformance%20only-critical)](#)
[![governance: cite-or-abstain](https://img.shields.io/badge/governance-cite--or--abstain-blueviolet)](#)
[![identity: JCS+SHA--256](https://img.shields.io/badge/identity-JCS%2BSHA--256-9cf)](#)
[![integrity: Merkle root](https://img.shields.io/badge/integrity-Merkle%20root-9cf)](#)
[![signing: Cosign / DSSE / SLSA](https://img.shields.io/badge/signing-Cosign%20%7C%20DSSE%20%7C%20SLSA-yellowgreen)](#)
[![CI: TODO](https://img.shields.io/badge/CI-TODO-lightgrey)](#)

| Status | Owners | Last reviewed |
|---|---|---|
| **draft** | _TBD — docs steward + release/governance lead_ | 2026-05-24 |

---

> [!CAUTION]
> **Scope guardrail.** This document is **not** the `ReleaseManifest` reference. It does **not** define the object's meaning, fields, validation rules, promotion gates, or admissibility. Those live in `contracts/v1/release/` (meaning), `schemas/contracts/v1/release/` (shape), `policy/release/` (admissibility), and `release/` (decisions and artifacts). This document only describes how a KFM `ReleaseManifest` aligns with the external standards an interoperability partner or external auditor would check it against. See §2 and Appendix B before adding any content here.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Scope guardrail — what this doc is NOT](#2-scope-guardrail--what-this-doc-is-not)
- [3. Authority and standing](#3-authority-and-standing)
- [4. External-standards conformance matrix](#4-external-standards-conformance-matrix)
- [5. Identity and canonicalization](#5-identity-and-canonicalization)
- [6. Content addressing and Merkle integrity](#6-content-addressing-and-merkle-integrity)
- [7. Signing and attestation](#7-signing-and-attestation)
- [8. Inclusion semantics — what the manifest binds](#8-inclusion-semantics--what-the-manifest-binds)
- [9. Catalog interoperability — STAC, DCAT, ISO 19115](#9-catalog-interoperability--stac-dcat-iso-19115)
- [10. Lifecycle integration — promotion, rollback, correction, withdrawal](#10-lifecycle-integration--promotion-rollback-correction-withdrawal)
- [11. ReleaseManifest vs delta manifest](#11-releasemanifest-vs-delta-manifest)
- [12. External verification flow](#12-external-verification-flow)
- [13. Tensions and known limits](#13-tensions-and-known-limits)
- [14. Open questions](#14-open-questions)
- [15. Related docs](#15-related-docs)
- [Appendix A — Worked external verification](#appendix-a--worked-external-verification)
- [Appendix B — Placement rationale](#appendix-b--placement-rationale)

---

## 1. Purpose

CONFIRMED doctrine — **KFM-P7-PROG-0003**: *"When the gate allows promotion to PUBLISHED, it emits a `ReleaseManifest`: a single, signed, hashable JSON object listing every dataset, bundle, and tile archive included in the release."* The manifest is **the** content-addressed binding for a release; consumers (the web client, the catalog harvester, downstream pipelines) bind to it, not to floating "latest" pointers.

The corpus elsewhere ranks the manifest unambiguously: *"every release is itself an `EvidenceBundle` in spirit: signable, gateable, citable."* That positioning puts `ReleaseManifest` directly in the path of multiple external standards: JCS+SHA-256 identity, Merkle content-addressing (sorted-pairwise per `KFM-P5-PROG-0002`), Cosign / Sigstore signing, SLSA / in-toto provenance, DSSE envelopes, OCI / ORAS distribution, STAC / DCAT / ISO 19115 catalog interoperability, SPDX licensing, and CDN cache-invalidation semantics tied to revocation and rollback.

This dossier collects the external-standards posture in one place so that:

1. An interoperability partner can read **one document** to know what they need to verify.
2. An external auditor can read **one document** to know which external standard each field maps to.
3. KFM contributors have **one document** governing version pins for the release-side external surface.
4. The corpus open question (KFM-P1-FEAT-0044, KFM-P1-IDEA-0056) — *"What vocabulary should be shared across API, UI, and release manifests?"* — has a release-side anchor that interlocks with the API-side anchor (`docs/standards/MAP_TRUST_STATES.md`) and the bundle-side anchor (`docs/standards/EVIDENCE_BUNDLE.md`).

> [!NOTE]
> This file is a **topical standards document** in the Directory Rules §6.1.a sense — UPPERCASE_WITH_UNDERSCORES, KFM-coined, sibling to `EVIDENCE_BUNDLE.md`, `MAP_TRUST_STATES.md`, `SENSITIVITY_RUBRIC.md`. It is **not** an external-standard short-name profile (those use UPPERCASE-WITH-HYPHENS — `ISO-19115.md`, `OAI-PMH.md`). See §3 and Appendix B for the placement rationale.

[Back to top](#quick-jump)

---

## 2. Scope guardrail — what this doc is NOT

> [!IMPORTANT]
> If you find yourself adding content that defines fields, validates fields, admits/denies releases, or executes rollback, **stop**. That content belongs in `contracts/`, `schemas/`, `policy/`, or `release/`, not here.

| If the content is about… | …it lives at | …not here |
|---|---|---|
| What a `ReleaseManifest` field **means** | `contracts/v1/release/release_manifest.md` (PROPOSED home) | this doc |
| The **machine shape** of a `ReleaseManifest` (JSON Schema) | `schemas/contracts/v1/release/release_manifest.schema.json` (PROPOSED home) | this doc |
| The OPA rules that **admit, deny, or restrict** a release | `policy/release/` (PROPOSED home) | this doc |
| The **promotion-gate sequence** and reviewer matrix | `policy/release/` + `release/` README | this doc |
| The **`RollbackCard`** object | `contracts/v1/release/rollback_card.md` + `schemas/contracts/v1/release/` | this doc |
| **`CorrectionNotice`** object meaning and workflow | `contracts/v1/correction/` + `policy/correction/` | this doc |
| Actual **release decisions and artifacts** (per-release files) | `release/decisions/`, `release/manifests/`, `release/rollback/` (PROPOSED homes) | this doc |
| The **map-asset family** (`LayerManifest`, `StyleManifest`, `TileArtifactManifest`, `PMTiles` sidecar) | their own `contracts/v1/` + `schemas/contracts/v1/` homes; see `docs/standards/PMTILES.md` | this doc |
| **CDN configuration**, purge APIs, cache TTLs | `infra/` | this doc |
| **Tests and fixtures** | `tests/standards/release/`, `fixtures/standards/release/` | this doc |
| Tutorials and how-tos for release authors | `docs/runbooks/release/` (PROPOSED home) | this doc |

What this document **does** own:

- The list of external standards a `ReleaseManifest` conforms to or crosswalks against.
- The version pin per external standard.
- The conformance level KFM targets per external standard.
- The integration touchpoint (which external term maps to which `ReleaseManifest` concept — without redefining the concept).
- The external-verification recipe — what an outside consumer does to verify a KFM release end-to-end.

[Back to top](#quick-jump)

---

## 3. Authority and standing

| Aspect | Value | Label |
|---|---|---|
| Document class | KFM-coined **topical standards document** | CONFIRMED per Directory Rules §6.1.a |
| Canonical path | `docs/standards/RELEASE_MANIFEST.md` | PROPOSED — placement rationale in Appendix B |
| Primary doctrine anchor | **KFM-P7-PROG-0003** — "ReleaseManifest as the publishable artifact" | CONFIRMED |
| Companion doctrine | KFM-P1-IDEA-0056 (Promotion as governed state transition), KFM-P5-PROG-0002 (MerkleManifest release content-addressing layer), KFM-P1-IDEA-0059 (Watcher output enters WORK_CANDIDATE, not PUBLISHED) | CONFIRMED |
| MapLibre report anchor | `MapReleaseManifest` in `Master_MapLibre_Components-Functions-Features` Object-Index — "Canonical publication envelope binding artifacts, evidence_refs, rights, sensitivity, release_state, policy result, attestations, correction_lineage and rollback" | CONFIRMED |
| Required content (per Atlas object-family table) | `release_id, contents[], digests, evidence_refs[], rollback_target, time` — triggered by PUBLISHED transition | CONFIRMED |
| Pass-15 addendum | Release index entries carry `dataset_id, spec_hash, run_receipt, SPDX, timestamp, evidence bundle digest` | CONFIRMED |
| Pass-32 corroboration | KFM-P5-PROG-0002 (Merkle manifest), KFM-P10-PROG-0006 (DSSE/SLSA attestations), KFM-P13-PROG-0011 (SLSA in-toto predicate), ML-058-031 (ReleaseManifest binds PMTiles to DSSE), ML-058-032 (Public runtime rule for ReleaseManifest) | CONFIRMED |
| Authority **NOT** held by this doc | Object meaning, machine shape, admissibility, promotion-gate sequence, per-release artifacts, rollback procedure, map-asset family | CONFIRMED (Directory Rules §6.1.a) |

> [!NOTE]
> Directory Rules §6.1.a names "release manifest patterns" explicitly alongside `EvidenceBundle` and "the trust membrane" as things `docs/standards/` does **not** own for object meaning. The placement rationale in Appendix B walks the scoping commitment that keeps this file's path legitimate.

[Back to top](#quick-jump)

---

## 4. External-standards conformance matrix

The matrix below is the **principal payload** of this document. Each row names an external standard, the KFM `ReleaseManifest` concept that touches it, the conformance level KFM targets, and where to look in the corpus for the doctrine anchor. PROPOSED — every implementation-level claim (Pinned version, Conformance level) NEEDS VERIFICATION against mounted-repo evidence (no mounted repo this session).

| External standard | KFM touchpoint | Conformance level | Pinned version | Doctrine anchor |
|---|---|---|---|---|
| **RFC 8785 — JSON Canonicalization Scheme (JCS)** | Canonical byte form of the manifest prior to `spec_hash` computation. | **CONFORMS** (default canonicalization) | NEEDS VERIFICATION per policy-bundle release | C1-02, C8-05 |
| **SHA-256 (FIPS 180-4)** | Digest over JCS bytes (manifest `spec_hash` = `jcs:sha256:<hex>`); also default Merkle leaf/node hash. | **CONFORMS** | n/a (algorithm) | C1-02, KFM-P5-PROG-0002 |
| **BLAKE3** | Permitted alternate digest for high-throughput Merkle layers (PMTiles sidecar precedent KFM-P32-PROG-0014). | **CONFORMS, alternate** | n/a | KFM-P5-PROG-0002 tension |
| **Merkle (sorted-pairwise)** | File-set integrity root over all release contents; KFM-P5-PROG-0002 specifies sorted-pairwise, **not** RFC 6962. | **CONFORMS, KFM-pinned variant** | sorted-pairwise SHA-256 — NEEDS ADR per KFM-P5-PROG-0002 | KFM-P5-PROG-0002 |
| **W3C JSON-LD 1.1** | If the manifest is published as JSON-LD (it MAY be), JSON-LD semantics apply. | **CONFORMS, optional** | JSON-LD 1.1 | C8-04 family |
| **W3C PROV-O** | Per-content provenance fragments threaded through `evidence_refs[]`; `prov:wasGeneratedBy` round-trip to `RunReceipt`. | **CONFORMS, REQUIRED for content provenance** | NEEDS VERIFICATION; profile in `docs/standards/PROV/` | C8-03, KFM-P26-PROG-0013 |
| **Sigstore / Cosign** | Keyless signing of the manifest's content-addressed digest; transparency-log entry in Rekor. | **CONFORMS, default** | Cosign current; OIDC issuer allowlist NEEDS VERIFICATION | C1-03 |
| **DSSE (Dead Simple Signing Envelope)** | Envelope format for Cosign signatures over the manifest and over content attestations. | **CONFORMS** | DSSE v1 | C1-03, KFM-P10-PROG-0006, ML-058-031 |
| **SLSA (Supply-chain Levels for Software Artifacts)** | Per-content `slsaprovenance` predicate attesting builder, materials, invocation; aggregated into the manifest's `attestations[]`. | **CONFORMS, target level NEEDS DECISION (1 / 2 / 3)** | SLSA target NEEDS VERIFICATION | C1-04, KFM-P13-PROG-0011 |
| **in-toto** | Predicate format underneath SLSA provenance; same DSSE envelope. | **CONFORMS** | in-toto attestation framework v1 | C1-04, KFM-P10-PROG-0006 |
| **Rekor (Sigstore transparency log)** | Public append-only log of signatures; Rekor entry IDs recorded in `attestations[]` slot. | **CONFORMS** | Rekor current | C1-03 |
| **OCI Image Spec 1.x / ORAS** | Optional content-addressed distribution: manifest may be published as an OCI artifact (KFM-P1-PROG-0041) alongside the JSON file. | **CONFORMS, optional transport** | OCI 1.x — NEEDS VERIFICATION pin | C4-04 family, KFM-P32-PROG (atlas Pass-32 OCI/ORAS rows) |
| **OGC STAC 1.x** | STAC catalog items reference release contents and (PROPOSED) the manifest itself via `rel:attestation` (KFM-P7-PROG-0001). | **CONFORMS, with KFM extension** | STAC 1.x — NEEDS VERIFICATION pin | KFM-P7-PROG-0001 |
| **W3C DCAT v3** | `dcat:Dataset` / `dcat:Distribution` records mirror release contents; `dcat:Distribution` may carry the manifest spec_hash. | **CONFORMS** | DCAT v3 | KFM-P10-PROG-0006 Pass-32 addendum |
| **ISO 19115** | Geographic-metadata crosswalk reached via DCAT, not directly bound to the manifest. | **CONFORMS, indirect** | ISO 19115-1:2014 + Amd 2:2020 — NEEDS VERIFICATION pin | `docs/standards/ISO-19115.md` |
| **SPDX (license expressions)** | Per-content `rights_spdx` field on release index entries (Pass-15 addendum) — e.g., `CC0-1.0`, `CC-BY-4.0`. | **CONFORMS** | SPDX License List current — NEEDS VERIFICATION pin | C1-01, Pass-15 addendum |
| **SPDX or CycloneDX SBOM** | SBOM produced at build time; referenced from `attestations[]` via `RunReceipt`. | **CONFORMS, SBOM format TBD** | NEEDS DECISION | ML-058-031, Master MapLibre v1.5/v2.1 |
| **RFC 7234 — HTTP Caching** | Cache headers and Cache-Control semantics for published artifacts referenced by the manifest. | **CONFORMS** | RFC 7234 | C6-08 |
| **CDN cache-invalidation (vendor-specific)** | Purge APIs triggered on release withdrawal / rollback / correction. | **CONFORMS, vendor-neutral** | n/a (per deployment) | C6-08, ML-M-007 |
| **OpenLineage** | Optional lineage facets on `RunReceipt`s included by reference. | **CONFORMS** | OpenLineage 1.x — NEEDS VERIFICATION pin | C1-05 |

> [!IMPORTANT]
> "Conformance level" in this table is a KFM target, not a third-party assessment. None of these claims have been independently audited; the column is a contract KFM commits to honor, not a certificate.

[Back to top](#quick-jump)

---

## 5. Identity and canonicalization

CONFIRMED doctrine — Pass-10 C1-02:

> *"The `spec_hash` for a dataset entry, model spec, contract, or evidence bundle is computed by canonicalizing the JSON via RFC 8785 JCS (JSON Canonicalization Scheme) and then taking SHA-256 over the canonical bytes; it is recorded as `jcs:sha256:<hex>`."*

The `ReleaseManifest` is itself a JSON object that **MUST** carry its own `spec_hash`. PROPOSED rule: the manifest is the union of three nested integrity claims, **all three of which must be reproducible** from the published bytes alone:

| Layer | What it identifies | How it is computed |
|---|---|---|
| **Manifest spec_hash** | The manifest object's logical identity. | JCS over the manifest's JSON; SHA-256 over the canonical bytes; recorded as `jcs:sha256:<hex>` at top level of the manifest. |
| **Per-content digests** | Each entry in `contents[]` carries the included artifact's own digest (`jcs:sha256:` for JSON; `sha256:` or `blake3:` for binary; `oci://...@sha256:...` for OCI artifacts). | Per the included artifact's own profile; mirrored from the artifact's `RunReceipt`. |
| **Merkle root** | The file-set integrity across the release. | Sorted-pairwise Merkle (KFM-P5-PROG-0002 PROPOSED variant) over the per-content digests; root stored on the manifest. |

> [!WARNING]
> The manifest's `spec_hash` and its Merkle root are **not** the same value. The `spec_hash` proves *"this manifest JSON is identical"*; the Merkle root proves *"these contents are identical."* A consumer that records only one is recording only half the release.

### 5.1 Canonicalization choice

The release-side canonicalization choice MUST match the bundle-side choice documented at `docs/standards/EVIDENCE_BUNDLE.md` §5 — **JCS by default**, URDNA2015 reserved for the narrow RDF-semantic case. The full decision matrix lives at `docs/standards/CANONICALIZATION.md` (PROPOSED, not yet authored — Pass-10 C1-02 expansion direction).

### 5.2 Cadence

Open per KFM-P7-PROG-0003: *"What is the cadence? Daily, weekly, on-demand? The corpus implies on-demand."* PROPOSED: cadence is **on-demand**, triggered by promotion gate, not by a clock. A clock-driven cadence is permitted for operational map releases (e.g., a daily streamflow snapshot) but **MUST NOT** be the default for atlas-class releases.

[Back to top](#quick-jump)

---

## 6. Content addressing and Merkle integrity

CONFIRMED — KFM-P5-PROG-0002: *"Catalog closure with attestations binds the artifact to its lineage; Merkle binds the file set to a single root, which is what enables partial-dataset proofs, cross-version verification, and downstream tamper detection without re-fetching the whole release."*

### 6.1 Merkle variant in use

PROPOSED — pending ADR per KFM-P5-PROG-0002 tension:

| Aspect | KFM choice | Notes |
|---|---|---|
| **Tree construction** | Sorted-pairwise binary Merkle | NOT RFC 6962 (Certificate Transparency Merkle). Choice is deterministic but format **MUST be pinned by ADR** before downstream verifiers proliferate. |
| **Leaf hash** | SHA-256 over the canonical per-content digest string | BLAKE3 considered for high-throughput cases (PMTiles sidecar precedent); algorithm of record is SHA-256 until ADR says otherwise. |
| **Sort key** | Lexicographic byte order over canonical content path | Reproducibility depends on stable path normalization. |
| **Empty release** | Forbidden — a `ReleaseManifest` with `contents[] == []` is invalid | Promotion gate fails closed. |

> [!IMPORTANT]
> The corpus is explicit (KFM-P5-PROG-0002 tension): *"This choice is deterministic but the format should be pinned in an ADR."* Until that ADR exists, this section is the canonical statement of intent. A consumer who computes the Merkle root differently from the rules above will get a different root for the same release.

### 6.2 Merkle scope

Open per KFM-P5-PROG-0002: *"Should the Merkle manifest cover ALL files in `data/published/<collection>/<version>/`, or only the canonical artifact files (excluding receipts and attestations, which are Merkle-secured separately)?"* The corpus implies the former.

PROPOSED until ADR: the Merkle root covers **all canonical artifact files** referenced by `contents[]`. Receipts, attestations, and signatures are **referenced by digest** in `contents[]` entries and `attestations[]` slots, so they are Merkle-secured transitively. Including them in the Merkle proper would create a circular dependency at sign time.

### 6.3 Distribution

A `ReleaseManifest` may be distributed as:

1. **A plain JSON file** at a stable URL under `data/published/`.
2. **An OCI artifact** in a registry (`oci://<registry>/<repo>@sha256:<hex>`) per the Pass-32 SRC-P32-001 OCI/ORAS/Cosign artifact-publication evidence.
3. **An IPFS object** when the deployment topology calls for it.

All three transports MUST resolve to **byte-identical** manifest content when the underlying release is the same; the identity is the `spec_hash`, not the transport URL.

[Back to top](#quick-jump)

---

## 7. Signing and attestation

CONFIRMED doctrine — Pass-10 C1-03 (Cosign keyless), C1-04 (SLSA / in-toto), Pass-32 KFM-P10-PROG-0006 (DSSE/SLSA attestations), ML-058-031 (ReleaseManifest binds PMTiles to DSSE provenance receipts).

### 7.1 The three-layer manifest signing stack

```mermaid
flowchart TB
  subgraph Layer1["Layer 1 — Identity"]
    A[JCS canonicalize manifest]
    B[SHA-256]
    M[Sorted-pairwise Merkle over contents]
    A --> B
    B --> C[manifest.spec_hash<br/>jcs:sha256:HEX]
    M --> R[manifest.merkle_root<br/>sha256:HEX]
  end

  subgraph Layer2["Layer 2 — Signature"]
    D[cosign sign manifest]
    E[Fulcio cert<br/>via OIDC]
    F[Rekor entry id]
    D --> E
    D --> F
  end

  subgraph Layer3["Layer 3 — Attestation"]
    G[SLSA release-level predicate]
    H[in-toto Statement]
    I[DSSE envelope]
    J[cosign attest --predicate]
    G --> H --> I --> J
  end

  C --> D
  R --> D
  C --> G
  R --> G
  J --> K[manifest.attestations[] slot]
  F --> K

  style C fill:#fff4cc,stroke:#b58900
  style R fill:#fff4cc,stroke:#b58900
  style K fill:#d9eaff,stroke:#2c5282
```

PROPOSED — diagram reflects C1-02 / C1-03 / C1-04 / KFM-P5-PROG-0002 / KFM-P10-PROG-0006 / ML-058-031 in combination. Tooling pins NEED VERIFICATION.

### 7.2 What the manifest's `attestations[]` slot carries

PROPOSED — implementation NEEDS VERIFICATION against `contracts/v1/release/release_manifest.md`.

| Attestation kind | What it attests | Standard |
|---|---|---|
| `cosign` envelope over the manifest | The manifest digest was signed by the named identity, recorded in Rekor. | Cosign + DSSE + Rekor |
| `slsaprovenance` over the release | The release was built by the named builder, with the named materials, at the named invocation. | SLSA + in-toto + DSSE |
| `sbom` per included artifact (by reference) | The SBOM of the build environment that produced the artifact. | SPDX or CycloneDX |
| `evidence_bundle` reference per content (by digest) | Each content has an `EvidenceBundle` resolvable to its `RunReceipt`. | KFM-internal; see `EVIDENCE_BUNDLE.md` |
| `correction_lineage` (when applicable) | The release supersedes a prior release and references its `CorrectionNotice`. | KFM-internal; see §10 |

### 7.3 Keyless-vs-keyed posture

CONFIRMED (C1-03): keyless via Sigstore is the **default**; a pinned key pair is the **air-gapped fallback**. The release-side signing posture is identical to the bundle-side posture; the full dual-mode policy and the OIDC-issuer allowlist live at `docs/standards/SIGNING.md` (PROPOSED, not yet authored). For releases specifically, the OIDC issuer **MUST** be one of the documented build-platform identities; ad-hoc developer identities are prohibited from signing releases.

[Back to top](#quick-jump)

---

## 8. Inclusion semantics — what the manifest binds

CONFIRMED — Atlas object-family table:

> *"`ReleaseManifest`: Records the contents, version, signatures, and rollback target for a release. Required content: `release_id, contents[], digests, evidence_refs[], rollback_target, time`. Triggered by PUBLISHED transition."*

CONFIRMED — Master MapLibre Object-Index:

> *"`MapReleaseManifest / ReleaseManifest`: Canonical publication envelope binding artifacts, evidence_refs, rights, sensitivity, release_state, policy result, attestations, correction_lineage and rollback."*

This document does **not** specify the field shape (that's the schema's job). It documents the **external-standards binding** each conceptual slot carries.

### 8.1 Conceptual slots and their external bindings

| Slot | External binding | Notes |
|---|---|---|
| `release_id` | KFM-internal; no external standard. | Stable, content-addressable. |
| `spec_hash` | JCS + SHA-256 — see §5. | The manifest's own identity. |
| `merkle_root` | Sorted-pairwise Merkle — see §6. | The file-set's integrity root. |
| `contents[]` entries | Per-entry: `dataset_id`, per-content `spec_hash`, `run_receipt` ref, `evidence_bundle` ref, `rights_spdx` (SPDX), `timestamp` (ISO 8601). | Pass-15 addendum. |
| `evidence_refs[]` | Resolves to `EvidenceBundle` per `docs/standards/EVIDENCE_BUNDLE.md`; carries PROV-O fragments per `docs/standards/PROV/`. | Required for every content with admissible-evidence weight. |
| `attestations[]` | DSSE envelopes per §7; each entry carries a `type` (cosign / slsaprovenance / sbom / evidence_bundle / correction_lineage). | Cosign DSSE entries are themselves signed; Rekor entry IDs included. |
| `rights_status` | SPDX-aligned per entry; aggregate posture at manifest level. | Aggregate is the most-restrictive across entries. |
| `sensitivity` | Sensitivity rubric tier per entry (see `SENSITIVITY_RUBRIC.md` PROPOSED); aggregate tier at manifest level. | Same most-restrictive aggregation rule. |
| `release_state` | One of: `current`, `withdrawn`, `superseded`. | Drives `MAP_TRUST_STATES` `verified` / `withdrawn` mapping per §10. |
| `policy_result` | `PolicyDecision` summary across the gates that admitted this release. | Full decision lives in `release/decisions/`. |
| `promotion_decision` | Reference to `PromotionDecision` (KFM-P1-IDEA-0056). | Records the reviewer chain. |
| `correction_lineage` | Reference to prior release(s) this one corrects; references the `CorrectionNotice`. | Empty for an originating release. |
| `rollback_target` | Reference to the previous `ReleaseManifest` the system rolls back to on failure. | Required field. See §10. |
| `cache_invalidation` | List of cache-purge actions to execute on `verified → withdrawn` / `verified → superseded` transitions. | Vendor-neutral; binds RFC 7234 semantics + CDN-specific purge APIs. |
| `time` | ISO 8601 timestamp. | Required. |

> [!CAUTION]
> The shape of these fields is **not** this document's authority — it is the contract and schema's. The mapping above identifies the **external standards** each slot binds to. If the schema renames a field, the binding follows the schema; this dossier follows the schema, not the other way around.

[Back to top](#quick-jump)

---

## 9. Catalog interoperability — STAC, DCAT, ISO 19115

A `ReleaseManifest` is reached **through** catalog records as well as referenced **by** them. Three external standards govern the reach.

### 9.1 STAC integration

CONFIRMED (KFM-P7-PROG-0001 *STAC attestation hook*): STAC items SHOULD expose a `rel:attestation` link directly to the release-side artifact whose `spec_hash` certifies them — that artifact is the relevant `EvidenceBundle`, and the `EvidenceBundle` is in turn referenced by the `ReleaseManifest.contents[]` entry for that dataset. So a STAC client following two link relations reaches the `ReleaseManifest`:

```text
STAC Item ──rel:attestation──▶ EvidenceBundle ──evidence_refs──▶ ReleaseManifest
```

The `rel:attestation` link relation is not currently a standard STAC link relation; KFM uses it under a controlled namespace pending submission through the STAC extension process.

### 9.2 DCAT integration

PROPOSED — Pass-32 SRC-P32 atlas addendum: `dcat:Dataset` and `dcat:Distribution` records mirror per-release content. A `dcat:Distribution` MAY carry the `ReleaseManifest` `spec_hash` as the distribution identity, so a DCAT-only consumer can verify the release without STAC-specific knowledge. The full crosswalk lives in `docs/standards/PROV/crosswalk-dcat.md` (PROPOSED, not yet authored).

### 9.3 ISO 19115 — reached via DCAT

ISO 19115 conformance is **indirect** — the manifest does not embed ISO 19115 records directly; the DCAT layer carries the ISO 19115 crosswalk for downstream geographic-metadata consumers. The profile lives at `docs/standards/ISO-19115.md` (prior-session-authored; presence NEEDS VERIFICATION).

[Back to top](#quick-jump)

---

## 10. Lifecycle integration — promotion, rollback, correction, withdrawal

CONFIRMED — Pass-10 C6-08, KFM-P1-IDEA-0056, KFM-P7-PROG-0003.

The `ReleaseManifest` is the **only artifact** that crosses the PUBLISHED boundary by name; everything else either lives behind the trust membrane or is referenced by the manifest. Its lifecycle is therefore the release lifecycle.

### 10.1 Lifecycle state map

```mermaid
flowchart LR
  PD[PromotionDecision] --> M1[ReleaseManifest v1<br/>release_state: current]
  M1 -->|correction issued| CN[CorrectionNotice]
  CN --> M2[ReleaseManifest v2<br/>release_state: current<br/>correction_lineage: [v1]]
  M1 -->|superseded by v2| M1S[ReleaseManifest v1<br/>release_state: superseded]
  M1 -->|rollback triggered| RC[RollbackCard]
  RC --> M1R[ReleaseManifest v0<br/>restored as current]
  M1 -->|withdrawn| M1W[ReleaseManifest v1<br/>release_state: withdrawn<br/>tombstone issued]

  M1W --> CI1[cache invalidation: purge CDN, bump PMTiles index]
  M2 --> CI2[cache invalidation: purge CDN, bump PMTiles index]
  M1R --> CI3[cache invalidation: purge CDN, bump PMTiles index]

  style M1 fill:#d9eaff,stroke:#2c5282
  style M2 fill:#d9eaff,stroke:#2c5282
  style M1W fill:#ffe4e1,stroke:#a04545
  style M1S fill:#fff4cc,stroke:#b58900
```

PROPOSED — diagram reflects C6-08 (revocation + cache invalidation), KFM-P1-IDEA-0056 (promotion as governed state transition), KFM-P7-PROG-0003 (manifest as publishable artifact). Tooling NEEDS VERIFICATION.

### 10.2 Cache-invalidation contract

CONFIRMED — Pass-10 C6-08: *"Every published item exposes a `revocation_endpoint`, an `embargo_until` field, and (where applicable) cache invalidation hooks (PMTiles index bump, tile server purge). On revocation: issue a signed tombstone, append a new `spec_hash` and `run_receipt` to the ledger, and trigger invalidation webhooks."*

For `ReleaseManifest` transitions:

| Transition | Cache invalidation required | Tombstone required |
|---|---|---|
| `current → superseded` | Yes — PMTiles index bump, CDN purge of content URLs. | No (supersession is graceful; old manifest remains resolvable). |
| `current → withdrawn` | Yes — same. | **Yes** — withdrawn content MUST NOT be served. |
| `current → (rollback)` | Yes — same, plus restore prior manifest's URL bindings. | No (the rollback target is itself a valid prior release). |
| `withdrawn → (re-publish)` | Yes — invalidate the withdrawal chip. | n/a (issue a new release; do not reanimate the withdrawn one). |

The cache-invalidation contract binds **RFC 7234** (HTTP caching semantics) and **vendor-specific CDN purge APIs**. KFM remains vendor-neutral: the `cache_invalidation[]` slot in §8.1 lists the actions, not the vendor.

### 10.3 Rollback target — required, not optional

CONFIRMED — Atlas object-family table: `rollback_target` is a **required** field. A `ReleaseManifest` with no `rollback_target` is invalid; promotion gate fails closed. The rollback target points at the prior `ReleaseManifest`'s digest (not at a floating "previous" pointer), so the rollback is content-addressed.

> [!WARNING]
> A release that ships without a tested rollback path is a trust-membrane violation. ML-061 anti-patterns category names this explicitly: rollback drills are part of release acceptance, not a post-launch nice-to-have.

[Back to top](#quick-jump)

---

## 11. ReleaseManifest vs delta manifest

CONFIRMED tension — KFM-P7-PROG-0003: *"The relationship between a `ReleaseManifest` and a `delta_manifest` (per-tile-set) is not fully resolved; both exist in the corpus and overlap."*

PROPOSED reconciliation (from KFM-P7-PROG-0003 expansion direction):

| Concept | Granularity | Scope | Relationship |
|---|---|---|---|
| `delta_manifest` | Per-product (e.g., per-PMTiles set, per-COG collection) | What changed in this product since the last release of *this product*. | A delta manifest is a **build artifact**; it exists to support efficient updates and partial-fetch verification. |
| `ReleaseManifest` | Per-release | What is published in this release across all products. | A release manifest **references** the relevant delta manifests by digest; the release manifest is the user-visible, signed envelope. |

> [!IMPORTANT]
> The PROPOSED rule: **`ReleaseManifest.contents[]` entries MAY reference `delta_manifest` digests, but consumers MUST resolve via the `ReleaseManifest`.** A consumer that binds to a `delta_manifest` directly is binding to a build artifact, not a release.

ADR resolution NEEDED — see §14 item 1. Until resolved, this document is the working statement of intent.

[Back to top](#quick-jump)

---

## 12. External verification flow

The recipe below is the **principal external-consumer payload** of this document. It describes what an outside auditor or interoperability partner does to verify a KFM release end-to-end.

PROPOSED. Tool names and step ordering NEED VERIFICATION when the `kfm-hash`, `kfm-merkle`, and `kfm-evidence-resolve` CLIs ship.

```text
Given:
  - A ReleaseManifest URI (https://, kfm://, oci://, or ipfs://)
  - The expected manifest spec_hash (jcs:sha256:<hex>)

Steps:
  1. Fetch the manifest bytes from the URI.
  2. Verify content-address: SHA-256(manifest bytes) MUST equal the URI digest (if OCI/IPFS).
  3. Canonicalize the manifest: RFC 8785 JCS over the JSON.
  4. Compute the manifest spec_hash: SHA-256(canonical bytes).
  5. Verify the spec_hash matches the expected value.
  6. Fetch the Cosign signature for the manifest digest.
  7. Verify the signature against the Sigstore root and the OIDC-issuer allowlist;
     check the Rekor transparency-log entry.
  8. Fetch the release-level SLSA provenance predicate from manifest.attestations[].
  9. Verify the predicate's subject digest matches the manifest spec_hash from step 4.
 10. Verify the predicate's builder identity is on the documented release-builder
     allowlist (developer identities are NOT acceptable for releases — §7.3).
 11. Recompute the Merkle root over manifest.contents[]:
       a. For each entry, take the per-content digest verbatim.
       b. Sort entries lexicographically by canonical content path.
       c. Build a sorted-pairwise Merkle tree (SHA-256 leaves and nodes).
       d. The computed root MUST equal manifest.merkle_root.
 12. For each entry in manifest.contents[]:
       a. Fetch the EvidenceBundle by its evidence_refs entry.
       b. Run the EvidenceBundle verifier per docs/standards/EVIDENCE_BUNDLE.md §11.
       c. Verify the bundle's spec_hash matches the manifest's recorded per-content digest.
 13. Walk manifest.correction_lineage[] (if any):
       a. Each prior ReleaseManifest referenced MUST itself be verifiable.
       b. The CorrectionNotice tying them together MUST resolve and verify.
 14. Verify manifest.rollback_target points at a previous manifest whose
     spec_hash is itself verifiable (content-addressed rollback).
 15. For consent-bearing content, additionally verify the ConsentSidecar per
     docs/standards/DUO_PROFILE.md §7.
```

A verifier that completes steps 1–15 has independently established: the manifest is byte-identical to what was signed; the signer is on the release-builder allowlist; the build environment was the one attested; the Merkle root matches the included contents; every content's evidence chain is intact; any corrections in the lineage are themselves verifiable; and rollback is content-addressed to a previously verifiable release. **That is the full external verification surface** of a KFM release.

[Back to top](#quick-jump)

---

## 13. Tensions and known limits

| Tension | Source | KFM posture |
|---|---|---|
| Sorted-pairwise Merkle vs RFC 6962 (CT Merkle). | KFM-P5-PROG-0002 | KFM ships sorted-pairwise; pin by ADR; document so consumers verify with the correct construction. |
| SHA-256 vs BLAKE3 as the Merkle leaf/node hash. | KFM-P5-PROG-0002 | SHA-256 is the algorithm of record; BLAKE3 is permitted for high-throughput sidecars only (e.g., PMTiles), not for the release Merkle proper. |
| Merkle scope: all files or only canonical artifact files? | KFM-P5-PROG-0002 open | PROPOSED: canonical artifacts only; receipts and attestations are Merkle-secured transitively via per-entry digests. |
| `ReleaseManifest` vs `delta_manifest` overlap. | KFM-P7-PROG-0003 tension | Reconciled in §11 PROPOSED; ADR resolution pending. |
| Release cadence: daily / weekly / on-demand. | KFM-P7-PROG-0003 open | PROPOSED: on-demand by default; clock-driven cadence permitted for operational, not atlas-class. |
| Atlas-class vs operational-map release gate sequence. | KFM-P1-IDEA-0056 open | Two PROPOSED gate sequences; ADR resolution pending. |
| SLSA target level (1 / 2 / 3). | C1-04 open | NEEDS DECISION; Level 3 requires hardened build platforms. |
| OIDC-issuer allowlist for release signing. | C1-03 open | NEEDS DECISION; release-side allowlist MUST be more restrictive than bundle-side. |
| SBOM format (SPDX vs CycloneDX). | ML-058-031 | NEEDS DECISION; KFM remains format-neutral at the doctrine level. |
| Cosign keyless mode depends on Sigstore availability at sign time. | C1-03 | KMS-managed-key fallback documented; air-gapped operation uses keyed mode. |
| Cache-invalidation contract is vendor-neutral; concrete vendor APIs live in `infra/`. | C6-08, ML-M-007 | Vendor neutrality is doctrine; per-vendor adapters are an implementation concern. |
| Title clash between this doc and the future `contracts/v1/release/release_manifest.md`. | this doc | The §2 scope guardrail is the protection; if drift accumulates, retitle this file (§14 item 5). |

[Back to top](#quick-jump)

---

## 14. Open questions

UNKNOWN / NEEDS VERIFICATION items, tracked here until resolved by ADR or mounted-repo evidence.

1. **`ReleaseManifest` vs `delta_manifest` reconciliation** — adopt the PROPOSED rule in §11 via ADR.
2. **Merkle variant pin** — sorted-pairwise SHA-256 per §6; pin by ADR per KFM-P5-PROG-0002 tension.
3. **Merkle scope** — canonical artifacts only vs all files in `data/published/<collection>/<version>/`. Resolution by ADR.
4. **Release cadence policy** — on-demand vs clock-driven per release class.
5. **This document's title clash** — if confusion arises with the future contract Markdown, retitle to `RELEASE_MANIFEST_CONFORMANCE.md` and leave a redirect.
6. **SLSA target level** — 1, 2, or 3; affects release-builder allowlist and build-platform requirements.
7. **OIDC-issuer allowlist for releases** — release-side must be more restrictive than bundle-side; specific issuers TBD.
8. **SBOM format** — SPDX or CycloneDX (or both).
9. **OCI/ORAS publication adoption** — whether the manifest's canonical transport becomes OCI per Pass-32 SRC-P32-001, or remains plain HTTP.
10. **STAC `rel:attestation` registration** — same submission as `docs/standards/EVIDENCE_BUNDLE.md` §13 item 7.
11. **Gate sequence per release class** — atlas-class vs operational-map (KFM-P1-IDEA-0056 open).
12. **Cache-invalidation telemetry contract** — what the `cache_invalidation[]` entries report on completion. NEEDS DECISION.
13. **Bundle reference verifier languages** — Python and Go per C8-04 expansion; TypeScript open.
14. **Partial-fetch / partial-verification protocol** — what the sorted-pairwise Merkle proof structure looks like; KFM-P5-PROG-0002 expansion direction.

[Back to top](#quick-jump)

---

## 15. Related docs

PROPOSED links — verify all paths against mounted repo before publishing.

- [`contracts/v1/release/`](../../contracts/v1/release/) — _PROPOSED contract home._ Object meaning for `ReleaseManifest`, `RollbackCard`, `CorrectionNotice`, `PromotionDecision`. **The canonical place for the manifest's definition; this dossier defers to it.**
- [`schemas/contracts/v1/release/`](../../schemas/contracts/v1/release/) — _PROPOSED schema home._ Machine shape.
- [`policy/release/`](../../policy/release/) — _PROPOSED policy home._ Admissibility, promotion-gate sequence, rollback authorization.
- [`release/`](../../release/) — _PROPOSED home._ Per-release decisions and artifacts.
- [`docs/standards/EVIDENCE_BUNDLE.md`](./EVIDENCE_BUNDLE.md) — companion topical standards document; the bundle whose digests this manifest aggregates.
- [`docs/standards/MAP_TRUST_STATES.md`](./MAP_TRUST_STATES.md) — the trust-state vocabulary `release_state` participates in.
- [`docs/standards/PROV/README.md`](./PROV/README.md) — provenance profile; PROV-O fragments threaded through `evidence_refs[]`.
- [`docs/standards/DUO_PROFILE.md`](./DUO_PROFILE.md) — consent vocabulary; consent-bearing content adds a verification step (§12 step 15).
- [`docs/standards/SIGNING.md`](./SIGNING.md) — _PROPOSED, not yet authored._ Cosign / Sigstore / SLSA / DSSE / Rekor.
- [`docs/standards/CANONICALIZATION.md`](./CANONICALIZATION.md) — _PROPOSED, not yet authored._ JCS-vs-URDNA2015 decision matrix.
- [`docs/standards/PMTILES.md`](./PMTILES.md) — published-tile profile; PMTiles index bump tied to cache invalidation.
- [`docs/standards/ISO-19115.md`](./ISO-19115.md) — geographic-metadata profile; reached via DCAT.
- [`docs/standards/OAI-PMH.md`](./OAI-PMH.md) — harvest protocol profile.
- [`docs/standards/SENSITIVITY_RUBRIC.md`](./SENSITIVITY_RUBRIC.md) — _PROPOSED, not yet authored._ Tier rule that drives `sensitivity` aggregation.
- [`docs/standards/REDACTION_DETERMINISM.md`](./REDACTION_DETERMINISM.md) — _PROPOSED, not yet authored._ Sister topical standards document.
- [`docs/architecture/contract-schema-policy-split.md`](../architecture/contract-schema-policy-split.md) — the rule that keeps this dossier out of `contracts/`, `schemas/`, and `policy/`.
- [`docs/doctrine/trust-membrane.md`](../doctrine/trust-membrane.md) — _PROPOSED placement._ Trust-membrane invariants the manifest is the publication-side expression of.
- [`docs/doctrine/lifecycle-law.md`](../doctrine/lifecycle-law.md) — _PROPOSED placement._ The lifecycle this manifest seals the PUBLISHED transition of.
- [`docs/runbooks/release/`](../runbooks/release/) — _PROPOSED runbook home._ Release author's how-to and rollback drill.

[Back to top](#quick-jump)

---

<details>
<summary><strong>Appendix A — Worked external verification</strong></summary>

A worked example for a hypothetical KFM release published via OCI plus the canonical JSON file. **All values are illustrative**; do not copy as a contract.

```bash
# 1-2. Fetch the manifest and verify content-address
oras pull <registry>/<repo>@sha256:<HEX> --output ./release.json
sha256sum ./release.json
# expected: <HEX>

# 3-5. Canonicalize and compute manifest spec_hash
kfm-hash --canonicalize=jcs ./release.json
# expected: jcs:sha256:<HEX-matching-release-record>

# 6-7. Fetch the cosign signature bundle and verify
cosign verify \
  --certificate-identity-regexp '^https://github.com/<KFM-RELEASE-BUILDER>/.+@refs/tags/release-.+$' \
  --certificate-oidc-issuer 'https://token.actions.githubusercontent.com' \
  <registry>/<repo>@sha256:<HEX>

# 8-10. Fetch and inspect the SLSA release predicate
cosign verify-attestation \
  --type slsaprovenance \
  --certificate-identity-regexp '^https://github.com/<KFM-RELEASE-BUILDER>/.+@refs/tags/release-.+$' \
  --certificate-oidc-issuer 'https://token.actions.githubusercontent.com' \
  <registry>/<repo>@sha256:<HEX> \
  | jq '.payload | @base64d | fromjson'
# verify subject digest == manifest spec_hash; builder is on release-builder allowlist

# 11. Recompute Merkle root
kfm-merkle --variant=sorted-pairwise --hash=sha256 < ./release.json
# expected: sha256:<HEX-matching-merkle_root>

# 12. Walk contents[] and verify each EvidenceBundle
jq '.contents[]' ./release.json | while read entry; do
  ref=$(echo "$entry" | jq -r '.evidence_ref')
  digest=$(echo "$entry" | jq -r '.spec_hash')
  kfm-evidence-resolve --ref "$ref" --expect-hash "$digest"
done

# 13. Walk correction_lineage and verify prior manifests + CorrectionNotice
jq -r '.correction_lineage[]' ./release.json | while read prior; do
  kfm-verify-release --uri "$prior"
done

# 14. Verify rollback target resolves
prior=$(jq -r '.rollback_target' ./release.json)
kfm-verify-release --uri "$prior"
```

The exact CLI commands depend on the tooling pin (`kfm-hash`, `kfm-merkle`, `kfm-evidence-resolve`, `kfm-verify-release`) — those CLIs are PROPOSED and NEEDS VERIFICATION against mounted-repo evidence. The shape of the steps is doctrine-grounded.

</details>

<details>
<summary><strong>Appendix B — Placement rationale</strong></summary>

This document lives at `docs/standards/RELEASE_MANIFEST.md` despite Directory Rules §6.1.a stating that `docs/standards/` "is the canonical home for **external** standards profiles … never for KFM's own object meaning (which lives in `contracts/`)." The §6.1.a authority text **names "release manifest patterns" explicitly**, alongside `EvidenceBundle` and the trust membrane, as KFM-canonical patterns that `docs/standards/` does not own. The placement is legitimate, but only because of a narrow scoping commitment that exactly parallels the one for `docs/standards/EVIDENCE_BUNDLE.md`.

**What §6.1.a forbids:** placing the `ReleaseManifest`'s **object meaning** here. That is owned by `contracts/v1/release/`. This document does not do that.

**What §6.1.a permits:** placing a "Multi-word topical standards document … not external standards" using UPPERCASE_WITH_UNDERSCORES. The pattern is established with `SENSITIVITY_RUBRIC.md`, `REDACTION_DETERMINISM.md`, `SMART_SYNC.md`, and (newly authored) `EVIDENCE_BUNDLE.md` and `MAP_TRUST_STATES.md`. This file matches that pattern: it documents the **standardized external-conformance posture** of `ReleaseManifest`.

**Why this scoping is non-trivial.** If left undefended, this file would drift toward becoming "the `ReleaseManifest` reference" — which is precisely what §6.1.a forbids. The scope guardrail in §2 is therefore not boilerplate; it is the structural defense that keeps the placement legitimate. Every reviewer who adds content here is asked to confirm the content is **about `ReleaseManifest`'s external-standards posture**, not about `ReleaseManifest` itself.

**Alternative paths considered:**

| Alternative | Verdict |
|---|---|
| Move to `contracts/v1/release/release_manifest.md` | Wrong — `contracts/` is object meaning, not external-conformance dossiers. The conformance dossier travels independently of contract revisions. |
| Split into per-standard files (`docs/standards/RELEASE_MANIFEST_JCS.md`, `..._SLSA.md`, `..._MERKLE.md`) | Wrong — fragments the cross-cutting view this dossier is meant to provide. |
| Rename to `RELEASE_MANIFEST_CONFORMANCE.md` for unambiguous scope | **Reasonable.** Recorded as §14 open question 5; resolution by README rule, not ADR. Parallels the same question in `EVIDENCE_BUNDLE.md`. |
| Embed the content into `contracts/v1/release/release_manifest.md` as a section | Wrong — couples object meaning to external-version churn; external pins should move independently of the contract. |
| Place under `docs/standards/PROV/` as a subsidiary | Wrong — release-side conformance is broader than provenance (Merkle, OCI, SLSA, STAC, DCAT, ISO 19115). The PROV folder owns only the PROV-O / PAV slice. |
| Place under `release/README.md` | Wrong — `release/` is the canonical home for **release decisions and artifacts**, not for external-standards conformance documentation. |

The current path is the least-bad choice given the constraints, and it consciously parallels `EVIDENCE_BUNDLE.md` to keep the pattern legible. If §14 item 5 resolves to a rename, the migration is a one-line redirect.

</details>

---

### Footer

> **Document class:** Topical standards document · **Scope:** External-standards conformance posture for `ReleaseManifest` · **Authority NOT held:** object meaning, machine shape, admissibility, promotion gates, per-release artifacts, rollback procedure, map-asset family.

| | |
|---|---|
| **Canonical homes** | Meaning → [`contracts/v1/release/`](../../contracts/v1/release/) · Shape → [`schemas/contracts/v1/release/`](../../schemas/contracts/v1/release/) · Admissibility → [`policy/release/`](../../policy/release/) · Decisions → [`release/`](../../release/) |
| **Sister conformance dossier** | [EVIDENCE_BUNDLE.md](./EVIDENCE_BUNDLE.md) |
| **Vocabulary anchor** | [MAP_TRUST_STATES.md](./MAP_TRUST_STATES.md) — `release_state` participation |
| **Related** | [PROV/](./PROV/README.md) · [DUO_PROFILE.md](./DUO_PROFILE.md) · [ISO-19115.md](./ISO-19115.md) · [OAI-PMH.md](./OAI-PMH.md) · [PMTILES.md](./PMTILES.md) · _SIGNING.md (PROPOSED)_ · _CANONICALIZATION.md (PROPOSED)_ |
| **Sister topical docs** | _SENSITIVITY_RUBRIC.md (PROPOSED)_ · _REDACTION_DETERMINISM.md (PROPOSED)_ |
| **Last updated** | 2026-05-24 |
| **Doc owner** | _TBD_ |

[Back to top](#quick-jump)
