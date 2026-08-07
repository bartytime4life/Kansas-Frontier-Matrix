# AQS Site-Metadata Delta Fixture Comparator

Deterministically compares two frozen synthetic EPA AQS site-metadata snapshots and emits a review-only semantic delta report.

```bash
python tools/ingest/aqs_watch/aqs_site_delta.py \
  --prior tests/ingest/aqs_watch/fixtures/prior.json \
  --current tests/ingest/aqs_watch/fixtures/current_unchanged.json
```

`NO_MATERIAL_CHANGE` exits `0`. Review signals and errors exit `1`.

A site that disappears from the current fixture is reported as `SITE_ABSENT_FROM_CURRENT_SNAPSHOT`, not `SITE_REMOVED`. The report binds that signal to `kfm:contract:source-record-absence-assessment:v1` and returns `ABSTAIN`; it does not infer source completeness, delete history, clear prior state, or create a transition candidate.

The helper performs no network access, source admission, lifecycle write, evidence resolution, policy decision, promotion, release, publication, or air-quality guidance.
