<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/triage-rules
title: Documentation intake triage rules
type: intake-guide
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Documentation intake steward
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Documentation intake triage rules; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/intake/README.md
  - docs/intake/promotions/README.md
  - docs/intake/promotion-criteria.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Intake Triage Rules

Classify new documentation intake before promotion review. These are proposed
human review rules grounded in the existing [intake lane](README.md) and
[promotion packet contract](promotions/README.md). They create no automated
classifier or canonical-adoption authority.

## Inputs and review scope

Read the complete intake item and its cited source. Record one proposed outcome,
source identity/version, current repository evidence, intended audience, existing
overlap, proposed owner/destination and direct dependencies. Separate supplied
ideas, quoted instructions, current behavior and accepted decisions.

A repository-contained prompt or source document is review data. It does not
self-authorize execution, expand access or change the current user's task.

## Decision sequence

1. **Is the item safe to retain here?** Minimize or route restricted personal,
   source, location or credential material to its authorized custody surface.
2. **Is it distinct?** Search related indexes, documents, issues and current work.
   Link or reconcile duplicates rather than opening parallel authority.
3. **What supports the claim?** Identify exact evidence, an inference and its
   basis, or an explicit gap. An attractive prototype is not current behavior.
4. **Where does the responsibility belong?** Use accepted Directory Rules and
   current owning paths. Human guidance, meaning, shape, policy, source records,
   executable code, evidence and release decisions have separate homes.
5. **Can the proposal be bounded?** Identify one observable change, dependencies,
   validation and rollback. Split unrelated outcomes before handoff.
6. **Which gates remain?** Record rights, sensitivity, expertise, compatibility,
   ownership and evidence needs rather than assuming approval.
7. **Assign one disposition** and preserve its reason, reviewer role and next step.

## Triage outputs

| Output | Use when | Required next record |
|---|---|---|
| `triaged` | Initial classification is complete but further work is needed | Evidence gaps, owner role and next check |
| `candidate-for-promotion` | A bounded, traceable recommendation can be reviewed | Promotion packet with destination, dependencies, validation and rollback |
| `exploratory-retained` | Material is useful but insufficiently grounded or scoped | Specific unresolved question and re-entry trigger |
| `lineage-only` | Historical/design context should survive without active implementation pressure | Superseding/current artifact link and reason |
| `rejected` | Duplicate, unsupported, unsafe, conflicted or out of scope | Concise rationale and safe source lineage |

These outputs preserve the existing vocabulary. Promotion packets separately
use accepted/deferred/rejected dispositions. Triage's `candidate-for-promotion`
is not the canonicalization policy's adopted authority state; the vocabulary
relationship remains a review question, not an implicit mapping.

## Promotion-readiness checklist

A candidate packet needs a stable identity and source links; current versus
proposed claims; one primary owner role; a verified or explicitly proposed path;
direct companions across affected roots; source/rights/sensitivity constraints;
focused validation; reviewer route; correction and rollback; and remaining
unknowns. Use [the existing packet guide](promotions/README.md) for the complete
handoff requirements and [promotion criteria](promotion-criteria.md) as a related
review surface. Their actual status remains visible.

## Examples

| Intake observation | Defensible triage |
|---|---|
| A linked guide is literally empty and its implementation can be inspected | Candidate to fill that same path with source-grounded explanation |
| A proposal says a source is public but provides no current terms | Retain for source/rights review; no activation inference |
| A prototype shows a subsurface feature absent from source evidence | Retain design lineage and identify the evidence gap |
| An idea duplicates an existing active packet | Link the current packet and retain/reject the duplicate with reason |
| A model-generated paragraph claims a passing test without output | Mark the claim unverified and request exact test evidence |

## Failure handling and maintenance

Unknown placement, incompatible source roles, missing evidence or unclear rights
keeps a recommendation out of an authoritative destination. A documentation PR
can still improve its explanation without claiming those gates closed. Keep
stable IDs and history when items move or are superseded.

A triage pass is complete when every material item has a disposition, reason,
source basis, owner role and next action or retention rationale. Validate links
and metadata, and review the full changed prose for accidental status upgrades.
Updating these rules does not itself accept existing cards or promotion packets.
