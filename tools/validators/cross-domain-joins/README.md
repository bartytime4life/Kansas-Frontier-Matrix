<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-cross-domain-joins-readme
title: tools/validators/cross-domain-joins README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-architecture-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; cross-domain-validator; joins; four-invariants; fail-closed
owning_root: tools/
responsibility: proposed cross-domain join validator lane for ownership, source-role, sensitivity, EvidenceBundle, lifecycle, policy, release, and public-surface checks across multi-domain relation candidates
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../../../docs/architecture/cross-domain/cross-lane-relations.md
  - ../../../docs/architecture/cross-domain/source-role-anti-collapse.md
  - ../../../docs/architecture/cross-domain/shared-kernel.md
  - ../../../docs/architecture/cross-domain/trust-membrane.md
  - ../../../docs/architecture/cross-domain/multi-domain-placement.md
  - ../../../docs/architecture/ecology-cross-domain.md
  - ../../../contracts/crosswalks/
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../data/proofs/evidence_bundle/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README documents a proposed validator lane. It does not confirm executable files."
  - "Cross-domain joins must preserve ownership, source role, sensitivity, and EvidenceBundle support. Missing or unresolved join support must fail closed."
  - "Validators enforce declared contracts, schemas, and policy. They do not define domain meaning, create EvidenceBundles, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/cross-domain-joins

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-cross--domain--joins-informational)
![invariants](https://img.shields.io/badge/invariants-4-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/cross-domain-joins/` is the proposed validator lane for multi-domain join candidates. It checks the four KFM cross-lane invariants: ownership preserved, source role preserved, sensitivity preserved, and EvidenceBundle support resolved.

---

## Purpose

`tools/validators/cross-domain-joins/` exists for validator logic that applies to any candidate relation joining two or more KFM domains.

The durable KFM question for this lane is:

> Does a cross-domain join preserve each side's owning domain, source role, sensitivity posture, evidence support, lifecycle state, policy posture, release references, and public-surface limits?

The answer should be a deterministic validation result. It should not create domain truth, relation truth, EvidenceBundles, policy decisions, release decisions, graph truth, map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/cross-domain-joins/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Cross-lane invariant doctrine | **CONFIRMED in repo evidence / draft** | Architecture docs define four invariants for every cross-lane relation. |
| Promotion/runtime placement | **CONFIRMED in repo evidence / draft** | Doctrine says gates C, E, G, OPA, validators, governed API, and governed AI must preserve the invariants. |
| Contract/schema paths | **PROPOSED / NEEDS VERIFICATION** | Concrete join schemas, policy bundles, fixtures, and relation contracts must be verified before implementation claims. |
| CI/release wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove CI, release gates, or public runtime checks are wired. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Cross-domain join validator entrypoints | `tools/validators/cross-domain-joins/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-lane join doctrine | `docs/architecture/cross-domain/cross-lane-relations.md` |
| Domain meaning | each owning domain's `docs/domains/<domain>/` and `contracts/domains/<domain>/` lanes |
| Crosswalk/relation contracts | `contracts/crosswalks/` or accepted cross-domain contract homes |
| Machine schemas | `schemas/contracts/v1/` or accepted schema homes |
| Policy rules | `policy/` or accepted domain/cross-domain policy homes |
| EvidenceBundles and proof support | `data/proofs/evidence_bundle/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Published public-safe artifacts | `data/published/` |
| Tests and fixtures | `tests/validators/cross-domain-joins/` or accepted test convention |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it enforces declared cross-domain join invariants and delegates domain meaning to owning lanes.
- **NEEDS VERIFICATION:** exact executable names, relation schemas, fixtures, policy bundles, source registry shape, release integration, and CI wiring.
- **DENY:** using this folder as a domain contract home, schema home, policy home, source registry, evidence store, lifecycle data store, release record store, graph authority, public runtime surface, or domain-meaning authority.

[Back to top](#top)

---

## Four invariant checks

Every cross-domain join must preserve all four invariants.

| Invariant | Validator expectation | Fail condition |
|---|---|---|
| Ownership preserved | Each side keeps its owning domain and object identity. | Join silently rebinds one side into the other domain. |
| Source role preserved | Each side carries observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic role as applicable. | Join collapses or drops role labels. |
| Sensitivity preserved | Output inherits the most restrictive applicable posture. | Join downgrades sensitivity or treats aggregation as automatic public release. |
| EvidenceBundle support | Each consequential side resolves to evidence support before public exposure. | EvidenceRef is missing, unresolved, or only resolves on one side. |

A join that fails any invariant is not valid for public KFM composition.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/cross-domain-joins/` include checks that:

- validate relation tuples that join two or more domain-owned objects;
- require `left.domain`, `right.domain`, relation type, source role, sensitivity, lifecycle state, and evidence references;
- reject ownership drift or relation tuples filed under only one participating domain when a cross-domain home is required;
- reject source-role collapse across observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic records;
- reject sensitivity downgrades across joined records;
- require EvidenceBundle resolution on every consequential side before public exposure;
- require policy posture, review state, release references, rollback targets, and correction paths for public-bound joins;
- check that graph, catalog, map, API, and AI outputs remain downstream carriers rather than join truth.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/cross-domain-joins/` | Correct home |
|---|---|
| Domain contracts | `contracts/domains/<domain>/` |
| Cross-domain relation contracts | `contracts/crosswalks/` or accepted cross-domain contract home |
| Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| EvidenceBundles or proof records | `data/proofs/` |
| Receipts | `data/receipts/` |
| Release records | `release/` |
| Catalog records | `data/catalog/` |
| Graph/triplet records | `data/triplets/` |
| Published artifacts | `data/published/` |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Cross-domain validation posture

This validator lane must fail closed, deny, abstain, or route to review when a join candidate:

- omits an owning domain on either side;
- collapses source roles into a single synthetic role;
- joins public context with restricted context and publishes the result as public;
- has evidence on one side but not the other;
- joins candidate or synthetic records into released truth without promotion support;
- points public surfaces at RAW, WORK, QUARANTINE, or unresolved candidate data;
- lets graph, catalog, map, API, or AI surfaces become sovereign truth;
- lacks release, correction, rollback, or review support where required.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `CROSS_DOMAIN_JOIN_PASS` | Configured cross-domain join checks passed. |
| `CROSS_DOMAIN_JOIN_FAIL` | Configured checks failed. |
| `OWNERSHIP_COLLAPSE` | Join rebinds or obscures an owning domain. |
| `SOURCE_ROLE_COLLAPSE` | Join collapses, drops, or fabricates source role. |
| `SENSITIVITY_DOWNGRADE` | Join lowers sensitivity or bypasses restrictive posture. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or EvidenceBundle pointer is absent. |
| `EVIDENCE_UNRESOLVED` | Evidence pointer does not resolve on one or more sides. |
| `POLICY_POSTURE_MISSING` | Required policy/sensitivity/rights/source-role posture is absent. |
| `RELEASE_REFERENCE_MISSING` | Required release-state pointer is absent. |
| `ROLLBACK_REFERENCE_MISSING` | Required correction or rollback path is absent. |
| `PUBLIC_BOUNDARY_VIOLATION` | Candidate is not safe for public/governed exposure as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/cross-domain-joins/
├── README.md
├── test_cross_domain_join_validators.py
└── fixtures/
    ├── valid_two_domain_join/
    ├── missing_owner_domain/
    ├── source_role_collapse/
    ├── sensitivity_downgrade/
    ├── missing_evidence_ref/
    ├── unresolved_evidence_one_side/
    ├── public_join_to_unreleased_candidate_denied/
    └── graph_projection_as_truth_denied/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/cross-domain-joins
```

```bash
python tools/validators/cross-domain-joins/validate_cross_domain_join.py --fixtures --dry-run
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_cross_domain_join.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared contracts and schemas rather than defining shape locally.
- [ ] Validator reads declared policy posture rather than defining policy locally.
- [ ] Each side of a join keeps its owning domain and object identity.
- [ ] Source roles remain explicit on every side.
- [ ] Output sensitivity uses the most restrictive applicable posture.
- [ ] Evidence support resolves on every consequential side before public exposure.
- [ ] Public-bound joins include review, release, correction, and rollback support where required.
- [ ] Graph, catalog, map, API, and AI outputs are downstream carriers, not sovereign truth.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify cross-domain relation schemas, policy bundles, fixtures, validator entrypoints, release references, and CI wiring before promoting this lane beyond draft. |
