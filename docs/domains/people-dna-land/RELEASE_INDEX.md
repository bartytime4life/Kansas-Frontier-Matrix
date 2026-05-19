<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-people-dna-land-release-index
title: People / DNA / Land — Release Index
type: standard
version: v1
status: draft
owners: TODO — Domain steward (People/DNA/Land); Release authority; Sensitivity reviewer
created: TODO-YYYY-MM-DD
updated: TODO-YYYY-MM-DD
policy_label: restricted
related:
  - docs/domains/people-dna-land/README.md            # PROPOSED — NEEDS VERIFICATION
  - docs/standards/RELEASE_MANIFEST.md                # PROPOSED — NEEDS VERIFICATION
  - docs/standards/EVIDENCE_BUNDLE.md                 # PROPOSED — NEEDS VERIFICATION
  - docs/standards/CONSENT_TOKENS.md                  # PROPOSED — NEEDS VERIFICATION
  - docs/runbooks/people-dna-land/                    # PROPOSED — NEEDS VERIFICATION
  - docs/registers/DRIFT_REGISTER.md                  # CONFIRMED rule / PROPOSED presence
  - docs/registers/VERIFICATION_BACKLOG.md            # CONFIRMED rule / PROPOSED presence
  - directory-rules.md                                # CONFIRMED (project doctrine)
tags: [kfm, domain, people, dna, land, release, sensitivity, governance]
notes:
  - "Domain-segment naming (`people-dna-land` vs `people`) is doctrinally unresolved between Directory Rules §12 and Atlas v1.1 §24.13; tracked as ADR-class (see §13)."
  - "All implementation-layer paths are PROPOSED until verified against a mounted repo."
[/KFM_META_BLOCK_V2] -->

# People / DNA / Land — Release Index

Governance contract for what may be published from the People / Genealogy / DNA / Land Ownership domain, in what form, behind which gates, and how it can be corrected or rolled back.

