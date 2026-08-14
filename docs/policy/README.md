<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-policy-readme
title: docs/policy/ — Human Policy Guidance Containment and Routing Lane
type: directory-readme
version: v1.0
status: draft; repository-grounded; containment-lane; noncanonical-under-directory-rules; migration-hold; non-policy-authority; non-release; non-publication
owners:
  - "@bartytime4life"
owner_status: "@bartytime4life is the confirmed CODEOWNERS fallback; independent documentation, policy, security, privacy, sensitivity, domain, and migration stewardship remains NEEDS VERIFICATION"
created: 2026-08-14
updated: 2026-08-14
policy_label: repository-public
current_path: docs/policy/README.md
owning_root: docs/
responsibility: "Document and contain the repository-present docs/policy lane, route readers to the owning doctrine, architecture, domain, security, standards, policy, contract, schema, validation, and release surfaces, and prevent explanatory or scaffold Markdown from becoming policy source or publication authority."
truth_posture: "CONFIRMED current lane inventory, one-byte prior README, child scaffold contents, adopted Directory Rules v2 placement law, canonical policy/ authority, and CODEOWNERS fallback / PROPOSED per-file convergence and retirement sequencing / UNKNOWN complete external consumers, final lane disposition, and independent stewardship / NEEDS VERIFICATION document-registry treatment, inbound-link closure, and accepted migration decisions"
evidence_commit: f90df7054d3bfa9d88d0bf3829e4b4b894705ffe
prior_blob: e25f1814e51579d5f55c0f1fe0135ddb28a47f4a
directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
policy_root_readme_blob: 52877f1befd3112f1aec0eb122669d3fdc2634e6
related:
  - docs/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/domains/people-dna-land/README.md
  - docs/domains/fauna/README.md
  - docs/security/README.md
  - docs/standards/README.md
  - policy/README.md
  - policy/domains/people-dna-land/README.md
  - policy/domains/fauna/README.md
  - contracts/policy/README.md
  - schemas/contracts/v1/policy/README.md
  - control_plane/document_registry.yaml
  - .github/CODEOWNERS
tags:
  - kfm
  - docs
  - policy-guidance
  - containment
  - migration-hold
  - non-authoritative
  - sensitivity
  - cite-or-abstain
