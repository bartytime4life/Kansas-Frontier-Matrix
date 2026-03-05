<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/4c76907b-c526-4b73-a0ea-4a720f4f8c7a
title: Governance Standard (Root)
type: standard
version: v1
status: draft
owners: ["KFM Standards WG", "KFM Governance Council"]
created: 2026-03-05
updated: 2026-03-05
policy_label: public
related:
  - ../../governance/ROOT_GOVERNANCE.md
  - ../../governance/ROOT_GOVERNANCE_CHARTER.md
  - ../../quality/SECURITY_BASELINE.md
tags: [kfm, standards, governance]
notes:
  - Standards-layer summary of governance requirements consumed by AI and pipeline docs.
[/KFM_META_BLOCK_V2] -->

# Governance Standard (Root)

This standard defines what implementation surfaces MUST satisfy to be considered governance-compliant in KFM.

## Normative requirements

1. Services MUST enforce policy decisions at request time (deny-by-default).
2. Pipelines MUST produce promotion evidence before publish actions.
3. Runtime and CI policy evaluations MUST use equivalent policy bundle versions.
4. All externally surfaced claims MUST include evidence references or abstain.

## Enforcement matrix

| Surface | Required control | Test strategy |
|---|---|---|
| API policy point | request-time allow/deny + obligations | contract tests with deny fixtures |
| Pipeline promotion | gate orchestration + immutable receipt | integration tests on fixture datasets |
| UI rendering | evidence link presence + abstain fallback | component tests + snapshot checks |
| Agent automation | PR-first behavior, no merge permission | dry-run and permission-scoped e2e |

## Implementation checklist

- [ ] Policy package digest pinned in build metadata.
- [ ] Gate report schema validated in CI.
- [ ] Evidence reference resolution tested against broken-link fixtures.
- [ ] Incident rollback runbook references current gate IDs.

## Example compliance assertion (YAML)

```yaml
service: kfm-governed-api
policy:
  bundle_digest: sha256:80149b22f3f75fb5d5e3a2a6408c5bcacdc2f84828681e22e163ce9abeb2dd5d
  mode: deny_by_default
controls:
  - id: api-pep-01
    description: "all read endpoints require policy decision"
    status: pass
  - id: evidence-ux-02
    description: "responses include evidence_refs when claim-bearing"
    status: pass
```

