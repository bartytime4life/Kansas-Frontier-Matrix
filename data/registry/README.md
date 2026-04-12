<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-VERIFY
title: Data Registry
type: standard
version: v1
status: draft
owners: @bartytime4life
created: 2026-02-14
updated: 2026-04-12
policy_label: TODO-VERIFY
related: [../README.md, ../raw/README.md, ../work/README.md, ../quarantine/README.md, ../processed/README.md, ../receipts/README.md, ../published/README.md, ../proofs/README.md, ./schemas/README.md, ../catalog/README.md, ../catalog/dcat/README.md, ../catalog/stac/README.md, ../catalog/prov/README.md, ../../contracts/README.md, ../../contracts/vocab/README.md, ../../schemas/README.md, ../../schemas/contracts/README.md, ../../docs/standards/README.md, ../../tests/README.md, ../../tests/contracts/README.md, ../../policy/README.md, ../../tools/README.md, ../../docs/README.md, ../../.github/workflows/README.md, ../../.github/CODEOWNERS, ../../.github/PULL_REQUEST_TEMPLATE.md]
tags: [kfm, data, registry, onboarding, catalog, provenance]
notes: [doc_id and policy_label remain unresolved in current public evidence; created date is preserved from the supplied draft baseline; updated reflects this revision date; current public main confirms data/registry/README.md and data/registry/schemas/README.md while the wider schema-home and vocabulary-home story is now split across contracts/, contracts/vocab/, schemas/, and schemas/contracts/]
[/KFM_META_BLOCK_V2] -->

# Data Registry
Governed source-registration surface for KFM dataset identity, onboarding, and lifecycle handoff.

