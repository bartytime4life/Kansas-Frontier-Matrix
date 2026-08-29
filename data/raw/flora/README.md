<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/flora/readme
title: data/raw/flora/ — Flora RAW Compatibility and Reference Hold
type: data-lifecycle-domain-readme
version: v0.1.0
status: repository-grounded; compatibility-and-reference boundary; payload-empty; source-first-placement-unresolved; live-ingest-hold; no-direct-public-path; non-release; non-publication
owner: NEEDS VERIFICATION — repository review routing does not establish Flora source, rights, sensitivity, storage, operations, evidence, release, or publication authority
created: 2026-08-28
updated: 2026-08-28
current_path: data/raw/flora/README.md
owning_root: data/
policy_label: restricted-review; raw; flora; compatibility-projection; immutable-reference; source-first; live-ingest-hold; rare-plant-sensitive; non-public
responsibility: Prevent domain-first duplication by limiting this Flora compatibility lane to immutable references to admitted source-first capture identities, while routing source-native bytes only through an accepted source-first capture placement and failing unresolved material closed.
base_commit: 1bc300c5aeaf5323edead670d648edfb8c3f21c2
prior_blob: 5a43f1788b887bd38fc54e593c566a915976413b
truth_posture: CONFIRMED accepted Directory Rules require source-first capture identity so one capture can support several domains without duplicated RAW bytes / CONFIRMED this tracked domain lane contains only this README, one root .gitkeep, and four source-label subdirectories containing .gitkeep files / CONFIRMED no payload, admitted live source, accepted source-first physical placement, writer, restricted storage contract, independent readback, capture receipt, live connector command, or public consumer is established / HOLD live Flora retrieval and all writes / UNKNOWN accountable stewards, source-specific activation decisions, and disposition of this compatibility lane
related:
  - ../README.md
  - ../../registry/sources/flora/README.md
  - ../../registry/flora/sources/README.md
  - ../../work/flora/README.md
  - ../../quarantine/flora/README.md
  - ../../processed/flora/README.md
  - ../../../docs/runbooks/flora/SOURCE_REFRESH_RUNBOOK.md
  - ../../../docs/domains/flora/SOURCE_INTAKE.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../policy/domains/flora/README.md
  - ../../../tools/validators/domains/flora/README.md
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora RAW compatibility and reference hold

> **Purpose.** This directory is a payload-empty compatibility and domain-projection
> hold. After governed admission it may reference an immutable source-first capture;
> it must not become the physical home for source-native bytes, a second capture,
> an active ingest destination, a source registry, a working area, a public dataset,
> or a publication path.

> [!WARNING]
> **Live Flora retrieval and all writes remain on hold.** The current repository
> does not establish a complete admitted Flora source product, accepted activation
> decision, source-specific connector command, source-first physical capture
> placement, RAW writer, restricted storage contract, independent readback, or
> capture receipt. Do not write source-native bytes beneath this domain lane.

> [!CAUTION]
> Exact or inferable locations for rare, protected, threatened, culturally
> sensitive, steward-controlled, commercially vulnerable, or collection-sensitive
> plants must fail closed. A source response, upstream obscuration, path name, or
> successful transfer does not authorize exposure or publication.

## Authority and scope

Accepted [Directory Rules](../../../docs/doctrine/directory-rules.md) govern this
lane. Rule DIR-SOURCE-001 requires source-first capture identity so one capture can
support several domains without duplicated RAW bytes. This domain path therefore
cannot establish a physical capture home for cross-domain providers.

The parent [RAW boundary](../README.md) describes RAW responsibility but currently
shows a domain-first operating example. That example conflicts with the accepted
source-first identity rule and cannot authorize duplicated captures here. Until a
reviewed source-first physical placement and migration decision exists, this lane
is compatibility/reference-only. RAW placement does not decide admissibility,
normalize records, resolve taxonomy, prove botanical truth, or publish data.

Current source status must be determined from the canonical
[Flora source-registry lane](../../registry/sources/flora/README.md), its accepted
activation decision when one exists, and the canonical
[source-refresh runbook](../../../docs/runbooks/flora/SOURCE_REFRESH_RUNBOOK.md).
The parallel [domain-first source registry](../../registry/flora/sources/README.md)
is a compatibility/no-write surface and must not be used to invent admission.

