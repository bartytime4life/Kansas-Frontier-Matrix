# Synthetic EPA AQS Site-Metadata Delta Contract

**Status:** PROPOSED fixture-only implementation contract  
**Owning domain:** Atmosphere / Air  
**Artifact family:** `AqsSiteMetadataDeltaReport`  
**Source basis:** *New Ideas 4-2-26.pdf* — semantic monitor-metadata change classification  
**Directory Rules basis:** domain meaning belongs under `contracts/domains/atmosphere/`; the deterministic watcher-shaped helper lives under the established `tools/ingest/` review-signal boundary.

## Purpose

Define a deterministic comparison between two frozen synthetic EPA AQS site-metadata snapshots. The report distinguishes lifecycle, spatial, method, parameter, POC, and low-impact metadata changes so reviewers can preserve network continuity and time-series comparability.

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

## Semantic change classes

| Change | Impact | Result |
|---|---:|---|
| New site | MEDIUM | `PROPOSED_WORK_RECORD` |
| Removed site | HIGH | `ABSTAIN` pending review |
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
- `ABSTAIN` — valid high-impact change requiring source/domain steward review.
- `ERROR` — unsafe or invalid input, inconsistent hashes/classification, or report-schema failure.

## Trust boundary

- Reports contain synthetic site IDs, change types, changed-field names, and rounded distance only; raw coordinates are not echoed.
- A watcher report is a review signal, not a `PolicyDecision`, `EvidenceBundle`, `ReleaseManifest`, or publication decision.
- Source admission, promotion, release, and publication are always false.
- No network access, lifecycle write, air-quality assessment, or health guidance occurs.

## Rollback

The slice is additive. Removing its contract, schema, helper, fixtures, tests, workflow, and generated authoring receipt restores prior repository behavior without data or release migration.
