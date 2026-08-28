<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-dossiers-readme
title: docs/dossiers/ — Provisional Documentation Lane
type: README
version: v0.1
status: hold; repository-grounded; non-authoritative; no-new-content
owners:
  - "@bartytime4life"
created: 2026-08-14
updated: 2026-08-14
policy_label: repository-facing
owning_root: docs/
responsibility: "Document the current docs/dossiers path, prevent it from becoming a parallel documentation authority, and route dossier-class material to an accepted documentation lane until placement is explicitly decided."
truth_posture: "CONFIRMED current path, inventory, history, adopted Directory Rules v2, ADR-0029, docs-root boundary, and CODEOWNERS route / HOLD lane authority and content admission / NEEDS VERIFICATION final dossier classification, canonical target, consumers, migration, and independent stewardship"
evidence_snapshot: "main@dc30e1d38f9a4ecf45fd589d388886fc872dd189; target blob e25f1814e51579d5f55c0f1fe0135ddb28a47f4a; Directory Rules blob fd49a0b83e55cef52c1124281f093e263526898d; docs root README blob 1f8bac189dac1d01c1185e8b4fb8e25efd11d09f; CODEOWNERS blob dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61"
related:
  - docs/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/architecture/README.md
  - docs/atlases/README.md
  - docs/domains/README.md
  - docs/intake/README.md
  - docs/archive/README.md
  - docs/registers/README.md
notes:
  - "The path was introduced on main by commit 1f0cf722669f9b4261ff84d6179fcd46ae76326e with only .gitkeep and a one-byte README containing y."
  - "Accepted Directory Rules v2 lists the canonical docs children and does not admit docs/dossiers/ as a canonical lane."
  - "This README freezes the lane and records routing guidance; it does not accept an ADR, amend Directory Rules, activate a compatibility lane, or authorize dossier content."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/dossiers/` — Provisional Documentation Lane

> [!IMPORTANT]
> **Placement outcome: `HOLD`.** This path exists in the repository, but the
> adopted Directory Rules v2 do not identify `docs/dossiers/` as a canonical
> documentation lane, and no accepted dossier-placement decision was verified
> in the inspected repository evidence. This README is a boundary guard. It
> does **not** authorize new dossier content.

A *dossier* is a document form, not an authority class. Its final home depends
on what responsibility the document actually carries: architecture, domain
guidance, source guidance, exploratory intake, atlas curation, historical
lineage, standards, security, operations, or a decision record. The word
“dossier” in a title never overrides that responsibility.

## Quick navigation

- [Current evidence and status](#current-evidence-and-status)
- [Purpose of this README](#purpose-of-this-readme)
- [Authority and non-effects](#authority-and-non-effects)
- [Current contents and write freeze](#current-contents-and-write-freeze)
- [Dossier-class routing](#dossier-class-routing)
- [Admission and promotion rules](#admission-and-promotion-rules)
- [Inputs, outputs, and consumers](#inputs-outputs-and-consumers)
- [Exposure, rights, and sensitivity](#exposure-rights-and-sensitivity)
- [Validation](#validation)
- [Ownership and review](#ownership-and-review)
- [Correction, migration, and rollback](#correction-migration-and-rollback)
- [Open verification backlog](#open-verification-backlog)
- [Status summary](#status-summary)

<a id="current-evidence-and-status"></a>

## Current evidence and status

The following statements are bounded to the inspected repository state.

| Question | Evidence-backed result |
|---|---|
| Does the path exist? | **CONFIRMED.** `docs/dossiers/` exists on `main`. |
| What was present at the evidence snapshot? | **CONFIRMED.** The direct inventory contained `.gitkeep` and `README.md`; the README blob contained only the single character `y`. |
| When was the README introduced? | **CONFIRMED.** Commit `1f0cf722669f9b4261ff84d6179fcd46ae76326e` created it on 2026-08-14. |
| Is `docs/dossiers/` listed in the adopted canonical `docs/` tree? | **No.** Directory Rules v2 lists `adr/`, `architecture/`, `archive/`, `atlases/`, `doctrine/`, `domains/`, `registers/`, `runbooks/`, `security/`, `sources/`, and `standards/`. |
| Does path presence make the lane canonical? | **No.** Current repository presence is implementation evidence, not automatic placement authority. |
| Is an accepted dossier-placement ADR verified? | **NEEDS VERIFICATION.** Older lineage documents mention an `ADR-S-02` concept, but no accepted, indexed dossier-placement ADR was verified in the inspected evidence. |
| May new dossier content be added here now? | **HOLD.** Add no content until one unique, governed home is selected. |
| Does this README change the lane’s authority? | **No.** It records and constrains the unresolved state. |

Accepted ADR-0029 adopts the exact Directory Rules v2 bytes at
[`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md). Those
rules make path selection an authority decision, prohibit parallel writable
homes, and require a finite placement outcome. Because the current evidence
does not establish a unique canonical responsibility for this lane, the safe
outcome is `HOLD`.

