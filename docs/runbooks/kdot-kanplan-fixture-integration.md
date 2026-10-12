<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/kdot-kanplan-fixture-integration
title: KDOT KanPlan private-fixture integration
type: runbook
version: v0.1.0
status: draft; fixture-only; no-source-admission
owners: ["@bartytime4life"]
created: 2026-09-05
updated: 2026-09-05
owning_root: docs/
policy_label: public
truth_posture: CONFIRMED bounded implementation; PROPOSED integration; NEEDS VERIFICATION graduation
[/KFM_META_BLOCK_V2] -->

# KDOT KanPlan private-fixture integration

This is an executable, no-network candidate slice, not a live KDOT importer,
operational EvidenceBundle resolver, released transportation dataset, or site update.
It adapts the supplied `KFM_KDOT_KANPLAN_Implementation_Handoff_2026-09-05.zip`
(SHA-256 `fee77473620355df891046bea0911eb8baf1c9698d682520e7556f1263b349d2`).

Inspection base: `main@702e97d824d7305698cd66bc1f9a57edc4063440`.
Delivery re-pin: `main@747e5dba9ffba6ca80074d53171f158b4911ea34`.
The intervening #4296 merge changed only the Explorer package lockfile; the
source, geometry, pipeline, tests and governing files used here were unchanged.
Re-pin current main and delivery controls before integration. Branch review is
not source admission, merge, release, deployment, or publication authority.

## What runs

The named synthetic State System-shaped fixture passes through bounded metadata,
count, ID, and chunk reconciliation; preserved response bytes; strict polyline
conversion; native Z/M and route-measure retention; versioned analytical/display
candidates; EvidenceRef/EvidenceBundle-shaped fixture objects; and a reproducible
analytical report. This shape reuse does not establish full native schema or
semantic validation. No canonical registry, catalog, proof, release, or published
store is written. These candidate maps and reports are not KDOT evidence.

The HTTP placeholder always returns `LIVE_SOURCE_NOT_ACTIVATED`. No constant,
environment variable, CLI flag, background schedule, token, or public URL proxy
can activate it. Importing the modules performs no network or file writes.

## Owning roots and bounded placement/migration note

The placement basis is adopted [Directory Rules](../doctrine/directory-rules.md),
[ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md), and the
inspected responsibility-root READMEs, not the handoff's temporary file layout.

| Artifact | Responsibility and placement basis |
|---|---|
| `connectors/kansas/kanplan.py` | Source-specific capture under the existing Kansas family, `DIR-EXEC-002`. This dormant module does not select a final canonical KDOT child directory or source identity. Final client packaging remains PROPOSED; review or relocate this one module before activation. |
| `packages/geo/src/geo/esri_polyline.py` | Reusable geometry implementation, `DIR-EXEC-001` and `DIR-DEP-001`. It has its own finite geometry errors and does not import connectors, pipelines, apps, or tools. |
| `packages/geo/pyproject.toml` | Declares only the optional `pyproj==3.7.2` transform dependency and Python baseline. It does not establish built/installed/distributed package maturity. |
| `pipelines/normalize/roads-rail-trade/kanplan_state_system.py` | Stage-first normalization and private-fixture candidate composition, adopted `DIR-EXEC-004`. No real lifecycle or release transitions. |
| `fixtures/synthetic/kanplan/` | Reusable authored synthetic inputs, not real captures or registry records. |
| `tests/pipelines/kanplan/` | Changed-area conformance and integration tests; network denial is scoped to this directory. |
| This runbook and leaf READMEs | Behavior-linked documentation and a bounded migration note; no independent doctrine or schema home. |

The older `pipelines/normalize/README.md` describes domain-first placement unless
an ADR or migration note says otherwise. Adopted v2 instead requires stage-first
implementation. This note applies that later rule to this new dormant slice.
The old `pipelines/domains/roads-rail-trade/ingest_kdot_kanplan_kandrive.py`
placeholder remains inert and unchanged; it is not a second working normalizer.
`connectors/kdot/` remains compatibility-only and receives no substantive code.
No Kansas/KDOT child directory, schema, policy, source registry, or release home
is created. Later relocation must remove this module's writers and update imports,
tests, and documentation together; do not leave parallel implementations.

