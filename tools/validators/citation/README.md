<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-citation-readme
title: tools/validators/citation/ — Citation Readiness Validator Boundary
type: readme; directory-readme; validator-lane; citation-readiness; evidence-aware; non-authoritative
version: v0.2
status: draft; repository-grounded; README-only-lane; direct-executable-unestablished; direct-tests-unestablished; citation-workflow-todo-only; evidence-report-contract-draft; evidence-report-schema-permissive; ui-report-profile-draft; focus-report-schema-permissive; citation-object-contract-unestablished; evidence-ref-schema-fielded; evidence-ref-validator-missing; evidence-bundle-validator-executable; shared-aggregate-registration-absent; policy-greenfield; package-scaffold; cite-or-abstain; sensitivity-aware; release-gated; fail-closed
owners: OWNER_TBD — Citation steward · Evidence steward · Source steward · Contract steward · Schema steward · Validator steward · Resolver steward · Rights/Sensitivity steward · Policy steward · Runtime/API steward · UI/Evidence Drawer steward · Release steward · Correction/Rollback steward · Security reviewer · CI steward · Docs steward
created: 2026-07-08
updated: 2026-07-16
supersedes: v0.1 planning-oriented citation validator README
policy_label: "repository-facing; tools; validators; citation; claim-citation-mapping; locator-aware; EvidenceRef-aware; EvidenceBundle-subordinate; source-role-preserving; time-aware; rights-aware; sensitivity-aware; correction-aware; release-gated; no-network-by-default; deterministic; fail-closed; no-proof-authority; no-policy-authority; no-release-authority; no-public-serving-authority"
owning_root: tools/
current_path: tools/validators/citation/README.md
responsibility: >
  Repository-grounded boundary for deterministic validation of citation carriers and claim-to-citation mappings. This lane may
  check citation presence, carrier shape, claim scope, locator/excerpt bounds, source identity linkage, source-role/time/caveat
  preservation, EvidenceRef handoff, report consistency, rights/sensitivity metadata presence, release/correction references,
  and finite negative outcomes. It delegates EvidenceRef resolution and EvidenceBundle closure to evidence/resolver lanes;
  policy decisions to policy; materialized proof to data/proofs; receipts to data/receipts; release decisions to release;
  and public rendering to governed runtime/API/UI surfaces.
truth_posture: >
  CONFIRMED target README v0.1 and prior blob; bounded repository search surfaced only README.md under the direct citation
  validator lane; representative direct executable and dedicated test paths were absent; the evidence-family
  CitationValidationReport contract is draft and its schema is an empty permissive scaffold with contract_doc null; separate
  UI and Focus report schemas exist as permissive projection candidates; no accepted standalone Citation contract/schema was
  established; EvidenceRef has a fielded closed schema but its declared validator path is absent; the executable
  validate_evidence_bundle.py delegates to the shared JSON Schema runner and is one of five aggregate validators; citation is
  not in that aggregate; citation-validation workflow jobs are TODO-only echo steps; policy/evidence is a greenfield stub;
  packages/citation is a Python scaffold / PROPOSED immutable input packet, deterministic CitationValidationReport profile,
  finite CIT_ reason codes, no-network fixtures, dedicated CI admission, correction cascade, migration, deprecation, and
  rollback / CONFLICTED evidence-family versus UI/Focus report realization, CitationValidationReport outcome vocabularies,
  citation helper versus resolver ownership, and documentation doctrine versus machine-enforced shape / NEEDS VERIFICATION
  owners, CODEOWNERS, canonical Citation contract/schema, canonical report schema/profile, canonical executable and registry
  id, resolver adapter, fixture inventory, policy bindings, report destination, CI significance, public projection, release
  adoption, and correction cascade / UNKNOWN production invocation, runtime consumers, emitted reports, metrics, deployment,
  current pass results, and branch-protection significance
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: "b22a43297c76248c174e15bfd6d5b2c75c563e92"
  prior_blob: 574848fac4394a618b5e3132705c903ad5846fcd
  citation_report_contract_blob: 36cdb2bab1e47479b816950d907868c4e4689283
  citation_report_evidence_schema_blob: 3cdb7dca322a1a5049afc1e60b89120fbfa1cd90
  citation_report_ui_contract_blob: b5c399d0fcb05fe21205d9488f24b44d1962d011
  citation_report_ui_schema_blob: 1c6ef8eb2c8f9f071e188f16e579b795ebd2f1a7
  citation_report_focus_schema_blob: 0707293f40cdcd381e4007314ba8bab14d4e4f4d
  evidence_ref_schema_blob: 42f499df613a9d68e5ca6fc5ec75ff8058c155b9
  evidence_bundle_validator_blob: c1760c5e92eae6390f5adcde4593e8e9bab26535
  citation_proof_readme_blob: 8964f5cb9ea517a6ba881aa1a606983b18f5d76d
  citation_package_blob: 8516033ca7b7f7458cfc0f09438853bd3ac3753e
  citation_package_module_blob: 445c464fe03da2fa963fbea7111bd68d04789d19
  evidence_parent_blob: c163fd6f77f1f8c0ce8a2e042e8594c7e73658a7
  evidence_bundle_lane_blob: 6499119af1aabb46e1c77f43518b1e6a0dfe30a4
  citation_workflow_blob: 644e60c968c8ad712ed5228d6bcaf1a4d1d9db38
  aggregate_runner_blob: 3375cce172631dc3675cf2e46bb7788d273ff425
  schema_test_blob: b04342cc034d7f1cc554e155fdd02d6e972976e6
  citation_guidance_blob: 073bc7348903b550c98f6fa5674bd1c7378dfc0e
  policy_evidence_blob: 61f9a3f699e69fef56e0fe04a6a415ff539f0363
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  generated_receipt_schema_blob: fba21ed27ebccf1362fe397fe0c3ebd85e072685
bounded_path_checks:
  - tools/validators/citation/ indexed as README-only
  - representative direct citation executable paths were absent
  - representative dedicated citation validator test paths were absent
  - representative evidence citation-report fixture path was absent
  - tools/validators/validate_evidence_ref.py was absent although referenced by schema metadata
  - tools/validators/validate_evidence_bundle.py exists and is executable
  - citation-validation workflow contains TODO echo steps only