[![Status](https://img.shields.io/badge/status-draft-yellow)](#)
[![Domain](https://img.shields.io/badge/domain-people--dna--land-7e57c2)](#)
[![Policy](https://img.shields.io/badge/policy-deny--by--default-critical)](#)
[![Sensitivity](https://img.shields.io/badge/default%20tier-T4-critical)](#)
[![Lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20PUBLISHED-blue)](#)
[![Doc lint](https://img.shields.io/badge/doc--lint-TODO-lightgrey)](#)
[![Last reviewed](https://img.shields.io/badge/last%20reviewed-TODO-lightgrey)](#)

> **Status:** `draft` · **Owners:** `TODO — domain steward, release authority, sensitivity reviewer, rights-holder representative (where applicable)` · **Last updated:** `TODO-YYYY-MM-DD`

> [!IMPORTANT]
> **This domain is deny-by-default.** Living-person fields, raw DNA segment data, and private person-parcel joins are `T4` (denied) unless an explicit, reviewed, receipted transform demotes them to a lower tier. Nothing in this document creates a default permission to publish. If a release decision is ambiguous, the gate fails closed and the prior state is preserved.

---

## Table of contents

1. [Purpose](#1-purpose)
2. [What this index governs](#2-what-this-index-governs)
3. [Sensitivity posture](#3-sensitivity-posture)
4. [Release manifest contract](#4-release-manifest-contract)
5. [Release lifecycle and gates](#5-release-lifecycle-and-gates)
6. [Per-class release postures](#6-per-class-release-postures)
7. [Release-index entry template](#7-release-index-entry-template)
8. [Correction, supersession, and rollback](#8-correction-supersession-and-rollback)
9. [Consent, revocation, and embargo](#9-consent-revocation-and-embargo)
10. [Decision outcomes for releases](#10-decision-outcomes-for-releases)
11. [Related artifacts and paths](#11-related-artifacts-and-paths)
12. [Verification backlog](#12-verification-backlog)
13. [Open questions and ADR backlog](#13-open-questions-and-adr-backlog)
14. [Related docs](#14-related-docs)

---

## 1. Purpose

**CONFIRMED doctrine.** This document is the human-facing release index for the People / Genealogy / DNA / Land Ownership domain — Chapter 16 of the *KFM Domains v1.1 Consolidated Atlas* ([DOM-PEOPLE], [ENCY]). It explains:

- which People/DNA/Land objects can become released artifacts at all,
- which gates a candidate must clear before promotion to `PUBLISHED`,
- what each release-index entry records (dataset, bundle, tile archive, layer manifest), and
- how a released claim is corrected, superseded, or rolled back.

**PROPOSED scope.** This document is governance, not the release ledger itself. The machine-readable release ledger and per-release `ReleaseManifest` artifacts live elsewhere — `release/candidates/people-dna-land/…` and `release/…` per Directory Rules §4, Step 1 (CONFIRMED rule, PROPOSED presence pending mounted-repo verification).

> [!NOTE]
> **Authority order.** Where this document and the v1.0 / v1.1 Atlas appear to disagree, the Atlas governs the substantive claim and any conflict is filed to `docs/registers/DRIFT_REGISTER.md` per Directory Rules §2.5.

---

## 2. What this index governs

**CONFIRMED scope, PROPOSED field realization.** The People/DNA/Land domain owns the following object families ([DOM-PEOPLE]):

| Object family | Notes |
|---|---|
| `Person Assertion`, `Person Identity Candidate`, `PersonCanonical` | Assertion-first; `PersonCanonical` is a release-state-aware derivative, never a sovereign claim. |
| `Genealogy Relationship`, `RelationshipAssertion`, `FamilyGroup`, `Relationship Hypothesis` | Evidence-bound; hypothesis confidence is exposed, not hidden. |
| `LifeEvent`, `Residence Event`, `Migration Event`, `NameAssertion` | Time-aware; valid / observed / source / retrieval / release / correction times stay distinct. |
| `Land Ownership Assertion`, `Deed Instrument`, `Title Instrument` | Land instruments are evidence, not title truth. |
| `Assessor Record`, `TaxRecord`, `Parcel Version`, `Ownership Interval` | Assessor-as-title is denied (`PROPOSED: assessor-as-title denial`). |
| `DNA Match Evidence`, `DNAKitToken`, `DNASegment` | DNA evidence; raw segments and kit IDs are non-public by doctrine. |

**Explicit non-ownership (CONFIRMED / PROPOSED, [DOM-PEOPLE]).** Settlements, roads, archaeology, hydrology, agriculture, hazards, and spatial foundation provide *context*; they do **not** weaken living-person, DNA, title, or parcel-boundary controls. The domain explicitly does *not* own: settlement legal status, route corridor semantics, or archaeological cultural-place ownership.

[↑ back to top](#table-of-contents)

---

## 3. Sensitivity posture

**CONFIRMED doctrine ([ENCY], [DOM-PEOPLE]).** Living-person output and DNA-derived outputs are **denied or restricted by default**. Raw kit IDs and DNA segments are not public. Assessor and tax records are not title truth. Parcel geometry is not legal boundary truth.

### 3.1 Default tier matrix

The table below extends the Atlas v1.1 §24.5 tier scheme into the People/DNA/Land lane. Tier names and definitions are CONFIRMED doctrine; per-class transforms and gates are PROPOSED until validator and policy implementations are confirmed.

| Object class | Default tier | Allowed transforms (PROPOSED) | Required gates | Citation |
|---|---|---|---|---|
| Living-person fields (any field directly identifying a living person) | `T4` Denied | Aggregation by tract or county + `AggregationReceipt` → `T1` Generalized. | Consent **or** aggregation gate + `ReviewRecord`. | [DOM-PEOPLE] |
| Raw DNA segment / kit / vendor-ID data | `T4` Denied | None to a public tier; `T3` Restricted only under named research agreement. | Named consent + `ReviewRecord` + `PolicyDecision`. | [DOM-PEOPLE] |
| Private person↔parcel join (deceased individual) | `T4` Denied | Generalized parcel + de-identified person → `T2` Reviewer only. | `RedactionReceipt` + `ReviewRecord`. | [DOM-PEOPLE] |
| Person assertion (historical, well-deceased) | `T1` Generalized / `T2` Reviewer (PROPOSED) | Generalization; evidence-bundle citation. | Standard release closure. | [DOM-PEOPLE] [ENCY] |
| Land instrument (deed / title / patent / assessor copy) | `T0` Open or `T1` (PROPOSED, source-dependent) | None when source rights permit; otherwise `RedactionReceipt` → `T1`. | Source-rights confirmation + `ReleaseManifest`. | [DOM-PEOPLE] |
| AI access to RAW / WORK / QUARANTINE for this domain | `T4` forever | None — boundary holds. | `PolicyDecision` + `AIReceipt` denial. | [GAI] |

> [!CAUTION]
> **A lower tier does not loosen the gates above it.** A `T1` release of an aggregated living-person layer still requires an `AggregationReceipt`, a `ReviewRecord`, and a `PolicyDecision`. Skipping any of these returns the candidate to `T4`.

### 3.2 Tier transitions (allowed motion)

| From → To | Required artifact | Required reviewer | Reversibility (CONFIRMED doctrine) |
|---|---|---|---|
| `T4` → `T3` | `PolicyDecision` + `ReviewRecord` + named agreement | Steward + rights-holder | Reversible — agreement revocation returns object to `T4` with `CorrectionNotice`. |
| `T4` → `T2` | `PolicyDecision` + `ReviewRecord` | Steward | Reversible — review revocation returns object to `T4`. |
| `T4` → `T1` | `RedactionReceipt` + `ReviewRecord` | Steward | Reversible — correction may demote a published `T1` back to `T4`. |
| `T1` → `T0` | `ReleaseManifest` + `ReviewRecord` | Steward + release authority | Reversible via `RollbackCard`. |

[↑ back to top](#table-of-contents)

---

## 4. Release manifest contract

**CONFIRMED doctrine** ([KFM-P7-PROG-0003], [NI-425]). When a promotion gate allows `CATALOG / TRIPLET → PUBLISHED`, it emits a `ReleaseManifest`: a single, signed, hashable JSON object that names every:

- included **dataset** by stable ID,
- included **`EvidenceBundle`** by `spec_hash`,
- included **PMTiles archive** by `spec_hash`,
- included **`LayerManifest`** by `spec_hash`.

Consumers — the web client, the catalog harvester, downstream pipelines — bind to the `ReleaseManifest`, not to floating "latest" pointers. A release is content-addressed by construction: any consumer that records the manifest's `spec_hash` is recording exactly which evidence it observed.

**CONFIRMED (Pass 15 addendum, [NI-425]).** `ReleaseManifest` expectations are extended with **release-index entries**, each carrying:

- `dataset_id` — stable domain identifier,
- `spec_hash` — canonical `jcs:sha256:<hex>` of the spec (per C1-02 / Directory Rules),
- `run_receipt` — pointer to the cosign-signed run receipt for the producing pipeline,
- `SPDX` — license identifier in the canonical allowlist (e.g., `CC0-1.0`, `CC-BY-4.0`; allowlist closure is an open ADR — see §13),
- `timestamp` — release time in ISO 8601 / RFC 3339,
- `evidence_bundle_digest` — digest of the supporting `EvidenceBundle`.

> [!NOTE]
> **Per-domain extension (PROPOSED).** For People/DNA/Land entries specifically, the release-index row **should also** carry the sensitivity tier of the released artifact, the active transform receipt(s) (`RedactionReceipt` / `AggregationReceipt`), and a `consent_token` reference where one applies. This is a domain-level proposal that does not contradict the canonical `ReleaseManifest` shape; resolution should be filed under the ADR-S-03 receipt-layout ADR or a dedicated People/DNA/Land release-extension ADR. **NEEDS VERIFICATION** against the live `release_manifest.schema.json`.

[↑ back to top](#table-of-contents)

---

## 5. Release lifecycle and gates

**CONFIRMED doctrine** ([DIRRULES], [DOM-PEOPLE], [ENCY]). People/DNA/Land follows the standard KFM lifecycle:

```text
RAW  →  WORK / QUARANTINE  →  PROCESSED  →  CATALOG / TRIPLET  →  PUBLISHED
```

Promotion is a governed state transition, not a file move. A transition is **closed** only when (i) every required artifact exists, (ii) every required artifact *resolves* — not just references — its dependencies (`EvidenceRef` → `EvidenceBundle`, `source_id` → `SourceDescriptor`), and (iii) the policy gate evaluated and recorded its decision. Missing any of these means the transition fails closed and the prior state is preserved.

```mermaid
flowchart LR
  R["RAW<br/><sub>SourceDescriptor</sub>"] --> WQ["WORK / QUARANTINE<br/><sub>Validation + Policy gate<br/>or Quarantine reason</sub>"]
  WQ --> P["PROCESSED<br/><sub>EvidenceRef · ValidationReport<br/>digest closure</sub>"]
  P --> CT["CATALOG / TRIPLET<br/><sub>CatalogMatrix · EvidenceBundle<br/>release candidate</sub>"]
  CT -->|"Release gate"| PUB["PUBLISHED<br/><sub>ReleaseManifest · ReviewRecord<br/>rollback target · correction path</sub>"]
  PUB -->|"Correction"| PUBp["PUBLISHED'<br/><sub>CorrectionNotice +<br/>ReleaseManifest update or supersession</sub>"]
  PUB -->|"Rollback"| PRIOR["Prior release<br/><sub>RollbackCard +<br/>CorrectionNotice</sub>"]

  classDef sensitive fill:#fdecea,stroke:#c0392b,color:#7b1f1f;
  class WQ,CT,PUB sensitive;
```

**Per-domain gate notes (CONFIRMED / PROPOSED, [DOM-PEOPLE], [ENCY]):**

- `Validation` failures on living-person, DNA, or person-parcel content hold in `QUARANTINE` with a structured reason; they do **not** advance.
- `Catalog` closure for this domain requires `EvidenceBundle` plus the appropriate sensitivity receipt (`RedactionReceipt` / `AggregationReceipt`) where the candidate would otherwise carry living-person, DNA, or private-parcel content.
- `Release` requires a `ReviewRecord` from the sensitivity reviewer **and**, where rights or sovereignty apply (e.g., named consent for DNA), a separate review from a rights-holder representative. Release authority is **distinct from the original author** when materiality applies (operating-law invariant 9).

> [!WARNING]
> **Reason-code surface for People/DNA/Land releases.** Expect `RIGHTS_UNKNOWN`, `SENSITIVITY_UNRESOLVED`, `MISSING_EVIDENCE`, `MISSING_REVIEW`, `RELEASE_MANIFEST_INVALID`, and `ROLLBACK_TARGET_MISSING` as dominant `DENY` reasons. The full reason-code catalog is PROPOSED in Atlas §24.6.3.

[↑ back to top](#table-of-contents)

---

## 6. Per-class release postures

The matrix below maps every object class to its release shape. **Status of the rules: CONFIRMED doctrine. Status of the named artifacts in the current repo: PROPOSED until verified.**

| Object class | Release form (PROPOSED) | Default tier | Required receipts | DENY-by-default conditions |
|---|---|---|---|---|
| `Person Assertion` (historical, well-deceased) | EvidenceBundle + Layer (point or address) | `T1`–`T2` | `SourceDescriptor`, `EvidenceBundle`, `ReleaseManifest` | Living-person flag set; rights unresolved; source role unknown. |
| `Person Identity Candidate` | EvidenceBundle (reviewer surface) | `T2` | `EvidenceBundle`, `ReviewRecord` | Conflicting assertions unresolved; weak evidence; living-person involved. |
| `Relationship Hypothesis` | EvidenceBundle with confidence | `T1`–`T2` | `EvidenceBundle` with confidence band | Living-person endpoints; DNA-only basis without consent. |
| `LifeEvent`, `Residence Event`, `Migration Event` | EvidenceBundle + (optional) PMTiles for migration paths | `T0`–`T1` | `EvidenceBundle`, `ReleaseManifest` | Living person; private location; uncertainty exceeds publishable threshold. |
| `Land Ownership Assertion`, `Deed`/`Title`/`Patent Instrument` | EvidenceBundle + instrument transcript | `T0`–`T1` | `EvidenceBundle`, source-rights confirmation | Chain-of-title gap; instrument rights unresolved. |
| `Parcel Version`, `Ownership Interval` | LayerManifest + PMTiles (parcel context) | `T1` (CAUTIONED) | `EvidenceBundle`, `LayerManifest`, "context-not-title" warning | Used as title truth; private person-parcel join active. |
| `Assessor Record`, `TaxRecord` | EvidenceBundle (administrative context) | `T1` | `EvidenceBundle`, source-rights confirmation | Treated as title truth (denied by `PROPOSED: assessor-as-title denial`). |
| `DNA Match Evidence` (released derivative only) | EvidenceBundle (reviewer surface) | `T3` (named agreement) | `EvidenceBundle`, named consent, `ReviewRecord` | Raw segment data; revocation pending; consent expired. |
| `DNAKitToken`, raw `DNASegment` | **Not released** | `T4` | n/a | Always — no transform releases raw genomic content to a public tier. |

> [!TIP]
> **Reading the table.** "Release form" is what reaches `PUBLISHED`; it is never the canonical store or graph internal. Public clients and normal UI surfaces consume released forms only.

[↑ back to top](#table-of-contents)

---

## 7. Release-index entry template

**PROPOSED template.** A release-index entry for this domain extends the canonical fields (§4) with the People/DNA/Land sensitivity surface. The shape below is illustrative until the canonical `release_manifest.schema.json` is verified in the mounted repo.

<details>
<summary><strong>Click to expand — illustrative release-index entry</strong></summary>

```json
{
  "dataset_id": "kfm:people-dna-land/<stable-id>",
  "spec_hash": "jcs:sha256:<hex>",
  "run_receipt": "kfm:receipt/<hex>",
  "evidence_bundle_digest": "sha256:<hex>",
  "rights_spdx": "CC-BY-4.0",
  "timestamp": "YYYY-MM-DDTHH:MM:SSZ",

  "sensitivity": {
    "tier": "T1",
    "tier_basis": ["AggregationReceipt", "ReviewRecord"],
    "transforms": [
      {"type": "aggregation", "grain": "county", "receipt": "kfm:receipt/<hex>"}
    ]
  },

  "consent": {
    "applies": false,
    "token_ref": null,
    "revocation_endpoint": null,
    "embargo_until": null
  },

  "release": {
    "manifest_ref": "kfm:release/<id>",
    "review_record": "kfm:review/<id>",
    "rollback_target": "kfm:release/<prior-id>",
    "correction_path": "kfm:correction/<id-or-null>"
  },

  "contents": {
    "evidence_bundles": [{"spec_hash": "jcs:sha256:<hex>"}],
    "layer_manifests":  [{"spec_hash": "jcs:sha256:<hex>"}],
    "pmtiles_archives": [{"spec_hash": "jcs:sha256:<hex>"}]
  }
}
```

**Notes (PROPOSED).** Field names follow the C1-01 run-receipt canonicalization where they overlap (`rights_spdx`, `spec_hash` formatting). Sensitivity, consent, and release sub-objects are proposed extensions specific to People/DNA/Land. The `consent.applies = true` branch requires the token to introspect on every render — see §9.

</details>

[↑ back to top](#table-of-contents)

---

## 8. Correction, supersession, and rollback

**CONFIRMED doctrine** ([ENCY], [DIRRULES]). A released People/DNA/Land claim never undergoes a silent edit. Three reversible transitions are available, each with its own receipt and review:

```mermaid
flowchart LR
  PUB["PUBLISHED"] -->|"Detected error<br/>or new evidence"| CN["Correction"]
  PUB -->|"Failed release<br/>or post-publication failure"| RB["Rollback"]
  PUB -->|"Newer release replaces"| SUP["Supersession"]

  CN --> PUBp["PUBLISHED'<br/><sub>CorrectionNotice +<br/>ReleaseManifest update</sub>"]
  RB --> PRIOR["Prior release<br/><sub>RollbackCard +<br/>CorrectionNotice +<br/>derivative invalidation</sub>"]
  SUP --> NEW["New release<br/><sub>Supersession link in registry</sub>"]
```

| Transition | Trigger | Required artifacts | Stale-state behavior |
|---|---|---|---|
| **Correction** (`PUBLISHED → PUBLISHED'`) | Detected error or new evidence; downstream derivatives identified. | `CorrectionNotice`, `ReviewRecord`, invalidation list, `ReleaseManifest` update or supersession. | Stale-state announcement; **no silent edit**. |
| **Rollback** (`PUBLISHED → prior release`) | Failed release or post-publication failure; targeted prior release identified. | `RollbackCard`, `CorrectionNotice`, `ReleaseManifest` reverts, downstream-derivative invalidation. | Held at current state until rollback validated. |
| **Supersession** | A newer release replaces an older one (no defect required). | Supersession link in bundle registry; lineage chain entry. | Older release remains discoverable in lineage; not surfaced as current. |

> [!IMPORTANT]
> **Right-to-be-forgotten vs tombstone (open boundary).** Revocation of consent for living-person or DNA-derived material may require *true erasure* rather than a tombstone. The corpus flags this boundary as open and aligned with GDPR / applicable Tribal data policies. Until an ADR resolves the boundary, People/DNA/Land defaults to erasure for living-person and DNA content, tombstone-with-supersession for everything else. **NEEDS VERIFICATION** against implemented policy.

[↑ back to top](#table-of-contents)

---

## 9. Consent, revocation, and embargo

**CONFIRMED doctrine (C6-07, C6-08, C9-04).** For any release that depends on consent (DNA-derived derivatives; named-agreement living-person research surfaces), consent is **machine-readable, signed, and introspected on every render** — not narrative text in a README.

A People/DNA/Land release that depends on consent **shall** carry, at minimum:

- a `consent_token` with `scopes`, `aud`, `exp`, `revocation_endpoint`, `consent_history_hash`, and a `redaction_profile` reference (JWT or GA4GH visa shape);
- an `embargo_until` field (release is denied if `now < embargo_until`);
- cache-invalidation hooks (PMTiles index bump, tile-server purge) so that revoked content does not survive in caches.

```mermaid
sequenceDiagram
  autonumber
  participant Client
  participant API as Governed API
  participant PDP as Policy Decision Point
  participant Rev as Revocation endpoint

  Client->>API: Request released People/DNA/Land artifact
  API->>PDP: Evaluate gate (token, embargo, tier, k-anon)
  PDP->>Rev: Introspect token (RFC 7662 / GA4GH AAI)
  Rev-->>PDP: active | revoked | unreachable
  alt active and embargo passed and k satisfied
    PDP-->>API: ALLOW
    API-->>Client: ANSWER (redacted to released tier)
  else revoked or expired or unreachable
    PDP-->>API: DENY (fail closed)
    API-->>Client: DENY with reason code
  end
```

> [!WARNING]
> **Fail-closed on introspection outage.** If the revocation endpoint is unreachable, the rendering must fail closed even when this inconveniences users. This is doctrine, not preference (C6-07, C6-08).

[↑ back to top](#table-of-contents)

---

## 10. Decision outcomes for releases

**CONFIRMED doctrine.** Every governed-API surface returns one of four outcomes. For People/DNA/Land, the per-outcome posture is:

| Outcome | When it fires | What the client receives |
|---|---|---|
| `ANSWER` | All gates pass for the requested released artifact at the requested tier. | Released form only (never canonical store, graph internal, vector index, or RAW/WORK content). |
| `ABSTAIN` | Evidence is insufficient or the claim depends on unresolved sensitivity. | A structured abstention with cite-or-abstain reason; **never** a generated stand-in. |
| `DENY` | Policy, rights, sensitivity, review state, or release state blocks the request. | A reason code (e.g., `RIGHTS_UNKNOWN`, `SENSITIVITY_UNRESOLVED`, `MISSING_REVIEW`, `CONSENT_REVOKED`) and any safe-to-disclose context. |
| `ERROR` | Infrastructure failure; gate cannot be evaluated. | Fail-closed; **no partial answer**. |

**Governed AI ([GAI], [DOM-PEOPLE]).** AI may summarize *released* People/DNA/Land `EvidenceBundle`s, compare evidence, explain limitations, and draft steward-review notes. AI **must** `ABSTAIN` when evidence is insufficient and **must** `DENY` where policy, rights, sensitivity, or release state blocks the request. AI never reads RAW or WORK content for this domain.

[↑ back to top](#table-of-contents)

---

## 11. Related artifacts and paths

**PROPOSED placement** per Directory Rules §4 / §12. All paths below are placement proposals, **NEEDS VERIFICATION** until a mounted-repo inspection confirms them. The domain segment shown is `people-dna-land/` (Directory Rules §12); a parallel naming `people/` appears in Atlas v1.1 §24.13 schema/policy crosswalks — see ADR-class open question OPEN-PEOPLE-NAMING in §13.

```text
docs/domains/people-dna-land/
├── README.md                      # domain landing (per-folder README, §15 of Directory Rules)
├── RELEASE_INDEX.md               # THIS FILE
├── SENSITIVITY.md                 # PROPOSED — sensitivity profile for the domain
├── CONSENT.md                     # PROPOSED — consent-token contract specific to People/DNA
└── runbooks/                      # PROPOSED — placement TBD per Directory Rules §18 OPEN-DR-02
    └── ...

# All paths below: PROPOSED — NEEDS VERIFICATION
release/
├── candidates/people-dna-land/    # release candidates, gated CATALOG → PUBLISHED
└── ...                            # ReleaseManifests, RollbackCards, CorrectionNotices

schemas/contracts/v1/<people | people-dna-land>/   # ADR-class naming open question
contracts/<people | people-dna-land>/
policy/sensitivity/<people | people-dna-land>/
policy/consent/<people | people-dna-land>/
tests/domains/<people | people-dna-land>/
fixtures/domains/<people | people-dna-land>/
data/published/layers/<people | people-dna-land>/
data/registry/sources/<people | people-dna-land>/
```

**Upstream / downstream binding (PROPOSED, [DOM-PEOPLE], [ENCY]):**

| Direction | Counterparts | Notes |
|---|---|---|
| **Upstream** (consumed by this domain) | `Settlements` (residence, cemetery, school, court, county, township, place); `Roads/Rail` (migration, access); `Archaeology` (historic person, documentary, cultural-place context); `Agriculture` (farm, producer-adjacent context). | Relation must preserve ownership, source role, sensitivity, and `EvidenceBundle` support. |
| **Downstream** (consumes from this domain) | `Frontier Matrix` (county-year panels cite well-deceased person assertions only); public Evidence Drawer; Focus Mode (released bundles only). | Living-person and raw-DNA payloads are **never** propagated downstream. |

[↑ back to top](#table-of-contents)

---

## 12. Verification backlog

Items below are drawn from Atlas v1.0 Ch. 16 §N (Verification backlog) and the Atlas v1.1 Ch. 24.12 Master Open-ADR backlog. They are **NEEDS VERIFICATION** until checked against mounted-repo files, schemas, registry entries, tests, logs, emitted artifacts, review records, or release manifests.

- [ ] Verify the **living-person policy** is implemented and enforced (validator + OPA rule + fail-closed test).
- [ ] Verify **DNA consent / revocation** is enforced on every render (PDP introspects revocation endpoint; cache invalidation fires; fail-closed on introspection outage).
- [ ] Verify **land-instrument chain logic** (chain-of-title gap test; `PROPOSED: assessor-as-title denial`).
- [ ] Verify **geometry ↔ role boundary** (parcel geometry never used as title truth; address-as-evidence is not address-as-occupancy).
- [ ] Verify **UI / API restricted-field no-leak** behavior across Evidence Drawer, Focus Mode, AI surface, and tile rendering.
- [ ] Verify the **`ReleaseManifest` schema** (`release_manifest.schema.json`) supports the Pass-15 release-index extension and any People/DNA/Land-specific sub-objects.
- [ ] Verify **SPDX allowlist** for this domain (corpus mentions `CC0-1.0`, `CC-BY-4.0`; `ODC-By`, `PDDL`, `US-PD` are open questions per C5-02).
- [ ] Verify **rollback drill** completes end-to-end (RollbackCard → ReleaseManifest revert → derivative invalidation → cache purge → audit ledger entry).

[↑ back to top](#table-of-contents)

---

## 13. Open questions and ADR backlog

Open architectural questions surfaced by this document. Resolutions migrate to `docs/registers/VERIFICATION_BACKLOG.md` or `docs/adr/` per Directory Rules §2.4–§2.5.

| # | Question | Why it's ADR-class | Suggested ADR title (PROPOSED) |
|---|---|---|---|
| **OPEN-PEOPLE-NAMING** | Is the canonical domain segment `people-dna-land/` (Directory Rules §12) or `people/` (Atlas v1.1 §24.13 crosswalk)? | Inconsistent segment naming across roots will fork docs, schema, and policy homes. Parallel to OPEN-ENC-04. | "Domain segment naming for People / DNA / Land." |
| **OPEN-PEOPLE-EXT** | Should the People/DNA/Land release-index extension (sensitivity, consent, transforms) live inside `release_manifest.schema.json` or in a domain-scoped sub-schema? | Creates a parallel home if domain-scoped (Directory Rules §2.4(5)). | "Release-manifest extension for People / DNA / Land." |
| **OPEN-PEOPLE-CONSENT** | What is the cache TTL for revocation introspection results, and what is the precise erasure-vs-tombstone boundary for living-person / DNA content? | Right-to-be-forgotten alignment is doctrine-class for this domain. | "Consent token TTL and erasure boundary." |
| **OPEN-PEOPLE-RIGHTS** | Which SPDX identifiers are admissible for People/DNA/Land sources beyond `CC0-1.0` and `CC-BY-4.0`? | Allowlist closure is the structural bedrock of default-deny promotion (C5-02). | "SPDX allowlist for People / DNA / Land sources." |
| **OPEN-PEOPLE-AUTHORITY** | Who is the release authority for `T3` named-agreement DNA releases — domain steward, rights-holder representative, both? | Separation-of-duties is operating-law invariant 9; under-specified separation invites silent author-approves-self events. | "Release authority and separation of duties for People / DNA / Land." |

[↑ back to top](#table-of-contents)

---

## 14. Related docs

> Links below are placement proposals (relative paths). Items marked **TODO** are not yet verified to exist; verify before relying on them.

- [`docs/domains/people-dna-land/README.md`](./README.md) — domain landing page · **TODO**
- [`docs/domains/people-dna-land/SENSITIVITY.md`](./SENSITIVITY.md) — sensitivity profile · **TODO**
- [`docs/domains/people-dna-land/CONSENT.md`](./CONSENT.md) — consent-token contract · **TODO**
- [`docs/standards/RELEASE_MANIFEST.md`](../../standards/RELEASE_MANIFEST.md) — canonical `ReleaseManifest` standard · **TODO**
- [`docs/standards/EVIDENCE_BUNDLE.md`](../../standards/EVIDENCE_BUNDLE.md) — `EvidenceBundle` standard · **TODO**
- [`docs/standards/CONSENT_TOKENS.md`](../../standards/CONSENT_TOKENS.md) — consent-token standard (referenced by C6-07) · **TODO**
- [`docs/standards/PROV.md`](../../standards/PROV.md) — W3C PROV profile (or `PROVENANCE.md` per ADR; both names appear in the corpus) · **NEEDS VERIFICATION**
- [`docs/runbooks/people-dna-land/`](../../runbooks/people-dna-land/) — operational runbooks for this domain · **TODO**
- [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) — drift entries · CONFIRMED rule / PROPOSED presence
- [`docs/registers/VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md) — verification backlog · CONFIRMED rule / PROPOSED presence
- [`directory-rules.md`](../../../directory-rules.md) — placement doctrine · CONFIRMED

[↑ back to top](#table-of-contents)

---

**Last updated:** `TODO-YYYY-MM-DD`
**Version:** `v1 (draft)`
**Steward review cadence:** quarterly while `draft`; on every release otherwise.

[↑ back to top](#table-of-contents)
