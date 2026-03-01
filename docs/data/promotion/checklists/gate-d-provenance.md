<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/0b1f25b8-9d42-4c94-acde-3f0b9f1a1a6a
title: Gate D — Provenance and Lineage
type: standard
version: v1
status: draft
owners: kfm-platform-data-governance (TODO: confirm)
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - docs/data/promotion/README.md (TODO: confirm path)
  - docs/data/promotion/promotion-contract.md (TODO: confirm path)
  - docs/data/promotion/checklists/gate-a-identity.md (TODO: confirm path)
  - docs/data/promotion/checklists/gate-b-licensing.md (TODO: confirm path)
  - docs/data/promotion/checklists/gate-c-sensitivity.md (TODO: confirm path)
tags: [kfm, promotion, checklist, gate-d, provenance, lineage, prov, run-receipt, audit]
notes:
  - This checklist is fail-closed by design.
  - Naming note: some drafts label “Gate D” as catalog triplet validation (DCAT+STAC+PROV) and “Gate F” as run receipt + audit record. This checklist covers provenance/lineage requirements spanning PROV + run receipts and their cross-links.
[/KFM_META_BLOCK_V2] -->

# Gate D — Provenance and Lineage
**Purpose:** block promotion unless a dataset version has **auditable lineage** (PROV + run receipt) that **cross-links** with catalogs and can be resolved by EvidenceRefs **without guessing**.

