<!--
KFM_WIKI_SOURCE
page_id: Glossary
title: Glossary
status: PROPOSED wiki source; review required
updated: 2026-08-14
authority: orientation-only; adopted doctrine, accepted ADRs, contracts, schemas, policy, and current repository evidence control exact meaning
source_path: docs/wiki/Glossary.md
publication_effect: none until separately synchronized to the native GitHub Wiki
evidence_checkpoint: main@f26484bdf775c949be3031bd258ce113c1ad1cce
prior_blob: 857f8b0cc26b1b02e97ea17635ff258d5934429b
-->
<a id="top"></a>

# Glossary

<p align="center">
  <strong>Shared KFM vocabulary for readers, reviewers, contributors, and downstream wiki users</strong>
</p>

<p align="center">
  <a href="Home.md">Home</a> ·
  <a href="Architecture.md">Architecture</a> ·
  <a href="Governance-and-Evidence.md">Governance and evidence</a> ·
  <a href="Data-Lifecycle.md">Data lifecycle</a> ·
  <a href="Contributing.md">Contributing</a>
</p>

KFM uses precise vocabulary because similar-looking objects can carry very different authority. This page gives concise reader-facing definitions and the distinctions needed to navigate the project safely.

> [!IMPORTANT]
> This glossary is an **orientation projection**, not a second vocabulary authority. Exact meaning comes from adopted doctrine and ADRs, the owning semantic contract, paired machine schema, applicable policy, tests and validators, and current implementation evidence. A term appearing here does not prove that its object family is accepted, fully implemented, released, deployed, or published.

## At a glance

### Three vocabularies that must stay separate

| Vocabulary | What it describes | Examples |
|---|---|---|
| **Truth labels** | How strongly a statement is supported in the current evidence boundary | `CONFIRMED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION` |
| **Finite runtime outcomes** | What a governed public or client-facing response may do | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| **Workflow and lifecycle states** | Where an item is in review, admission, processing, release, or correction | `HOLD`, `Pre-RAW`, `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG / TRIPLET`, `PUBLISHED` |

Do not use a truth label as a runtime outcome, a runtime outcome as a lifecycle state, or a path name as proof that a transition occurred.

### Distinctions that protect the trust membrane

| Commonly collapsed terms | KFM distinction |
|---|---|
| Canonical · public · published | Canonical identifies the governing source for a responsibility. Public describes exposure. `PUBLISHED` is a governed lifecycle state. None implies the others. |
| Contract · schema · policy | A contract defines meaning. A schema defines machine-valid shape. Policy decides admissibility and obligations. |
| Validation · review · promotion · release | Validation checks declared conditions. Review records authorized judgment. Promotion changes governed state. Release binds an approved set and rollback context. |
| Receipt · proof · catalog · manifest | A receipt records process memory. Proof supports a declared condition. A catalog enables discovery. A manifest binds an identified set, versions, and digests. |
| Source · evidence · claim | A source has identity, role, rights, and limitations. Evidence is support resolved from sources. A claim is what KFM asserts within a bounded scope. |
| Map · tile · graph · AI response | These are downstream carriers or interpretations. They are never sovereign truth by themselves. |
| Stage · directory | A lifecycle stage is a governed state contract. A directory is one possible materialization and cannot promote an object by placement alone. |
| Merge · deployment · publication | A merge changes repository history. A deployment changes a running environment. Publication exposes a governed release. Each is a separate transition. |

### Core operating shorthand

```text
(Pre-RAW) -> RAW -> WORK / QUARANTINE -> PROCESSED
          -> CATALOG / TRIPLET -> PUBLISHED
```

Public and ordinary semi-public clients should reach released public-safe state through the Governed API or another accepted trust-membrane interface—not by reading RAW, WORK, QUARANTINE, candidate, canonical/internal, or direct model-runtime stores.

## A–Z index

