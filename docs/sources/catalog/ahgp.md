<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://docs/sources/catalog/ahgp-flat-index
title: AHGP Source-Family Catalog — Flat-Path Navigation Boundary
type: source-catalog index; compatibility navigation; implementation-status boundary
version: v1.0.0
status: repository-grounded; navigation-only; source-not-admitted; connector-placeholder
owners: NEEDS VERIFICATION — source, archaeology, people/genealogy, rights, sensitivity, and connector stewards
updated: 2026-08-29
policy_label: source-candidate; rights-review-required; sensitivity-review-required; non-publisher
current_path: docs/sources/catalog/ahgp.md
owning_root: docs/
truth_posture: >
  CONFIRMED flat path, detailed AHGP directory, five product pages, proposed
  archaeology registry template, and placeholder connector package at the
  reviewed base / UNKNOWN flat-versus-directory canonical status, rights,
  authority, role, cadence, access, and stewardship / DENY source admission,
  activation, claim authority, release, or publication from catalog presence
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 2b0ea9bbbc9d9a120ea94d92fb4617d96fe7d2a0
  prior_blob: 3cf7b62914a0ffeff41d37e7bfe59aba6f19aae8
  method: complete target read; catalog family, product pages, registry template, connector tree, schema index, open-PR, Drive, and Notion inspection
notes:
  - "Replaces proposal-era prose at the same path without declaring a document-identity supersession relationship."
  - "No source, descriptor, connector, lifecycle, release, or publication state is superseded."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AHGP Source-Family Catalog — Flat-Path Navigation Boundary

This flat file routes maintainers to the current American History and Genealogy
Project (AHGP) catalog, registry-candidate, and connector documentation. It is
not a source descriptor, source admission, activation decision, rights finding,
genealogy authority, EvidenceBundle, release record, or publication surface.

> [!IMPORTANT]
> The detailed AHGP family page and five product pages already exist under
> [`docs/sources/catalog/ahgp/`](./ahgp/README.md). Do not create a second
> full family page here or treat this shorter path as higher authority.

## Correction from the prior stub

The prior page contained two materially stale directions:

| Prior direction | Current repository evidence |
|---|---|
| Use `data/registry/sources/ahgp.yaml` as the source descriptor. | That path does not exist. The committed AHGP registry candidate is [`data/registry/archaeology/sources/ahgp.yaml`](../../../data/registry/archaeology/sources/ahgp.yaml). |
| Replace this file with a full source-family page. | A substantive [AHGP family page](./ahgp/README.md) and five product pages already exist in the adjacent directory. |

The existing registry YAML is explicitly a **PROPOSED greenfield template**.
Its role, authority, license, redistribution, sensitivity floor, cadence,
access posture, and citation template remain `TBD`. Its presence does not
admit or activate AHGP.

## Current repository map

| Surface | Current role | Bounded status |
|---|---|---|
| [AHGP family page](./ahgp/README.md) | Detailed source-family research, candidate role, rights, sensitivity, lifecycle, and activation prerequisites | Draft; proposed specifics; not activation authority |
| [Cemetery transcriptions](./ahgp/cemetery-transcriptions.md) | Product-family catalog page | Candidate documentation only |
| [Census transcriptions](./ahgp/census-transcriptions.md) | Product-family catalog page | Candidate documentation only |
| [County and town histories](./ahgp/county-town-histories.md) | Product-family catalog page | Candidate documentation only |
| [Family trees](./ahgp/family-trees.md) | Product-family catalog page | Candidate documentation only |
| [Newspaper and obituary transcriptions](./ahgp/newspaper-obituary-transcriptions.md) | Product-family catalog page | Candidate documentation only |
| [Archaeology registry candidate](../../../data/registry/archaeology/sources/ahgp.yaml) | Proposed AHGP source metadata template | Unresolved `TBD` fields; not admitted |
| [AHGP connector lane](../../../connectors/ahgp/README.md) | Source-specific connector boundary | Draft, placeholder-only implementation |
| [Connector source inventory](../../../connectors/ahgp/src/README.md) | Exact package and module status | `0.0.0`; empty or comment-only Python modules |
| [Connector-local descriptor placeholder](../../../connectors/ahgp/src/ahgp/descriptor.yaml) | Package-local placeholder metadata | `role: TBD`, `rights: TBD`; not a registry decision |

No current file in this map establishes a live endpoint, accepted crawling
method, stable URL pattern, permission to retrieve, source role, redistribution
right, privacy disposition, or public-use approval.

