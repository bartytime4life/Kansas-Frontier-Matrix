# Contributing to Kansas Frontier Matrix

Thank you for contributing to **Kansas Frontier Matrix (KFM)**.

KFM is not a generic app, data lake, or map viewer. It is a **governed spatial evidence system**. Contributions must preserve the project’s core operating posture:

- evidence first
- map first and time aware
- fail closed when proof, rights, or policy are incomplete
- authoritative truth kept distinct from derived projections
- public claims must resolve to inspectable evidence or abstain
- documentation treated as a production surface

This guide explains how to contribute without weakening those guarantees.

---

## 1. Non-negotiable contribution rules

### 1.1 Preserve the truth path
Do not introduce shortcuts that bypass the governed lifecycle.

The expected path is:

**Source edge → RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED**

A contribution is not complete just because a transform runs or a UI renders. It is complete when the resulting behavior still fits the governed publication path.

### 1.2 Preserve the trust membrane
No client-visible feature should bypass governed APIs, policy checks, evidence resolution, or release state.

Do not add:

- direct client access to raw stores, operational databases, or internal artifacts
- hidden side channels around policy checks
- uncited “best effort” outputs when evidence is missing

### 1.3 Keep authoritative and derived layers separate
Search indexes, vectors, tiles, graphs, summaries, scene layers, and AI outputs are useful, but they are not automatically authoritative.

If your change introduces a derived surface, cache, index, or synthesis layer, make sure it remains visibly downstream of canonical evidence and publishable release state.

### 1.4 Fail closed
When rights are unclear, sensitivity is unresolved, validation fails, or evidence does not support the claim, the correct behavior is to block, quarantine, narrow scope, deny, or abstain.

Do not replace governed failure with silent fallback.

### 1.5 Treat docs as part of the system
If your change affects runtime behavior, contracts, policy handling, contributor workflow, review flow, evidence semantics, or user-visible trust cues, update documentation in the same change.

---

## 2. Contribution types

KFM welcomes contributions across several lanes:

- documentation and architecture clarification
- contracts, schemas, examples, and invalid fixtures
- source onboarding, dataset descriptors, and ingestion logic
- QA, validation, and verification harnesses
- API, evidence-resolution, and runtime envelope work
- map, story, dossier, review, and Focus Mode surfaces
- policy, governance, redaction, and sensitivity handling
- tests, CI, observability, runbooks, and operational hardening

Contributions are strongest when they tighten governance and implementation at the same time.

---

## 3. Before you start

Before opening a substantial pull request, do the following:

1. Identify the exact problem being solved.
2. State which KFM invariant or workflow the change touches.
3. Name the smallest acceptable scope.
4. Decide what evidence, contracts, tests, and docs must move with it.
5. Decide what a safe rollback would look like.

For non-trivial work, open an issue, discussion, or design note first.

Use **ADRs** for changes that affect:

- storage formats
- API surface changes
- policy boundaries
- model-serving architecture
- canonical data model shifts
- release sequencing that affects governance or migration safety

---

## 4. Truth posture in contributions

KFM benefits from explicit truth labeling when a change includes design reasoning, migration notes, or architecture prose.

Use these labels when precision matters:

- **CONFIRMED** — directly supported by visible project evidence in the current working context
- **PROPOSED** — recommended direction or implementation choice not yet established as live project fact
- **UNKNOWN** — not verified strongly enough to present as fact

Do not smooth unknowns into confident prose.

---

## 5. Pull request expectations

Keep pull requests:

- small enough to review carefully
- reversible where possible
- additive rather than destructive when feasible
- explicit about operational impact

Every non-trivial PR should include:

- purpose and scope
- summary of what changed
- affected invariants, contracts, or workflows
- evidence posture summary where relevant
- tests added or updated
- docs updated, or explicit rationale for no doc changes
- rollback path
- operational notes if runtime behavior changes

If the change affects user-visible surfaces, include screenshots, state diagrams, or interaction notes when useful.

If the change affects a release path, include the relevant proof objects, fixtures, or validation results.

---

## 6. Separation of duty and review boundaries

KFM depends on review boundaries that prevent convenience from overruling governance.

As a default:

- contributors submit changes
- reviewers or stewards validate rights, sensitivity, evidence completeness, and policy fit
- operators manage runtime and deployment concerns
- governance authorities ratify policy-significant exceptions or rule changes

Do not self-approve policy-significant release paths.

That includes changes involving:

- rights posture
- sensitivity handling
- public release state
- policy bundles or reason codes
- evidence-resolution behavior
- AI answer-release rules

---

## 7. Documentation expectations

A behavior-significant change should update the relevant docs in the same PR.

That may include:

- architecture docs
- governance docs
- domain docs
- contracts and examples
- runbooks
- ADRs
- contributor or reviewer workflow docs

If a change alters how something is verified, promoted, published, denied, abstained, corrected, or rolled back, documentation is required.

---

## 8. Contract and schema changes

If your contribution changes a contract, schema, or envelope, include:

