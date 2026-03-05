<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/c5ff504e-122d-4e74-9b89-04d7ed920464
title: PARTIAL — Governance callouts
type: standard
version: v1
status: draft
owners: KFM
created: 2026-03-04
updated: 2026-03-04
policy_label: public
related: []
tags: [kfm, templates, partials, governance]
notes: ["Reusable callout blocks for governance, policy, and evidence discipline. Intended for inclusion in other docs."]
[/KFM_META_BLOCK_V2] -->

<!--
PURPOSE
  A small library of reusable, copy/paste-able callouts that reinforce KFM governance requirements.
WHERE IT FITS
  docs/templates/_partials/ (include these blocks in design docs, runbooks, PR templates, etc.)
ACCEPTABLE INPUTS
  Markdown documents that need short governance reminders or non-negotiable policy statements.
EXCLUSIONS
  This file is NOT the authoritative governance policy. It is a reusable *presentation layer* for policy.
-->

<!-- KFM_CALLOUT: NON_NEGOTIABLES -->
> [!CAUTION]
> **KFM governance — non‑negotiables (CONFIRMED)**  
> 1) **Trust membrane:** UI and external clients never access databases directly — all access is via the **governed API + policy boundary**.  
> 2) **Fail‑closed policy** on every request (data, Story Nodes, AI).  
> 3) **Dataset promotion gates:** **Raw → Work → Processed**; promotion requires **checksums + STAC/DCAT/PROV catalogs**.  
> 4) **Focus Mode:** **cite or abstain**; every answer produces an **audit reference**.

<!-- KFM_CALLOUT: FAIL_CLOSED_POSTURE -->
> [!CAUTION]
> **Fail‑closed posture (CONFIRMED)**  
> If policy, rights, or citations are unclear, **block promotion/publishing** and return policy‑safe errors. Do not weaken gates “temporarily.”

<!-- KFM_CALLOUT: TRUST_MEMBRANE_MEANING -->
> [!IMPORTANT]
> **Trust membrane (CONFIRMED — meaning in practice)**  
> - Clients never access storage/DB directly.  
> - Backend logic uses repository interfaces; governed APIs apply **policy, redaction, and logging**.  
> - UI can display policy badges/notices, but **UI never makes policy decisions**.

<!-- KFM_CALLOUT: POLICY_AS_CODE_SHARED_SEMANTICS -->
> [!IMPORTANT]
> **Policy‑as‑code (CONFIRMED): CI and runtime must agree**  
> KFM requires the **same policy semantics** in CI and runtime (or at minimum the same fixtures and outcomes). Otherwise, CI guarantees are meaningless.

<!-- KFM_CALLOUT: EVIDENCE_DISCIPLINE -->
> [!IMPORTANT]
> **Evidence discipline (CONFIRMED)**  
> - Label meaningful claims as **CONFIRMED / PROPOSED / UNKNOWN**.  
> - If **UNKNOWN**, list the **smallest verification steps** required to make it **CONFIRMED** (and stop there).  
> - Treat “latest/current/most recent” as unstable: include **explicit dates** and verify against a trusted source.  
> - If evidence is missing or restricted: **abstain**, or provide a **redacted/generalized** answer and record the policy reason.

<!-- KFM_CALLOUT: SENSITIVITY_HANDLING -->
> [!WARNING]
> **Sensitivity handling (CONFIRMED)**  
> Some data must be treated as sensitive (e.g., private ownership, **precise archaeological site locations**, certain health/public‑safety indicators).  
> Sensitivity is handled by:  
> - **policy labels** at dataset/record/field level  
> - **derivative datasets** with explicit **redaction provenance**  
> - **fail‑closed** policy checks

