<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0035-repository-wide-adr-identity-numbering-domain-indexing
title: "ADR-0035 — Repository-Wide ADR Identity, Numbering, and Domain Indexing"
type: adr
adr_id: ADR-0035
version: v1.0
status: proposed
effective_decision_status: proposed
owners:
  - "OWNER_TBD — architecture decision owner"
  - "OWNER_TBD — documentation governance steward"
  - "OWNER_TBD — affected domain stewards"
owner_status: "CODEOWNERS routes repository review to @bartytime4life; accepted stewardship, decision quorum, independent review, and authority to accept this decision remain unverified"
reviewers_required:
  - Architecture steward
  - Docs steward
  - At least one affected domain steward
  - Directory-governance reviewer
  - Validation and CI steward
created: 2026-08-14
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
owning_root: docs/
responsibility_root: docs/
responsibility: "Record the proposed repository-wide ADR identity, numbering, indexing, domain-discovery, migration, and supersession model without accepting any decision or moving any existing scaffold."
current_path: docs/adr/ADR-0035-repository-wide-adr-identity-numbering-and-domain-indexing.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3974da9794fa11bd5355c49243c9193d22b9e81e
  base_tree: 193f52bf6439ea9f39d762db905623ef31d78faf
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  adr_readme_blob: 793015c38f4066c2c23753d4e3dd26bcc890279d
  adr_cross_register_blob: c1cb6af908e4a8170d21ebb4f63c263804d020e8
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  fauna_domain_adr_index_path: docs/domains/fauna/adr/README.md
inspection_boundary: >
  Current-session GitHub reads covered current main, the canonical ADR operating
  contract and index, the non-duplicating ADR cross-register, accepted ADR-0029,
  adopted Directory Rules v2, the ADR validator, the twelve unassigned scaffolds
  recorded by the canonical index, and the Fauna domain ADR index that preserves
  the unresolved central-versus-domain placement and numbering questions. No
  ADR acceptance review, domain-steward quorum, repository setting, merge,
  release, deployment, publication, or migration was exercised.
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-template.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/registers/ADR_INDEX.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/domains/fauna/adr/README.md
  - tools/validators/validate_adr_index.py
  - tests/validators/test_validate_adr_index.py
  - .github/workflows/docs-control-plane.yml
tags: [kfm, adr, governance, identity, numbering, indexing, domains, scaffolds, migration, supersession]
notes:
  - "This record assigns ADR-0035 under the current repository-wide sequence while preserving proposed status; assignment is inventory identity, not acceptance."
  - "The decision is additive to accepted Directory Rules v2: docs/adr/ remains the decision-record lane, while docs/domains/ remains a human domain-guidance lane."
  - "No existing unassigned scaffold is renamed, deleted, accepted, rejected, or superseded by this documentation-only packet."
  - "Domain-local adr/ directories remain untouched and retain no new authority through this proposal."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0035 — Repository-Wide ADR Identity, Numbering, and Domain Indexing

