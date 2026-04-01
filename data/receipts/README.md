<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS_VERIFICATION_UUID>
title: receipts
type: standard
version: v1
status: draft
owners: @bartytime4life
created: <NEEDS_VERIFICATION_CREATED_DATE>
updated: <NEEDS_VERIFICATION_UPDATED_DATE>
policy_label: <NEEDS_VERIFICATION_POLICY_LABEL>
related: [data/README.md, data/raw/README.md, data/work/README.md, data/quarantine/README.md, data/processed/README.md, data/catalog/README.md, data/published/README.md, data/proofs/README.md, data/registry/README.md, contracts/README.md, schemas/README.md, policy/README.md, tests/README.md, .github/workflows/README.md, .github/CODEOWNERS, .github/PULL_REQUEST_TEMPLATE.md]
tags: [kfm, data, receipts]
notes: [owner confirmed from public CODEOWNERS; doc_id/dates/policy_label need verification; public main confirms data/receipts/ is README-only at the directory level; adjacent lifecycle README surfaces are visible on public main]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# receipts

Audit-facing process-memory surface for run receipts, validation reports, and replay/correction-ready evidence links in KFM.

> **Status:** experimental  
> **Doc state:** draft  
> **Owners:** `@bartytime4life`  
> **Path:** [`data/receipts/README.md`](./README.md)  
> **Repo fit:** inside [`../README.md`](../README.md); lifecycle neighbors in [`../raw/README.md`](../raw/README.md), [`../work/README.md`](../work/README.md), [`../quarantine/README.md`](../quarantine/README.md), [`../processed/README.md`](../processed/README.md), [`../catalog/README.md`](../catalog/README.md), [`../published/README.md`](../published/README.md), [`../proofs/README.md`](../proofs/README.md), and [`../registry/README.md`](../registry/README.md); shared control surfaces in [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md), [`../../policy/README.md`](../../policy/README.md), [`../../tests/README.md`](../../tests/README.md), [`../../.github/workflows/README.md`](../../.github/workflows/README.md), [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS), and [`../../.github/PULL_REQUEST_TEMPLATE.md`](../../.github/PULL_REQUEST_TEMPLATE.md)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)  
> ![status: experimental](https://img.shields.io/badge/status-experimental-6f42c1) ![owners: @bartytime4life](https://img.shields.io/badge/owners-%40bartytime4life-1f6feb) ![branch: main](https://img.shields.io/badge/branch-main-0a7d5a) ![role: process memory](https://img.shields.io/badge/role-process__memory-0a7ea4) ![proofs: separate](https://img.shields.io/badge/proofs-separate-f59e0b) ![truth: bounded](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20PROPOSED%20%7C%20UNKNOWN-2ea043)

> [!IMPORTANT]
> `data/receipts/` is a **real directory on the public `main` branch**, and current public-tree evidence still shows this directory as **`README.md`-only**.
>
> This README therefore separates:
>
> - **CONFIRMED current public-tree presence**
> - **CONFIRMED KFM doctrine about receipt/process-memory responsibilities**
> - **PROPOSED starter structure** for a fuller receipt surface
> - **UNKNOWN / NEEDS VERIFICATION** details about emitted files, validators, and merge-blocking automation

> [!NOTE]
> In KFM terms, **receipts are not proofs**.
>
> Receipts preserve process memory: ingest, run, validation, and audit-facing evidence needed for replay, correction, and release review.
> Release-significant manifests, attestations, and proof packs stay separate, typically behind release/proof surfaces.

---

## Scope

`data/receipts/` is the repo-facing surface for **queryable process memory** inside the broader KFM data lifecycle.

This is **zone-level** documentation. It defines the role, boundaries, and placement rules for receipt-shaped artifacts without pretending that all lower-level filenames, validators, or workflow emitters are already settled.

The surrounding `data/` doctrine makes three things especially clear:

1. process evidence must remain durable enough for replay, rollback, correction, and release review,
2. receipt-like artifacts may live in a central audited surface **or** in version-adjacent packs, and
3. process memory must not silently collapse into release proof, canonical authority, or public runtime truth.

### Evidence posture used here

| Marker | Meaning in this README |
|---|---|
| **CONFIRMED** | Visible on the current public branch or directly aligned with stable KFM lifecycle doctrine already expressed in neighboring repo docs |
| **PROPOSED** | Starter structure, placement rule, or naming pattern that fits doctrine but is not yet visible as current branch reality |
| **UNKNOWN / NEEDS VERIFICATION** | Any checked-out branch detail, emitted receipt inventory, exact validator wiring, or canonical schema-home decision not proven from the current public tree |

### Working rule

Use `data/receipts/` for receipt-shaped artifacts that must stay easy to resolve during:

- replay,
- correction,
- release review,
- incident reconstruction,
- audit-facing explanation.

If a lane keeps receipt packs **beside a dataset version or release**, that is still acceptable.
This README governs the **boundary** and **role** of receipt artifacts, not one mandatory storage pattern for every lane.

[Back to top](#top)

## Repo fit

`receipts/` sits inside the `data/` lifecycle surface, but it should remain visibly adjacent to sibling zone docs, shared contract/policy surfaces, and workflow/review control.

### Path and adjacent surfaces

| Relation | Surface | Status | Why it matters |
|---|---|---:|---|
| Upstream | [`../README.md`](../README.md) | **CONFIRMED** | Defines the broader `data/` lifecycle role and the receipts-vs-proofs distinction |
| Adjacent lifecycle | [`../raw/README.md`](../raw/README.md) · [`../work/README.md`](../work/README.md) · [`../quarantine/README.md`](../quarantine/README.md) · [`../processed/README.md`](../processed/README.md) · [`../catalog/README.md`](../catalog/README.md) · [`../published/README.md`](../published/README.md) · [`../proofs/README.md`](../proofs/README.md) · [`../registry/README.md`](../registry/README.md) | **CONFIRMED** | These neighboring `data/` surfaces are visible on public `main` and clarify where receipts stop and stronger/later objects begin |
| Upstream | [`../../contracts/README.md`](../../contracts/README.md) | **CONFIRMED** | Shared contract authority should stay explicit rather than reappearing ad hoc under `data/receipts/` |
| Upstream | [`../../schemas/README.md`](../../schemas/README.md) | **CONFIRMED** | Current repo docs still keep schema-home authority unresolved; this directory must not worsen that ambiguity |
| Upstream | [`../../policy/README.md`](../../policy/README.md) | **CONFIRMED** | Rights, sensitivity, deny-by-default, and obligation logic belong in executable policy surfaces |
| Downstream pressure | [`../../tests/README.md`](../../tests/README.md) | **CONFIRMED** | Tests should exercise receipt behavior, not duplicate receipt ownership |
| Control surfaces | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) · [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) · [`../../.github/PULL_REQUEST_TEMPLATE.md`](../../.github/PULL_REQUEST_TEMPLATE.md) | **CONFIRMED** | Workflow intent, ownership routing, and PR review expectations are already public control surfaces that shape this lane |

### Current verified snapshot

| Item | Status | Current meaning |
|---|---:|---|
| `data/receipts/` directory exists | **CONFIRMED** | Visible on public `main` |
| `data/receipts/README.md` exists | **CONFIRMED** | Substantive draft README is present on public `main` |
| Additional checked-in receipt files are visible in this directory | **UNKNOWN / NEEDS VERIFICATION** | Current public tree signal for this lane is still `README.md` only |
| Sibling lifecycle README surfaces under `data/` are visible | **CONFIRMED** | `raw/`, `work/`, `quarantine/`, `processed/`, `catalog/`, `published/`, `proofs/`, and `registry/` all expose public README surfaces |
| `data/catalog/` child catalog lanes are visible | **CONFIRMED** | `dcat/`, `stac/`, and `prov/` are documented as the outward catalog closure sublanes |
| Current public workflow lane is README-only | **CONFIRMED** | `.github/workflows/README.md` explicitly records README-only current-tree state on public `main` |
| Current public control-surface ownership resolves to `@bartytime4life` | **CONFIRMED** | `.github/CODEOWNERS` routes `/data/`, `/contracts/`, `/policy/`, and `/tests/` to `@bartytime4life` |
| Authoritative schema home is settled | **UNKNOWN / NEEDS VERIFICATION** | `contracts/README.md` and `schemas/README.md` still keep schema-home authority pending |

> [!CAUTION]
> Do **not** treat this directory as a stealth schema home, release-proof lane, or public runtime surface.
> Its value is in preserving process memory without confusing where stronger authority lives.

[Back to top](#top)

## Accepted inputs

The following are appropriate for `data/receipts/` when they are stored centrally rather than only version-adjacently:

| Accepted input | Why it belongs here | Typical linkage |
|---|---|---|
| Run receipts | Preserve what ran, when, with what inputs, and with what outcome | run ↔ source / subject / audit |
| Validation reports | Preserve structural, spatial, temporal, or domain QC memory | validation ↔ run / subject |
| Audit-facing process memory | Make replay, correction, and review reconstructable | audit refs ↔ decision / release review |
| Watcher or probe receipts | Preserve operational fetch/probe memory without pretending they are release proofs | watcher ↔ run / artifact / drift check |
| Redacted receipt mirrors | Keep repo-safe traceability when the full operational payload cannot be committed directly | mirror ↔ stronger internal source |
| Lightweight lookup indexes | Help grouped replay/review without becoming a second source of truth | batch ↔ receipt set |

### Minimum bar for anything added here

- It is clearly **receipt-shaped** rather than release-proof-shaped.
- It is small enough to diff and inspect.
- It links to a stronger object or decision when one exists.
- It does not create a second, quieter authority path.
- It can survive replay, correction, or release review without guesswork.

## Exclusions

The following do **not** belong here as the authoritative home:

| Exclusion | Keep it under / behind | Why |
|---|---|---|
| Shared schema files, shared vocab registries, OpenAPI fragments | [`../../contracts/README.md`](../../contracts/README.md) and any later-resolved canonical schema home | Prevents a second schema universe |
| Executable policy bundles or rule sources | [`../../policy/README.md`](../../policy/README.md) | Policy must remain independently reviewable and testable |
| Canonical processed dataset authority | [`../processed/README.md`](../processed/README.md) | Receipts should point to authority, not replace it |
| Catalog triplet closure (`DCAT + STAC + PROV`) | [`../catalog/README.md`](../catalog/README.md) | Discoverability and outward lineage closure are a different seam |
| Release manifests, proof packs, attestations, correction trace as the primary record | [`../proofs/README.md`](../proofs/README.md) and release-bearing surfaces | Proofs are release-significant, not just process memory |
| Public runtime envelopes, `EvidenceBundle` payloads, UI state payloads | governed APIs and surface-contract lanes | Runtime trust objects are downstream consumers |
| Raw source bytes or unresolved sensitive material | [`../raw/README.md`](../raw/README.md) or [`../quarantine/README.md`](../quarantine/README.md) | `receipts/` is not a bypass around rights or sensitivity handling |
| Secrets, tokens, host-local credentials, or machine-specific dumps | deployment/runtime secret handling | Auditability is not permission to leak secret material |

> [!WARNING]
> If a file here starts behaving like a release proof, a public runtime object, or a canonical schema, it is in the wrong place.

[Back to top](#top)

## Directory tree

### Current confirmed snapshot

```text
data/receipts/
└── README.md
```

### Confirmed nearby README surfaces on public `main`

```text
data/
├── README.md
├── catalog/README.md
├── processed/README.md
├── proofs/README.md
├── published/README.md
├── quarantine/README.md
├── raw/README.md
├── receipts/README.md
├── registry/README.md
└── work/README.md
```

> [!NOTE]
> The tree above is a **README-surface map**, not a full subtree inventory.
> It is included here to make the surrounding lifecycle boundaries easy to navigate in GitHub review.

### Doctrine-aligned starter shape (`PROPOSED`)

```text
data/receipts/
├── README.md
├── ingest/                 # fetch + landing receipts
├── runs/                   # transform / watcher / pipeline receipts
├── validation/             # validation reports and QC outputs
└── _lookup/                # small indexes for replay / grouped review
```

### Placement rule

Use the tree above as a **starter shape**, not as a claim that those paths already exist on the current branch.

If a lane already keeps receipt packs beside:

- a `DatasetVersion`,
- a release bundle,
- or a lane-local audited surface,

prefer **stable linking** over gratuitous duplication.

## Quickstart

### Safe inspection commands

```bash
# inspect the currently checked-in receipts surface
find data/receipts -maxdepth 4 -type f | sort

# inspect neighboring lifecycle and control docs side by side
for p in \
  data/README.md \
  data/raw/README.md \
  data/work/README.md \
  data/quarantine/README.md \
  data/processed/README.md \
  data/catalog/README.md \
  data/published/README.md \
  data/proofs/README.md \
  data/registry/README.md \
  contracts/README.md \
  schemas/README.md \
  policy/README.md \
  tests/README.md \
  .github/workflows/README.md \
  .github/CODEOWNERS \
  .github/PULL_REQUEST_TEMPLATE.md
do
  echo
  echo "== $p =="
  sed -n '1,220p' "$p" 2>/dev/null || true
done

# inspect references to receipt-shaped objects and downstream trust objects
grep -RIn \
  "IngestReceipt\|ValidationReport\|DecisionEnvelope\|ReviewRecord\|ReleaseManifest\|ReleaseProofPack\|ProjectionBuildReceipt\|EvidenceBundle\|RuntimeResponseEnvelope\|CorrectionNotice\|audit_ref\|run_id" \
  data contracts schemas policy tests docs .github 2>/dev/null || true
```

### First local review pass

1. Confirm whether the checked-out branch still matches the public tree for `data/receipts/`.
2. Confirm whether receipts are stored centrally here, version-adjacently, or as a hybrid.
3. Confirm the authoritative schema home before adding any contract-shaped files.
4. Confirm which workflow checks, if any, actually validate receipt-shaped artifacts.
5. Confirm how receipt files link forward to dataset, decision, release, and correction surfaces.
6. Confirm whether any receipt content must be redacted, linked, or split before commit.

> [!TIP]
> Inspection-first is safer than inventing a validator or path convention in README prose.
> Let the checked-out branch prove the runner, schema, and gate wiring before this file names them as fact.

## Usage

### What `data/receipts/` is

`data/receipts/` is:

- the repo-facing home for **process memory** when central receipt placement is useful,
- the place where replay, correction, and release review can find run/validation context quickly,
- a support surface for auditability,
- a bridge between lifecycle work and later trust-bearing proof or runtime surfaces.

### Placement rules

1. Prefer **diff-friendly, text-first receipt artifacts** over opaque blobs.
2. Preserve **stable join points** across run, subject, decision, release, and audit contexts.
3. Link forward to stronger objects instead of duplicating them wholesale.
4. Keep receipt artifacts easy to resolve during replay, correction, and release review.
5. If a receipt pack is mirrored here from a version-adjacent lane, keep the relationship explicit.
6. When sensitive operational detail is present, commit a redacted mirror here and keep the stronger source elsewhere under policy control.

### What `data/receipts/` is not

`data/receipts/` is **not**:

- a second release lane,
- a second contract registry,
- a place to bury policy logic,
- a replacement for `processed/`, `catalog/`, or `proofs/`,
- a generic scratch folder,
- a quiet workaround for trust-membrane boundaries.

[Back to top](#top)

## Diagram

```mermaid
flowchart LR
    A[Source admission<br/>SourceDescriptor] --> B[RAW<br/>immutable capture]
    B --> C[WORK / QUARANTINE<br/>normalize, validate, hold]
    C --> D[data/receipts/<br/>run receipts + validation reports]
    C --> E[PROCESSED<br/>DatasetVersion]
    E --> F[CATALOG<br/>DCAT + STAC + PROV]
    F --> G[PUBLISHED<br/>release-backed scope]
    G --> H[PROOFS<br/>ReleaseManifest + ReleaseProofPack]
    G --> I[Runtime / trust surfaces<br/>EvidenceBundle drill-through]

    D -. replay / correction / review memory .-> E
    D -. audit context .-> H
```

## Tables

### Receipt boundary map

| Object family | Normal home | Keep in `data/receipts/`? | Why |
|---|---|---:|---|
| `IngestReceipt` | RAW-adjacent or central audited receipt surface | **Sometimes** | Centralization is acceptable if replay remains easy |
| `ValidationReport` | WORK / QUARANTINE or central audited receipt surface | **Yes** | Core process memory |
| Run / watcher / pipeline receipt | Central or lane-adjacent receipt surface | **Yes** | Operational history should stay queryable |
| `DatasetVersion` | `processed/` | **No** | Canonical authority belongs elsewhere |
| `CatalogClosure` | `catalog/` | **No** | Outward metadata closure is a distinct seam |
| `ReleaseManifest` / `ReleaseProofPack` | `proofs/` or release bundle | **No** | Release-significant proof is not just process memory |
| `EvidenceBundle` | runtime / evidence surface | **No** | Inspectable claim support is downstream of receipts |
| `CorrectionNotice` | release / published lineage surface | **No** | Public correction memory must remain visible as correction, not just as a receipt |

### Minimum linkage expectations (`PROPOSED starter rule`)

| Link target | Why it matters |
|---|---|
| source or admission reference | reconstruct what the run or validation event touched |
| subject reference | identify the dataset, feature family, or batch under review |
| decision / review reference | explain why something was allowed, held, generalized, or denied |
| release reference | connect process memory forward to the publishable unit when one exists |
| audit reference | support review, incident reconstruction, or external explanation |

## Task list

- [ ] Replace remaining meta-block placeholders for `doc_id`, dates, and `policy_label`.
- [ ] Confirm whether `data/receipts/` remains central, version-adjacent, or hybrid on the checked-out branch.
- [ ] Confirm the authoritative schema home before adding any schema-like files here.
- [ ] Add at least one real emitted receipt example once the branch exposes it.
- [ ] Add one real linked validation-report example once visible.
- [ ] Verify all relative links against the checked-out branch.
- [ ] Name the first actual validator or workflow path only after it is visible and reviewable.
- [ ] Confirm that receipt artifacts link cleanly into dataset, decision, release, and correction review paths.

### Definition of done

This README is in a healthy state when:

- it describes the **real current branch** more strongly than it describes hopeful future structure,
- it keeps **receipts**, **proofs**, **contracts**, and **runtime trust objects** visibly distinct,
- it gives contributors a clear place to put receipt-shaped artifacts without creating a second authority path.

[Back to top](#top)

## FAQ

### Is `data/receipts/` different from `data/proofs/`?

Yes.

Receipts preserve process memory such as run receipts, validation reports, and audit-ready context.
Proofs preserve release-significant evidence such as manifests, attestations, and correction-ready release trace.

### Can a dataset version keep its own receipt pack outside this directory?

Yes.

The surrounding `data/` guidance already allows `data/receipts/` **or** a version-adjacent audited surface.
What matters is not one mandatory path; what matters is that replay, correction, and release review stay easy.

### Should schemas or policy bundles live here?

No.

This directory may **consume** or **link to** contracts and policy, but it should not quietly become the canonical home for either.

### Can this directory contain protected material?

Only when policy explicitly allows it.

When a receipt contains operational or sensitive detail that should not live in the repo unchanged, prefer a redacted mirror here plus a stronger linked source elsewhere.

## Appendix

<details>
<summary><strong>Illustrative starter conventions</strong> (<code>PROPOSED</code>)</summary>

### Filename pattern ideas

```text
data/receipts/<lane-or-source>/<yyyy-mm-dd>/<receipt-id>.json
data/receipts/<lane-or-source>/<yyyy-mm-dd>/<validation-report-id>.json
```

### Illustrative JSON shape

> [!NOTE]
> This is an illustrative shape only.
> Use the authoritative contract home when the repo resolves it.

```jsonc
{
  "kind": "<RunReceipt|ValidationReport>",
  "schema_version": "<NEEDS_VERIFICATION>",
  "receipt_id": "<stable-id>",
  "created_at": "<RFC3339 timestamp>",
  "refs": {
    "source": "<source-or-admission-ref>",
    "subject": "<optional dataset-or-batch-ref>",
    "decision": "<optional decision-ref>",
    "release": "<optional release-ref>",
    "audit": "<optional audit-ref>"
  },
  "inputs": [],
  "outputs": [],
  "integrity": [],
  "notes": []
}
```

### Small naming rules worth preserving

- Prefer sortable, stable IDs.
- Keep filenames lowercase and diff-friendly.
- Use explicit timestamps instead of ambiguous local date strings.
- Link forward to stronger authority rather than copying large objects into receipts.

</details>

[Back to top](#top)