This README documents routing and present limitations. It creates no source,
connector, policy decision, storage contract, receipt, evidence object, release,
deployment, promotion, or publication state.

## Current inventory

Verified at the pinned base commit:

```text
data/raw/flora/
├── .gitkeep
├── README.md
├── gbif/
│   └── .gitkeep
├── inaturalist/
│   └── .gitkeep
├── natureserve/
│   └── .gitkeep
└── usfws_ecos/
    └── .gitkeep
```

The four child names are inherited domain projections only. Their presence does
**not** prove that GBIF, iNaturalist, NatureServe, or USFWS ECOS is admitted,
active, licensed for a proposed use, connected, retrieved, retained, reviewed, or
public-safe. They must not receive domain-scoped copies of cross-domain captures.
No source payload, immutable capture reference, or capture receipt is tracked in
this lane.

## Admission and write prerequisites

Before any live request or RAW write, all of the following must resolve for one
exact source product:

1. one complete, current, schema-valid SourceDescriptor in the accepted registry;
2. an accepted activation/admission decision for the exact product, endpoint,
   request scope, fields, geography, temporal window, and source role;
3. current rights, terms, attribution, redistribution, record/media-license, and
   retention decisions;
4. current sensitivity, geoprivacy, harmful-precision, collection-security, and
   cultural-authority review;
5. one accepted connector home, pinned implementation, bounded command, host
   allowlist, rate/size/time limits, and credential reference without secret
   values;
6. deterministic no-network request, change-detection, capture, failure,
   cancellation, and sensitive-field fixtures;
7. an accepted source-first physical capture placement plus RAW and QUARANTINE
   writers with restricted storage, retention, cleanup, and independent readback;
8. an accepted privacy-safe capture/source-run receipt and writer; and
9. an accountable operator, escalation route, kill switch, and downstream
   correction notification path.

If any prerequisite is absent, ambiguous, expired, or contradicted, stop. Do not
infer it from a README, placeholder, connector directory, fixture, test, prior
capture, workflow result, or external planning document.

## Routing boundary

| Material or condition | Route | Boundary |
|---|---|---|
| Authorized, complete, immutable source-native bytes | Accepted source-first RAW placement through its writer | Do not store a domain-scoped copy here; preserve one capture identity for all authorized domain projections. |
| Approved immutable reference to a source-first capture | This compatibility lane only after an accepted reference contract exists | Preserve exact source/product/capture identity, rights, sensitivity, time, digest, and receipt references without copying bytes. |
| Partial transfer, schema/content-type drift, mixed rights, sensitive detail, ambiguous provenance, or unresolved completeness | [Flora QUARANTINE](../../quarantine/flora/README.md) | Record a bounded reason and review requirement; do not repair in place or publish. |
| Normalization, taxonomy reconciliation, deduplication, geospatial transformation, or derived analysis | [Flora WORK](../../work/flora/README.md) after an accepted handoff | RAW remains immutable; working transformations must not overwrite the capture. |
| Validated and normalized internal products | [Flora PROCESSED](../../processed/flora/README.md) through its owning procedure | A later lifecycle state is not implied by successful capture. |
| Registry, catalog, triplet, proof, release, deployment, or publication work | Its accepted owning surface and separate decision | No direct transition from this README or a source response. |
| Unknown rights, sensitivity, source identity, activation, writer, storage, or receipt | HOLD, DENY, ABSTAIN, or QUARANTINE as the accepted control requires | Never default to RAW or public visibility. |

RAW is not a public interface. Public clients must use governed interfaces or
released public-safe artifacts, not this directory or any internal canonical
store.

## Reference and capture-linkage envelope

An accepted source-first writer and any later domain-reference writer must preserve
or reference at least:

- stable source and exact product identity;
- descriptor and activation-decision references;
- request-scope identity without credentials;
- retrieval start/end and upstream version, release, cursor, manifest, or
  equivalent source head;
