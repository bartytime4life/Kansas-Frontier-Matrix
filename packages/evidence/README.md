<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/1e6f2093-c5c0-4d2a-950c-713826b87e77
title: packages/evidence — Evidence resolver + bundle contracts
type: standard
version: v1
status: draft
owners: TBD (KFM Engineering + Governance)
created: 2026-02-22
updated: 2026-02-22
policy_label: restricted
related:
  - (not confirmed in repo) kfm://doc/KFM-GDG-2026
  - (not confirmed in repo) kfm://doc/KFM-IB5-2026
tags: [kfm, evidence, governance, contracts, policy]
notes:
  - This README documents the evidence package’s contract surfaces and testable invariants.
  - Source intent: KFM vNext “Definitive Design & Governance Guide” (2026-02-20).
[/KFM_META_BLOCK_V2] -->

# packages/evidence
Evidence resolver + EvidenceBundle contracts for the Kansas Frontier Matrix (KFM).

**Status:** Draft • **Owners:** TBD • **Policy:** Restricted (internal engineering)

![status](https://img.shields.io/badge/status-draft-informational)
![layer](https://img.shields.io/badge/layer-governed%20API%20boundary-blue)
![invariant](https://img.shields.io/badge/invariant-cite--or--abstain%20%2B%20trust%20membrane-critical)

---

## Quick navigation
- [What this package does](#what-this-package-does)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Core concepts](#core-concepts)
- [API contract](#api-contract)
- [EvidenceBundle shape](#evidencebundle-shape)
- [Policy enforcement](#policy-enforcement)
- [Directory layout](#directory-layout)
- [Tests and CI gates](#tests-and-ci-gates)
- [Implementation notes](#implementation-notes)
- [Troubleshooting](#troubleshooting)

---

## What this package does

`packages/evidence` implements the **Evidence Resolver** contract:

- Accept an **EvidenceRef** (e.g., `dcat://…`, `stac://…`, `prov://…`, `doc://…`, `graph://…`) *or* a structured reference.
- Enforce **policy decisions** (allow/deny) and apply **obligations** (redaction/generalization) before any content is returned.
- Return an **EvidenceBundle**:
  - a **human-readable “card”** (renderable in UI),
  - **machine metadata** (JSON),
  - optional **artifact links** (only when policy allows),
  - **digests**, **dataset_version identifiers**, and **audit references**.

This package is part of the **trust membrane**: clients must not access storage/DB directly; evidence resolution is the only permissible path from UI/Focus citations to underlying artifacts.

### Who uses it
- **Map / Story UI**: evidence drawer (click feature → resolve evidence → show bundle)
- **Focus Mode**: citations must resolve to evidence bundles (hard gate)
- **Governed API**: `/api/v1/evidence/resolve` endpoint
- **CI**: contract tests proving resolvability and “no leakage” behavior

[Back to top](#packagesevidence)

---

## Non-negotiable invariants

These are enforced by design + tests (fail closed):

1) **Trust membrane**
- UI/external clients never fetch from object storage/DB directly.
- Core logic does not bypass repository interfaces to reach storage.
- Every evidence resolve performs policy evaluation and logging.

2) **Evidence-first UX**
- Every map layer and story claim must open into evidence showing:
  dataset version, license/rights, policy label + redactions, provenance chain, checksums and artifact links.

3) **Cite-or-abstain**
- Any answer that includes factual claims must cite EvidenceBundles that are resolvable for the requesting user role.
- If citations cannot be verified, the system must abstain or reduce scope.

[Back to top](#packagesevidence)

---

## Core concepts

### EvidenceRef
A stable reference to evidence, using explicit schemes. **The resolver must resolve it in bounded calls** (no “guessing”). Minimum schemes:

- `dcat://…` → dataset/distribution metadata
- `stac://…` → collection/item/asset metadata
- `prov://…` → run lineage (activities/entities/agents)
- `doc://…` → governed documents (and story citations)
- `graph://…` → entity relations (if/when enabled)

> **Rule of thumb:** indexes (search, graph, PostGIS, vectors) may help *find* candidates, but anything surfaced to users must map back to an `EvidenceRef` and resolve through this package.

### EvidenceBundle
An immutable resolved view (addressed by digest) that supports caching and reproducibility.

### Policy label + obligations
Policy evaluation returns allow/deny plus obligations (e.g., generalize geometry, remove fields) and reason codes used for auditing + UX.

### Run receipts + audit ledger
Every pipeline run and every Focus query emits a run receipt. Evidence bundles include `audit_ref` links back to the receipt/ledger.

[Back to top](#packagesevidence)

---

## API contract

> **Illustrative endpoint** (actual routing may live elsewhere):  
> `POST /api/v1/evidence/resolve`

### Request (example)
```json
{
  "evidence_ref": "stac://collection/noaa-storm-events/items/2026-02-19#record=123",
  "view_state": {
    "bbox": [-102.0, 36.9, -94.6, 40.0],
    "time_window": ["2026-02-01", "2026-03-01"],
    "active_layers": ["storm-events"]
  }
}
```

### Response (example: allow)
```json
{
  "bundle_id": "sha256:bundle...",
  "dataset_version_id": "2026-02.abcd1234",
  "title": "Storm event record: 2026-02-19",
  "policy": {
    "decision": "allow",
    "policy_label": "public",
    "obligations_applied": []
  },
  "license": { "spdx": "CC-BY-4.0", "attribution": "Source org" },
  "provenance": { "run_id": "kfm://run/2026-02-20T12:00:00Z.abcd" },
  "artifacts": [
    {
      "href": "processed/events.parquet",
      "digest": "sha256:2222",
      "media_type": "application/x-parquet"
    }
  ],
  "checks": { "catalog_valid": true, "links_ok": true },
  "audit_ref": "kfm://audit/entry/123"
}
```

### Response (example: deny)
- HTTP `403` (or `404` where appropriate)
- **Must not leak** restricted dataset names, precise locations, or other sensitive metadata in the error payload.

[Back to top](#packagesevidence)

---

## EvidenceBundle shape

**Minimum fields** (template; codify as JSON Schema in this package):

| Field | Type | Notes |
|---|---|---|
| `bundle_id` | string | Digest-addressed immutable ID (e.g., `sha256:…`). |
| `dataset_version_id` | string | Immutable DatasetVersion identifier. |
| `title` | string | Human-friendly label for the evidence. |
| `policy` | object | Decision, label, obligations applied. |
| `license` | object | SPDX + attribution/rights holder info. |
| `provenance` | object | At least `run_id` / receipt reference. |
| `artifacts` | array | Zero or more artifacts (only if policy allows). |
| `checks` | object | e.g., catalog valid, cross-links OK. |
| `audit_ref` | string | Link into append-only audit ledger. |

> **Immutability rule:** bundles are written/served by digest. If something changes (policy, redaction, source version), you emit a new bundle.

[Back to top](#packagesevidence)

---

## Policy enforcement

This package is a **Policy Enforcement Point (PEP)**.

Minimum behaviors:

- **Default deny** when:
  - the EvidenceRef is unresolvable,
  - catalogs/provenance are missing,
  - rights are unclear,
  - the caller role is not allowed.
- Apply obligations **before** any user-visible content is returned.
- Redaction/generalization is treated as a first-class transform and must be recorded in provenance.

### Policy decision inputs (typical)
- caller role / auth context
- dataset policy_label
- requested operation (`resolve`, `download`, `export`, etc.)
- requested view_state (bbox/time/layers) — used to enforce “no restricted bbox leakage” rules

[Back to top](#packagesevidence)

---

## Directory layout

> This is a **recommended** (PROPOSED) structure. Adjust to the repo’s actual tooling.

```text
packages/evidence/
├─ README.md
├─ src/
│  ├─ index.(ts|py|go)
│  ├─ resolve/
│  │  ├─ resolveEvidenceRef.(ts|py|go)
│  │  ├─ schemes/
│  │  │  ├─ dcat.(ts|py|go)
│  │  │  ├─ stac.(ts|py|go)
│  │  │  ├─ prov.(ts|py|go)
│  │  │  ├─ doc.(ts|py|go)
│  │  │  └─ graph.(ts|py|go)
│  │  └─ obligations/
│  │     ├─ applyObligations.(ts|py|go)
│  │     └─ redactGeneralize.(ts|py|go)
│  ├─ render/
│  │  ├─ renderCard.(ts|py|go)
│  │  └─ markdown.(ts|py|go)
│  └─ ports/
│     ├─ PolicyClient.(ts|py|go)
│     ├─ CatalogRepo.(ts|py|go)
│     ├─ ObjectStoreRepo.(ts|py|go)
│     └─ AuditLedgerRepo.(ts|py|go)
├─ schemas/
│  ├─ evidence_ref.schema.json
│  └─ evidence_bundle.schema.json
├─ fixtures/
│  ├─ public.example.json
│  ├─ restricted.example.json
│  └─ invalid.example.json
└─ test/
   ├─ contract/
   ├─ policy/
   └─ unit/
```

[Back to top](#packagesevidence)

---

## Tests and CI gates

This package is “release critical” because it underpins evidence-first UX and cite-or-abstain.

Minimum CI checks (implement in this repo’s test runner / CI system):

- **Schema validation**
  - EvidenceRef and EvidenceBundle schemas compile
  - fixtures validate (valid examples pass; invalid examples fail)

- **Link-checking** (repo-context)
  - DCAT ↔ STAC ↔ PROV cross-links resolve for promoted dataset versions

- **Evidence resolver contract tests**
  - “public evidence resolves” → bundle with allowed artifacts
  - “restricted evidence denies” → 403/404 with **no sensitive metadata leakage**
  - spec_hash stability / deterministic outputs (where applicable)

> Tie these checks into the Promotion Contract: a dataset version cannot be promoted unless evidence resolution works and contracts validate.

[Back to top](#packagesevidence)

---

## Implementation notes

### Two-call UX constraint
Evidence must be usable in **≤ 2 calls** from the UI, otherwise users ignore provenance:
1) feature → resolve evidence → view bundle  
2) citation → resolve evidence → view same bundle

### Don’t let the UI decide policy
The UI can show badges and reasons, but policy decisions happen here (or in the shared policy engine it calls).

### Caching
Cache by `bundle_id` (digest). Never cache by mutable tags.

### Observability
Emit structured events for:
- resolve start/end
- policy decision id + obligations applied
- bundle_id produced/served
- deny reasons (safe, non-leaking)

[Back to top](#packagesevidence)

---

## Troubleshooting

### “EvidenceRef cannot be resolved”
- Check catalogs exist (DCAT/STAC/PROV) and cross-links are valid.
- Check the referenced dataset_version is promoted (not in RAW/WORK/QUARANTINE).
- Check policy label + role allow access.

### “Public request returns 403”
- Verify rights metadata is complete and license is explicit.
- Verify no sensitivity obligations are triggering default deny.

### “Restricted request leaks details in errors”
- Add / tighten “no sensitive metadata leakage” contract tests.
- Ensure error payloads are constant-shape and do not echo internal identifiers.

[Back to top](#packagesevidence)
