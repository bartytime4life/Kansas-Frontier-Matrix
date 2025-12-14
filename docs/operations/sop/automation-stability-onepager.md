---
title: "🛠️ KFM — Day‑to‑Day Automation Stability SOP (Schedulers · SemVer in STAC/DCAT · SLO/Alerts · Rollback)"
path: "docs/operations/sop/automation-stability-onepager.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability & FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "SOP"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "day-to-day-automation-stability"
audience:
  - "Reliability Engineering"
  - "Data Engineering"
  - "Catalog Engineering"
  - "Governance Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Reliability Council · FAIR+CARE Council"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

commit_sha: "<latest-commit-hash>"
semantic_document_id: "kfm-sop-automation-stability-onepager"
doc_uuid: "urn:kfm:ops:sop:automation-stability:v11.2.6"
event_source_id: "ledger:ops/sop/automation-stability"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

<div align="center">

# 🛠️ **KFM — Day‑to‑Day Automation Stability SOP**
`docs/operations/sop/automation-stability-onepager.md`

**Purpose**  
A one‑page, daily‑use playbook to keep KFM automation reliable:
**Schedulers**, **SemVer embedded in STAC/DCAT**, **minimal SLO/alert tiers**, and **immutable rollback**.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-blue" />

</div>

---

## 📘 Overview

This SOP standardizes:

- **Schedulers** (when/how jobs run),
- **Dataset SemVer** embedded in **STAC/DCAT** metadata (what changed & compatibility),
- **Minimal SLO/alert tiers** (OpenTelemetry → Prometheus → Pager/Ticket), and
- **Immutable snapshot rollback** (time‑travel / `replacedBy` + governed republish).

This plugs into KFM governance (STAC/DCAT/PROV, SBOM/SLSA attestations) and complements saga/promotion choreography by focusing on the operational steps you run every day.

---

## 🗓️ 1) Scheduler Choices & Daily Patterns

Use **simple, observable, back‑pressure‑aware** schedulers with explicit contracts.

### A. Default scheduler set

- **Intra‑day micro‑batches (every 15–30 min)** for streaming-adjacent feeds (air quality, sensors).
- **Hourly** for external APIs with rate limits; include **jitter (±5 min)** to avoid thundering herds.
- **Nightly (02:00–04:00 UTC)** for heavy ETL (spatial joins, re-tiling, embeddings refresh).
- **Weekly (Sun 05:00 UTC)** for reconciliations (dedup, referential integrity checks, lineage compaction).
- **Monthly (1st 06:00 UTC)** for cold‑tier compaction, catalog reindex, long‑horizon QA.

### B. Operational patterns

- **Idempotent tasks only**: reruns do not corrupt state; writes are replace‑by‑version.
- **Write‑ahead logs (WAL) + retry/replay**: persist intent; bound retries (e.g., 3x, exponential backoff).
- **Rate‑limit guards**: shared token bucket per provider; fail closed with friendly backoff.
- **Backfill windows** are explicit (`from_ts`, `to_ts`) and recorded in PROV.
- **Circuit breakers**: if error budget at risk (see §3), degrade gracefully (skip noncritical steps).

### C. Minimal contracts (per job)

- `inputs`: immutable URIs + checksums.
- `outputs`: versioned URIs (`dataset@MAJOR.MINOR.PATCH/partition/...`).
- `timeout_s`: hard cap; fail fast → alert (Tier B or Tier A depending on criticality).
- `sla`: expected wall‑clock; `sla_miss_action`: degrade, page, or ticket.
- `lineage_ref`: PROV‑O JSON‑LD path.

---

## 🧾 2) Dataset SemVer Mapping in STAC/DCAT (Enforced)

Every dataset MUST carry **SemVer** reflecting compatibility. Enforce via CI schema‑lint.

### A. Version bumps (SemVer)

- **MAJOR**: breaking schema change (field removed/renamed, CRS change, semantics differ).
- **MINOR**: backward‑compatible additions (new optional fields, new assets/bands).
- **PATCH**: data corrections/quality fixes without schema/semantics change.

### B. Where to put it

**STAC**

- `version`: `"MAJOR.MINOR.PATCH"`
- `kfm:compatibility`: `"backward-compatible" | "breaking"`
- `links[]`: use `"rel": "predecessor-version"` and `"rel": "successor-version"`
- `properties.kfm:replacedBy`: URI when superseded

**DCAT**

- `dct:hasVersion` and `adms:versionNotes`
- `dcat:previousVersion` / `dct:isReplacedBy`

**PROV**

- `prov:wasRevisionOf` and commit/attestation refs.

### C. CI enforcement

Lint that:

- Schema diffs ↔ SemVer bump type match.
- **MAJOR** requires migration notes and deprecation window.
- **PATCH** prohibits field removals or meaning changes.

Reject publish if:

- Missing `digest` (checksum), `license`, or `governance_ref`.
- `replacedBy` points to a non‑existent or un‑governed artifact.