![status](https://img.shields.io/badge/status-draft-yellow)
![gate](https://img.shields.io/badge/promotion-gate%20D-blue)
![posture](https://img.shields.io/badge/posture-fail--closed-red)

---

## Navigation
- [Scope](#scope)
- [Pass criteria](#pass-criteria)
- [Required artifacts](#required-artifacts)
- [Checklist](#checklist)
- [CI assertions](#ci-assertions)
- [Deny codes and remediation](#deny-codes-and-remediation)
- [Minimum verification steps](#minimum-verification-steps)
- [Appendix](#appendix)
- [Back to top](#gate-d--provenance-and-lineage)

---

## Scope
This gate applies when promoting a **DatasetVersion** into runtime surfaces (PUBLISHED), and is concerned with **lineage/provenance completeness and resolvability**:

- Provenance artifacts exist (PROV bundle + run receipt) and are immutable/identified by digest.
- Provenance is **linked** into the catalog triplet (DCAT/STAC/PROV).
- Evidence references that rely on provenance (**prov://…**, run IDs) resolve via the evidence resolver (or equivalent) **without manual interpretation**.

### Prerequisites
This gate assumes the following are already satisfied (or are being satisfied in the same PR/workflow):
- Identity & versioning gate (DatasetVersion ID, spec_hash determinism, artifact digests)
- Licensing/rights gate (license captured; terms snapshotted)
- Sensitivity/policy gate (policy_label + obligations applied)
- QA gate (domain checks and thresholds)

> **NOTE**
> This gate is intentionally conservative: if lineage is missing or ambiguous, **promotion must be blocked**.

---

## What “provenance” means in KFM
KFM treats catalogs and provenance as **contract surfaces** between pipelines and runtime:
- **DCAT** describes dataset-level metadata and distributions.
- **STAC** describes spatiotemporal extents and assets.
- **PROV** describes lineage: which inputs, tools, parameters, and agents produced which outputs — including environment capture (container digest, git commit, params digest).  

The key requirement: **DCAT + STAC + PROV are cross-linked** so EvidenceRefs resolve deterministically.

---

## Pass criteria
Gate D passes if and only if all of the following are true:

1. **PROV lineage exists** for the dataset version (per-run provenance, not hand-written narrative).
2. **Run receipt exists** for the same run/dataset version, capturing inputs, outputs, environment, validation outcome, and policy decision reference.
3. **Cross-links are complete**:
   - STAC ↔ DCAT links exist.
   - STAC/DCAT ↔ PROV links exist (run_id / prov bundle reference).
4. **EvidenceRefs resolve**:
   - `prov://…` (or run_id → prov bundle) resolves to lineage.
   - Any STAC/DCAT references used by the UI, Story Nodes, or Focus Mode resolve without guessing.
5. **Integrity checks pass**:
   - Artifact digests match across receipt, catalogs, and provenance.
   - No broken links/hrefs for assets referenced by catalogs.
6. **Policy traceability exists**:
   - The run receipt references a policy decision record (decision_id), and provenance includes the agent(s) responsible for the run and any required approvals.

---

## Required artifacts

| Artifact | Required | Why it exists | Minimum content (normative) | Notes |
|---|---:|---|---|---|
| PROV bundle (JSON-LD) | ✅ | Standards-based lineage: Entities, Activities, Agents; used/generated; policy decision references; environment capture | `prov:Activity` per run, `prov:Entity` per artifact, `prov:Agent` for pipeline + approvals; `prov:used` + `prov:wasGeneratedBy`; environment digests/commit/params; `kfm:policy_decision` refs | Path is repo-convention-dependent |
| Run receipt (JSON) | ✅ | Typed run record for CI gating + audit | run_id, actor, operation, dataset_version_id, inputs (uri+digest), outputs (uri+digest), environment (container_digest, git_commit, params_digest), validation status/report digest, policy decision_id, created_at | Treated as first-class artifact |
| Link map / linkcheck report | ✅ | Proves cross-links are resolvable | “all links resolve” output; must include failures | Can be machine-generated in CI |
| (Optional) OpenLineage event(s) | ◻️ | Observability/telemetry stream for lineage tooling | job/run IDs, inputs/outputs, execution state | Useful but not a substitute for PROV |
| (Optional) build provenance + attestations | ◻️ | Supply-chain evidence attached to builds/PRs | cosign/sigstore verification results + signed attestations | Recommended for hardened posture |

---

## Checklist

### 1) Existence and identity
- [ ] A **PROV bundle** exists for the run that produced this DatasetVersion.
- [ ] A **run receipt** exists for the same run/dataset_version_id.
- [ ] PROV + receipt are referenced (directly or indirectly) by the promotion manifest/release metadata for this DatasetVersion.
- [ ] PROV and receipt are stored in an immutable or append-only manner (repo history, content-addressed store, or both).

### 2) Schema/profile validation
- [ ] PROV bundle validates under the project’s PROV profile (JSON-LD shape / required fields).
- [ ] Run receipt validates under the project’s run_receipt schema.
- [ ] (If used) OpenLineage event schema validates.

### 3) Cross-link completeness (triplet stitching)
- [ ] DCAT ↔ STAC cross-links exist (dataset/distribution ↔ collection/item/distribution).
- [ ] STAC items include a link/reference to PROV lineage or run receipt (run_id / prov locator).
- [ ] DCAT includes provenance linkage (`prov:wasGeneratedBy` or equivalent) to the run/prov bundle.
- [ ] EvidenceRef schemes used by the system (at minimum: dcat, stac, prov, doc; graph if enabled) resolve for this dataset version.

### 4) Digest and integrity invariants
- [ ] Every processed artifact referenced in STAC assets includes a **digest** (sha256 or project-approved).
- [ ] Digest values match across:
  - [ ] run receipt outputs
  - [ ] PROV Entities for artifacts
  - [ ] STAC asset checksum/digest fields
  - [ ] promotion/release manifest (if present)
- [ ] No broken asset `href`s; linkcheck passes.

### 5) Policy traceability
- [ ] Run receipt references a **policy decision** record (`decision_id` or equivalent).
- [ ] PROV references the pipeline agent/principal that executed the run.
- [ ] If steward approval is required (by policy), approvals are captured and referenced (as Agents and/or approval records linked from provenance/manifest).

### 6) Idempotency and reproducibility
- [ ] The run is replayable in principle: environment capture includes at least container digest + git commit + params digest.
- [ ] Provenance includes enough upstream identifiers to avoid “mystery inputs” (e.g., upstream URI and digest; optional ETag/Last-Modified).
- [ ] Re-running validation is idempotent: repeated CI runs do not create ambiguous duplicate lineage for the same dataset_version_id.

---

## CI assertions
**Goal:** make Gate D machine-checkable and merge-blocking.

### Suggested CI jobs (names are illustrative)
- `validate:run-receipt`
  - Validate receipt JSON against schema
  - Fail if required fields missing
- `validate:prov`
  - Validate PROV JSON-LD bundle (shape/profile)
  - Fail if Activities/Entities/Agents or required edges missing
- `validate:triplet-links`
  - Validate DCAT/STAC/PROV and cross-links
  - Fail if any link is broken or any required link missing
- `verify:evidence-resolve`
  - Run a small suite of EvidenceRef resolution tests against fixtures
  - Fail if resolution requires guessing

> **TIP**
> Deny messages must be explainable: name the missing field, violated constraint, and remediation. Keep policy bundles versioned and reviewed.

---

## Deny codes and remediation
| Deny code | Trigger | How to fix |
|---|---|---|
| `PROV_MISSING` | No PROV bundle found for promoted DatasetVersion | Emit PROV during pipeline; ensure it is stored and referenced |
| `RECEIPT_MISSING` | No run receipt found | Ensure every run writes a receipt artifact; add CI check to enforce |
| `PROV_INVALID` | PROV fails validation/profile | Fill required Activity/Entity/Agent fields; ensure used/generated edges exist |
| `RECEIPT_INVALID` | Receipt schema validation fails | Add missing fields (env digests, inputs/outputs digests, policy ref) |
| `LINK_BROKEN` | Any catalog/prov linkcheck fails | Fix hrefs and cross-links; regenerate catalogs if needed |
| `DIGEST_MISMATCH` | Digest differs across receipt/prov/stac/manifest | Recompute digests; ensure single source of truth and consistent propagation |
| `EVIDENCE_UNRESOLVABLE` | EvidenceRef cannot be resolved deterministically | Add missing IDs/links; ensure resolver mapping exists |

---

## Minimum verification steps
These steps are the smallest practical set to confirm the gate is enforced end-to-end:

1. **Happy path:** run the full promotion workflow for a known dataset version and confirm:
   - receipt validates
   - PROV validates
   - linkcheck passes
   - EvidenceRefs resolve
2. **Fail path:** delete (or rename) the PROV bundle for a fixture dataset version and confirm CI fails with `PROV_MISSING`.
3. **Integrity path:** corrupt one digest in a fixture STAC asset (or receipt output) and confirm CI fails with `DIGEST_MISMATCH`.
4. **Resolution path:** remove a required cross-link (STAC → PROV or DCAT → STAC) and confirm CI fails with `LINK_BROKEN` or `EVIDENCE_UNRESOLVABLE`.

---

## Appendix

### A. Minimal run receipt template (illustrative)
```json
{
  "run_id": "kfm://run/<timestamp>.<suffix>",
  "dataset_version_id": "<dataset_version_id>",
  "actor": { "principal": "svc:<name>", "role": "pipeline" },
  "operation": "ingest+publish",
  "inputs": [{ "uri": "<raw-or-upstream-uri>", "digest": "sha256:<...>" }],
  "outputs": [{ "uri": "<processed-uri>", "digest": "sha256:<...>", "media_type": "<...>" }],
  "environment": {
    "container_digest": "sha256:<...>",
    "git_commit": "<sha>",
    "params_digest": "sha256:<...>"
  },
  "validation": { "status": "pass|fail", "report_digest": "sha256:<...>" },
  "policy": { "decision_id": "kfm://policy_decision/<id>" },
  "created_at": "<iso8601>"
}
```

### B. Minimal PROV bundle expectations (illustrative)
- **Activity**: one per run (`prov:Activity`)
- **Entities**: one per artifact (`prov:Entity`) including digest and path/URI
- **Agents**: pipeline principal + approvers (`prov:Agent`)
- **Edges**:
  - `prov:used` (Activity → input Entities)
  - `prov:wasGeneratedBy` (output Entities → Activity)
  - `prov:wasAssociatedWith` (Activity → Agent)
- **KFM fields**:
  - dataset_version_id
  - policy decision references
  - environment capture references (container, commit, params digest)

---

<a name="back-to-top"></a>
**Back to top:** [Gate D — Provenance and Lineage](#gate-d--provenance-and-lineage)