## Navigation rule

Use the narrowest current surface for the task:

- source-family research, role distinctions, and activation prerequisites:
  [AHGP family page](./ahgp/README.md);
- product-specific source limitations: the relevant product page listed above;
- current proposed domain registry bytes:
  [archaeology AHGP YAML](../../../data/registry/archaeology/sources/ahgp.yaml);
- connector implementation status:
  [AHGP connector](../../../connectors/ahgp/README.md) and
  [source inventory](../../../connectors/ahgp/src/README.md);
- source-descriptor machine-shape drift and validation posture:
  [source schema family](../../../schemas/contracts/v1/source/README.md);
- general catalog rules: [source catalog index](./README.md);
- admission procedure: [source admission process](../ADMISSION_PROCESS.md);
- rights and sensitivity:
  [rights guidance](../RIGHTS_GUIDANCE.md) and
  [catalog rights/sensitivity map](./RIGHTS-AND-SENSITIVITY-MAP.md).

The repository does not yet establish whether the flat `ahgp.md` path should
remain a permanent compatibility pointer, be retired after reference closure,
or have another role. This page records navigation without deciding that
topology question.

## Source-role and evidence boundary

AHGP is a volunteer-hosted aggregation and transcription surface, not automatic
authority for every underlying record or claim. A product page may preserve
candidate context, but a consequential statement about a person, family
relationship, residence, burial, event, or place must retain the source role
and support appropriate to that claim.

Where the underlying record is identified, cite and evaluate that record rather
than laundering authority through the convenient AHGP copy. Where support,
identity, time, or provenance is insufficient, narrow the claim or abstain.

## Rights and sensitivity hold

Before any retrieval or admission, resolve at least:

- AHGP page-level terms and attribution requirements;
- rights in the underlying record, transcription, compilation, image, and
  contributor material;
- whether redistribution, caching, quotation, or derivative use is permitted;
- living-person, obituary, cemetery, burial, address, family-linkage, and
  culturally sensitive content;
- harmful precision, private-land implications, and join-induced sensitivity;
- source authority, source role, update cadence, access posture, and steward;
- correction, removal, withdrawal, retention, and rollback behavior.

Unknown or conflicted rights, sensitivity, consent, provenance, or authority
must route to a governed hold, quarantine, denial, or abstention. A catalog
page, YAML file, connector path, validation pass, pull request, or merge cannot
resolve those questions by itself.

## Activation and lifecycle boundary

The current connector package contains placeholder metadata and no implemented
fetch or admission function. The test directory contains no executable AHGP
tests. Therefore this page does not provide a command for source retrieval.

Any future source operation must separately establish:

1. a reviewed descriptor with no unresolved required fields;
2. rights, attribution, access, rate-limit, privacy, sensitivity, and source-role
   decisions;
3. explicit endpoint configuration and bounded traversal;
4. deterministic, rights-safe no-network fixtures and positive/negative tests;
5. fail-closed admission to RAW or QUARANTINE only;
6. provenance, retrieval time, content digest, and receipt behavior;
7. downstream evidence, policy, review, correction, release, and rollback
   dependencies.

The default lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

No catalog or connector document performs a lifecycle transition.

## Maintenance guidance

- Update this pointer when the detailed family directory, product inventory,
  registry candidate, or connector status changes.
- Do not duplicate the detailed family page into this flat file.
- Do not rewrite the registry path until an actual reviewed migration changes
  the committed authority surface.
- Preserve explicit `PROPOSED`, `UNKNOWN`, and `NEEDS VERIFICATION`
  labels until current repository evidence supports a narrower result.
- Resolve flat-file versus directory topology only through a link-preserving,
  reversible documentation decision.

## Open verification register

| Question | Status |
|---|---|
| Flat `ahgp.md` versus directory `ahgp/README.md` disposition | `NEEDS VERIFICATION` |
| Accepted AHGP descriptor and registry home | `NOT ESTABLISHED` |
| Source role, authority, rights, redistribution, cadence, and access | `TBD / HOLD` |
| Accountable source and sensitivity stewards | `NEEDS VERIFICATION` |
| Stable endpoint, rate limit, and retrieval method | `UNKNOWN` |
| Connector implementation and no-network tests | `ABSENT` |
| Source activation, admitted payloads, evidence closure, and release | `NOT PROVED` |

[Back to top](#top)
