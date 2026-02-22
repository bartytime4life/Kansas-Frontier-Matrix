# Kansas Frontier Matrix (KFM) — CHANGELOG
One place to track *what changed*, *why it changed*, and *what it impacts* across code, data, governance, and UX.

**Status:** Template (fill in as releases land) • **Owners:** @<team-or-handle> • **Last updated:** 2026-02-22

Quick links: [Unreleased](#unreleased) · [Versioning Policy](#versioning-policy) · [Entry Template](#entry-template) · [Release Checklist](#release-checklist)

---

## How to Use This Changelog
- Add changes to **[Unreleased]** as you merge work.
- On release, move items from **[Unreleased]** into a new version section (with an ISO date).
- Prefer entries that answer: **what changed**, **who is affected**, **migration/rollback**, and **evidence/provenance impact** (when relevant).

Change type keywords:
- **Added** · **Changed** · **Deprecated** · **Removed** · **Fixed** · **Security**

---

## Versioning Policy
> Keep this section accurate; update it if the project’s versioning conventions change.

**(PROPOSED) Code & APIs — SemVer:** `MAJOR.MINOR.PATCH`
- **MAJOR**: breaking API/contract changes
- **MINOR**: backward-compatible additions
- **PATCH**: backward-compatible fixes

**(PROPOSED) Data artifacts — DatasetVersion IDs:** use deterministic IDs, and record:
- dataset name + version identifier
- temporal extent (event/valid time when applicable)
- checksums/hashes + provenance pointers
- promotion zone movement (RAW → WORK/QUARANTINE → PROCESSED → PUBLISHED)

**(PROPOSED) Governance/policy schema:** version policy labels & redaction rules independently when they change behavior.

---

## Release Flow (Conceptual)
~~~mermaid
flowchart LR
  A[Dev changes merged] --> B[Unreleased updated]
  B --> C[Release candidate]
  C --> D{Promotion gates pass?}
  D -- no --> E[Fix / rollback / quarantine]
  D -- yes --> F[Tag + publish release]
  F --> G[Post-release verification]
~~~

---

## Unreleased
> Changes staged for the next release. Keep entries small and link to PRs/issues.

### Added
- _TBD_

### Changed
- _TBD_

### Deprecated
- _TBD_

### Removed
- _TBD_

### Fixed
- _TBD_

### Security
- _TBD_

---

## [0.1.0] — TBD (First Release)
> Reserve for the first tagged release. Move finalized items here.

### Added
- _TBD_

### Changed
- _TBD_

### Fixed
- _TBD_

---

## Entry Template
Copy/paste for each notable change (especially anything that alters behavior, governance, or public narratives):

### <Change Type>: <Short title>
- **What:** <1–2 sentences>
- **Why:** <reason / user value / risk addressed>
- **Impact:** <who/what breaks or benefits>
- **Migration:** <steps, if needed>
- **Rollback:** <how to revert safely>
- **Evidence/Provenance:** <new/changed EvidenceRefs, datasets, receipts, or citations>
- **Links:** <PR/issue/docs>

---

## Release Checklist
Use this when cutting a release (fail-closed if any required gate is unknown).

- [ ] Changelog updated; **[Unreleased]** emptied into version section
- [ ] Version tagged and traceable to commit SHA
- [ ] CI green: unit/integration/e2e (as applicable)
- [ ] Security checks run (deps, secrets scanning, code scanning)
- [ ] Data changes (if any) include:
  - [ ] schema + sample validated
  - [ ] checksums recorded
  - [ ] provenance captured
  - [ ] promotion zone transitions logged
- [ ] Governance changes (if any) include:
  - [ ] policy label deltas documented
  - [ ] redaction obligations reviewed
  - [ ] access/permissions matrix updated (if impacted)
- [ ] UX/Story changes (if any) include:
  - [ ] citations/evidence links verified
  - [ ] time semantics (event/valid/transaction time) not broken
- [ ] Post-release smoke test complete

---

## Notes
- Prefer concrete dates (`YYYY-MM-DD`) over “today/yesterday”.
- Don’t record secrets, private locations, or sensitive operational details here—summarize and link to controlled artifacts instead.

[Back to top](#kansas-frontier-matrix-kfm--changelog)