- source-native content identity, byte size, digest, and completeness result;
- response metadata permitted by rights and sensitivity controls;
- rights, attribution, sensitivity, geoprivacy, and cultural-authority references;
- source-first RAW or QUARANTINE destination identity and any domain-reference identity;
- writer version, independent readback result, and temporary-object disposition;
- finite outcome and privacy-safe reason codes; and
- an explicit statement that capture did not constitute admission, normalization,
  evidence closure, review, release, deployment, promotion, or publication.

Do not store API keys, tokens, cookies, authorization headers, hidden coordinates,
restricted locality text, reversible obscuration parameters, culturally restricted
knowledge, private-property access details, or unnecessary personal data in
tracked Markdown, broadly visible logs, pull requests, or public receipts.

## Current executable evidence

The [Flora validator boundary](../../../tools/validators/domains/flora/README.md)
documents one deterministic, no-network, synthetic public-safe fixture profile.
That profile can prove only its declared assertions at a pinned revision. It does
not contact an upstream source, exercise this RAW lane, validate a live connector,
establish rights or sensitivity clearance, or authorize a capture.

The canonical [source-refresh runbook](../../../docs/runbooks/flora/SOURCE_REFRESH_RUNBOOK.md)
contains the detailed finite outcomes, stop conditions, handoff packet, and
graduation gates. Its live-refresh determination remains **HOLD**.

## Focused validation

Run from the repository root:

```bash
git ls-tree -r --name-only HEAD data/raw/flora/
python tools/validators/docs/link-check/check_links.py \
  data/raw/flora/README.md \
  docs/runbooks/flora/SOURCE_REFRESH_RUNBOOK.md
python tools/validators/docs/meta-block/check_meta_blocks.py \
  --profile required \
  data/raw/flora/README.md \
  docs/runbooks/flora/SOURCE_REFRESH_RUNBOOK.md
```

The tree command confirms tracked paths only. The documentation validators confirm
their bounded link and metadata assertions only. None of these commands admits a
source, retrieves a payload, proves botanical truth, activates a writer, or
authorizes release or publication.

Also review the complete base-to-head diff for one H1 per file, balanced fences,
resolvable relative paths and fragments, final newlines, exact inventory claims,
and absence of secrets or sensitive Flora data.

## Maintenance, correction, and rollback

Recheck this README when the lane inventory, source-first placement, accepted
source registry, activation decision, connector, rights, sensitivity, storage,
writer, readback, receipt, retention, correction, or lifecycle contract changes.
Keep the canonical
source-refresh runbook synchronized with material maturity changes.

For an unmerged documentation change, rollback is closing the draft pull request
or reverting the focused branch commits. After merge, use a reviewed revert or a
bounded forward correction. Reverting this README to the prior stub removes
guidance only; it does not deactivate a source, revoke credentials, delete bytes,
withdraw evidence, reverse a lifecycle transition, or roll back a release.

## Open verification register

| ID | Open item | Current posture |
|---|---|---|
| FLORA-RAW-001 | Accepted Flora source product and activation decision | **NOT ESTABLISHED / HOLD** |
| FLORA-RAW-002 | Canonical source-specific connector command and bounded network contract | **NOT ESTABLISHED / HOLD** |
| FLORA-RAW-003 | Source-first physical capture placement; RAW and QUARANTINE writers, restricted storage, retention, and readback | **UNKNOWN / HOLD** |
| FLORA-RAW-004 | Privacy-safe capture/source-run receipt contract and writer | **NEEDS VERIFICATION** |
| FLORA-RAW-005 | Accountable source, rights, sensitivity, cultural, storage, operations, correction, and release stewards | **NEEDS VERIFICATION** |
| FLORA-RAW-006 | Accepted disposition of the four source-label subdirectories | **UNKNOWN** |

## Changelog

| Version | Date | Change | Runtime effect |
|---|---|---|---|
| v0.1.0 | 2026-08-28 | Replaced the greenfield stub with a source-first-safe compatibility/reference hold; prohibited domain-scoped copies of cross-domain source captures. | None; documentation only. |

[Back to top](#top)