[ABSTAIN](#abstain) · [Accepted ADR](#accepted-adr) · [ADR](#adr) · [AIReceipt](#aireceipt) · [ANSWER](#answer) · [Artifact](#artifact) · [Authority ladder](#authority-ladder) · [Canonical](#canonical) · [CATALOG](#catalog) · [Citation validation](#citation-validation) · [Cite-or-abstain](#cite-or-abstain) · [Compatibility surface](#compatibility-surface) · [CONFIRMED](#confirmed) · [Contract](#contract) · [CorrectionNotice](#correctionnotice) · [DENY](#deny) · [Derived artifact](#derived-artifact) · [Deterministic identity](#deterministic-identity) · [Directory Rules](#directory-rules) · [Domain lane](#domain-lane) · [ERROR](#error) · [EvidenceBundle](#evidencebundle) · [Evidence Drawer](#evidence-drawer) · [EvidenceRef](#evidenceref) · [Fixture](#fixture) · [Focus Mode](#focus-mode) · [GENERATED_RECEIPT](#generated_receipt) · [Governed API](#governed-api) · [Harmful precision](#harmful-precision) · [HOLD](#hold) · [Inspectable claim](#inspectable-claim) · [Integrity](#integrity) · [Lifecycle](#lifecycle) · [Manifest](#manifest) · [MapLibre](#maplibre) · [Merge](#merge) · [Native wiki projection](#native-wiki-projection) · [NEEDS VERIFICATION](#needs-verification) · [Negative state](#negative-state) · [Object family](#object-family) · [Policy](#policy) · [PolicyDecision](#policydecision) · [Pre-RAW](#pre-raw) · [PROCESSED](#processed) · [Promotion](#promotion) · [Proof](#proof) · [PROPOSED](#proposed) · [Public-safe](#public-safe) · [Publication](#publication) · [PUBLISHED](#published) · [QUARANTINE](#quarantine) · [RAW](#raw) · [Receipt](#receipt) · [Registry](#registry) · [Release](#release) · [ReleaseManifest](#releasemanifest) · [Replay](#replay) · [Responsibility root](#responsibility-root) · [Review](#review) · [Rollback](#rollback) · [RuntimeResponseEnvelope](#runtimeresponseenvelope) · [Schema](#schema) · [Sensitivity](#sensitivity) · [SourceActivationDecision](#sourceactivationdecision) · [SourceDescriptor](#sourcedescriptor) · [Source role](#source-role) · [spec_hash](#spec_hash) · [Steward](#steward) · [Supersession](#supersession) · [TRIPLET / TRIPLETS](#triplet--triplets) · [Trust membrane](#trust-membrane) · [Truth labels](#truth-labels) · [UNKNOWN](#unknown) · [Validation](#validation) · [ValidationReport](#validationreport) · [Watcher](#watcher) · [Wiki source](#wiki-source) · [WithdrawalNotice](#withdrawalnotice) · [WORK](#work)

---

## Terms

### ABSTAIN

A finite response outcome used when the system can operate safely but cannot support an answer—for example because evidence is missing, stale, conflicted, unresolved, outside scope, or insufficient for the requested precision. `ABSTAIN` is not an error and is not a weaker form of `DENY`.

**See:** [ADR-0020 (proposed)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0020-abstain-is-a-first-class-decision.md) · [RuntimeResponseEnvelope](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/contracts/runtime/runtime_response_envelope.md)

### Accepted ADR

An Architecture Decision Record whose repository status and adoption evidence make the decision effective within its stated scope. A proposed ADR may guide discussion but cannot authorize dependent structural or authority-changing work as though it were accepted.

### ADR

An **Architecture Decision Record**: a durable record of a significant design or governance choice, its context, alternatives, consequences, status, and supersession path. ADRs decide; architecture notes and planning documents explain or propose.

### AIReceipt

A process record describing a governed AI operation: relevant inputs or evidence references, effective adapter/model configuration, finite outcome, citations, policy posture, and other replay or accountability details defined by its owning contract. It does not make generated language true or released.

### ANSWER

The finite outward outcome used when a response is in scope and supported by admissible evidence, applicable policy, required citations, freshness/correction state, and evidence-supported precision. An `ANSWER` must not be inferred merely from model confidence or successful execution.

### Artifact

A durable or transient product of repository, data, validation, build, release, or runtime work. The word says nothing by itself about authority: an artifact may be source material, a candidate, a receipt, a proof, a derived carrier, or a released product.

### Authority ladder

The rule for deciding which evidence or governing surface controls a specific question. KFM resolves placement, meaning, current behavior, admissibility, and release using the authority appropriate to that question rather than treating every document or file as equal.

### Canonical

The currently governing or single-writer source for a defined responsibility. Canonical does **not** mean infallible, public, implemented, released, or immutable; it means competing writable authorities are not allowed for that responsibility.

### CATALOG

The governed discovery and interoperability projection produced from validated upstream state. Catalog presence does not prove evidence closure, policy approval, release, or publication.

### Citation validation

A check that citations are present, structurally valid, resolvable as required, in scope, and consistent with the claims they support. Passing citation validation does not prove the underlying claim true beyond the evidence and checks actually examined.

### Cite-or-abstain

KFM’s default truth posture: a consequential statement must resolve admissible support, or the system narrows scope or returns `ABSTAIN` rather than inventing certainty.

### Compatibility surface

A legacy path, mirror, alias, external export, or transitional path retained for verified consumers. Compatibility should be single-write, bounded by an owner, parity checks, exit criteria, and rollback; it must not become a second writable authority.

### CONFIRMED

A core truth label meaning the claim was verified within the stated evidence boundary. `CONFIRMED` is always scoped: it does not silently prove adjacent behavior.

### Contract

The human-readable semantic authority for what an object, field, interface, or operation means. A contract is distinct from the paired schema, applicable policy, and implementation.

### CorrectionNotice

A first-class record identifying what was wrong, the affected object or release, the correction scope and time, successor or supersession links, and required propagation. A correction does not erase prior lineage.

### DENY

A finite outcome indicating that an operation or response is not allowed because policy, rights, sensitivity, source role, access, release state, or exposure risk blocks it. A denial should reveal only safe reason information.

### Derived artifact

A rebuildable output—such as a tile archive, raster derivative, index, graph projection, summary, scene, score, or generated explanation—produced from upstream state. Derived artifacts remain derived and do not replace canonical evidence.

### Deterministic identity

An identity rule that produces the same identifier for the same governed inputs and versioning context where practical. It supports deduplication, replay, correction, cache invalidation, and audit.

### Directory Rules

The adopted placement law describing how responsibility, lifecycle, execution role, scope, exposure, mutability, retention, compatibility, and migration determine repository paths. A path is an authority claim, not a convenience label.

**See:** [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md) · [ADR-0029](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)

### Domain lane

A domain-specific segment inside the responsibility roots that own documentation, contracts, schemas, policy, fixtures, tests, lifecycle data, and release objects. A domain name normally does not justify a new repository root.

### ERROR

A finite outward outcome indicating that a resolver, validator, adapter, policy service, runtime, or other required mechanism failed. `ERROR` must fail safely rather than falling back to an unsupported answer.

### EvidenceBundle

A resolved package of support that identifies sources, source roles, scope, provenance, limitations, citations, and other fields defined by its contract. EvidenceBundle outranks generated language, map pixels, graph edges, and summaries.

### Evidence Drawer

A trust-visible UI surface that presents evidence-backed detail, source role, time and spatial scope, policy/release state, transformations, limitations, and correction posture for a selected claim or feature.

### EvidenceRef

A stable pointer from a claim, object, or response to evidence that should resolve through governed services. A reference is not the evidence payload and may fail to resolve, be denied, or be stale.

### Fixture

A bounded test input and expected result used to prove schema, validator, policy, runtime, or workflow behavior. Synthetic and public-safe fixtures are preferred; a fixture is not live domain truth.

### Focus Mode

A bounded, map-context-aware interpretive interface that operates through governed APIs and finite outcomes. It may explain released evidence; it cannot turn model language or browser properties into authority.

### GENERATED_RECEIPT

A per-artifact provenance record for AI-authored or substantively AI-modified work. It binds artifact paths and hashes, model/contract identity, inputs, truth labels, validation gates, citations, and human-review state. It is process memory—not approval, proof, policy, release, or publication.

### Governed API

The executable trust membrane used by ordinary public and semi-public clients. It resolves permitted state and returns bounded envelopes instead of exposing canonical/internal stores or direct model-runtime output.

### Harmful precision

Spatial, temporal, attribute, relationship, or operational detail whose exposure could create privacy, ecological, archaeological, cultural, infrastructure, security, or other harm. KFM redacts, generalizes, stages, delays, denies, or abstains before public delivery when precision is unsupported or unsafe.

### HOLD

A review or transition disposition indicating that one or more prerequisites remain unresolved. `HOLD` is intentional fail-closed behavior, not a permissive default and not the same as `ABSTAIN`.

### Inspectable claim

A claim whose evidence, source role, spatial and temporal scope, transformations, policy posture, review state, release state, correction lineage, and rollback context can be examined at the level appropriate to its significance.

### Integrity

Evidence that bytes, identifiers, manifests, references, or signed statements have not changed unexpectedly and correspond to declared inputs. Integrity does not prove factual truth, rights clearance, policy approval, or public safety.

### Lifecycle

The governed movement of data and accountability state through `(Pre-RAW) -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`. Promotion is a governed transition, not a file move.

### Manifest

A structured record binding an identified set of objects or artifacts to versions, digests, dependencies, source/release context, and other declared metadata. A manifest is not a release decision by itself.

### MapLibre

KFM’s primary web map renderer and interaction runtime. MapLibre is downstream of trust: it renders released layers and emits interaction context, but it does not establish truth, evidence, policy, review, or publication.

### Merge

A repository-history transition that incorporates reviewed commits into a target branch. Merge does not itself activate a source, move lifecycle state, deploy software, approve policy, release data, synchronize the native wiki, or publish KFM claims.

### Native wiki projection

The separately synchronized GitHub Wiki repository that presents an allowlisted, reviewed orientation page set. It is downstream of `docs/wiki/`, not a second writable KFM authority.

### NEEDS VERIFICATION

A core truth label meaning a concrete check could resolve the question but has not yet been completed strongly enough to rely on the claim.

### Negative state

A first-class bounded result such as `ABSTAIN`, `DENY`, `ERROR`, `HOLD`, stale, conflicted, withdrawn, or unresolved. Negative states are not empty spaces to be filled with confident prose.

### Object family

A group of records sharing one semantic responsibility, identity model, contract/schema relationship, lifecycle role, and governance posture—for example EvidenceBundle, receipt, release, or correction families.

### Policy

The canonical source of admissibility rules: under which conditions an operation is allowed, denied, restricted, held, redacted, delayed, generalized, or obligation-bearing. Policy does not create evidence or factual truth.

### PolicyDecision

A governed result from evaluating a bounded operation and input context against an identified policy version. It records the outcome, safe reasons, and obligations; it does not replace evidence, review, or release authority.

### Pre-RAW

The admission stage for source-change events, watcher signals, and candidate intake before material becomes RAW. Pre-RAW events are non-public, auditable, and cannot publish.

### PROCESSED

Validated normalized records or products ready for catalog, evidence, or proof closure. `PROCESSED` does not automatically mean public-safe, released, or published.

### Promotion

A governed state transition supported by identity, evidence, validation, policy, review, integrity, release context, correction, and rollback. Promotion is never inferred from a copy, path, workflow completion, merge, or deployment.

### Proof

Verifiable support for a declared condition, such as schema validity, citation closure, integrity, review, or release readiness. Proof remains distinct from receipts, catalogs, policy decisions, and releases.

### PROPOSED

A core truth label for a design, recommendation, path, placement, interpretation, or future state not yet verified as current implementation or adopted authority.

### Public-safe

Transformed and reviewed for the intended audience so that rights, sensitivity, harmful precision, source terms, and reconstruction risk are handled. Public-safe is audience- and release-specific; it does not mean unrestricted forever.

### Publication

The governed act of exposing an approved release to an intended audience through public or semi-public products. Publication is separate from merge, deployment, wiki synchronization, and artifact generation.

### PUBLISHED

The lifecycle state for immutable or versioned release-approved public-safe carriers. Placement under a published-looking path does not establish this state without the required decision and lineage.

### QUARANTINE

The fail-closed lifecycle lane for material whose identity, rights, sensitivity, validity, quality, policy, or release posture is unresolved or unsafe. Exit requires recorded remediation and re-evaluation.

### RAW

The immutable or append-only source-edge capture, preserving source-native bytes or governed logical pointers and retrieval identity. RAW is non-public and is not normalized truth.

### Receipt

A process-memory record describing what ran, against which inputs, with which tools/configuration, and which outputs or dispositions resulted. A receipt is not factual proof, policy approval, review, or release by itself.

### Registry

A governed collection of stable identities and operating metadata—for example sources, datasets, layers, rights, sensitivity, or crosswalks. Registry presence does not make the registered subject true, active, public, or released.

### Release

A governed decision and identified set prepared for an intended audience, with required evidence, policy, review, integrity, correction, and rollback context. A GitHub release, deployment, or file bundle is not automatically a KFM release.

### ReleaseManifest

A release-governance record binding a released set, versions, digests, dependencies, policy/review references, correction behavior, and rollback target. A manifest does not self-approve the release it describes.

### Replay

A controlled attempt to re-run or re-evaluate a process from pinned inputs, versions, policies, and configurations to reproduce or compare declared outcomes. Replay evidence can expose drift.

### Responsibility root

A top-level repository directory admitted because it owns one project-wide responsibility—such as human documentation, contracts, schemas, policy, applications, data lifecycle, or release decisions. Roots are authority boundaries, not topic buckets.

### Review

An authenticated human or governed reviewer judgment recorded separately from generation and validation. Review is not inferred from CODEOWNERS routing, mergeability, or an author’s own receipt.

### Rollback

A governed response that retires or replaces an active release, reverses a deployment or projection where possible, invalidates affected caches, and preserves lineage. Rollback does not erase history or turn derived state back into RAW.

### RuntimeResponseEnvelope

The governed client-facing response object carrying the finite outcome, safe reason information, evidence references, policy/freshness/correction state, and—for `ANSWER`—the precision actually supported. It is a trust-membrane envelope, not evidence storage or public truth by itself.

### Schema

The machine-readable authority for valid object shape: required fields, types, enums, patterns, conditional requirements, and closed/open properties. A schema cannot decide what an object means, whether its contents are true, or whether the operation is allowed.

### Sensitivity

The risk and handling posture associated with exposing, combining, transforming, or retaining information. Sensitivity may depend on audience, precision, joins, time, sovereignty, living-person status, ecological or archaeological risk, infrastructure context, rights, and source terms.

### SourceActivationDecision

The governed decision recording whether and under what conditions a source may move from proposed or observed status into active acquisition/admission posture. Activation does not mean every retrieved record is admissible, true, public-safe, or released.

### SourceDescriptor

The governed identity and operating record for a source: stable identifier, authority/source role, steward, access method, rights and terms, cadence, scope, citation requirements, sensitivity, activation state, and other fields required by its contract.

### Source role

The explicit function a source may play in supporting a claim—for example observation, authoritative interpretation, forecast, model, aggregate, regulatory record, historical context, or synthetic fixture. Similar content or geometry does not make roles interchangeable.

### `spec_hash`

A digest binding an object, receipt, run, or envelope to the effective specification, contract, schema, policy bundle, configuration, or other declared semantic inputs. Exact canonicalization and hash rules come from the owning object-family contract.

### Steward

A role accountable for a bounded responsibility such as a domain, source, policy family, evidence process, schema, release, or documentation lane. A role name is not automatically a verified GitHub identity or reviewer assignment.

### Supersession

The explicit relationship by which a newer object, document, decision, or release replaces an older one while preserving identity, history, reason, effective scope, and correction/rollback implications. Superseded does not mean deleted.

### TRIPLET / TRIPLETS

A derived relationship or graph projection built from governed records and evidence. Current documents may use singular `TRIPLET` for the lifecycle concept and plural `triplets/` for a collection path; neither form makes graph edges sovereign truth.

### Trust membrane

The boundary preventing ordinary clients and public surfaces from reaching RAW, WORK, QUARANTINE, candidate, canonical/internal, restricted, or direct model-runtime state. Governed interfaces expose only the evidence-, policy-, review-, and release-bounded response allowed for the audience.

### Truth labels

The core evidence-status vocabulary: `CONFIRMED`, `PROPOSED`, `UNKNOWN`, and `NEEDS VERIFICATION`. Qualifiers such as conflicted, stale, superseded, or inferred may add context but do not replace the core label.

### UNKNOWN

A core truth label meaning the available evidence is insufficient to determine the claim or the question is not resolvable within the current evidence boundary. `UNKNOWN` is an honest state, not permission to guess.

### Validation

A deterministic or reviewable check of declared shape, semantics, policy preconditions, integrity, compatibility, topology, links, or other bounded conditions. Validation proves only the checks, inputs, version, and outcome actually recorded.

### ValidationReport

A record of which validator or test profile ran, against which inputs and versions, which checks passed or failed, reason codes, limitations, and resulting disposition. It is not a policy decision, human approval, or release manifest.

### Watcher

Automation that detects source or repository change and emits bounded events, candidates, observations, or receipts. A watcher may trigger review work; it is never a publisher and must not write `PUBLISHED` state directly.

### Wiki source

The reviewable Markdown page under `docs/wiki/` that participates in the main repository’s branch, pull-request, receipt, correction, and rollback workflow. It is the source for a later native-wiki projection, not a substitute for canonical KFM sources.

### WithdrawalNotice

A first-class record declaring that a release, artifact, claim, or public exposure is withdrawn, including scope, effective time, reason, successor/correction relationships, and propagation obligations. Withdrawal preserves lineage and is not silent deletion.

### WORK

The non-public transformation and quality-assurance stage where RAW inputs become normalized or interpreted candidates. Failed, unsafe, or unresolved work routes to QUARANTINE; manual changes must remain traceable.

## How this glossary is maintained

1. **Preserve page identity and stable term headings.** Existing term anchors should not be renamed casually because wiki pages and external readers may link to them.
2. **Update from the owning authority.** A material definition change should follow the accepted ADR, doctrine, contract, schema, policy, or implementation change that actually changed the term.
3. **Do not normalize conflicts silently.** Label the conflict or open the appropriate ADR, drift, or verification work rather than inventing one blended definition.
4. **Keep orientation concise.** Detailed field semantics belong in contracts and schemas; operational procedure belongs in runbooks.
5. **Validate before projection.** Check one H1, anchors, relative links, repository targets, public safety, generated-receipt integrity, and exact-head documentation checks.
6. **Synchronize separately.** Updating this source page does not update or publish the native GitHub Wiki.

## Canonical vocabulary sources

| Source | Role |
|---|---|
| [Doctrine index](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/README.md) | KFM-wide invariants and governing doctrine |
| [Doctrine encyclopedia](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/encyclopedia.md) | Doctrine vocabulary and concept cross-reference |
| [Directory Rules](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md) | Placement, responsibility roots, compatibility, migration, and lifecycle/accountability homes |
| [Lifecycle Law](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/lifecycle-law.md) | Stage meanings and publication-as-transition |
| [Trust Membrane](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/trust-membrane.md) | Governed public-client boundary |
| [Contracts](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/contracts) | Semantic meaning for object families and interfaces |
| [Schemas](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/schemas) | Machine-valid object shape |
| [Policy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/tree/main/policy) | Admissibility, reason codes, obligations, rights, sensitivity, and release constraints |
| [Data root](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/data/README.md) | Lifecycle and accountability materialization |
| [Release root](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/release/README.md) | Release decisions, manifests, correction, withdrawal, and rollback |
| [Wiki source contract](README.md) | Source-versus-native-wiki boundary and maintenance rules |

---

[Home](Home.md) · [Architecture](Architecture.md) · [Governance and Evidence](Governance-and-Evidence.md) · [Data Lifecycle](Data-Lifecycle.md) · [Back to top](#top)
