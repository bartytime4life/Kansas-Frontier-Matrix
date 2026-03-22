<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS_VERIFICATION_UUID>
title: data/
type: standard
version: v1
status: draft
owners: NEEDS VERIFICATION
created: NEEDS_VERIFICATION_YYYY-MM-DD
updated: 2026-03-21
policy_label: NEEDS VERIFICATION
related: [../README.md, ./registry/README.md, ./specs/README.md, ./catalog/README.md, ./catalog/stac/README.md]
tags: [kfm, data, truth-path, catalog, provenance]
notes: [Baseline doctrine grounded mainly in March 2026 KFM master manuals; continuity artifacts document repo-root data/ plus data/registry/README.md and data/catalog/stac/README.md at an earlier commit, but the mounted live checkout was not available in this session.]
[/KFM_META_BLOCK_V2] -->

# `data/`

Governed storage, lifecycle, and release-artifact surface for KFM evidence-bearing data.

> **Status:** experimental  
> **Doc state:** draft  
> **Owners:** NEEDS VERIFICATION  
> **Path target:** `data/README.md`  
> ![status](https://img.shields.io/badge/status-experimental-orange)
> ![doc](https://img.shields.io/badge/doc-directory__README-blue)
> ![owners](https://img.shields.io/badge/owners-NEEDS_VERIFICATION-lightgrey)
> ![truth_path](https://img.shields.io/badge/truth_path-governed-0a7d5a)
> ![catalog](https://img.shields.io/badge/catalog-DCAT%2BSTAC%2BPROV-5b4bdb)
> ![checkout](https://img.shields.io/badge/checkout-unmounted-lightgrey)
> ![path_evidence](https://img.shields.io/badge/path_evidence-continuity__artifact-yellow)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> This README keeps three evidence layers separate on purpose:
>
> - **CONFIRMED doctrine** for KFM lifecycle law, trust boundaries, artifact families, catalog closure, and promotion posture.
> - **INFERRED continuity** for `data/` as a documented repo-root surface and for a small number of neighboring README and schema paths described in continuity artifacts.
> - **PROPOSED starter shape** for concrete zone directories that align strongly with doctrine but were **not** reverified from a mounted live checkout in this session.

> [!NOTE]
> This file uses **CATALOG** for the lifecycle state and **catalog triplet** for the linked `DCAT + STAC + PROV` closure that makes a version discoverable, traceable, and evidence-resolvable.

## Scope

In continuity artifacts, `data/` is described at repo root as the surface for **registry entries, example datasets, catalog artifacts, and zone manifests**. In March 2026 doctrine, that practical repo role is widened into the explicit KFM truth-path model:

`Source edge -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG -> PUBLISHED`

That makes `data/` more than storage. In KFM, it is the governed surface where intake, transformation, validation, catalog closure, release evidence, and correction lineage remain inspectable enough to audit, review, replay, and repair.

### What this README is for

This file is meant to help maintainers do four things quickly:

1. understand what belongs in `data/`,
2. distinguish **CONFIRMED doctrine** from **INFERRED / PROPOSED repo shape**,
3. keep storage responsibilities separate from contracts, policy, and governed APIs,
4. extend the live tree without quietly weakening KFM’s trust posture.

### Evidence posture for this README

| Layer | Status | How to read it |
|---|---|---|
| Truth path, trust membrane, authoritative-versus-derived split, catalog triplet, promotion/correction posture | **CONFIRMED** | Safe to treat as current project doctrine. |
| `data/` as a documented repo-root surface | **INFERRED** | Supported by continuity artifacts, but not reverified from a mounted checkout in this run. |
| `data/registry/README.md` and `data/catalog/stac/README.md` | **INFERRED** | Documented at an earlier repo state in continuity artifacts; current checkout still needs direct verification. |
| `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/receipts/`, `data/published/`, `data/proofs/` | **PROPOSED** | Doctrine-aligned starter skeleton; not live-tree fact here. |
| `data/specs/README.md` and `data/catalog/README.md` | **NEEDS VERIFICATION** | Retained because task metadata expects them, but their live presence was not proven in this session. |

[Back to top](#data)

## Repo fit

`data/` sits at the seam where governed source intake becomes durable project state.

### Path and adjacent surfaces

| Relation | Surface | Posture | Why it matters |
|---|---|---|---|
| Upstream | [`../README.md`](../README.md) | **NEEDS VERIFICATION** | Expected repo-wide overview and navigation surface. |
| Upstream | [`../packages/`](../packages/) | **INFERRED** | Shared reusable law should stay in packages rather than leaking into ad hoc storage layouts. |
| Upstream | [`../contracts/`](../contracts/) | **INFERRED** | Shared schemas, profiles, and controlled vocabularies should remain explicit rather than hiding inside data zones. |
| Upstream | [`../policy/`](../policy/) | **INFERRED** | Rights, sensitivity, deny-by-default rules, and review obligations belong in executable policy as well as prose. |
| Upstream | [`../docs/`](../docs/) | **INFERRED** | Architecture docs, ADRs, templates, and runbooks should track behavior-significant changes to the data surface. |
| Lateral | [`./registry/README.md`](./registry/README.md) | **INFERRED** | Continuity artifacts point here as the likely source and dataset registration surface. |
| Lateral | [`./catalog/stac/README.md`](./catalog/stac/README.md) | **INFERRED** | Continuity artifacts point here as the likely STAC-facing catalog surface. |
| Lateral | [`./catalog/README.md`](./catalog/README.md) | **NEEDS VERIFICATION** | Doctrine-aligned adjacency, but not proven live in this session. |
| Lateral | [`./specs/README.md`](./specs/README.md) | **NEEDS VERIFICATION** | Kept because task metadata names it, but `../contracts/` still appears stronger for shared schema authority unless the checkout proves otherwise. |
| Downstream | [`../apps/`](../apps/) | **INFERRED** | Public and role-limited surfaces should consume promoted scope through governed APIs, not direct storage reads. |
| Downstream | [`../tools/`](../tools/) | **INFERRED** | Validators, link checks, catalog QA, and evidence linting should prove the data surface rather than merely describe it. |
| Downstream | [`../tests/`](../tests/) | **INFERRED** | Schema, catalog, policy, freshness, correction, and replay tests should enforce this surface. |
| Downstream | [`../infra/`](../infra/) | **INFERRED** | Deployment, backup, restore, correction, and reconciliation logic must preserve the trust membrane. |

### Repo-fit summary

| Question | Answer |
|---|---|
| What is `data/` for? | Governed intake, lifecycle state, catalog closure, release evidence, and repo-facing data surfaces such as registry entries and catalog artifacts. |
| What is `data/` **not**? | Not the trust membrane, not the public API surface, and not a license to expose RAW, WORK, QUARANTINE, or unpublished candidates directly. |
| What stays adjacent instead of buried here? | Shared contracts, executable policy, app routes, worker logic, and most implementation law. |

[Back to top](#data)

## Accepted inputs

The following belong in or immediately around `data/` when KFM doctrine is being honored:

| Accepted input | Why it belongs here | Typical stage |
|---|---|---|
| Source registration artifacts | Source onboarding is a contract, not just a fetch | Registry / admission |
| Immutable raw captures and acquisition manifests | RAW must preserve source-native bytes and intake memory | RAW |
| Reproducible transforms, redactions, and QA outputs | WORK exists to normalize and validate without pretending to publish | WORK |
| Rights-unclear, sensitive, or failed-validation material | QUARANTINE is the regular hold state for unresolved material | QUARANTINE |
| Canonical processed dataset versions | PROCESSED is where publishable authority becomes stable and inspectable | PROCESSED |
| Run receipts, validation reports, and audit-ready process memory | Replay, rollback, and correction fail without durable process evidence | WORK / receipts |
| `DCAT + STAC + PROV` closure artifacts | Catalog closure is part of release truth, not decorative metadata | CATALOG |
| Release manifests, proof packs, and integrity objects | Promotion is a governed transition and should leave receipts | Release boundary |
| Zone manifests, public-safe exemplars, and example datasets | Continuity artifacts describe these as part of the repo-facing role of `data/` | Reference / exemplar |

### Artifact families at a glance

| Artifact family | What it does | Stage seam |
|---|---|---|
| `SourceDescriptor` | Declares source identity, access mode, rights posture, cadence, and publication intent | Admission |
| `IngestReceipt` | Proves what was fetched, when, and with what integrity result | RAW |
| `ValidationReport` | Records structural, spatial, temporal, unit, and domain QC outcomes | WORK / QUARANTINE |
| `DatasetVersion` | Carries immutable processed authority with stable identity and time semantics | PROCESSED |
| `CatalogClosure` | Links outward catalog metadata and lineage for releasable scope | CATALOG |
| `DecisionEnvelope` / `ReviewRecord` | Carries policy and review-bearing admissibility outcomes | Review / release |
| `ReleaseManifest` / `ReleaseProofPack` | Assembles a publishable trust unit | Promotion / release |
| `EvidenceBundle` | Resolves visible claims or surface state to inspectable support | Runtime / trust surfaces |
| `CorrectionNotice` | Preserves visible lineage for rollback, supersession, withdrawal, or narrowed republication | Post-release governance |

### Dataset-version pack *(PROPOSED starter shape)*

| Part | Typical location | Why it exists |
|---|---|---|
| Manifest + checksums | `data/processed/<theme>/<dataset>/<version>/manifest.json`, `SHA256SUMS.txt` | Stable fingerprinting and replay |
| Version README | `data/processed/<theme>/<dataset>/<version>/README.md` | Human-readable method, CRS, units, caveats, license, and links |
| Receipt / validation pack | `data/receipts/` or version-adjacent audit surface | Run receipts, validation reports, policy decisions, and replay memory |
| STAC / DCAT / PROV | `data/catalog/stac/`, `data/catalog/dcat/`, `data/catalog/prov/` | Discoverability, lineage, and policy-facing metadata closure |
| Proof / attestation pack | `data/proofs/` or equivalent release bundle | Promotion evidence, integrity, and rollback traceability |

> [!TIP]
> `data/` may **consume** shared schemas from `../contracts/`, but that is different from treating `data/` as the canonical home for every shared schema, vocabulary, or standards profile.

[Back to top](#data)

## Exclusions

The following do **not** belong here as sovereign truth or as the normal public path:

| Exclusion | Put it under / behind | Why |
|---|---|---|
| Direct client reads from canonical stores or unpublished artifacts | Governed APIs and trust-visible app surfaces | Storage is not the trust membrane. |
| Secrets, credentials, tokens, or host-specific secret material | Runtime secret management / deployment layer | `data/` is evidence-bearing, not secret-bearing. |
| Shared schemas and standards profiles | `../contracts/` | Keeps machine-readable contract authority explicit and reviewable. |
| Policy bundles, reason registries, and deny-by-default logic | `../policy/` | Policy should remain executable, testable, and independently reviewable. |
| Unreviewed analyst scratch outputs presented as publishable truth | `work/` or quarantine | Exploration is valid; silent publication is not. |
| Derived layers treated as authority by convenience | Rebuildable downstream layers | Search, graph, tile, vector, scene, cache, and summary layers remain downstream of stronger truth. |
| Silent overwrite of raw capture, processed authority, or released state | Correction / rollback / supersession flow | KFM requires visible correction lineage. |

> [!WARNING]
> `data/` is a governed evidence surface. It is **not** the public edge, **not** the trust boundary, and **not** permission to expose RAW, WORK, QUARANTINE, or unpublished candidates directly.

[Back to top](#data)

## Directory tree

### Continuity-artifact paths *(INFERRED; mounted checkout still needs verification)*

```text
data/
├── registry/
│   └── schemas/
└── catalog/
    └── stac/
```

### Doctrine-aligned starter skeleton *(PROPOSED)*

```text
data/
├── README.md
├── registry/                # source and dataset registration surfaces
├── raw/                     # immutable source-native capture
├── work/                    # transforms, QA, and reproducible intermediate work
├── quarantine/              # unresolved rights / sensitivity / validation hold
├── processed/               # canonical publishable derivatives and dataset versions
├── catalog/                 # catalog closure boundary
│   ├── dcat/
│   ├── stac/
│   └── prov/
├── receipts/                # run receipts, validation reports, and audit-ready process memory
├── published/               # optional materialized release scope; publication remains a state first
└── proofs/                  # release manifests, proof packs, attestations, and correction trace
```

### Path posture

| Path claim | Status | Reading rule |
|---|---|---|
| `data/` is a documented repo-root area | **INFERRED** | Supported by continuity artifacts; verify live presence in checkout. |
| `data/registry/` and `data/catalog/stac/` exist as documented continuity subpaths | **INFERRED** | Earlier audited materials point to both; current checkout still needs verification. |
| `data/registry/schemas/` carries registry schema material | **INFERRED** | A continuity artifact points to `data/registry/schemas/dataset_entry.schema.json`; verify live tree before wiring automation. |
| `data/raw/`, `data/work/`, `data/processed/`, `data/catalog/`, and possibly `data/receipts/` are part of the documented lifecycle shape | **NEEDS VERIFICATION** | Strong continuity support exists, but exact live naming and placement still need direct checkout confirmation. |
| `data/quarantine/`, `data/published/`, and `data/proofs/` exist today as real directories | **PROPOSED** | Strong doctrine-aligned starter skeleton; not live-tree fact in this session. |
| `data/specs/` is canonical | **UNKNOWN** | Keep only as a task-level adjacency until the mounted repo proves it. |

### What this README intentionally does *not* assert

- any specific worker, package, or service already wired to every zone,
- any exact filename convention below the zone level,
- any guarantee that `published/`, `proofs/`, or `receipts/` are already materialized directories in the live checkout,
- any claim that `data/catalog/README.md` or `data/specs/README.md` currently exist.

[Back to top](#data)

## Quickstart

Before trusting any path-level claim in this README, inspect the live checkout.

```bash
# Confirm the target surface exists
pwd
find data -maxdepth 4 -print 2>/dev/null | sort

# Read local README files if present
test -f data/README.md && sed -n '1,240p' data/README.md
test -f data/registry/README.md && sed -n '1,220p' data/registry/README.md
test -f data/catalog/README.md && sed -n '1,220p' data/catalog/README.md
test -f data/catalog/stac/README.md && sed -n '1,220p' data/catalog/stac/README.md
test -f data/specs/README.md && sed -n '1,220p' data/specs/README.md

# Inspect registry-local schema evidence if present
test -f data/registry/schemas/dataset_entry.schema.json && \
  sed -n '1,120p' data/registry/schemas/dataset_entry.schema.json

# Inspect artifact-shaped files if present
find data -maxdepth 6 -type f \
  \( -iname '*manifest*' -o -iname '*receipt*' -o -iname '*proof*' -o -iname '*catalog*' -o -iname '*.json' -o -iname '*.jsonld' -o -iname '*.prov' -o -iname '*.yaml' -o -iname '*.yml' \) \
  2>/dev/null | sort | sed -n '1,240p'
```

### Minimal verification pass

```bash
# Confirm or downgrade the continuity and starter-shape claims
for p in \
  data \
  data/registry \
  data/registry/schemas \
  data/catalog \
  data/catalog/stac \
  data/raw \
  data/work \
  data/quarantine \
  data/processed \
  data/receipts \
  data/published \
  data/proofs \
  data/specs
do
  test -e "$p" && echo "FOUND $p" || echo "MISSING $p"
done

# Check whether catalog-triplet artifacts exist
find data -type f 2>/dev/null | grep -Ei '/(stac|dcat|prov)/|catalog' || true

# Check whether receipt/proof-bearing artifacts are already emitted somewhere under data/
find data -type f 2>/dev/null | grep -Ei 'receipt|manifest|proof|attest|bundle|correction|checksum' || true

# If data/specs is absent, compare with contracts/
test -d data/specs && echo "FOUND data/specs" || echo "VERIFY ../contracts before creating data/specs"
```

> [!TIP]
> If the checkout shows `../contracts/` as the canonical home for shared schemas and vocabularies, keep `./specs/README.md` as a documentation adjacency only, not as a prompt to create drift.

[Back to top](#data)

## Usage

### 1. Register before you fetch

In KFM, source intake is a contract, not a download. A source that cannot be named, replayed, rights-reviewed, and quality-checked is not ready for governed movement into `data/`.

### 2. Keep RAW immutable

`RAW` should preserve source-native bytes, request context, rights or terms snapshots, and checksums. Cleanup, normalization, OCR, reprojection, redaction, and summarization belong later.

### 3. Transform in `WORK`, hold ambiguity in `QUARANTINE`

`WORK` is where normalization, parsing, joins, QA, redaction, and repair happen. Rights ambiguity, failed validation, unresolved sensitivity, or low-confidence extraction belong in `QUARANTINE`, not in `PROCESSED`.

### 4. Treat `PROCESSED` as governed authority candidates

`PROCESSED` is where stable dataset versions emerge. They should already point back to receipts, validation outputs, source context, and reproducible transform memory strongly enough to survive audit and replay.

### 5. Keep receipts and reports queryable

Run receipts, validation reports, and audit references are part of KFM’s operational memory. Whether they live under `data/receipts/` or an equivalent audited surface, they should remain easy to resolve during replay, correction, and release review.

### 6. Close the catalog triplet before promotion

A version is not outward-ready until `DCAT + STAC + PROV` can cross-link identifiers, assets, lineage, and evidence references without guesswork.

### 7. Publish by governed transition

`PUBLISHED` is first a release state, not merely a directory name. A repo may materialize supporting release artifacts under `data/published/`, but promotion still binds dataset version, catalog closure, policy state, review state, and proof objects into one inspectable decision.

### 8. Keep proofs attached to the exact release they justify

Checksums, manifests, proof packs, attestations, and correction evidence should remain linked to the exact dataset version or release scope they support. Detached proof objects are much less useful during rollback, audit, or dispute.

### Illustrative artifact chain

The exact live filenames are **NEEDS VERIFICATION**, but the intended sequence is stable:

```text
registry/      source descriptor / source admission context
raw/           ingest receipt + immutable capture
work/          validation report + transform evidence
quarantine/    rights / sensitivity / validation hold
processed/     dataset version + manifest + checksums
receipts/      run receipts / validation outputs / audit-ready process memory
catalog/       catalog closure (DCAT + STAC + PROV)
published/     optional materialized release scope
proofs/        release proof pack / attestation / correction trace
```

[Back to top](#data)

## Diagram

```mermaid
flowchart LR
    REG[Registry / SourceDescriptor] --> RAW[RAW<br/>immutable capture]
    RAW --> WORK[WORK<br/>transform + QA]
    WORK --> QUAR[QUARANTINE<br/>rights / sensitivity / failure hold]
    WORK --> PROC[PROCESSED<br/>dataset version]
    WORK --> REC[RECEIPTS<br/>run receipts + validation]
    PROC --> CAT[CATALOG<br/>DCAT + STAC + PROV]
    CAT --> PUB[PUBLISHED<br/>governed release state]

    PUB --> API[Governed API]
    API --> UI[Map / Dossier / Story / Export]
    API --> FOCUS[Focus Mode]

    REC -. support .-> CAT
    PROOF[Proofs / manifests / attestations] -. support .-> PUB
    EVD[EvidenceBundle] -. drill-through .-> CAT

    UI -. no direct path .-> RAW
    UI -. no direct path .-> PROC
    FOCUS -. no uncited answer path .-> RAW
```

[Back to top](#data)

## Tables

### Truth-path zone matrix

| Zone / state | Core question | What belongs here | Block if |
|---|---|---|---|
| `RAW` | What exactly arrived? | Source-native payloads, request details, checksums, rights snapshots, unmodified source bytes | Raw bytes are mutated in place or exposed directly |
| `WORK` | What deterministic transform is happening? | Repair, normalization, OCR, reprojection, QA, joins, redaction transforms | Transform logic is irreproducible or undocumented |
| `QUARANTINE` | What is unresolved or unsafe? | Rights ambiguity, sensitivity ambiguity, failed validation, low-confidence extraction | Ambiguous material is treated as “almost publishable” |
| `PROCESSED` | What is now canonical and publishable? | Immutable processed artifacts, dataset versions, final QA outputs, stable manifests | The artifact cannot support valid catalog closure |
| `CATALOG` | Can the release be discovered and explained? | Cross-linked `DCAT + STAC + PROV`, outward identifiers, evidence pointers | Triplet members are missing, broken, or unresolved |
| `PUBLISHED` | May this scope be exposed? | Governed release state through API and trust-visible surfaces | Publication is treated as a folder copy instead of a gated transition |

### Release-adjacent support surfaces

| Surface | Status | Role | Caution |
|---|---|---|---|
| `receipts/` | **NEEDS VERIFICATION as directory / CONFIRMED as artifact family** | Run receipts, validation reports, and audit-ready process memory | Exact placement may differ even if receipt artifacts are already part of the doctrine |
| `published/` | **PROPOSED directory / CONFIRMED state concept** | Optional materialized release scope for governed outputs | Publication itself still must be treated as a transition, not a folder copy |
| `proofs/` | **PROPOSED** | Release manifests, proof packs, attestations, signatures, correction trace | Proof objects must stay linked to the release or dataset version they justify |
| Dataset version README | **PROPOSED** | Human-readable summary of method, CRS, units, caveats, license, and links | Do not let README prose replace machine-checkable manifests or catalog closure |

### Minimum gates before outward trust widens

| Gate family | What it proves | Fail-closed outcome |
|---|---|---|
| Source admission | A source has a descriptor, owner/steward context, rights posture, and quality intent | Reject, defer, or quarantine |
| Source replay | Intake memory is strong enough to re-fetch and verify | Hold or quarantine |
| Schema / structure | Required fields, enums, and structural rules are satisfied | Block merge or promotion |
| Geometry / CRS | Geometry is valid and spatial support is coherent | Hold in `WORK / QUARANTINE` |
| Time validity | Time fields are present and semantically meaningful | Hold or quarantine |
| Identifier stability | IDs, spec hashes, and lineage pointers are deterministic enough to audit | Block canonical write or release |
| Catalog closure | `STAC + DCAT + PROV` resolve coherently | Block release or promotion |
| Policy bundle | Rights, sensitivity, reason codes, and deny-by-default logic are sufficient | Deny or hold |
| Evidence resolution | Consequential visible claims resolve to inspectable support | Runtime must abstain, deny, or error |
| Correction drill | Supersession, withdrawal, rollback, and correction remain visible and auditable | Prevent silent overwrite |

### Path-certainty matrix

| Claim | Status | Safer wording |
|---|---|---|
| `data/` exists as a repo-root path | **INFERRED** | “documented repo-root surface; verify in mounted checkout” |
| `data/` is governed by the canonical truth path | **CONFIRMED** | “load-bearing KFM doctrine” |
| `data/registry/README.md` exists | **INFERRED** | “documented in continuity artifact; current checkout still needs verification” |
| `data/catalog/stac/README.md` exists | **INFERRED** | “documented in continuity artifact; current checkout still needs verification” |
| `data/raw/`, `data/work/`, `data/processed/`, `data/catalog/`, and maybe `data/receipts/` are already live | **NEEDS VERIFICATION** | “continuity artifacts suggest these zones; verify actual subpaths” |
| `data/quarantine/`, `data/published/`, and `data/proofs/` exist today | **PROPOSED** | “starter skeleton from March 2026 manuals; verify live tree” |
| `data/specs/` is canonical | **UNKNOWN** | “requested adjacency; verify against `../contracts/` and the live tree” |

[Back to top](#data)

## Task list

### Definition of done for this README

- [ ] The file clearly separates **CONFIRMED doctrine** from **INFERRED / PROPOSED repo shape**.
- [ ] `data/` is described as a governed truth-path surface, not a generic storage bucket.
- [ ] Accepted inputs and exclusions are explicit.
- [ ] The tree distinguishes continuity-artifact paths from the March 2026 starter skeleton.
- [ ] The README makes clear that storage is not the trust membrane.
- [ ] At least one Mermaid diagram explains real KFM structure.
- [ ] Verification steps tell a maintainer how to confirm or downgrade path claims in a live checkout.

### Review checks before merge

- [ ] Replace placeholder `doc_id`, owners, created date, and policy label with repo-backed values.
- [ ] Verify all relative links against the actual checkout.
- [ ] Confirm whether shared schemas belong under `data/specs/` or `../contracts/`.
- [ ] Confirm whether `data/quarantine/` is a sibling directory or nested under `data/work/` in the live tree.
- [ ] Confirm whether `data/receipts/`, `data/published/`, and `data/proofs/` are real directories or only conceptual support surfaces.
- [ ] Add one real emitted artifact path once a live release lane is visible.
- [ ] Keep terminology aligned with KFM doctrine: truth path, trust membrane, authoritative vs derived, catalog closure, EvidenceBundle, promotion, correction.

[Back to top](#data)

## FAQ

### Is `published` a directory?

By doctrine, **published** is first a governed release state. `data/published/` is a plausible support directory for materialized release scope, but publication is still not reducible to “copy files somewhere.”

### Is `receipts` different from `proofs`?

Yes, conceptually. **Receipts** are process-memory artifacts such as ingest receipts, validation reports, and run records. **Proofs** are release-significant objects such as manifests, attestations, and correction trace. The exact live directory placement for either still needs verification.

### Are `data/registry/README.md` and `data/catalog/stac/README.md` already real?

They are **INFERRED**, not currently mounted facts. Continuity artifacts point to both paths at an earlier repo state, but this session did not expose a live checkout to verify them directly.

### Where should schemas live: `data/specs/` or `../contracts/`?

The strongest current-session evidence still favors `../contracts/` for shared schema authority. A narrow registry-local schema surface under `data/registry/schemas/` may exist for dataset-entry validation, but that does not automatically make `data/specs/` canonical.

### Are per-version dataset READMEs expected?

They are **PROPOSED**, but strongly aligned with the corpus. Dataset-gate design packs recommend a `README.md` beside promoted dataset artifacts describing source, method, CRS, units, caveats, license, and links to STAC/DCAT/PROV.

### Do graph, search, vector, tile, or scene layers belong under `data/`?

They may exist as downstream artifacts or build products, but they must remain explicitly downstream of approved release scope and must not become sovereign truth by convenience.

[Back to top](#data)

## Appendix

<details>
<summary>Glossary</summary>

| Term | Meaning in this README |
|---|---|
| Truth path | The governed movement from source edge through RAW, WORK / QUARANTINE, PROCESSED, CATALOG, and into PUBLISHED state. |
| Trust membrane | The rule that clients do not bypass governed APIs, policy mediation, and evidence resolution to reach storage directly. |
| Catalog triplet | The linked metadata boundary formed by `DCAT + STAC + PROV`. |
| SourceDescriptor | Intake contract describing access mode, cadence, rights posture, normalization plan, and publication intent. |
| IngestReceipt | Evidence-bearing record of what was fetched, when, and with what integrity result. |
| DatasetVersion | Immutable governed version of a processed subject set. |
| EvidenceBundle | Governed support object that resolves a visible claim or answer into inspectable evidence. |
| Derived layer | Search, graph, vector, tile, scene, summary, or export surface built downstream of stronger truth. |
| CorrectionNotice | Evidence-bearing supersession, withdrawal, rollback, or narrowed republication object. |

</details>

<details>
<summary>Verification backlog carried by this file</summary>

| Item | Why it matters |
|---|---|
| Actual `data/` tree snapshot | Converts documented target shape into inspectable repo fact |
| Owners / dates / policy label / doc UUID | Lets the meta block stop carrying placeholders |
| Real placement of `data/catalog/README.md` and `data/specs/README.md` | Prevents relative-link drift and schema-surface confusion |
| Whether `quarantine/` is nested or sibling | Avoids teaching the wrong tree shape |
| Whether `receipts/`, `published/`, and `proofs/` are materialized | Clarifies state-versus-directory behavior for release support |
| One emitted dataset pack with manifest + triplet + receipts/proof objects | Grounds examples in real artifacts rather than doctrine alone |

</details>

<details>
<summary>Related entrypoints</summary>

- [`../README.md`](../README.md)
- [`./registry/README.md`](./registry/README.md)
- [`./specs/README.md`](./specs/README.md)
- [`./catalog/README.md`](./catalog/README.md)
- [`./catalog/stac/README.md`](./catalog/stac/README.md)
- [`../packages/`](../packages/)
- [`../contracts/`](../contracts/)
- [`../policy/`](../policy/)
- [`../docs/`](../docs/)
- [`../tools/`](../tools/)
- [`../tests/`](../tests/)

</details>

[Back to top](#data)