---

## 🚦 3) Minimal SLOs & Alert Tiers (Otel → Prom → Pager/Ticket)

Keep it tiny, objective, and budget‑based.

### A. Core SLOs (per pipeline)

- **Availability** (job success ratio): target **99.0%** rolling 30d.
- **Freshness** (data lag): **p95 ≤ target_lag** (domain‑set; e.g., sensors ≤ 30 min, daily ETL ≤ 24 h).
- **Quality pass rate** (Great Expectations / rule deck): **p99 ≥ 99.5%**.
- **Cost/Energy guard** (optional): upper bound per run; alert on p95 breach 3x.

### B. Error budgets (30d)

Availability EB = `1 - SLO`. Spend EB before paging humans. Auto‑degrade first.

### C. Alert tiers

- **Tier A (Page)**: threatens SLO immediately
  - consecutive **2** hard failures for critical jobs, or freshness p95 > 2× target for **>2 hours**
  - action: on‑call page, create incident record, start runbook
- **Tier B (Ticket)**: chronic but non‑urgent
  - availability dip consuming **>50%** monthly EB or quality pass rate p99 < target for **24 h**
  - action: auto‑ticket with context; assign within 24 h
- **Tier C (Digest)**: hygiene & trends
  - weekly drift report (latency, cost, cardinality), no paging

### D. Telemetry wiring

Instrument jobs with **OpenTelemetry** spans/metrics:

- `kfm.job.duration_s`
- `kfm.job.success{job=,version=}`
- `kfm.data.freshness_s{dataset=}`
- `kfm.quality.pass_ratio`
- `kfm.energy.kwh`
- `kfm.cost.usd`

Export to **Prometheus/Mimir**.

Rules:

- alerts defined declaratively per pipeline (checked into repo)
- cardinality budgets enforced; drop high‑cardinality labels at source

---

## 🧯 4) Immutable Snapshot Rollback (Time‑Travel · replacedBy · Republish)

A safe, 5‑minute recipe to revert a dataset or pipeline release.

### A. When to roll back

- Tier A alerts persist **>30 min** or critical data corruption confirmed.

### B. Snapshot source

Use an **immutable object store path** pinned by content digest:

- `s3://kfm/immutable/datasets/<dataset>/<MAJOR.MINOR.PATCH>/...`

Verify SBOM + SLSA attestation and checksum before promotion.

### C. Steps

1. **Freeze current**: mark live version with `properties.kfm:replacedBy` → the **target rollback version** (semantic downgrade).
2. **Promote snapshot**: atomically repoint catalog indexes and API manifest to the target version.
3. **Republish catalogs**:
   - STAC: update `links` (`successor-version`/`predecessor-version`) and write a rollback note.
   - DCAT: set `dct:isReplacedBy` on bad version; `dcat:previousVersion` on the restored live.
   - PROV: emit `prov:invalidated` for bad artifact and `prov:wasDerivedFrom` for restored.
4. **Warm caches** (tiles/embeddings) for top queries.
5. **Post‑verify**: run minimal quality & freshness smoke tests.
6. **Announce**: post incident update; open follow‑up ticket for root cause.

### D. Guardrails

- Never mutate the bytes of a published artifact. **Only change pointers.**
- Rollback MUST itself produce governance artifacts (note, attestation, checksums).

---

## ✅ 5) Daily Operator Checklist (10 minutes)

- [ ] Review Tier A/B alerts; execute rollback if criteria met.
- [ ] Scan freshness dashboard: top 5 datasets vs target lag.
- [ ] Inspect quality failures: confirm SemVer alignment (patch vs minor/major).
- [ ] Check cardinality & cost digests; prune noisy labels/jobs.
- [ ] Approve promotion PRs only with valid SemVer, diffs, and attestations.

---

## 🗃️ 6) Files, Paths & Contracts (KFM)

- **Schedulers & rules**: `.github/workflows/`, `infra/schedules/`, `configs/pipelines/*.yaml`
- **Alerting**: `infra/alerts/prometheus/*.rules.yaml` (CI‑linted)
- **Catalogs**: `data/stac/**`, `data/dcat/**` (schema‑linted)
- **Lineage/PROV**: `.github/lineage/**` per job (single‑file emission)
- **Governance**: `docs/standards/**`, `docs/patterns/**`, `docs/operations/**`
- **Snapshots**: `s3://kfm/immutable/...` (digest‑addressed)

---

## ⚖ 7) Notes on Governance & Ethics

- FAIR+CARE: document any access/sovereignty constraints in catalog metadata before promotion.
- NHPA §304‑sensitive: ensure rollback does not expose hidden locations; access controls MUST follow the snapshot.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial one‑page SOP covering schedulers, SemVer enforcement, SLO tiers, and immutable rollback. |

---

<div align="center">

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅ Back to Index](../../README.md) ·
[🏗 Data Architecture](../../architecture/data/README.md) ·
[🏛️ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
