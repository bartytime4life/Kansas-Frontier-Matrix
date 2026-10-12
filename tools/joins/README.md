<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-joins-readme
title: tools/joins README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-domain-stewards-plus-policy-reviewer
created: 2026-07-07
updated: 2026-07-07
policy_label: public; tooling-boundary; derived-join-review; no-publication
owning_root: tools/
responsibility: proposed deterministic join helper boundary for cross-lane candidate joins, anti-collapse checks, and reviewer handoff reports
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/architecture/people-place-joins.md
  - ../../docs/architecture/sensitivity.md
  - ../../docs/architecture/sensitivity-tiers.md
  - ../../docs/domains/hazards/SOURCE_ROLE_MATRIX.md
  - ../../docs/domains/people-dna-land/ARCHITECTURE.md
  - ../../docs/domains/people-dna-land/SENSITIVITY.md
  - ../../docs/domains/hydrology/BOUNDARY.md
  - ../../docs/domains/flora/RIGHTS_AND_SENSITIVITY.md
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
  - ../../data/registry/sources/
  - ../../data/processed/
  - ../../data/catalog/
  - ../../data/triplets/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../release/
notes:
  - "This README defines a proposed join tooling boundary, not a confirmed implementation."
  - "A KFM join is a derived claim candidate, not a database convenience join and not truth by itself."
  - "Join helpers may compute deterministic candidate links, evidence references, source-role checks, sensitivity inheritance, and reviewer handoff reports; they must not publish, promote, create EvidenceBundles, decide identity truth, or weaken input policy."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/joins

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-deterministic--join--helpers-informational)
![authority](https://img.shields.io/badge/authority-review--candidate--only-blueviolet)
![publication](https://img.shields.io/badge/publication-denied-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/joins/` is the proposed tooling lane for deterministic, reviewable KFM join helpers. It may compute candidate cross-lane links and anti-collapse reports, but it is not a source registry, not a canonical identity resolver, not a graph truth store, not a policy engine, not a catalog/proof/release root, and not a publication path.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Authority boundary](#authority-boundary)
- [Join posture](#join-posture)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Governed join rules](#governed-join-rules)
- [Candidate join families](#candidate-join-families)
- [Standard finite outcomes](#standard-finite-outcomes)
- [Standard report envelope](#standard-report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/joins/` exists to hold durable, repo-wide helper code for deterministic KFM join support.

A helper in this lane may compare already-governed records, compute candidate links, emit confidence and reason codes, check source-role compatibility, inherit sensitivity posture, and produce reviewer handoff reports. It exists to make cross-lane joins inspectable and reproducible.

The durable KFM question for this lane is:

> Can these two or more governed records be proposed as a join candidate without collapsing source roles, weakening sensitivity, bypassing EvidenceBundle requirements, or implying publication?

The answer should be a bounded candidate report. It should never be a final join truth, catalog closure, graph projection of record, public API payload, or release decision.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/joins/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Join helper executable code | **PROPOSED-to-create / NEEDS VERIFICATION** | No script or package name is claimed as implemented by this README. |
| `tools/` root authority | **CONFIRMED in repo evidence** | `tools/` owns durable executable support; policy, contracts, schemas, data, and release authority live elsewhere. |
| People-place join architecture | **CONFIRMED in repo evidence / draft** | Join architecture treats a join as a derived claim that must preserve evidence, policy, source role, and sensitivity. |
| Source-role anti-collapse doctrine | **CONFIRMED in repo evidence / draft applications** | Source role is first-class; roles fail closed when conflated. |
| Join output as publication | **DENY here** | A helper report cannot publish or promote. |
| Join output as EvidenceBundle | **DENY here** | Helpers may reference evidence inputs, but EvidenceBundle creation/closure lives outside this lane. |
| Join output as identity truth | **DENY here** | Helpers may propose candidates, not canonical identity decisions. |
| Join output as policy decision | **DENY here** | Helpers may report policy inputs and inherited sensitivity, not decide policy. |

> [!IMPORTANT]
> `tools/joins/` is a helper lane. A join candidate is a derived assertion requiring evidence, validation, policy review, and release controls before any public use.

[Back to top](#top)

---

## Authority boundary

`tools/joins/` inherits the `tools/` root boundary:

- `tools/` owns executable support and deterministic helpers.
- `contracts/` owns object meaning.
- `schemas/` owns field shape.
- `policy/` owns admissibility, sensitivity, rights, and release decisions.
- `data/registry/sources/` owns source identity and source-role truth.
- `data/processed/` owns validated processed records.
- `data/catalog/` and `data/triplets/` own catalog and graph projection records.
- `data/receipts/` and `data/proofs/` own trust artifacts.
- `release/` owns release manifests, rollback targets, correction state, and publication decisions.

Safe interpretation for this path:

- **CONFIRMED:** the README exists at `tools/joins/README.md`.
- **PROPOSED:** deterministic join helper code may live here if it is report-oriented, fixture-tested, source-role-aware, and unable to publish.
- **NEEDS VERIFICATION:** whether future join helpers should be split by family, for example `people_place/`, `spatial_overlay/`, `temporal_overlap/`, or `source_crosswalk/`.
- **DENY:** any use of this folder as source registry, canonical identity store, EvidenceBundle store, graph truth store, public API, or release authority.

[Back to top](#top)

---

## Join posture

A KFM join is not merely a SQL join or spatial overlay. It is a derived claim candidate about a relationship between governed records.

Examples:

- a person assertion linked to a residence event and settlement;
- a storm event joined to a county/time window;
- a rare plant occurrence candidate joined to a generalized ecoregion;
- a hydrology observation joined to a watershed or reach;
- a road segment joined to a county or historical route context;
- a source record joined to a source descriptor and EvidenceRef;
- a county-year aggregate joined to a Focus Mode panel as aggregate context only.

Every join helper must keep four questions visible:

1. **What is being joined?** Object identifiers, source descriptors, temporal scope, geometry scope, and source role.
2. **Why is the join plausible?** Deterministic rule, exact key, normalized key, spatial predicate, temporal overlap, crosswalk, or reviewed mapping.
3. **What can the join not say?** Role, sensitivity, confidence, and release limits.
4. **What downstream review is required?** Validation, EvidenceBundle resolution, PolicyDecision, ReviewRecord, catalog closure, release manifest, and rollback path where applicable.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/joins/` include:

- deterministic exact-key join helpers;
- source crosswalk candidate helpers;
- spatial predicate candidate helpers;
- temporal overlap candidate helpers;
- event-first people-place join candidate helpers;
- source-role compatibility checks;
- sensitivity inheritance checks;
- aggregation guard checks;
- geometry precision and redaction-readiness checks;
- join confidence and reason-code calculators;
- duplicate candidate detection helpers;
- candidate join report emitters;
- reviewer handoff generators;
- no-network fixture adapters for tests.

A helper belongs here only when it is:

- deterministic;
- read-only or dry-run by default;
- explicit about input records and output reports;
- explicit about source descriptor references;
- explicit about source-role inheritance;
- explicit about temporal and spatial scope;
- unable to publish or promote;
- unable to create EvidenceBundles, PolicyDecisions, or ReleaseManifests;
- tested with synthetic or public-safe fixtures;
- conservative when rights, sensitivity, identity, source-role, or geometry precision is unclear.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/joins/` | Correct home | Reason |
|---|---|---|
| Source descriptors | `data/registry/sources/` | Source identity and role truth live in the registry. |
| Contracts | `contracts/` | Object meaning belongs in contracts. |
| JSON Schemas | `schemas/` | Field shape belongs in schemas. |
| Policy rules | `policy/` | Admissibility and release decisions live outside tooling. |
| Raw source captures | `data/raw/` | RAW is a lifecycle state. |
| Quarantine holds | `data/quarantine/` | Holds are lifecycle artifacts. |
| Processed joined records of record | `data/processed/` | Validated records are data, not tool code. |
| Catalog records | `data/catalog/` | Catalog closure is not helper code. |
| Triplet/graph records | `data/triplets/` or accepted graph root | Graph projection is downstream of validation and catalog closure. |
| EvidenceBundles | `data/proofs/` or accepted evidence/proof root | Evidence closure is outside this helper lane. |
| Receipts | `data/receipts/` | Receipts are trust artifacts, not tools. |
| Release manifests / rollback cards | `release/` | Release authority is separate. |
| Public API payloads or UI behavior | governed app/release surfaces | Public clients use governed APIs and released artifacts only. |
| Tests | `tests/joins/` or existing test convention | Tests prove this lane; they are not the lane itself. |

[Back to top](#top)

---

## Governed join rules

All join helpers must preserve these rules.

### 1. Join output is a candidate

A helper may emit a `JoinCandidateReport`. It must not emit a public record or final graph edge.

### 2. Evidence comes first

Every consequential join must be traceable back to source descriptors and EvidenceRefs. The helper may check pointers and report missing evidence. It must not invent evidence closure.

### 3. Source role never upgrades

A join inherits the strictest source-role posture of its inputs. Joining an aggregate record to a more precise place does not turn it into a per-place observation. Joining a modeled surface to an observed point does not make the model observed.

### 4. Sensitivity inherits the strictest input

If any input is restricted, private, geoprivacy-sensitive, living-person-sensitive, DNA-derived, archaeology-sensitive, rare-species-sensitive, infrastructure-sensitive, or rights-unclear, the join must fail closed until policy/review allows a bounded output.

### 5. Time is part of the claim

A valid join needs temporal scope. Observation time, valid time, retrieval time, processing time, release time, and correction time must not be collapsed when material.

### 6. Geometry precision is policy-significant

A spatial join must preserve geometry precision, uncertainty, CRS/datum, generalization state, and redaction posture. A generalized polygon does not authorize exact-coordinate disclosure.

### 7. Identity confidence is not identity truth

A candidate match score does not create a canonical identity. Identity resolution belongs to the owning domain contracts, validators, reviews, and release controls.

### 8. Public use requires downstream gates

A join cannot reach a public client unless it passes validation, policy, catalog/proof closure, release review, and rollback requirements through governed paths.

[Back to top](#top)

---

## Candidate join families

| Family | Example | Required guardrail |
|---|---|---|
| Exact-key source crosswalk | Source row id to SourceDescriptor id. | Descriptor is referenced, not rewritten. |
| Temporal overlap | Event valid time overlaps county-year panel. | Time kind and uncertainty are preserved. |
| Spatial predicate | Point within county, HUC, ecoregion, parcel, or buffer. | CRS, precision, uncertainty, and sensitivity are preserved. |
| Event-first people-place | ResidenceEvent links PersonAssertion to Place. | Living-person, DNA, private parcel, and rights constraints fail closed. |
| Hydrology context | Gauge observation to reach/HUC context. | Observation, aggregate, modeled, and regulatory records remain distinct. |
| Flora/fauna context | Occurrence to habitat/ecoregion context. | Rare/protected exact geometry is not exposed by helper output. |
| Hazards context | Storm/earthquake/fire/smoke candidate to geography/time context. | Current context, modeled products, administrative records, and observations remain separate. |
| Roads/rail context | Route segment to county or historical corridor context. | Corridor membership is not continuous presence unless evidence supports it. |
| Aggregation join | County-year panel to Focus Mode summary. | Aggregation receipt required; not per-place or per-person truth. |

[Back to top](#top)

---

## Standard finite outcomes

Child tools may extend these outcomes, but should preserve the core pattern.

| Outcome | Meaning |
|---|---|
| `JOIN_CANDIDATE` | A deterministic rule produced a reviewable candidate join. |
| `NO_JOIN_CANDIDATE` | No reviewable candidate was found under configured rules. |
| `MULTIPLE_CANDIDATES` | More than one plausible candidate exists; review required. |
| `EVIDENCE_REF_MISSING` | Required EvidenceRef or source descriptor pointer is absent. |
| `SOURCE_ROLE_CONFLICT` | Input roles cannot be joined without role collapse. |
| `SENSITIVITY_REVIEW_REQUIRED` | Strictest-input sensitivity blocks automatic downstream use. |
| `TEMPORAL_SCOPE_AMBIGUOUS` | The join cannot preserve valid time or time-kind separation. |
| `GEOMETRY_PRECISION_BLOCKED` | Geometry precision, uncertainty, CRS, or redaction posture blocks safe output. |
| `IDENTITY_AMBIGUOUS` | Candidate identity confidence is not strong enough for automatic handoff. |
| `POLICY_REVIEW_REQUIRED` | Rights, consent, sovereignty, sensitivity, or release posture requires policy review. |
| `PROPOSED_WORK_RECORD` | Join candidate exists and downstream review is required. |
| `ABSTAIN` | The helper cannot decide with available evidence. |
| `ERROR` | The helper could not safely complete. |

[Back to top](#top)

---

## Standard report envelope

A first-slice join helper report should be compact, deterministic, and non-authoritative.

```json
{
  "tool": "join-helper-placeholder",
  "status": "JOIN_CANDIDATE",
  "join_family": "spatial_temporal_context",
  "candidate_id": "join_candidate_placeholder",
  "inputs": [
    {
      "object_id": "source_object_a",
      "source_id": "source_descriptor_a",
      "source_role": "observed",
      "evidence_ref": "evidence_ref_a",
      "temporal_scope": "2026-01-01/2026-01-31",
      "sensitivity": "T1"
    },
    {
      "object_id": "source_object_b",
      "source_id": "source_descriptor_b",
      "source_role": "aggregate",
      "evidence_ref": "evidence_ref_b",
      "temporal_scope": "2026",
      "sensitivity": "T0"
    }
  ],
  "checks": {
    "deterministic_rule": "within_and_overlap",
    "source_role_result": "aggregate_inherited",
    "sensitivity_result": "strictest_input_inherited",
    "temporal_result": "needs_review",
    "geometry_result": "generalized_only",
    "evidence_refs": "present"
  },
  "decision": {
    "outcome": "PROPOSED_WORK_RECORD",
    "reason_codes": ["JOIN_CANDIDATE", "TEMPORAL_SCOPE_AMBIGUOUS"],
    "publication": false,
    "evidence_bundle_created": false,
    "policy_decision_created": false,
    "release_decision_created": false
  },
  "next_review": [
    "confirm source descriptors and EvidenceRefs",
    "preserve strictest source role and sensitivity posture",
    "validate contracts and schemas before catalog work",
    "resolve policy and review requirements before any public surface",
    "ensure release manifest and rollback path before publication"
  ]
}
```

Reports are not receipts unless a separate governed workflow adopts them and stores them under the proper receipt root.

[Back to top](#top)

---

## Validation

Recommended first test surface:

```text
tests/joins/
├── README.md
├── test_join_candidates.py
└── fixtures/
    ├── exact_key_match/
    │   ├── input.json
    │   └── expected_report.json
    ├── spatial_temporal_match/
    │   ├── input.json
    │   └── expected_report.json
    ├── aggregate_role_block/
    │   ├── input.json
    │   └── expected_report.json
    ├── sensitive_geometry_block/
    │   ├── input.json
    │   └── expected_report.json
    ├── living_person_join_denied/
    │   ├── input.json
    │   └── expected_report.json
    └── evidence_ref_missing/
        ├── input.json
        └── expected_report.json
```

Recommended assertions:

- exact-key fixture returns `JOIN_CANDIDATE` with deterministic candidate id;
- multiple plausible matches return `MULTIPLE_CANDIDATES`;
- aggregate input cannot become observed output;
- modeled input cannot become observed output;
- missing EvidenceRef returns `EVIDENCE_REF_MISSING` or `ABSTAIN`;
- living-person/private person-parcel input returns `SENSITIVITY_REVIEW_REQUIRED` or `POLICY_REVIEW_REQUIRED`;
- rare/protected exact geometry returns `GEOMETRY_PRECISION_BLOCKED`;
- temporal ambiguity returns `TEMPORAL_SCOPE_AMBIGUOUS`;
- generated reports are deterministic;
- no helper writes to lifecycle or release roots without explicit workflow control.

Suggested future command pattern:

```bash
pytest -q tests/joins
```

```bash
python tools/joins/join_candidates.py \
  --input tests/joins/fixtures/spatial_temporal_match/input.json \
  --output .tmp/join-candidate-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `join_candidates.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing join helper code, reviewers should confirm:

- [ ] The helper is deterministic and dry-run friendly.
- [ ] The helper cannot publish, promote, or create release artifacts.
- [ ] The helper does not create EvidenceBundles, PolicyDecisions, or canonical graph records.
- [ ] The helper references SourceDescriptors and EvidenceRefs instead of duplicating authority.
- [ ] Source roles remain separate and never upgrade.
- [ ] Strictest sensitivity and rights posture is inherited.
- [ ] Temporal scope and time-kind separation are preserved.
- [ ] Geometry precision, uncertainty, CRS/datum, and redaction/generalization posture are preserved.
- [ ] Candidate identity confidence is not treated as canonical identity truth.
- [ ] Sensitive domains fail closed when rights, consent, sovereignty, location precision, or living-person/DNA status is unclear.
- [ ] Outputs are deterministic and machine-readable.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Any proposed work record points to downstream validation, review, correction, and rollback requirements.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace empty README with governed `tools/joins/` contract | **DONE in this README** | Establishes helper boundary and anti-collapse posture. |
| Add `tests/joins/README.md` | **PROPOSED** | Defines public-safe fixtures and deterministic report expectations. |
| Add `join_candidates.py` dry-run helper | **PROPOSED** | Emits candidate reports without lifecycle or release side effects. |
| Add shared outcome enum or schema | **PROPOSED / NEEDS VERIFICATION** | Prevents incompatible join report envelopes. |
| Add source-role and sensitivity inheritance fixtures | **PROPOSED** | Proves aggregate, modeled, sensitive geometry, living-person, and evidence-missing behavior. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces join drift without promotion or publication side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing empty file. |
| Next smallest safe change | Add `tests/joins/README.md`, then add synthetic fixtures for exact-key, spatial-temporal, source-role conflict, sensitive geometry, living-person join denial, and missing EvidenceRef cases. |
