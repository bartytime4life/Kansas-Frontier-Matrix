# hydrology

Public-safe, non-authoritative hydrology thin-slice examples for Kansas Frontier Matrix.

> **Status:** Experimental  
> **Owners:** `@bartytime4life`  
> ![status](https://img.shields.io/badge/status-experimental-orange) ![surface](https://img.shields.io/badge/surface-examples%2Fthin__slice%2Fhydrology-blue) ![trust](https://img.shields.io/badge/trust-non--authoritative-lightgrey) ![slice](https://img.shields.io/badge/slice-hydrology--first-0a7ea4)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list / definition of done](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)  
> **Repo fit:** `examples/thin_slice/hydrology/README.md` · upstream [../README.md](../README.md) · [../../README.md](../../README.md) · [../../../README.md](../../../README.md) · stronger owner surfaces [../../../contracts/README.md](../../../contracts/README.md) · [../../../schemas/README.md](../../../schemas/README.md) · [../../../tests/README.md](../../../tests/README.md) · [../../../policy/README.md](../../../policy/README.md) · [../../../docs/standards/README.md](../../../docs/standards/README.md)

> [!IMPORTANT]
> This directory is **example space**, not canonical truth space.
>
> Use it to explain the hydrology-first thin slice with **public-safe**, **redacted**, and **illustrative** material. Do **not** let this folder become the only home of contracts, proof objects, policy fixtures, release artifacts, or live hydrology data.

> [!NOTE]
> Read statements in this file with KFM truth labels:
>
> - **CONFIRMED** — visible in the current repository branch or repeated clearly in attached KFM doctrine
> - **INFERRED** — strongly implied by adjacent repo structure or repeated doctrine, but not directly proven as mounted implementation here
> - **PROPOSED** — recommended shape for this directory if it grows beyond the current scaffold
> - **UNKNOWN** — cannot be verified from the current visible repo and attached evidence
> - **NEEDS VERIFICATION** — worth checking at merge time because repo state may have moved

---

## Scope

`examples/thin_slice/hydrology/` is the **illustrative lane** for the KFM hydrology-first thin slice.

Its job is to help contributors, reviewers, and maintainers understand what a real hydrology slice should prove end to end without pretending that this folder is the real runtime, the real publication lane, or the real proof-object registry.

In practice, that means this directory is a good place for:

- small, redacted example payloads
- screenshot or mock payload packs for trust-visible surfaces
- narrow walkthrough assets that explain how hydrology moves from source admission to evidence-backed surface behavior
- reviewer-oriented examples of honest negative outcomes such as **ABSTAIN**, **DENY**, **ERROR**, or **stale-visible**

This directory is **not** where authoritative hydrology state should live.

[Back to top](#hydrology)

---

## Repo fit

### What this directory is

A compact, repo-local place to document and demonstrate the **hydrology-first** example lane inside `examples/thin_slice/`.

### What this directory is not

Not a replacement for:

- contract ownership in [`../../../contracts/`](../../../contracts/README.md)
- schema governance in [`../../../schemas/`](../../../schemas/README.md)
- merge-blocking fixtures in [`../../../tests/`](../../../tests/README.md)
- policy bundle ownership in [`../../../policy/`](../../../policy/README.md)
- release-bearing docs and standards in [`../../../docs/`](../../../docs/standards/README.md)
- runtime behavior owned by apps, services, or governed APIs

### Repo-fit table

| Dimension | This directory | Stronger owner if material becomes authoritative |
|---|---|---|
| Role | Example lane for a hydrology thin slice | Varies by artifact family |
| Trust posture | Non-authoritative, explanatory, public-safe | Governed, machine-checked, release-bearing |
| Typical contents | Redacted payload examples, screenshots, sequence notes, negative-path examples | Schemas, fixtures, emitters, policies, proofs, release objects |
| Best audience | Contributors, reviewers, maintainers | Runtime, policy, CI, release, steward workflows |
| Update rhythm | Lightweight and review-friendly | Gate-driven and compatibility-sensitive |
| Failure risk | Documentation drift | Trust drift, release drift, policy drift |

### Why hydrology lives here at all

Hydrology is the preferred first thin slice because it is usually public-safe enough to demonstrate outwardly, but still demanding enough to exercise:

- source admission
- time semantics
- validation and quarantine behavior
- release linkage
- evidence drill-through
- bounded runtime outcomes
- correction and rollback lineage

That makes it the right **teaching lane** for `examples/thin_slice/`, even when the real implementation remains elsewhere.

[Back to top](#hydrology)

---

## Accepted inputs

This directory accepts **illustrative** material that helps explain the hydrology-first slice without claiming to be the slice itself.

Examples that belong here:

- redacted example objects showing the doctrinal artifact chain
- sample `EvidenceBundle` and `RuntimeResponseEnvelope` payloads labeled as examples
- screenshots of map, dossier, Evidence Drawer, or stale/correction states
- miniature walkthrough docs for one bounded hydrology scenario
- public-safe mock query/response pairs for Focus outcomes
- diagrams showing how hydrology passes through the governed path

Keep inputs:

- small
- reviewable in Git
- explicit about example status
- public-safe
- easy to delete or replace without destabilizing the real system

[Back to top](#hydrology)

---

## Exclusions

The following do **not** belong here.

| Do not place here | Why | Put it here instead |
|---|---|---|
| Canonical `SourceDescriptor`, `DatasetVersion`, `ReleaseManifest`, or `CorrectionNotice` objects | These are trust-bearing objects, not tutorial props | Authoritative contract/data/release owner surface |
| Merge-blocking valid/invalid fixture inventories | They should be exercised by CI, not just explained by docs | [`../../../tests/`](../../../tests/README.md) and schema/contract owner lanes |
| Real raw captures, processed hydrology datasets, or release artifacts | This folder is not a truth-path storage zone | Governed data and publication lanes |
| Policy bundles, reason/obligation registries, or review-required mappings | Policy must remain machine-readable and centralized | [`../../../policy/`](../../../policy/README.md) |
| Runtime-only DTOs or route contracts treated as source of truth | Prevents example drift from becoming API drift | [`../../../contracts/`](../../../contracts/README.md) |
| Rights-unclear, steward-only, or sensitive hydrology geometry | Example space must stay public-safe | Restricted or steward-only governed lanes |
| Duplicate schema-home material with no ownership decision | The repo already distinguishes `contracts/` and `schemas/` as stronger surfaces | Resolve ownership first, then link from here |

[Back to top](#hydrology)

---

## Directory tree

### Current verified shape

```text
examples/
└── thin_slice/
    ├── README.md
    └── hydrology/
        └── README.md
```

### PROPOSED growth shape for this folder

The structure below is illustrative only. It is a **starter pattern**, not a claim that these files already exist.

```text
examples/
└── thin_slice/
    └── hydrology/
        ├── README.md
        ├── source_descriptor.example.json
        ├── ingest_receipt.example.json
        ├── validation_report.example.json
        ├── dataset_version.example.json
        ├── catalog_closure.example.json
        ├── release_manifest.example.json
        ├── projection_build_receipt.example.json
        ├── evidence_bundle.example.json
        ├── runtime_response_envelope.answer.example.json
        ├── runtime_response_envelope.abstain.example.json
        ├── runtime_response_envelope.deny.example.json
        ├── correction_notice.example.json
        ├── query_examples.md
        └── views/
            ├── overview.md
            ├── detail.md
            └── stale_visible.md
```

### Naming rule

Prefer `*.example.json` or similarly explicit sample labels for anything illustrative in this folder.

That keeps example assets from being mistaken for authoritative artifacts with canonical filenames.

[Back to top](#hydrology)

---

## Quickstart

Use these commands when reviewing or extending this lane.

```bash
# Inspect the immediate example lane
ls -la examples/thin_slice/hydrology

# Inspect nearby README surfaces for tone, ownership, and placement
sed -n '1,240p' examples/README.md
sed -n '1,240p' examples/thin_slice/README.md
sed -n '1,260p' examples/thin_slice/hydrology/README.md

# Inspect stronger owner surfaces before adding example files
sed -n '1,240p' contracts/README.md
sed -n '1,240p' schemas/README.md
sed -n '1,240p' tests/README.md
sed -n '1,240p' policy/README.md
sed -n '1,240p' docs/standards/README.md
```

When adding new material, review the owner surface first. If the file should become merge-blocking, release-bearing, or policy-enforced, this directory is probably the wrong destination.

[Back to top](#hydrology)

---

## Usage

### 1. Start from the governed chain, not the screenshot

Any example here should point back to the hydrology-first chain, not just to a polished map.

The minimum story this directory should help a reader understand is:

1. a source is admitted
2. a fetch is receipted
3. validation can pass or quarantine
4. a stable dataset version exists before release
5. release and projection are linked
6. a visible surface drills through to evidence
7. runtime answers stay finite and honest
8. correction and rollback remain visible

### 2. Pair happy-path and negative-path examples

A trustworthy example pack should never show only the green path.

For every outward-facing example, prefer a paired negative example:

- **ANSWER** paired with **ABSTAIN**
- **released** paired with **stale-visible**
- **normal detail** paired with **generalized**
- **current** paired with **superseded** or **correction-pending**

### 3. Keep examples public-safe

Hydrology may be comparatively public-safe, but that does not erase KFM review burdens.

Keep example material:

- generalized when exact detail is unnecessary
- redacted when rights or sensitivity could be ambiguous
- explicit about observed vs modeled status
- explicit about freshness basis
- explicit about correction state

### 4. Route examples back to stronger owner surfaces

If you add an example file here, add a short note naming the stronger owner surface.

For example:

- schema-facing example → `contracts/` or the settled schema-home
- CI-facing fixture example → `tests/`
- reason/obligation example → `policy/`
- runbook or merge guidance → `docs/`
- runtime payload owned by actual service code → app/service package plus contract surface

### 5. Prefer reviewable text first

Before adding images or binaries, consider whether a compact Markdown table, JSON sample, or Mermaid flow explains the point more clearly.

If visuals are needed, pair them with text explaining:

- what is being shown
- whether it is illustrative or emitted
- what release/freshness/correction state it represents

[Back to top](#hydrology)

---

## Diagram

```mermaid
flowchart LR
    subgraph Real_Governed_Path["Real governed hydrology path"]
        A[SourceDescriptor]
        B[IngestReceipt]
        C[ValidationReport]
        D[DatasetVersion]
        E[CatalogClosure]
        F[DecisionEnvelope / ReviewRecord]
        G[ReleaseManifest / ReleaseProofPack]
        H[ProjectionBuildReceipt]
        I[EvidenceBundle]
        J[RuntimeResponseEnvelope]
        K[CorrectionNotice]
        A --> B --> C --> D --> E --> F --> G --> H --> I --> J --> K
    end

    subgraph Example_Lane["examples/thin_slice/hydrology/"]
        X[README + redacted example payloads + public-safe views]
    end

    X -. illustrates .-> A
    X -. illustrates .-> I
    X -. illustrates .-> J
    X -. illustrates .-> K
    X -. never replaces .-> G
```

The key distinction is deliberate:

- the **real governed path** emits trust-bearing objects
- this **examples lane** only documents and demonstrates those objects

[Back to top](#hydrology)

---

## Tables

### Recommended illustrative pack

| Illustrative artifact | What it demonstrates | Status in this directory | Stronger owner if hardened |
|---|---|---|---|
| `source_descriptor.example.json` | Source admission for one bounded hydrology source family | PROPOSED | Contract/schema owner |
| `ingest_receipt.example.json` | Replayable fetch receipt shape | PROPOSED | Contract/schema owner |
| `validation_report.example.json` | Pass/quarantine reasons, spatial + temporal checks | PROPOSED | Contract/schema owner |
| `dataset_version.example.json` | Stable authoritative version shape | PROPOSED | Contract/schema owner |
| `catalog_closure.example.json` | Outward metadata closure and lineage linkage | PROPOSED | Contract/schema/catalog owner |
| `release_manifest.example.json` | Release linkage and public-safe inventory concept | PROPOSED | Release/proof owner |
| `projection_build_receipt.example.json` | Derived delivery linkage back to release | PROPOSED | Derived-delivery owner |
| `evidence_bundle.example.json` | Evidence Drawer and dossier drill-through concept | PROPOSED | Evidence resolver / contract owner |
| `runtime_response_envelope.answer.example.json` | Honest ANSWER outcome | PROPOSED | Runtime contract owner |
| `runtime_response_envelope.abstain.example.json` | Honest insufficiency path | PROPOSED | Runtime contract owner |
| `runtime_response_envelope.deny.example.json` | Rights/sensitivity refusal path | PROPOSED | Runtime contract owner |
| `correction_notice.example.json` | Visible correction/supersession lineage | PROPOSED | Correction/release owner |
| `views/overview.md` | High-level map state and release/freshness explanation | PROPOSED | Example lane |
| `views/detail.md` | Evidence Drawer drill-through example | PROPOSED | Example lane |
| `views/stale_visible.md` | Stale/superseded/correction-pending visibility | PROPOSED | Example lane |

### What a genuine slice proves vs what this folder should show

| Question | Genuine governed slice | This example folder |
|---|---|---|
| Does it emit proof objects? | Yes | It may only mirror or explain them |
| Can it publish? | Potentially, if release-bearing | No |
| Can it own policy? | No, policy should be centralized | No |
| Can it host public-safe examples? | Yes | Yes |
| Can it prove correction lineage behavior? | Yes, through drills or emitted objects | It can only demonstrate what that behavior should look like |
| Can it bypass governed APIs? | No | No |

[Back to top](#hydrology)

---

## Task list / definition of done

A healthy README for this directory should make the following true.

- [ ] The file is no longer a one-line scaffold.
- [ ] The current verified tree is stated plainly before any proposed growth shape.
- [ ] Every future sample file in this directory is labeled **illustrative**, **redacted**, or **example**.
- [ ] No file here is treated as the sole authoritative source for contracts, policy, releases, or runtime behavior.
- [ ] Any added runtime examples include at least one honest negative outcome.
- [ ] Any visual examples show trust-visible state, not just the happy path.
- [ ] Any added material points to the stronger owner surface that should carry the hardened version.
- [ ] Merge-time review re-checks whether the live repo tree has changed since this README was written.

### Practical done criteria for future additions

If this folder grows beyond `README.md`, the addition should satisfy all of the following:

1. it helps explain the hydrology-first slice more clearly than a nearby README already does
2. it stays public-safe
3. it does not create a parallel schema or policy universe
4. it is obvious whether it is **CONFIRMED**, **PROPOSED**, or **illustrative only**
5. deleting it would not break the real trust path

[Back to top](#hydrology)

---

## FAQ

### Is this the real hydrology slice?

No. This is the **examples lane around the slice**, not the release-bearing slice itself.

### Why is hydrology the first thin slice?

Because it is map-native, time-aware, comparatively public-safe, and strong enough to exercise the hard seams of KFM: admission, validation, release linkage, evidence drill-through, finite runtime outcomes, and correction lineage.

### Should valid/invalid schema fixtures live here?

Only when they are clearly **instructional examples**. Merge-blocking or authoritative fixtures belong in the proper contract/schema/test owner surfaces.

### Should I use canonical artifact filenames here?

Prefer explicit example names such as `*.example.json` until the owning surface is settled and the files are meant to become authoritative.

### Can I add screenshots here?

Yes, but only if they teach something concrete: release state, freshness state, Evidence Drawer drill-through, or negative-path behavior. Decorative screenshots do not earn their keep.

[Back to top](#hydrology)

---

## Appendix

<details>
<summary><strong>Doctrinal artifact chain this lane may illustrate</strong></summary>

A future example pack in this directory should stay aligned to the hydrology-first artifact chain commonly described across the attached KFM March 2026 manuals:

1. `SourceDescriptor`
2. `IngestReceipt`
3. `ValidationReport`
4. `DatasetVersion`
5. `CatalogClosure`
6. `DecisionEnvelope`
7. `ReviewRecord` *(when required)*
8. `ReleaseManifest / ReleaseProofPack`
9. `ProjectionBuildReceipt`
10. `EvidenceBundle`
11. `RuntimeResponseEnvelope`
12. `CorrectionNotice`

A good example pack does not need to implement every owner surface, but it should not contradict this order.

</details>

<details>
<summary><strong>Merge-time review prompts</strong></summary>

Before approving changes under `examples/thin_slice/hydrology/`, ask:

- Is this file teaching the hydrology-first slice, or duplicating stronger owner material?
- Could a reviewer mistake this for an authoritative emitted artifact?
- Does the example stay public-safe?
- Does it preserve KFM’s negative-outcome honesty?
- If repo structure changed, do the upstream/downstream links in this README still resolve?

</details>

<details>
<summary><strong>Suggested next small addition</strong></summary>

If this folder remains example-only, the highest-value next file is probably one compact, redacted `EvidenceBundle` example paired with one `RuntimeResponseEnvelope` **ABSTAIN** example and one short `stale_visible.md` walkthrough.

That combination would explain:

- evidence drill-through
- finite runtime outcomes
- visible trust state

without pretending the full hydrology lane is already mounted here.

</details>

[Back to top](#hydrology)
