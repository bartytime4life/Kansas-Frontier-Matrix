<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domain-hydrology-release-index
title: Hydrology — Release Index
type: domain_readme
version: v2
status: draft
owners: <hydrology-steward> + <docs-steward>   # TODO confirm against CODEOWNERS
created: 2026-05-18
updated: 2026-06-07
policy_label: public
related:
  - ai-build-operating-contract.md
  - directory-rules.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/registers/DRIFT_REGISTER.md
tags: [kfm, domain, hydrology, release, manifest, rollback, evidence-bundle, index]
notes:
  - 'CONTRACT_VERSION = "3.0.0"'
  - "This page indexes and links; it does not decide. Release authority lives in release/ and data/."
  - "release/ tree matches the CONFIRMED §9.2 layout; domain-segment and per-file existence remain PROPOSED."
  - "NFHL is regulatory context only; never an observed-flood or life-safety surface."
[/KFM_META_BLOCK_V2] -->

# Hydrology — Release Index

> Human-readable index and navigation map for governed Hydrology releases — release candidates, ReleaseManifests, PromotionDecisions, rollback cards, correction notices, and published artifacts. This page **explains and links**; it does not decide. Release authority lives in `release/` and `data/` per Directory Rules.

<!-- Badge targets are placeholders. Replace with the actual repo, workflow, and policy
     endpoints once the repo is mounted and authoritative URLs are known. -->

