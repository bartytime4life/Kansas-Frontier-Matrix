<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0036
title: Planning Encyclopedia Carrier, Single-Writer, and Scaffold Disposition
type: adr
version: v1.1
status: proposed
effective_decision_status: proposed
owners:
  - "@bartytime4life via the current CODEOWNERS review route"
created: 2026-08-14
updated: 2026-09-14
policy_label: public
owning_root: docs/
responsibility: >-
  Propose one planning-encyclopedia lane, one writable manuscript source, one
  generated assembly relationship, and a reversible disposition for overlapping
  encyclopedia scaffolds and compatibility surfaces.
truth_posture: >-
  CONFIRMED targeted current repository and supplied-source readback / PROPOSED
  carrier, writer, generation, and migration decision / UNKNOWN source-PDF
  repository carrier, external consumers, independent stewardship, and
  publication effects / NEEDS VERIFICATION acceptance, inbound-reference closure,
  deterministic assembly tooling, chapter review, compatibility retirement, and
  current execution of the listed validation commands.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 2c1d921717ba972861b249c2030179a310221d9e
  target_prior_blob: 01cb4829c182ac580da17234963165adbb0b8b80
  adr_index_blob: 0c143676dfd3c1bda16cb44398c5ad5d4a49cf67
  adr_0029_blob: 4c1ef5f7f812d58fbdde9898acc96bb4c9280b2c
  adr_0035_blob: d9284faec018135f7e18f6e6cb17abb8bc65ad33
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  docs_root_readme_blob: 48926c51d952836cc7d4f0ba22a47e0d1a34e4f4
  encyclopedia_readme_blob: 4988edaf94d067980ac0c1ea0fabf2ba7a1b1530
  encyclopedia_index_blob: 51ace44010435b776d33bbdefe6998cd5fd4d816
  encyclopedia_changelog_blob: 543140c5113dad8825ba64cf8517903d0416fb51
  encyclopedia_assembly_blob: 23ca512eb2b1ec58c020d1991df5bbf670a697ac
  encyclopedia_chapter_tree: 28b053a9ff7c77d243e4225f9571e168b9dccc9a
  compatibility_index_blob: 7a2a66a42033f80c291a7176e3ca586ea0576b18
  doctrine_encyclopedia_blob: 4392fb99d8ad6221beb4ea165092a20673814ac2
  supplied_source_pdf_sha256: cc899a7a57cbadb5870709be07d9b0dbfd01712cd794d63dc4d640485970419a
inspection_boundary: >-
  v1.1 is grounded in targeted GitHub reads at main@2c1d921717ba972861b249c2030179a310221d9e: this ADR;
  ADR index; accepted ADR-0029; proposed ADR-0035; Directory Rules bytes;
  docs root README; the direct encyclopedia tree; control documents;
  chapter-tree listing; compatibility index; and doctrine encyclopedia. The
  supplied 82-page source PDF was re-hashed and its title and ordered
  sixteen-section contents were checked. No complete inbound-reference scan,
  source-PDF rights review, CODEOWNERS review, assembler, generation,
  validator, workflow, build, release, deployment, promotion, or publication
  action was performed.
related:
  - docs/encyclopedia/README.md
  - docs/encyclopedia/INDEX.md
  - docs/encyclopedia/CHANGELOG.md
  - docs/encyclopedia/encyclopedia.md
  - docs/encyclopedia/chapters/
  - docs/KFM-encyclopedia.md
  - docs/doctrine/encyclopedia.md
  - docs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/adr/ADR-0035-repository-wide-adr-identity-numbering-and-domain-indexing.md
  - docs/doctrine/directory-rules.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
tags: [adr, documentation, encyclopedia, planning, carrier, single-writer, generated-mirror, migration]
supersedes: []
superseded_by: []
notes:
  - "This record is proposed. Filing, merging, indexing, or validating it does not accept the decision or authorize dependent migration."
  - "The source manuscript is the 82-page Kansas Frontier Matrix Domain and Capability Encyclopedia v0.1, SHA-256 cc899a7a57cbadb5870709be07d9b0dbfd01712cd794d63dc4d640485970419a, as recorded by docs/KFM-encyclopedia.md."
  - "The current docs/encyclopedia tree is a scaffold: seven direct children, seventeen chapter files, sixteen generic placeholders, and one bounded settlements/infrastructure scaffold."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0036: Planning Encyclopedia Carrier, Single-Writer, and Scaffold Disposition

