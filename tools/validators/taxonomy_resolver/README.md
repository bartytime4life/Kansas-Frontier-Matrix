<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-taxonomy-resolver-readme
title: tools/validators/taxonomy_resolver README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-taxonomy-steward-plus-validator-steward-plus-schema-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; taxonomy-resolver-validator-index; controlled-vocabulary-aware; alias-aware; hierarchy-aware; crosswalk-aware; deprecation-aware; provenance-aware; fail-closed; release-gated; non-authoritative
owning_root: tools/
responsibility: taxonomy resolver validator routing README under tools/validators; documents validation expectations for taxonomy refs, class ids, labels, slugs, aliases, synonyms, broader/narrower hierarchy, vocabulary versions, vocabulary refs, deprecated terms, stale terms, duplicate ids, conflicting aliases, untrusted roots, crosswalk candidates, domain/layer/object/source/policy class admissibility, provenance refs, release refs, rollback refs, fixture/test routing, and finite outcomes while deferring canonical taxonomy records, source registries, semantic contracts, canonical schemas, policy decisions, evidence records, receipts, lifecycle data, release records, public runtime code, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../source/README.md
  - ../source_role/README.md
  - ../policy/README.md
  - ../rights/README.md
  - ../sensitivity/README.md
  - ../release/README.md
  - ../promotion_gate/README.md
  - ../../../packages/taxonomy/README.md
  - ../../../packages/identity/README.md
  - ../../../packages/schema-registry/README.md
  - ../../../packages/envelopes/README.md
  - ../../../contracts/
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../data/registry/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../fixtures/
  - ../../../tests/