related:
  - ../README.md
  - ../_common/README.md
  - ../evidence/README.md
  - ../evidence_bundle/README.md
  - ../validate_evidence_bundle.py
  - ../../../docs/sources/CITATION_GUIDANCE.md
  - ../../../contracts/evidence/citation_validation_report.md
  - ../../../contracts/evidence/evidence_ref.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../contracts/ui/citation_validation_report.md
  - ../../../schemas/contracts/v1/evidence/citation_validation_report.schema.json
  - ../../../schemas/contracts/v1/evidence/evidence_ref.schema.json
  - ../../../schemas/contracts/v1/ui/citation_validation_report.schema.json
  - ../../../schemas/contracts/v1/focus/citation_validation_report.schema.json
  - ../../../data/proofs/citation_validation/README.md
  - ../../../data/proofs/evidence_bundle/README.md
  - ../../../data/registry/sources/
  - ../../../data/receipts/
  - ../../../packages/citation/README.md
  - ../../../packages/citation/src/citation/README.md
  - ../../../policy/evidence/README.md
  - ../../../release/
  - ../../../tests/validators/README.md
  - ../../../.github/workflows/citation-validation.yml
  - ../../../.github/workflows/validator-suite.yml
tags: [kfm, tools, validators, citation, evidence-ref, evidence-bundle, source-role, locator, rights, sensitivity, release, correction, rollback, cite-or-abstain]
notes:
  - "Documentation-only update paired with a generated provenance receipt."
  - "No executable, schema, contract, policy, fixture, test, workflow, proof, receipt family, release record, route, UI component, or public artifact behavior changes."
  - "The evidence-family CitationValidationReport is treated as the semantic authority candidate; UI and Focus forms remain projection candidates until an accepted contract/schema decision."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Citation Readiness Validator Boundary

`tools/validators/citation/`

> Validate citation carriers and claim-to-citation mappings without turning a citation, locator, report, helper, resolver result, or rendered attribution into evidence closure, policy permission, release approval, or public truth.

<p>
  <img alt="Status draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Implementation README only" src="https://img.shields.io/badge/implementation-README__only-orange">
  <img alt="Posture cite or abstain" src="https://img.shields.io/badge/posture-cite--or--abstain-success">
  <img alt="Schema conflict" src="https://img.shields.io/badge/report__shape-CONFLICTED-red">
  <img alt="Network denied" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Authority validator only" src="https://img.shields.io/badge/authority-validator__only-blueviolet">
</p>

> [!IMPORTANT]
> No working direct citation validator was established in this directory. The current evidence-family citation-report schema accepts any object, the UI/Focus schemas are separate placeholders, the citation workflow is TODO-only, and citation is absent from the shared five-entry validator aggregate.

