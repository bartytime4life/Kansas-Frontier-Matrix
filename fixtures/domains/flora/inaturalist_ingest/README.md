<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixtures/flora/inaturalist-ingest
title: Synthetic iNaturalist Plant Captures
type: fixture-guide
version: v0.1.0
status: proposed; fixture-first; no-network; non-writing
owners: OWNER_TBD — Flora steward · iNaturalist source steward · Rights and sensitivity reviewers · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public-metadata; private-source-candidates; no-public-coordinates
owning_root: fixtures/
responsibility: describe sealed plant-query source packets and privacy checks
truth_posture: CONFIRMED bounded supplied-page replay; PROPOSED candidate profile; NEEDS VERIFICATION cross-domain source admission, human review and downstream use
[/KFM_META_BLOCK_V2] -->

# Synthetic iNaturalist Plant Captures

Three packets seal exact supplied capture-envelope text, its SHA-256 and the full
expected held candidate. Observation, observer and leaf-taxon IDs, names, logins,
coordinates, times and private-profile markers are invented. The Plantae root ID
47126 is the documented provider query filter; no live observations are included.

- `complete.json`: three observations across two pages. Open source geometry,
  randomized obscured geometry and private withheld geometry stay distinct.
  Noncommercial terms, needs-ID grade, unresolved rights and unknown plant lineage
  retain flags or quarantine. Two records are quarantined; all three remain held.
- `count-drift.json`: same records with a changed remaining count on the second
  page. The capture stays incomplete; no rows are silently dropped.
- `empty.json`: a short zero-count first page, with coverage unestablished.

Deliberate profile/email/bio/top-level markers occur only in original synthetic
input. Expected candidates omit them, retain minimized ID/login attribution and
carry separate original/minimized byte identities. This targeted minimization is
not broad redaction. Use the [runbook](../../../../docs/runbooks/inaturalist-fixture-ingest.md).
Golden changes require review; no source admission, public-use or taxonomy approval
is inferred from passing them.
