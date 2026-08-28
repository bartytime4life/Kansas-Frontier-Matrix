# FluencyLoop review-packet source map

**Intake status:** exploratory source interpretation  
**Selected repository slice:** deterministic implementation review packet  
**Upstream revision inspected:** `baokhang83/fluencyloop@fe3ccf6dada2c36057a3d65b84ca150bd9b9c96e`  
**KFM base inspected:** `bartytime4life/Kansas-Frontier-Matrix@14b9608addcf6cac80adaa0a836182f7a6e47806`  
**Authority:** none

## Question

Which remaining FluencyLoop idea can improve KFM without importing its agent
packaging, storing conversational traces, inferring intent from code, or
collapsing KFM's existing evidence and review boundaries?

## Sources inspected

### Upstream FluencyLoop

- `README.md`
- `plugins/fluencyloop/templates/design.md`
- `plugins/fluencyloop/templates/session.md`
- `claude-skills/review/SKILL.md`
- `plugins/fluencyloop/scripts/bash/slice-context.sh`
- `LICENSE` (Apache License 2.0)

### Existing KFM implementation

- `docs/intake/exploratory/fluencyloop-implementation-decision-source-map.md`
- `docs/intake/exploratory/fluencyloop-change-context-source-map.md`
- `contracts/governance/implementation_decision_record.md`
- `contracts/governance/implementation_change_context.md`
- `schemas/contracts/v1/governance/implementation_decision_record.schema.json`
- `schemas/contracts/v1/governance/implementation_change_context.schema.json`
- `tools/validators/governance/validate_implementation_decision_record.py`
- `tools/validators/governance/validate_implementation_change_context.py`
- `tools/validators/governance/implementation_change_context_model.py`
- `.github/PULL_REQUEST_TEMPLATE.md`

## Upstream pattern

FluencyLoop's review stage assembles a reviewer-facing view from branch scope
and recorded session decisions. It emphasizes decisions that deserve review
attention, exposes unexplained drift, preserves the distinction between known
and undocumented rationale, and prepares a pull-request view instead of leaving
fragments disconnected.

Its slice helper also derives mechanical change statistics and a decision
attention signal from Git state. The upstream implementation includes raw diff
content because its purpose is to support an interactive coding loop.

## KFM fit analysis

KFM had already adapted the two safe prerequisites before this slice:

1. `ImplementationDecisionRecord` stores explicitly authored implementation
   choice, rationale, alternatives, support, reviewer questions, and rollback;
2. `ImplementationChangeContext` binds a committed base/head range to
   value-minimized path, status, count, binary, root, and signal metadata.

The earlier KFM source maps explicitly deferred a deterministic reviewer view
that consumes those validated objects. No equivalent exact-bound packet,
validator, renderer, branch, or pull request was found at the inspected base.

A generic constitution, design template, session journal, or replacement PR
template would duplicate stronger KFM authority surfaces. Reading raw hunks to
reconstruct intent would weaken KFM's no-invention and privacy boundaries.

## Selected adaptation

Implement an original KFM-native `ImplementationReviewPacket` renderer that:

- validates each existing input with its canonical validator;
- requires exact equality between context decision references and supplied
  decision IDs;
- requires each decision to bind to the context content identity;
- rejects decision scope outside the context changed/previous-path set;
- propagates `HOLD` and `ERROR` without upgrading them;
- puts held and less-confirmed decision records first;
- renders change metadata, declared rationale, alternatives, questions,
  support, and rollback in deterministic order;
- lists changed destination paths not covered by a decision as informational;
- omits raw diff, changed-file content, local input paths, prompts, hidden
  reasoning, and person profiles; and
- performs no network or write action.

The implementation is conceptually informed by FluencyLoop but contains no
copied upstream program text. KFM's contracts, finding vocabulary, finite
outcomes, content boundary, and authority model control the adaptation.

## Assay matrix

| Candidate | Value | KFM fit | Disposition |
|---|---|---|---|
| Deterministic review packet over branch scope and decisions | High | Closes a named gap between two existing profiles | **Implement** |
| Living project constitution | Medium | Duplicates doctrine, ADR, contracts, policy, and directory authority | Reject |
| Free-form session journal | Medium | Risks conversational/private-reasoning retention and post-hoc narrative | Reject |
| Raw-diff decision inference | Medium | Violates metadata-only context boundary and can invent rationale | Reject |
| Replace KFM pull-request template | Low | Would erase required human scope, trust, validation, and rollback fields | Reject |
| Automatic PR mutation/comment posting | Medium | Adds credentials and write authority beyond the core deterministic tool | Defer |
| Historical backfill of rationale | Medium | Must preserve `DRAFT` / `NEEDS_VERIFICATION` and requires human confirmation | Defer |

## Dependency closure

The selected slice consists of:

- this pinned source map;
- `contracts/governance/implementation_review_packet.md`;
- deterministic packet validator and Markdown renderer;
- exact polarity fixtures;
- focused no-network tests;
- a read-only GitHub Actions workflow; and
- a generated authoring receipt binding the final artifact bytes.

It does not modify the two existing input profiles, their schemas, validators,
workflows, or receipts.

## Trust boundary

This map establishes design provenance only. It does not authenticate upstream
claims, adopt upstream policy, prove the implementation correct, approve the
change, grant merge authority, or create evidence, promotion, release,
deployment, publication, or public-use authority.
