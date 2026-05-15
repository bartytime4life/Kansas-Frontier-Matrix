<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0017-source-descriptor-admission-process
title: ADR-0017 — Source Descriptor Admission Process
type: adr
version: v1.1
status: proposed
owners: ["@kfm-source-stewards", "@kfm-governance-stewards"]
created: 2026-05-09
updated: 2026-05-15
policy_label: public
related:
  - docs/adr/ADR-0001-schema-home.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/truth-posture.md
  - docs/doctrine/trust-membrane.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - contracts/source/_TEMPLATE_source_descriptor.md
  - schemas/contracts/v1/sources/source_descriptor.schema.json
  - schemas/contracts/v1/sources/source_admission_rules.schema.json
  - control_plane/source_authority_register.yaml
tags: ["adr", "source", "admission", "governance", "lifecycle"]
notes: "v1.1 strengthens Directory Rules alignment, repo-evidence boundaries, activation-decision fields, validation gates, and pilot acceptance criteria. Status remains proposed until reviewed by source and governance stewards and reconciled against mounted-repo state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0017 — Source Descriptor Admission Process

> The gate at which **the world** becomes **KFM-admissible evidence**.
> No source enters the lifecycle without an admitted descriptor; no descriptor is admitted without a record-level admission contract.

> [!IMPORTANT]
> **Status:** `proposed`  
> **Owner:** `@kfm-source-stewards` · `@kfm-governance-stewards`  
> **Target path:** `docs/adr/ADR-0017-source-descriptor-admission-process.md` — **PROPOSED** until mounted-repo inspection confirms ADR naming convention  
> **Truth posture:** CONFIRMED doctrine where supported by attached corpus; PROPOSED implementation/file homes; UNKNOWN current repo depth

| Label | Meaning in this ADR |
|---|---|
| **CONFIRMED** | Supported by attached KFM doctrine or the existing ADR baseline. |
| **PROPOSED** | Recommended design, path, contract, validator, policy, or workflow not verified in the mounted repo. |
| **UNKNOWN** | Not verified because repo files, tests, workflows, dashboards, logs, or emitted artifacts were not inspected. |
| **NEEDS VERIFICATION** | Checkable before acceptance or implementation, but not checked strongly enough here. |
| **OPEN** | A design choice this ADR intentionally leaves for pilot evidence or successor decision. |

| Field | Value |
|---|---|
| **ADR ID** | ADR-0017 |
| **Title** | Source Descriptor Admission Process |
| **Status** | `proposed` |
| **Date** | 2026-05-09 |
| **Last updated** | 2026-05-15 |
| **Decision class** | Governance — source intake, lifecycle gate |
| **Authors** | _placeholder — confirm at acceptance_ |
| **Reviewers required** | Source steward · Governance steward · Rights/sensitivity reviewer · Release steward (separation of duties) |
| **Proposed target path** | `docs/adr/ADR-0017-source-descriptor-admission-process.md` — **PROPOSED** until mounted repo inspection confirms ADR naming convention |
| **Supersedes** | _none_ |
| **Superseded by** | _none_ |
| **Related ADRs** | ADR-0001 schema home _(referenced; verify acceptance state in mounted repo — **NEEDS VERIFICATION**)_ |
| **Related doctrine** | Directory Rules; lifecycle law (RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED); truth posture (cite-or-abstain); trust membrane; watcher-as-non-publisher |
| **Conformance language** | RFC 2119-style: MUST · SHOULD · MAY |
| **Truth posture of this ADR** | Doctrine **CONFIRMED** where supported by attached corpus; implementation depth **UNKNOWN** without mounted repo; file paths **PROPOSED** unless verified in a repo checkout |

> [!NOTE]
> **Evidence boundary.** This ADR records doctrine and proposed repository homes. It does **not** prove that validators, schemas, policy bundles, register files, dashboards, workflows, or CODEOWNERS rules already exist in the target repository. Current implementation remains **UNKNOWN** until a mounted repo, tests, workflows, release artifacts, or logs are inspected.

---

## Table of contents