- the schema change itself
- at least one valid example
- at least one invalid example when practical
- tests or validators that prove the rule
- versioning notes or migration notes if compatibility is affected

This especially applies to objects such as:

- source descriptors
- ingest receipts
- validation reports
- dataset versions
- catalog closure records
- decision envelopes
- review records
- release manifests
- projection build receipts
- evidence bundles
- runtime response envelopes
- correction notices

Avoid free-text drift in machine-governed decision fields when a controlled vocabulary belongs there.

---

## 9. Source, dataset, and ingestion contributions

If you add or modify a source or dataset path, include the minimum governed intake shape.

A complete source-facing contribution usually needs:

- source registry or descriptor entry
- acquisition method and scope
- rights and terms capture plan
- cadence or snapshot posture
- QA checks
- sensitivity and redaction notes
- canonical transform or normalization plan
- target processed artifacts
- catalog outputs
- sample evidence-resolution path

Raw acquisition must remain reproducible and checksummed.

If rights, provenance, schema quality, or sensitivity are unresolved, the contribution should preserve a **QUARANTINE** path instead of pretending the source is publication-ready.

---

## 10. Story, evidence, and Focus Mode changes

### 10.1 Story work
Stories are governed narrative artifacts, not freeform copy.

A story-related contribution should preserve:

- stable story identity or versioning
- EvidenceRef-backed citations
- review state
- publication state
- correction path instead of silent overwrite

### 10.2 Evidence surfaces
If a claim is visible, its route back to evidence should remain visible.

Do not weaken:

- evidence drawer reachability
- citation clarity
- dataset version visibility
- rights and policy cues
- lineage or freshness cues

### 10.3 Focus Mode / AI work
Any Focus or model-enabled change must preserve:

- governed retrieval
- policy pre-checks
- evidence bundling
- citation verification
- answer / abstain / deny / error behavior
- audit linkage

A model is a language surface, not an independent source of truth.

---

## 11. Testing baseline

At minimum, add or update the tests that prove your change did not weaken KFM’s core guarantees.

Depending on the change, that may include:

- docs lint and link checks
- schema validation
- catalog validation
- policy tests
- unit tests
- integration tests
- reproducibility checks
- evidence-resolution tests
- runtime negative tests
- UI and accessibility tests
- smoke tests for published surfaces

Examples of especially important checks:

- broken citations lead to abstain or block, not fabricated support
- restricted assets do not leak through errors or partial metadata
- generated artifacts remain reproducible where required
- map and evidence surfaces remain keyboard reachable
- public UI does not imply more certainty than the evidence supports

---

## 12. Security, rights, and sensitivity

Contributors must not:

- commit secrets
- weaken least-privilege boundaries
- expose restricted or sensitive data in examples or fixtures
- publish exact sensitive locations when policy requires generalization or suppression
- merge modeled outputs into observed truth without explicit labeling

If a source has uncertain reuse terms, preserve the rights investigation record and treat publication as blocked until resolved.

For culturally sensitive, sovereignty-sensitive, archival, oral-history, archaeology, biodiversity, or exact-location material, err toward review, redaction, or restricted handling.

---

## 13. Accessibility and calm failure

Accessibility is part of the trust contract.

If your contribution changes a user-facing surface, it should preserve or improve:

- keyboard navigation
- focus order
- readable labels and headings
- screen-reader clarity
- reduced-motion handling where relevant
- evidence visibility under normal and failure states

A governed system should fail calmly and visibly.

Do not hide:

- stale state
- missing evidence
- denied access
- unresolved citations
- partial coverage

---

## 14. Suggested PR checklist

Use this as a starting checklist in pull requests:

- [ ] Scope is clear and bounded
- [ ] The change preserves truth path and trust membrane rules
- [ ] Rights, sensitivity, and policy implications were reviewed
- [ ] Contracts/schemas/examples were updated if needed
- [ ] Tests were added or updated
- [ ] Docs were updated, or rationale for no doc change is given
- [ ] Rollback path is stated
- [ ] User-visible trust cues remain intact
- [ ] No direct bypass of governed evidence or policy paths was introduced

---

## 15. Definition of done

A contribution is done when:

- another reviewer can understand what changed and why
- the project’s governed path still holds
- tests prove the intended behavior
- docs and contracts are aligned with the implementation
- required review boundaries were honored
- rollback or correction is not an afterthought

In KFM, “works on my machine” is not enough.

---

## 16. Need help?

Open an issue or discussion when:

- the right policy class is unclear
- a source’s rights posture is ambiguous
- a schema or envelope boundary is uncertain
- a proposed feature might weaken evidence visibility
- a dataset should enter QUARANTINE instead of normal promotion
- a change may require an ADR

When in doubt, choose the path that keeps provenance, policy, and public trust explicit.

---

## 17. Closing principle

KFM is strongest when contributions make the system more inspectable, more reproducible, and more governable.

Prefer one reliable evidence path over five impressive shortcuts.