> **Decision proposal.** Admit `docs/encyclopedia/` as KFM's non-authoritative planning-encyclopedia lane, use the ordered chapter set as its only writable manuscript source, generate `encyclopedia.md` from that source, retain `docs/KFM-encyclopedia.md` as a temporary compatibility index, and keep `docs/doctrine/encyclopedia.md` as a separate doctrine-vocabulary surface.

[![status](https://img.shields.io/badge/status-proposed-d4a72c?style=flat-square)](#status)
[![single writer](https://img.shields.io/badge/single%20writer-chapters%2F-0969da?style=flat-square)](#decision)
[![migration](https://img.shields.io/badge/migration-after%20acceptance-b42318?style=flat-square)](#implementation-sequence)
[![publication](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#non-effects)

> [!IMPORTANT]
> **This ADR is not accepted.** Under the adopted Directory Rules two-change discipline, this proposal cannot authorize chapter population, source-PDF placement, generation tooling, moves, deletion, compatibility retirement, release, or publication.

**Quick navigation:** [Status](#status) · [Context](#context) · [Decision](#decision) · [Boundaries](#authority-boundaries) · [Compatibility](#compatibility-and-scaffolds) · [Implementation](#implementation-sequence) · [Consequences](#consequences) · [Alternatives](#alternatives) · [Acceptance](#acceptance-and-validation) · [Non-effects](#non-effects) · [Rollback](#correction-supersession-and-rollback) · [Open questions](#open-questions)

---

## Status

| Field | Value |
|---|---|
| **ID** | `ADR-0036` |
| **Status** | `proposed` |
| **Decision class** | Documentation-lane admission, single-writer selection, generated mirror, and compatibility migration |
| **Evidence checkpoint** | main@2c1d921717ba972861b249c2030179a310221d9e (v1.1 targeted source readback; no assembler, validation, or workflow execution) |
| **Primary responsibility root** | `docs/` |
| **Affected surfaces** | `docs/encyclopedia/`, `docs/KFM-encyclopedia.md`, `docs/doctrine/encyclopedia.md` |
| **Source manuscript** | *Kansas Frontier Matrix Domain and Capability Encyclopedia* v0.1, 82 pages, 2026-05-05 |
| **Source digest** | `sha256:cc899a7a57cbadb5870709be07d9b0dbfd01712cd794d63dc4d640485970419a` |
| **Current maturity** | Directly inventoried planning scaffold, planning index, and doctrine vocabulary surface; no accepted chapter writer, deterministic assembly, migration, or publication was verified |
| **Acceptance effect** | None until this ADR and the canonical index transition together through explicit review |
| **Release/publication effect** | None |

Repository presence, ADR acceptance, migration implementation, chapter review, and publication are separate states.

[Back to top](#top)

---

## Context

Current repository evidence exposes three encyclopedia-shaped surfaces:

| Surface | Current role | Unresolved point |
|---|---|---|
| `docs/KFM-encyclopedia.md` | Repository-grounded planning index and source-manuscript crosswalk | Root-level compatibility-shaped path; not the full manuscript |
| `docs/doctrine/encyclopedia.md` | Doctrine vocabulary and concept index | Must remain distinct from planning narrative |
| docs/encyclopedia/ | Tracked planning scaffold with seven direct children and 17 listed chapter files | No accepted lane classification, canonical chapter writer, or deterministic assembly |

At the v1.1 evidence checkpoint, the immediate tree retains README.md, INDEX.md, CHANGELOG.md, encyclopedia.md, assets/, chapters/, and lineage/. The chapter listing has the ordered 01- through 16- spine and the additional 11-settlements-infrastructure.md scaffold. The direct readback confirms the existing control-document, assembly-target, compatibility-index, and doctrine-vocabulary postures; it does not verify a repository-wide consumer inventory, canonical writer, assembly tool, generated parity, or external consumer.

The source manuscript's ordered structure is:

1. Cover Page
2. Executive Summary
3. Source Ledger and Evidence Method
4. KFM Operating Law
5. Master Domain Atlas
6. Cross-Domain Capability Taxonomy
7. Domain Chapters
8. Cross-Domain Systems Chapters
9. Master Feature Matrix
10. Master Action Matrix
11. Master Viewing Mode Atlas
12. Programming Possibilities Backlog
13. Sensitive / Deny-by-Default Register
14. Implementation Roadmap
15. Validation and Acceptance Plan
16. Appendices and Self-Check

Without a decision, three paths can become competing writers, a generated output can be edited manually, domain stubs can duplicate `docs/domains/`, and compatibility paths can be removed before consumer closure.

[Back to top](#top)

---

## Currentness reconciliation

**CONFIRMED at the v1.1 checkpoint:** the supplied PDF hash remains sha256:cc899a7a57cbadb5870709be07d9b0dbfd01712cd794d63dc4d640485970419a; its title, v0.1/2026-05-05 document control, and sixteen-section order match the lineage recorded by the compatibility index. ADR-0029 remains the accepted placement authority for the human-readable docs/ responsibility root. ADR-0035 remains proposed. The ADR index continues to register ADR-0036 as proposed without accepting its carrier, writer, mirror, or migration decision.

**CONFIRMED only as targeted path presence and document posture:** the immediate planning-scaffold tree, the chapter listing, the reserved assembly target, the compatibility index, and the doctrine encyclopedia are present at the recorded base. Their presence does not establish a canonical writer, a generated output, accepted migration, rights-cleared PDF carrier, review, implementation maturity, or publication state.

**NOT EXECUTED / NEEDS VERIFICATION:** a full inbound-reference inventory; source-PDF rights, provenance, retention, and repository-carrier review; chapter substantive-content review; deterministic assembly and generated-parity proof; validation commands; CODEOWNERS and independent review; and all release, deployment, promotion, and publication controls.

[Back to top](#top)

---

## Decision

If accepted:

### 1. Lane

`docs/encyclopedia/` becomes a canonical **planning-reference documentation lane** under the existing `docs/` root. It remains subordinate to doctrine, accepted ADRs, contracts, schemas, policy, source authority, evidence, tests, review, release, correction, and rollback records.

### 2. Single writable manuscript source

The ordered files `docs/encyclopedia/chapters/01-*.md` through `16-*.md` are the only writable manuscript source.

Each chapter must preserve source lineage, truth labels, citations, and upstream authority links. Domain summaries remain synthesis and must not replace `docs/domains/<domain>/`.

### 3. Generated assembly

`docs/encyclopedia/encyclopedia.md` is a deterministic, read-only assembly generated from the ordered chapter source. It must declare its producer, input order and hashes, output digest, generation time, and source revision. CI must fail on manual edits or source/output drift.

### 4. Control documents

- `README.md` owns lane boundaries and contributor rules.
- `INDEX.md` owns chapter order, navigation, and current chapter status.
- `CHANGELOG.md` owns edition, migration, correction, and supersession history.

None of these creates doctrine, evidence, release, or publication authority.

### 5. Compatibility and doctrine surfaces

`docs/KFM-encyclopedia.md` remains a read-only compatibility index until link inventory and consumer migration are complete. `docs/doctrine/encyclopedia.md` remains a separate doctrine-vocabulary surface and is never generated from the planning manuscript.

### 6. Source PDF

The source PDF's repository carrier remains `UNKNOWN`. It may not be copied, renamed, or declared canonical until identity, rights, provenance, retention, and generation relationships are reviewed.

[Back to top](#top)

---

## Authority boundaries

Allowed planning content includes source ledgers, domain/capability summaries, matrices, view/action taxonomies, proposed roadmaps, validation plans, and clearly labeled examples.

The lane must not own:

- doctrine or accepted decisions;
- semantic contracts, schemas, policy, source registries, or rights decisions;
- EvidenceBundles, receipts, proofs, catalogs, release objects, or published data;
- generated implementation claims unsupported by current repository evidence;
- protected exact locations, living-person or genomic data, or rights-uncertain content.

Implementation-shaped claims must point to current evidence or remain `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Compatibility and scaffolds

The sixteen structural paths are retained as proposed chapter identities, but acceptance alone does not populate them.

`docs/encyclopedia/chapters/11-settlements-infrastructure.md` is outside the ordered source spine. A later migration must inventory references and unique content, compare it with `docs/domains/settlements-infrastructure/`, move uniquely useful material to the proper owner, preserve a migration note or pointer, and retire the duplicate ordinal only after closure.

`assets/` and `lineage/` remain conditional. They may hold encyclopedia-specific, rights-cleared figures or edition/source lineage; they must not become general asset, source, evidence, receipt, or proof homes.

[Back to top](#top)

---

## Implementation sequence

Implementation is a separate change after acceptance:

1. Transition this ADR and `docs/adr/INDEX.md` together and update the `docs/` root map.
2. Establish `README.md`, `INDEX.md`, and `CHANGELOG.md` as the accepted control documents.
3. Populate chapters incrementally from the source manuscript, reconciling against current repository authority and obtaining domain review.
4. Add a repository-owned, no-network assembler plus deterministic manifest, parity tests, and drift rejection.
5. Inventory and migrate consumers of `docs/KFM-encyclopedia.md`; resolve the extra `11-` scaffold.
6. Run metadata, link, fragment, document-graph, staleness, topology, generated-parity, and receipt checks before closing migration.

Physical deletion remains held until zero-consumer evidence exists.

[Back to top](#top)

---

## Consequences

Benefits:

- one writable planning source;
- bounded chapter review;
- deterministic whole-manuscript assembly;
- explicit separation from doctrine and domain authority;
- reversible compatibility migration;
- preserved source structure without implementation overclaim.

Costs and risks:

- substantial editorial and verification work;
- generator and parity-test maintenance;
- possible long compatibility window;
- multi-owner domain review;
- unresolved source-PDF rights and carrier;
- stale planning content without review cadence.

Failure modes include hand-editing the generated assembly, treating chapters as doctrine, duplicating domain authority, copying the PDF without review, deleting compatibility paths early, or calling a completed encyclopedia KFM publication.

[Back to top](#top)

---

## Alternatives

| Alternative | Disposition |
|---|---|
| Keep `docs/KFM-encyclopedia.md` as sole writer | Rejected: it is an index, has an awkward compatibility-shaped name, and is difficult to review by domain |
| Hand-write only `docs/encyclopedia/encyclopedia.md` | Rejected: large-file conflicts and unused chapter scaffold |
| Move the manuscript under `docs/atlases/` | Rejected: atlas and planning-encyclopedia responsibilities differ |
| Retire the scaffold and keep only the index | Rejected: no repository-native chapter source for the full manuscript |
| Allow both single-file and chaptered writers | Denied: parallel writable authority |

[Back to top](#top)

---

## Acceptance and validation

Acceptance should include the repository owner/review route, documentation and directory-governance review, architecture review, and a domain reviewer for the chapter-review model. CODEOWNERS routing is not proof of review.

Before acceptance, confirm:

- no later merge or PR selected another carrier;
- filename, H1, metadata, and index row agree;
- the ordered spine matches the source manuscript;
- planning and doctrine surfaces remain distinct;
- the decision creates no machine or publication authority under `docs/`;
- implementation remains a separate post-acceptance change;
- compatibility and rollback requirements are sufficient.

Repository-native validation should include (not run for this documentation-only v1.1 currentness readback):

```bash
python tools/validators/validate_adr_index.py
python -m pytest tests/validators/test_validate_adr_index.py -q --strict-config --strict-markers
```

A later implementation also needs metadata, Markdown, links/fragments, document graph, staleness, topology, duplicate-ordinal, generated-parity, sensitive-content, and authoring-receipt checks. Passing checks do not accept this ADR or publish the manuscript.

[Back to top](#top)

---

## Non-effects

This proposal does not:

- accept ADR-0036 or ADR-0035;
- populate a chapter or admit the lane before acceptance;
- change the `docs/` root map;
- assign the PDF a repository home;
- add a generator or generated manuscript;
- convert the compatibility index;
- move, rename, delete, or retire any scaffold;
- change doctrine, contracts, schemas, policy, sources, evidence, receipts, proofs, release, apps, or runtime;
- release, deploy, promote, publish, merge, or change repository settings.

[Back to top](#top)

---

## Correction, supersession, and rollback

Before acceptance, rollback is a normal revert of this proposal packet.

After acceptance, a meaning-changing reversal requires an accepted successor ADR with reciprocal links. Implementation commits remain independently reversible; generated output must be reproducible from the last accepted chapter set; compatibility pointers remain until consumer closure; and corrections must preserve edition, source, reason, and rollback lineage.

No rollback may restore two writable manuscript sources.

[Back to top](#top)

---

## Open questions

1. Which repository-owned assembler and manifest shape should be used?
2. Should the source PDF be generated, archived as immutable lineage, or remain external?
3. Which chapter changes require domain-specific approval?
4. What cadence or source-change trigger makes a chapter stale?
5. Which legacy anchors and external consumers require compatibility?
6. When should `assets/` and `lineage/` be activated or retired?

[Back to top](#top)

---

## Change history

| Version | Date | Change |
|---|---|---|
| `v1.0` | 2026-08-14 | Initial proposed carrier, single-writer, generated-mirror, and scaffold-disposition decision. |
| v1.1 | 2026-09-14 | Same-path currentness reconciliation at main@2c1d921717ba972861b249c2030179a310221d9e; rechecks the supplied source digest, planning-scaffold inventory, adjacent authority surfaces, and ADR index while preserving proposed and non-effect boundaries. |

[Back to top](#top)
