<!--
KFM_WIKI_SOURCE
page_id: Security-and-Sensitivity
title: Security and Sensitivity
status: PROPOSED wiki source; review required
updated: 2026-08-07
authority: orientation-only; canonical repository evidence and adopted KFM authority outrank this page
source_path: docs/wiki/Security-and-Sensitivity.md
publication_effect: none until separately synchronized to the native GitHub Wiki
-->
# Security and Sensitivity

KFM favors fail-closed behavior when rights, sensitivity, identity, precision, authority, or public consequences are unclear. Public usefulness does not justify exposing protected or harmful detail.

> [!CAUTION]
> Do not post credentials, vulnerabilities, private endpoints, restricted source payloads, living-person private data, DNA/genomic material, exact rare-species or archaeology locations, sacred/cultural knowledge, or critical-infrastructure exposure details in public issues, pull requests, wiki pages, logs, screenshots, or generated receipts.

## Default handling

| Condition | Default response |
|---|---|
| Rights or source terms unknown | Quarantine or deny use/publication |
| Living-person private information | Deny or restrict to a reviewed role |
| DNA or genomic information | Deny public use; require explicit consent and qualified review |
| Rare species or rare plants | Generalize, delay, stage access, or deny exact location |
| Archaeology or sacred/cultural material | Restrict exact locations; require sovereignty/cultural review |
| Critical infrastructure | Remove harmful precision and operational detail |
| Private wells, land, title, or facilities | Review ownership, privacy, and public consequence |
| Security vulnerability | Follow private reporting; do not publish exploit detail |
| Unclear classification | Hold; do not guess a permissive state |

## Transform before delivery

Sensitive information should be transformed before it reaches a public client:

- coordinate generalization or aggregation;
- field removal or categorical replacement;
- delayed or seasonal release;
- role-gated projections;
- minimum-count thresholds;
- redacted evidence summaries;
- public-safe derived geometry;
- source-specific attribution and use restrictions.

A client-side style filter is not an adequate security boundary when the sensitive values are already in the payload.

## Policy, evidence, and review are separate

- Evidence may support a claim and still be unsafe to expose.
- A schema may validate a payload and still permit a policy violation.
- A policy decision may allow a generalized product but not the exact source record.
- A successful test does not replace rights or steward review.
- A release decision must name the public-safe transform and correction/rollback path where material.

## Public-error behavior

Denied and error responses should return safe reason codes and audit references without:

- internal filesystem or database paths;
- source credentials or signed URLs;
- stack traces;
- blocked field values;
- hidden-model prompts or private reasoning;
- detailed sensitivity rules that help locate protected material.

## Reporting a security issue

Use the repository's current [SECURITY.md](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/SECURITY.md). Do not open a public issue for a vulnerability or sensitive exposure unless that policy explicitly directs it.

## Wiki-specific rule

The wiki is public. Publish only orientation material already suitable for public repository documentation. Do not copy internal receipts, denied payloads, exact fixtures, private review notes, or source terms that restrict redistribution.

## Review questions

- Is the source allowed to be used and redistributed in this form?
- Is the subject or location sensitive at the requested precision?
- Is a qualified domain, legal, privacy, cultural, tribal, or security reviewer required?
- Is the transform deterministic and recorded?
- Can the public artifact be corrected, withdrawn, and purged from caches?
- Does the UI reveal withheld content indirectly?
- Does a generated summary exceed what the evidence and policy allow?

## Related roots

- [Security policy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/SECURITY.md)
- [Policy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/policy)
- [Sensitivity doctrine](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/sensitivity.md)
- [Review console](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/apps/review-console)
- [Release decisions](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/release)
