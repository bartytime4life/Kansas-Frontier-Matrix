<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/reports/adr-review-2026-11-19
title: ADR review and disposition — 2026-11-19
type: review-report
version: v1.0
status: draft; repository-grounded
owners: ["@bartytime4life"]
created: 2026-11-19
updated: 2026-11-19
policy_label: public
truth_posture: "Pinned repository review; recommendations are not decision acceptance"
responsibility_root: docs/
owning_root: docs/
evidence_base: c47f52e185bd1c6540801af8551c75cf12e6cbb6
[/KFM_META_BLOCK_V2] -->

# ADR review and disposition — 2026-11-19

The review found an omitted draft, stale inventory summaries, an obsolete shell
proposal and a renderer exception that was never recorded as an accepted
architecture decision. This packet repairs the documentation/control-plane gaps
and proposes the missing bounded exception.

## Scope and evidence

Base: `main@c47f52e185bd1c6540801af8551c75cf12e6cbb6`. All 49 numbered records' status,
decision summaries and inventory relationships, all 12 unassigned candidates,
the template and three inventory/support surfaces were reviewed. Targeted
implementation inspection covers the retired Explorer, preserved Site, MapLibre
package/seams, Three.js entrypoints and their existing scene tests. This is not
an implementation-conformance or acceptance audit of every subsystem.

The source index contains **49** numbered records: **11 accepted**, **38 proposed
effective** (27 source `proposed`, 11 source `draft`). Twelve unassigned candidates
exist, but the index table and validator found only eleven: discovery depended
on the exact prose phrase `PROPOSED scaffold`, which the Habitat schema-home
candidate no longer contains. The cross-register still described 37 records and
three accepted decisions; its copied counters were not an authority source.

After this packet, the canonical index contains **50** numbered records:
**11 accepted**, **39 proposed effective**, and all **12 unassigned candidates**.
Source metadata is 28 `proposed`, 11 `draft`, 11 `accepted`. No existing effective
status changes. There are 66 direct Markdown files in `docs/adr/`, including the
template and three support files. The report lives in `docs/reports/`.

## Changes made

1. Discover every unnumbered `ADR-*.md` candidate by path, excluding only the
   authoring template. Add the missing Habitat row without assigning a number.
2. Require valid Markdown separators for both inventory tables and reject stale
   visible index badges when present. Existing fixtures without badges remain
   valid; badges do not become an authority source.
3. Rewrite proposed ADR-0005 around the existing preserved Site, retaining its
   permanent ID, legacy filename, anchors and prior Git history. Remove current
   instructions for the retired consumer.
4. Add dated implementation evidence to accepted ADR-0006/0007. Preserve their
   decisions, earlier snapshot values and acceptance evidence. State that the
   Site MapLibre seam is a packaging exception, not general renderer permission.
5. Propose ADR-0050 for the two existing Three.js subsurface views. Its scope,
   alternatives, owner/review duties, acceptance, rollback and limitations are
   explicit. It is not an accepted exception or a runtime change.
6. Refresh index/README counts and make the cross-register a pointer without
   independent totals. Keep draft-to-proposed normalization conservative.

## Numbered-record disposition

`Retain` means no rewrite/deletion is justified by this review. It does not
accept a proposal or certify the implementation. Domain-specific migrations,
privacy/release choices and operational readiness remain separate decisions.

