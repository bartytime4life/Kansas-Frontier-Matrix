<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/5e2f6fdc-d4a8-49be-af1f-2cd71868c345
title: Promotion Readiness Checklist
type: checklist
version: v1
status: draft
owners: kfm-core (TBD)
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - ./README.md
  - ../governance/REVIEW_GATES.md
tags: [kfm, quality, promotion, checklist]
[/KFM_META_BLOCK_V2] -->

# Promotion Readiness Checklist

Use this checklist before promoting data/products toward `PUBLISHED`.

## Gate A — Identity & versioning

- [ ] `dataset_id` and `dataset_version_id` are stable and documented.
- [ ] Spec hash is deterministic and captured.
- [ ] Artifact digests are generated and retained.

## Gate B — Licensing & rights

- [ ] License/rights fields are populated and valid.
- [ ] Upstream terms snapshot is retained.
- [ ] Attribution requirements are documented.

## Gate C — Sensitivity & redaction

- [ ] `policy_label` is assigned and justified.
- [ ] Required obligations are defined (redaction/generalization/deny).
- [ ] Sensitive fields/geometry handling is verified.

## Gate D — Catalog triplet

- [ ] DCAT validates.
- [ ] STAC validates.
- [ ] PROV validates.
- [ ] Cross-links resolve across all three catalogs.
- [ ] Evidence references resolve deterministically.

## Gate E — QA thresholds

- [ ] Dataset-specific QA checks were executed.
- [ ] Thresholds were met or quarantine rationale is documented.
- [ ] QA outputs are attached or linked from the promotion record.

## Gate F — Receipt & audit

- [ ] Run receipt captures inputs, tools, hashes, and decisions.
- [ ] Receipt validates against schema.
- [ ] Audit trail append is confirmed.

## Gate G — Release manifest

- [ ] Manifest exists for the release candidate.
- [ ] Manifest references correct artifact digests.
- [ ] Version and timestamp metadata are complete.

## Exceptions (only when necessary)

- [ ] Exception is explicitly documented and time-bounded.
- [ ] Governance/steward approval is linked.
- [ ] Compensating controls and risk notes are included.