<!-- KFM_CALLOUT: SENSITIVITY_CLASSES -->
> [!CAUTION]
> **Sensitivity classes (CONFIRMED — recommended)**  
> - **Public:** safe to publish without redaction.  
> - **Restricted:** requires role‑based access (e.g., parcel ownership).  
> - **Sensitive‑location:** coordinates must be **generalized or suppressed** (e.g., archaeology, sensitive species).  
> - **Aggregate‑only:** only publish above thresholds (e.g., health/crime small counts).

<!-- KFM_CALLOUT: SENSITIVITY_DEFAULT_RULES -->
> [!CAUTION]
> **Sensitivity default rules (PROPOSED — aligned to KFM posture)**  
> - Default deny for **sensitive‑location** and **restricted** datasets.  
> - If any public representation is allowed, produce a separate **public_generalized** dataset version.  
> - Never leak restricted metadata in 403/404 responses.  
> - Do not embed precise coordinates in Story Nodes or Focus Mode outputs unless policy explicitly allows.

<!-- KFM_CALLOUT: REDACTION_FIRST_CLASS -->
> [!IMPORTANT]
> **Redaction is a first‑class transformation (CONFIRMED)**  
> Redaction must be recorded in **PROV**. The **raw dataset remains immutable**; the redacted output is a **separate DatasetVersion** (often a separate dataset_id) with a documented policy label.

<!-- KFM_CALLOUT: CI_POLICY_REGRESSION_SUITE -->
> [!WARNING]
> **CI policy regression suite (CONFIRMED)**  
> - **Golden queries** that previously leaked restricted fields must fail tests forever (**non‑regression**).  
> - **Negative tests:** ensure sensitive‑location layers cannot be returned at high precision to unauthorized roles.  
> - **Field‑level tests:** verify owner names, health small counts, and exact archaeological coordinates are redacted.  
> - **Audit integrity tests:** every API response must include an **audit reference** and **evidence bundle hash**.

<!-- KFM_CALLOUT: RIGHTS_AND_LICENSING -->
> [!WARNING]
> **Licensing & rights enforcement (CONFIRMED)**  
> Key principle: **online availability does not equal permission to reuse**.  
> Operational rules:  
> - Promotion gate requires **license + rights holder** for every distribution.  
> - “Metadata‑only reference” mode is allowed (catalog without mirroring) when rights do not allow rehosting.  
> - Exports should include **attribution and license text** automatically.  
> - Story publishing must block when rights are unclear for included media.

<!-- KFM_CALLOUT: OPERATIONS_SLOS -->
> [!NOTE]
> **Operations (CONFIRMED): freshness SLOs + monitoring**  
> Operational discipline prevents data sources from silently going stale. Each dataset carries a **freshness SLO** (examples: Mesonet < 1 hour, Storm Events < 30 days; static archives exempt).  
> Alerting triggers when SLOs are violated.

<!-- KFM_CALLOUT: OBSERVABILITY_SIGNALS -->
> [!NOTE]
> **Observability signals (CONFIRMED — minimum)**  
> - Ingest runs: success/fail, duration, rows/bytes processed, retry counts  
> - Freshness: last successful run timestamp per dataset + expected cadence  
> - Quality drift: distribution checks, missingness, geometry errors  
> - API: request latency, cache hit rate, policy denials, evidence resolution failures  
> - Storage: object store growth, PostGIS index health, search index lag

<!--
SOURCE TRACE (for editors; not rendered)
- KFM Comprehensive Data Source Integration Blueprint v1.0 (2026-02-12):
  - “Boss mode summary (non-negotiables)”
  - “Governance, FAIR/CARE, and sensitivity handling”
  - “CI policy regression suite”
  - “Operations, SLOs, and monitoring”
- KFM — Definitive Design & Governance Guide (vNext) + Ultimate Blueprint (Draft) excerpts (Source Snapshots bundle):
  - “Policy-as-code architecture (shared CI and runtime semantics)”
  - “Sensitivity default rules” (explicitly labeled PROPOSED in-source)
  - “Licensing and rights enforcement”
  - “Non-negotiable invariants” table (trust membrane, repository interfaces, cite-or-abstain)
-->
