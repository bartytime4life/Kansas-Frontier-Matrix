<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-root-readme
title: docs/ — Human-Readable Governance and Explanation Root
type: readme/root-readme
authority: documentation-boundary
version: v1.0
status: active
owners:
  - "@bartytime4life"
created: "NEEDS VERIFICATION — root README predates this modernization"
updated: 2026-08-08
policy_label: repository-facing
owning_root: docs/
responsibility: "Define the docs/ responsibility boundary, navigation contract, exposure posture, validation expectations, and relationships to KFM authority roots."
truth_posture: "CONFIRMED current repository and adopted Directory Rules evidence / NEEDS VERIFICATION exhaustive nested inventory, external consumers, and independent stewardship"
related:
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - control_plane/README.md
  - control_plane/document_registry.yaml
  - contracts/README.md
  - schemas/README.md
  - policy/README.md
  - tests/README.md
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `docs/` — Human-Readable Governance and Explanation Root

`docs/` is KFM's canonical human-readable governance and explanation surface. It explains doctrine, decisions, architecture, domain guidance, operations, source use, standards, security, drift, and verification without taking over the machine authority of contracts, schemas, policy, evidence, release objects, or lifecycle data.

> [!IMPORTANT]
> **Documentation is part of the working control system, but documentation is not sovereign truth.** A Markdown file, PDF, diagram, badge, pull request, or passing documentation check does not by itself create source authority, evidence closure, policy approval, release state, promotion, publication, or runtime behavior.

## Quick navigation