<a id="purpose-of-this-readme"></a>

## Purpose of this README

This README has four bounded purposes:

1. **Replace the one-byte placeholder with an inspectable lane contract.**
2. **Prevent accidental authority creation.** A folder with a polished README
   must not silently become a canonical dossier repository.
3. **Route dossier-class material by responsibility.** Authors should place a
   document in an already admitted documentation lane when one clearly owns it.
4. **Preserve reversibility.** A later accepted decision may admit, migrate,
   mirror, or retire this path without first disentangling ungoverned content.

This file is not a dossier index, a document registry, a doctrine artifact
catalog, or a release surface. It does not claim that any dossier exists,
passes preflight, is adopted, is public-safe, or has been published.

<a id="authority-and-non-effects"></a>

## Authority and non-effects

| Property | Current posture |
|---|---|
| Owning responsibility root | `docs/` — human-readable governance and explanation |
| Direct-child lane status | `HOLD`; present but not admitted as canonical |
| Artifact kind | Lane README and boundary guard |
| Exposure | Repository-facing |
| Mutability | Reviewed, versioned replacement |
| Retention | Durable until the path is admitted, migrated, or retired through governed change |
| Normal writer | Reviewed feature-branch change routed through current CODEOWNERS |
| Machine authority | None |
| Release or publication authority | None |

This README does **not**:

- amend the canonical `docs/` child map;
- accept or create an ADR;
- classify `docs/dossiers/` as canonical, compatibility, deprecated, archive,
  or generated;
- create a new object family or document lifecycle;
- authorize another file, subdirectory, PDF, export, or generated artifact here;
- migrate material from `docs/atlases/`, `docs/architecture/`,
  `docs/domains/`, `docs/intake/`, or `docs/archive/`;
- update `control_plane/` or a documentation registry;
- establish source authority, evidence closure, policy approval, review,
  release, promotion, publication, correction, or rollback state.

> [!CAUTION]
> A document can call itself a “dossier” while its real responsibility belongs
> elsewhere. Routing by filename or literary form would create parallel
> authority and weaken correction and supersession tracking.

<a id="current-contents-and-write-freeze"></a>

## Current contents and write freeze

The permitted direct inventory while the lane is on `HOLD` is:

```text
docs/dossiers/
├── .gitkeep
└── README.md
```

### Permitted changes

- Correct or clarify this README without changing the lane’s authority.
- Remove `.gitkeep` in the same governed change that adds a verified real
  child, but only after placement authority exists.
- Add a migration or retirement pointer only when an accepted decision and a
  verified consumer require it.

### Prohibited changes while on `HOLD`

Do not add:

- dossiers, reports, atlases, idea indexes, expansion packets, manuals, or PDFs;
- another README that claims a sub-lane;
- copied or converted content from attached source documents;
- source snapshots, datasets, EvidenceBundles, receipts, proofs, manifests,
  policy decisions, or release records;
- machine schemas, contracts, policy code, tests, fixtures, validators, app
  code, pipeline code, or generated build output;
- secrets, private endpoints, restricted source material, protected exact
  locations, or harmful precision;
- symlinks, mirrors, redirects, or aliases without verified consumers and an
  explicit migration record.

A pull request that adds dossier content here before placement is resolved
should return `HOLD_UNRESOLVED` or fail the applicable topology guard rather
than treating folder existence as permission.

<a id="dossier-class-routing"></a>

## Dossier-class routing