**Quick links:** [Purpose](#purpose) · [Status](#status) · [Placement](#placement) · [Topology](#topology) · [Vocabulary](#vocabulary) · [Scope](#scope) · [Input packet](#packet) · [Citation carrier](#carrier) · [Claim coverage](#coverage) · [Locators](#locators) · [Source roles](#roles) · [Time and freshness](#time) · [Evidence handoff](#evidence) · [Rights and sensitivity](#sensitivity) · [Surface rules](#surfaces) · [Report conflict](#report-conflict) · [Report profile](#report) · [Invariants](#invariants) · [Outcomes](#outcomes) · [Reason codes](#reason-codes) · [Security](#security) · [Tests](#tests) · [CI](#ci) · [Implementation sequence](#sequence) · [Definition of done](#done) · [Migration](#migration) · [Correction and rollback](#rollback) · [Open verification](#open) · [Evidence ledger](#ledger) · [Changelog](#changelog)

---

<a id="purpose"></a>

## Purpose

This lane answers one bounded question:

> For a declared subject, claim scope, audience, and surface, are the supplied citations present, structurally usable, mapped to the claims they support, linked to governed source/evidence references, and safe to hand to downstream evidence, policy, release, and rendering gates?

A pass means only that the configured citation-readiness checks passed for the exact packet, profile, and input digests named in the report.

A pass does **not** prove that the cited claim is true, the source is admitted, an `EvidenceRef` resolved, an `EvidenceBundle` is complete, rights permit reuse, sensitivity policy permits disclosure, review is complete, release exists, or a public surface may speak.

[Back to top](#top)

---

<a id="status"></a>

## Status and evidence boundary

**Snapshot:** `main@b22a43297c76248c174e15bfd6d5b2c75c563e92`
**Prior target blob:** `574848fac4394a618b5e3132705c903ad5846fcd`

| Surface | Status | Consequence |
|---|---|---|
| Direct `citation/` lane | **CONFIRMED README-only in bounded search** | Do not claim executable behavior. |
| Direct citation executable | **NOT ESTABLISHED** | Entrypoint, CLI, registry id, exit codes, and report emission remain proposed. |
| Dedicated citation tests | **NOT ESTABLISHED** | No pass rate or behavioral coverage is claimed. |
| Evidence-family report contract | **CONFIRMED draft semantic contract** | Strongest current meaning candidate. |
| Evidence-family report schema | **CONFIRMED empty permissive scaffold** | Schema success proves almost nothing about report semantics. |
| UI report contract/schema | **CONFIRMED draft projection + placeholder schema** | Must remain downstream of evidence validation and policy filtering. |
| Focus report schema | **CONFIRMED empty permissive scaffold** | Cannot be treated as canonical report authority. |
| Standalone `Citation` contract/schema | **NOT ESTABLISHED** | Carrier shape remains profile-bound and proposed. |
| `EvidenceRef` schema | **CONFIRMED fielded and closed; status PROPOSED** | Its declared validator path is absent. |
| EvidenceBundle validator | **CONFIRMED executable JSON Schema wrapper** | Bundle shape checks exist outside this lane. |
| Shared aggregate | **CONFIRMED five entrypoints; citation absent** | Citation readiness is not aggregate-enforced. |
| Citation workflow | **CONFIRMED TODO-only echo steps** | Workflow presence is not enforcement. |
| `policy/evidence/` | **CONFIRMED greenfield stub** | Policy automation is unestablished. |
| Citation package | **CONFIRMED scaffold/documentation-led** | Helper implementation and runtime integration remain unestablished. |
| Runtime consumers and emitted reports | **UNKNOWN** | No production behavior is claimed. |

Bounded absence is not historical or global proof. Generated, ignored, branch-local, package-local, dynamically loaded, or unindexed files remain possible.

[Back to top](#top)

---

<a id="placement"></a>

## Directory Rules and authority

| Responsibility | Owning home | This lane may do |
|---|---|---|
| Citation validation implementation | `tools/validators/citation/` | Check declared citation-readiness rules. |
| Shared validation runtime | `tools/validators/_common/` | Provide deterministic mechanics. |
| Broad evidence routing | `tools/validators/evidence/` | Coordinate evidence-facing families. |
| EvidenceBundle validation | `tools/validators/evidence_bundle/` and verified entrypoints | Check bundle-specific requirements. |
| Citation/EvidenceRef/EvidenceBundle meaning | `contracts/evidence/` | Define semantics. |
| UI report projection meaning | `contracts/ui/` | Define presentation-safe projection semantics. |
| Machine shape | `schemas/contracts/v1/` | Define accepted JSON Schema. |
| Reusable helper code | `packages/citation/` | Normalize and preserve references without authority escalation. |
| Resolution logic | Accepted evidence-resolver package/tool | Resolve references under bounded access rules. |
| Source identity, role, rights, cadence | `data/registry/sources/` | Own source governance records. |
| Materialized proof support | `data/proofs/` | Store EvidenceBundles and citation-validation proof artifacts. |
| Process memory | `data/receipts/` | Store run/validation/AI/transform/review receipts. |
| Admissibility | `policy/` | Decide allow/deny/restrict/hold/abstain obligations. |
| Release and rollback | `release/` | Own publication state and reversible change. |
| Public output | Governed application/runtime roots | Render released, policy-safe projections. |
| Tests and fixtures | `tests/` and `fixtures/` | Prove refusal and acceptance behavior. |

This directory must not become a proof store, source registry, policy engine, release service, citation cache, web crawler, public API, Evidence Drawer store, or AI answer authority.

[Back to top](#top)

---

<a id="topology"></a>

## Validator topology and delegation

```text
claim / layer / answer / export candidate
  -> citation readiness validator
       - carrier/profile shape
       - claim-to-citation mapping
       - locator and excerpt bounds
       - source/evidence reference presence
       - role/time/caveat preservation
       - safe dependency handoff
  -> EvidenceRef resolver
  -> EvidenceBundle validator / evidence closure
  -> rights + sensitivity + policy
  -> review + release
  -> governed runtime/API projection
  -> UI / export / AI surface
```

A citation validator may normalize dependency results, but it must never upgrade `DENY`, `HOLD`, `REVIEW_REQUIRED`, `ABSTAIN`, or `ERROR` into a result that permits rendering.

[Back to top](#top)

---

<a id="vocabulary"></a>

## Bounded vocabulary

| Term | Meaning here | Not equivalent to |
|---|---|---|
| Citation carrier | Structured reference and display metadata. | Evidence or truth. |
| Citation target | Claim, field, feature, statement, or answer fragment requiring support. | Entire document by default. |
| Claim scope | Exact semantic, spatial, temporal, and audience bounds. | Broad topic label. |
| Locator | Page, line, section, record id, feature id, time window, or anchor. | Proof that the source supports the claim. |
| Excerpt | Rights- and sensitivity-safe fragment, when allowed. | Full-source reproduction. |
| `EvidenceRef` | Governed pointer. | Resolved `EvidenceBundle`. |
| `EvidenceBundle` | Claim-scope evidence closure artifact. | Policy decision or release manifest. |
| `CitationValidationReport` | Structured citation-readiness findings. | EvidenceBundle, receipt, policy decision, or release approval. |
| UI/Focus projection | Audience-safe projection of findings. | Canonical evidence-family report. |
| Citation count | Number of carriers checked. | Evidence strength. |

[Back to top](#top)

---

<a id="scope"></a>

## Supported validation scopes

| Scope | Examples | Required caution |
|---|---|---|
| Single claim | One sentence or assertion | Citation supports the exact assertion. |
| Field-level claim | Value, date, status, classification | Preserve source field and time semantics. |
| Feature/layer claim | Map popup, legend, feature details | Geometry and attribute sensitivity are separate. |
| Evidence Drawer candidate | Citation/evidence payload | Internal refs may require redaction. |
| Focus/AI answer candidate | Answer fragments and citations | Generated text is never evidence. |
| Story/report section | Narrative or card | Every consequential claim has mapped support. |
| Export/screenshot caption | Downloaded carrier | Export may create new leakage. |
| API response | Structured public answer | Use governed envelope and released projection. |
| Release candidate | Public-bound artifact set | Release authority remains separate. |

Ambiguous “validate everything” invocations must fail unless a profile defines exhaustive scope and resource limits.

[Back to top](#top)

---

<a id="packet"></a>

## Proposed immutable validation packet

```yaml
packet_version: kfm.citation_validation_packet.v1
request_id: req_<stable-id>
checked_subject:
  ref: <immutable subject ref>
  type: <claim|feature|layer|drawer|answer|story|export|api|release-candidate>
  digest: <sha256>
claim_scope:
  semantic_scope: <bounded description>
  spatial_scope: <public-safe scope or none>
  temporal_scope: <explicit time-kind values or none>
  audience: <internal|reviewer|restricted|public>
surface:
  kind: <popup|drawer|focus|story|export|api|release-review>
  profile_ref: <accepted profile ref>
  profile_hash: <digest>
citations:
  - citation_id: <stable id>
    target_ids: [<claim id>]
    source_ref: <SourceDescriptor ref>
    evidence_ref: <EvidenceRef>
    locator: <typed locator or null>
    excerpt_digest: <digest or null>
dependency_context:
  evidence_bundle_refs: []
  policy_decision_refs: []
  review_refs: []
  release_refs: []
  correction_refs: []
  rollback_refs: []
execution:
  validator_ref: <entrypoint + version>
  rule_hash: <digest>
  network_mode: denied
  max_citations: <bounded integer>
  max_bytes: <bounded integer>
  timeout_ms: <bounded integer>
```

Inputs are immutable or content-addressed. Missing audience, surface, claim scope, or mandatory dependencies produce finite negative results, not inferred defaults.

[Back to top](#top)

---

<a id="carrier"></a>

## Citation carrier requirements

Until an accepted standalone Citation schema exists, profiles should require stable citation id, exact target mapping, source reference, EvidenceRef where required, source role, typed locator, distinct time context, rights and sensitivity posture, caveats, pinned version/digest, and correction state.

A rendered string is a projection of the structured carrier and must not replace it.

[Back to top](#top)

---

<a id="coverage"></a>

## Claim-to-citation coverage

1. Every consequential target declares whether citation is required.
2. Every required target has mapped support or a finite negative outcome.
3. Every citation maps to at least one target.
4. A citation mapped to multiple targets supports each independently.
5. Topic overlap is not support.
6. Citation count is not support strength.
7. Contradictory citations are surfaced, not averaged away.
8. Unsupported fragments remain unsupported even when adjacent text is cited.
9. Derived or synthetic claims cite underlying evidence and derivation context.
10. Aggregate citations cannot silently support record- or person-level claims.

Reports may summarize required, supported, unsupported, blocked, and review-required target counts, but must retain target-level findings.

[Back to top](#top)

---

<a id="locators"></a>

## Locator, excerpt, and quotation boundary

| Locator kind | Checks |
|---|---|
| Page/line | Range, source version, extraction provenance. |
| Section/heading | Anchor exists in pinned version. |
| Record/feature id | Dataset version and identity continuity. |
| Spatial locator | Policy-safe precision and reconstruction risk. |
| Temporal locator | Correct time kind and bounded interval. |
| URI fragment | Scheme/host/path allowlist; no secret-bearing query. |
| Content digest | Canonicalization profile and digest algorithm. |

Excerpts are optional unless a profile requires them. They must respect rights, attribution, privacy, sensitivity, and quotation limits. Reports should prefer excerpt digests and safe summaries over restricted or copyrighted text. OCR and generated summaries remain derived carriers with visible provenance.

[Back to top](#top)

---

<a id="roles"></a>

## Source role and knowledge-character preservation

The citation validator preserves the admitted role:

```text
observed | regulatory | modeled | aggregate | administrative | candidate | synthetic
```

| Role | Must preserve | Forbidden collapse |
|---|---|---|
| `observed` | Observer/instrument/method and observation time | Model or compilation as observation. |
| `regulatory` | Authority, jurisdiction, effective version/time | Regulatory layer as event. |
| `modeled` | Model identity, run/version, input and uncertainty refs | Model as observation. |
| `aggregate` | Aggregation unit, method, and period | Aggregate as individual/place truth. |
| `administrative` | Compilation authority and source time | Compilation as observed event. |
| `candidate` | Candidate disposition and non-public state | Candidate as released truth. |
| `synthetic` | Method and Reality Boundary Note | Synthetic as observed reality. |

Promotion, rendering, or validation must not upgrade a role.

[Back to top](#top)

---

<a id="time"></a>

## Time, version, freshness, and correction state

Citation checks keep `source_time`, `observed_time`, `valid_time`, `retrieval_time`, `release_time`, and `correction_time` distinct where material.

Freshness is profile- and cadence-dependent; the validator does not invent a universal threshold. New retrieval does not make old content current. Historic claims are not stale merely because they are old. Current-status claims with unresolved freshness must abstain, hold, or fail according to profile and policy. Correction state outranks cached display state.

[Back to top](#top)

---

<a id="evidence"></a>

## EvidenceRef and EvidenceBundle handoff

The current `EvidenceRef` schema is fielded and closed, but its declared validator path was not found. The current EvidenceBundle validator is executable and uses the shared JSON Schema runner.

| State | Required result |
|---|---|
| Evidence ref absent | `ABSTAIN` or `FAIL` |
| Evidence ref malformed | `FAIL` |
| Evidence ref unresolved | `ABSTAIN`, `HOLD`, or `ERROR` |
| Bundle schema invalid | `FAIL` |
| Bundle incomplete | Negative evidence-lane result |
| Bundle policy-blocked | `DENY` or `HOLD` |
| Bundle released and admissible | Citation checks may continue; still not release approval |

Dependency identity, version, input ref, outcome, safe reason code, report ref, and blocking status must be recorded. Full bundles and restricted payloads must not be copied into citation reports.

[Back to top](#top)

---

<a id="sensitivity"></a>

## Rights, sensitivity, privacy, and metadata leakage

A citation is an exposure carrier. Validators inspect titles, filenames, source ids, locators, URIs, query strings, geometry refs, timestamps, attribution text, caveats, thumbnails, export metadata, and linked identifiers.

Fail closed for precise sensitive-species, archaeology, sacred-site, private-property, living-person, DNA, or critical-infrastructure leakage; infrastructure condition/vulnerability detail; private/signed URLs; internal hostnames or paths; reversible redaction; restricted excerpts; unknown public-use rights; missing attribution duties; unresolved consent; and public links to unreleased or quarantined evidence.

The most restrictive policy wins. Client-side hiding, CSS, map styling, or collapsed UI sections do not make unsafe citation data safe.

[Back to top](#top)

---

<a id="surfaces"></a>

## Surface-specific rules

| Surface | Required behavior |
|---|---|
| Map popup | Consequential claims require mapped citations and a governed Evidence Drawer path. |
| Evidence Drawer | Render public-safe report projection; preserve negative states and limitations. |
| Focus/AI answer | Cite underlying evidence, never the generated answer; unsupported fragments abstain. |
| Story/report | Preserve target-level support; prevent citation laundering across sections. |
| API response | Return governed finite outcome and released public-safe refs only. |
| Export/download | Carry citations, caveats, release refs, and correction state. |
| Screenshot/share | Caption and metadata must not bypass sensitivity or release rules. |
| Reviewer UI | Additional findings require authorized access and audit. |

Surface profiles may be stricter than the general profile, never weaker without accepted policy or ADR authority.

[Back to top](#top)

---

<a id="report-conflict"></a>

## CitationValidationReport conflict register

| Family | Current posture | Conflict |
|---|---|---|
| Evidence | Empty permissive schema; `contract_doc: null` | Strong semantic contract is not machine-bound. |
| UI | Placeholder requiring only `id`; UI projection contract | Projection may diverge from evidence findings. |
| Focus | Empty permissive schema; `contract_doc: null` | May become a parallel authority. |

Default posture: treat `contracts/evidence/citation_validation_report.md` as the strongest semantic authority candidate; treat UI and Focus forms as downstream projections; do not create a fourth canonical shape here; and require an accepted contract/schema/ADR or migration note before implementation pins a family.

[Back to top](#top)

---

<a id="report"></a>

## Proposed deterministic report profile

```yaml
report_version: kfm.citation_validation_report.v1
report_id: cvr_<content-hash>
checked_subject_ref: <immutable ref>
checked_subject_digest: <sha256>
profile_ref: <profile id>
profile_hash: <sha256>
validator_ref: <entrypoint id>
validator_version: <version>
rule_hash: <sha256>
network_mode: denied
overall_outcome: <PASS|WARN|FAIL|HOLD|DENY|ABSTAIN|ERROR|REVIEW_REQUIRED>
findings:
  - finding_id: <stable id>
    target_ids: []
    citation_ids: []
    outcome: <finite outcome>
    reason_code: <CIT_*>
    blocking: true
    dependency_refs: []
    public_safe_message: <bounded text>
counts:
  citations_checked: 0
  required_targets: 0
  supported_targets: 0
  unsupported_targets: 0
dependency_results: []
limitations: []
policy_decision_refs: []
review_refs: []
release_refs: []
correction_refs: []
rollback_refs: []
input_hashes: {}
```

Given identical packet bytes, rule/profile hashes, dependency results, and validator version, the report body excluding run timestamps should be byte-stable after accepted canonicalization.

Reports must omit private chain-of-thought, secrets, restricted payloads, hidden thresholds, unsafe exact coordinates, full copyrighted text, signed URLs, private access instructions, and public stack traces.

[Back to top](#top)

---

<a id="invariants"></a>

## Citation readiness invariants

1. Citation is traceability, not truth.
2. Presence is not support.
3. Count is not confidence.
4. Locator is not entailment.
5. Rendered attribution is not the carrier.
6. Every required target has support or a finite negative result.
7. Unsupported fragments stay unsupported.
8. EvidenceRef is not EvidenceBundle closure.
9. Bundle closure is not policy permission.
10. Policy permission is not release approval.
11. Generated text is never evidence.
12. Tiles, graphs, scenes, indexes, and UI payloads are not proof.
13. Source roles remain distinct.
14. Aggregate scope cannot silently shrink.
15. Modeled cannot silently become observed.
16. Regulatory cannot silently become event evidence.
17. Candidate cannot appear as released.
18. Synthetic requires a reality boundary.
19. Time kinds remain distinct.
20. Freshness is profile-bound.
21. Missing rights or sensitivity fails closed for public use.
22. Most-restrictive policy wins.
23. Redaction/generalization is not style-only.
24. Citation metadata cannot reconstruct protected content.
25. Network is denied by default.
26. Arbitrary URI fetching is not validation.
27. Dependency errors cannot become render-permitting warnings.
28. Negative dependency outcomes are monotonic.
29. Permissive schema pass is not semantic completeness.
30. UI/Focus projections cannot override evidence findings.
31. Reports and receipts remain separate.
32. Proof data and validator source remain separate.
33. Public clients use governed interfaces and released projections.
34. Correction, withdrawal, and rollback stay visible.
35. Cached displays invalidate when support changes.
36. Pass is scoped to named inputs, rules, dependencies, and time.
37. Human review remains visible when required.
38. Citation validation cannot authorize its own release.

[Back to top](#top)

---

<a id="outcomes"></a>

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Configured readiness checks passed; continue to later gates. |
| `WARN` | Non-blocking limitation under accepted profile. |
| `FAIL` | Deterministic validation defect. |
| `HOLD` | Dependency, review, or governance state incomplete. |
| `DENY` | Requested use unsafe or disallowed. |
| `ABSTAIN` | Support insufficient to emit the claim. |
| `ERROR` | Validator/dependency/runtime failed. |
| `REVIEW_REQUIRED` | Human review mandatory. |

Runtime mappings must be explicit and must not weaken outcomes.

[Back to top](#top)

---

<a id="reason-codes"></a>

## Proposed `CIT_` reason-code families

| Family | Examples |
|---|---|
| Profile | `CIT_PROFILE_MISSING`, `CIT_RULE_HASH_MISMATCH` |
| Subject/scope | `CIT_SUBJECT_MISSING`, `CIT_CLAIM_SCOPE_UNBOUNDED` |
| Carrier | `CIT_CARRIER_MALFORMED`, `CIT_TARGET_MAPPING_MISSING` |
| Coverage | `CIT_REQUIRED_TARGET_UNCITED`, `CIT_SUPPORT_SCOPE_MISMATCH` |
| Locator/excerpt | `CIT_LOCATOR_INVALID`, `CIT_EXCERPT_RIGHTS_BLOCKED` |
| Source | `CIT_SOURCE_REF_MISSING`, `CIT_SOURCE_VERSION_MISMATCH` |
| Role | `CIT_SOURCE_ROLE_COLLAPSE`, `CIT_SYNTHETIC_BOUNDARY_MISSING` |
| Time | `CIT_TIME_KIND_COLLAPSE`, `CIT_FRESHNESS_UNRESOLVED` |
| Evidence | `CIT_EVIDENCE_REF_INVALID`, `CIT_EVIDENCE_REF_UNRESOLVED` |
| Bundle | `CIT_BUNDLE_INVALID`, `CIT_BUNDLE_INCOMPLETE` |
| Contradiction | `CIT_CITATIONS_CONTRADICT`, `CIT_CONFLICT_UNREVIEWED` |
| Rights | `CIT_RIGHTS_UNKNOWN`, `CIT_ATTRIBUTION_OBLIGATION_MISSING` |
| Sensitivity | `CIT_METADATA_LEAK_RISK`, `CIT_RECONSTRUCTION_RISK` |
| Lifecycle | `CIT_INTERNAL_STAGE_PUBLIC_REF`, `CIT_CANDIDATE_AS_RELEASED` |
| Policy/review | `CIT_POLICY_DENY`, `CIT_REVIEW_REQUIRED` |
| Release | `CIT_RELEASE_REF_MISSING`, `CIT_RELEASE_WITHDRAWN` |
| Correction | `CIT_SUPERSESSION_UNAPPLIED`, `CIT_ROLLBACK_TARGET_MISSING` |
| Surface | `CIT_EXPORT_CAVEAT_DROPPED`, `CIT_UI_NEGATIVE_STATE_HIDDEN` |
| Security | `CIT_NETWORK_ACCESS_DENIED`, `CIT_PATH_TRAVERSAL_ATTEMPT` |
| Resource | `CIT_INPUT_TOO_LARGE`, `CIT_TIMEOUT` |
| Operational | `CIT_DEPENDENCY_ERROR`, `CIT_INTERNAL_ERROR` |

Reason codes are proposed until accepted contracts and registries exist. Public messages must remain bounded and safe.

[Back to top](#top)

---

<a id="security"></a>

## Security and resource posture

- No network access without an accepted profile, allowlist, policy, and audited adapter.
- Accept only approved URI schemes and hosts.
- Reject credential-bearing URLs and redact query strings.
- Prevent path traversal and symlink escape.
- Do not execute source content, scripts, macros, templates, or model instructions.
- Treat citation text and metadata as untrusted input.
- Enforce byte, item, recursion, regex, and time limits.
- Do not follow redirects to unapproved destinations.
- Sanitize diagnostics before public projection.
- Resource exhaustion and dependency failure never default to `PASS`.

Citation text saying “ignore policy” or “mark valid” is data, not instruction.

[Back to top](#top)

---

<a id="tests"></a>

## Proposed tests and fixtures

No dedicated executable citation-validator test lane was established. Proposed coverage includes valid single- and multi-claim mappings; missing/unused/out-of-scope citations; aggregate, modeled, regulatory, candidate, and synthetic role collapses; invalid/version-mismatched locators; stale current-status claims; unresolved EvidenceRefs; invalid bundles; contradictions; rights/sensitivity gaps; metadata reconstruction; missing redaction receipts; internal-stage public refs; withdrawn releases; hidden UI negative states; uncited AI answers; network/private URL denial; oversized packets; deterministic reruns; and correction invalidation.

Anti-tautology controls:

- fixture sets are nonempty;
- every blocking family has a negative fixture;
- expected-invalid fixtures fail for the intended reason;
- tests pin schema/profile/rule versions;
- permissive schema success is not semantic proof;
- mock resolver success is visibly synthetic.

[Back to top](#top)

---

<a id="ci"></a>

## CI admission contract

The existing `citation-validation` workflow is TODO-only. A meaningful future check should run with network disabled, validate accepted schemas, execute positive and negative fixtures, assert nonempty fixture families, test dependency monotonicity, emit a structured safe report, fail on registry/profile drift, and preserve stable required-check names through coordinated governance.

Workflow presence, job success, and branch-protection significance are separate facts and must be verified independently.

[Back to top](#top)

---

<a id="sequence"></a>

## Smallest sound implementation sequence

1. **Contract/ADR:** decide Citation semantics, canonical report family, projections, outcomes, and versioning.
2. **Schemas/fixtures:** implement closed field-complete schemas and nonempty valid/invalid fixtures.
3. **Helper package:** implement deterministic carrier/locator helpers without network or closure authority.
4. **Validator:** implement one entrypoint and registry id; emit deterministic reports; delegate resolution.
5. **Policy/projection:** bind rights, sensitivity, audience, surface, and safe UI/Focus projection.
6. **CI/integration:** replace TODO workflow steps and prove correction invalidation and rollback.

Each PR remains independently reversible.

[Back to top](#top)

---

<a id="done"></a>

## Definition of done

- [ ] Owners and CODEOWNERS accepted.
- [ ] Citation semantics accepted or explicitly unnecessary.
- [ ] Canonical report contract/schema accepted.
- [ ] UI and Focus projections reference the canonical report.
- [ ] Outcomes and reason codes accepted.
- [ ] One executable entrypoint and registry id confirmed.
- [ ] EvidenceRef validator/path drift resolved.
- [ ] Resolver and EvidenceBundle dependencies tested.
- [ ] Rights, sensitivity, role, time, freshness, and release profiles bound.
- [ ] Positive and negative fixtures nonempty.
- [ ] Dedicated refusal tests implemented.
- [ ] Reports deterministic and safe.
- [ ] Network denied by default.
- [ ] Resource budgets enforced.
- [ ] Citation workflow executes real checks.
- [ ] Required-check significance verified.
- [ ] Public projections preserve negative states and caveats.
- [ ] Correction/withdrawal invalidates dependent reports.
- [ ] Release integration remains separate.
- [ ] Rollback exercised.
- [ ] Documentation matches behavior.

[Back to top](#top)

---

<a id="migration"></a>

## Migration and deprecation

Known drift includes overlapping evidence/UI/Focus report schemas, missing evidence schema fields and contract pointer, missing Citation contract/schema, helper-versus-resolver overlap, missing EvidenceRef validator path, and no canonical citation entrypoint.

Canonicalization requires an accepted ADR or migration note; explicit versioned adapters; input/output hashes and receipts; shared-corpus comparison during a bounded compatibility window; blocking any change that weakens denial, abstention, or sensitivity; and deprecation notices naming replacement, deadline, consumers, correction path, and rollback target.

[Back to top](#top)

---

<a id="rollback"></a>

## Correction, supersession, withdrawal, and rollback

A pass becomes stale when source identity/role/rights, source version, EvidenceRef target, EvidenceBundle, profile/rules, locator, policy, review, sensitivity, release, projection, or validator behavior changes.

```text
changed dependency
  -> identify affected citation reports
  -> mark stale/superseded
  -> identify affected claims, exports, UI projections, releases, and AI answers
  -> hold or withdraw affected public carriers where required
  -> rerun against pinned corrected inputs
  -> emit correction/supersession/rollback records
```

Before merge, close the draft PR and abandon the branch. After merge, revert the README commit and revert or supersede the generated receipt. This documentation update changes no runtime or release state.

[Back to top](#top)

---

<a id="open"></a>

## Open verification register

1. Owners and CODEOWNERS.
2. Standalone Citation contract requirement.
3. Canonical Citation schema/profile registry.
4. Canonical report contract and schema.
5. Evidence/UI/Focus projection relationship.
6. Outcome and reason-code vocabularies.
7. Report persistence and proof/receipt homes.
8. Canonical validator entrypoint and registry id.
9. CLI/library and exit-code contracts.
10. Deterministic canonicalization profile.
11. EvidenceRef validator and resolver.
12. EvidenceBundle dependency interface.
13. Resolver access/network policy.
14. Source registry interface and role authority.
15. Locator vocabulary and excerpt policy.
16. Rights and sensitivity inputs.
17. Freshness/cadence and time representation.
18. Contradiction handling.
19. Claim mapping and required-citation rules.
20. Public versus reviewer fields.
21. Evidence Drawer, Focus/AI, popup, export, story, and API integrations.
22. Fixture inventory and direct tests.
23. Package tests and fixtures.
24. Negative-state and nonempty coverage.
25. Resource budgets and SSRF controls.
26. Structured report destination and retention.
27. Workflow implementation and required-check significance.
28. Operational metrics.
29. Correction cascade and release-gate adoption.
30. Rollback drill and compatibility retirement.

Unresolved items remain `NEEDS VERIFICATION`, not implementation facts.

[Back to top](#top)

---

<a id="ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Target README v0.1 | CONFIRMED | Existing lane and prior scope | Executable behavior |
| Evidence report contract | CONFIRMED draft | Meaning and boundary | Accepted schema/runtime |
| Evidence report schema | CONFIRMED permissive scaffold | Machine-shape weakness | Semantic completeness |
| UI report contract/schema | CONFIRMED draft/placeholder | Projection concept | Canonical authority |
| Focus report schema | CONFIRMED permissive scaffold | Overlapping shape | Focus runtime behavior |
| EvidenceRef schema | CONFIRMED fielded/closed | Pointer shape candidate | Resolver success |
| Missing EvidenceRef validator path | CONFIRMED at tested path | Metadata/path drift | Global absence |
| EvidenceBundle validator | CONFIRMED executable wrapper | Existing schema-runner integration | Full closure/release readiness |
| Shared aggregate | CONFIRMED five entrypoints | Citation absent | No other invocation |
| Citation workflow | CONFIRMED TODO-only | Workflow scaffold | Enforcement |
| Citation proof README | CONFIRMED documentation | Proof-family boundary | Proof inventory |
| Citation package/module | CONFIRMED scaffold | Helper boundary | Runtime integration |
| Citation Guidance v0.3 | CONFIRMED document/doctrine support | Cite-or-abstain, roles, times, sensitivity | Machine enforcement |
| `policy/evidence/README.md` | CONFIRMED greenfield stub | Policy lane | Policy automation |
| Directory Rules | CONFIRMED doctrine | Placement/authority | Runtime maturity |
| Generated receipt schema | CONFIRMED schema | Provenance shape | Human approval |

[Back to top](#top)

---

<a id="changelog"></a>

## Changelog

### v0.2 — 2026-07-16

- Replaced planning language with a repository-grounded implementation boundary.
- Recorded README-only direct lane, aggregate absence, and TODO-only workflow.
- Recorded evidence/UI/Focus report overlap and EvidenceRef validator drift.
- Separated citation readiness from bundle closure, policy, release, proof storage, helpers, and rendering.
- Added packet, carrier, coverage, locator, role, time, evidence, sensitivity, surface, report, outcome, reason-code, security, test, CI, migration, correction, rollback, verification, and evidence-ledger contracts.
- Added generated-work provenance receipt requirement.

### v0.1 — 2026-07-08

- Replaced a stray one-character file with an initial proposed citation-validator guide.

<p align="right"><a href="#top">Back to top</a></p>
