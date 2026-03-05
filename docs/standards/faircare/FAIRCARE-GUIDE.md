<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/a6f0ec21-c33f-4e31-a5f2-c189b53707d4
title: FAIR + CARE Guide for KFM
type: standard
version: v1
status: draft
owners: ["KFM AI Governance Board", "KFM Data Stewards"]
created: 2026-03-05
updated: 2026-03-05
policy_label: public
related:
  - ../../ai/MODEL_CARDS_INDEX.md
  - ../../data/LICENSING_AND_ATTRIBUTION.md
  - ../../governance/ROOT_GOVERNANCE_CHARTER.md
tags: [kfm, fair, care, governance, ai]
notes:
  - Operationalizes FAIR and CARE principles for datasets and model cards.
[/KFM_META_BLOCK_V2] -->

# FAIR + CARE Guide for KFM

Use this guide when onboarding data, publishing model cards, or approving downstream use.

## FAIR requirements

- **Findable:** every dataset/model must have stable IDs and searchable metadata.
- **Accessible:** access pathways must be explicit and policy-labeled.
- **Interoperable:** use approved schemas and vocabularies (DCAT/STAC/PROV where applicable).
- **Reusable:** rights, lineage, and quality constraints must be documented.

## CARE requirements

- **Collective Benefit:** document who benefits and who may be burdened.
- **Authority to Control:** indicate governance rights for communities represented in the data.
- **Responsibility:** define steward contacts, review cadence, and incident response obligations.
- **Ethics:** record known harms, mitigations, and prohibited uses.

## Required fields for model cards

```yaml
faircare:
  fair:
    findable_id: "kfm.model.focus-mode-transformer-v3"
    metadata_index: "docs/ai/MODEL_CARDS_INDEX.md"
  care:
    authority_to_control: "required-review-for-sensitive-regions"
    collective_benefit_statement: "supports public safety and planning"
    ethics_constraints:
      - "must not generate precise sensitive coordinates"
      - "must abstain if provenance unresolved"
```

## Review rubric

| Check | Pass criteria |
|---|---|
| FAIR completeness | All four FAIR dimensions documented with implementation evidence |
| CARE accountability | Named steward + review date + escalation path |
| Harm analysis | Concrete misuse cases and mitigations listed |
| Policy alignment | obligations map to runtime-enforceable controls |

## CI automation suggestion

Use a docs-linter step that fails if model cards lack FAIR+CARE sections:

```bash
rg -n --glob 'mcp/model_cards/*.md' '^faircare:'
```