- [1. Context](#1-context)
- [2. Decision](#2-decision)
  - [2.1 Two senses of "admission"](#21-two-senses-of-admission)
  - [2.2 Descriptor-level admission: the activation flow](#22-descriptor-level-admission-the-activation-flow)
  - [2.3 Activation states](#23-activation-states)
  - [2.4 Required descriptor sections (template)](#24-required-descriptor-sections-template)
  - [2.5 Required descriptor field groups](#25-required-descriptor-field-groups)
  - [2.6 Record-level admission: minimum bar and fail-closed triggers](#26-record-level-admission-minimum-bar-and-fail-closed-triggers)
  - [2.7 Reason-code family convention](#27-reason-code-family-convention)
  - [2.8 Separation of duties](#28-separation-of-duties)
  - [2.9 Companion paths and authorities](#29-companion-paths-and-authorities)
  - [2.10 Minimum activation decision record](#210-minimum-activation-decision-record)
  - [2.11 Pilot acceptance package](#211-pilot-acceptance-package)
- [3. Consequences](#3-consequences)
- [4. Alternatives considered](#4-alternatives-considered)
- [5. Validation and enforcement](#5-validation-and-enforcement)
  - [5.1 Static checks](#51-static-checks)
  - [5.2 Fixtures](#52-fixtures)
  - [5.3 CI gate](#53-ci-gate)
  - [5.4 Re-review cadence](#54-re-review-cadence)
  - [5.5 Acceptance criteria for this ADR](#55-acceptance-criteria-for-this-adr)
  - [5.6 Non-goals and blocked shortcuts](#56-non-goals-and-blocked-shortcuts)
- [6. Rollback and supersession](#6-rollback-and-supersession)
- [7. Open questions and NEEDS VERIFICATION](#7-open-questions-and-needs-verification)
- [8. References](#8-references)

---

## 1. Context

KFM treats every governed claim as evidence-backed, policy-aware, and reversible. Source intake is the single hardest entry point in that promise: every downstream gate — validation, policy, evidence resolution, release, runtime envelope — depends on the decision that **this source** is allowed to feed **this lane** with **this role** under **this rights posture**. The failure mode is well-known and structural: when admission rules live only inside connector code, they drift silently, escape review, and are reconstructed inconsistently per source.

The project corpus is unambiguous on the doctrine. Two independent threads converge on the same conclusion:

- The **operational** view (KFM Build Companion, §8): the repository needs an *"admission office"* — a documented activation flow with explicit gates, a `SourceDescriptor` of governed minimum fields, a `SourceAuthorityRegister` entry, and an auditable `SourceActivationDecision`.[^build-co-8]
- The **doctrinal** view (Components Pass 13 Part 2, Chapter B): every authoritative source has a single Markdown descriptor with a fixed section structure. The descriptor declares both the **minimum admission bar** (what a record MUST satisfy to enter normalized form) and the **fail-closed triggers** (what blocks outward use even if the record was admitted). Descriptors are *"not a publication-rights grant"* but *"the precondition for admission into normalization."*[^pass13-srcB]

Both threads describe the same machinery from different sides. This ADR consolidates them into a single admission contract, names responsibility-rooted companion homes, and pins the conformance language so validators, registers, and gates can be built against a stable target.

> [!IMPORTANT]
> A descriptor is **not** an authorization to publish. Activation merely admits a source into normalization or candidate processing. Publication still requires rights, sensitivity, evidence-bundle, validation, catalog, review, release, correction, and rollback gates downstream.

[^build-co-8]: KFM Build Companion, §8 — *Source activation and authority: the repo needs an admission office* — including §8.1 activation flow, §8.2 minimum descriptor fields, §8.3 source-role examples by domain. Preserved from baseline; attached corpus support is doctrinal, not mounted-repo proof.
[^pass13-srcB]: KFM Components Pass 13 Part 2, §5.B Chapter B — *Source Descriptors and Source-Role Doctrine*, KFM-IDX-SRC-001 through KFM-IDX-SRC-006. iNaturalist and eBird descriptors are the most fully developed prototypes.

<sub>[⬆ Back to top](#top)</sub>

---

## 2. Decision

### 2.1 Two senses of "admission"

The corpus uses *admission* in two distinct senses. This ADR governs both, and requires every descriptor to satisfy each:

| Sense | Subject | Question answered | Owning artifact |
|---|---|---|---|
| **Descriptor-level admission** | The source itself | "Is this source allowed in KFM, in what role, under what rights, at what activation state?" | `SourceDescriptor` (Markdown) + `SourceAuthorityRegister` entry + `SourceActivationDecision` |
| **Record-level admission** | A single record from the source | "Does this individual record meet the minimum bar to enter normalized form, and is any fail-closed trigger active?" | `Source Admission Rules` section of the descriptor + per-source admission validator |

Both senses MUST resolve before any source-derived record is promoted past RAW / QUARANTINE toward processed, cataloged, triplet, or published surfaces.

> [!CAUTION]
> RAW capture and normalized admission are different questions. A source fetch MAY be preserved as RAW when source terms allow; a record that fails the minimum bar MUST NOT become a normalized KFM record and SHOULD move to QUARANTINE with a reason code.

### 2.2 Descriptor-level admission: the activation flow

The activation flow MUST follow this path. Each step emits or updates a governed artifact; no step may be skipped.

```mermaid
flowchart LR
  C["Candidate<br/>source identified"] --> D["SourceDescriptor<br/>draft"]
  D --> R["SourceRightsAssessment"]
  R --> S["SensitivityAssessment"]
  S --> A["SourceAuthorityRegister<br/>entry"]
  A --> X["SourceActivationDecision"]
  X --> F["No-network fixture<br/>(synthetic sample)"]
  F --> Y["Connector<br/>dry-run"]
  Y --> V["Validation +<br/>policy gate"]
  V --> W["Steward review"]
  W --> ST{{"Activation state"}}
  ST --> denied
  ST --> draft
  ST --> active_internal
  ST --> active_public_candidate
  ST --> retired
```

The flow above is **CONFIRMED doctrine** from the attached corpus and preserved baseline. The corresponding **6-step onboarding mechanics**, drawn from the geology dossier and stated to recur across domain dossiers, are the operational form of the same flow:[^geo-onboard]

| # | Step | Required action | Fail-closed condition |
|---|---|---|---|
| 1 | **Draft descriptor** | Create descriptor with role, rights, cadence, identity, caveats, and public-safe defaults | Missing `source_role`, `rights`, or caveats → cannot activate |
| 2 | **Endpoint / source verification** | Lock endpoint or item ID, fields, formats, ETag / Last-Modified / checksum behavior, license / terms snapshot | Unverified endpoint or terms → QUARANTINE only |
| 3 | **Fixture before live connector** | Author synthetic source-shaped fixture and pass schema, source-role, and public-safety tests | No fixture → no connector |
| 4 | **Connector dry run** | Fetch to `data/raw/` only, emit ingest receipt, **no public artifact** | Checksum, schema, or rights drift → QUARANTINE |
| 5 | **Promotion candidate** | Processed object, catalog matrix, `EvidenceBundle`, release manifest, redaction receipt if needed | Any unresolved evidence / policy / catalog mismatch → DENY |
| 6 | **Living docs update** | Update source index, dataset/layer index, evolution log, and change-impact matrix when those homes are confirmed | Docs not updated → PR fails or remains unmergeable |

> [!CAUTION]
> Step 4 enforces the **watcher-as-non-publisher** invariant. Connectors emit receipts and candidates only — they do not write to `data/published/`, mutate canonical records, or bypass review. Enforcement by CODEOWNERS, CI guards, protected paths, and release workflow checks is **PROPOSED / NEEDS VERIFICATION** until the mounted repo proves those mechanisms exist.

[^geo-onboard]: KFM Geology & Natural Resources Architecture (PDF-only report, 2026-04-21), §12.3 *Source onboarding mechanics*. The same six-step shape recurs across the per-domain dossiers (atmosphere, archaeology, fauna, flora, hazards, hydrology, settlements/infrastructure, soil, transport).

### 2.3 Activation states

A descriptor's `activation.status` MUST be one of:

| State | Meaning | Allowed downstream effect |
|---|---|---|
| `denied` | Decision: source MUST NOT be admitted | None. Record reasons in the register. |
| `draft` | Descriptor exists; no activation decision yet | Internal-only design and fixture work. No live fetch. |
| `active_internal` | Activated for internal use only | Connector may run; outputs land in `data/raw/` or `data/quarantine/`. **Public release is denied.** |
| `active_public_candidate` | Cleared for the public candidate path | Eligible for release pipelines, subject to per-record rules, evidence resolution, policy, review, and release gates. **Activation is not release.** |
| `retired` | Was admitted; now withdrawn from active use | Historical records remain; new fetches are blocked. Re-activation requires a new decision. |

The state vocabulary is **CONFIRMED doctrine** from the attached corpus. Transitions MUST be recorded as append-only entries in `control_plane/source_authority_register.yaml` or the repo's confirmed equivalent with reviewer, decision date, allowed roles, denied roles, obligations, re-review date, and rollback target.[^build-co-82]

[^build-co-82]: KFM Build Companion, §8.2, Activation field group: *"status, reviewer, decision date, allowed roles, denied roles, obligations, re-review date."* Preserved from baseline; repo presence remains **NEEDS VERIFICATION**.

### 2.4 Required descriptor sections (template)

Every descriptor MUST follow the canonical section order (the structure is repeated identically across the iNaturalist and eBird descriptors and is **CONFIRMED** as the doctrinal template):[^pass13-template]

1. `KFM_META_BLOCK_V2` header
2. **Status block** (current activation state, last decision, next re-review)
3. **Scope** — explicit `includes` / `excludes`
4. **Source identity** table — `source_id`, publisher, source family, official / aggregator / community / model / archive flags
5. **KFM working interpretation** — what the source *is* and is *not* allowed to be flattened into
6. **Accepted input shape**
7. **Source admission rules** — minimum bar + fail-closed triggers (see §2.6)
8. **Rights posture** — including the rule that rights MAY be observation-level, not source-global
9. **Geoprivacy and sensitivity posture** — explicit mapping to KFM public-safe precision
10. **Mapping table** to the canonical evidence object (e.g., `OccurrenceEvidenceObject`)
11. **Normalization notes** — taxonomy, observation shape, geometry, identity
12. **Validator pressure** — likely reason-code families (see §2.7)
13. **Runtime cautions** — checklist semantics, observation-vs-specimen, precision burdens, etc.
14. **Exclusions**
15. **Next related files**

A descriptor missing any of these sections SHOULD NOT be promoted past `draft`. A starter template SHOULD live at `contracts/source/_TEMPLATE_source_descriptor.md` (**PROPOSED** path; verify in mounted repo).

[^pass13-template]: Pass 13 Part 2, KFM-IDX-SRC-001 *— The Source Descriptor Template* (status: CONFIRMED). The corpus also notes the descriptor's primary job: *"to bound the source. It names what the source is allowed to be ingested as ... what it is not allowed to be flattened into ... what minimum bar a record must meet ... what fail-closed triggers must block outward use even if the record has been admitted."*

### 2.5 Required descriptor field groups

The descriptor MUST carry these field groups. They are **CONFIRMED doctrine** from the Build Companion table of minimum fields.[^build-co-82]

| Group | Minimum fields | Why it matters |
|---|---|---|
| **Identity** | `source_id`, `title`, `publisher`, `source_family`, `source_role`, official / aggregator / community / model / archive flags | Prevents source-role confusion |
| **Access** | `access_method`, endpoint or path, auth requirement, rate / terms notes, retrieval mode, contact / steward | Allows safe connector design and rechecks |
| **Rights** | license / terms, attribution, `public_release_allowed`, redistribution limits, commercial limits, no-assertion reason | Unknown rights block public promotion |
| **Scope** | spatial scope, temporal scope, subject scope, domain lanes, excluded uses | Prevents overbroad claims |
| **Data character** | observation / model / regulatory / archive / interpretation / administrative / derived / supporting | Controls admissibility and claim language |
| **Sensitivity** | precise-location sensitivity, living-person data, cultural / tribal / steward restrictions, infrastructure risk, rare-species risk | Fail-closed public exposure |
| **Freshness** | `update_cadence`, `stale_after`, retrieval schedule, last checked, verification required | Time-aware trust display |
| **Validation** | required schemas, fixtures, validators, known caveats, null handling, CRS / units expectations | Prevents source-specific surprises |
| **Activation** | status, reviewer, decision date, allowed roles, denied roles, obligations, re-review date | Makes activation auditable |

Where rights vary per record (e.g., iNaturalist), the descriptor MUST declare **observation-level rights** and the four normalized rights fields — `rights.license`, `rights.redistribution_allowed`, `rights.commercial_use_allowed`, `rights.attribution_required` — for downstream artifacts.[^pass13-rights]

[^pass13-rights]: Pass 13 Part 2, KFM-IDX-SRC-003 *— Observation-Level Rights and the Four Required Normalized Fields* (status: CONFIRMED).

### 2.6 Record-level admission: minimum bar and fail-closed triggers

Each descriptor MUST contain a **Source Admission Rules** section that names two explicit lists.[^pass13-srcRules]

#### 2.6.1 Minimum admission bar

The conditions a record MUST satisfy to enter normalized KFM form. The list is descriptor-specific but follows a stable shape. Reference example, from the iNaturalist descriptor (CONFIRMED from corpus):

> non-empty provider record id · taxon label · observation date · reconstructible source URI · explicit rights posture · explicit geoprivacy posture

Absence of any required item blocks normalized admission and moves the candidate record to QUARANTINE with a matching reason code. If source terms allow, the raw fetch may still be retained as RAW evidence of the attempted ingest; the failed normalized record MUST NOT be silently promoted.

#### 2.6.2 Fail-closed triggers

Conditions that block outward public-safe use **even if the record was admitted**. Reference examples (CONFIRMED):

- absent or unresolved license
- obscured / private geoprivacy without a public-safe geometry
- incomplete source identity
- unreconstructible provenance
- materially unresolved taxon
- precision too exact for the intended public surface
- runtime overstatement (e.g., presenting checklist support as exact-site truth)

A fail-closed trigger MUST cause `DENY` (for an outward decision) or `ABSTAIN` (when scope is too broad), never silent passage.

#### 2.6.3 Machine-readable mirror (PROPOSED)

To make the validator's branches map one-to-one to descriptor lines, each descriptor SHOULD ship a co-located `admission_rules.json` (or equivalent) that mirrors the prose lists. The validator loads it at startup. This is **PROPOSED** per the Pass 13 expansion direction (KFM-IDX-SRC-005, *"Suggested future work"*).

> [!TIP]
> The following example is illustrative. Field names and path placement remain **PROPOSED** until the mounted repo confirms the schema convention.

```json
{
  "source_id": "SOURCE_ID_TBD",
  "minimum_bar": [
    { "id": "prov.provider_record_id", "required": true },
    { "id": "rights.license", "required": true },
    { "id": "geom.public_safe_geometry", "required": true }
  ],
  "fail_closed_triggers": [
    { "id": "rights.unresolved_license", "outcome": "DENY" },
    { "id": "sens.exact_location_public_risk", "outcome": "DENY" },
    { "id": "prov.unreconstructible_source_uri", "outcome": "ABSTAIN" }
  ]
}
```

> [!NOTE]
> Whether `admission_rules.*` is embedded inside `KFM_META_BLOCK_V2` or lives as a sibling file is **OPEN** in the corpus and tracked in §7. Default in this ADR: sibling file.

[^pass13-srcRules]: Pass 13 Part 2, KFM-IDX-SRC-005 *— Source Admission Rules: Minimum Bar and Fail-Closed Triggers* (status: CONFIRMED).

### 2.7 Reason-code family convention

Validators emit reason codes inside fixed families so that runtime envelopes, evidence drawers, and gate reports present cautions consistently. The families are **CONFIRMED** from corpus and are non-negotiable across sources:[^pass13-reason]

| Family | Covers |
|---|---|
| `prov.*` | Provenance, source identity, reconstructible URI |
| `rights.*` | License, redistribution, commercial use, attribution |
| `geom.*` | Geometry, precision, public-safe-precision mismatch |
| `sens.*` | Sensitivity, geoprivacy, sensitive-location, living-person, cultural / tribal restrictions |
| `taxon.*` | Taxonomy resolution, name authority |
| `obs.*` | Observation semantics — checklist vs. specimen, count, methodology |

A new family MUST NOT be invented inside a single descriptor; expansion goes through this ADR's amendment path.

[^pass13-reason]: Pass 13 Part 2, KFM-IDX-SRC-006 *— Reason-Code Family Convention* (status: CONFIRMED).

### 2.8 Separation of duties

Activation MUST be the work of separated roles. No single actor MAY draft, approve, and release the same descriptor.

| Role | Responsibilities | Cannot also |
|---|---|---|
| **Source steward** | Drafts descriptor; runs onboarding mechanics; maintains fixtures | Approve activation; sign release |
| **Rights / sensitivity reviewer** | Reviews rights, sensitivity, geoprivacy posture | Author the same descriptor it reviews |
| **Governance steward** | Approves `SourceActivationDecision`; enters `SourceAuthorityRegister` row | Edit canonical truth without recorded decision |
| **Release steward** | Decides `release_state`; assembles `ReleaseManifest` | Bypass evidence / validation / policy gates |

This pattern aligns with the Master Action Matrix in `kfm_encyclopedia.pdf` §10 (CONFIRMED doctrine on separation of duties for source activation, policy result, and promotion).

### 2.9 Companion paths and authorities

Directory Rules govern placement by responsibility root: `contracts/` owns object meaning, `schemas/` owns machine-checkable shape, `policy/` owns admissibility/release decisions, `control_plane/` owns structured governance maps, `tests/` and `fixtures/` prove enforceability, and `data/` owns lifecycle data and registries.[^dir-rules]

#### 2.9.1 Descriptor and schema artifacts

| Artifact | Proposed path | Authority class | Status of path |
|---|---|---|---|
| Descriptor (Markdown) | `contracts/source/<source>_source_descriptor.md` | Object meaning | **PROPOSED** filename pattern; responsibility-root basis **CONFIRMED** by Directory Rules; mounted-repo presence **NEEDS VERIFICATION** |
| Descriptor template | `contracts/source/_TEMPLATE_source_descriptor.md` | Object meaning | **PROPOSED** |
| Descriptor contract note | `contracts/source/source_descriptor.md` | Object meaning / object-family explainer | **PROPOSED** if the repo uses object-family contract notes |
| Machine schema | `schemas/contracts/v1/sources/source_descriptor.schema.json` | Machine shape | **PROPOSED**; verify ADR-0001 and singular/plural `source(s)` convention |
| Per-source admission-rules schema | `schemas/contracts/v1/sources/source_admission_rules.schema.json` | Machine shape | **PROPOSED** |
| Per-source admission rules | `contracts/source/<source>_admission_rules.json` _(co-located with descriptor)_ | Semantic mirror of record-level rule lists | **PROPOSED**; if JSON is treated as schema-shaped data in the repo, migrate under the confirmed schema/data convention by ADR |

#### 2.9.2 Validation, policy, and test artifacts

| Artifact | Proposed path | Authority class | Status of path |
|---|---|---|---|
| Validator | `tools/validators/sources/source_descriptor_validator.*` | Repo-wide validator | **PROPOSED** |
| Policy bundle | `policy/sources/source_descriptor.rego` | Admissibility / deny-abstain rules | **PROPOSED** |
| Tests | `tests/sources/test_source_descriptor.*` | Enforceability proof | **PROPOSED** |
| Fixtures | `fixtures/sources/valid/` and `fixtures/sources/invalid/` | Golden / negative inputs | **PROPOSED** |

#### 2.9.3 Registry and decision artifacts

| Artifact | Proposed path | Authority class | Status of path |
|---|---|---|---|
| Per-domain registry | `data/registry/<domain>/sources.yaml` or `data/registry/sources/<domain>.yaml` | Source registry | **PROPOSED**; choose one after mounted repo inspection; do not maintain both without ADR |
| Authority register | `control_plane/source_authority_register.yaml` | Governance map | **PROPOSED** filename; responsibility-root basis **CONFIRMED** by Directory Rules; append-only behavior **NEEDS VERIFICATION** |
| Activation decision | recorded inside `control_plane/source_authority_register.yaml` or a confirmed sibling register | Governance map | **PROPOSED** placement; see §2.10 |

> [!IMPORTANT]
> No parallel home for source descriptors, source schemas, source registries, or source policy is permitted without an amending ADR. Per Directory Rules §2.4, creating a parallel home for schemas, contracts, policy, sources, registries, releases, proofs, or receipts MUST be ADR-gated.

[^dir-rules]: Directory Rules §0, §2.4, §4, and §6.2–§6.5. Directory Rules establish the responsibility-root split and the default schema-home convention, while specific path presence remains **PROPOSED** until mounted-repo evidence verifies it.

### 2.10 Minimum activation decision record

Every `SourceActivationDecision` MUST be inspectable, append-only, and reversible. The register row or decision object MUST carry at least:

| Field | Meaning |
|---|---|
| `decision_id` | Stable identifier for this activation decision |
| `source_id` | Descriptor source identifier |
| `descriptor_ref` | Path or URI to the descriptor version under review |
| `descriptor_digest` | Hash of the descriptor at decision time |
| `activation_status` | One of §2.3 states |
| `allowed_roles` / `denied_roles` | Source roles this source may or may not play in KFM |
| `rights_summary` | Current rights posture and release limits |
| `sensitivity_summary` | Current sensitivity / geoprivacy posture |
| `obligations` | Attribution, re-review, redaction, access, cadence, or steward obligations |
| `reviewers` | Source, governance, rights/sensitivity, and release reviewers as applicable |
| `decision_date` | Date of the decision |
| `effective_date` | Date the decision becomes active, if different |
| `re_review_date` | Required re-review date |
| `decision_receipt_ref` | Receipt or review artifact proving the decision path, if emitted |
| `supersedes_decision_id` | Prior decision replaced by this one, if any |
| `rollback_target` | Prior descriptor/register state to restore if withdrawn |
| `reason_codes` | Reason-code families supporting deny, restriction, or caution |

Fields MAY be implemented as YAML, JSON, or another repo-native structured form, but the semantics above MUST be preserved.

> [!TIP]
> The example below is illustrative, not a claim that this exact YAML file exists. It shows the minimum shape reviewers should be able to inspect.

```yaml
decision_id: SOURCE-ACTIVATION-DECISION-ID-TBD
source_id: SOURCE_ID_TBD
descriptor_ref: contracts/source/SOURCE_ID_TBD_source_descriptor.md
descriptor_digest: sha256:DESCRIPTOR_DIGEST_TBD
activation_status: draft
allowed_roles: []
denied_roles: []
rights_summary: NEEDS VERIFICATION
sensitivity_summary: NEEDS VERIFICATION
obligations:
  - re_review_required
reviewers:
  source_steward: OWNER_TBD
  governance_steward: OWNER_TBD
  rights_sensitivity_reviewer: OWNER_TBD
decision_date: 2026-05-15
effective_date: 2026-05-15
re_review_date: DATE_TBD_AFTER_REVIEW
decision_receipt_ref: kfm://receipt/NEEDS-VERIFICATION
supersedes_decision_id: null
rollback_target: ROLLBACK_TARGET_TBD
reason_codes: []
```

### 2.11 Pilot acceptance package

Before this ADR is accepted, the project SHOULD run a two-source pilot. The baseline names iNaturalist and eBird because their descriptor prototypes exercise different risks: observation-level rights, geoprivacy, taxonomy, community-science semantics, checklist semantics, and runtime overstatement.

The pilot SHOULD produce:

- [ ] two Markdown source descriptors following §2.4;
- [ ] two `admission_rules` mirrors or a documented reason for omitting mirrors;
- [ ] valid and invalid no-network fixtures;
- [ ] a descriptor validator dry run;
- [ ] `SourceActivationDecision` rows in the proposed authority register;
- [ ] a short review note showing which claims remain `PROPOSED`, `OPEN`, or `NEEDS VERIFICATION`;
- [ ] no public release unless downstream release gates independently pass.

<sub>[⬆ Back to top](#top)</sub>

---

## 3. Consequences

### 3.1 Positive

- **Auditable admission.** Implicit admission rules drift; explicit ones are reviewable, testable, and inspectable in pull-request diffs.
- **Uniform downstream surface.** Reason-code families are uniform across sources, so the runtime envelope, evidence drawer, and gate reports can present cautions consistently.
- **Separation of authorization concerns.** Activation is divorced from publication; descriptors stop being mistaken for release grants.
- **Replicable pattern.** Once two descriptors (iNaturalist, eBird) are written to this contract, any new source can be drafted by following the template, reducing the marginal cost of source onboarding.
- **CI-checkable.** Section presence, field-group presence, the activation state vocabulary, and the reason-code family prefixes are all amenable to lightweight static checks.
- **Rollback-ready.** The activation decision record names descriptor digest, decision receipt, supersession, and rollback target.

### 3.2 Negative / costs

- **Authoring overhead.** Each new source costs a multi-step descriptor + fixture + dry-run + register entry + decision before any record flows. This is the intended cost.
- **Validator cost.** Per-source admission rules ship as machine-readable mirrors; a small DSL or hand-written validator is required. The corpus prefers hand-written validators but flags the cost.[^pass13-srcRules]
- **Doc surface.** Multiple companion homes per source (descriptor, admission rules mirror, schema, validator, policy, tests, fixtures, register entry) raise the per-source doc-graph footprint.
- **Drift between Markdown prose and JSON mirror.** A CI parity check is required to keep the prose lists and `admission_rules.json` aligned.
- **Path-placement review.** Directory Rules make responsibility roots explicit; source-admission work must resist convenient but conflicting homes.

### 3.3 Risks if not adopted

- Source-global rights assumptions silently violate per-observation licenses at scale.
- "Source role" gets reinvented per connector; aggregators get treated as canonical truth; modeled surfaces get presented as observed evidence.
- Activation state lives in chat / commits / tribal memory; rollback is impossible.
- Connectors become de facto publishers because no formal descriptor + decision gate blocks outward use.

---

## 4. Alternatives considered

| Alternative | Why rejected |
|---|---|
| **No descriptor; admission rules live inside connector code** | Status quo failure mode. Rules become invisible to reviewers, drift across connectors, escape audit. The whole point of this ADR is to refuse this option. |
| **Descriptor as YAML only (no Markdown)** | Loses the *KFM working interpretation*, *runtime cautions*, *normalization notes*, and *exclusions* sections, which are inherently prose. The corpus's two prototype descriptors (iNaturalist, eBird) are Markdown for this reason. |
| **One global admission rule set across sources** | Sources differ materially: iNaturalist has observation-level rights; eBird has checklist semantics; SMAP has authenticated-federal-source ingest; KGS has interpretive map units. A global rule set would either be too loose (admits everything) or too tight (admits nothing). |
| **Embed admission rules inside `KFM_META_BLOCK_V2`** | Considered. Tracked as **OPEN** in §7. Default for now: sibling JSON file, because the lists can grow and Meta-Block-V2 is intended to stay compact. |
| **Activation decision stored in source repo only (no register)** | Loses cross-source reporting (which sources are active, stale, denied, retired, need rights recheck). The Build Companion §26.1 *Source health* dashboard requires a queryable register. |
| **Skip the no-network fixture step** | The corpus is consistent: *"No fixture → no connector."* Without a fixture, the validator and policy bundle have nothing to test against before live fetch. |
| **Use mounted repo convention even if it conflicts with Directory Rules** | Directory Rules require drift registration and ADR/migration handling rather than silent normalization. Repo drift does not become doctrine by convenience. |

---

## 5. Validation and enforcement

### 5.1 Static checks

A new validator under `tools/validators/sources/` SHOULD assert each of the following on every PR touching `contracts/source/**` or the repo-confirmed descriptor home:

- [ ] `KFM_META_BLOCK_V2` present and parseable
- [ ] All 15 canonical sections present (§2.4)
- [ ] All 9 field groups populated (§2.5)
- [ ] `Source Admission Rules` section contains a non-empty minimum-bar list and a non-empty fail-closed-triggers list
- [ ] If `admission_rules.json` exists, its lists match the prose lists (parity check)
- [ ] `activation.status` ∈ { `denied`, `draft`, `active_internal`, `active_public_candidate`, `retired` }
- [ ] All declared reason codes use the family prefix vocabulary (`prov.*`, `rights.*`, `geom.*`, `sens.*`, `taxon.*`, `obs.*`)
- [ ] `source_role` resolves against the closed source-role registry
- [ ] No descriptor declares `public_release_allowed: true` while `rights.status` is `noassertion` or `unknown`
- [ ] Every activation decision row names `descriptor_digest`, `reviewers`, `decision_date`, `re_review_date`, and `rollback_target`
- [ ] No connector path is added for a source whose descriptor is missing or still `draft`, unless the PR is explicitly fixture-only

### 5.2 Fixtures

Each source SHOULD ship at least one valid fixture and at least one invalid fixture per minimum-bar item and per fail-closed trigger. A failed fixture MUST emit a reason code from the family vocabulary (§2.7).

Fixtures MUST be synthetic, minimal, and no-network unless a later ADR or test policy explicitly allows recorded-source fixtures with rights review.

### 5.3 CI gate

A PR that adds or modifies a descriptor MUST cite this ADR by ID in the PR description and pass the descriptor validator. PRs that add a new admission state, new reason-code family, new descriptor section, or parallel descriptor/schema/policy/source home without amending this ADR or Directory Rules MUST be rejected.

### 5.4 Re-review cadence

Each descriptor's `activation` block names a `re_review_date`. CI SHOULD emit a warning when any active descriptor's re-review date is overdue, and SHOULD surface that signal on the **Source health** dashboard once that dashboard exists.

> [!NOTE]
> Source-health dashboard behavior is **PROPOSED** until mounted repo or runtime evidence proves the dashboard exists.

### 5.5 Acceptance criteria for this ADR

This ADR SHOULD NOT move from `proposed` to `accepted` until:

- [ ] mounted repo inspection confirms the target ADR path and related roots;
- [ ] ADR-0001 schema-home status is verified;
- [ ] Directory Rules drift, if any, is logged or resolved;
- [ ] at least two pilot descriptors are drafted and reviewed;
- [ ] descriptor section checks and field-group checks pass on pilot descriptors;
- [ ] valid and invalid fixture checks pass;
- [ ] `SourceActivationDecision` rows are represented in the proposed authority register or confirmed equivalent;
- [ ] no public release path bypasses descriptor admission, evidence, policy, review, and release gates.

### 5.6 Non-goals and blocked shortcuts

This ADR does **not**:

- authorize publication;
- grant rights to redistribute source data;
- validate source endpoint terms;
- prove that source connectors exist;
- prove that CI, CODEOWNERS, dashboards, release manifests, or policy engines are implemented;
- allow source descriptors to replace `EvidenceBundle`, `PromotionDecision`, `ReleaseManifest`, or rollback objects;
- allow public surfaces to read RAW, WORK, QUARANTINE, candidate, canonical/internal stores, or direct model output.

<sub>[⬆ Back to top](#top)</sub>

---

## 6. Rollback and supersession

- This ADR is `proposed` and may be amended freely until accepted.
- After acceptance, breaking changes (vocabulary, section structure, activation states, reason-code families) MUST be made by a successor ADR. This ADR is then marked `superseded` with a forward link.
- Rollback target for individual descriptor PRs: the descriptor's prior commit and the prior `SourceAuthorityRegister` row. Append-only register entries make the rollback path inspectable.
- Rollback target for validator or policy changes: revert the validator / policy bundle to the prior passing revision and re-run descriptor fixture tests.
- Rollback target for the ADR itself: revert to no formal admission contract and route source intake decisions through ad-hoc review. **Strongly discouraged**; record the reason in the deprecation register.

<sub>[⬆ Back to top](#top)</sub>

---

## 7. Open questions and NEEDS VERIFICATION

### 7.1 Path and authority checks

| Item | Status | Resolution path |
|---|---|---|
| Whether `contracts/source/` is the live home in the mounted repo, or whether an alternate path is in use | **NEEDS VERIFICATION** | Inspect mounted repo; if drifted, open `docs/registers/DRIFT_REGISTER.md` entry per Directory Rules §2.5 |
| Whether `schemas/contracts/v1/sources/` or `schemas/contracts/v1/source/` is the live machine-schema home | **NEEDS VERIFICATION** | Verify ADR-0001 acceptance state and mounted-repo `schemas/contracts/v1/` presence; do not maintain divergent definitions |
| Whether `control_plane/source_authority_register.yaml` exists and is append-only | **NEEDS VERIFICATION** | Inspect mounted repo; if absent, create per Directory Rules §6.2 or confirm alternate register home |
| Whether prior ADRs in `docs/adr/` actually exist as referenced (e.g., ADR-0001) | **NEEDS VERIFICATION** | The corpus references ADR-0001 as the schema-home decision; presence in the mounted repo MUST be confirmed before this ADR is accepted |
| Whether per-domain source registries use `data/registry/<domain>/sources.yaml` or `data/registry/sources/<domain>.yaml` | **NEEDS VERIFICATION** | Inspect mounted repo; choose one by Directory Rules / ADR; add drift entry if both exist without authority |

### 7.2 Design and process questions

| Item | Status | Resolution path |
|---|---|---|
| Whether `admission_rules.*` belongs inside `KFM_META_BLOCK_V2` or as a sibling JSON | **OPEN** | Pilot both on iNaturalist and eBird; choose by validator-ergonomics evidence; record decision in a successor ADR or amendment |
| Whether descriptor sections that do not apply to a given source remain as empty headings or are omitted | **OPEN** (per Pass 13, KFM-IDX-SRC-001 open question) | Default in this ADR: keep heading, write a one-line justification (e.g., "Source-global rights — no observation-level variance") |
| Should source descriptors be enforced via a CI block that DENIES PRs touching `connectors/<source>/` without a corresponding descriptor? | **OPEN** | Default in this ADR: advisory; promote to hard block once two pilot descriptors are accepted |
| Whether a `schemas/contracts/v1/common/source_role.schema.json` should be authored so all descriptors and evidence objects can `$ref` it | **OPEN** (per Pass 13, KFM-IDX-SRC-002 expansion direction) | Track as follow-up ADR |
| Whether the source-health dashboard exists or is only proposed | **NEEDS VERIFICATION** | Inspect apps, reports, dashboards, or release artifacts; until proven, describe dashboard use as PROPOSED |
| Whether `SourceActivationDecision` is a row inside the authority register or a separate object with a register reference | **OPEN** | Pilot with two descriptors; choose the smallest auditable representation; preserve §2.10 fields either way |

<sub>[⬆ Back to top](#top)</sub>

---

## 8. References

### 8.1 Project sources (attached or referenced in this session)

<details>
<summary>Show project-source ledger</summary>

- `kfm_build_companion.pdf` — §8 *Source activation and authority: the repo needs an admission office* (§8.1 activation flow; §8.2 minimum descriptor fields; §8.3 source-role examples by domain). Sketches: Appendix C.1 SourceDescriptor sketch. **Status:** baseline reference preserved; not mounted-repo proof.
- `KFM_Components_Pass_13_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` — §5.B *Chapter B — Source Descriptors and Source-Role Doctrine*; idea entries KFM-IDX-SRC-001 through KFM-IDX-SRC-006.
- `KFM_Geology_Natural_Resources_Architecture_PDF_Only_Report_20260421.pdf` — §12.3 *Source onboarding mechanics* (the 6-step shape replicated across domains).
- `KFM_Governed_AI_Extended_Pro_Source_Ledger_PDF_Only_Architecture_Report_20260420.pdf` — §7 *Required object-family map* (`SourceDescriptor`, `SourceAliasMap`, `UnresolvedSourceReference`, `SourceIntakeRecord`).
- `Directory Rules.pdf` / `docs/doctrine/directory-rules.md` — §0 (status, schema-home convention, lifecycle invariant), §2.4 (changes that require ADR), §4 (placement protocol), §6.2 (`control_plane/`), §6.3 (`contracts/`), §6.4 (`schemas/`), §6.5 (`policy/`).
- `kfm_encyclopedia.pdf` — §10 *Master Action Matrix* (separation of duties for source activation, policy result, promotion).

</details>

### 8.2 Per-domain corroboration

The 6-step onboarding pattern recurs in: KFM Atmosphere/Air; Archaeology; Fauna; Flora; Hazards; Hydrology; Settlements/Infrastructure; Soil; Roads/Rail/Trade Routes; Habitat. Each per-domain dossier names ADRs of the form `ADR-<domain>-source-role-*` and registries at `data/registry/<domain>/sources.yaml` — all **PROPOSED** until inspected against the mounted repo.

### 8.3 Doctrinal anchors

- **Lifecycle invariant.** RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED. Promotion is a governed state transition, not a file move.
- **Watcher-as-non-publisher.** Connectors emit receipts and candidates only; they do not publish.
- **Cite-or-abstain.** Descriptor admission is a precondition for cited claims; without an admitted descriptor, downstream claims must `ABSTAIN`.
- **Trust membrane.** Public surfaces consume only governed envelopes; a descriptor is part of the evidence chain that backs those envelopes.
- **Directory placement discipline.** Responsibility root beats topic name; new parallel homes for schemas, contracts, policy, sources, registries, releases, proofs, or receipts require ADR review.

---

<sub>[⬆ Back to top](#top)</sub>