Use the document’s **primary responsibility**, not the word “dossier,” to pick
its home.

| Primary responsibility of the proposed document | Existing lane to evaluate first | Boundary |
|---|---|---|
| Explain current or proposed system structure | [`docs/architecture/`](../architecture/) | Architecture remains subordinate to accepted decisions and current implementation evidence. |
| Explain one domain’s concepts, source roles, risks, and implementation boundary | [`docs/domains/<domain>/`](../domains/) | Domain guidance must not become contract, schema, policy, evidence, or release authority. |
| Curate a versioned atlas, master index, category atlas, or atlas-derived reference | [`docs/atlases/`](../atlases/) | Check existing carrier and naming conflicts before adding another artifact. |
| Preserve a new proposal, exploratory packet, prior-pass fragment, or unclassified research note | [`docs/intake/`](../intake/) — current repository surface; placement authority must be rechecked | Intake is exploratory and cannot be cited as canon; if its own authority remains unresolved, return `HOLD`. |
| Preserve frozen, superseded, deprecated, or lineage documentation | [`docs/archive/`](../archive/) | Archive material must identify prior identity, status, and forward lineage. |
| Describe source identity, attribution, rights, limits, or human source use | `docs/sources/` | Human source guidance does not replace machine source registry instances. |
| Define stable KFM operating or trust law | `docs/doctrine/` | Requires the doctrine authority and review burden appropriate to the change. |
| Record an architecture decision | `docs/adr/` | Status comes from the ADR process, not from document wording. |
| Record human-readable drift, verification, or status tracking | [`docs/registers/`](../registers/) | Registers describe state; machine projections remain under `control_plane/`. |
| Document an operational procedure | `docs/runbooks/` | A runbook does not establish architecture or policy authority. |
| Document a threat, incident, exposure, or security review | `docs/security/` | Sensitive details remain redacted or staged. |
| Document a KFM or external standard/profile | `docs/standards/` | Separate normative KFM requirements from external reference material. |

If more than one row appears to own the document, split it into linked
artifacts or return `HOLD`. Do not create a cross-cutting dossier here to avoid
making the ownership decision.

### Routing examples

| Proposed title | Likely classification | Safe next action |
|---|---|---|
| “Soil Source Roles and Validation Dossier” | Domain guidance plus possible source guidance | Put domain meaning in `docs/domains/soil/`; link to source guidance rather than copying it. |
| “MapLibre Operating Architecture Dossier” | System architecture | Update the existing architecture surface rather than creating a parallel dossier. |
| “Pass 34 Idea Index and Expansion Dossier” | Exploratory intake or curated atlas, depending on adoption state | Start in `docs/intake/`; move to `docs/atlases/` only after identity, scope, lineage, and carrier conflicts are resolved. |
| “Superseded Geology Planning Dossier” | Frozen lineage | Route to `docs/archive/` with a forward pointer to current guidance. |
| “Source Rights Verification Dossier” | Source guidance or a register | Split stable guidance into `docs/sources/` and unresolved work into `docs/registers/`. |

These examples are routing guidance, not proof that the named documents exist.

<a id="admission-and-promotion-rules"></a>

## Admission and promotion rules

A document must not enter a canonical documentation lane merely because its
content is detailed or persuasive. Before adding a dossier-class artifact:

1. **Classify the artifact.** State its one authority owner and primary human
   responsibility.
2. **Search for an existing home and equivalent artifact.** Reuse or update the
   current surface instead of creating a parallel “new,” “final,” or “v2”
   document.
3. **Freeze governing evidence.** Record the adopted Directory Rules, relevant
   ADRs, current repository ref, target prior identity, and direct consumers.
4. **Resolve source status.** Separate current repository evidence, adopted
   doctrine, lineage sources, external references, and proposals.
5. **Choose one finite placement outcome.** `PLACE`, `SPLIT`, `MIGRATE`,
   `MIRROR`, `HOLD`, or `DENY`.
6. **Apply the documentation metadata contract.** Use stable `doc_id`, valid
   dates, explicit owner, policy label, responsibility, related surfaces, and
   truth posture.
7. **Define supersession and correction.** Identify what the document replaces,
   what replaces it later, and how errors will be corrected.