| Record | Existing effective status | Disposition and reason |
|---|---|---|
| [ADR-0001](<../adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md>) | `proposed` | Retain: schema routing and compatibility migration are a distinct proposal; accepted root placement does not accept every family migration. |
| [ADR-0002](<../adr/ADR-0002-contracts-vs-schemas-split.md>) | `proposed` | Retain: cross-surface coupling is distinct from schema placement. Draft metadata already normalizes conservatively to proposed. |
| [ADR-0003](<../adr/ADR-0003-policy-singular-is-canonical-(policies-is-compatibility).md>) | `proposed` | Retain: singular policy authority and compatibility retirement need a scoped migration, not deletion of a parallel path by inference. |
| [ADR-0004](<../adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md>) | `proposed` | Retain for API-boundary review: a proposed normal trust membrane is not proof that every current Site route uses it. |
| [ADR-0005](<../adr/ADR-0005-apps-explorer-web-is-the-canonical-map-first-shell.md>) | `proposed` | Rewrite now: replace retired-shell instructions with a proposed preserved-Site composition; keep ID, legacy filename, anchors and historical Git evidence. |
| [ADR-0006](<../adr/ADR-0006-maplibre-boundary--only-maplibreadapter-imports-maplibre.md>) | `accepted` | Update implementation evidence now: MapLibre 6.9.0, retired Explorer consumer and the already accepted Site seam. Preserve the accepted decision. |
| [ADR-0007](<../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md>) | `accepted` | Update implementation evidence now: distinguish normal map family, Site packaging exception and unresolved Three.js exception. Preserve accepted status. |
| [ADR-0008](<../adr/ADR-0008-ollama-subordinate-to-governed-api.md>) | `proposed` | Retain: local/provider AI subordination is a separate boundary from the adapter shape in ADR-0019 or Focus-specific orchestration. |
| [ADR-0009](<../adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md>) | `proposed` | Retain: first proof-bearing lane priority does not certify current source admission, release or operational proof. |
| [ADR-0010](<../adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md>) | `proposed` | Retain: cross-domain sensitive-data denial is not replaced by ordinary public-domain self-release exceptions. |
| [ADR-0011](<../adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md>) | `proposed` | Retain: receipts/proofs/manifests/catalog separation is distinct from release instance generation; no automatic artifact migration. |
| [ADR-0012](<../adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md>) | `proposed` | Retain: restricted connector sinks and receipt outputs are distinct from pipeline candidate transforms and downstream publication. |
| [ADR-0013](<../adr/ADR-0013-spec_hash-and-run_id-identity-grammar.md>) | `proposed` | Retain: identity grammar and migration are versioned decisions; no global hash or run-ID conversion is warranted by this review. |
| [ADR-0014](<../adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md>) | `proposed` | Retain: six time-kind identifiers are not a demand to rename all source-specific timestamp fields. |
| [ADR-0015](<../adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md>) | `proposed` | Retain: logical alias correction/rollback needs its own release binding; a mutable current pointer does not prove release permission. |
| [ADR-0016](<../adr/ADR-0016-telemetry-redaction-posture.md>) | `proposed` | Retain for privacy review: signal classification and redaction are independent of model/runtime selection; no new logging permission. |
| [ADR-0017](<../adr/ADR-0017-source-descriptor-admission-process.md>) | `proposed` | Retain: descriptor, activation and record-level admission remain separate from a successful connector or fixture run. |
| [ADR-0018](<../adr/ADR-0018-promotion-gate-sequence.md>) | `proposed` | Retain: the proposed A–G readiness profile must not silently replace existing versioned runtime gate profiles. |
| [ADR-0019](<../adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md>) | `proposed` | Retain: provider-neutral adapter/envelope proposal covers shared runtime semantics, unlike a single local provider or Focus view. |
| [ADR-0020](<../adr/ADR-0020-abstain-is-a-first-class-decision.md>) | `proposed` | Retain: ABSTAIN semantics remain distinct from errors, holds, pending work and empty results. |
| [ADR-0021](<../adr/ADR-0021-quarantine-has-structured-exit-paths.md>) | `proposed` | Retain: quarantine exit decisions need explicit lineage and review; no deletion or promotion follows from file presence. |
| [ADR-0022](<../adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md>) | `proposed` | Retain: STAC/DCAT/PROV agreement is a release-level contract, not a reason to merge those owning representations. |
| [ADR-0023](<../adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md>) | `proposed` | Retain: immutable geo-manifest/signature binding is distinct from catalog agreement and renderer acquisition. |
| [ADR-0024](<../adr/ADR-0024-steward-separation-of-duties-for-release.md>) | `proposed` | Retain: general review-separation proposal coexists with the accepted five narrowly scoped public-source self-release exceptions. |
| [ADR-0025](<../adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md>) | `proposed` | Retain for current API/export review: public delivery boundaries are not granted by browser rendering or a local route. |
| [ADR-0026](<../adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md>) | `proposed` | Retain: WBD HUC12 source-spine priority is distinct from first-lane selection and individual water-source admission. |
| [ADR-0027](<../adr/ADR-0027-county-focus-mode-control-plane.md>) | `proposed` | Retain: county Focus identity/control-plane proposal is distinct from state scope; no county-lane migration in this packet. |
| [ADR-0028](<../adr/ADR-0028 — State-scale Focus Mode scope.md>) | `proposed` | Retain: one Kansas state scope is distinct from 105 county scopes and from view/theme/version identities. |
| [ADR-0029](<../adr/ADR-0029-adopt-directory-governance-standard-v2.md>) | `accepted` | Retain accepted record unchanged: adopted doctrine, digest pins and migration history must not be rewritten as editorial cleanup. |
| [ADR-0030](<../adr/ADR-0030-geology-resource-character-vocabulary.md>) | `proposed` | Retain: geology resource-character vocabulary is domain claim semantics, not renderer or raw source naming. |
| [ADR-0031](<../adr/ADR-0031-shared-watcher-ownership-and-placement.md>) | `proposed` | Retain: shared watcher ownership separates inert registry, acquisition, orchestration and executable implementation. |
| [ADR-0032](<../adr/ADR-0032-attested-compute-boundary.md>) | `proposed` | Retain: attested-compute assessment is bounded simulation/proposal work, not authorization to operate a trusted runtime. |
| [ADR-0033](<../adr/ADR-0033-geoparquet-version-readiness.md>) | `proposed` | Retain: GeoParquet readiness separates adopted baseline and candidate evaluation; no standards/dependency upgrade is selected. |
| [ADR-0034](<../adr/ADR-0034-compass-qualitative-checklist-boundary.md>) | `proposed` | Retain: COMPASS qualitative planning is distinct from scoring, policy authority and source/release decisions. |
| [ADR-0035](<../adr/ADR-0035-repository-wide-adr-identity-numbering-and-domain-indexing.md>) | `proposed` | Retain proposed: global identity/pointer-only indexing remains a governance decision; this cleanup uses existing inventory convention without accepting it. |
| [ADR-0036](<../adr/ADR-0036-planning-encyclopedia-carrier-single-writer-and-scaffold-disposition.md>) | `proposed` | Retain: encyclopedia carrier/single-writer disposition requires its own ownership and compatibility decision. |
| [ADR-0037](<../adr/ADR-0037-evidence-drawer-payload-ui-authority-and-compatibility.md>) | `proposed` | Retain: EvidenceDrawerPayload family authority and retained compatibility projections need explicit migration review. |
| [ADR-0038](<../adr/ADR-0038-trusted-base-topology-correction-transitions.md>) | `accepted` | Retain accepted record unchanged: trusted-base exact-transition mechanism has a narrower scope than a general topology baseline update. |
| [ADR-0039](<../adr/ADR-0039-layer-manifest-frame-contract-home.md>) | `proposed` | Retain: LayerManifest/LayerFrame family routing is distinct from UI payload ownership and must not be merged by similar filenames. |
| [ADR-0040](<../adr/ADR-0040-catalog-redirect-metadata-corrections.md>) | `accepted` | Retain accepted record unchanged: exact catalog redirect target blobs and later binding/transition gates must keep their historical scope. |
| [ADR-0041](<../adr/ADR-0041-proportional-handling-of-inherited-repository-holds.md>) | `proposed` | Retain proposed: inherited-hold classification cannot weaken checks or declare current failures passed by editorial action. |
| [ADR-0042](<../adr/ADR-0042-people-dna-land-genealogy-validator-tooling-home.md>) | `proposed` | Retain: genealogy validator home/retirement is a tooling migration proposal, separate from policy ownership. |
| [ADR-0043](<../adr/ADR-0043-people-dna-land-genealogy-policy-tooling-home.md>) | `proposed` | Retain: genealogy policy-home/retirement is a separate authority boundary from validator tooling. |
| [ADR-0044](<../adr/ADR-0044-owner-self-release-for-admitted-public-water-data.md>) | `accepted` | Retain accepted: water self-release applies only when every bundle is public and has a listed admitted-source license. |
| [ADR-0045](<../adr/ADR-0045-owner-self-release-for-admitted-public-weather-data.md>) | `accepted` | Retain accepted: weather self-release is scoped to the GHCN-Daily profile/license list, not a global one-person release rule. |
| [ADR-0046](<../adr/ADR-0046-owner-self-release-for-admitted-public-soil-data.md>) | `accepted` | Retain accepted: soil self-release is scoped to the USCRN daily soil profile/license list. |
| [ADR-0047](<../adr/ADR-0047-owner-self-release-for-admitted-public-storm-events-data.md>) | `accepted` | Retain accepted: storm-event self-release is scoped to its NOAA profile/license list. |
| [ADR-0048](<../adr/ADR-0048-external-mirror-names-are-externally-fixed.md>) | `accepted` | Retain accepted: externally fixed names require upstream-backed receipt entries; repository-only overlays are not blanket exemptions. |
| [ADR-0049](<../adr/ADR-0049-owner-self-release-for-admitted-public-earthquake-data.md>) | `accepted` | Retain accepted: earthquake self-release is scoped to the USGS ComCat profile/license list. |

