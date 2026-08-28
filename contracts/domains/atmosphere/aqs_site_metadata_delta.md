# Synthetic EPA AQS Site-Metadata Delta Contract

**Status:** PROPOSED fixture-only implementation contract  
**Owning domain:** Atmosphere / Air  
**Artifact family:** `AqsSiteMetadataDeltaReport`  
**Source basis:** *New Ideas 4-2-26.pdf* — semantic monitor-metadata change classification; *KFM Briefing-to-System Integration Architecture* — missing-record source semantics and false-clear prevention  
**Directory Rules basis:** domain meaning belongs under `contracts/domains/atmosphere/`; the deterministic watcher-shaped helper lives under the established `tools/ingest/` review-signal boundary; common missing-record meaning remains owned by `contracts/source/source_record_absence_assessment.md`.

## Purpose

Define a deterministic comparison between two frozen synthetic EPA AQS site-metadata snapshots. The report distinguishes lifecycle, spatial, method, parameter, POC, low-impact metadata, and current-snapshot absence signals so reviewers can preserve network continuity and time-series comparability.

This contract does not select or call a live AQS endpoint, resolve KDHE notices, create an `EvidenceBundle`, admit a source, update a catalog, issue air-quality guidance, promote data, or publish a layer.

## Snapshot profile

Every input uses `kfm.aqs-site-metadata.synthetic.v1`, declares `fixture_only: true`, and references `fixture://source/epa-aqs`. A bounded site record preserves:

- synthetic AQS-style `site_id`;
- site name and lifecycle status;
- coordinates used only for deterministic distance comparison;
- parameter and method identity;
- parameter occurrence code (`poc`);
- capture time and source-revision metadata.

`content_hash` binds the stable canonical site inventory. `retrieval_hash` also binds capture time and source revision. Retrieval-only changes therefore remain auditable without being misrepresented as a source-surface change.

## Missing-record rule

A previously present site that is absent from the current snapshot is emitted as `SITE_ABSENT_FROM_CURRENT_SNAPSHOT`, never as `SITE_REMOVED`. The change carries:

- `absence_assessment_required: true`; and
- `absence_contract_ref: kfm:contract:source-record-absence-assessment:v1`.

The comparator returns `ABSTAIN` with `SOURCE_RECORD_ABSENCE_REQUIRES_ASSESSMENT`. It does not assume that the source is a healthy, complete authoritative snapshot, retain or clear state, create a transition candidate, delete history, or authorize public use. A later adapter-specific assessment must establish source mode, health, completeness, parse status, chronology, evidence, and domain authority before any transition is proposed.

Version `1.1.0` reports use this fail-closed rule. The schema still recognizes version `1.0.0` and its legacy `SITE_REMOVED` token only so historical fixture reports remain readable; version `1.1.0` explicitly rejects that token.

## Semantic change classes

| Change | Impact | Result |
|---|---:|---|
| New site | MEDIUM | `PROPOSED_WORK_RECORD` |
| Absent from current snapshot | HIGH | `ABSTAIN`; common absence assessment required |
| Active/inactive/retired transition | HIGH | `ABSTAIN` pending review |
| Coordinate movement greater than 250 m | HIGH | `ABSTAIN` pending spatial review |
| Smaller coordinate correction | LOW | `PROPOSED_WORK_RECORD` |
| Method code or method name change | HIGH | `ABSTAIN` pending comparability review |
| Parameter code change | HIGH | `ABSTAIN` pending comparability review |
| POC reassignment | HIGH | `ABSTAIN` pending continuity review |
| Site-name correction | LOW | `PROPOSED_WORK_RECORD` |

The 250 m location threshold is a frozen fixture-profile rule adapted from the source packet. It is not adopted live policy.

## Finite outcomes

- `NO_MATERIAL_CHANGE` — stable canonical site content.
- `PROPOSED_WORK_RECORD` — valid low- or medium-impact source-surface change.
- `ABSTAIN` — high-impact change or source-record absence requiring source/domain steward review.
- `ERROR` — unsafe or invalid input, inconsistent hashes/classification, or report-schema failure.

## Trust boundary

- Reports contain synthetic site IDs, change types, changed-field names, and rounded distance only; raw coordinates are not echoed.
- A watcher report is a review signal, not a `SourceRecordAbsenceAssessment`, `PolicyDecision`, `EvidenceBundle`, `ReleaseManifest`, or publication decision.
- Source admission, source-state mutation, clearance, promotion, release, publication, and public use are always false or outside this object.
- No network access, lifecycle write, air-quality assessment, or health guidance occurs.

## Rollback

Revert this contract/schema/helper/fixture/test/workflow/receipt update to restore the prior fixture profile. Retain historical reports and receipts; do not rewrite them to erase the legacy token. If a later adapter emits stable absence-assessment IDs, preserve them through correction or supersession rather than destructive deletion.