8. **Validate the authored result and its neighborhood.** Check metadata, links,
   anchors, document graph, stale references, generated relationships, and
   sensitivity.
9. **Obtain the required review.** Authority-changing placement requires the
   decision class named by Directory Rules; an ordinary content PR cannot
   silently admit a new lane.
10. **Keep publication separate.** Merge, rendered output, a PDF, or a passing
    docs workflow does not create KFM publication.

### Activating this lane

A future proposal to make `docs/dossiers/` writable must define at least:

- the dossier artifact class and how it differs from architecture, domain,
  atlas, intake, archive, register, source, and report material;
- whether the lane is canonical, compatibility, or another adopted class;
- its owning responsibility and permitted writers;
- naming, versioning, metadata, supersession, correction, retention, and
  sensitivity rules;
- existing producers and consumers;
- relationship to `docs/atlases/` and any older dossier references;
- migration, alias, exit, and rollback conditions;
- validator and documentation-graph coverage;
- the accepted decision that amends or interprets the adopted `docs/` lane set.

Until those conditions are met, this path remains `HOLD`.

<a id="inputs-outputs-and-consumers"></a>

## Inputs, outputs, and consumers

### Inputs

This README may be updated from:

- accepted Directory Rules and ADRs;
- current repository tree, history, CODEOWNERS, validators, workflows, and
  document-registry evidence;
- verified inbound references or producers;
- accepted migration, alias, deprecation, or retirement records;
- review findings that materially change the lane’s disposition.

Historical dossiers, planning PDFs, atlases, and prompts are design lineage.
They can inform the classification question, but they cannot activate this path
or prove current implementation.

### Outputs

While on `HOLD`, this lane produces only:

- this human-readable boundary contract;
- a visible no-new-content rule; and
- a routing checklist for proposed dossier-class documents.

It emits no document registry entry, policy decision, evidence object,
promotion receipt, release manifest, proof, published artifact, or runtime
payload.

### Consumers

The expected consumers are maintainers, docs reviewers, architecture reviewers,
domain stewards, source stewards, and automation evaluating a proposed path.
No runtime, API, MapLibre, AI, release, or publication consumer is established
by this README.

<a id="exposure-rights-and-sensitivity"></a>

## Exposure, rights, and sensitivity

Repository documentation may be publicly readable. A dossier’s breadth can
make it especially likely to aggregate information that is harmless in
isolation but sensitive when combined.

Before any dossier-class material is committed to an admitted lane, review:

- source rights, attribution, quotation, and redistribution limits;
- living-person and genealogy content;
- DNA or genomic material;
- rare-species locations;
- archaeology, sacred, sovereign, or culturally restricted information;
- infrastructure, private wells, land/title, or security-relevant details;
- exact coordinates, images, screenshots, examples, and linked attachments;
- whether the document reveals a denial reason that itself creates exposure.

When support is unclear, redact, generalize, stage, delay, quarantine, abstain,
or deny. A public README may describe a control without exposing the protected
payload.

<a id="validation"></a>

## Validation

A change to this README should use the smallest repository-native validation
set that covers the actual delta.

### Required changed-area checks

- `KFM_META_BLOCK_V2` structure, identity, dates, ownership, root agreement,
  responsibility, related-path hygiene, and review-only registry comparison;
- exactly one H1 and orderly headings;
- repo-relative link, path, case, and fragment resolution;
- internal anchor uniqueness and table/fence integrity;
- documentation graph and stale-reference checks;
- secret, privacy, rights, and sensitivity review;
- changed-area docs build and control-plane checks;
- repository-topology validation, classified against the exact base so an
  inherited finding is not misreported as introduced.

### Negative acceptance checks

The change must not:

- classify this lane as active or canonical;
- introduce dossier content or a child lane;
- create a second writable atlas, architecture, domain, intake, or archive
  authority;
- claim an accepted ADR that was not verified;
- claim review, release, publication, runtime behavior, or whole-repository
  conformance without evidence;
- mutate `control_plane/document_registry.yaml` from generated review output;
- hide an inherited workflow failure or attribute it to this README without
  exact-base evidence.

Documentation QA is evidence about document quality. It is not proof of
architecture, policy, security, release, deployment, promotion, or
publication.

<a id="ownership-and-review"></a>