New [ADR-0050](../adr/ADR-0050-bounded-site-subsurface-three-scenes.md) remains
`proposed`. No record is marked superseded, rejected or accepted by this review.

## Unassigned-candidate disposition

Inbound counts below are bounded literal-filename references in repository
content at the review base, excluding the candidate itself. They are navigation
evidence, not acceptance evidence or an exhaustive semantic dependency graph.
All candidates contain substantive planning material; none is an empty duplicate
that can be removed safely merely because it lacks a number.

| Candidate | Other files referencing its filename | Disposition |
|---|---:|---|
| [ADR-NNNN-connectors-domain-segment.md](../adr/ADR-NNNN-connectors-domain-segment.md) | 2 | Retain unassigned. Connector domain segmentation is a placement/migration question, not an empty numbered ADR. |
| [ADR-XXXX-atmosphere-advisory-non-life-safety.md](../adr/ADR-XXXX-atmosphere-advisory-non-life-safety.md) | 2 | Retain unassigned. Advisory referral/non-life-safety boundary is distinct from vocabulary and schema routing. |
| [ADR-XXXX-atmosphere-knowledge-character-vocabulary.md](../adr/ADR-XXXX-atmosphere-knowledge-character-vocabulary.md) | 2 | Retain unassigned. Domain claim-character vocabulary needs its own source/schema review. |
| [ADR-XXXX-atmosphere-schema-home.md](../adr/ADR-XXXX-atmosphere-schema-home.md) | 2 | Retain unassigned. Domain routing/migration is not accepted by generic root placement. |
| [ADR-archaeology-exact-location-policy.md](../adr/ADR-archaeology-exact-location-policy.md) | 9 | Retain unassigned. Exact/reconstructive location protection is not duplicate source-role semantics. |
| [ADR-archaeology-source-roles.md](../adr/ADR-archaeology-source-roles.md) | 5 | Retain unassigned. Shared source-role crosswalk is distinct from disclosure policy. |
| [ADR-focus-model-adapter-boundary.md](../adr/ADR-focus-model-adapter-boundary.md) | 6 | Retain unassigned. Compare with ADR-0008/0019 before assignment; Focus-specific orchestration and evidence obligations remain substantive. |
| [ADR-habitat-fauna-thin-slice.md](../adr/ADR-habitat-fauna-thin-slice.md) | 6 | Retain unassigned. Cross-domain proof harness is distinct from either domain model or publication approval. |
| [ADR-habitat-modeled-vs-critical.md](../adr/ADR-habitat-modeled-vs-critical.md) | 3 | Retain unassigned. Modeled habitat and regulatory designation must not be conflated. |
| [ADR-habitat-schema-home.md](../adr/ADR-habitat-schema-home.md) | 2 | Restore index entry now. Metadata says unassigned-scaffold; loss of a magic prose phrase hid this substantive schema-home conflict. |
| [ADR-habitat-source-roles.md](../adr/ADR-habitat-source-roles.md) | 4 | Retain unassigned. Domain source-role meanings remain separate from modeled/regulatory product classes. |
| [ADR-habitat-stewardship-zone-policy.md](../adr/ADR-habitat-stewardship-zone-policy.md) | 3 | Retain unassigned. Stewardship, sensitivity and public geometry exposure require their own review. |