> **Status:** experimental  
> **Owners:** `@bartytime4life` *(per current public `.github/CODEOWNERS` coverage for `/data/`)*  
> **Path:** `data/registry/README.md`  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![owners](https://img.shields.io/badge/owners-%40bartytime4life-blue) ![surface](https://img.shields.io/badge/surface-data%20registry-0a7ea4) ![tree](https://img.shields.io/badge/current%20tree-README%20%2B%20schemas%2FREADME-lightgrey) ![onboarding](https://img.shields.io/badge/onboarding-governed-0a7d5a) ![triplet](https://img.shields.io/badge/triplet-DCAT%20%2B%20STAC%20%2B%20PROV-8250df) ![schema-home](https://img.shields.io/badge/schema_home-unresolved-red) ![vocab](https://img.shields.io/badge/vocab-shared%20lane%20visible-6f42c1)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)  
> **Repo fit:** parent [Data README][data-readme] · lifecycle [RAW][raw-readme] · [WORK][work-readme] · [QUARANTINE][quarantine-readme] · [PROCESSED][processed-readme] · [RECEIPTS][receipts-readme] · [PUBLISHED][published-readme] · [PROOFS][proofs-readme] · local [Registry Schemas][registry-schemas-readme] · catalog [Catalog][catalog-readme] · [DCAT][catalog-dcat-readme] · [STAC][catalog-stac-readme] · [PROV][catalog-prov-readme] · shared [Contracts][contracts-readme] · [Contract Vocabulary][contracts-vocab-readme] · [Schemas][schemas-readme] · [Schemas / Contracts][schemas-contracts-readme] · [Standards][docs-standards-readme] · [Tests][tests-readme] · [Tests / Contracts][tests-contracts-readme] · [Policy][policy-readme] · [Tools][tools-readme] · [Docs][docs-readme] · [Workflows][workflows-readme] · [CODEOWNERS][codeowners] · [PR template][pr-template]

> [!IMPORTANT]
> Current public `main` confirms that `data/registry/` currently contains `README.md` and `schemas/README.md` only.  
> The same public tree also confirms the broader sibling lifecycle lanes around it: `raw/`, `work/`, `quarantine/`, `processed/`, `catalog/`, `receipts/`, `published/`, and `proofs/`. Catalog child README surfaces are visible for `dcat/`, `stac/`, and `prov/`.

> [!NOTE]
> The adjacent contract and schema story is now stronger — and more split — than an older “README-only everywhere” reading allowed. Current public `main` shows a shared vocabulary lane under `contracts/vocab/`, a live parent `schemas/` subtree, and a machine-file-bearing `schemas/contracts/` scaffold, but those same README surfaces explicitly stop short of declaring canonical registry-schema authority settled.

> [!CAUTION]
> Treat dataset entry inventories, concrete schema bodies under `data/registry/schemas/`, runnable validators, emitted receipt/proof artifacts, and merge-blocking workflow YAML as **PROPOSED**, **UNKNOWN**, or **NEEDS VERIFICATION** until the active branch proves them.

## Scope
`data/registry/` is the KFM lane where source admission becomes reviewable before publication work begins.

In current KFM doctrine, this lane belongs to the **source / admission plane**. That means work should begin with a named source or dataset, a visible rights posture, cadence, support, spatial/time semantics, and QA expectations — not with an informal download or an unexplained blob dropped into storage.

In practical terms, this directory should capture the stable identity and governance posture of a dataset or source family: what it is, who publishes it, how it is acquired, what rights or restrictions apply, what cadence is expected, what default policy label or review posture applies, and which downstream lifecycle and catalog surfaces it is meant to feed.

It is **not** a data lake, a runtime database, or a place to drop raw downloads “for now.” Registry material should stay small, explicit, diffable, and PR-reviewable.

### Truth labels used here

| Label | Meaning in this README |
|---|---|
| **CONFIRMED** | Directly supported by current public repo evidence or stable March–April 2026 KFM doctrine |
| **INFERRED** | Strongly suggested by adjacent repo docs or continuity artifacts, but not freshly proven from a mounted local checkout in this session |
| **PROPOSED** | Doctrine-consistent target shape or working rule that fits KFM but is not yet proven as current branch reality |
| **NEEDS VERIFICATION** | A path, owner, schema-home choice, command, or implementation detail that should be checked before merge |
| **UNKNOWN** | Not supported strongly enough in this session to present as current repo fact |

### Current evidence boundary

| Signal | Current reading |
|---|---|
| Public repo tree | **CONFIRMED:** `data/registry/README.md` exists and `data/registry/` currently shows `README.md` plus `schemas/README.md` |
| Parent `data/` lifecycle tree | **CONFIRMED:** current public `main` shows sibling lanes for `raw/`, `work/`, `quarantine/`, `processed/`, `catalog/`, `receipts/`, `published/`, and `proofs/` |
| Current repo neighbors | **CONFIRMED:** public `main` now exposes registry-adjacent README surfaces including `data/README.md`, `data/catalog/README.md`, `contracts/README.md`, `contracts/vocab/README.md`, `schemas/README.md`, `schemas/contracts/README.md`, `docs/standards/README.md`, `tests/contracts/README.md`, `.github/workflows/README.md`, `.github/CODEOWNERS`, and `.github/PULL_REQUEST_TEMPLATE.md` |
| Owner routing | **CONFIRMED:** current public `.github/CODEOWNERS` routes `/data/` to `@bartytime4life` |
| Strong doctrine | **CONFIRMED:** KFM treats source onboarding as contract-bearing, fixes the governed truth path as `Source edge -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG -> PUBLISHED`, and increasingly centers proof-bearing objects such as `SourceDescriptor`, `CatalogClosure`, `EvidenceBundle`, `RuntimeResponseEnvelope`, `spec_hash`, `run_receipt`, and `ai_receipt` |
| Not proven here | **NEEDS VERIFICATION:** current dataset entry inventory, active local schema files below `data/registry/schemas/`, mounted validator entrypoints, workflow YAML enforcement depth, exact emitted receipt/proof packs, and the final authoritative home for registry-entry schemas |

[Back to top](#data-registry)

## Repo fit
`data/registry/` sits at the seam between **source onboarding** and the broader **truth path**.

It should describe what KFM intends to integrate and under what governance, while sibling lifecycle zones and downstream services prove acquisition, transformation, catalog closure, evidence resolution, receipt memory, release evidence, and public-safe release.

| Relation | Path / surface | Status here | Why it matters |
|---|---|---|---|
| Parent | [Data README][data-readme] | **CONFIRMED** | `data/` defines the governed lifecycle surface and already points to the registry lane |
| Sibling lifecycle lanes | [RAW][raw-readme] · [WORK][work-readme] · [QUARANTINE][quarantine-readme] · [PROCESSED][processed-readme] · [RECEIPTS][receipts-readme] · [PUBLISHED][published-readme] · [PROOFS][proofs-readme] | **CONFIRMED** | Registry should hand work off into these lanes rather than silently absorbing raw capture, transform work, release evidence, or publication responsibilities |
| Local | [Registry Schemas][registry-schemas-readme] | **CONFIRMED** | Registry-local schema boundary exists publicly, but the subtree is still README-first today |
| Catalog parent | [Catalog][catalog-readme] | **CONFIRMED** | Registry entries should prepare for outward catalog closure, not stop at admission |
| Catalog child lanes | [DCAT][catalog-dcat-readme] · [STAC][catalog-stac-readme] · [PROV][catalog-prov-readme] | **CONFIRMED** | Registry handoff should anticipate dataset discovery, asset description, and provenance traceability together |
| Shared machine contract lane | [Contracts][contracts-readme] | **CONFIRMED** | Root `contracts/` still presents itself as KFM’s canonical contract lane for shared schemas, proof objects, and contract-first release rules |
| Shared vocabulary lane | [Contract Vocabulary][contracts-vocab-readme] | **CONFIRMED** | Current public `main` now exposes a shared vocabulary lane for contract-shared term families; registry-local vocab files should not be assumed by default anymore |
| Top-level schema boundary | [Schemas][schemas-readme] | **CONFIRMED** | `schemas/` is now a live parent subtree, but its own README explicitly says visible machine files do **not** settle canonical schema-home authority |
| Live schema-contract subtree | [Schemas / Contracts][schemas-contracts-readme] | **CONFIRMED** | Current public `main` now exposes a machine-file-bearing `schemas/contracts/` scaffold, which sharpens the authority question rather than resolving it |
| Standards routing lane | [Standards][docs-standards-readme] | **CONFIRMED** | Current standards docs route cross-cutting profiles and point into both `contracts/` and `schemas/contracts/`; registry docs should not flatten that split into a false certainty |
| Shared policy lane | [Policy][policy-readme] | **CONFIRMED** | Default-deny, reasons/obligations, and finite outcomes should shape registry review and downstream access |
| Verification lanes | [Tests][tests-readme] · [Tests / Contracts][tests-contracts-readme] | **CONFIRMED** | Registry contracts should eventually be exercised by valid examples, invalid fixtures, and negative-path checks |
| Tooling lane | [Tools][tools-readme] | **CONFIRMED** | Validators, diff helpers, catalog QA, and attestation helpers belong there rather than inside registry entries |
| Workflow lane | [Workflows][workflows-readme] | **CONFIRMED** | Current public workflow lane is still `README.md`-only, so enforcement claims remain target-state until checked-in YAML proves them |
| PR review template | [PR template][pr-template] | **CONFIRMED** | Current checked-in review template explicitly requires truth labels and calls out data / source onboarding / catalog impact |
| Owner routing | [CODEOWNERS][codeowners] | **CONFIRMED** | Current public owner routing assigns `/data/` to `@bartytime4life`, making the owner line here traceable |
| Downstream consumers | governed APIs, evidence resolution, catalog builders, release proof packs | **PROPOSED** | Registry entries should feed these surfaces, not replace them |

### Working interpretation
A good `data/registry/` README now has five jobs at once:

1. make the current public `data/registry/` subtree legible without exaggerating maturity,
2. place registry work accurately inside the broader `data/` lifecycle already visible on public `main`,
3. define what a source or dataset registration surface is responsible for,
4. keep the split contract / schema / vocabulary story visible instead of silently choosing a winner, and
5. prevent drift between registry-local notes, shared contracts, policy, tests, workflows, and the governed runtime.

[Back to top](#data-registry)

## Accepted inputs
The following belong in `data/registry/` or in immediately adjacent registry-owned subpaths when the repo chooses to grow them.

| Belongs here | Why it belongs here | Current posture |
|---|---|---|
| Registry README and boundary notes | The lane exists publicly today and needs an explicit operating contract | **CONFIRMED** |
| One file per dataset or source registration entry | Small, reviewable identity and governance records are the core purpose of the registry lane | **PROPOSED** |
| Registry-local schema notes or entry schemas | Useful only if the repo explicitly assigns local authority here instead of a shared contract or `schemas/contracts/` home | **NEEDS VERIFICATION** |
| Tiny valid/invalid fixtures for registry-entry validation | Keep onboarding reviewable and fail-closed once validators exist | **PROPOSED** |
| Cross-links to shared vocabulary families | Useful when fields such as source role, cadence class, knowledge character, or policy posture need stable machine-readable terms | **CONFIRMED adjacent lane / PROPOSED local consumption** |
| Cross-links to pipeline spec, connector contract, or downstream catalog targets | Registry entries should point to the governed path they expect to feed | **PROPOSED** |
| Cross-links to sibling lifecycle lanes | Keeps admission records resolvable into `RAW`, `WORK`, `PROCESSED`, `RECEIPTS`, `PROOFS`, and `PUBLISHED` without duplicating those lanes | **INFERRED / PROPOSED** |
| Steward notes and governance flags tied directly to a dataset entry | Rights, sensitivity, escalation, and release posture belong close to admission records | **PROPOSED** |

### Minimum intent for a registry entry
A registry entry should be able to answer these questions without requiring a reviewer to reverse-engineer the whole system:

- What is this dataset or source called in KFM?
- Which **source role** or equivalent governed intake character does it carry?
- Who publishes or controls it?
- How is it acquired?
- What formats, CRS / time semantics, and cadence are expected?
- What rights or restrictions apply?
- What default policy label or review-needed posture applies before promotion?
- What canonical spec or connector definition will eventually drive version identity?
- Where should processed versions, catalog closure, receipt memory, and release evidence land downstream?

### Admission minimums from current doctrine
Current KFM doctrine is increasingly explicit that admission should start with a small but durable contract.

| Admission signal | Why it should be visible before fetch | Current posture |
|---|---|---|
| Source role or equivalent intake classification | Prevents direct observation, statutory record, discovery mirror, modeled product, and documentary evidence from collapsing into one vague “source” bucket | **CONFIRMED concept / NEEDS VERIFICATION exact field name** |
| Rights posture | Publication should fail closed when rights are missing or ambiguous | **CONFIRMED doctrine** |
| Cadence / freshness basis | Supports replay, staleness reasoning, and downstream planning | **CONFIRMED doctrine** |
| CRS / time semantics expectations | Makes normalization and validator scope inspectable up front | **CONFIRMED doctrine / PROPOSED entry fielding** |
| Validation plan | Stops “we’ll check later” from becoming the normal onboarding path | **CONFIRMED doctrine / PROPOSED local shape** |
| Publication intent | Keeps intake separate from public release, derived delivery, and review state | **CONFIRMED doctrine** |

[Back to top](#data-registry)

## Exclusions
The registry lane should stay focused. The following do **not** belong here as authoritative storage or control surfaces.

| Exclusion | Goes instead | Why |
|---|---|---|
| Raw downloads, acquisition snapshots, and checksum manifests | [RAW][raw-readme] | Registry records describe admission; they are not the captured bytes |
| Work outputs, QA scratch files, redaction experiments, or temporary joins | [WORK][work-readme] or [QUARANTINE][quarantine-readme] | Reviewable transformation and blocked state belong in lifecycle zones, not registry definitions |
| Canonical processed artifacts and published dataset versions | [PROCESSED][processed-readme] and [PUBLISHED][published-readme] | Registry entries should point to governed outputs, not become them |
| Run receipts, validation reports, or replay memory | [RECEIPTS][receipts-readme] | Process memory belongs in the receipt lane, not in admission records |
| Release proof packs, attestations, rollback packs, or correction-release evidence | [PROOFS][proofs-readme] | Promotion evidence should stay separate, reviewable, and linkable |
| DCAT, STAC, and PROV closure artifacts | [Catalog][catalog-readme] and its child lanes | Catalog triplet records are boundary artifacts of releasable scope |
| Executable policy bundles, deny rules, and decision tests | [Policy][policy-readme] | Policy should remain separately reviewable and executable |
| Shared trust-bearing schema families duplicated locally | [Contracts][contracts-readme] and/or [Schemas / Contracts][schemas-contracts-readme] | Parallel authority is drift, not resilience |
| Shared vocabulary registries duplicated locally | [Contract Vocabulary][contracts-vocab-readme] or the repo’s decided shared home | Contract-shared vocabulary should not fork by convenience inside one lane |
| Runtime API handlers, UI payloads, or evidence resolvers | `../../apps/` or `../../packages/` | Registry is admission and identity, not runtime behavior |
| Secrets, tokens, signed URLs, or sensitive acquisition credentials | protected config or secret-management surfaces | Public repo docs must not become secret-handling channels |
| Free-text policy labels, rights buckets, or acquisition methods that bypass controlled vocabularies | one canonical shared vocabulary home | Governance becomes untestable when field values drift into prose |

> [!WARNING]
> The most likely failure mode here is **parallel authority**: a registry-local schema or vocabulary quietly drifting away from the shared contract, schema, or policy lanes.  
> Current public `main` now makes that risk more visible, not less, because the repo exposes both shared vocabulary guidance and a live schema-contract subtree without fully resolving canonical authority.

[Back to top](#data-registry)

## Directory tree

### Current verified local snapshot

```text
data/registry/
├── README.md
└── schemas/
    └── README.md
```

### Confirmed parent-lifecycle context

```text
data/
├── README.md
├── raw/
│   └── README.md
├── work/
│   └── README.md
├── quarantine/
│   └── README.md
├── processed/
│   └── README.md
├── catalog/
│   ├── README.md
│   ├── dcat/
│   │   └── README.md
│   ├── stac/
│   │   └── README.md
│   └── prov/
│       └── README.md
├── receipts/
│   └── README.md
├── published/
│   └── README.md
├── proofs/
│   └── README.md
└── registry/
    ├── README.md
    └── schemas/
        └── README.md
```

### Doctrine-aligned target shape *(PROPOSED)*

```text
data/registry/
├── README.md
├── schemas/
│   ├── README.md
│   └── dataset_entry.schema.json        # only if registry-local schema authority is explicit
├── datasets/
│   └── <dataset_slug>.yml
├── fixtures/
│   ├── valid/
│   └── invalid/
└── examples/
    └── public_sample_dataset.yml
```

> [!NOTE]
> The target shape above is intentionally narrower than an older “local vocab by default” sketch.  
> Current public `main` already exposes a stronger shared vocabulary lane under `contracts/vocab/`, so local `data/registry/vocab/` growth should happen only if the checked-out branch explicitly justifies a registry-local authority boundary.

[Back to top](#data-registry)

## Quickstart
Start with inspection, not assumption.

```bash
# inspect the current registry lane
find data/registry -maxdepth 3 -type f | sort

# inspect the surrounding data lifecycle surface
find data -maxdepth 2 -type f -name 'README.md' | sort

# read the local, sibling, and shared boundary docs side by side
for f in \
  data/registry/README.md \
  data/registry/schemas/README.md \
  data/README.md \
  data/raw/README.md \
  data/work/README.md \
  data/quarantine/README.md \
  data/processed/README.md \
  data/receipts/README.md \
  data/published/README.md \
  data/proofs/README.md \
  data/catalog/README.md \
  data/catalog/dcat/README.md \
  data/catalog/stac/README.md \
  data/catalog/prov/README.md \
  contracts/README.md \
  contracts/vocab/README.md \
  schemas/README.md \
  schemas/contracts/README.md \
  docs/standards/README.md \
  tests/README.md \
  tests/contracts/README.md \
  policy/README.md \
  tools/README.md \
  docs/README.md \
  .github/workflows/README.md \
  .github/CODEOWNERS \
  .github/PULL_REQUEST_TEMPLATE.md
do
  test -f "$f" && { echo "===== $f"; sed -n '1,240p' "$f"; }
done

# search the repo for registry-relevant vocabulary and proof carriers
grep -RIn "dataset_entry\|source_role\|knowledge_character\|spec_hash\|policy_label\|EvidenceBundle\|run_receipt" \
  data contracts schemas docs policy tests tools .github 2>/dev/null || true
```

### Minimal review order
1. Confirm what currently exists under `data/registry/` on the active branch.
2. Confirm the broader `data/` lifecycle neighbors so registry responsibilities stay separate from `RAW`, `WORK`, `PROCESSED`, `RECEIPTS`, `PROOFS`, and `PUBLISHED`.
3. Confirm current owner routing and review expectations from `.github/CODEOWNERS` and `.github/PULL_REQUEST_TEMPLATE.md`.
4. Confirm where the authoritative registry-entry schema is supposed to live across `contracts/`, `contracts/vocab/`, `schemas/`, and `schemas/contracts/`.
5. Confirm which controlled vocabularies are already canonical versus still documentary.
6. Confirm whether any validator, fixture, or workflow gate already consumes this directory.
7. Only then add entry files, local schemas, or fixtures.

> [!TIP]
> If a new registry field requires a shared contract, vocabulary, or policy change, update the owning lane in the same change set rather than hiding the meaning inside one README or one local schema stub.

[Back to top](#data-registry)

## Usage

### Add a new registry entry safely
1. Choose a **stable** `dataset_slug` and `dataset_id`.
2. Record source role, publisher/owner, acquisition method, expected formats, expected cadence, and contact/escalation details.
3. Capture rights, redistribution posture, and the default policy label or review-needed posture.
4. Link the canonical intake/connector/pipeline spec that will eventually participate in version identity.
5. Record the intended lifecycle handoff: where raw capture, work/quarantine review, processed versions, catalog closure, receipt memory, and release evidence should land.
6. Add or update the canonical schema and fixture surfaces that prove the entry is reviewable.
7. Open a PR with evidence, review notes, and any sensitivity/redaction obligations called out explicitly.

> [!TIP]
> When a registry PR changes field meaning, contract shape, or downstream handoff semantics, use the checked-in PR template completely and keep truth labels, evidence links, and catalog-triplet impact explicit in the same change set.

### Starter registry-entry contract
Use the table below as a **minimum working contract** until the repo’s authoritative schema home is fixed and published.

| Field | Minimum posture | Why it matters |
|---|---|---|
| `dataset_slug` | Required | Stable short name for filenames, IDs, and review conversations |
| `dataset_id` | Required | Canonical KFM identifier for the dataset/source lane |
| `title` | Required | Human-readable name used in review and downstream discovery |
| `description` | Required | Explains what the dataset/source is and what it is for |
| `source_role` or equivalent controlled term | Recommended | Distinguishes direct observation, statutory record, discovery mirror, modeled product, or documentary evidence without collapsing them into one vague source class |
| `publisher` or `owner` | Required | Identifies the upstream publisher or controlling steward |
| `acquisition_method` | Required | Makes fetch/upload expectations reviewable |
| `expected_formats` | Required | Helps validate intake and downstream artifact expectations |
| `expected_cadence` or `static_snapshot` | Required | Clarifies freshness expectations and versioning posture |
| `spatial_coverage` | Required | States geography, grain, or bounds of relevance |
| `temporal_coverage` | Required | States time bounds or the absence of time semantics |
| `rights` / `license` capture | Required | Promotion should fail closed if rights are unclear |
| `default_policy_label` | Required | Establishes the first review posture before runtime filtering or release |
| `contact` / `escalation` | Required | Gives reviewers and operators a real owner path |
| `pipeline_spec_ref` or `connector_ref` | Required | Links registry identity to the governed build path that will create versioned outputs |
| `catalog_targets` | Recommended | Prevents registry work from stopping at admission without a discoverable catalog handoff |
| `receipt_targets` | Recommended | Keeps run / validation memory linkable once receipts mature as a checked-in lane |
| `proof_expectations` | Recommended | Makes promotion / rollback evidence expectations explicit even before emitters exist |
| `notes` / `governance` | Recommended | Preserves special handling, redaction duties, or steward guidance |

### Identity, versioning, and `spec_hash`
KFM’s doctrine is consistent on this point: stable dataset identity should be separate from **version identity**, and version identity should be deterministic enough to audit and rebuild.

**Working rules:**
- Keep `dataset_slug` stable, lowercase, and date-free.
- Use a stable dataset identifier family such as `kfm://dataset/<slug>`.
- Derive `dataset_version_id` from a canonical spec and its `spec_hash`, not from ephemeral runtime details.
- Include registry identity fields and transform rules that change output meaning in the hash input.
- Exclude run IDs, staging paths, and non-semantic timestamps from the hash input.
- Store the exact canonicalized spec next to the computed hash whenever the implementation lands.

**Illustrative identifier families:**

```text
kfm://dataset/<slug>
kfm://run/<run_id>
kfm://artifact/sha256:<digest>
kfm://evidence/<resolver_safe_token>
```

### Registry handoff checkpoints
Use the table below as the working handoff model. It is grounded in KFM doctrine plus the currently visible sibling lifecycle docs; exact filenames inside each downstream lane still remain **NEEDS VERIFICATION** unless the active branch proves them.

| Handoff stage | Expected sibling lane | Registry burden before handoff |
|---|---|---|
| Source-native capture | [RAW][raw-readme] | acquisition method, source URL family, expected package type, rights snapshot expectations |
| Blocked or unclear intake | [QUARANTINE][quarantine-readme] | policy label, sensitivity flags, uncertainty notes, escalation path |
| Working transform | [WORK][work-readme] | connector/pipeline reference, expected QA steps, known transform caveats |
| Stable dataset version | [PROCESSED][processed-readme] | version rule, `spec_hash` inputs, expected format family, version-pack expectations |
| Catalog closure | [DCAT][catalog-dcat-readme] · [STAC][catalog-stac-readme] · [PROV][catalog-prov-readme] | outward discovery, asset description, and provenance targets named up front |
| Process memory | [RECEIPTS][receipts-readme] | run / validation / replay memory should be referenceable once those objects exist |
| Release evidence | [PROOFS][proofs-readme] | promotion, attestation, rollback, and correction-proof expectations stay visible |
| Materialized release scope | [PUBLISHED][published-readme] | no direct publish until policy, review, release evidence, and catalog closure all resolve |

[Back to top](#data-registry)

## Diagram

```mermaid
flowchart LR
    R[Registry entry<br/>dataset_id, rights, cadence, source_role] --> S[Connector or intake spec]
    V[Shared vocabulary<br/>contracts/vocab/] -. constrains .-> R
    SH[Shared contract / schema lanes<br/>contracts/ + schemas/contracts/] -. validates .-> R
    S --> H[spec_hash<br/>version identity]
    H --> RAW[RAW capture<br/>manifest + checksums]
    RAW --> W[WORK / QUARANTINE<br/>QA, redaction, fixes]
    W --> P[PROCESSED<br/>immutable dataset version]
    P --> C[CATALOG closure<br/>DCAT + STAC + PROV]
    P --> REC[RECEIPTS<br/>run + validation memory]
    C --> PRF[PROOFS<br/>release evidence]
    PRF --> PUB[PUBLISHED<br/>release-backed scope]
    C --> E[Evidence resolution<br/>EvidenceRef -> EvidenceBundle]
    E --> A[Governed API]
    A --> U[Map / Story / Focus]
    POL[Policy + review gates] -. admission and promotion .-> R
    POL -. release readiness .-> C
    POL -. publishability .-> PRF
```

This is the operating intent: registry work should start the governed path, not replace it, and shared vocabulary / contract lanes should constrain the local registry surface rather than quietly duplicating it.

[Back to top](#data-registry)

## Tables

### Admission and promotion gates that matter to the registry lane

| Gate | Minimum proof | Registry implication | Block if |
|---|---|---|---|
| A — Identity and versioning | stable `dataset_id`, version rule, `spec_hash`, naming discipline | Registry entries must not allow unstable or duplicate identity | identity is missing, duplicated, or semantically unstable |
| B — Rights and license clarity | explicit license/rights basis, source-terms capture, obligations | Registry entry must make rights posture reviewable before promotion | rights are missing, unclear, or incompatible |
| C — Sensitivity and redaction | classification, default policy label, redaction/generalization plan when needed | Registry entry must surface whether review stops, narrows, or generalizes output | sensitivity is unresolved or no handling plan exists |
| D — Catalog triplet validity | `DCAT + STAC + PROV` generated, valid, and cross-linked | Registry should point toward catalog closure instead of stopping at admission | catalog closure is missing or inconsistent |
| E — Run receipt and checksums | acquisition manifest, run receipt, output digests | Registry should tie identity to replayable build memory | lineage cannot be reconstructed |
| F — Policy and contract tests | schema, policy, link, and negative-path checks pass | Registry entry must be exercisable by validation, not prose-only | any blocking validation or policy failure remains |
| G — Operational readiness | owner, rollback path, monitoring/review posture | Registry should not feed public release lanes without named responsibility | owner, rollback, or support posture is missing |

### Authority split to retire explicitly

| Concern | Current confirmed signal | Working rule until the repo decides |
|---|---|---|
| Shared human-readable contract route | [Contracts][contracts-readme] still presents root `contracts/` as the canonical contract lane for shared schemas, proof objects, and contract-first release rules | Treat shared registry-entry semantics as belonging to one canonical shared contract story, not to whichever directory is easiest to edit |
| Shared vocabulary route | [Contract Vocabulary][contracts-vocab-readme] now exists publicly and treats contract-shared vocabularies as a first-class lane | Prefer one shared vocabulary home for contract-shared enums and taxonomies; do not assume registry-local vocab by default |
| Top-level schema boundary | [Schemas][schemas-readme] now confirms a live nested subtree and still says machine-file presence does **not** settle canonical authority | Keep the parent schema lane as an authority-warning surface until the repo writes the decision down explicitly |
| Live schema-contract subtree | [Schemas / Contracts][schemas-contracts-readme] now shows a machine-file-bearing `v1/` and `vocab/` scaffold | File presence here is real, but should not silently promote this lane into canonical law without an explicit boundary decision |
| Registry-local schema lane | [Registry Schemas][registry-schemas-readme] exists publicly but remains README-only today | Add local schema files only with an explicit ownership note or ADR |
| Standards routing | [Standards][docs-standards-readme] now references both `contracts/` and `schemas/contracts/` as adjacent governed areas | Registry docs should reflect the split honestly instead of pretending the standards lane already chose one winner |
| Contract-facing verification | [Tests / Contracts][tests-contracts-readme] now exists as a visible verification family | Keep fixtures and validation responsibilities in sync with whichever contract home ends up canonical |
| Review burden | [PR template][pr-template] requires explicit truth labels, evidence links, and data / source onboarding / catalog impact disclosure | Registry changes should use that burden instead of burying uncertainty in prose |
| Workflow enforcement | [Workflows][workflows-readme] still documents public `.github/workflows/` as README-only on current `main` | Do not claim merge-blocking validator enforcement until checked-in YAML and entrypoints prove it |

[Back to top](#data-registry)

## Task list & definition of done

### Definition of done for this README
- [ ] KFM Meta Block v2 is present, and unresolved identifiers or policy labels remain honestly marked.
- [ ] Current public-tree fact for `data/registry/` is clearly separated from the broader confirmed `data/` lifecycle context.
- [ ] Upstream, sibling, and downstream links resolve relative to `data/registry/README.md`.
- [ ] Lifecycle neighbor links reflect the public `raw/`, `work/`, `quarantine/`, `processed/`, `receipts/`, `published/`, and `proofs/` doc surfaces.
- [ ] Catalog child-lane links reflect the public `dcat/`, `stac/`, and `prov/` README surfaces.
- [ ] Shared vocabulary and live schema-contract split are made explicit instead of implying registry-local vocab by default.
- [ ] Schema-home ambiguity is made explicit instead of glossed over.
- [ ] No sentence implies live CI gates, validators, fixtures, or emitted registry payloads unless they are branch-confirmed.
- [ ] Commands are either verified shell inspection steps or clearly marked illustrative.
- [ ] PR-template truth/evidence burden stays aligned with this README.
- [ ] Long-form reference material stays in the appendix, not in the scanning path.

### Definition of done for a registry-entry PR
- [ ] The entry validates against the **canonical** schema home.
- [ ] Rights/license posture is explicit and reviewable.
- [ ] Default policy label or review-needed posture is recorded.
- [ ] Source owner/publisher and escalation contact are named.
- [ ] Source role or equivalent intake classification is explicit when the schema supports it.
- [ ] Canonical pipeline/connector spec reference is present.
- [ ] Planned lifecycle handoff is named across processed / catalog / receipts / proofs / publication as needed.
- [ ] Any sensitivity or redaction obligations are stated explicitly.
- [ ] At least one validation path, fixture, or downstream proof obligation is referenced.
- [ ] Catalog-triplet impact (`DCAT / STAC / PROV` or equivalent) is called out explicitly in the PR when it changes.
- [ ] The PR keeps `CONFIRMED`, `INFERRED`, `PROPOSED`, and `NEEDS VERIFICATION` claims honest.

[Back to top](#data-registry)

## FAQ

### Does current public `main` already expose dataset entry files here?
No. Current public `main` shows `data/registry/` with `README.md` and `schemas/README.md` only.

### Does current public `main` now expose broader lifecycle docs next to registry?
Yes. Public `main` now exposes README surfaces for `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/receipts/`, `data/published/`, and `data/proofs/`. That widens the confirmed context around the registry lane without changing the fact that the registry subtree itself is still small.

### Should registry-entry schemas live in `data/registry/schemas/`?
Not automatically. Current public `main` shows the local scaffold, but it also shows a stronger shared contract / schema split across `contracts/`, `contracts/vocab/`, `schemas/`, and `schemas/contracts/`. Treat local schema placement as **NEEDS VERIFICATION** until the repo makes authority explicit.

### Do shared vocabularies now have a stronger public home?
Yes. Current public `main` now exposes `contracts/vocab/README.md` as a dedicated shared vocabulary lane. That is a stronger signal than an older “just add a local registry vocab directory” instinct, but it still does not fully settle every field family or enum owner.

### Does current public `main` show machine-file scaffolds under `schemas/contracts/`?
Yes. Current public `main` now shows a live `schemas/contracts/` subtree with `v1/` and `vocab/` scaffolds. That confirms machine-file presence, not canonical authority.

### Does this directory store datasets?
No. The registry lane should store **registration records and boundary guidance**, not the raw or processed dataset payloads themselves.

### Is a registry entry the same thing as a published dataset version?
No. A registry entry is an admission and identity artifact. Publication still depends on acquisition, QA, processed outputs, catalog closure, policy/review, receipts, proofs, and release-backed publication state.

### Can the UI or API read registry files directly?
Not as a trust shortcut. Runtime claim surfaces should still go through governed APIs, policy mediation, catalog closure, and evidence resolution.

### What should happen when rights or sensitivity are unclear?
Fail closed. Keep the work out of release surfaces until the rights posture and required handling plan are explicit.

[Back to top](#data-registry)

## Appendix

<details>
<summary><strong>Illustrative starter registry entry (example only — adapt field names to the canonical schema home before commit)</strong></summary>

```yaml
dataset_slug: ks_census_1870_population
dataset_id: kfm://dataset/ks_census_1870_population
title: Kansas 1870 Census Population by County
description: County-level population counts for Kansas from the 1870 census.
source_role: administrative_record # illustrative token; verify canonical enum + owner
publisher: IPUMS NHGIS
acquisition_method: bulk_download
expected_formats:
  - csv
  - parquet
expected_cadence: static_snapshot
spatial_coverage:
  grain: county
  area: Kansas
temporal_coverage:
  start: 1870-01-01
  end: 1870-12-31
rights:
  license: US-PD
  rights_holder: IPUMS NHGIS
  attribution: IPUMS NHGIS / source publication
default_policy_label: public
contact:
  steward: TODO-VERIFY
  escalation: TODO-VERIFY
pipeline_spec_ref: <VERIFY-CANONICAL-SCHEMA-HOME-AND-PATH>
catalog_targets:
  dcat: <VERIFY>
  stac_collection: <VERIFY>
  prov: <VERIFY>
receipt_targets:
  run_receipt: <VERIFY>
proof_expectations:
  release_manifest: <VERIFY>
  proof_pack: <VERIFY>
notes:
  - Example only; keep field names aligned to the canonical registry-entry schema.
  - Do not commit unresolved rights or sensitivity as if they were public-safe facts.
```

### Quick reviewer prompts
- Does the entry describe a **source or dataset lane**, not a runtime payload?
- Are source role, rights, cadence, and policy posture explicit?
- Is the version-identity path (`spec_hash` / canonical spec) understandable?
- Does the entry point toward processed scope, catalog closure, receipt memory, and release evidence rather than stopping at acquisition?
- Would a steward know who to contact if something is wrong?

</details>

[Back to top](#data-registry)

[data-readme]: ../README.md
[raw-readme]: ../raw/README.md
[work-readme]: ../work/README.md
[quarantine-readme]: ../quarantine/README.md
[processed-readme]: ../processed/README.md
[receipts-readme]: ../receipts/README.md
[published-readme]: ../published/README.md
[proofs-readme]: ../proofs/README.md
[registry-schemas-readme]: ./schemas/README.md
[catalog-readme]: ../catalog/README.md
[catalog-dcat-readme]: ../catalog/dcat/README.md
[catalog-stac-readme]: ../catalog/stac/README.md
[catalog-prov-readme]: ../catalog/prov/README.md
[contracts-readme]: ../../contracts/README.md
[contracts-vocab-readme]: ../../contracts/vocab/README.md
[schemas-readme]: ../../schemas/README.md
[schemas-contracts-readme]: ../../schemas/contracts/README.md
[docs-standards-readme]: ../../docs/standards/README.md
[tests-readme]: ../../tests/README.md
[tests-contracts-readme]: ../../tests/contracts/README.md
[policy-readme]: ../../policy/README.md
[tools-readme]: ../../tools/README.md
[docs-readme]: ../../docs/README.md
[workflows-readme]: ../../.github/workflows/README.md
[codeowners]: ../../.github/CODEOWNERS
[pr-template]: ../../.github/PULL_REQUEST_TEMPLATE.md