![status](https://img.shields.io/badge/status-PROPOSED-orange "TODO: link to release-state register")
![doctrine](https://img.shields.io/badge/doctrine-CONFIRMED-blue "Hydrology doctrine confirmed; implementation PROPOSED")
![CONTRACT_VERSION](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational "ai-build-operating-contract.md v3.0")
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-informational "Promotion is a governed state transition, not a file move")
![policy](https://img.shields.io/badge/policy-fail--closed-critical "Deny-by-default, cite-or-abstain")
![release-gate](https://img.shields.io/badge/release--gate-catalog%20closure-yellow "Catalog/proof closure required before public release")
![last%20updated](https://img.shields.io/badge/last%20updated-2026--06--07-lightgrey "TODO: wire to docs lastmod workflow")

| Field | Value |
|---|---|
| **Status** | PROPOSED — doctrine CONFIRMED, implementation NEEDS VERIFICATION (no mounted repo this session) |
| **Doc type** | README-like — orientation, navigation, registry-style index |
| **Authority level** | `docs/` — explanatory and navigational. **Not** release authority. Release authority lives under `release/` and `data/`. |
| **Owners** | Hydrology steward(s) + Docs steward · *TODO: confirm against `CODEOWNERS`* |
| **Reviewers required** | Hydrology steward + Release authority (separate from author when materiality applies) |
| **Contract** | `CONTRACT_VERSION = "3.0.0"` (`ai-build-operating-contract.md` v3.0) |
| **Last reviewed** | 2026-06-07 — *TODO: wire to docs lastmod automation* |
| **Supersedes** | None — net-new index file |
| **Related doctrine** | `ai-build-operating-contract.md`, `directory-rules.md` (§9.1 lifecycle, §9.2 `release/` layout, §13 anti-patterns) |

---

## Mini-TOC

1. [Scope](#1-scope)
2. [Repo fit](#2-repo-fit)
3. [What this index records](#3-what-this-index-records)
4. [What does NOT belong here](#4-what-does-not-belong-here)
5. [Hydrology release lanes](#5-hydrology-release-lanes)
6. [Release flow diagram](#6-release-flow-diagram)
7. [Release-state legend](#7-release-state-legend)
8. [Release register (template)](#8-release-register-template)
9. [Closure rules — what every Hydrology release must resolve](#9-closure-rules--what-every-hydrology-release-must-resolve)
10. [Sensitivity, rights, and publication posture](#10-sensitivity-rights-and-publication-posture)
11. [Quickstart — how to use this index](#11-quickstart--how-to-use-this-index)
12. [Verification backlog and open questions](#12-verification-backlog-and-open-questions)
13. [FAQ](#13-faq)
14. [Related docs](#14-related-docs)
15. [Appendix A — Source families and source-role doctrine](#appendix-a--source-families-and-source-role-doctrine)
16. [Appendix B — Hydrology-specific deny-by-default register](#appendix-b--hydrology-specific-deny-by-default-register)

---

## 1. Scope

This index is the **navigational entry point** for everything a reviewer, steward, or downstream consumer needs in order to locate, understand, or audit a Hydrology release.

**CONFIRMED doctrine:** Hydrology governs watersheds, HUC units, hydro features and reach identity, gauge sites, flow and water-level observations, water-quality observations, groundwater wells, NFHL regulatory flood context, observed flood events, hydrographs, and upstream/downstream traces — bound by source role, evidence, time, and release state, and explicitly *not* a flood-warning or life-safety system. [DOM-HYD] [ENCY]

**CONFIRMED doctrine:** Public-facing Hydrology artifacts reach the `PUBLISHED` state only when a `ReleaseManifest`, supporting `EvidenceBundle`, validation/policy support, review state (where required), correction path, stale-state rule, and rollback target all exist and resolve to one another. [DOM-HYD §M] [ENCY Appendix E]

> [!IMPORTANT]
> This file is **PROPOSED** in placement and is doctrinally consistent with `docs/domains/<domain>/` per Directory Rules §12. Until the repo is mounted, every path quoted here is PROPOSED unless explicitly marked CONFIRMED. Verify against mounted-repo evidence before treating any path or filename as canonical.

[Back to top](#hydrology--release-index)

---

## 2. Repo fit

**Upstream of this index** — the records this index points at. The top-level `release/` and `data/` layout is **CONFIRMED** per Directory Rules §9.1–§9.2; the `hydrology` domain segment and per-file existence are **PROPOSED**.

- `release/candidates/hydrology/` — release candidate dossiers for Hydrology *(CONFIRMED root + segment pattern; contents PROPOSED)*
- `release/manifests/` — `ReleaseManifest` records keyed by `release_id` *(CONFIRMED §9.2 home)*
- `release/promotion_decisions/` — `PromotionDecision` records *(CONFIRMED §9.2 home)*
- `release/rollback_cards/` — rollback **decision** artifacts *(CONFIRMED §9.2 home; §28 glossary)*
- `release/correction_notices/` — public correction notices touching Hydrology *(CONFIRMED §9.2 home)*
- `release/withdrawal_notices/` — Hydrology withdrawals *(CONFIRMED §9.2 home)*
- `release/signatures/` — DSSE / Sigstore artifacts for Hydrology releases *(CONFIRMED §9.2 home)*
- `data/proofs/evidence_bundle/` and `data/proofs/proof_pack/` — Hydrology proof-closure objects *(PROPOSED leaf names)*
- `data/catalog/stac/`, `…/dcat/`, `…/prov/`, `data/catalog/domain/hydrology/` — catalog records *(PROPOSED leaf names)*
- `data/published/layers/hydrology/`, `data/published/pmtiles/`, `data/published/geoparquet/` — published artifacts
- `data/receipts/release/` — release receipts *(PROPOSED leaf name)*
- `data/registry/sources/hydrology/` — Hydrology source descriptors
- `data/rollback/hydrology/<release_id>/` — alias-revert **receipts** / prior-state references *(data plane; distinct from `release/rollback_cards/`, the decision plane — see §13.7 OPEN)*

**Downstream of this index** — consumers that use it for navigation (PROPOSED):

- `apps/governed-api/` resolvers serving the Hydrology API surface (`HydrologyDecisionEnvelope`, `LayerManifest`, `EvidenceDrawerPayload`)
- `apps/explorer-web/` map and Evidence Drawer flows (read through the governed API; **never** directly from canonical stores). *The canonical web shell is `apps/explorer-web/`, not `apps/web/` — DIRRULES §11, CONFIRMED at commit `b6a279…`.*
- Steward review tools and the verification backlog
- Cross-domain documents that need to cite a specific Hydrology release

> [!NOTE]
> `docs/` **does not decide**. This page indexes and explains; the authoritative records live in `release/` (decisions) and `data/published/` (artifacts). If a discrepancy arises between this index and the authoritative records, the records win and this page is updated. [DIRRULES §9.2, §13]

[Back to top](#hydrology--release-index)

---

## 3. What this index records

The index is intentionally narrow. It registers and links — it does not duplicate authoritative content.

| Record class | What we record here | Authoritative home |
|---|---|---|
| Release candidate | `release_id`, candidate dossier link, source descriptors covered, status | `release/candidates/hydrology/<release_id>/` *(PROPOSED leaf)* |
| `ReleaseManifest` | `release_id`, manifest link, artifact-digest summary, supersedes / superseded_by | `release/manifests/<release_id>.json` *(CONFIRMED dir; PROPOSED filename)* |
| `PromotionDecision` | Decision outcome (`ANSWER` / `ABSTAIN` / `DENY` / `ERROR`), reviewer, gate evidence ref | `release/promotion_decisions/<release_id>.json` *(CONFIRMED dir)* |
| `EvidenceBundle` closure | Bundle id, validation-report ref, policy-decision ref | `data/proofs/evidence_bundle/<bundle_id>.json` *(PROPOSED leaf)* |
| Published artifacts | Layer ids, PMTiles versioned filenames, COG/GeoParquet refs, sidecar digests | `data/published/layers/hydrology/`, `…/pmtiles/`, `…/geoparquet/` |
| Catalog closure | STAC / DCAT / PROV item refs, citation report | `data/catalog/stac/`, `…/dcat/`, `…/prov/`, `…/domain/hydrology/` |
| Rollback target | Prior `release_id`, rollback-card link, verification status | `release/rollback_cards/<release_id>.json` *(CONFIRMED dir)* |
| Correction notice | Notice id, scope of correction, supersession notes | `release/correction_notices/<notice_id>.json` *(CONFIRMED dir)* |
| Withdrawal | Notice id, reason, public-facing impact | `release/withdrawal_notices/<notice_id>.json` *(CONFIRMED dir)* |
| Signatures | DSSE / cosign artifact refs, Rekor index, key/cert identity | `release/signatures/<release_id>/` *(CONFIRMED dir)* |

> [!TIP]
> The index entry for a release is the **shortest** thing that lets a reviewer reach every record above by following one or two links. If the entry is growing into a narrative, that content belongs in a candidate dossier or an ADR, not here.

[Back to top](#hydrology--release-index)

---

## 4. What does NOT belong here

- Raw, work, quarantine, or unreleased candidate payloads. Those are governed by lifecycle-phase rules. [DIRRULES §9.1]
- Schema definitions, contract definitions, or policy bundles. Those live under `schemas/`, `contracts/`, `policy/`.
- Test fixtures, validation reports, or pipeline run logs as primary content. Linked refs only.
- Live emergency-flood instructions, alerts, or warnings of any kind. KFM is **not** a life-safety authority and **must not** be used as one. [DOM-HYD] [ENCY §20.4 emergency-alert boundary]
- NFHL polygons presented as observed flood inundation. NFHL is regulatory context, not observation. [DOM-HYD]
- Exact, restricted, or steward-only geometry beyond what the release-state register allows for public exposure.
- AI-generated summaries treated as evidence. AI is interpretive, never the root truth source. [GAI]
- `.rego` policy code. Policy lives under `policy/`; `release/*.rego` is a CONFIRMED drift anti-pattern. [DIRRULES §13.5]

[Back to top](#hydrology--release-index)

---

## 5. Hydrology release lanes

The **top-level `release/` layout is CONFIRMED** per Directory Rules §9.2. The `data/` lifecycle roots are CONFIRMED per §9.1. The `hydrology` **domain segment** and the existence of any specific subfolder/file are **PROPOSED** until mounted-repo evidence confirms them.

> [!WARNING]
> Domain lanes live **inside** responsibility roots; the domain segment is `hydrology`. A release manifest does **not** live in `data/published/`, and a published PMTiles file does **not** live in `release/` — mixing them is one of the four drift patterns. [DIRRULES §9.2, §10, §13]

```text
release/                                  # CONFIRMED root (§9.2)
├── README.md                             # CONFIRMED — required per §15 README contract
├── candidates/                           # CONFIRMED dir
│   └── hydrology/                        # PROPOSED segment — release candidate dossiers
│       └── <release_id>/                 # PROPOSED — one folder per candidate
├── manifests/                            # CONFIRMED — ReleaseManifest by release_id
├── promotion_decisions/                  # CONFIRMED — PromotionDecision records
├── rollback_cards/                       # CONFIRMED — rollback decision artifacts
├── correction_notices/                   # CONFIRMED — public correction notices
├── withdrawal_notices/                   # CONFIRMED — withdrawal records
├── signatures/                           # CONFIRMED — DSSE / Sigstore artifacts
└── changelog/                            # CONFIRMED — release-level changelog

data/                                     # CONFIRMED lifecycle roots (§9.1)
├── catalog/
│   ├── stac/                             # PROPOSED leaf — STAC records
│   ├── dcat/                             # PROPOSED leaf — DCAT records
│   ├── prov/                             # PROPOSED leaf — PROV records
│   └── domain/
│       └── hydrology/                    # PROPOSED — Hydrology domain catalog
├── proofs/
│   ├── evidence_bundle/                  # PROPOSED leaf — EvidenceBundle objects
│   ├── proof_pack/                       # PROPOSED leaf — ProofPack objects
│   ├── validation_report/                # PROPOSED leaf — validation reports
│   └── citation_validation/              # PROPOSED leaf — citation-validation reports
├── published/
│   ├── api_payloads/                     # PROPOSED leaf — public-safe API payload snapshots
│   ├── layers/
│   │   └── hydrology/                    # CONFIRMED pattern (§9.1: data/published/layers/<domain>/)
│   ├── pmtiles/                          # PROPOSED leaf — versioned PMTiles artifacts
│   └── geoparquet/                       # PROPOSED leaf — GeoParquet artifacts
├── receipts/
│   └── release/                          # PROPOSED leaf — release receipts
├── registry/
│   └── sources/
│       └── hydrology/                    # PROPOSED — Hydrology source descriptors
└── rollback/                             # CONFIRMED data-plane root (§9.1)
    └── hydrology/
        └── <release_id>/                 # PROPOSED — alias-revert receipts, prior-state refs

docs/
└── domains/
    └── hydrology/                        # CONFIRMED docs home (§12)
        ├── README.md                     # Hydrology domain landing
        ├── RELEASE_INDEX.md              # this file
        ├── PUBLICATION_POSTURE.md        # lane publication posture
        └── …                            # PROPOSED — domain-scoped docs
```

> [!NOTE]
> **Rollback split (DIRRULES §13.7 OPEN).** `release/rollback_cards/` holds the rollback
> *decision* (release plane); `data/rollback/hydrology/<release_id>/` holds alias-revert
> *receipts* and prior-state references (data plane). An ADR may later merge them; this index
> keeps both per current doctrine.

[Back to top](#hydrology--release-index)

---

## 6. Release flow diagram

The diagram below is a **doctrine-grounded** representation of the Hydrology release lifecycle. Lifecycle phases and gates follow KFM doctrine; exact tool wiring is PROPOSED. [ENCY §24] [DIRRULES §9.1]

```mermaid
flowchart LR
    RAW[RAW<br/>source-edge capture]
    WORK[WORK<br/>normalized intermediates]
    QUAR[QUARANTINE<br/>failed validation /<br/>unresolved rights or sensitivity]
    PROC[PROCESSED<br/>validated canonical records]
    CAT[CATALOG / TRIPLET<br/>STAC · DCAT · PROV<br/>EvidenceBundle · graph]
    PUB[PUBLISHED<br/>public-safe artifacts]

    RAW --> WORK
    WORK -->|fail / sensitive| QUAR
    WORK --> PROC
    PROC --> CAT
    CAT --> PUB

    PUB -. correction .-> PUB2["PUBLISHED prime"]
    PUB -. rollback .-> PRIOR[Prior PUBLISHED]

    subgraph Gates [Promotion gates — fail-closed]
      G1{{Admission<br/>SourceActivationDecision · rights}}
      G2{{Validation<br/>schemas · validators · receipts}}
      G3{{Catalog closure<br/>STAC/DCAT/PROV + EvidenceBundle}}
      G4{{Release<br/>ReleaseManifest · rollback · review}}
    end

    RAW -. G1 .-> WORK
    PROC -. G2 .-> CAT
    CAT -. G3 .-> PUB
    PUB -. G4 .-> PUB
```

> [!NOTE]
> Each gate is a **governed state transition**, not a file move. Closure means (i) required artifacts exist, (ii) every artifact resolves the artifacts it depends on (`EvidenceRef` → `EvidenceBundle`, `source_id` → `SourceDescriptor`, `model_id` → `ModelRunReceipt`), and (iii) the policy gate evaluated and recorded its decision. Missing any of these means the transition fails closed and the prior state is preserved. [ENCY §24.6.2]

[Back to top](#hydrology--release-index)

---

## 7. Release-state legend

| State | Meaning | Public surface? |
|---|---|---|
| `candidate` | Release dossier exists; gates pending or failing | No |
| `review` | Awaiting steward / release-authority sign-off | No |
| `approved` | All gates pass; promotion authorized | No (about to publish) |
| `published` | `ReleaseManifest` resolves; artifacts public-safe | Yes |
| `superseded` | Replaced by a newer release; correction notice issued | Read-only (historical) |
| `withdrawn` | Withdrawn from public surfaces; rollback target activated | No |
| `rolled_back` | Rollback card invoked; prior release reinstated | Yes (prior release) |
| `held` | Gate failed; held at prior state pending remediation | No change at public edge |

> [!NOTE]
> These state names are **PROPOSED** working vocabulary for this index. The canonical
> release-state enum is NEEDS VERIFICATION against the release-state register / schema.

[Back to top](#hydrology--release-index)

---

## 8. Release register (template)

The table below is the **template** for the per-release rows this index will accumulate. Until the repo is mounted, the rows are illustrative placeholders. *(Schema PROPOSED; actual rows UNKNOWN.)*

<!-- EDITORS: when adding a real release row, fill every column. If a field is unknown,
     mark it UNKNOWN explicitly rather than leaving it blank or guessed. -->

| Release ID | Scope | State | ReleaseManifest | EvidenceBundle | PromotionDecision | Rollback target | Correction(s) | Signatures | Notes |
|---|---|---|---|---|---|---|---|---|---|
| `hyd-YYYYMMDD-001` *(illustrative)* | Kansas HUC12 + 1 USGS gauge fixture + NHDPlus crosswalk + NFHL contextual overlay | `candidate` | *PROPOSED:* `release/manifests/hyd-YYYYMMDD-001.json` | *PROPOSED:* `data/proofs/evidence_bundle/…` | *PROPOSED:* `release/promotion_decisions/hyd-YYYYMMDD-001.json` | *UNKNOWN until prior release exists* | none | *PROPOSED:* DSSE / cosign + Rekor index | First credible Hydrology thin slice per [DOM-HYD §N]. NFHL renders as *regulatory context*; **never** as observed flood. |
| *…add rows here as releases land…* | | | | | | | | | |

> [!IMPORTANT]
> The single illustrative row above is **labeled as such**. It is not a record of any actual release. Do not cite this row as evidence that a release exists.

[Back to top](#hydrology--release-index)

---

## 9. Closure rules — what every Hydrology release must resolve

Every Hydrology release that reaches `PUBLISHED` must satisfy the following, in addition to KFM-wide gate doctrine. [DOM-HYD §M] [ENCY §24] [DIRRULES §9.1]

<details>
<summary><b>Closure rules — full list</b></summary>

1. **`SourceDescriptor` + `SourceActivationDecision`** for every source the release touches (USGS Water APIs, WBD/HUC, NHDPlus HR, FEMA NFHL/MSC, 3DEP, state water offices, water-quality programs, groundwater wells, irrigation/drought sources). [DOM-HYD §D]
2. **Source-role separation** is preserved. NFHL regulatory polygons MUST NOT be promoted as observed inundation; operational warnings MUST NOT be treated as life-safety authority inside KFM. A source role is fixed at admission and **never upgraded by promotion**. [DOM-HYD] [ENCY §20.4, §24.9.2]
3. **Identity rules** for `HUCUnit`, `HydroFeature`, `ReachIdentity`, `GaugeSite`, `FlowObservation`, `WaterLevelObservation`, `WaterQualityObservation`, `GroundwaterWell`, `NFHLZone` — PROPOSED basis: `source_id + object_role + temporal_scope + normalized_digest`. [DOM-HYD §E]
4. **Temporal separation**: `observed_time`, `valid_time`, `source_time`, `retrieval_time`, `release_time`, and `correction_time` stay distinct where material. Provisional vs. final USGS status is preserved. [DOM-HYD §E]
5. **NHDPlus HR / WBD crosswalk** ambiguity is recorded with `alignment_score` and `decision_reason`. The release `ABSTAIN`s on ambiguous reach identity rather than collapsing it. [DOM-HYD §K]
6. **Validation report** binds to the release. PROPOSED validators include HUC12 fingerprint validation, NHDPlus HR identity-ambiguity tests, USGS parameter/unit/qualifier/no-data tests, NFHL role-separation tests, and `EvidenceBundle` closure tests. [DOM-HYD §K]
7. **`EvidenceBundle` closure** — every `EvidenceRef` resolves to an `EvidenceBundle`; `source_id` resolves to `SourceDescriptor`; `model_id` resolves to `ModelRunReceipt`. [ENCY §24.6.2]
8. **Catalog closure** — STAC, DCAT, and PROV records exist, mutually reference each other, and reference the `EvidenceBundle` and `ReleaseManifest`. [ENCY §24]
9. **`ReleaseManifest`** exists, lists artifacts with digests, declares supersession or first-release status. A `ReleaseManifest` is a single, signed, hashable object pinning the release to specific evidence. [DIRRULES §9.2] [ENCY §24.2]
10. **`PromotionDecision`** is recorded; release authority is separate from the original author when materiality applies. [ENCY §24.6.1, §24.7.2]
11. **Rollback target** is identified and a `RollbackCard` exists before the release is treated as safely publishable. [ENCY §24.6.1]
12. **Correction path** is published: stale-state rule, supersession lineage, and downstream-derivative invalidation list are pre-staged. [ENCY §24.6.1, §24.8]
13. **Signatures** — DSSE / cosign attestation, Rekor inclusion (where applicable), with `spec_hash` of the canonical sidecar matching the attested predicate. *(PROPOSED operational pattern.)*
14. **Trust-membrane invariant** — no public client, no normal UI surface, and no released AI surface reaches `RAW`, `WORK`, `QUARANTINE`, canonical/internal stores, graph internals, vector indexes, source APIs, or direct model runtimes. The governed API is the only route to `ANSWER`. [GAI] [ENCY §24.6.2]

</details>

> [!CAUTION]
> Visual correctness is **not** release readiness. A Hydrology layer that renders is still unready if any closure link above is broken — missing evidence ref, unresolved provenance, unresolved policy, missing proof, or a `ReleaseManifest` pointing to a phantom record. [KFM-IDX-REL-001]

[Back to top](#hydrology--release-index)

---

## 10. Sensitivity, rights, and publication posture

**CONFIRMED doctrine.** Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state **blocks** public promotion. [ENCY] [DIRRULES]

Hydrology-specific posture (CONFIRMED doctrine, PROPOSED enforcement):

- **Unclear rights** for a Hydrology source → deny public promotion until resolved.
- **Flood-role misuse** (NFHL-as-observed-flood, forecast-as-truth, KFM-as-alert-authority) → **deny by default**. [DOM-HYD] [ENCY §20.4]
- **Infrastructure / private-property implications** (e.g., gauge locations on private land, well owners) → require review and public-safe generalization before exposure.
- **Emergency-alert boundary** — Hydrology shares this with Hazards and Air: KFM **must not** be used as a life-safety instruction surface. [ENCY §20.4]

For the full lane posture see [`PUBLICATION_POSTURE.md`](./PUBLICATION_POSTURE.md); for the deny-by-default summary see [Appendix B](#appendix-b--hydrology-specific-deny-by-default-register). Route any genuinely sensitive disposition through the operating contract's §23.2 sensitive-domain decision matrix.

[Back to top](#hydrology--release-index)

---

## 11. Quickstart — how to use this index

```text
1. Find the release.
   • Look up the release_id in the register table (§8).
   • The row links to the ReleaseManifest, EvidenceBundle, PromotionDecision,
     rollback target, signatures, and any corrections.

2. Trace evidence.
   • From ReleaseManifest → EvidenceBundle → SourceDescriptor(s).
   • Every cited claim resolves to evidence, not the other way around.

3. Verify integrity.
   • Match artifact digests in ReleaseManifest against published artifacts.
   • If signatures are present, verify DSSE / cosign and Rekor inclusion.
   • Confirm the sidecar spec_hash matches the attested predicate.

4. Check supersession & rollback.
   • If state is 'superseded' or 'rolled_back', follow the lineage links
     before quoting the release as current.

5. Respect the trust membrane.
   • Consume Hydrology data through the governed API, not via raw or
     canonical stores.
```

[Back to top](#hydrology--release-index)

---

## 12. Verification backlog and open questions

Each item is **NEEDS VERIFICATION** / `OPEN` / `UNKNOWN` until checked against mounted-repo evidence. [DOM-HYD §N]

| Item | Evidence that would settle it | Status |
|---|---|---|
| Verify the schema home for `HydrologyDecisionEnvelope` and Hydrology object schemas | mounted-repo files, schemas, ADR-0001 reference | NEEDS VERIFICATION |
| Verify HUC12 fixture and fingerprint rule | repo fixtures, validators, tests | NEEDS VERIFICATION |
| Verify NHDPlus HR crosswalk and ambiguity `ABSTAIN` behavior | validator output, no-network fixture, decision-envelope tests | NEEDS VERIFICATION |
| Verify USGS Water normalizer + NFHL source-role separation | repo code, schemas, fixtures, test suite | NEEDS VERIFICATION |
| Verify Hydrology API resolver routes (`/hydrology/...`) | mounted `apps/governed-api/` source | NEEDS VERIFICATION |
| Verify MapLibre Hydrology layer adapter + `LayerManifest` shape | mounted `packages/maplibre-runtime/` + `LayerManifest` schema *(name updated: `packages/maplibre/` retired in v1.3, DIRRULES §8.1)* | NEEDS VERIFICATION |
| Confirm `release/candidates/hydrology/` is populated (the **dir pattern is CONFIRMED**, the segment is not) | mounted-repo directory listing | NEEDS VERIFICATION |
| Confirm `data/published/layers/hydrology/` is populated (pattern CONFIRMED §9.1) | mounted-repo directory listing, release-manifest fixtures | NEEDS VERIFICATION |
| Confirm signature workflow (cosign + Rekor) for Hydrology PMTiles | mounted CI workflow, signature artifacts | NEEDS VERIFICATION |
| Resolve `PROV.md` vs. `PROVENANCE.md` naming impact on Hydrology PROV records | ADR (OPEN-DR-01) + docs reference scan | OPEN ADR |
| Determine which actor approves Hydrology promotion (steward role + authority recording) | governance ADR (ADR-S-09), CODEOWNERS, release register | UNKNOWN |
| Confirm canonical release-state enum vs. the §7 working vocabulary | release-state register / schema | NEEDS VERIFICATION |
| Validator exit-code → finite-outcome contract (cross-tool standard) | ADR (OPEN-DR-03); CI calls `tools/validate_all.py` | OPEN ADR |

[Back to top](#hydrology--release-index)

---

## 13. FAQ

**Q. Is this file the place to publish a release?**
No. This file *indexes* releases. The authoritative `ReleaseManifest`, `PromotionDecision`, signatures, and rollback cards live under `release/`. Published artifacts live under `data/published/`. [DIRRULES §9.2]

**Q. Why is NFHL not an observed flood layer?**
NFHL is a regulatory flood-hazard mapping product, not a record of observed inundation. Collapsing them would misrepresent both regulatory exposure and real flood evidence and is denied by KFM doctrine. [DOM-HYD §B, §I] [ENCY §20.4]

**Q. What if a release fails one closure rule but seems fine to publish?**
It is not fine. The closure rules are *invariants*, not recommendations. A release that fails any closure rule fails closed and is held at the prior state. [ENCY §24.6.2]

**Q. Can AI write the release summary on this page?**
Generated language may help draft text, but the index **must** resolve to evidence — `ReleaseManifest`, `EvidenceBundle`, `PromotionDecision`, signatures. AI is interpretive, never the root truth source. [GAI]

**Q. What about historical Hydrology releases predating this index?**
Add a row per historical release, mark `state` accurately (`superseded`, `withdrawn`, `rolled_back`, or `published`), and link the existing manifests and proofs. If no `ReleaseManifest` exists for a historical artifact, mark it `UNKNOWN` and open a verification-backlog entry rather than fabricating a manifest.

**Q. How does this index handle cross-domain releases (e.g., Hydrology × Hazards)?**
Cross-domain releases are indexed by the domain whose `release_id` owns the artifact. A cross-link row in the other domain's `RELEASE_INDEX.md` references the canonical row here. Shared validators live under a topic segment (e.g., `tools/validators/<topic>/`), not under a single domain folder, per Directory Rules §12.

[Back to top](#hydrology--release-index)

---

## 14. Related docs

> Links below are **PROPOSED** unless marked CONFIRMED. Replace each `TODO` with the canonical path when known. Note that the canonical operating contract and directory rules live at the **repo root**, not under `docs/doctrine/`.

- [`docs/domains/hydrology/README.md`](./README.md) — Hydrology domain landing
- [`docs/domains/hydrology/PUBLICATION_POSTURE.md`](./PUBLICATION_POSTURE.md) — lane publication posture
- `ai-build-operating-contract.md` — canonical operating contract (`CONTRACT_VERSION = "3.0.0"`) — *root path CONFIRMED in project*
- `directory-rules.md` — placement law (§9.1 lifecycle, §9.2 `release/`, §12 domain placement, §13 anti-patterns) — *root path CONFIRMED in project*
- `docs/architecture/governed-ai/` — governed AI behavior for Hydrology — *TODO: confirm*
- `docs/standards/PROV.md` — provenance standard profile *(open ADR: `PROV.md` vs `PROVENANCE.md`, OPEN-DR-01)*
- `docs/standards/ISO-19115.md` — geospatial metadata crosswalk — *TODO: confirm*
- `docs/standards/OGC-API-TILES.md`, `docs/standards/PMTILES.md` — tile / PMTiles standard profiles — *TODO: confirm*
- `docs/standards/OAI-PMH.md` — metadata harvest standard — *TODO: confirm*
- `docs/runbooks/hydrology/SOURCE_REFRESH_RUNBOOK.md` — *PROPOSED, mirrors the Fauna source-refresh runbook pattern; subfolder convention OPEN-DR-02*
- `release/candidates/hydrology/README.md` — candidate home README — *TODO: create per DIRRULES §15 required-README contract*

[Back to top](#hydrology--release-index)

---

## Appendix A — Source families and source-role doctrine

**CONFIRMED source families** for Hydrology. [DOM-HYD §D] [ENCY]

| Source family | Source role | Notes |
|---|---|---|
| USGS Water Data / NWIS APIs | Observation (primary; canonical streamgage authority) | Preserve site metadata, parameter code, unit, qualifier, provisional/final status. USGS is the canonical authority for streamgage data. |
| USGS WBD (Watershed Boundary Dataset) / HUC | Authority / reference geometry | HUC12 is the working unit; carry `alignment_score` for crosswalks |
| USGS NHDPlus HR / 3DHP | Authority / reference network + value-added attributes | ABSTAIN on ambiguous reach identity |
| FEMA NFHL / MSC | Regulatory / context | **NOT observed flood**, **NOT life-safety**, **NOT alert authority** |
| 3DEP | Authority / context (terrain raster) | Used for hydro-enforced derivatives, not as observation |
| State water offices (KDA-DWR / KGS / KDHE; WIMAS/WRIS, WWC5, WIZARD) | Authoritative state records / observation | Source-role determined per dataset; WIMAS/WRIS shapes have shifted historically — receipt records the observed shape version |
| Water-quality programs | Observation (variable role) | Preserve method, detection limits, qualifiers |
| Groundwater wells | Observation + reference | Sensitivity review for ownership and precise location |
| Irrigation / drought sources | Mixed (observation / aggregate / model) | Aggregations preferred over precise sub-parcel claims |

> [!NOTE]
> Source role MUST be declared in the `SourceDescriptor` and MUST NOT be inferred from
> convenience. A regulatory layer is not an observation; an operational warning is not
> life-safety authority inside KFM. [DOM-HYD]
>
> **NEEDS VERIFICATION:** the project notes that USGS APIs "occasionally restructure" and that
> watchers must track API versions explicitly, but it does **not** state a specific
> `waterservices.usgs.gov` phase-out date. Any specific deprecation timeline (e.g., a
> particular year) is NEEDS VERIFICATION against current USGS documentation before being
> asserted — pin clients to a recorded API version regardless.

[Back to top](#hydrology--release-index)

---

## Appendix B — Hydrology-specific deny-by-default register

Selected entries from the global deny-by-default register that touch Hydrology releases. [ENCY §20.4–§20.5]

| Failure mode | Default outcome | Required for non-default outcome |
|---|---|---|
| Unclear rights on a Hydrology source | `DENY` | Steward review + rights resolution + `SourceActivationDecision` |
| NFHL surfaced as observed flood | `DENY` | Not allowed — re-frame as regulatory context |
| KFM presented as emergency-alert authority | `DENY` | Not allowed under any framing |
| Missing `EvidenceBundle` closure for a release | `DENY` | Complete closure (see §9) |
| Catalog/release digest mismatch | `HOLD` / `DENY` / `ERROR` | Manifest fix + verifier re-run |
| Missing rollback target | `RELEASE_MANIFEST_INVALID` / `ROLLBACK_TARGET_MISSING` → fail closed | Supply rollback target + verify |
| Reach identity ambiguous after NHDPlus HR crosswalk | `ABSTAIN` | Record `alignment_score` + `decision_reason`; await steward decision |
| Uncited AI claim on a Hydrology Focus Mode answer | `ABSTAIN` / `DENY` | Resolve `EvidenceRef` → released `EvidenceBundle` |

[Back to top](#hydrology--release-index)

---

<sub>**Citation key.** [DOM-HYD] Hydrology domain dossier (KFM Domains Culmination Atlas §4) · [ENCY] KFM Encyclopedia · [DIRRULES] Directory Rules v1.3 · [BLD-COMP] Components Pass 10 · [IMPL-PIPE] Unified Implementation Architecture Build Manual · [GAI] Governed AI doctrine · [KFM-IDX-REL-001] Idea index — catalog closure.</sub>

---

> [!NOTE]
> **Doctrine vs. implementation.** Every claim about doctrine in this file is CONFIRMED against the attached KFM corpus. Every claim about repository paths, filenames, validator names, route names, or active enforcement is PROPOSED / NEEDS VERIFICATION until the repo is mounted and inspected — except the top-level `release/` and `data/` layout, which is CONFIRMED against Directory Rules §9.1–§9.2.

---

*Last updated: 2026-06-07 · `CONTRACT_VERSION = "3.0.0"` · Maintainers: Hydrology steward(s) + Docs steward (TBD)* · [Back to top](#hydrology--release-index)