Parent READMEs containing older evidence snapshots are retained as history.
These leaf docs describe only the new behavior, without rewriting unrelated
inventory, governance, or commissioning claims.

## Run locally from the repository root

Use a reviewed Python environment with the repository's test dependencies and
the optional geo transform dependency available. PROJ grid networking stays off.
No dependency installation or network source acquisition is performed by these
commands. The output directory must be new and outside the repository.

```sh
PROJ_NETWORK=OFF python -m pytest tests/pipelines/kanplan -q
PROJ_NETWORK=OFF python -m pipelines.normalize.roads-rail-trade.kanplan_state_system \
  --fixture-output /tmp/kfm-kanplan-private-fixture
```

The CLI validates first, refuses abbreviated options, refuses in-repository or
existing output locations, and creates a private-mode directory. It does not
start a server. Never serve this directory or copy it into the existing Sites
project: it includes synthetic RAW-like and analytical evaluation material.

The six JSON/GeoJSON outputs and eight synthetic response files are reproducible
in the same transform environment. Raw-byte hashes, normalized content hashes,
retrieval receipts, dataset versions, and evidence identities stay distinct.
Evidence identities bind both the capture receipt and derived dataset version.
Mutable capture objects are rechecked against preserved response bytes before
compilation. Hashes establish consistency, not authenticity, rights or approval.

## Source and claim boundaries

Discovery target only:
`https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation/State_System/FeatureServer/0`.
Metadata locator: append `?f=pjson` to that layer URL. The allowlist also records
the earlier seven layer discovery targets, not admitted source records.

Consult [KDOT website terms](https://www.ksdot.gov/about/publications-and-reports/kdot-website-terms-of-use)
and [existing KDOT source guidance](../sources/catalog/kansas/kdot.md).
No product-specific permission is asserted here. Capture, transformation, caching,
display, export, redistribution and AI retrieval require separately recorded
permission and admission decisions before real use. No permission email is sent.

State System is not every Kansas road. Its graphics are not interchangeable with
KDOT adjusted traveled mileage. Reports count analytical source records, not map
or tile fragments. Their lengths are whole intersecting feature lengths on the
WGS84 ellipsoid, not clipped county mileage, calibrated measures, or legal access.
Observation years and historical intervals remain unknown; retrieval time does
not fill them. Native measures are not altitude. Curves and unsupported or
conflicting CRSs fail closed rather than being silently flattened or relabeled.

The AADT validation helper is a deferred-slice test seam only: it does not ingest
traffic, invent missing count years, sum segment counts, or represent live speed.
No rail, county, historical, bridge, culvert, traveler-information, terrain,
operational-routing, emergency, or AI feature is enabled.

## Validation and graduation

The authoring run executed 119 fixture tests in an isolated, repository-shaped
source export using the exact root pytest configuration. Python compilation and
deterministic replay are separate recorded checks. This is not a full checkout
or hosted CI result. Available pytest 9.0.2 was below the repository's declared
>=9.1.1 test baseline; rerun in the supported environment before integration.
PROJ/pyproj version and grid differences can change transformed output identity.

Still NEEDS VERIFICATION: full repository topology/native validators; exact-head
hosted checks; approved source descriptor and capture admission; product rights,
originator and field profile; native CRS/datum accuracy; a separately reviewed
release; actual Sites project/version inspection; real MapLibre browser loading,
selection, keyboard/mobile interaction, evidence resolution and report export.
The existing renderer seam, Explorer source, UI dependencies and hosting are
unchanged. Mapping and AI are not claimed operational by this fixture result.

## Rollback and next dependency

Leave the feature branch unintegrated to roll back this draft work. After a
separately authorized merge, revert the complete slice and rerun changed-area
checks. No live-source, site, runtime, network, source-registry or release rollback
is needed for this slice. Private evaluation output may be retained or removed
by its owner; it has never been a KFM release.

Next: review placement and dependency choices, rerun native validation, and obtain
operation-specific State System permission. Only then qualify a bounded real
capture. Actual source activation, release and in-place Sites editing remain
separate decisions; rollback must never restore withdrawn or rights-revoked data.