## Ownership and review

`.github/CODEOWNERS` has no path-specific rule for `docs/dossiers/`; the
repository-wide fallback routes review to `@bartytime4life`. CODEOWNERS is a
routing mechanism, not proof that review occurred or that independent
stewardship exists.

| Change type | Minimum review posture |
|---|---|
| Clarify this boundary without changing authority | Current repository owner route |
| Add, move, or classify a dossier artifact | Docs owner plus the owning architecture, domain, source, security, or standards reviewer |
| Activate this lane or create a compatibility role | Accepted authority decision, migration analysis, owner review, and independent trust review appropriate to significance |
| Add sensitive or rights-constrained content | Qualified rights, sensitivity, sovereignty, privacy, cultural, security, or domain review |

Independent documentation stewardship remains **NEEDS VERIFICATION**.

<a id="correction-migration-and-rollback"></a>

## Correction, migration, and rollback

### Correcting this README

Use normal reviewed replacement. Preserve `doc_id` and update `updated` when
the lane’s evidence or disposition changes. If the path is admitted, migrated,
or retired, update status, related surfaces, evidence snapshot, validation, and
rollback instructions in the same coherent change.

### Migrating or retiring the path

Do not delete or repurpose `docs/dossiers/` merely because it is absent from the
canonical lane map. A future structural change must first verify:

- exact tracked inventory and history;
- producers, consumers, links, fragments, generators, and external references;
- whether any artifact was placed here after this freeze;
- canonical targets for every item;
- stable identity and supersession behavior;
- alias or tombstone needs;
- migration validation and rollback target;
- zero-writer and zero-consumer evidence before physical removal.

### Rollback

Before merge, close the pull request and delete its feature branch. After an
authorized merge, revert the README commit to restore the prior bytes. No data,
schema, contract, policy, release, runtime, deployment, cache, or published
artifact requires rollback because this document changes no operational state.

<a id="open-verification-backlog"></a>

## Open verification backlog

| ID | Question | Required evidence | Current state |
|---|---|---|---|
| `DOS-001` | Should `docs/dossiers/` exist as a distinct writable lane? | Accepted placement decision grounded in Directory Rules v2 | `HOLD` |
| `DOS-002` | What document class would this lane own that no current lane owns? | Artifact taxonomy and non-overlap analysis | `UNKNOWN` |
| `DOS-003` | Are there verified producers or consumers of this exact path? | Current repository search plus external-consumer review where applicable | `NEEDS VERIFICATION` |
| `DOS-004` | Does an accepted or historical dossier-placement ADR exist under another identifier? | Canonical ADR index and decision-history review | `NEEDS VERIFICATION` |
| `DOS-005` | How should “idea index and expansion dossier” artifacts relate to `docs/intake/` and `docs/atlases/`? | Explicit lifecycle, carrier, naming, and supersession decision | `HOLD` |
| `DOS-006` | Should the current empty lane be retired if no unique responsibility is found? | Zero-producer/consumer proof, migration plan, and rollback evidence | `NEEDS VERIFICATION` |
| `DOS-007` | Is a dedicated CODEOWNERS route or independent docs steward required? | Verified GitHub identity and stewardship assignment | `NEEDS VERIFICATION` |
| `DOS-008` | Does the topology ratchet already baseline this newly introduced path? | Exact-base validator output and current baseline inspection | `NEEDS VERIFICATION` |

Open questions belong in governed review work; they are not permission to add
content here.

<a id="status-summary"></a>

## Status summary

**CONFIRMED**

- `docs/dossiers/` exists and currently contains only `.gitkeep` and this
  README.
- The prior README was a one-byte placeholder.
- ADR-0029 adopts Directory Rules v2.
- The adopted canonical `docs/` map does not list `docs/dossiers/`.
- Current review routing falls back to `@bartytime4life`.

**HOLD**

- Canonical or compatibility status for this lane.
- Admission of any dossier, PDF, index, report, manual, or child directory.
- Migration between `docs/dossiers/` and another documentation lane.

**NEEDS VERIFICATION**

- A unique dossier artifact class, accepted placement decision, current
  producers and consumers, topology-baseline treatment, independent
  stewardship, and final migration or retirement disposition.

[Back to top](#top)
