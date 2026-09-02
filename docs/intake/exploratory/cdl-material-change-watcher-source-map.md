<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/cdl-material-change-watcher-source-map
title: CDL Material-Change Watcher - Governed Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; repository-grounded
owners: OWNER_TBD - Agriculture source steward; tooling QA; intake steward
created: 2026-08-02
updated: 2026-08-02
policy_label: public; intake; exploratory; fixture-only; no-network; no-publication
owning_root: docs/
responsibility: Preserve reviewable identities and a bounded disposition map from two supplied architecture documents to the fixture-only CDL material-change comparator without promoting live source, policy, schema, receipt, lifecycle, release, or publication claims into authority.
source_evidence:
  - captured_filename: KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md
    sha256: 57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780
    byte_count: 554630
    line_count: 4049
  - captured_filename: Unified Implementation Architecture Build Manual.md
    sha256: e92500f9b40007e8b69d183ecaa6247c542ffec25857875ecd2dbd00709785b1
    byte_count: 84595
    line_count: 1769
repository_evidence:
  repository: bartytime4life/Kansas-Frontier-Matrix
  remote_main_snapshot: 658bd477e769646cd70131ca824af0780b6812b4
  remote_state_verified_at: 2026-08-02
  open_pull_requests_at_verification: 0
related:
  - ./README.md
  - ../README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../sources/catalog/usda/usda-nass-cdl.md
  - ../../../tools/ingest/README.md
  - ../../../tools/ingest/cdl_watch/README.md
  - ../../../tests/ingest/README.md
  - ../../../tests/ingest/cdl_watch/README.md
  - ../../../.github/workflows/domain-agriculture.yml
tags: [kfm, intake, agriculture, cdl, watcher, material-change, source-map, fixture-only, no-network]
notes:
  - "The supplied documents are not committed by this change; filenames, digests, sizes, and line counts preserve their identities."
  - "The implementation adapts comparison mechanics only. It does not adopt the documents' proposed SourceIntakeRecord, signed-receipt, live-source, or policy authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# CDL material-change watcher — governed source map

> **Outcome:** Two supplied architecture documents are retained as exploratory
> design evidence for a fixture-first source-drift comparator. Current
> repository evidence supports only a bounded synthetic helper that produces
> review signals and cannot publish.

> [!IMPORTANT]
> The documents prove that these ideas were proposed. They do not prove a live
> CDL endpoint, rights, source admission, cadence, classmap authority, county
> geometry authority, canonical materiality policy, receipt closure, or release
> safety.

## Source identities

| Supplied document | SHA-256 | Size |
|---|---|---:|
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | `57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780` | 554,630 bytes; 4,049 lines |
| `Unified Implementation Architecture Build Manual.md` | `e92500f9b40007e8b69d183ecaa6247c542ffec25857875ecd2dbd00709785b1` | 84,595 bytes; 1,769 lines |

The repository comparison used
`main@658bd477e769646cd70131ca824af0780b6812b4` with zero open pull
requests at the verification point.

## Source map and disposition

| Source location | Design pressure | Disposition in this slice |
|---|---|---|
| Pass 20 Part II `KFM-IDX-SRC-006`, `KFM-IDX-VAL-001`, `KFM-IDX-VAL-003`, `KFM-IDX-VAL-005`, and `KFM-IDX-ANA-003` | Watchers emit source-drift candidates only; material-change gates, negative fixtures, and no-network dry runs make change reviewable. | **ADAPT** into a local synthetic comparator, closed fixtures, and deterministic tests. |
| Pass 20 Part II `EXP-001` | A fixture-first CDL/PLANTS watcher should distinguish changed and unchanged inputs. | **PARTIAL ADAPT** of comparison mechanics only; `SourceIntakeRecord`, signed receipts, outbox, and live-source dependencies remain deferred. |
| Build Manual §§8.3-8.4 | Watchers may compare metadata and material metrics but must not publish; sidecars preserve change inputs. | **ADAPT** into finite review outcomes and an immutable non-publication decision. |
| Build Manual §10.7 | Agriculture and landcover public posture is county/generalized first; watchers propose work only. | **ADAPT** using a non-real county sentinel and no field, parcel, owner, or person geometry. |

## Repository-grounded implementation

The selected homes follow adopted directory governance:

| Responsibility | Existing home |
|---|---|
| Deterministic watcher helper | `tools/ingest/cdl_watch/` |
| Synthetic proof corpus | `tests/ingest/cdl_watch/fixtures/` |
| Executable behavior proof | `tests/ingest/cdl_watch/` |
| Read-only orchestration | `.github/workflows/domain-agriculture.yml` |
| Product doctrine and unresolved live-source questions | `docs/sources/catalog/usda/usda-nass-cdl.md` |

The frozen `kfm-cdl-watch-fixture-v1` profile uses only local files, the
non-real county sentinel `99999`, integer square metres, integer parts per
million, and a fixture-only source reference. Metadata and CDL-year drift stay
diagnostic unless a histogram threshold is reached. The proof covers
inclusive relative and absolute thresholds, below-threshold behavior, year or
timestamp regression, chronology consistency, positive covered area, canonical
class IDs, classmap drift, geometry/denominator drift, malformed input,
deterministic diagnostics, repository-output denial, and active network denial.

The profile's `profile_hash` is deliberately local. It is not a generic JCS or
RFC 8785 implementation and does not establish KFM-wide `spec_hash` policy.

## Deferred authority and remaining work

The following remain **PROPOSED / NEEDS VERIFICATION**:

- a live CDL `SourceDescriptor`, endpoint, rights and attribution decision;
- operational polling cadence, source admission, connector, and pipeline;
- canonical classmap and county-geometry registries;
- steward-approved materiality thresholds and their policy home;
- a canonical cross-watcher report or `SourceIntakeRecord` contract;
- receipt, EvidenceBundle, policy, promotion, release, correction, and rollback
  closure for any real source change.

No source was accessed or activated, and no lifecycle, receipt, proof, catalog,
release, or publication artifact was produced by the watcher.

## Rollback

Rollback is a normal revert of the bounded feature commit. It removes the
helper, synthetic fixtures, tests, workflow wiring, source-map reconciliation,
and generated implementation receipt without changing live source, lifecycle,
release, or published state.

[Back to top](#top)
