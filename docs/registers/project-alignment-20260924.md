<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/registers/project-alignment-20260924
title: KFM cross-location project alignment
type: reconciliation-register
status: draft; branch-only; bounded-validation; non-authoritative
updated: 2026-09-24
owning_root: docs/
responsibility: Reconcile implementation, current coordination pointers, duplicate documentation, validation scope, and open verification without creating release authority.
[/KFM_META_BLOCK_V2] -->

# KFM project alignment

This register records the extensive alignment against repository base
`bb08d3e9b92e9251c193debab6567be843136070` and owner-private Site version **70**.
Repository changes remain on `codex/project-alignment-20260924`. Main integration,
source admission, release, and production acceptance are separate decisions.

## Where to maintain each fact

| Responsibility | Primary location | Other locations |
|---|---|---|
| Executable behavior, contracts, schemas, tests | [Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) at an exact commit | Site and coordination summaries link to source; they do not override it |
| Repository orientation | [README](../../README.md), [system map](../architecture/SYSTEM_MAP.md) | Google Drive master reference summarizes and points here |
| Hosted Site source and deployment | [Site alignment record](../../apps/kansas-frontier-matrix-explorer/docs/sites-source-alignment.md) | Site is separately versioned; matching project ID does not mean matching implementation |
| Project coordination and current checkpoint | [Notion alignment register](https://app.notion.com/p/3c5a92021bf681b5982ee75dc4376b4e) | Project hub, Workbench, roadmap, and backfill link to this checkpoint |
| Drive synthesis | [Master reference](https://docs.google.com/document/d/1H3unk1ks0RM8zy28uoWpCoAjwg_CYjetFbB02GJMyUk) | Roadmap, Living Atlas design, charter and chronicle retain their distinct roles |
| Telemetry profile meaning | [Telemetry contracts](../../contracts/telemetry/README.md) | [Validators](../../tools/validators/telemetry/README.md) own executable invocation; [stack specification](../dashboards/observability/OPENTELEMETRY_STACK.md) remains proposed |
| Historical design and source lineage | Existing dated documents, PDFs, receipts, snapshots | Preserve dates and caveats; never silently turn them into current acceptance |

Update the current section in place. Do not stack another competing “latest”
summary above old ones. Keep unique dated evidence in historical sections and
link to it when useful. This register is explanatory, not a new machine registry.

## Functionality matched to inspected files

| Claim | Source evidence | Correct boundary |
|---|---|---|
| Living Atlas map | `apps/explorer-web/src/site/mount-living-atlas.ts`; `packages/maplibre/src/maplibre-vite-adapter.ts`; package manifest | Bounded inline MapLibre 6.9.0 composition exists. Browser acceptance and admitted layers remain separate. The laboratory uses NullMapRuntime. |
| Repository Sites application | `apps/kansas-frontier-matrix-explorer/main.tsx`, `vite.config.ts`, `worker/index.ts`, `.openai/hosting.json` | Vite/React routes `/` and `/about`; NullMapRuntime; `/api` returns 503 `KFM_API_NOT_CONFIGURED`; D1/R2 unbound in this source. |
| Hosted Explorer | Standalone source `c402b063c60dc7ec8f23a497715d01cff6f7ffa5`; Site version 70 | Vinext/React and separately configured storage bindings. Local build/tests and successful private deployment are confirmed. No tree equivalence with the monorepo is claimed. |
| Live repository status | Standalone `app/api/repository-status/route.ts`, `app/repository-status.ts`, `app/page.tsx` | Read-only fixed GitHub metadata; bounded body; no-store HTTP responses; observation expires after 60 seconds and then requires refresh. A differing hash does not prove ancestry. |
| Local KML/GeoJSON import | Both applications' `app/import-preview.ts` | Unadmitted browser preview; actual UTF-8 size limit, bounded KML depth/elements, balanced extraction, no external entity or network execution. |
| Telemetry | Four schemas under `schemas/contracts/v1/telemetry/`, local validators and `.github/workflows/telemetry-policy.yml` | Fixture-only trace linkage, OpenLineage, remote-sensing lineage and sustainability validation. No operational emitter, redactor, collector, sink, retention or dashboard acceptance. |
| General telemetry safety | `tools/validators/validate_telemetry_safety.py`; raw/prompt Rego modules | Explicit placeholders remain held. They are not disclosure-prevention controls. |
| Governed API | `apps/governed-api/src/governed_api/main.py`, `stub.py`, `routes/registry.py` | Loopback negative-envelope scaffold with fixed routes; no authenticated production data service established. |
| Model and service deployment | `runtime/model_adapters/OllamaAdapter.py`; `infra/docker/` Dockerfiles | Placeholder adapter and payload-free images; naming and configuration examples do not prove a running service. |
| External map context / Earth Engine | Standalone Site preservation record and adapters | Display context or disconnected discovery/recipes. No KFM EvidenceBundle, source admission, warning authority or executed Earth Engine pipeline inferred. |

## Corrections and local validation

- Telemetry candidates outside the canonical JSON domain now return a bounded
  error without exception chains or candidate values. Empty/malformed lineage
  fixture inventories cannot succeed. Trace-link input checks apply to the
  actual bounded regular-file descriptor and reject observable replacement.
- Malformed KML extraction is bounded in both applications. Valid namespaced
  geometry and ExtendedData remain covered by regression tests.
- Site identity and catalog counts derive from the correct current source;
  old repository observations become visibly stale. Historical cards remain dated.
- Explorer Web's catalog reflects its 6.9.0 adapter composition while retaining
  the independent readiness/acceptance hold.

Observed local validation for the final changed code:

| Check | Result |
|---|---|
| Telemetry directory unit tests | 66 passed |
| TraceReceiptLink unit tests | 14 passed |
| Explorer Web unit tests | 648 passed across 65 files |
| Explorer Web build/typecheck | Passed; large-bundle advisory remains |
| Repository Sites app build/typecheck/tests | 288 passed, 2 existing skips; 5 lint-compatibility tests passed |
| Standalone Site build/typecheck/tests | 147 passed |
| Documentation local links | 25 changed documents; 347 local targets resolve; external URLs not network-tested by the checker |
| Site platform deployment | Version 70 succeeded; owner-private access preserved |

These are local changed-area results, not a claim that every repository test,
hosted workflow, browser interaction, source endpoint, or production service was
verified. Root aggregate scripts intentionally retain `WORKFLOW_HOLD`.

Codex Security performed partial source review and architecture mapping. Its
formal report could not be saved/sealed because the host's registered report
storage ancestors failed ownership/permission validation. The guard was not
weakened. There is no completed security scan or clean-scan claim; review notes
were retained privately. The input fixes have local regressions, not independent
security acceptance.

## Deduplication and migration

The initial inventory covered **4,951 tracked Markdown files** and found 13
byte-identical groups above 200 bytes, plus document-ID collisions and a
line-ending-only duplicate. Twelve duplicate bodies were consolidated using
full normalized-text equality, without removing unique authored content.
Their existing paths now retain compatibility pointers and legacy fragments.
The retained body keeps its original identity; each pointer has a distinct
identity and records its alias relationship.

| Compatibility path | Retained body |
|---|---|
| `docs/domains/flora/OBJECT_FAMILIES.md` | `docs/domains/flora/MISSING_OR_PLANNED_FILES.md` |
| `docs/domains/flora/RELEASE_INDEX.md` | `docs/domains/flora/README.md` |
| `docs/domains/flora/modalities/M3-VOUCHER.md` | `docs/domains/flora/modalities/README.md` |
| `docs/domains/geology/CONTINUITY_INVENTORY.md` | `docs/domains/geology/CANONICAL_PATHS.md` |
| `docs/domains/geology/SENSITIVITY_POSTURE.md` | `docs/domains/geology/SENSITIVITY.md` |
| `docs/domains/habitat/SOURCES.md` | `docs/domains/habitat/SENSITIVITY_POLICY.md` |
| `docs/domains/people-dna-land/SENSITIVITY.md` | `docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md` |
| `docs/domains/soil/DATA_LIFECYCLE.md` | `docs/domains/soil/CONTINUITY_INVENTORY.md` |
| `docs/sources/catalog/ahgp/family-trees.md` | `docs/sources/catalog/ahgp/county-town-histories.md` |
| `docs/sources/catalog/blm/glo-land-patents.md` | `docs/sources/catalog/blm/glo-field-notes.md` |
| `docs/sources/catalog/nrcs/conservation-practice-records.md` | `docs/sources/catalog/nrcs/README.md` |
| `docs/sources/catalog/usfws_ecos/critical-habitat.md` | `docs/sources/catalog/usfws_ecos/README.md` |

The OTel lowercase document is also a compatibility pointer. Its unique signal
thresholds and public-rollup question were retained in section 17 of
`OPENTELEMETRY_STACK.md`; thresholds remain proposed and require review.

**Directory Rules basis:** existing `docs/` owns human-readable explanations and
registers. Accepted ADR-0029 and `docs/registers/README.md` permit drift and
migration records in this lane. No new root, machine registry, policy authority,
schema family, or lifecycle location is created. Existing application code,
validator code, tests, and contract documentation stay in their responsibility
roots. Review remains required before repository integration.

## Deliberate preservation and open verification

- Frozen doctrine, source PDFs, synced project `sources/`, historical receipts,
  baselines, and prior local edits were not rewritten. Identical names alone are
  insufficient evidence to delete Drive PDFs or snapshots.
- The exact `trust-membrane.md` / `truth-posture.md` doctrine duplication and
  Sherman/Stevens foreign county plan remain held evidence. The existing Sherman
  README explicitly records the identity conflict; no county facts were invented.
- Non-identical competing archaeology contracts, geology sublanes/lifecycle,
  trade-route drafts, BLM/NOAA/NRCS profiles, and canonicalization case variants
  retain unique material. They require field-level reconciliation and applicable
  owner/ADR decisions. `STD-DRIFT-001` remains held. Fixture duplicate identities
  and unassigned placeholder IDs were not relabeled as production documents.
- Issue [#4024](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024)
  was open at readback. This branch was not submitted as a PR or merged. No
  ruleset, source admission, frozen-catalog correction, promotion, or KFM release
  was performed. Private Site deployment is explicitly recorded separately.
- Hosted exact-branch CI, authenticated browser/WebGL, end-to-end live feeds,
  Qwen connectivity, independent review, operational telemetry and restoration
  rehearsal remain unverified by this alignment.

Rollback: revert each bounded branch commit together with its associated docs
and tests; the earlier source remains in Git. Restore prior Site v69 or protected
v68 only through a separately checked deployment. Native Notion/Docs histories
retain earlier content; revert targeted edits without replacing whole documents.
