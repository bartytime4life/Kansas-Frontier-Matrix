<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-NEEDS-UUID-PROV-STAC-DCAT
title: KFM Provenance + Catalog Mapping (PROV / STAC / DCAT)
type: standard
version: v1
status: draft
owners: TODO-VERIFY-OWNERS
created: TODO-VERIFY-CREATED-DATE
updated: 2026-04-27
policy_label: public
related: [
  docs/architecture/CONTROL_PLANE_INDEX.md,
  docs/registers/schema_registry.md,
  docs/registers/source_registry.md,
  docs/adr/TODO-PROV-STAC-DCAT.md,
  docs/adr/TODO-SCHEMA-HOME.md,
  docs/adr/TODO-STAC-DCAT-PROV-VERSION-PINS.md
]
tags: [kfm, provenance, prov, stac, dcat, receipts, proof-objects, catalog, promotion, governance]
notes: [Draft profile; paths, owners, doc_id, created date, schema home, and version pins require repo verification before publication.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Provenance + Catalog Mapping

Evidence-first profile for binding **EvidenceBundle**, **run_receipt**, promoted artifacts, and outward catalog records without weakening KFM’s trust membrane.

![Status: draft](https://img.shields.io/badge/status-draft-yellow)
![Policy: public--review](https://img.shields.io/badge/policy-public--review-lightgrey)
![Evidence: corpus--led](https://img.shields.io/badge/evidence-corpus--led-blue)
![Implementation: proposed](https://img.shields.io/badge/implementation-proposed-orange)

> [!IMPORTANT]
> **CONFIRMED doctrine:** KFM treats evidence, policy, review state, provenance, and release state as load-bearing.  
> **PROPOSED profile:** this document defines how promoted artifacts should map into **PROV**, **STAC**, and **DCAT**.  
> **UNKNOWN implementation depth:** this editing pass did not verify a mounted repository, schema registry, CI workflow, route, validator, or emitted catalog object.

---

## Quick jump

- [Purpose](#purpose)
- [Repo fit](#repo-fit)
- [Version posture](#version-posture)
- [One-minute model](#one-minute-model)
- [Core mapping: KFM → PROV](#core-mapping-kfm--prov)
- [PROV sidecar contract](#prov-sidecar-contract)
- [STAC mapping](#stac-mapping)
- [DCAT mapping](#dcat-mapping)
- [Catalog closure rules](#catalog-closure-rules)
- [Attestation and integrity](#attestation-and-integrity)
- [Proposed file layout](#proposed-file-layout)
- [Validation and policy gates](#validation-and-policy-gates)
- [Definition of done](#definition-of-done)
- [Open ADRs and verification backlog](#open-adrs-and-verification-backlog)

---

## Purpose

Define a portable, inspectable provenance and catalog profile that keeps KFM’s proof objects connected across release, catalog, UI, and downstream harvesting surfaces.

This document exists to make the following rule operational:

> A public KFM artifact is not “published” merely because a file exists. It is published only when the artifact, evidence, provenance, rights, sensitivity posture, catalog entries, receipts, and release state resolve as a governed set.

### This profile should

- keep **EvidenceBundle** sovereign rather than merging it into catalog metadata;
- keep **run_receipt**, **ai_receipt**, **redaction_receipt**, proof bundle, and release manifest as distinct objects;
- map KFM release objects into interoperable **PROV**, **STAC**, and **DCAT** surfaces;
- preserve `spec_hash` and artifact digests as deterministic identity anchors;
- support Evidence Drawer and Focus Mode without exposing canonical stores or raw model output;
- fail closed when provenance, rights, sensitivity, or catalog closure cannot be verified.

### This profile does not

- define the canonical EvidenceBundle schema;
- define every lane-specific STAC or DCAT extension;
- activate live source connectors;
- authorize public release of sensitive geometry;
- replace promotion, policy, review, or release manifests;
- prove that any target repo file, validator, workflow, or route already exists.

[↑ Back to top](#top)

---

## Repo fit

| Item | Status | Value |
|---|---:|---|
| Suggested path | **PROPOSED** | `docs/architecture/provenance_catalog_mapping.md` |
| Document role | **PROPOSED** | Standard architecture/profile document for outward provenance and catalog closure |
| Upstream objects | **PROPOSED** | `SourceDescriptor`, canonical spec, `EvidenceBundle`, `run_receipt`, `policy_decision`, `release_manifest`, optional `ai_receipt`, optional `redaction_receipt` |
| Downstream consumers | **PROPOSED** | STAC catalog, DCAT catalog, PROV sidecars, release review, Evidence Drawer, Focus Mode, export/harvest tools |
| Machine-contract home | **NEEDS VERIFICATION** | `schemas/contracts/v1/...` vs `contracts/...` requires ADR before implementation |
| Public data path | **PROPOSED** | governed API and published catalog artifacts only; no public RAW/WORK/QUARANTINE path |

### Accepted inputs

A provenance/catalog export may consume only release-eligible inputs:

| Input | Required? | Notes |
|---|---:|---|
| Promoted artifact digest | Yes | Artifact bytes must hash to the release manifest digest. |
| EvidenceBundle reference | Yes | Must resolve before catalog publication. |
| `run_receipt` | Yes | Captures process memory for the generating activity. |
| SourceDescriptor reference | Yes | Required for source role, rights, and authority posture. |
| Policy decision | Yes | Must permit the requested release class. |
| Review state | Yes | Must satisfy the lane’s release burden. |
| `ai_receipt` | Conditional | Required only if model mediation contributed to the published claim or summary. |
| `redaction_receipt` | Conditional | Required when geometry, attributes, or timing were transformed for public safety. |
| Attestation bundle | Conditional | Required when release policy demands signing or integrity proof. |

### Exclusions

| Excluded from this profile | Where it belongs instead |
|---|---|
| RAW, WORK, or QUARANTINE records | Source lifecycle and ingest policy docs |
| Canonical schema definitions | Schema registry / contract docs |
| Live connector code | Pipeline implementation docs |
| Emergency or life-safety instruction | Official source guidance, not KFM catalog prose |
| Unreviewed generated summaries | Governed AI receipts, evaluator outputs, and review queues |
| Exact sensitive locations | Restricted access surfaces or generalized public derivatives with redaction receipts |

[↑ Back to top](#top)

---

## Version posture

The standards below support the profile. They do not replace KFM-specific contracts, policy gates, or release decisions.

| Surface | External status | KFM posture |
|---|---|---|
| **PROV-O** | **CONFIRMED standard basis** | Use for lineage sidecars: entities, activities, agents, and generated/used/attributed relationships. |
| **STAC** | **CONFIRMED standard basis / NEEDS VERSION PIN** | Use for itemized geospatial asset discovery. Pin STAC target version in ADR before implementation. |
| **DCAT v3** | **CONFIRMED standard basis** | Use for dataset/distribution discovery, access rights, and federation-friendly catalog records. |
| **Sigstore / DSSE-style bundles** | **PROPOSED integrity mechanism** | Use as attestation/proof material when policy requires it; do not collapse into provenance or receipts. |
| **KFM `kfm:` namespace** | **PROPOSED local profile** | Use only for KFM-specific fields not provided by the external standard. Publish a schema before relying on it in CI. |

> [!WARNING]
> If existing repo tooling already pins a different STAC, DCAT profile, or provenance serialization, do not silently migrate. Record the decision in an ADR, add fixtures, and run a closure validator before changing public output.

[↑ Back to top](#top)

---

## One-minute model

```mermaid
flowchart LR
  subgraph Lifecycle["KFM governed lifecycle"]
    RAW[RAW] --> WORK[WORK / QUARANTINE]
    WORK --> PROCESSED[PROCESSED]
    PROCESSED --> CATALOG[CATALOG / TRIPLET]
    CATALOG --> PUBLISHED[PUBLISHED]
  end

  subgraph Proof["Proof objects"]
    EB[EvidenceBundle]
    RR[run_receipt]
    RM[release_manifest]
    PD[policy_decision]
    AR[attestation bundle]
  end

  subgraph Outward["Outward surfaces"]
    PROV[PROV sidecar]
    STAC[STAC item / collection]
    DCAT[DCAT dataset / distribution]
    UI[Evidence Drawer / Focus Mode]
  end

  PUBLISHED --> RM
  RM --> EB
  RM --> RR
  RM --> PD
  RM -. if required .-> AR
  RM --> PROV
  RM --> STAC
  RM --> DCAT
  STAC --> UI
  PROV --> UI
  DCAT --> UI
```

**Operating rule:** STAC and DCAT make released artifacts discoverable. PROV explains how the released artifact was generated. EvidenceBundle remains the stronger KFM evidence object.

[↑ Back to top](#top)

---

## Core mapping: KFM → PROV

| KFM object | PROV class/property | Profile role | Requirement |
|---|---|---|---:|
| EvidenceBundle | `prov:Entity` | Released evidence-bearing artifact or evidence reference target | Required |
| Canonical spec | `prov:Entity` | Input definition used by the run | Required |
| SourceDescriptor | `prov:Entity` | Source identity and authority context used by the run | Required |
| Pipeline run | `prov:Activity` | Transformation, derivation, export, or promotion activity | Required |
| `run_receipt` | `prov:Entity` | Process memory linked to the activity | Required |
| Signer / service / steward | `prov:Agent` | Responsible software or human/steward actor | Required |
| `ai_receipt` | `prov:Entity` | Model-mediated interpretive trace | Conditional |
| `redaction_receipt` | `prov:Entity` | Geoprivacy or sensitivity transform record | Conditional |
| Attestation bundle | `prov:Entity` | Integrity proof or signature verification material | Conditional |

### Required relations

| Relation | Meaning |
|---|---|
| `prov:wasGeneratedBy` | Artifact or EvidenceBundle was generated by a pipeline or release activity. |
| `prov:used` | Activity used a spec, source descriptor, input artifact, or EvidenceBundle. |
| `prov:wasAttributedTo` | Artifact is attributed to a signer, service, steward, or responsible system. |
| `prov:wasAssociatedWith` | Activity was associated with an agent. |
| `prov:wasDerivedFrom` | Derived artifact was produced from an earlier artifact or source. |

> [!NOTE]
> KFM receipts are not automatically authoritative truth. They are auditable process memory. EvidenceBundle, policy decision, review state, and release state still determine whether a public claim may be made.

[↑ Back to top](#top)

---

## PROV sidecar contract

### Placement rule

Each published artifact **SHOULD** include a colocated PROV sidecar. A release policy **MAY** escalate this to **MUST** for public or semi-public artifacts.

```text
artifact.ext
artifact.prov.jsonld
artifact.bundle.json        # conditional; attestation/proof bundle
artifact.release.json        # release manifest or release reference, if colocated
```

### Minimum fields

| Field | Required? | Purpose |
|---|---:|---|
| `@context` | Yes | Namespaces for PROV, DCTERMS, KFM, and optional checksum terms. |
| Artifact entity | Yes | Identifies the released artifact, EvidenceBundle, digest, license, and release subject. |
| Activity | Yes | Identifies the pipeline or promotion activity and its inputs. |
| Agent | Yes | Identifies the responsible signer, system, steward, or service. |
| `prov:wasGeneratedBy` | Yes | Binds output to activity. |
| `prov:used` | Yes | Binds activity to spec, source, and input evidence. |
| `prov:wasAttributedTo` | Yes | Binds artifact to responsible agent. |
| Receipt links | Yes | Links `run_receipt` and conditional receipts without merging them into the artifact. |
| Policy/release links | Yes | Binds provenance to release state and policy decision. |

### Minimal JSON-LD shape

> [!TIP]
> This is a **profile example**, not final schema authority. Move the machine contract into the verified schema home after the schema-home ADR is resolved.

```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "dct": "http://purl.org/dc/terms/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "kfm": "https://kfm.local/ns#"
  },
  "@graph": [
    {
      "@id": "kfm://artifact/TODO-ARTIFACT-ID",
      "@type": ["prov:Entity", "kfm:PublishedArtifact"],
      "dct:identifier": "kfm://artifact/TODO-ARTIFACT-ID",
      "dct:license": "TODO-LICENSE-URI",
      "kfm:evidence_bundle": { "@id": "kfm://evidence/TODO-EVIDENCE-ID" },
      "kfm:release_manifest": { "@id": "kfm://release/TODO-RELEASE-ID" },
      "kfm:spec_hash": "sha256:TODO-SPEC-HASH",
      "kfm:artifact_digest": "sha256:TODO-ARTIFACT-DIGEST",
      "prov:wasGeneratedBy": { "@id": "kfm://run/TODO-RUN-ID" },
      "prov:wasAttributedTo": { "@id": "kfm://agent/TODO-AGENT-ID" }
    },
    {
      "@id": "kfm://run/TODO-RUN-ID",
      "@type": ["prov:Activity", "kfm:PipelineRun"],
      "prov:used": [
        { "@id": "kfm://spec/TODO-SPEC-ID" },
        { "@id": "kfm://source/TODO-SOURCE-ID" },
        { "@id": "kfm://evidence/TODO-EVIDENCE-ID" }
      ],
      "prov:wasAssociatedWith": { "@id": "kfm://agent/TODO-AGENT-ID" },
      "prov:endedAtTime": {
        "@value": "2026-04-27T00:00:00Z",
        "@type": "xsd:dateTime"
      },
      "kfm:run_receipt": { "@id": "kfm://receipt/run/TODO-RUN-RECEIPT-ID" },
      "kfm:policy_decision": { "@id": "kfm://policy-decision/TODO-POLICY-ID" }
    },
    {
      "@id": "kfm://receipt/run/TODO-RUN-RECEIPT-ID",
      "@type": ["prov:Entity", "kfm:RunReceipt"],
      "kfm:receipt_digest": "sha256:TODO-RECEIPT-DIGEST"
    },
    {
      "@id": "kfm://agent/TODO-AGENT-ID",
      "@type": "prov:SoftwareAgent",
      "dct:identifier": "TODO-SYSTEM-OR-SIGNER-ID"
    }
  ]
}
```

### Conditional receipt nodes

Add these only when they apply:

| Receipt | Include when | Public handling |
|---|---|---|
| `ai_receipt` | AI contributed to a released summary, claim draft, interpretation, or Focus Mode response | Public pointer may be allowed; chain-of-thought is not a KFM truth object. |
| `redaction_receipt` | Geometry, timing, or attributes were generalized, suppressed, delayed, or otherwise transformed | Public pointer should explain transform class without revealing restricted detail. |
| `review_receipt` | Steward, reviewer, or separation-of-duty review is required | Public pointer depends on policy and reviewer privacy. |
| `withdrawal_receipt` | Artifact was corrected, superseded, withdrawn, or rolled back | Public correction lineage should remain discoverable. |

[↑ Back to top](#top)

---

## STAC mapping

STAC carries itemized geospatial asset discovery. It should remain lightweight and link outward to KFM proof objects.

### Required KFM profile fields

| STAC location | Field | Requirement | Purpose |
|---|---|---:|---|
| `id` | release-scoped item id | Required | Stable discovery id for the promoted artifact. |
| `stac_version` | pinned STAC version | Required | Must match ADR-approved target. |
| `properties` | `kfm:spec_hash` | Required | Deterministic spec identity. |
| `properties` | `kfm:release_id` | Required | ReleaseManifest subject. |
| `properties` | `kfm:evidence_bundle_id` | Required | EvidenceBundle pointer. |
| `properties` | `kfm:policy_label` | Required | Release/sensitivity class visible to clients. |
| `properties` | `kfm:review_state` | Required | Review burden visible to clients. |
| `assets.data` | `href`, `type`, digest field | Required | Artifact access and integrity check. |
| `assets.provenance` | PROV sidecar asset | Required for public release unless policy says otherwise | Machine-readable lineage pointer. |
| `assets.attestation` | attestation bundle asset | Conditional | Integrity/signature proof. |
| `links` | `rel=provenance` | Required | Discoverable PROV sidecar. |
| `links` | `rel=attestation` | Conditional | Discoverable signature/proof bundle. |

### STAC Item profile example

```json
{
  "type": "Feature",
  "stac_version": "1.1.0",
  "stac_extensions": [
    "TODO-PIN-KFM-STAC-EXTENSION-SCHEMA",
    "TODO-PIN-CHECKSUM-EXTENSION-IF-USED"
  ],
  "id": "kfm-example-artifact-TODO",
  "geometry": null,
  "bbox": null,
  "properties": {
    "datetime": "2026-04-27T00:00:00Z",
    "kfm:spec_hash": "sha256:TODO-SPEC-HASH",
    "kfm:release_id": "kfm://release/TODO-RELEASE-ID",
    "kfm:evidence_bundle_id": "kfm://evidence/TODO-EVIDENCE-ID",
    "kfm:policy_label": "public",
    "kfm:review_state": "reviewed",
    "kfm:rights_state": "verified",
    "processing:software": "kfm-pipeline",
    "processing:version": "TODO-PIPELINE-VERSION",
    "processing:datetime": "2026-04-27T00:00:00Z"
  },
  "assets": {
    "data": {
      "href": "../../published/example/artifact.ext",
      "type": "application/octet-stream",
      "roles": ["data"],
      "title": "Published KFM artifact",
      "kfm:artifact_digest": "sha256:TODO-ARTIFACT-DIGEST"
    },
    "provenance": {
      "href": "../../published/example/artifact.prov.jsonld",
      "type": "application/ld+json",
      "roles": ["metadata", "provenance"],
      "title": "PROV sidecar"
    },
    "attestation": {
      "href": "../../published/example/artifact.bundle.json",
      "type": "application/json",
      "roles": ["metadata", "attestation"],
      "title": "Attestation bundle"
    }
  },
  "links": [
    {
      "rel": "provenance",
      "href": "../../published/example/artifact.prov.jsonld",
      "type": "application/ld+json"
    },
    {
      "rel": "attestation",
      "href": "../../published/example/artifact.bundle.json",
      "type": "application/json"
    },
    {
      "rel": "via",
      "href": "../../published/example/artifact.release.json",
      "type": "application/json",
      "title": "KFM release manifest"
    }
  ]
}
```

> [!CAUTION]
> STAC asset links must not bypass KFM access policy. Restricted, steward-only, or sensitive derivatives need either governed URLs, generalized public artifacts, or no public asset link.

[↑ Back to top](#top)

---

## DCAT mapping

DCAT carries dataset and distribution discovery. Use it to make release objects harvestable while preserving rights, access, and provenance references.

### Required DCAT profile fields

| DCAT location | Field | Requirement | Purpose |
|---|---|---:|---|
| Dataset | `dct:identifier` | Required | Release-scoped dataset id. |
| Dataset | `dct:title` | Required | Human-readable name. |
| Dataset | `dct:license` | Required | Legal reuse posture. Must not be unknown for public release. |
| Dataset | `dct:accessRights` | Required | Public/restricted/suppressed access posture. |
| Dataset | `dct:provenance` | Required | Pointer to PROV sidecar or provenance statement. |
| Dataset | `dcat:distribution` | Required | Published artifact distributions. |
| Distribution | `dcat:accessURL` or `dcat:downloadURL` | Required | Access point, governed if needed. |
| Distribution | `dcat:mediaType` | Recommended | Artifact MIME/media type. |
| Distribution | digest/checksum field | Required by KFM profile | Must match release manifest digest. |
| Distribution | `kfm:evidence_bundle_id` | Required by KFM profile | EvidenceBundle pointer. |

### DCAT JSON-LD profile example

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#",
    "kfm": "https://kfm.local/ns#"
  },
  "@id": "kfm://dataset/TODO-DATASET-ID",
  "@type": "dcat:Dataset",
  "dct:identifier": "kfm://dataset/TODO-DATASET-ID",
  "dct:title": "TODO KFM Published Dataset Title",
  "dct:license": "TODO-LICENSE-URI",
  "dct:accessRights": "public",
  "dct:provenance": {
    "@id": "kfm://artifact/TODO-ARTIFACT-ID/provenance"
  },
  "kfm:release_id": "kfm://release/TODO-RELEASE-ID",
  "kfm:evidence_bundle_id": "kfm://evidence/TODO-EVIDENCE-ID",
  "kfm:spec_hash": "sha256:TODO-SPEC-HASH",
  "dcat:distribution": [
    {
      "@id": "kfm://distribution/TODO-DISTRIBUTION-ID",
      "@type": "dcat:Distribution",
      "dcat:accessURL": "https://catalog.example.invalid/kfm/published/example/artifact.ext",
      "dcat:mediaType": "application/octet-stream",
      "kfm:artifact_digest": "sha256:TODO-ARTIFACT-DIGEST",
      "kfm:provenance_url": "https://catalog.example.invalid/kfm/published/example/artifact.prov.jsonld",
      "kfm:attestation_url": "https://catalog.example.invalid/kfm/published/example/artifact.bundle.json"
    }
  ]
}
```

> [!NOTE]
> `https://catalog.example.invalid/...` is a placeholder. Replace it with the governed catalog or API host selected by deployment policy.

[↑ Back to top](#top)

---

## Catalog closure rules

Catalog closure means the release subject can be reconstructed across release manifest, EvidenceBundle, PROV, STAC, and DCAT without relying on guesswork.

| Closure check | PASS condition | DENY condition |
|---|---|---|
| Release subject | Same `release_id` or resolvable release subject appears in STAC, DCAT, and PROV. | Catalog records point to different subjects. |
| Artifact digest | STAC asset digest, DCAT distribution digest, PROV artifact digest, and ReleaseManifest digest match. | Missing or mismatched digest. |
| Spec identity | `kfm:spec_hash` matches canonical spec hash used by the run. | Missing, unstable, or recomputed mismatch. |
| Evidence resolution | `EvidenceRef` resolves to the expected EvidenceBundle. | Missing, inaccessible, stale, or mismatched EvidenceBundle. |
| Rights | License and access rights are verified for the requested release class. | Unknown license, unknown access rights, or source terms prohibit release. |
| Sensitivity | Public artifact is safe for its policy class and has required redaction receipt if transformed. | Restricted geometry, sensitive attributes, or unrecorded transform reaches public surface. |
| Provenance | PROV sidecar includes generated/used/attributed relations and links receipts. | Sidecar missing or does not connect artifact to run and inputs. |
| Attestation | Required bundle is present and verifies against artifact digest. | Required attestation missing, unverifiable, or digest-mismatched. |

### Minimal closure matrix

```yaml
release_id: kfm://release/TODO-RELEASE-ID
artifact_digest: sha256:TODO-ARTIFACT-DIGEST
spec_hash: sha256:TODO-SPEC-HASH
checks:
  release_manifest:
    subject_matches: true
    artifact_digest_matches: true
  evidence_bundle:
    resolves: true
    evidence_digest_matches: true
  prov_sidecar:
    was_generated_by_run: true
    used_spec_and_source: true
    attributed_to_agent: true
  stac:
    item_id_matches_release_subject: true
    asset_digest_matches: true
    provenance_link_resolves: true
  dcat:
    dataset_identifier_matches_release_subject: true
    distribution_digest_matches: true
    access_rights_verified: true
  policy:
    rights_not_unknown: true
    sensitivity_allowed: true
    restricted_geometry_absent: true
  attestation:
    required: true
    present: true
    verifies: true
```

[↑ Back to top](#top)

---

## Attestation and integrity

KFM should keep integrity proofs separate from provenance and receipts.

| Object | What it proves | What it does not prove |
|---|---|---|
| PROV sidecar | Lineage: what generated what, using which inputs, associated with which agent. | Artifact bytes are untampered unless digests/signatures also verify. |
| `run_receipt` | Process memory: execution metadata, inputs, outputs, decisions, failures. | The published claim is true or policy-approved by itself. |
| EvidenceBundle | Evidence support for a claim or artifact. | That release policy was satisfied unless linked to review/policy state. |
| Attestation bundle | Integrity/origin/signature material for artifact or statement. | Rights, sensitivity, or claim correctness by itself. |
| ReleaseManifest | Release subject and closure spine. | Source authority or evidence validity by itself. |

### Supported mechanisms

| Mechanism | Status | Placement |
|---|---|---|
| Sigstore bundle | **PROPOSED / NEEDS TOOLCHAIN VERIFICATION** | `artifact.bundle.json` and STAC/DCAT links |
| DSSE envelope | **PROPOSED / NEEDS POLICY DECISION** | Attestation content or proof bundle |
| Digest-only manifest | **PROPOSED fallback** | ReleaseManifest, PROV sidecar, STAC/DCAT digest fields |

> [!IMPORTANT]
> If policy requires attestation and the bundle fails verification, the public release must stop even if STAC, DCAT, and PROV files are present.

[↑ Back to top](#top)

---

## Proposed file layout

All paths in this section are **PROPOSED** until the real repo layout is verified.

```text
data/
  published/
    <lane>/
      <release-id>/
        artifact.ext
        artifact.prov.jsonld
        artifact.bundle.json          # conditional
        artifact.release.json         # release manifest or release pointer

  catalog/
    stac/
      <lane>/
        collection.json
        items/
          <release-id>.json
    dcat/
      <lane>/
        dataset.<release-id>.jsonld
    prov/
      <lane>/
        artifact.<release-id>.prov.jsonld

schemas/
  contracts/
    v1/
      catalog/
        kfm_prov_sidecar.schema.json
        kfm_stac_profile.schema.json
        kfm_dcat_profile.schema.json
        kfm_catalog_closure.schema.json

policy/
  catalog/
    catalog_closure.rego
    provenance_release.rego
    sensitivity_publication.rego

tests/
  fixtures/
    catalog/
      valid/
      invalid/
      deny/
```

### Layout rules

- Published artifacts remain downstream of promotion; publication is not a file move.
- Catalog records may be rebuilt from release manifests and proof objects.
- Sidecars may be colocated with artifacts and mirrored into catalog/provenance folders for harvesting.
- Public clients should resolve through governed APIs or published catalog surfaces, never internal canonical stores.
- Checksums and release identifiers must remain stable across mirrored copies.

[↑ Back to top](#top)

---

## Validation and policy gates

### Required checks before publication

| Gate | Outcome grammar | Required behavior |
|---|---|---|
| Evidence resolution | `PASS` / `DENY` | `EvidenceRef` resolves to the expected EvidenceBundle. |
| Stable identity | `PASS` / `DENY` | `spec_hash` recomputes under the approved canonicalization rule. |
| Artifact integrity | `PASS` / `DENY` | Artifact digest matches release manifest and catalog references. |
| Provenance sidecar | `PASS` / `DENY` | PROV sidecar exists and links artifact, run, inputs, and agent. |
| Rights | `PASS` / `DENY` | License and source terms allow the requested release. Unknown rights deny public release. |
| Sensitivity | `PASS` / `DENY` | Release class is compatible with geometry and attributes. |
| Redaction | `PASS` / `DENY` / `NOT_APPLICABLE` | Required transform receipt exists when public geometry or attributes are generalized/suppressed. |
| Attestation | `PASS` / `DENY` / `NOT_REQUIRED` | Required bundle is present and verifies. |
| Cross-catalog closure | `PASS` / `DENY` | STAC, DCAT, PROV, and ReleaseManifest identify the same release subject and digest. |
| Public surface check | `PASS` / `DENY` | No public URL exposes RAW, WORK, QUARANTINE, restricted, or unreviewed data. |

### DENY conditions

Publication must fail closed when any of these are true:

- provenance sidecar is missing when required;
- `run_receipt` is missing;
- EvidenceBundle cannot be resolved;
- `spec_hash` is missing or unstable;
- license, source terms, or access rights are unknown;
- policy class does not permit the requested release;
- restricted coordinates or attributes appear in a public DTO/catalog record;
- required redaction receipt is missing;
- catalog records disagree on release id or artifact digest;
- required attestation is absent or fails verification;
- public links bypass governed access controls.

### Illustrative policy input

```json
{
  "release_id": "kfm://release/TODO-RELEASE-ID",
  "release_class": "public",
  "artifact_digest": "sha256:TODO-ARTIFACT-DIGEST",
  "spec_hash": "sha256:TODO-SPEC-HASH",
  "rights_state": "verified",
  "sensitivity_state": "public_safe",
  "evidence_bundle_resolves": true,
  "run_receipt_present": true,
  "prov_sidecar_present": true,
  "catalog_closure_passed": true,
  "attestation": {
    "required": true,
    "present": true,
    "verified": true
  },
  "public_surface": {
    "contains_restricted_geometry": false,
    "uses_governed_access_url": true
  }
}
```

[↑ Back to top](#top)

---

## Definition of done

A provenance/catalog mapping slice is ready for review when:

- [ ] `doc_id`, owners, created date, and related links are verified or explicitly accepted as placeholders.
- [ ] Schema-home ADR is resolved.
- [ ] STAC, DCAT, and PROV versions/profiles are pinned.
- [ ] `kfm:` extension fields have a published schema or profile note.
- [ ] Valid, invalid, and deny fixtures exist for PROV, STAC, DCAT, and catalog closure.
- [ ] Policy gates deny unknown rights and public restricted geometry.
- [ ] Example public artifact has a matching release manifest, EvidenceBundle pointer, run receipt, PROV sidecar, STAC item, DCAT dataset, and optional attestation bundle.
- [ ] Evidence Drawer can display provenance, rights, review state, and release state from governed surfaces.
- [ ] Focus Mode can answer only from released, policy-safe EvidenceBundle context or abstain.
- [ ] Rollback or correction flow preserves previous catalog records with visible supersession/withdrawal lineage.

[↑ Back to top](#top)

---

## Open ADRs and verification backlog

| Item | Status | Why it matters |
|---|---:|---|
| ADR: schema home | **NEEDS VERIFICATION** | Prevents divergence between `contracts/` and `schemas/contracts/v1/`. |
| ADR: STAC target version and extensions | **NEEDS VERIFICATION** | Avoids silent change from existing STAC tooling. |
| ADR: DCAT profile and checksum vocabulary | **NEEDS VERIFICATION** | Defines digest/access-rights fields for harvesters. |
| ADR: PROV serialization | **NEEDS VERIFICATION** | Decides JSON-LD profile, PROV-JSON, or both. |
| ADR: canonical JSON / JCS enforcement | **PROPOSED** | Required for stable `spec_hash`. |
| ADR: attestation baseline | **PROPOSED** | Decides Sigstore bundle, DSSE, digest-only fallback, or layered policy. |
| ADR: public access-rights vocabulary | **PROPOSED** | Prevents inconsistent `public`, `restricted`, `suppressed`, `steward_only`, and similar labels. |
| Validator: cross-catalog closure | **PROPOSED** | Checks release id, artifact digest, EvidenceBundle, PROV, STAC, and DCAT as one set. |
| Fixture: sensitive release deny case | **PROPOSED** | Proves exact restricted geometry cannot leak through public catalog records. |

[↑ Back to top](#top)

---

<details>
<summary><strong>Appendix A — Compact KFM field map</strong></summary>

| KFM field | PROV | STAC | DCAT | Notes |
|---|---|---|---|---|
| `release_id` | `kfm:release_manifest` / entity id | `properties.kfm:release_id` | `kfm:release_id` | Release subject must close across all surfaces. |
| `spec_hash` | `kfm:spec_hash` | `properties.kfm:spec_hash` | `kfm:spec_hash` | Hash canonicalization must be pinned elsewhere. |
| `artifact_digest` | `kfm:artifact_digest` | asset digest field | distribution digest field | Digest field vocabulary must be pinned. |
| `evidence_bundle_id` | `kfm:evidence_bundle` | `properties.kfm:evidence_bundle_id` | `kfm:evidence_bundle_id` | Must resolve before release. |
| `run_receipt_id` | `kfm:run_receipt` | link or property | `kfm:run_receipt_id` if public | Public exposure may depend on policy. |
| `policy_label` | `kfm:policy_decision` | `properties.kfm:policy_label` | `dct:accessRights` + `kfm:policy_label` | Use a controlled vocabulary. |
| `review_state` | `kfm:review_state` | `properties.kfm:review_state` | `kfm:review_state` | Review state is not the same as policy label. |
| `license` | `dct:license` | asset/link license field or KFM property | `dct:license` | Unknown license denies public release. |
| `provenance_url` | sidecar id | `links[rel=provenance]` | `dct:provenance` / `kfm:provenance_url` | Must resolve to sidecar. |
| `attestation_url` | attestation entity | `links[rel=attestation]` | `kfm:attestation_url` | Conditional by release policy. |

</details>

<details>
<summary><strong>Appendix B — Review checklist for maintainers</strong></summary>

- Does the document preserve the KFM lifecycle and trust membrane?
- Are all implementation claims labeled as PROPOSED or UNKNOWN unless verified?
- Are external standard versions pinned or marked NEEDS VERIFICATION?
- Are public release gates fail-closed?
- Are EvidenceBundle, receipts, proofs, manifests, catalogs, and attestations kept distinct?
- Are sensitive-location and rights failures represented as DENY conditions?
- Are examples clearly examples rather than implementation proof?
- Are placeholders reviewable and easy to find?

</details>

---

<a href="#top">↑ Back to top</a>
