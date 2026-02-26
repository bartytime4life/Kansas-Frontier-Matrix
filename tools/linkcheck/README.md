<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/cb299109-a84e-48ce-bfcb-b107245cc921
title: tools/linkcheck/README
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-26
updated: 2026-02-26
policy_label: public
related:
  - docs/MASTER_GUIDE_v13.md
  - docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md
  - tools/validators/
  - policy/rego/
tags: [kfm, tooling, ci, governance, linkcheck]
notes:
  - Fail-closed reference integrity gate for catalogs, docs, and Story Nodes.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Linkcheck

**Purpose:** fail-closed validation of **links, citations, and cross-references** so that *nothing user-facing ships with broken evidence*.  
**Primary use:** CI promotion gates (blocks merge/promotion when references don’t resolve).

**Status:** `draft` (verify wiring + entrypoints) · **Owners:** `TBD`

![Gate](https://img.shields.io/badge/gate-linkcheck-informational) <!-- TODO: wire to real workflow badge -->
![Mode](https://img.shields.io/badge/mode-fail--closed-critical)
![Runtime](https://img.shields.io/badge/runtime-nodejs%20(expected)-blue) <!-- TODO: confirm runtime + versions in repo -->

---

## Quick navigation

- [What this tool is](#what-this-tool-is)
- [Where it fits in KFM](#where-it-fits-in-kfm)
- [Quickstart](#quickstart)
- [What gets checked](#what-gets-checked)
- [Inputs and outputs](#inputs-and-outputs)
- [CI integration](#ci-integration)
- [Definition of done](#definition-of-done)
- [Governance and safety notes](#governance-and-safety-notes)
- [Troubleshooting](#troubleshooting)
- [Directory layout](#directory-layout)
- [Appendix](#appendix)

---

## What this tool is

`tools/linkcheck/` is the home for **reference integrity checks** used by KFM CI to prevent:

- docs pointing to files that were moved/removed,
- Story Nodes citing sources that don’t exist,
- catalog artifacts (DCAT/STAC/PROV) that don’t cross-link cleanly,
- “EvidenceRef” / citation handles that can’t be resolved.

> **Fail-closed rule:** if a reference is ambiguous or missing, the tool should exit non‑zero and CI should block.

---

## Where it fits in KFM

KFM treats **cross-links and citations** as a promotion requirement (alongside schema-valid catalogs, policy tests, etc.). Link checking is part of the CI workflow and is intended to run after catalog schema validators and before policy/contract gates.

```mermaid
flowchart LR
  A[Docs and Story Nodes] --> C[Linkcheck]
  B[Catalog triplet: DCAT STAC PROV] --> C[Linkcheck]
  C --> D[Report artifact]
  C --> E[Exit code for CI]
  E -->|non zero| F[Block merge or promotion]
  E -->|zero| G[Allow next gates]
```

---

## Quickstart

### Run in CI (expected)

The design docs show CI invoking the catalog link checker like this:

```bash
node tools/linkcheck/catalog_linkcheck.js
```

If your repo uses a different entrypoint name (or a wrapper script), update this README and the CI step accordingly.

### Run locally

```bash
# from repo root
node tools/linkcheck/catalog_linkcheck.js

# always check help if available
node tools/linkcheck/catalog_linkcheck.js --help
```

---

## What gets checked

> **Important:** the *exact* checks depend on the implementation in this folder. The table below captures the **required intent** (what CI is trying to guarantee).

| Check area | Examples of what must resolve | Why it matters | Expected behavior |
|---|---|---|---|
| **Catalog cross-links** | DCAT ↔ STAC ↔ PROV references line up; IDs referenced exist | Prevent “published” datasets that can’t be traced end-to-end | Fail the run |
| **Asset href existence** | STAC assets / distributions point to real artifacts (or a resolvable stable URI) | Prevent UI from linking to missing data | Fail the run |
| **EvidenceRef resolvability** | EvidenceRefs used by Story Nodes / Focus cases point to known evidence bundles or catalog items | Enforces cite-or-abstain and protects trust membrane | Fail the run |
| **Doc and Story Node links** *(recommended)* | Internal links, citations, and reference tags are valid | Prevent broken narratives and missing sources | Fail the run |

---

## Inputs and outputs

### Typical inputs (expected locations)

These are the canonical homes used throughout KFM:

- Catalogs: `data/catalog/dcat/`, `data/stac/`, `data/prov/`
- Docs / Story Nodes: `docs/`, plus any Story Node directories under `docs/` (project-dependent)

> If your repo uses different paths, treat them as configuration and keep the tool deterministic.

### Outputs (recommended contract)

Even if the implementation differs, KFM benefits from a stable output contract:

- **Exit code**
  - `0` → all references resolve
  - `!= 0` → at least one unresolved/invalid reference
- **Machine report** (recommended)
  - `artifacts/reports/linkcheck.json`
- **Human summary** (recommended)
  - `artifacts/reports/linkcheck.md`

<details>
<summary><strong>Suggested JSON report shape</strong> (proposed)</summary>

```json
{
  "ok": false,
  "checked_at": "2026-02-26T00:00:00Z",
  "counts": { "files_scanned": 123, "refs_checked": 456, "errors": 2, "warnings": 7 },
  "errors": [
    {
      "type": "missing_target",
      "source_file": "data/catalog/dcat/example.jsonld",
      "ref": "stac://items/does-not-exist",
      "message": "Referenced STAC item not found"
    }
  ],
  "warnings": []
}
```

</details>

---

## CI integration

### Minimal GitHub Actions example

```yaml
- name: Validate catalogs
  run: |
    node tools/validators/validate_dcat.js
    node tools/validators/validate_stac.js
    node tools/validators/validate_prov.js

- name: Linkcheck citations
  run: node tools/linkcheck/catalog_linkcheck.js
```

### Gate placement guidance

Recommended ordering (high-level):

1. **Lint / typecheck**
2. **Unit tests**
3. **Catalog schema validators**
4. **Linkcheck (this tool)**
5. **Policy tests**
6. **Spec-hash drift / contract tests**
7. **Focus Mode eval harness (optional early)**

---

## Definition of done

This folder is “gate-ready” when:

- [ ] The CI job runs linkcheck on every PR that touches catalogs/docs.
- [ ] Broken or missing references cause a non-zero exit code.
- [ ] The tool produces a stable, machine-readable report artifact.
- [ ] There are fixtures/tests for at least:
  - [ ] one passing case
  - [ ] one broken-cross-link case
  - [ ] one missing-asset-href case
  - [ ] one unresolved EvidenceRef/citation case (if applicable)
- [ ] External URL fetching is either disabled in CI or tightly allowlisted.

---

## Governance and safety notes

- **Default-deny / fail-closed:** do not “best effort” a broken reference into a pass.
- **Don’t leak sensitive content in logs:** if a missing reference points to a restricted dataset, keep the error message descriptive but not disclosive.
- **Be careful with external network calls:** prefer *offline* validation (existence + formatting) unless an explicit allowlist is configured (avoid accidental scanning of third-party sites from CI runners).
- **Determinism:** results should not depend on time-of-day or external availability.

---

## Troubleshooting

### “It fails on my branch but not on main”

Common causes:

- You moved or renamed a file without updating all references (docs, Story Nodes, catalog links).
- A dataset version ID changed but an EvidenceRef wasn’t updated everywhere.
- A catalog validator passed schema, but cross-links between catalogs are now inconsistent.

**Fix pattern:** locate the first reported broken reference, update the source to point to the new target, and rerun.

### “CI is timing out”

If your implementation checks external URLs:

- add an allowlist + caching, or
- switch to offline-only mode in CI, and run deep external checking only in scheduled jobs.

---

## Directory layout

> Directory documentation standard: **title + purpose**, **where it fits**, **acceptable inputs**, **exclusions**.

```text
tools/linkcheck/
  README.md                   # You are here
  catalog_linkcheck.js         # (expected) catalog cross-link validator used by CI
  ...                          # implementation-specific helpers, tests, configs
```

### Acceptable inputs

- Catalog artifacts and/or docs that are part of the governed KFM build.
- Configuration files for link checking (ignore lists, allowlists), if present.

### Exclusions

- Not a content linter for prose quality.
- Not a replacement for JSON Schema validation (that belongs in `tools/validators/`).
- Not a network scanner / crawler unless explicitly configured and approved.

---

## Appendix

### Minimum verification steps (to confirm this README matches reality)

1. List the directory: `ls -la tools/linkcheck/`
2. Confirm the CI entrypoint: search CI config for `tools/linkcheck/`
3. Run locally and confirm expected exit codes + reports:
   - `node tools/linkcheck/catalog_linkcheck.js`
4. Ensure failures block merge in CI.

---

**Back to top:** [↑](#top)<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/3455e0ac-e920-4872-938b-63640d57c707
title: Linkcheck tool
type: standard
version: v1
status: draft
owners: KFM Engineering
created: 2026-02-22
updated: 2026-02-22
policy_label: public
related: []
tags: [kfm, tooling, ci, promotion-gate, linkcheck]
notes:
  - Contract-first README for tools/linkcheck.
[/KFM_META_BLOCK_V2] -->

# Linkcheck
Deterministic, **fail-closed** link integrity checks for KFM catalogs and citations.

![status](https://img.shields.io/badge/status-draft-orange)
![gate](https://img.shields.io/badge/promotion%20gate-linkcheck-blue)
![mode](https://img.shields.io/badge/mode-fail--closed-red)

## Navigate
- [Purpose](#purpose)
- [What this checks](#what-this-checks)
- [Quick start](#quick-start)
- [Directory layout](#directory-layout)
- [CI integration](#ci-integration)
- [Configuration](#configuration)
- [Reports and exit codes](#reports-and-exit-codes)
- [Adding new checks](#adding-new-checks)
- [Governance and safety](#governance-and-safety)
- [Troubleshooting](#troubleshooting)
- [References](#references)

---

## Purpose

KFM relies on **cross-linked catalogs** (DCAT + STAC + PROV) to make datasets navigable, auditable, and citeable.
If those links drift or break, *everything above them* (evidence resolution, citations, UI “evidence drawers”, and
Focus Mode cite-or-abstain) becomes unreliable.

**This tool exists to turn “catalog cross-linking” into enforceable behavior in CI.**

### Promotion gate alignment

**CONFIRMED requirement:** promotion must be blocked unless **cross-links resolve** and **EvidenceRefs resolve** for the dataset version being promoted.

Linkcheck is the mechanism that enforces that gate as code (not as “reviewer memory”).

### What “fail-closed” means here

If a promoted dataset version contains broken or ambiguous links, linkcheck must exit non‑zero so CI blocks promotion.

> ✅ Linkcheck is intended to be run **after** schema validation (DCAT/STAC/PROV validators) and **before** any
> “promotion” step that publishes the dataset to governed runtime surfaces.

### Where it fits in the Truth Path

```mermaid
flowchart LR
  RAW[RAW] --> WORK[WORK or QUARANTINE]
  WORK --> PROCESSED[PROCESSED]
  PROCESSED --> CATALOG[CATALOG triplet]
  CATALOG --> LINKCHECK[tools/linkcheck]
  LINKCHECK -->|pass| PUBLISHED[PUBLISHED surfaces]
  LINKCHECK -->|fail| BLOCK[CI blocks promotion]
```

[Back to top](#linkcheck)

---

## What this checks

### Catalog cross-links

Minimum cross-link rules this tool must be able to verify:

- A DCAT Dataset record enumerates Distributions, and each Distribution points to an artifact digest (or a digest-pinned URI)
- A DCAT Dataset record points to the PROV activity that generated it (for example via `prov:wasGeneratedBy`)
- A STAC Collection links to its DCAT Dataset record via `rel="describedby"`
- Each STAC Item links to a PROV activity and/or a run receipt (so you can trace “what produced this”)
- EvidenceRef schemes map to these objects **deterministically** (no heuristics / no guessing)

> NOTE  
> Cross-links must be deterministic. “Best effort” resolution is not acceptable for promoted artifacts.

### Repo-context resolution

By default, linkcheck should operate in **repo context**:

- Resolve relative paths against the repo checkout
- Resolve content-addressed digests against the expected artifact layout
- Treat network access as *optional* (see [Configuration](#configuration))

### Non-goals

Linkcheck is **not** intended to be:

- a full internet crawler
- a validator for JSON schema (that’s `tools/validators/*`)
- a content checker (it verifies referential integrity, not scientific/historical correctness)

[Back to top](#linkcheck)

---

## Quick start

> This README documents the **contract** for the linkcheck tool. If your implementation uses different filenames
> or a different runtime (Node/Python/etc.), update the commands below to match.

### Run locally

```bash
# Typical entrypoint for catalog cross-link checking
node tools/linkcheck/catalog_linkcheck.js
```

### Run against a specific dataset subtree

```bash
node tools/linkcheck/catalog_linkcheck.js \
  --root data \
  --include "data/**/catalog/**" \
  --report artifacts/linkcheck-report.json
```

### Developer-friendly output

```bash
node tools/linkcheck/catalog_linkcheck.js --format pretty
```

[Back to top](#linkcheck)

---

## Directory layout

Expected layout (adjust if your repo differs):

```text
tools/
└─ linkcheck/
   ├─ README.md
   ├─ catalog_linkcheck.js        # catalog cross-link verification (entrypoint; name from KFM CI example)
   ├─ linkcheck.config.json       # optional config (repo defaults)
   ├─ lib/                        # implementation helpers (resolvers, scanners)
   └─ fixtures/                   # tiny catalog fixtures for tests
```

[Back to top](#linkcheck)

---

## CI integration

The intended CI posture is “run on every PR that touches promoted artifacts or catalogs”.

Example (GitHub Actions style):

```yaml
- name: Validate catalogs
  run: |
    node tools/validators/validate_dcat.js
    node tools/validators/validate_stac.js
    node tools/validators/validate_prov.js

- name: Linkcheck citations
  run: node tools/linkcheck/catalog_linkcheck.js
```

### When to run it

Run linkcheck when any of the following change:

- DCAT / STAC / PROV JSON or JSON-LD files
- processed artifact manifests or digest lists
- run receipts
- schema/profile changes that alter cross-link expectations

[Back to top](#linkcheck)

---

## Configuration

> **PROPOSED** default config shape. Adopt only if your implementation supports it.

### Configuration file

`tools/linkcheck/linkcheck.config.json`:

```json
{
  "mode": "offline",
  "roots": ["data", "prov", "catalog"],
  "include": ["**/*.json", "**/*.jsonld"],
  "exclude": ["**/node_modules/**", "**/.git/**"],
  "external": {
    "enabled": false,
    "allowDomains": [],
    "timeoutMs": 5000,
    "maxConcurrency": 8
  },
  "policy": {
    "redactInLogs": true,
    "skipSchemes": ["mailto", "tel"]
  }
}
```

### Offline vs online

- **offline (default)**: verify only what can be proven from repo + artifacts + digests
- **online (optional)**: also `HEAD`/`GET` external URLs (recommended only with allowlisted domains)

> WARNING  
> Online checking can introduce flakiness. If enabled, keep it **allowlist-only** and cache results.

[Back to top](#linkcheck)

---

## Reports and exit codes

### Exit codes

- `0` — all checks passed
- `1` — at least one broken link (promotion must be blocked)
- `2` — invalid arguments/config
- `3` — unexpected exception (treat as failure in CI)

### Report format

> **PROPOSED** report schema. Keep it stable once adopted.

```json
{
  "tool": "kfm-linkcheck",
  "version": "1.0.0",
  "started_at": "2026-02-22T00:00:00Z",
  "finished_at": "2026-02-22T00:00:02Z",
  "mode": "offline",
  "totals": { "checked": 123, "errors": 2, "warnings": 1 },
  "errors": [
    {
      "code": "E_LINK_MISSING",
      "from": "data/hazards/noaa/catalog/stac-collection.json",
      "to": "prov/run/2026-02-20T12:34Z.noaa.abcd1234.jsonld",
      "message": "STAC item links to a PROV run receipt that does not exist in repo context."
    }
  ],
  "warnings": []
}
```

[Back to top](#linkcheck)

---

## Adding new checks

When you add a new catalog profile field or EvidenceRef scheme, treat linkcheck as part of the
**promotion contract**:

1. Add/adjust a resolver (how to resolve this link in repo context)
2. Add fixture(s) in `fixtures/` for pass + fail cases
3. Add a unit test that asserts:
   - the failure is detected
   - the error code is stable and actionable
4. Update this README with the new rule (and why it’s required)

### Definition of Done for a new rule

- [ ] Rule is deterministic (no guessing)
- [ ] Rule is covered by tests (pass + fail)
- [ ] Report includes actionable remediation text
- [ ] CI blocks promotion when the rule fails

[Back to top](#linkcheck)

---

## Governance and safety

### Don’t leak sensitive paths or links

If catalogs include restricted locations, partner-controlled endpoints, or private artifact stores:

- redact tokens and credentials in logs
- consider masking full URLs in failure output (show domain + path prefix only)
- treat “restricted” policy labels as **default-deny** for external checks

### Determinism over convenience

Prefer checks that are:

- local and reproducible
- pinned by digest
- independent of third-party uptime

### Threat considerations

Link sources are untrusted input. Linkcheck must:

- treat catalogs and markdown as data, not code
- never execute embedded scripts or follow `file://` outside the repo root
- cap recursion and concurrency to avoid DoS during CI runs

[Back to top](#linkcheck)

---

## Troubleshooting

### “It passes locally but fails in CI”

Common causes:

- CI runs from a different working directory (use repo-root resolution)
- files generated locally are missing from the PR
- config differs between local and CI

Recommended debugging:

```bash
node tools/linkcheck/catalog_linkcheck.js --debug --format pretty
```

### “We have legit external links, but CI is flaky”

- keep external checking disabled in CI
- move the external URL into a “reference registry” and pin it via snapshot if it matters for promotion
- if you must check external links, allowlist domains and increase timeouts modestly

[Back to top](#linkcheck)

---

## References

Internal KFM requirements that motivate this tool:

- KFM: cross-linking rules and “CI should include a link-checker” (see Definitive Design & Governance Guide, vNext draft)
- KFM: promotion workflow includes “Linkcheck citations” step in CI (illustrative workflow)