notes:
  - "This same-path repair replaces a one-byte README whose complete content was the character y."
  - "The adopted Directory Rules v2 canonical docs direct-child map does not name docs/policy/; this README therefore contains and routes the current lane rather than declaring it canonical."
  - "No child file, executable policy rule, contract, schema, fixture, test, registry, receipt, proof, release object, runtime, or public surface is changed by this document."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/policy/` — Human Policy Guidance Containment and Routing Lane

`docs/policy/` is a repository-present documentation lane containing two small,
proposal-only policy-guidance scaffolds and an empty test placeholder. This README
makes that current state inspectable, routes readers to the responsibility roots
that actually own policy-related work, and prevents the lane from silently becoming
a second policy authority.

> [!IMPORTANT]
> **This path exists, but adopted Directory Rules v2 do not list `docs/policy/` as
> a canonical documentation lane.** The safe current posture is containment and
> migration review. Existing references remain readable; new substantive policy
> guidance should be placed by its primary responsibility under an adopted
> documentation lane.

> [!WARNING]
> **Executable policy source is singular under [`policy/`](../../policy/README.md).**
> A document in this folder cannot allow or deny an operation, authenticate consent,
> clear rights, downgrade sensitivity, establish evidence, approve release, or
> authorize publication.

> [!CAUTION]
> The current child scaffolds concern living-person/DNA geoprivacy and fauna
> sensitivity. Do not add real personal data, genomic material, exact protected
> locations, private-land details, consent tokens, restricted evidence, or
> reconstruction-enabling examples to this repository-facing lane.

**Quick navigation:** [Purpose](#purpose-and-authority) · [Status](#current-repository-state) · [Inventory](#current-direct-child-map) · [Routing](#authority-routing) · [Containment](#containment-contract) · [Sensitive content](#rights-sensitivity-and-public-exposure) · [Migration](#convergence-and-migration-discipline) · [Validation](#validation) · [Review](#ownership-and-review) · [Rollback](#correction-and-rollback) · [Open work](#open-verification-register)

---

## Purpose and authority

This README has a deliberately narrow responsibility:

1. describe the current `docs/policy/` contents without promoting them;
2. distinguish human explanation from policy, contract, schema, runtime, evidence,
   review, release, and publication authority;
3. route future work to the responsibility root that owns it;
4. preserve existing references while per-file convergence is decided;
5. make verification, migration, correction, and rollback requirements visible.

It does **not** decide the final home of either child scaffold, retire this lane,
create a compatibility alias, or amend Directory Rules.

| Field | Current contract |
|---|---|
| Path | `docs/policy/` |
| Owning root | `docs/` — human-readable explanation only |
| Current lane class | Repository-present containment lane; canonical status not established |
| Placement outcome for new substantive content | `HOLD` until the primary documentation responsibility and existing canonical equivalent are verified |
| Policy-source authority | [`policy/`](../../policy/README.md) |
| Semantic policy-object authority | [`contracts/policy/`](../../contracts/policy/README.md) |
| Machine-shape authority | [`schemas/contracts/v1/policy/`](../../schemas/contracts/v1/policy/README.md) |
| Public-path role | Repository-facing documentation only; never a normal policy-evaluation or data-serving path |
| Normal writers | Reviewed documentation changes on feature branches |
| Normal consumers | Maintainers, reviewers, domain stewards, and documents following retained links |
| Trust posture | Cite or abstain; fail closed where rights, sensitivity, consent, or public exposure is unresolved |

### Directory Rules basis

Accepted
[`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the exact Directory Rules v2 bytes at
[`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md).

Those rules establish that:

- `docs/` explains matters to humans but cannot create machine, policy, evidence,
  release, or data authority through prose;
- the canonical documentation map contains `adr/`, `architecture/`, `archive/`,
  `atlases/`, `doctrine/`, `domains/`, `registers/`, `runbooks/`, `security/`,
  `sources/`, and `standards/`;
- executable policy source is singular under `policy/`;
- a README is required where authority, exposure, mutation, or lifecycle behavior
  changes;
- compatibility and migration require explicit classification, single-write
  discipline, verified consumers, exit criteria, and rollback.

The same-path README repair is therefore a containment action inside the existing
`docs/` root. It does not authorize continued growth of `docs/policy/` as a
parallel lane.

[Back to top](#top)

---

## Current repository state

The evidence snapshot is `main@f90df7054d3bfa9d88d0bf3829e4b4b894705ffe`.

| Surface | Confirmed state | Safe interpretation |
|---|---|---|
| `docs/policy/README.md` | One byte: `y`; blob `e25f1814e51579d5f55c0f1fe0135ddb28a47f4a` | Broken placeholder, not a lane contract |
| Creation history | Added by commit `e4b50174944d27dc2b73aefc83f8487f5c809590` on 2026-08-14 | Supplies the legitimate creation date; does not establish authority |
| Direct entries | This README, one Markdown file, and two directories | Small containment surface |
| `living_persons_geoprivacy.md` | Explicit `PROPOSED scaffold`; source points to the People/DNA/Land DNA sublane | Not authoritative privacy or geoprivacy guidance |
| `sensitivity/` | Contains one `fauna.md` proposal scaffold and no child README | Not an accepted sensitivity documentation family |
| `tests/` | Contains only `.gitkeep` | No documentation or policy test implementation |
| Canonical policy root | `policy/README.md` is a current repository-grounded root contract | Policy-source work belongs under `policy/`, not here |
| Canonical docs map | Does not include a `policy/` direct-child lane | Per-file routing and lane disposition remain unresolved |
| Inbound references | Repository code search finds references to the child scaffold paths | Do not move or delete without a current consumer and link analysis |
| Runtime, release, or publication effect | None | Documentation presence cannot establish enforcement or public state |

### Material conclusion

**CONFIRMED:** the lane needs a real containment README.

**PROPOSED:** existing child documents should be classified and converged into
their owning documentation responsibilities.

**UNKNOWN:** whether external consumers, old bookmarks, generated reports, or
uninspected branches rely on the current paths.

**NEEDS VERIFICATION:** the accepted migration or retirement decision, complete
inbound-link closure, independent stewardship, and machine document-registry
disposition.

[Back to top](#top)

---

## Current direct-child map

This tree shows only the directory governed by this README and its direct
children, as required by the Directory Rules README profile.

```text
docs/policy/
├── README.md                         # containment, routing, and migration boundary
├── living_persons_geoprivacy.md      # PROPOSED scaffold; no policy authority
├── sensitivity/                      # contains one fauna scaffold; no child README
└── tests/                            # empty placeholder apart from .gitkeep
```

| Direct child | Current evidence | Current posture |
|---|---|---|
| [`living_persons_geoprivacy.md`](living_persons_geoprivacy.md) | Names [`docs/domains/people-dna-land/sublanes/dna.md`](../domains/people-dna-land/sublanes/dna.md) as its source and asks for later authoritative content | `HOLD`; compare domain, security/privacy, standards, and executable-policy responsibilities before editing |
| [`sensitivity/`](sensitivity/) | Contains `fauna.md`, which names [`docs/domains/fauna/IDENTITY_MODEL.md`](../domains/fauna/IDENTITY_MODEL.md) as its source | `HOLD`; no accepted child-lane contract or final documentation home |
| [`tests/`](tests/) | Contains only `.gitkeep` | `HOLD`; a directory name does not prove a test family or justify future test content here |

No child is promoted, accepted, activated, released, or made canonical by this
inventory.

[Back to top](#top)

---

## Authority routing

Policy-related material is routed by **primary responsibility**, not by the word
“policy.”

| Primary responsibility | Owning surface | Examples |
|---|---|---|
| Stable KFM operating law | [`docs/doctrine/`](../doctrine/) | Cite-or-abstain, lifecycle, trust-membrane doctrine |
| Architecture decision | [`docs/adr/`](../adr/) | Accepted or proposed decisions and supersession |
| Policy-system architecture | [`docs/architecture/`](../architecture/) | Evaluator boundaries, consumer flow, contract/schema/policy split |
| Domain explanation | [`docs/domains/<domain>/`](../domains/) | Fauna geoprivacy guidance, People/DNA/Land scope and limitations |
| Security, privacy, threat, or exposure guidance | [`docs/security/`](../security/) | Threat models, public-exposure risks, incident guidance |
| External or KFM standards profile | [`docs/standards/`](../standards/) | Consent, privacy, provenance, or data-use standards mappings |
| Operational procedure | [`docs/runbooks/`](../runbooks/) | Policy rollout, deactivation, correction, or incident response |
| Drift, verification, or unresolved authority | [`docs/registers/`](../registers/) | Migration holds, contradictions, verification backlog |
| Executable admissibility rule | [`policy/`](../../policy/) | Rego, OPA-compatible, or equivalent reviewed policy source |
| Policy-object meaning | [`contracts/policy/`](../../contracts/policy/) | `PolicyInputBundle`, `PolicyDecision`, reasons, obligations |
| Machine-valid policy-object shape | [`schemas/contracts/v1/policy/`](../../schemas/contracts/v1/policy/) | JSON Schema and versioned constraints |
| Policy evaluator or reusable runtime | Accepted app/package/runtime implementation | Evaluator, adapter, decision normalization, consumer client |
| Synthetic fixtures and executable tests | [`fixtures/`](../../fixtures/) and [`tests/`](../../tests/) | Positive, negative, fail-closed, and compatibility coverage |
| Emitted decision, receipt, proof, review, or release object | Its governed data, review, proof, or release family | Historical process and release state, never policy source |

### Anti-collapse rule

A human document may explain an accepted rule and link to its source. It must not
copy the rule into an independently writable second authority. When a description
and executable policy disagree, preserve the discrepancy, identify the owning
authority, and route correction through review rather than choosing whichever text
is more convenient.

[Back to top](#top)

---

## Containment contract

While lane disposition remains unresolved, the following content is permitted here:

- this README;
- the current proposal scaffolds, unchanged except for bounded correction or
  migration preparation;
- explicit tombstone, alias, or migration facts after an accepted decision;
- links that route readers to the current owning policy, domain, security, standards,
  contract, schema, validation, and release surfaces;
- current evidence and verification status.

The following is **not** permitted as new substantive content:

- executable policy rules, bundles, package namespaces, or evaluator configuration;
- machine schemas, DTOs, enumerations, or generated language bindings;
- semantic contracts duplicated from `contracts/policy/`;
- domain doctrine that should evolve under `docs/domains/`;
- security or privacy guidance that should evolve under `docs/security/`;
- test implementations or fixtures;
- emitted `PolicyDecision`, consent, review, receipt, proof, release, correction, or
  rollback instances;
- real sensitive data or exact protected geometry;
- a new `docs/policy/<topic>/` hierarchy used to bypass placement review.

### New-content rule

Before adding or materially expanding a file under this lane, reviewers must answer:

1. What one human-document responsibility owns the content?
2. Which adopted documentation lane owns that responsibility?
3. Does a current document already serve the same role?
4. Is the current path required by a verified consumer?
5. Would the change create a parallel writable authority?
6. What migration, compatibility, validation, and rollback evidence is required?

If these questions do not produce one supportable home, the result is `HOLD`.

[Back to top](#top)

---

## Human policy-guidance contract

A policy-related human document, wherever it ultimately belongs, should keep the
following distinctions visible.

| Requirement | Minimum expectation |
|---|---|
| Identity | Stable document ID, title, path, status, version, and owning documentation responsibility |
| Scope | Operation, audience, domain, geography, time, and explicit exclusions |
| Authority | Accepted doctrine/ADR, policy package or entrypoint, semantic contract, schema, and release relationship |
| Evidence posture | What is confirmed, proposed, unknown, stale, conflicted, or still needs verification |
| Input model | Governed references required for source, evidence, rights, consent, sensitivity, lifecycle, review, and release |
| Outcome model | Contract-defined finite outcomes, reasons, and obligations; no invented vocabulary |
| Fail-closed behavior | Missing or untrusted context remains denied, held, restricted, or abstained as the owning policy specifies |
| Sensitivity | Public-safe examples, precision limits, reconstruction risk, and protected reason handling |
| Validation | Fixtures, tests, validator/evaluator profile, version, digest, and current execution evidence |
| Consumers | Governed APIs, applications, release gates, or operators that consume the result |
| Non-effects | No factual truth, consent inference, policy activation, promotion, release, or publication by documentation alone |
| Correction and rollback | Supersession, deactivation, correction propagation, and restoration target |

Do not use this README to normalize unresolved engine-native and outward runtime
vocabularies. The accepted semantic contract and evaluator binding must define that
translation.

[Back to top](#top)

---

## Inputs, outputs, and writers

### Permitted inputs

Human policy guidance may consume and cite:

- accepted doctrine and ADRs;
- current policy rule source, bundle declarations, entrypoints, and digests;
- semantic contracts and machine schemas;
- synthetic fixtures, tests, validator reports, and bounded workflow results;
- SourceDescriptor, EvidenceRef, EvidenceBundle, rights, consent, sensitivity,
  lifecycle, review, release, correction, and rollback references;
- authoritative external standards or legal guidance when currentness and
  jurisdiction are recorded.

A source becomes neither accepted nor authoritative merely because a document
mentions it.

### Permitted outputs

This containment lane may output only human-readable navigation, boundary,
verification, correction, and migration guidance. It emits no policy decision,
obligation execution, evidence closure, test result, review record, release state,
or public artifact.

### Writers

Changes are made through reviewed repository work. The current GitHub review route
falls through to `@bartytime4life`; CODEOWNERS is routing, not proof of policy,
privacy, sensitivity, domain, legal, security, release, or independent review.

Automation may validate or propose documentation. It must not treat its own prose,
metadata, badge, receipt, workflow, or pull request as approval.

[Back to top](#top)

---

## Rights, sensitivity, and public exposure

`docs/` is repository-facing and may be publicly readable. Public documentation
must not expose the protected payload while explaining that a protection exists.

### Fail-closed subjects

Apply heightened review to:

- living-person identity, location, behavior, contact, family, health, or financial
  information;
- DNA, genomic, genealogy, kinship, and consent or revocation state;
- private-land, parcel, title, ownership, tenancy, or person–parcel joins;
- rare, threatened, harvested, nesting, denning, breeding, roosting, or otherwise
  sensitive fauna locations;
- archaeology, cultural knowledge, sacred places, sovereignty, tribal information,
  infrastructure, private wells, and other harmful-precision subjects;
- reasons, thresholds, or transformations whose disclosure could reconstruct the
  protected information.

### Documentation rules

- Use synthetic or irreversibly generalized examples.
- Describe categories and obligations without embedding real protected records.
- Do not commit consent tokens, private identifiers, credentials, signed URLs, or
  source payloads.
- Do not infer consent, rights, sensitivity, or public safety from missing data.
- Do not use client-side hiding as a substitute for pre-release transformation.
- Record redaction or generalization concepts without leaking the removed value.
- Route a consequential disclosure question to the owning policy and qualified
  reviewer; documentation prose cannot waive the requirement.

[Back to top](#top)

---

## Convergence and migration discipline

This README does not pick migration targets. It records the questions that must be
answered before structural action.

| Current item | Primary-responsibility candidates | Current result | Evidence needed before action |
|---|---|---|---|
| `living_persons_geoprivacy.md` | People/DNA/Land domain explanation; security/privacy guidance; standards profile | `HOLD` | Compare current domain and security docs, policy consumers, standards references, stable identity, inbound links, and qualified review |
| `sensitivity/fauna.md` | Fauna domain explanation; security/geoprivacy guidance; standards profile | `HOLD` | Compare current fauna docs, domain and sensitivity policy lanes, source-role boundaries, inbound links, and public-safe review |
| `tests/` | No supported documentation responsibility established | `HOLD` | Verify writers, consumers, intended test type, and whether the placeholder can be retired |
| This README | Containment and navigation while referenced paths remain | `PLACE` for current containment only | Revisit after child migrations and zero-consumer proof |

### Required migration sequence

A future move, rename, consolidation, or retirement must:

1. freeze the current tree, identities, content digests, producers, consumers, and
   governing decisions;
2. classify each file by one primary responsibility;
3. verify a unique target under adopted Directory Rules;
4. inspect current and external inbound references;
5. preserve stable document identity or record a versioned identity change;
6. use canonical single-write and bounded dual-read only when a verified consumer
   requires it;
7. update links, document registry candidates, indexes, generators, and consumers;
8. run metadata, link, graph, staleness, topology, sensitivity, and changed-area
   validation;
9. retain correction and rollback evidence;
10. prove zero writers and zero consumers before retiring the old path.

Do not bulk-move files by filename or topic. A migration must not create two writable
authorities.

[Back to top](#top)

---

## Validation

Documentation checks provide quality evidence only. They do not prove policy
correctness, policy activation, runtime enforcement, release approval, or
publication.

| Check | Applies to this README | Boundary |
|---|:---:|---|
| [`docs-meta-block`](../../.github/workflows/docs-meta-block.yml) | Yes | Validates changed metadata and emits a review-only registry delta |
| [`link-check`](../../.github/workflows/link-check.yml) | Yes | Validates changed local targets; external URLs remain unrequested |
| [`docs-document-graph`](../../.github/workflows/docs-document-graph.yml) | Yes | Builds a bounded documentation graph projection |
| [`docs-stale-scan`](../../.github/workflows/docs-stale-scan.yml) | Yes | Reports changed-file freshness and verification debt |
| [`docs-build`](../../.github/workflows/docs-build.yml) | Yes | Records the explicit generator/preview hold; it does not publish |
| Directory-topology validation | Yes | Detects new drift; this change must not admit a new canonical lane |
| Policy-rule or evaluator tests | No behavior changed | This README changes no policy source or evaluator |
| Rights and sensitivity review | Yes | Confirms no protected data or harmful precision is introduced |

### Changed-file acceptance checks

- `KFM_META_BLOCK_V2` parses under the repository validator.
- Exactly one H1 exists.
- Fences, tables, alerts, and explicit anchors are balanced.
- Every introduced local link resolves with correct case.
- The direct-child map matches the inspected tree.
- No child file is silently promoted.
- No policy source, schema, contract, runtime, fixture, test, decision, receipt,
  proof, release, or publication state is created.
- No real sensitive data, secret, credential, or protected exact location appears.
- The diff remains limited to this README unless a directly caused validation defect
  requires a bounded repair.

[Back to top](#top)

---

## Ownership and review

[`CODEOWNERS`](../../.github/CODEOWNERS) has no `docs/policy/`-specific rule, so
the repository-wide fallback routes review to `@bartytime4life`.

Additional review is required according to content:

| Change | Required review class |
|---|---|
| Policy-system meaning or outcome vocabulary | Policy, contract, schema, and runtime owners |
| Living-person, DNA/genomic, genealogy, land/title, or consent content | Domain, privacy, consent, rights, sensitivity, and security reviewers |
| Fauna sensitivity or geoprivacy content | Fauna, source, rights, biodiversity, sensitivity, and geoprivacy reviewers |
| External standard or legal interpretation | Standards steward plus qualified legal/privacy/domain review |
| Move, alias, consolidation, or retirement | Documentation governance, Directory Rules, affected owner, and migration review |
| Public or semi-public guidance | Policy, sensitivity, release, correction, and rollback review appropriate to consequence |

The independent role assignments remain `NEEDS VERIFICATION`. Do not encode
placeholder role names as executable GitHub owners.

[Back to top](#top)

---

## Correction and rollback

### Documentation correction

A correction to this README should identify:

- the affected claim or inventory row;
- the current repository evidence;
- whether a child, governing decision, or authority route changed;
- links or consumers requiring propagation;
- the prior blob or forward-fix target.

### Rollback

This change modifies one file. The exact prior blob is
`e25f1814e51579d5f55c0f1fe0135ddb28a47f4a`, whose content is the single
character `y`.

A reviewed revert can restore that blob mechanically, but doing so would recreate
the broken placeholder. Unless rollback is required for repository integrity, a
reviewed forward fix is safer. No child file or operational state needs rollback
because none is changed here.

A future structural migration needs its own migration record and rollback plan.
Reverting this README cannot undo moved files, aliases, consumer updates, or
generated indexes.

[Back to top](#top)

---

## Open verification register

| Item | Status | Closure evidence |
|---|---|---|
| Final class and lifetime of `docs/policy/` | `NEEDS VERIFICATION` | Accepted documentation-lane or migration decision |
| Canonical target for each child scaffold | `HOLD` | Per-file responsibility classification and existing-equivalent comparison |
| Complete repository and external inbound references | `UNKNOWN` | Current recursive search plus known external-consumer inventory |
| `living_persons_geoprivacy.md` ownership and qualified review | `NEEDS VERIFICATION` | Domain/privacy/security/standards disposition |
| `sensitivity/fauna.md` ownership and qualified review | `NEEDS VERIFICATION` | Fauna/geoprivacy/security/standards disposition |
| Purpose of `docs/policy/tests/` | `UNKNOWN` | Verified writer, consumer, test type, or zero-use proof |
| Independent documentation and policy stewardship | `NEEDS VERIFICATION` | Approved assignments and repository access |
| Machine document-registry disposition | `NEEDS VERIFICATION` | Review of the `docs-meta-block` registry delta |
| Compatibility window and exit criteria | `UNKNOWN` | Accepted migration plan and verified consumers |
| Branch-protection and required-check coupling | `NEEDS VERIFICATION` | Repository settings evidence; workflow presence is insufficient |
| Public release or runtime enforcement | `NONE` | Separate governed implementation and release evidence |

[Back to top](#top)

---

## Related documentation

- [Documentation root contract](../README.md)
- [Adopted Directory Rules bytes](../doctrine/directory-rules.md)
- [Accepted ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Human drift register](../registers/DRIFT_REGISTER.md)
- [Human verification backlog](../registers/VERIFICATION_BACKLOG.md)
- [People, DNA, and Land domain guidance](../domains/people-dna-land/README.md)
- [Fauna domain guidance](../domains/fauna/README.md)
- [Security documentation lane](../security/README.md)
- [Standards documentation lane](../standards/README.md)
- [Canonical policy-source root](../../policy/README.md)
- [People, DNA, and Land policy boundary](../../policy/domains/people-dna-land/README.md)
- [Fauna policy boundary](../../policy/domains/fauna/README.md)
- [Policy semantic contracts](../../contracts/policy/README.md)
- [Policy machine schemas](../../schemas/contracts/v1/policy/README.md)
- [Machine document registry](../../control_plane/document_registry.yaml)

---

## Evidence review triggers

Re-review this containment contract when:

- an ADR or documentation-lane decision classifies `docs/policy/`;
- either child scaffold gains a reviewed canonical successor;
- a current consumer requires a compatibility alias;
- the direct inventory changes;
- `policy/`, domain policy, domain documentation, security, or standards boundaries
  change materially;
- CODEOWNERS, document-registry, topology, or documentation QA coverage changes;
- sensitivity, rights, consent, correction, withdrawal, or rollback requirements
  change;
- a migration reaches single-write, dual-read, zero-consumer, or retirement state.

**Last evidence review:** 2026-08-14 against
`main@f90df7054d3bfa9d88d0bf3829e4b4b894705ffe`.

## Status

**CONFIRMED:** same-path repair of a one-byte README; current direct-child
inventory; adopted Directory Rules and canonical `policy/` authority; no child or
runtime change.

**PROPOSED:** per-file convergence after responsibility and consumer review.

**UNKNOWN / NEEDS VERIFICATION:** final lane disposition, migration targets,
complete consumers, independent stewardship, registry treatment, and any public or
runtime effect.

[Back to top](#top)