notes:
  - "This README replaces an empty placeholder at tools/validators/taxonomy_resolver/README.md. It does not confirm executable taxonomy resolver validators, registry wiring, schemas, fixtures, policy bundles, receipt emission, runtime behavior, or CI behavior."
  - "packages/taxonomy/ is the helper-code lane for taxonomy lookup, class ids, labels, aliases, hierarchy traversal, crosswalk candidates, and deterministic taxonomy validation helpers. This validator lane may call or test such helpers, but must not become helper package authority or canonical taxonomy authority."
  - "Canonical taxonomy records, admitted vocabularies, aliases, deprecations, source registries, schemas, contracts, policy rules, lifecycle data, proofs, receipts, and release decisions belong in their owning roots, not in this validator folder."
  - "Missing, ambiguous, duplicate, stale, deprecated, untrusted, conflicting, or crosswalk-drifted taxonomy refs must fail closed or route to review, not silently normalize to a public-safe term."
  - "Generated labels, fuzzy matches, AI suggestions, UI strings, and map legend labels are not canonical taxonomy truth. They require governed source, taxonomy, evidence, policy, and release support before authority use."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/taxonomy_resolver

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-taxonomy--resolver--validator-informational)
![authority](https://img.shields.io/badge/authority-validator--not--taxonomy-lightgrey)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/taxonomy_resolver/` is the taxonomy-resolution validator routing lane for checking controlled vocabulary refs, class ids, labels, aliases, hierarchy traversal, crosswalk candidates, deprecations, stale terms, provenance, and release posture without becoming canonical taxonomy authority, schema authority, policy authority, evidence authority, or release authority.

---

## Purpose

`tools/validators/taxonomy_resolver/` exists to make taxonomy-resolution validation visible under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Does a taxonomy-bearing candidate resolve its class id, label, alias, vocabulary ref, version, hierarchy context, crosswalk candidate, deprecation state, review state, provenance refs, policy posture, release ref, rollback ref, and public-surface envelope from admitted taxonomy inputs without inventing domain truth, silently normalizing ambiguity, or upgrading generated text into authority?

The answer should be a deterministic validation result or routing decision. This folder should not author canonical taxonomy records, define schemas, define semantic contracts, decide policy, create EvidenceBundles, write receipts, store lifecycle data, approve release, publish artifacts, expose public API/map/AI payloads, or convert labels into truth.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/taxonomy_resolver/README.md` | **CONFIRMED README** | This README replaces the previous empty placeholder. |
| `packages/taxonomy/README.md` | **CONFIRMED package README / implementation NEEDS VERIFICATION** | Shared helper package for taxonomy lookup, class ids, labels, aliases, hierarchy traversal, crosswalk candidates, and deterministic taxonomy validation helpers. |
| Canonical taxonomy record home | **NEEDS VERIFICATION** | The helper package explicitly says canonical taxonomy authority belongs in a repo-confirmed taxonomy/registry home, not the helper package. |
| Executable taxonomy resolver scripts, registry wiring, schemas, fixtures, policy bundles, vocabulary snapshots, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README is documentation only. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home | Boundary |
|---|---|---|
| Taxonomy resolver validation | `tools/validators/taxonomy_resolver/` | Check resolver outputs and fail-closed behavior. |
| Taxonomy helper code | `packages/taxonomy/` | Reusable lookup, alias, traversal, crosswalk, and validation helpers only. |
| Canonical taxonomy records | repo-confirmed taxonomy/registry home | Owns admitted terms, versions, aliases, deprecations, and release state. |
| Source registries | `data/registry/` and accepted source registry homes | Own source authority, rights, cadence, and limitations. |
| Semantic contracts | `contracts/` | Define meaning and normative behavior. |
| JSON Schemas | `schemas/contracts/v1/` | Define machine shape for taxonomy records and refs. |
| Policy rules | `policy/` | Own sensitivity, rights, publication, access, and obligation decisions. |
| Evidence/proofs and receipts | `data/proofs/`, `data/receipts/` | Store proof artifacts and receipts; validators check refs. |
| Release and rollback | `release/` | Own publication, correction, rollback, withdrawal, and supersession. |
| Fixtures and tests | `fixtures/`, `tests/` | Synthetic examples and tests prove behavior; they are not taxonomy authority. |
| Public API/UI/map/AI runtime | governed application/runtime roots | Consume governed taxonomy status; they do not resolve authority from labels alone. |

[Back to top](#top)

---

## Taxonomy resolver validation packet

A taxonomy resolver candidate should expose enough explicit context for deterministic validation.

| Required family | Validator expectation | Must not be treated as |
|---|---|---|
| Resolver identity | Resolver id, package/helper version, registry id, run context, and output envelope are visible. | Taxonomy authority by tool name. |
| Vocabulary identity | Vocabulary ref, taxonomy ref, version, release ref, hash/digest, status, steward, and source vocabulary ref where used. | Current truth without release support. |
| Term identity | Class id, slug, label, alias, synonym, term hash, status, deprecation ref, replacement ref, and review state. | Truth by label match. |
| Hierarchy context | Parent id, broader/narrower relationship, path, depth, domain lane, object family, and facet context. | Invented missing parentage. |
| Alias/synonym handling | Alias source, confidence/status, ambiguity flag, conflict flag, and review posture are explicit. | Silent canonicalization. |
| Crosswalk context | Source vocabulary ref, target vocabulary ref, mapping method, mapping confidence/status, review state, and limitation notes. | Equivalence as truth. |
| Domain admissibility | Domain, layer, object family, source family, policy class, UI facet, or map layer class is admitted for the requested use. | Universal taxonomy membership. |
| Evidence/provenance support | EvidenceRef, source refs, vocabulary refs, digest refs, review refs, and validation report refs resolve where required. | Generated classification as evidence. |
| Policy/release support | Policy decision, reason codes, obligations, release reference, correction path, withdrawal posture, rollback target, and supersession state exist where required. | Publication by resolver success. |
| Consumer envelope | API/map/tile/export/search/facet/graph/Focus Mode/embedding/AI surfaces are limited to approved terms, caveats, and release state. | Unbounded reuse across surfaces. |

[Back to top](#top)

---

## Taxonomy resolver invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Explicit inputs only | Resolver consumes supplied/repo-confirmed taxonomy inputs, not hidden globals, source systems, UI state, memory, or generated language. | Missing terms are fetched, guessed, or generated. |
| Labels are not authority | Labels, aliases, UI strings, map legends, and AI prose are not canonical term truth. | Label match becomes authoritative classification. |
| Ambiguity fails closed | Missing, duplicate, conflicting, stale, deprecated, ambiguous, or untrusted refs do not silently normalize. | Resolver chooses a term without review or reason code. |
| Crosswalks are candidates | Crosswalk output is candidate mapping unless accepted review/release state says otherwise. | Candidate crosswalk is treated as equivalence truth. |
| Hierarchy is not invented | Broader/narrower/path traversal uses admitted records only. | Missing parent/child terms are synthesized. |
| Deprecation propagates | Deprecated, replaced, withdrawn, superseded, or stale terms route to replacement/review/correction where required. | Deprecated term remains active without review. |
| Provenance travels | Taxonomy ref, term id, vocabulary ref, version, status, review state, hash, and release metadata persist downstream. | Downstream surfaces keep only a display label. |
| Public use is gated | Rights, sensitivity, source, policy, review, release, correction, and rollback support close before public exposure where material. | Public surface receives unsupported taxonomy state. |
| Carriers are not authority | Search facets, map legends, popups, reports, exports, graph labels, embeddings, and AI answers are downstream carriers. | Carrier becomes taxonomy source of truth. |

[Back to top](#top)

---

## Fail-closed conditions

A taxonomy resolver candidate should fail closed, deny, restrict, hold, abstain, or route to steward review when:

- vocabulary ref, taxonomy ref, class id, term id, version, status, hash, release ref, or review state is missing;
- term id is unknown, duplicate, deprecated, stale, withdrawn, superseded, conflicted, or not admitted for the requested domain/layer/object/source/policy class;
- alias, synonym, slug, label, or UI string resolves to multiple possible terms without explicit ambiguity handling;
- crosswalk mapping lacks source vocabulary ref, target vocabulary ref, mapping method, review state, confidence/status, limitation notes, or release posture;
- hierarchy traversal requires missing parent, child, broader, narrower, or path records;
- resolver consumes hidden globals, source downloads, raw stores, UI labels, operator memory, generated text, or online lookup instead of supplied governed inputs;
- taxonomy helper output is treated as canonical taxonomy authority, evidence closure, policy approval, release approval, or public-surface permission;
- public API, map, tile, export, screenshot, graph, Focus Mode, search facet, embedding, or AI answer drops taxonomy provenance, status, caveats, deprecation state, or release limits.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Taxonomy resolver validator routing | `tools/validators/taxonomy_resolver/` |
| Taxonomy helper code | `packages/taxonomy/` |
| Identity helpers | `packages/identity/` |
| Schema registry helpers | `packages/schema-registry/` |
| Runtime response envelopes | `packages/envelopes/` |
| Canonical taxonomy records | repo-confirmed taxonomy/registry home — **NEEDS VERIFICATION** |
| Semantic contracts | `contracts/` |
| Machine schemas | `schemas/contracts/v1/` |
| Source registries | `data/registry/` and accepted registry homes |
| Policy | `policy/` |
| Evidence/proofs | `data/proofs/` |
| Receipts | `data/receipts/` |
| Lifecycle data | governed `data/` lifecycle roots |
| Release records and rollback | `release/` |
| Fixtures | `fixtures/` and accepted fixture homes |
| Tests | `tests/` and accepted test homes |
| Public API/UI/map/AI runtime | governed application/runtime roots |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared taxonomy resolver invariants and delegates canonical taxonomy records, schema authority, semantic meaning, policy decisions, evidence, receipts, lifecycle data, release records, and public runtime authority to owning roots.
- **NEEDS VERIFICATION:** exact executable files, registry entries, canonical taxonomy record homes, vocabulary snapshot homes, schema ids, fixture files, test paths, policy bundle homes, report destinations, receipt emission, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as canonical taxonomy record home, vocabulary authority, source registry, schema home, contract home, policy home, evidence store, proof store, receipt store, lifecycle data store, release record store, public runtime surface, AI answer source, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/taxonomy_resolver/` include:

- this README;
- small validation adapters that check taxonomy resolver outputs;
- checks for class id, slug, label, alias, synonym, version, vocabulary ref, status, deprecation, and replacement posture;
- checks for duplicate ids, conflicting aliases, stale versions, untrusted roots, and ambiguous matches;
- checks for crosswalk candidate method, confidence/status, review state, and limitation notes;
- checks that downstream objects preserve taxonomy refs, term ids, vocabulary refs, versions, review state, hash/digest refs, release refs, and rollback refs;
- finite outcome vocabulary and reason-code mapping;
- report destination notes that keep generated outputs out of taxonomy, policy, receipt, proof, lifecycle, and release authority unless explicitly routed to accepted homes.

[Back to top](#top)

---

## What does not belong here

| Do not put in this folder | Correct home |
|---|---|
| Canonical taxonomy datasets, term registries, vocabulary snapshots, deprecation ledgers, accepted crosswalks | repo-confirmed taxonomy/registry home, not validator docs |
| JSON Schemas, DTOs, enums, or machine shape | `schemas/contracts/v1/` or accepted schema homes |
| Semantic contracts | `contracts/` |
| Policy rules, allowlists, denylists, steward decisions, release decisions | `policy/`, `release/`, accepted governance homes |
| Source descriptors and source registries | `data/registry/` and accepted registry homes |
| EvidenceBundles, proof packs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, MapLibre runtime code, tile service code, Focus Mode, export, screenshot, graph, embedding, or AI runtime code | governed application/runtime roots |
| Real sensitive examples, private labels, source credentials, hidden thresholds, production signing keys, or reconstruction hints | denied here; keep out of repository-facing validator docs |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `TAXONOMY_RESOLVER_PASS` | Candidate passed configured taxonomy resolver checks. |
| `TAXONOMY_RESOLVER_FAIL` | Candidate failed one or more configured taxonomy resolver checks. |
| `TAXONOMY_RESOLVER_DENY` | Candidate must not proceed because taxonomy, evidence, policy, review, release, rollback, or public-surface support cannot be resolved. |
| `TAXONOMY_RESOLVER_RESTRICT` | Candidate may proceed only in restricted/steward-gated contexts. |
| `TAXONOMY_RESOLVER_HOLD` | Candidate must remain held pending taxonomy steward review or vocabulary closure. |
| `TAXONOMY_RESOLVER_ABSTAIN` | Candidate lacks enough support for a taxonomy assertion. |
| `TAXONOMY_REF_MISSING` | Required taxonomy or vocabulary reference is absent. |
| `TAXONOMY_TERM_MISSING` | Required class id, term id, slug, label, or alias is absent. |
| `TAXONOMY_TERM_UNKNOWN` | Term cannot be found in admitted taxonomy inputs. |
| `TAXONOMY_TERM_DUPLICATE` | Duplicate ids, aliases, slugs, or labels conflict. |
| `TAXONOMY_TERM_AMBIGUOUS` | Supplied label/alias resolves to multiple candidates without review. |
| `TAXONOMY_TERM_DEPRECATED` | Term is deprecated, replaced, withdrawn, or superseded. |
| `TAXONOMY_VERSION_STALE` | Vocabulary or taxonomy version is stale or unsupported. |
| `TAXONOMY_ROOT_UNTRUSTED` | Resolver consumed an untrusted or unadmitted taxonomy root. |
| `TAXONOMY_HIERARCHY_MISSING` | Required parent, child, broader, narrower, or path relation is missing. |
| `TAXONOMY_CROSSWALK_UNREVIEWED` | Crosswalk candidate lacks review, method, confidence/status, limitations, or release support. |
| `TAXONOMY_CROSSWALK_DRIFT` | Source and target vocabulary versions no longer align with accepted crosswalk posture. |
| `TAXONOMY_PROVENANCE_MISSING` | Required vocabulary ref, version, status, review state, hash, release ref, or rollback ref is absent. |
| `TAXONOMY_GENERATED_LABEL_DENIED` | Generated label, fuzzy match, or AI suggestion was treated as authority. |
| `PUBLIC_SURFACE_LEAKAGE_DENIED` | Candidate would expose unsupported taxonomy state to public API, map, tile, export, screenshot, graph, Focus Mode, embedding, or AI surfaces. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, evaluator error, timeout, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future layout

Future implementation should remain small and reversible:

```text
tools/validators/taxonomy_resolver/
├── README.md
├── validate_taxonomy_resolution.py      # PROPOSED; not confirmed
├── validate_taxonomy_crosswalk.py       # PROPOSED; not confirmed
├── validate_taxonomy_provenance.py      # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

Do not add executable validators, local vocabulary records, taxonomy datasets, accepted crosswalk ledgers, local schema files, source data, release records, or fixtures unless the placement decision is documented, the canonical authority relationship is explicit, and tests prove fail-closed behavior without granting taxonomy, public-surface, or release authority.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty placeholder at `tools/validators/taxonomy_resolver/README.md`.
- [x] It marks this path as taxonomy resolver validator routing, not canonical taxonomy authority, schema authority, contract authority, policy authority, evidence authority, proof/receipt storage, release record storage, public runtime, or AI authority.
- [x] It preserves fail-closed posture for missing, duplicate, stale, deprecated, ambiguous, untrusted, generated, or crosswalk-drifted terms.
- [x] It routes taxonomy helper code to `packages/taxonomy/`, source registries to `data/registry/`, schemas to `schemas/`, contracts to `contracts/`, policy to `policy/`, receipts/proofs to `data/`, release records to `release/`, fixtures to `fixtures/`, and tests to `tests/`.
- [x] It marks executable scripts, registry wiring, canonical taxonomy homes, vocabulary snapshots, schema ids, fixtures, tests, policy bundles, receipt emission, release integration, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to taxonomy resolver validators are searched and classified.
- [ ] Canonical taxonomy record homes, vocabulary snapshot homes, deprecation ledgers, and accepted crosswalk homes are verified.
- [ ] Taxonomy ref, term id, vocabulary ref, version, status, review state, hash, release ref, and rollback ref schema bindings are verified.
- [ ] Fixture files are added only as synthetic/minimized public-safe payloads with documented expected outcomes.
- [ ] Tests prove positive, negative, deny, restrict, hold, abstain, missing-term, duplicate-term, ambiguous-alias, stale-version, deprecated-term, untrusted-root, crosswalk-unreviewed, generated-label-denied, provenance-missing, and public-surface-blocked cases.
- [ ] CI invokes taxonomy resolver validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty placeholder with taxonomy resolver validator README. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