## Deletion, supersession and new decisions

No deletion is warranted in this packet. Keep accepted decision history and the
referenced unassigned proposals. The retired app does not make the earlier
composition decision history disposable. Existing proposals can be rewritten
without pretending they were accepted; material changes to accepted choices
need an explicitly accepted successor or exception.

The only new decision proposed here is the bounded Three.js exception. Broad
Site/API conformity, one global policy migration or bulk acceptance of the
backlog would combine unrelated authority questions and has not been inferred
from this documentation request.

## Validation

- ADR index validator: **PASS**, 50 numbered records and 12 unassigned drafts.
- ADR negative-path tests: **15 passed**; five new regressions failed on the
  unmodified validator before the fix.
- Existing subsurface slice, cutaway rendering and aquifer volume tests: **35
  passed**. These are local implementation tests, not independent browser proof.
- MapLibre acquisition inventory: **HOLD**, exit 3, reason
  `RENDERER_ACQUISITION_PRESENT`; zero boundary findings. This is a finite
  acquisition/governance hold, not a green dependency-admission result.
- Repository QA, ADR and adjacent program-baseline tests: **384 passed**,
  45 subtests passed.
- Gap/scaffold checks: **PASS**, zero broken local links or new findings.
- Topology: **PASS**, zero new drift; 89 existing baseline warnings.
- Changed Markdown: unique metadata, one H1, closed fences/comments, resolved
  local links and anchors; **PASS**.
- Packet integrity: [generated receipt](../../data/receipts/generated/genrec-adr-review-20261119.json);
  exact artifact bytes are bound separately from pending human acceptance.
- Hosted CI, device/GPU/browser behavior, dependency admission, source/data
  admission, release, deployment and publication: not established by this review.

## Review and rollback

The repository owner receives the review packet and proposed decision. Acceptance
of ADR-0005 or ADR-0050 requires a recorded decision with affected reviewers;
merging Markdown does not supply that decision. Revert the documentation,
validator/tests as one packet with a correction receipt if the review is wrong.
Preserve the earlier ADR blobs and generated receipt records. No runtime, source,
storage or operational migration is executed.
