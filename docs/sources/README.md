<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: Sources
type: standard
version: v1
status: draft
owners: NEEDS-VERIFICATION
created: 2026-04-23
updated: 2026-04-23
policy_label: NEEDS-VERIFICATION
related: [docs/sources/SOURCE_DESCRIPTOR_STANDARD.md, docs/sources/SOURCE_REFRESH_RULES.md, docs/registers/AUTHORITY_LADDER.md, docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md, docs/intake/IDEA_INTAKE.md, contracts/OBJECT_MAP.md, data/registry/source-descriptors/]
tags: [kfm, sources, source-descriptor, source-refresh, documentation-control]
notes: [Generated as a repo-ready draft from attached KFM doctrine. Owner, policy label, doc_id, adjacent path existence, and current repo history remain NEEDS VERIFICATION.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Sources

Source-admission and refresh guidance for KFM: turn named data, API, archive, sensor, model, and documentary sources into evidence-bearing contracts before ingestion.

> [!IMPORTANT]
> **Status:** `experimental` / metadata `draft`  
> **Owners:** `NEEDS-VERIFICATION`  
> **Path:** `docs/sources/README.md`  
> **Authority posture:** `PROPOSED canonical/supporting` until the mounted repository confirms adjacent files, owners, and link targets.
>
> [![Status: experimental](https://img.shields.io/badge/status-experimental-orange)](#status--impact)
> [![Truth posture: evidence first](https://img.shields.io/badge/truth%20posture-evidence--first-blue)](#truth-posture)
> [![Policy: fail closed](https://img.shields.io/badge/policy-fail--closed-critical)](#source-admission-gates)
> [![Repo evidence: needs verification](https://img.shields.io/badge/repo%20evidence-needs%20verification-lightgrey)](#verification-gates)
>
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Source roles](#source-roles) · [Admission gates](#source-admission-gates) · [Diagram](#flow) · [Verification](#verification-gates)

---

## Scope

`docs/sources/` is the documentation home for **source onboarding rules**, **source-role discipline**, and **source refresh expectations**.

This directory exists to answer one question before any connector, watcher, scraper, import job, or map layer is trusted:

> Has this source been described well enough to become admissible evidence in KFM?

A source being technically reachable is not enough. KFM source admission requires explicit identity, role, rights, sensitivity, cadence, spatial support, temporal support, validation burden, and publication intent.

### This directory owns

- Source-admission guidance.
- Source role vocabulary and burden notes.
- Source descriptor documentation standards.
- Source refresh and staleness rules.
- Cross-links from source guidance to contracts, schemas, policy, fixtures, runbooks, receipts, proofs, and catalog objects.

### This directory does not own

- Raw source payloads.
- Source descriptor instances.
- Connector implementation.
- Runtime API routes.
- Promotion decisions.
- Public release manifests.
- Evidence bundles for specific claims.

[Back to top](#top)

---

## Status & impact

| Field | Value |
|---|---|
| README-like status | `experimental` |
| Metadata status | `draft` |
| Owners | `NEEDS-VERIFICATION` |
| Current implementation evidence | `UNKNOWN` until mounted repo inspection |
| Intended authority class | `PROPOSED canonical/supporting` |
| First review burden | Verify adjacent files, owner, schema home, and data registry paths |
| Safe merge mode | Additive documentation PR; no live connector activation |

> [!NOTE]
> This README is safe as a documentation-control surface. It is **not** proof that source descriptors, validators, registries, workflows, or promotion gates already exist in the checked-out repository.

---

## Repo fit

| Direction | Surface | Expected relationship | Status |
|---|---|---|---|
| Current file | `docs/sources/README.md` | Directory landing page for source onboarding and refresh guidance | `PROPOSED` |
| Upstream docs landing | [`../README.md`](../README.md) | Should link into this source guidance once verified | `NEEDS VERIFICATION` |
| Authority register | [`../registers/AUTHORITY_LADDER.md`](../registers/AUTHORITY_LADDER.md) | Should define how sources, doctrine, repo evidence, and external standards rank | `NEEDS VERIFICATION` |
| Canon/status register | [`../registers/CANONICAL_LINEAGE_EXPLORATORY.md`](../registers/CANONICAL_LINEAGE_EXPLORATORY.md) | Should identify whether source docs are canon, lineage, exploratory, or reference | `NEEDS VERIFICATION` |
| Peer source standard | [`SOURCE_DESCRIPTOR_STANDARD.md`](SOURCE_DESCRIPTOR_STANDARD.md) | Should define the `SourceDescriptor` documentation and field expectations | `NEEDS VERIFICATION` |
| Peer refresh rules | [`SOURCE_REFRESH_RULES.md`](SOURCE_REFRESH_RULES.md) | Should define cadence, freshness, no-change receipts, and staleness handling | `NEEDS VERIFICATION` |
| Semantic contracts | [`../../contracts/README.md`](../../contracts/README.md) / [`../../contracts/OBJECT_MAP.md`](../../contracts/OBJECT_MAP.md) | Should define object meaning and invariants | `NEEDS VERIFICATION` |
| Executable schemas | [`../../schemas/README.md`](../../schemas/README.md) | Should define machine-checkable shapes | `NEEDS VERIFICATION` |
| Policy | [`../../policy/README.md`](../../policy/README.md) | Should enforce rights, sensitivity, promotion, runtime, and denial logic | `NEEDS VERIFICATION` |
| Source instances | [`../../data/registry/source-descriptors/`](../../data/registry/source-descriptors/) | Should hold source descriptor instances, not prose standards | `NEEDS VERIFICATION` |
| Fixtures | [`../../tests/fixtures/README.md`](../../tests/fixtures/README.md) | Should hold valid/invalid examples for source descriptors and gate behavior | `NEEDS VERIFICATION` |
| Runbook | [`../runbooks/SOURCE_REFRESH.md`](../runbooks/SOURCE_REFRESH.md) | Should describe operational refresh procedure and emitted receipts | `NEEDS VERIFICATION` |

[Back to top](#top)

---

## Inputs

Content belongs here when it defines **how a source may enter KFM**, not when it is the source itself.

| Accepted input | Belongs here when it… | Example |
|---|---|---|
| Source descriptor guidance | Defines minimum fields, review burden, and admissibility expectations | “Every source descriptor must declare owner, rights, sensitivity, cadence, role, and validation checks.” |
| Source role taxonomy | Stabilizes meanings such as observation, regulatory record, modeled surface, or documentary evidence | “Operational warning feed is not the same as regulatory flood layer.” |
| Source refresh rules | Defines update cadence, freshness, staleness, no-change receipts, and quarantine behavior | “A no-change refresh still emits a receipt.” |
| Source admission checklists | Helps reviewers decide whether a new source can be normalized, quarantined, deferred, or denied | “Unresolved redistribution terms block public promotion.” |
| Crosswalk guidance | Links source documentation to contracts, schemas, policy, fixtures, and registry instances | “A `SourceDescriptor` prose card points to a schema and invalid fixture.” |
| Lane-specific burden notes | Explains source burden differences for hydrology, hazards, biodiversity, archaeology, people/DNA/land, and other lanes | “Rare species exact coordinates fail closed for public surfaces.” |

[Back to top](#top)

---

## Exclusions

| Do not put this in `docs/sources/` | Use this instead | Why |
|---|---|---|
| Raw downloaded files, API dumps, rasters, CSVs, PDFs, scans | `data/raw/`, `data/work/`, or `data/quarantine/` | Raw materials belong to the lifecycle, not the documentation standard. |
| Source descriptor instances | `data/registry/source-descriptors/` | Instances are registry records; this directory defines how to write and review them. |
| Ingest receipts or refresh receipts | `data/receipts/` | Receipts are emitted process memory, not normative prose. |
| Proof packs or promotion evidence | `data/proofs/` | Proofs support release; they do not define source admission rules. |
| Release manifests or catalog closure outputs | `data/manifests/`, `data/catalog/`, or release-specific homes | Releases are outputs of promotion gates. |
| Connector code, watchers, scrapers, fetch scripts | `pipelines/`, `tools/`, `packages/`, or app-specific homes | Implementation must remain downstream of source admission. |
| Human semantic object definitions | `contracts/` | Contracts explain object meaning and invariants. |
| JSON Schema or executable validation shape | `schemas/` | Schemas are machine-checkable definitions. |
| Policy-as-code or gate rules | `policy/` | Policy decides allow, deny, restrict, quarantine, or require review. |
| Domain lane doctrine | `docs/domains/` | Domains define lane burden; sources define source admission. |
| Exploratory “New Ideas” packets | `docs/intake/` or `docs/archive/exploratory/` | Exploratory pressure must not become accidental authority. |

[Back to top](#top)

---

## Directory tree

Expected source-documentation shape:

```text
docs/sources/
├── README.md                         # this file
├── SOURCE_DESCRIPTOR_STANDARD.md      # NEEDS VERIFICATION
└── SOURCE_REFRESH_RULES.md            # NEEDS VERIFICATION
```

Related but separate source-admission surfaces:

```text
contracts/
└── OBJECT_MAP.md                      # human semantic object map; NEEDS VERIFICATION

schemas/
└── ...                                # executable source descriptor schema; NEEDS VERIFICATION

policy/
└── ...                                # rights/sensitivity/release policy; NEEDS VERIFICATION

data/
└── registry/
    └── source-descriptors/            # source descriptor instances; NEEDS VERIFICATION

tests/
└── fixtures/
    └── ...                            # valid/invalid descriptor examples; NEEDS VERIFICATION
```

[Back to top](#top)

---

## Quickstart

Use these commands from the repository root during review. They are read-only discovery checks.

```bash
# 1. Inspect source-documentation and registry surfaces.
find docs/sources data/registry/source-descriptors -maxdepth 4 -type f 2>/dev/null | sort

# 2. Inspect adjacent contract, schema, policy, and fixture surfaces.
find contracts schemas policy tests/fixtures -maxdepth 4 -type f 2>/dev/null | sort

# 3. Trace source-admission vocabulary across the repo.
grep -RInE \
  'SourceDescriptor|source_descriptor|source role|source_role|rights|sensitivity|cadence|freshness|crs|valid_time|as_of|EvidenceBundle|ReleaseManifest|DecisionEnvelope' \
  docs contracts schemas policy data tests tools pipelines 2>/dev/null || true

# 4. Confirm this README's links before promoting the doc from draft.
python - <<'PY'
from pathlib import Path

root = Path.cwd()
targets = [
    "docs/README.md",
    "docs/registers/AUTHORITY_LADDER.md",
    "docs/registers/CANONICAL_LINEAGE_EXPLORATORY.md",
    "docs/sources/SOURCE_DESCRIPTOR_STANDARD.md",
    "docs/sources/SOURCE_REFRESH_RULES.md",
    "contracts/README.md",
    "schemas/README.md",
    "policy/README.md",
    "tests/fixtures/README.md",
    "data/registry/source-descriptors",
]
for target in targets:
    p = root / target
    print(("OK   " if p.exists() else "MISS ") + target)
PY
```

> [!WARNING]
> Discovery output is not proof of enforcement. A file existing is weaker evidence than a passing validator, emitted receipt, policy decision, release proof pack, or runtime trace.

[Back to top](#top)

---

## Truth posture

Use the narrowest truthful label when documenting source material.

| Label | Meaning in this directory |
|---|---|
| `CONFIRMED` | Verified from mounted repo evidence, accepted doctrine, source descriptor instance, validator output, receipt, proof, or release artifact. |
| `INFERRED` | Strongly supported by doctrine or nearby repo structure, but not directly proven. |
| `PROPOSED` | Design or documentation plan not yet verified as implemented. |
| `UNKNOWN` | Not resolved by currently visible evidence. |
| `NEEDS VERIFICATION` | Checkable before promotion, release, or owner assignment. |

### Source-grounded vs. source-like

A source-looking URL, dataset name, API endpoint, shapefile, table, map service, or PDF is only a **candidate source** until KFM records the source’s role, rights, sensitivity, cadence, support, validation burden, and intended use.

[Back to top](#top)

---

## Source roles

Source roles are not interchangeable. A map can render multiple roles together, but KFM must not collapse their meanings.

| Source role | Typical material | Handling rule |
|---|---|---|
| Direct observation / measurement | Gauges, sensors, field samples, point clouds, station observations | Preserve units, support, calibration context, uncertainty, and valid time. Do not repackage as policy truth. |
| Statutory / regulatory record | Flood hazard layers, designations, lists, declarations, administrative boundaries | Preserve legal status, effective date, supersession path, and exact source identity. |
| Operational context feed | Advisories, alerts, watches, live operations feeds, transit positions | Useful for context; not a replacement for archival, regulatory, or source-of-record evidence. |
| Discovery mirror / index | Dataset catalogs, STAC collections, portals, search indexes | Treat as discovery scaffolding; verify against source of record where required. |
| Modeled / assimilated / derived surface | Habitat models, anomaly surfaces, smoke masks, flow accumulation, interpolated rasters | Keep visibly derived; store method, lineage, support, and uncertainty. |
| Documentary evidence object | Newspapers, oral histories, maps, plats, scans, reports, notebooks | Preserve original identity; extraction, OCR, summarization, and interpretation require review-aware lanes. |
| Authority / crosswalk system | GNIS, LCNAF, VIAF, taxonomic authorities, identifier crosswalks | Use for disambiguation and stitching, not as a replacement for source identity or proof. |
| Community-contributed source | Citizen observations, volunteered geography, crowd reports | Require explicit provenance, review burden, rights posture, precision handling, and public-safety controls. |

[Back to top](#top)

---

## Source admission gates

A source should not move from candidate to admitted source unless the minimum gates below can be answered.

| Gate | Required evidence | Fails closed when… |
|---|---|---|
| Identity | Stable source name, steward, source-of-record or provider status, source URL/acquisition path | Source identity is ambiguous, mirrored without source-of-record checks, or unauditable. |
| Role | Declared source role and lane fit | A source is treated as generic “data” without epistemic role. |
| Rights | License, terms, redistribution, attribution, and automation posture | Rights are unknown, incompatible, or unreviewed for the intended output. |
| Sensitivity | Sensitive classes, exact-location rules, public precision, steward review burden | Sensitive geometry or personal/cultural/critical-infrastructure risk can leak. |
| Spatial basis | Native CRS, support, scale/resolution, extent, geometry precision, transform burden | CRS/support is missing, incompatible, or silently transformed. |
| Temporal basis | Valid time, issue time, retrieved time, update cadence, freshness, expiry, supersession | Event time, issue time, update time, and publication time are flattened. |
| Validation | Expected checks, required fixtures, known failure modes, quarantine rules | No invalid fixture, no validator, or no remediation path exists. |
| Publication intent | Intended KFM use, public-safe derivative plan, citation expectations | The source is useful internally but not safe or legal for public release. |
| Lifecycle hooks | Expected receipts, catalog records, proof objects, and rollback/correction hooks | Admission cannot be reconstructed after ingest or release. |

[Back to top](#top)

---

## Flow

```mermaid
flowchart TD
  A[Candidate source named] --> B[docs/sources guidance]
  B --> C{SourceDescriptor ready?}

  C -->|No| D[Keep as candidate / idea intake]
  C -->|Yes| E[Validate descriptor shape]

  E --> F{Rights, sensitivity, role, support, time clear?}
  F -->|No| G[Quarantine / deny / needs review]
  F -->|Yes| H[data/registry/source-descriptors]

  H --> I[Connector or fixture-only ingest]
  I --> J[IngestReceipt]
  J --> K[ValidationReport]
  K --> L{Promotion eligible?}

  L -->|No| M[Work / quarantine with visible reason]
  L -->|Yes| N[Catalog / proof / release surfaces]

  N --> O[EvidenceBundle]
  O --> P[Governed API / UI / Focus Mode]
```

This flow is intentionally conservative: documentation and descriptors come before live automation.

[Back to top](#top)

---

## Source refresh rules

Source refresh belongs here as doctrine and in runbooks as operations. Keep these principles visible:

1. A refresh run must emit a receipt even when nothing changes.
2. Source freshness is not the same as claim validity.
3. Retrieval time, source valid time, issue time, expiry time, and publication time should not be silently collapsed.
4. Conditional requests, checksums, ETags, and last-modified headers should be recorded when supported.
5. Changed source bytes do not automatically imply a promotable dataset change.
6. No public output should update without validation, policy checks, and release-state transition.
7. Staleness should surface as a state, not disappear behind cached map tiles or summaries.

[Back to top](#top)

---

## Maintainer workflow

When adding or revising source documentation:

1. Start with the source role and admissibility question.
2. Check the authority ladder and canon/status register before adding a new document.
3. Put prose standards in `docs/sources/`.
4. Put source descriptor instances in `data/registry/source-descriptors/`.
5. Link the source descriptor to its semantic contract, executable schema, validator, policy, and fixtures.
6. Include at least one valid and one invalid fixture before proposing automation.
7. Mark unresolved rights, sensitivity, owner, cadence, or source-of-record status as `NEEDS VERIFICATION`.
8. Keep live connector activation separate from documentation acceptance.
9. Record rollback/correction expectations before publication.
10. Update this README when the adjacent standards and registries become verified repo reality.

[Back to top](#top)

---

## Verification gates

Before this README is promoted beyond draft:

- [ ] Owner is replaced with a verified team, role, or maintainer group.
- [ ] `policy_label` is replaced with the project-approved label.
- [ ] `doc_id` is replaced with a real KFM document identifier.
- [ ] All relative links resolve in the mounted repository.
- [ ] `SOURCE_DESCRIPTOR_STANDARD.md` exists or the README clearly states its absence.
- [ ] `SOURCE_REFRESH_RULES.md` exists or the README clearly states its absence.
- [ ] `data/registry/source-descriptors/` existence and purpose are verified.
- [ ] Contract/schema/policy/fixture homes are verified against the real repo conventions.
- [ ] README badges still reflect the document’s actual status.
- [ ] Any examples are marked illustrative unless backed by checked-in fixtures.
- [ ] No source instance, raw data, receipt, proof, or release artifact is stored in `docs/sources/`.
- [ ] The repo’s pre-publish documentation checklist passes.

[Back to top](#top)

---

<details>
<summary><strong>Appendix: minimal source descriptor review card</strong></summary>

Use this as a human review card when the executable schema is not yet mounted.

| Field | Required question |
|---|---|
| Source name | What is the source called by its steward or provider? |
| Steward / owner | Who maintains it, and who in KFM reviews it? |
| Source-of-record status | Is it authoritative, mirrored, derived, community-contributed, or discovery-only? |
| Source role | Observation, regulatory record, operational context, modeled surface, documentary object, authority crosswalk, or other? |
| Access method | API, bulk download, archive request, manual acquisition, restricted steward path, or fixture-only? |
| Auth posture | Public, key-based, account-based, steward-restricted, embargoed, or unknown? |
| Rights posture | What license, terms, attribution, redistribution, and automation constraints apply? |
| Sensitivity posture | What exact-location, personal, cultural, species, infrastructure, or legal risks apply? |
| Spatial basis | Native CRS, support, scale, precision, geometry type, extent, and transform burden. |
| Temporal basis | Valid time, issue time, retrieved time, update cadence, expiry, supersession, and freshness window. |
| Normalization target | Which KFM object family may this source feed? |
| Validation checks | What must pass before work, processed, catalog, or published state? |
| Failure handling | What conditions require `DENY`, `ABSTAIN`, `QUARANTINE`, `RESTRICT`, or `NEEDS REVIEW`? |
| Publication intent | Is this intended for public release, steward-only use, internal analysis, or citation support only? |
| Downstream evidence | Which receipts, validation reports, catalog records, proof objects, and EvidenceBundles should be emitted? |

</details>

<details>
<summary><strong>Appendix: common anti-patterns</strong></summary>

- Treating a source as admissible because it has an API.
- Treating a discovery portal as the source of record.
- Treating modeled, observed, regulatory, and documentary sources as interchangeable.
- Publishing source-derived geometry before sensitivity and public precision are reviewed.
- Reusing a source without carrying rights, attribution, and redistribution constraints.
- Running live refresh automation before valid/invalid fixtures exist.
- Letting map layers, search indexes, summaries, or AI outputs cite a source that has no descriptor.
- Moving source instances, receipts, proofs, or release manifests into `docs/sources/`.
- Upgrading `PROPOSED` source guidance to `CONFIRMED` because it is well written.
- Collapsing refresh time, event time, source valid time, and public release time into one timestamp.

</details>