> **Proposed decision.** KFM will use one permanent repository-wide `ADR-NNNN` identity sequence for every architecture decision, including decisions whose substantive scope is limited to one domain. Numbered decision records live directly under `docs/adr/`; domain documentation may maintain pointer-only ADR indexes for discovery, but it must not create a second numbering authority or a parallel store of binding decision records.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![ADR identity: assigned](https://img.shields.io/badge/ADR--0035-assigned-0969da?style=flat-square)](#status)
[![Canonical inventory: one](https://img.shields.io/badge/canonical%20inventory-one-1a7f37?style=flat-square)](#canonical-inventory)
[![Domain indexes: pointer only](https://img.shields.io/badge/domain%20indexes-pointer%20only-8250df?style=flat-square)](#domain-discovery-indexes)
[![Scaffold migration: none](https://img.shields.io/badge/scaffold%20migration-none-6e7781?style=flat-square)](#non-effects)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **Identity is assigned; the decision is not accepted.** Adding this file and its canonical index row establishes a collision-free repository identity only. The source record and index remain `proposed`. No scaffold, domain decision, policy, implementation, release, or public behavior becomes binding by implication.

> [!CAUTION]
> **This proposal does not perform the convergence it describes.** The repository currently contains twelve unassigned placeholder or slug-only ADR scaffolds and at least one domain ADR index that records unresolved numbering and placement questions. Those files remain in place until separately reviewed migration packets classify overlap, preserve source lineage, assign numbers where warranted, and validate references.

> [!WARNING]
> **A domain label does not create a separate decision authority.** A decision may be domain-scoped, require domain-steward review, and be indexed from a domain dossier while still using the repository-wide permanent ID and canonical decision lane.

**Quick navigation:** [Status](#status) · [Evidence](#evidence-boundary) · [Context](#context) · [Decision](#decision) · [Identity](#permanent-identity-and-numbering) · [Domain indexes](#domain-discovery-indexes) · [Scaffolds](#candidate-and-scaffold-identities) · [Inventory](#canonical-inventory) · [Authority](#authority-and-publication-boundary) · [Migration](#migration-and-convergence-plan) · [Acceptance](#acceptance-gates) · [Consequences](#consequences) · [Alternatives](#alternatives-considered) · [Risks](#risk-ledger) · [Rollback](#rollback-and-supersession) · [Validation](#validation) · [Open questions](#open-questions) · [References](#references) · [History](#revision-history)

---

<a id="status"></a>

## Status

| Field | Current value |
| --- | --- |
| **ADR ID** | `ADR-0035` — unique at the evidence checkpoint |
| **Tracked path** | `docs/adr/ADR-0035-repository-wide-adr-identity-numbering-and-domain-indexing.md` |
| **Source metadata** | `proposed` |
| **Effective decision status** | `proposed` |
| **Decision class** | Repository-wide architecture-decision identity, numbering, discovery, indexing, migration, and supersession |
| **Primary responsibility root** | `docs/` — human architecture decision record |
| **Canonical decision lane** | `docs/adr/` under accepted Directory Rules v2 |
| **Current numbered inventory after this packet** | 35 records: `ADR-0001` through `ADR-0035` |
| **Current unassigned scaffold inventory** | 12; unchanged by this packet |
| **Implementation effect** | Documentation control-plane update only |
| **Migration effect** | None |
| **Release/publication effect** | None |
| **Supersedes / superseded by** | None / none |

### Assignment, acceptance, implementation, and release are separate

1. **Number assignment** gives a decision record stable repository identity and makes it discoverable in the canonical inventory.
2. **ADR acceptance** approves the decision through explicit reviewed status evidence in the source record and index.
3. **Implementation or migration** changes repository behavior or paths under the accepted decision and its own validation/rollback plan.
4. **Release or publication** authorizes a specific governed outward effect through separate release authority.

None of these transitions implies the next. A numbered ADR can remain proposed indefinitely. A merged proposed ADR does not authorize the migration it describes.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This record is grounded in current repository evidence at `main@3974da9794fa11bd5355c49243c9193d22b9e81e`.

| Surface | CONFIRMED observation | Bounded meaning |
| --- | --- | --- |
| `docs/adr/INDEX.md` | The canonical inventory contains one contiguous sequence from `ADR-0001` through `ADR-0034`, one accepted decision, 33 proposed decisions, and 12 unassigned scaffolds. | A central inventory already operates; it does not by itself settle domain-local decision placement. |
| `docs/adr/README.md` | The ADR operating contract requires permanent `ADR-NNNN-kebab-case-slug.md` identities, same-change index updates, and conservative status handling. | Current process evidence; individual decisions remain proposed until reviewed. |
| `docs/registers/ADR_INDEX.md` | The register is intentionally a non-duplicating pointer to `docs/adr/INDEX.md`. | KFM already rejects a second repository-wide ADR row set. |
| Accepted ADR-0029 | Exact Directory Rules v2 bytes are adopted at `docs/doctrine/directory-rules.md`. | Placement authority is accepted within ADR-0029's scope. |
| Directory Rules v2 | `docs/adr/` owns architecture decisions and decision history; `docs/domains/` owns human domain guidance. | Supports one canonical decision lane and domain pointer indexes rather than parallel ADR stores. |
| ADR validator | It enforces unique numbered files, exact index coverage, filename/H1 agreement, source/effective status parity, scaffold separation, and supersession reciprocity. | The current machine gate can enforce the proposed global identity model after acceptance. |
| Fauna domain ADR index | It explicitly records central-versus-domain placement and domain-numbering questions as unresolved while treating the local file as an index. | Direct evidence of the ambiguity this ADR is designed to settle. |
| Open PR and branch review | No open pull request or branch matching ADR-0035 or this exact decision topic was found immediately before authoring. | Number collision was not observed at the checkpoint; later concurrency still requires exact-head recheck. |

### Truth labels

| Label | Use here |
| --- | --- |
| **CONFIRMED** | Verified from current repository bytes or accepted Directory Rules evidence |
| **PROPOSED** | The decision, future migration, or review model described by this record |
| **NEEDS VERIFICATION** | A concrete owner, consumer, migration, or review check remains |
| **UNKNOWN** | Available evidence cannot establish the state |
| **CONFLICTED** | Current documentation describes incompatible numbering or placement models |
| **HOLD** | Do not assign, move, or retire a candidate until evidence and review close |

[Back to top](#top)

---

<a id="context"></a>

## Context

KFM currently has a functioning repository-wide ADR inventory and a separate set of unassigned decision candidates:

- explicit `ADR-NNNN-*` and `ADR-XXXX-*` placeholders;
- slug-only `ADR-*.md` scaffolds;
- Atlas backlog identifiers such as `ADR-S-*`;
- domain-planning identifiers such as `ADR-FAUNA-*`;
- domain-local `adr/` indexes that are intended as discovery surfaces but describe their own placement and numbering rules as unresolved.

These forms are useful during discovery, but they become dangerous when they are treated as interchangeable permanent identities. The same decision can be copied under several names, a domain can appear to override a repository-wide decision, and an index can silently become a second authority.

The current ADR operating contract already provides much of the necessary mechanism: one numbered sequence, one canonical index, source/effective status separation, complete scaffold inventory, and reciprocal supersession checks. What remains undecided is whether that mechanism is the permanent model for domain-scoped decisions and how historical candidate identifiers converge without lost lineage.

### Problem statement

Without an accepted identity and indexing decision, KFM risks:

1. allocating the same permanent number to concurrent work;
2. maintaining separate global and domain sequences with ambiguous precedence;
3. treating `ADR-S-*`, `ADR-FAUNA-*`, `ADR-XXXX`, or slug-only paths as accepted decisions;
4. copying binding decision bodies into domain folders;
5. losing inbound links and source lineage during ad hoc renames;
6. accepting a decision through an index edit rather than explicit reviewed source status;
7. deleting rejected or superseded history instead of retaining it;
8. creating competing machine projections of the ADR set.

[Back to top](#top)

---

<a id="decision"></a>

## Decision

If accepted, KFM will apply the following rules.

### 1. One permanent repository-wide sequence

Every permanent architecture decision uses exactly one four-digit ID:

```text
ADR-NNNN
```

The ID is allocated from the next collision-free value in the canonical repository-wide sequence. The sequence is global across all domains, applications, packages, object families, source families, infrastructure, security, policy boundaries, and documentation-governance decisions.

### 2. One canonical decision-record lane

The permanent human decision record lives directly under:

```text
docs/adr/ADR-NNNN-kebab-case-slug.md
```

This follows accepted Directory Rules v2: `docs/adr/` owns architecture decisions and decision history. A domain, source, county, renderer, package, or feature name may appear in the slug and metadata but does not create another decision root.

### 3. Domain scope is metadata and review burden, not a numbering authority

A domain-scoped decision:

- uses the global `ADR-NNNN` sequence;
- names affected domains and required domain reviewers in metadata;
- links to domain contracts, schemas, policy, tests, and docs;
- may be surfaced by a domain-local pointer index;
- cannot contradict an accepted repository-wide ADR through a local override.

A genuine exception to a cross-cutting decision requires a new repository-wide numbered ADR that explicitly amends or supersedes the controlling decision.

### 4. Candidate identifiers remain non-permanent until assignment

The following are candidate or lineage identities, not permanent ADR IDs:

- `ADR-NNNN-*`;
- `ADR-XXXX-*`;
- slug-only `ADR-*.md` scaffolds;
- `ADR-S-*` Atlas backlog IDs;
- `ADR-<DOMAIN>-*` planning IDs;
- issue numbers, idea-card IDs, document section IDs, and filenames without a four-digit assignment.

A candidate may cite these historical identities in its source lineage. Assignment requires a separately reviewed rename/create-and-index packet; acceptance remains a later decision.

### 5. Number assignment does not accept the decision

A new numbered record begins with effective status `proposed`. The canonical index records source metadata and effective status separately. A number assignment, file presence, pull request, workflow pass, merge, generated receipt, or domain-index link cannot promote the decision.

### 6. Permanent IDs are never reused

Once assigned, an `ADR-NNNN` remains bound to that decision history even if the record becomes rejected or superseded. Historical records are retained. A later decision receives a new number and links through `supersedes` / `superseded_by`.

### 7. One canonical per-record inventory

`docs/adr/INDEX.md` is the only human row-level inventory of numbered records and unassigned scaffolds.

Other surfaces may:

- point to the canonical index;
- summarize counts and status;
- filter or group links for a domain or subsystem;
- project accepted decisions for machine enforcement.

They may not maintain a competing complete row set or independently change status.

### 8. Machine projections are subordinate

Any future `control_plane/` ADR projection must be generated or validated against accepted source ADRs and the canonical index. Editing a projection cannot assign a number, accept a decision, establish supersession, or alter source status.

### 9. Renames preserve lineage and compatibility

When a scaffold or legacy path becomes numbered:

1. inspect exact-path and topical overlap;
2. preserve source attribution and useful content;
3. assign the next collision-free ID;
4. update filename, H1, metadata, and canonical index together;
5. repair inbound links or provide a time-bounded compatibility pointer where a verified consumer requires one;
6. record the prior candidate identity inside the new ADR;
7. validate link, index, status, and supersession closure;
8. retain rollback instructions.

### 10. Decision bodies are not duplicated for convenience

A domain index or architecture overview links to the central ADR. It may summarize the decision's relevance but must not copy a writable binding decision body. If a local document needs distinct normative content, that is evidence the concerns should be split into separate artifacts with separate authority owners.

[Back to top](#top)

---

<a id="permanent-identity-and-numbering"></a>

## Permanent identity and numbering

### Allocation protocol

Before assigning a number:

1. fetch current `main` and record the exact SHA;
2. inspect `docs/adr/INDEX.md`;
3. search open pull requests and active branches for the next number and the decision topic;
4. inspect unassigned scaffolds for overlap;
5. select the next unused number;
6. create or rename the record and update the canonical index in the same commit or dependency-closed pull request;
7. run repository-native ADR validation;
8. keep status `proposed` unless the same packet contains explicit, authorized acceptance evidence.

### Identity grammar

| Field | Rule |
| --- | --- |
| Permanent ID | `ADR-` plus exactly four decimal digits |
| Filename | `ADR-NNNN-kebab-case-slug.md` |
| H1 | Must contain the same `ADR-NNNN` |
| Metadata | Must expose a supported source status |
| Canonical index | Must link to the exact tracked filename |
| Reuse | Forbidden |
| Renumbering | Forbidden after merge except through an explicit correction for an unmerged or demonstrably erroneous assignment |
| Domain classification | Metadata, tags, related paths, and pointer indexes |
| Acceptance | Explicit reviewed status transition, independent from assignment |

### Concurrency posture

The canonical sequence is repository state, not a reservation service. If two branches assign the same next number, neither branch may infer priority from creation time alone. The later integration packet must rebase or renumber before merge, preserving any public discussion links and updating generated receipts.

[Back to top](#top)

---

<a id="domain-discovery-indexes"></a>

## Domain discovery indexes

A domain may retain a path such as:

```text
docs/domains/<domain>/adr/README.md
```

only as a **pointer index** when it improves domain discovery.

### Allowed contents

- links to relevant central numbered ADRs;
- domain impact summaries;
- accepted/proposed/superseded status copied from the canonical source with a visible “derived” label;
- domain reviewer guidance;
- domain-specific open questions that may later mature into central ADR candidates;
- links to contracts, schemas, policy, tests, runbooks, and release guidance.

### Forbidden contents

- a second permanent numbering sequence;
- writable copies of central ADR bodies;
- local acceptance or supersession authority;
- status that disagrees with the source ADR;
- a domain override of a repository-wide accepted decision;
- machine policy or schema disguised as a decision index.

### Update behavior

Domain indexes should be updated when domain discovery materially changes, but they are not required in every ADR packet. A missing domain index link does not invalidate the central ADR. A stale domain index is documentation drift and must not change the source decision.

[Back to top](#top)

---

<a id="candidate-and-scaffold-identities"></a>

## Candidate and scaffold identities

### Current candidate classes

| Candidate form | Current role | Proposed long-term disposition |
| --- | --- | --- |
| `ADR-NNNN-*` | Explicit unassigned placeholder | Assign a number only after overlap and decision-scope review |
| `ADR-XXXX-*` | Explicit unassigned placeholder | Same as above |
| Slug-only `ADR-*.md` | Unassigned scaffold or developed candidate | Number, merge, retire, or preserve as non-ADR planning lineage through reviewed cleanup |
| `ADR-S-*` | Atlas/open-decision backlog identity | Cross-reference from a permanent ADR or retain as backlog lineage |
| `ADR-<DOMAIN>-*` | Domain-planning identity | Map to a central permanent ADR when the decision is admitted |
| Domain-local ADR row | Discovery entry | Point to the central source record |

### Admission test for numbering a scaffold

A scaffold is ready for permanent numbering only when:

- the decision is genuinely ADR-class;
- its scope is coherent and not already decided elsewhere;
- overlap with numbered ADRs and other scaffolds has been reconciled;
- owners and required reviewers are identified at least by role;
- context, decision, consequences, alternatives, migration, rollback, validation, and open questions are substantive;
- placement follows accepted Directory Rules;
- source lineage is preserved;
- the packet can pass canonical index validation.

Minimal placeholder text is not sufficient merely because the path has existed for a long time.

[Back to top](#top)

---

<a id="canonical-inventory"></a>

## Canonical inventory

The human control surfaces remain intentionally separated:

| Path | Responsibility | Authority limit |
| --- | --- | --- |
| `docs/adr/README.md` | ADR authoring, status, review, and validation rules | Does not accept individual decisions |
| `docs/adr/INDEX.md` | Canonical file-to-ID and status inventory | Cannot promote a source record independently |
| `docs/registers/ADR_INDEX.md` | Cross-register pointer and consumer map | Must not duplicate numbered rows |
| `docs/domains/<domain>/adr/README.md` | Optional domain discovery index | No numbering or decision authority |
| `control_plane/` projection | Machine-readable accepted-decision projection | Cannot mint or accept decisions |

If counts or summaries disagree, the exact source ADR files plus `docs/adr/INDEX.md` control inventory interpretation; the disagreement is documentation drift, not a status transition.

[Back to top](#top)

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

This ADR, if accepted, would decide identity and indexing only.

It would not:

- accept any currently proposed ADR;
- reject or supersede any ADR;
- assign permanent IDs to the twelve current scaffolds;
- rename, move, delete, consolidate, or retire current files;
- amend the substantive decision recorded by another ADR;
- authorize domain policy, schema, source activation, migration, implementation, release, deployment, or publication;
- create a machine registry that can override source records;
- prove independent review or decision quorum.

A generated receipt records authorship and validation evidence. It is not human review, acceptance, merge authority, or publication authority.

[Back to top](#top)

---

<a id="non-effects"></a>

## Non-effects of this packet

The initial ADR-0035 packet is intentionally documentation-only:

- **No scaffold mutation.**
- **No domain-index mutation.**
- **No status promotion.**
- **No supersession relationship.**
- **No code, schema, policy, workflow, or repository-setting change.**
- **No release, deployment, or publication.**

The canonical index, ADR operating summary, and ADR cross-register are synchronized only because the numbered inventory count changes from 34 to 35.

[Back to top](#top)

---

<a id="migration-and-convergence-plan"></a>

## Migration and convergence plan

Migration begins only after this ADR is accepted.

### Phase 0 — inventory and freeze

- Pin current main and complete the exact scaffold/domain-index inventory.
- Search open work and inbound references.
- Classify each candidate as `NUMBER`, `MERGE`, `RETAIN_AS_LINEAGE`, `RETIRE`, or `HOLD`.
- Freeze creation of new domain-local numbering schemes.

### Phase 1 — high-value candidates

Prepare separate, dependency-closed numbering packets for developed candidates whose decisions are not duplicated. Each packet updates the source candidate, canonical index, necessary pointer indexes, references, and generated provenance.

### Phase 2 — overlapping candidates

Merge domain schema-home and source-role candidates into the appropriate cross-cutting decision where one shared vocabulary or authority is required. Preserve candidate IDs in source-lineage notes.

### Phase 3 — pointer-index convergence

Update domain indexes to link only to central numbered ADRs and clearly separate unresolved local questions from accepted decisions.

### Phase 4 — legacy cleanup

Retire empty or superseded scaffolds only after inbound-link analysis and a documented rollback target. Historical decision discussions remain discoverable.

### Phase 5 — optional machine projection

Create or update a machine projection only from accepted decisions. Validate exact source path, status, scope, and supersession identity.

### Rollback target for each migration

Before any rename or retirement, record:

- prior path and blob SHA;
- successor path and permanent ID;
- inbound reference inventory;
- compatibility window where required;
- command or commit that restores the prior state;
- reason the migration can be reversed without losing decision history.

[Back to top](#top)

---

<a id="acceptance-gates"></a>

## Acceptance gates

This ADR remains proposed until every required gate closes.

| Gate | Acceptance evidence |
| --- | --- |
| A — identity coherence | Filename, H1, metadata, and canonical index agree on `ADR-0035` |
| B — placement authority | Accepted Directory Rules confirm `docs/adr/` as the decision lane and `docs/domains/` as guidance |
| C — overlap review | Existing numbered ADRs, scaffolds, domain indexes, branches, and PRs have been reviewed for contradiction |
| D — domain review | At least one affected domain steward reviews the pointer-only domain-index model |
| E — migration safety | Scaffold assignment, merge, retention, and retirement classes have a reversible protocol |
| F — validation | ADR index validator and focused tests pass at exact head |
| G — documentation closure | README, canonical index, and cross-register summaries agree |
| H — explicit decision review | Authorized reviewers record acceptance in the source ADR and canonical index together |

A green validator satisfies structural gates only. It cannot satisfy Gate H.

[Back to top](#top)

---

<a id="consequences"></a>

## Consequences

### Positive

- Permanent ADR identities are globally unique and stable.
- Domain-scoped decisions remain discoverable without fragmenting authority.
- Atlas and domain planning IDs retain useful lineage without masquerading as adopted decisions.
- Supersession, rejection, and correction history remain inspectable.
- Existing validator machinery can enforce most structural rules.
- Concurrent work has one visible collision-resolution protocol.
- Machine projections can remain subordinate to source decisions.

### Costs

- Domain teams cannot reserve familiar local sequences such as `ADR-FAUNA-01`.
- Assigning a developed scaffold requires coordinated filename, index, link, receipt, and review work.
- Some existing domain indexes and source documents will need later reconciliation.
- A global sequence is less semantically descriptive than domain prefixes, so metadata and discovery indexes must carry domain context.
- Acceptance still requires human governance; numbering does not reduce that burden.

### Tradeoff

KFM chooses one stable decision identity plane over locally convenient numbering. Domain context remains rich through metadata and pointer indexes, while precedence and decision history stay unambiguous.

[Back to top](#top)

---

<a id="alternatives-considered"></a>

## Alternatives considered

### Alternative A — independent domain sequences

Example: `ADR-FAUNA-01`, `ADR-HABITAT-01`.

**Rejected by the proposed decision.** It improves local readability but creates collision-free identities only within a domain, complicates cross-domain decisions, weakens one canonical inventory, and invites local override semantics.

### Alternative B — keep every scaffold identity permanently

Example: treat `ADR-S-05` or `ADR-XXXX-*` as final.

**Rejected.** Candidate identities come from different source corpora and allocation rules. They do not provide one repository-wide collision or status model.

### Alternative C — store domain ADR bodies under domain folders and mirror them centrally

**Rejected.** Two writable bodies create parallel authority and status drift. A domain pointer index provides discovery without copying the binding record.

### Alternative D — no domain indexes

**Not selected as a mandatory rule.** Central search and the canonical index may be sufficient for some domains, but pointer-only indexes are useful where a domain dossier needs an explicit decision map.

### Alternative E — encode domain in the permanent global ID

Example: `ADR-FAUNA-0001`.

**Rejected for current KFM.** It complicates ordering, cross-domain scope, validator logic, and migration from the established four-digit repository sequence without adding authority value.

### Alternative F — use GitHub issue numbers as ADR identities

**Rejected.** Issue identity is platform-specific and does not encode decision lifecycle, stable path, source status, or retained repository history.

[Back to top](#top)

---

<a id="risk-ledger"></a>

## Risk ledger

| Risk | Current posture | Mitigation |
| --- | --- | --- |
| This ADR appears to accept itself | `HOLD` | Keep source/index status proposed; require explicit later acceptance review |
| A concurrent branch also claims ADR-0035 | `NEEDS VERIFICATION` until merge | Recheck current main, branches, and PRs immediately before integration; renumber if needed |
| Domain indexes copy stale status | `PROPOSED` migration risk | Require derived labels and source links; treat disagreement as drift |
| Developed scaffolds lose source lineage during numbering | `PROPOSED` migration risk | Preserve prior path, candidate ID, source documents, and blob identity |
| Empty scaffolds are numbered merely to clean the tree | `DENY` | Apply substantive admission test before assignment |
| Central sequence hides domain ownership | Accepted tradeoff if decision passes | Require domain tags, related paths, and reviewers |
| Machine projection becomes decision authority | `DENY` | Source ADR and canonical human index remain controlling |
| A mass-renaming PR becomes unreviewable | `DENY` | Use small dependency-closed migration packets |
| Rejected or superseded records are deleted | `DENY` | Retain permanent identities and reciprocal lineage |
| Acceptance is inferred from merge | `DENY` | Source status plus explicit reviewed evidence control acceptance |

[Back to top](#top)

---

<a id="rollback-and-supersession"></a>

## Rollback and supersession

### Rollback of this proposed packet

Before acceptance, rollback is a normal branch or pull-request reversion:

1. remove the ADR-0035 file;
2. remove its row from `docs/adr/INDEX.md`;
3. restore inventory counts and summaries in the ADR README and cross-register;
4. remove the generated provenance receipt tied to the candidate bytes;
5. rerun ADR index and documentation validation.

No runtime, policy, source, data, release, or public state is affected.

### If accepted and later replaced

A successor ADR must:

- receive a new permanent number;
- name ADR-0035 in `supersedes`;
- mark ADR-0035 `superseded`;
- add reciprocal `superseded_by`;
- preserve this file and its decision history;
- include migration and rollback instructions for any changed numbering or storage model.

Reopening or editing the rationale of an accepted ADR is not a substitute for a successor decision.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

Required repository-native checks:

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers
```

Recommended changed-area documentation checks:

```bash
git diff --check
python tools/validate_all.py
```

The focused ADR validator must establish:

- unique IDs and exact `ADR-0001` through `ADR-0035` coverage;
- filename, H1, source status, effective status, and index agreement;
- unchanged complete inventory of the twelve unassigned scaffolds;
- no competing row table in the cross-register;
- valid supersession reciprocity;
- exact resolution of introduced local links.

Hosted exact-head checks remain required because this connector-first environment does not provide a mounted checkout for repository-native execution.

[Back to top](#top)

---

<a id="open-questions"></a>

## Open questions

1. Which named people or teams will hold architecture, docs, and domain-steward authority beyond the current repository-wide CODEOWNERS route?
2. Which of the twelve current scaffolds should be numbered, merged into an existing ADR, retained as planning lineage, or retired?
3. Which domain-local ADR indexes exist beyond the confirmed Fauna surface, and which consumers depend on their current anchors?
4. Should the optional machine projection contain every numbered record or only accepted decisions?
5. What compatibility window is required when a widely linked scaffold is renamed?
6. Should the validator enforce domain-index pointer-only behavior after this ADR is accepted?
7. Should source-corpus IDs such as `ADR-S-*` receive a formal crosswalk register, or are source-lineage notes sufficient?
8. What review quorum is required to accept a repository-wide governance ADR while independent stewardship remains limited?

[Back to top](#top)

---

<a id="references"></a>

## References

### Governing repository sources

- [`docs/adr/README.md`](./README.md) — current ADR operating contract.
- [`docs/adr/INDEX.md`](./INDEX.md) — canonical human inventory.
- [`docs/adr/ADR-template.md`](./ADR-template.md) — current authoring structure.
- [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md) — accepted Directory Rules v2 adoption.
- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) — accepted placement law.
- [`docs/registers/ADR_INDEX.md`](../registers/ADR_INDEX.md) — non-duplicating cross-register.
- [`docs/domains/fauna/adr/README.md`](../domains/fauna/adr/README.md) — current domain-index ambiguity evidence.
- [`tools/validators/validate_adr_index.py`](../../tools/validators/validate_adr_index.py) — structural enforcement.
- [`tests/validators/test_validate_adr_index.py`](../../tests/validators/test_validate_adr_index.py) — validator behavior tests.
- [`.github/workflows/docs-control-plane.yml`](../../.github/workflows/docs-control-plane.yml) — hosted documentation control-plane gate.

### Authority interpretation

Repository bytes establish current inventory and current enforcement surfaces. Accepted ADR-0029 and its pinned Directory Rules bytes govern placement. This proposed ADR would govern identity and domain indexing only after explicit acceptance.

[Back to top](#top)

---

<a id="revision-history"></a>

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| v1.0 | 2026-08-14 | Initial proposed ADR defining one repository-wide permanent ADR sequence, central decision storage, pointer-only domain indexes, candidate-ID handling, migration discipline, validation, and rollback. |