- [Purpose and authority](#purpose-and-authority)
- [Adoption and conformance](#adoption-and-conformance)
- [What belongs here](#what-belongs-here)
- [Inputs, outputs, and writers](#inputs-outputs-and-writers)
- [Exposure and sensitivity](#exposure-and-sensitivity)
- [Mutability, retention, and storage](#mutability-retention-and-storage)
- [Validation](#validation)
- [Ownership and review](#ownership-and-review)
- [Governing decisions and adjacent authorities](#governing-decisions-and-adjacent-authorities)
- [Direct-child map](#direct-child-map)
- [Evidence review and triggers](#evidence-review-and-triggers)

## Purpose and authority

| Field | Current contract |
|---|---|
| Root | `docs/` |
| Root class | Canonical governance and authority root |
| Primary responsibility | Human-readable governance, explanation, decision history, operational guidance, source guidance, standards guidance, and documentation lineage |
| Authority owner | Documentation responsibility under the adopted Directory Rules; repository review currently routes to `@bartytime4life` where CODEOWNERS applies |
| Normal consumers | Maintainers, reviewers, stewards, developers, operators, researchers, and other repository documentation |
| Public-path role | Repository-facing documentation only; not a normal data or runtime API |
| Trust posture | Cite or abstain; keep implementation, adoption, review, release, and publication claims bounded by evidence |

The adopted Directory Rules define `docs/` as the human-readable governance and explanation surface. They separate it from `control_plane/`, which projects accepted governance for machines; `contracts/`, which defines meaning; `schemas/`, which defines machine shape; and `policy/`, which decides admissibility.

## Adoption and conformance

**CONFIRMED:** ADR-0029 is accepted and adopts the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md`. Under that adopted standard, every canonical root uses the `ROOT_FULL` README profile.

**CONFIRMED:** this file already existed at `docs/README.md`, so this change keeps the same path and upgrades the boundary description in place. No root, authority owner, lifecycle phase, schema home, policy home, release home, or public interface is created by this README.

**NEEDS VERIFICATION:** exhaustive conformance of every nested documentation lane, every external consumer, every historical alias, and independent stewardship is outside this root README's evidence boundary.

## What belongs here

Content belongs under `docs/` when its primary responsibility is to explain something to humans or record a human-readable governance decision. Typical families include:

- accepted and proposed ADRs plus decision history;
- architecture descriptions subordinate to accepted decisions;
- stable doctrine and operating law;
- domain and cross-domain human guidance;
- operational runbooks and maintenance procedures;
- human-readable drift, verification, and governance registers;
- security, threat, incident, and exposure guidance;
- source guidance, attribution notes, and human source catalogs;
- KFM and external standards guidance;
- curated atlases, reports, implementation references, and frozen historical documentation when their lane contract permits them.

### Prohibited authority collapse

The following do **not** belong here as their canonical writable authority merely because documentation describes them:

| Artifact or responsibility | Canonical authority family |
|---|---|
| Machine governance registers and projections | `control_plane/` |
| Semantic object/interface contracts | `contracts/` |
| Machine-valid object shapes | `schemas/` |
| Policy rule source | `policy/` |
| Executable validators, generators, operators, or pipeline code | `tools/`, `pipelines/`, `packages/`, `apps/`, or another execution root selected by role |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLETS, PUBLISHED data instances | `data/` lifecycle and accountability lanes |
| Receipts and proofs | Their governed `data/` accountability families |
| Release decisions, manifests, correction notices, and rollback cards | `release/` and the adopted release/data accountability families |
| Secrets or private credentials | Never committed to documentation |

> [!CAUTION]
> A document may **reference** any of these families. It must not become a parallel writable copy of their authority. When documentation and current implementation disagree, preserve the disagreement explicitly and route the correction through the owning authority.

## Inputs, outputs, and writers

### Inputs

Documentation may consume and explain:

- accepted doctrine and ADRs;
- current repository files, configs, contracts, schemas, policy, tests, workflows, manifests, and generated artifacts;
- evidence and release state when a claim depends on them;
- source terms, standards, and authoritative external references when currentness matters;
- bounded design lineage such as prior reports, atlases, and implementation plans.

Inputs do not gain authority merely by being cited here. Historical plans and generated prose remain lineage or proposal material unless stronger evidence upgrades them.

### Outputs

The root produces human-readable artifacts such as doctrine, ADRs, architecture notes, runbooks, domain guidance, source guidance, standards profiles, review guidance, reports, and documentation indexes. Machine projections derived from accepted documentation belong in `control_plane/` or another owning machine authority and must preserve their source relationship.

### Permitted writers

Normal writers are reviewed repository changes made by maintainers or authorized automation on feature branches. Writers must preserve stable identity, anchors, metadata, generated/mirror boundaries, and current truth labels where material.

Documentation automation may validate or propose changes. It must not use its own generated prose, metadata, receipt, badge, or pull request as human approval, evidence authority, release authority, or publication authority.

## Exposure and sensitivity

`docs/` is repository-facing and may be publicly readable when the repository is public. Treat that visibility as an exposure boundary.

Do not commit secrets, private endpoints, signed URLs, private personal data, restricted source material, protected exact locations, or other content whose rights or sensitivity posture is unresolved. For living-person, genomic, rare-species, archaeology, infrastructure, land/title, sovereignty, cultural, or harmful-precision material, documentation follows the same fail-closed posture as the rest of KFM: redact, generalize, stage, delay, abstain, deny, or quarantine as appropriate.

A public README may describe that a denial or redaction rule exists without leaking the protected payload or a sensitive reason that itself creates exposure.

## Mutability, retention, and storage

| Property | Rule |
|---|---|
| Physical storage | Tracked Git content unless a child lane declares a governed external or generated relationship |
| Mutability | Reviewed, versioned replacement; append-only history where the document class requires it |
| Retention | Durable for current authority and decision history; superseded material moves only through governed lineage or migration rules |
| Generated content | Edit the canonical source and regenerate; do not hand-edit a verified generated or mirrored output |
| Compatibility | Dual-read/single-write where an accepted migration requires an alias or tombstone |
| Deletion | Requires exact identity, inbound-reference review, migration/retirement evidence when applicable, and Git-recoverable rollback |

`docs/architecture/directory-rules.md` is a specific compatibility surface governed by ADR-0029; it must not evolve into a second Directory Rules authority.

## Validation

Documentation validation is evidence about repository quality, not proof of doctrine, implementation, security, release, or publication.

For changed Markdown, use the smallest repository-native check set that covers the actual delta. Depending on the file, that can include:

- `KFM_META_BLOCK_V2` validation and review-only document-registry comparison;
- Markdown structure, one-H1, heading-order, fence, table, alert, and HTML checks;
- repo-relative link, path, case, and fragment checks;
- stable anchor and inbound-reference checks when headings move;
- generated/mirror synchronization checks;
- documentation graph and stale-reference checks;
- secret, privacy, rights, and sensitivity review;
- repository-specific tests or workflows that directly govern the changed document family.

The `docs-meta-block` workflow is intentionally no-network for its validator path and treats its emitted document-registry delta as review-only. A green result does not mutate the registry or create authority.

### Negative checks

A documentation change should fail or be held when it would:

- create a second writable doctrine, contract, schema, policy, source, registry, release, receipt, or proof authority;
- claim implementation, deployment, review, release, or publication without supporting evidence;
- expose secrets, private data, restricted content, or unsafe precision;
- hand-edit a generated or mirror target instead of its canonical source;
- break a stable identity or known inbound anchor without compatibility handling;
- use an unaccepted governance proposal to authorize dependent structural work.

## Ownership and review

**CONFIRMED repository identity:** `bartytime4life/Kansas-Frontier-Matrix`.

**CONFIRMED named review route:** `@bartytime4life` is the currently verified named owner in accepted ADR-0029. Additional domain, architecture, policy, security, source, release, or documentation reviewers are required when a change crosses their responsibility boundary or significance warrants independent review.

**NEEDS VERIFICATION:** a complete independent documentation-steward roster and every nested lane's current CODEOWNERS route.

Escalate instead of guessing when a documentation change would alter authority, contradict an accepted ADR, change public-path behavior, expose sensitive material, create or retire a canonical lane, or require a destructive migration.

## Governing decisions and adjacent authorities

| Surface | Relationship to `docs/` |
|---|---|
| [`docs/doctrine/directory-rules.md`](doctrine/directory-rules.md) | Adopted placement law through ADR-0029 |
| [`docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`](adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted adoption decision and migration boundary for Directory Rules v2 |
| [`control_plane/`](../control_plane/README.md) | Machine-readable projection and governance-index root; cannot self-authorize doctrine |
| [`contracts/`](../contracts/README.md) | Semantic meaning authority |
| [`schemas/`](../schemas/README.md) | Machine-shape authority |
| [`policy/`](../policy/README.md) | Admissibility and policy-rule authority |
| [`tests/`](../tests/README.md) | Verification and regression evidence; passing tests are not publication authority |

## Direct-child map

The map below records the **adopted Directory Rules v2 canonical documentation lanes**, not an exhaustive listing of every current file or compatibility surface under `docs/`.

```text
docs/
├── adr/                    # architecture decisions and decision history
├── architecture/           # system structure subordinate to accepted decisions
├── archive/                # frozen lineage, not current authority
├── atlases/                # curated atlas collections
├── doctrine/               # stable KFM operating and trust law
├── domains/                # human domain guidance
├── registers/              # human-readable drift and verification views
├── runbooks/               # operational procedures
├── security/               # threat, incident, and exposure guidance
├── sources/                # source guidance and human source catalog
└── standards/              # KFM and external standards guidance
```

> [!NOTE]
> Current repository evidence also contains documentation artifacts and lanes beyond this canonical map. Their presence is implementation evidence, not automatic placement authority. Do not infer that an omitted current child should be deleted or migrated from this README alone; classify it against adopted Directory Rules, current consumers, and any applicable ADR before changing structure.

## Evidence review and triggers

**Last evidence review:** 2026-08-08 against `main@1001a87233e0f23695b6b12e60c654f938e6ffb5`, `docs/README.md` blob `7254b81741822a7f1cfdffa74ee9caece50fbc38`, adopted Directory Rules blob `fd49a0b83e55cef52c1124281f093e263526898d`, and accepted ADR-0029 blob `b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62`.

Re-review this boundary when:

- the `docs/` authority, root class, writer, consumer, exposure, sensitivity, or storage posture changes;
- a governing ADR is accepted or superseded;
- Directory Rules changes;
- CODEOWNERS or documentation validation coverage changes materially;
- a documentation compatibility deadline or tombstone phase arrives;
- drift, security, correction, withdrawal, or rollback affects documentation;
- a new canonical direct-child lane is admitted or an existing one is retired.

## Status

**CONFIRMED:** same-path root README modernization; adopted Directory Rules v2 and ADR-0029 evidence; repository-facing documentation boundary.

**NEEDS VERIFICATION:** exhaustive nested-lane conformance, external consumers, independent stewardship, and any structural migration not explicitly authorized by an accepted decision.

[Back to top](#top)
