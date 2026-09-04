<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-atmosphere-readme
title: "configs/domains/atmosphere/ — Governed Atmosphere Configuration Boundary"
type: readme
version: v0.4
status: draft; repository-grounded; documentation-only; non-authoritative; non-publisher
owners: ["@bartytime4life — CODEOWNERS review route only"]
stewardship: "NEEDS VERIFICATION — configuration, Atmosphere, scientific-method, rights, policy, and release responsibilities are not assigned by review routing"
created: 2026-07-13
updated: 2026-09-04
policy_label: "public; non-secret; non-authoritative; no-live-binding; source-role-preserving; time-aware; non-alert; not-for-life-safety; no-release-authority"
current_path: configs/domains/atmosphere/README.md
owning_root: configs/
responsibility: "Explain safe Atmosphere configuration authoring, explicit consumer binding, compatibility, validation, and rollback without creating domain or publication authority"
truth_posture: "CONFIRMED pinned directory contents, adopted placement, review routing, selected schema bytes, and validator source / PROPOSED future configuration design / UNKNOWN loader, operational enforcement, source admission, and release use / NEEDS VERIFICATION for broader implementation and independent review"
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  ref: main
  commit: 700570cbcf191038aa20a030174c2dd08cf93675
  tree: f98d5965812e9a29f55d820f9942549719930408
  initial_inspection_commit: bb3eb695e6068b38453ca3ded8f1394a8fdebc20
  prior_target_blob: 6379c8123a278723f89b3bb3913f0371eff95f8b
  tracked_config_files: [configs/domains/atmosphere/README.md]
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
related:
  - ../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/atmosphere/README.md
  - ../../../tools/validators/domains/atmosphere/README.md
notes:
  - "This is a dated evidence snapshot, not a moving claim about main. Re-pin before acting."
  - "Re-pin comparison changed only catalog/triplet/README.md; the target and inspected dependencies were unchanged from the initial inspection."
  - "v0.4 replaces July-wide scaffold assertions with bounded evidence and consolidates repeated safeguards while retaining the existing H2 navigation."
  - "README-only configuration does not imply an unimplemented Atmosphere domain; schema and validator maturity must be assessed individually."
  - "Only this README changes. No payload, source, schema, policy, validator, runtime, release, or scheduler is changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Atmosphere Domain Configuration

`configs/domains/atmosphere/`

> Configure a named consumer without redefining what the evidence means.
> This lane is for safe, non-secret configuration support—not observations,
> source admission, scientific interpretation, policy, alerts, or release decisions.

**Status:** draft `v0.4` · **Tracked lane:** README-only · **Implementation outside this lane:** mixed · **Review route:** `@bartytime4life`; stewardship and independent review remain unverified.

**Start here:** [Status](#status) · [Allowed content](#what-belongs-here) · [Validation](#validation) · [Compatibility](#adrs-and-drift-triggers) · [Consumer binding](#consumer-binding-precedence-and-discovery) · [First payload](#definition-of-done-for-the-first-payload) · [Evidence](#evidence-ledger)

> [!CAUTION]
> KFM Atmosphere is not an emergency-alert, clinical, public-health,
> occupational-safety, aviation-safety, fire-behavior, or life-safety system.
> AQI is not concentration; AOD and smoke context are not observed surface PM2.5;
> model and forecast products are not observations. Refer advisory users to the
> official issuing authority. The Hazards lane owns the related KFM context,
> not the official authority itself. [ATM] [PDF]

## Purpose

Help contributors place, review, and eventually bind small Atmosphere configuration
files without creating a second domain authority. A configuration may select an
accepted profile for a verified consumer; it cannot establish station identity,
measurement validity, source rights, evidence closure, or publication permission.

The audience is configuration maintainers, consumer owners, Atmosphere and
scientific-method reviewers, rights/sensitivity reviewers, and policy/release
reviewers. This README explains the boundary; executable behavior belongs to its
owning implementation root. [PARENT] [DIR]

## Authority level

**Owning root: `configs/`.** Accepted [ADR-0029] adopts [Directory Rules][DIR],
whose §7.2 assigns non-secret defaults, profiles, templates, and examples to this
root. This existing same-path README update creates no directory or authority
home and requires no new placement decision.

| Responsibility | Configuration relationship |
| --- | --- |
| Domain meaning and semantic contracts | Reference the owning documentation/contracts; do not redefine them. |
| Machine shape and admissibility | Reference schemas and policy; a config file is neither authority. |
| Source and station identity | Use governed identifiers and approved crosswalks; do not admit sources or merge stations. |
| Evidence, review, release, correction | Preserve references and decisions; do not manufacture or approve them. |
| Consumer behavior | Support only an explicit, validated binding with documented precedence. |

The invariant remains:

```text
RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED
EvidenceRef -> EvidenceBundle
Public consumers -> governed APIs or released public-safe artifacts
```

Promotion is a governed transition, not a file move, successful parse, commit,
layer toggle, or model response. Public consumers must not read internal,
unreleased, RAW, WORK, QUARANTINE, or direct model stores. Receipts record executions, proofs support closure, and
review and release decisions remain separate. [DIR] [ATM]

## Status

**Evidence snapshot:** `main@700570cbcf191038aa20a030174c2dd08cf93675`, inspected
2026-09-04. These statements are limited to the sources in the [evidence ledger](#evidence-ledger).

| Surface | Confirmed evidence | Limit |
| --- | --- | --- |
| This configuration directory | Exact contents listing contains only `README.md`; no child directories. | No tracked config payload here. Ignored, untracked, and external configuration are not inventoried. |
| Parent and domain guidance | Parent config boundary and Atmosphere domain README exist. | Their historical implementation snapshots are not runtime proof. |
| Placement | ADR-0029 is accepted; the adopted Directory Rules blob is unchanged at the evidence pin. | ADR-0001 remains proposed; this README does not ratify it. |
| `air` compatibility | Current domain guidance uses `atmosphere`; the existing `air` pipeline README is a documentation-only compatibility guardrail. | No automatic alias, duplicate executable lane, or retirement is authorized. |
| AirObservation shape | `air_observation.schema.json` contains a bounded `DRAFT_SCHEMA` with properties and constraints; `AirObservation.schema.json` explicitly references it as `MIRROR`. | One inspected pair does not settle every object family's naming or schema maturity. |
| Observed/modeled validator | Inspected source defines a synthetic profile, closed field sets, and forbidden observation/model fields. | Source inspection is not execution, scientific validation, live evidence resolution, or policy evaluation. |
| Other fixture validators | The validator index documents precipitation, knowledge-character, and low-cost-sensor fixture checks. | This update does not claim those implementations or their tests were fully re-audited. |
| Review routing | `/configs/` routes to `@bartytime4life` in CODEOWNERS. | Routing is not stewardship, independent review, approval, or an enforced merge gate. |
| Config loading and public use | No active binding is established by the inspected configuration surface. | Loader, precedence, operational enforcement, deployment, and release use remain UNKNOWN. |

**Correction to v0.3:** README-only configuration must not be described as proof
that all Atmosphere schemas, validators, workflows, or applications are scaffolds.
Conversely, the existence of a bounded validator or schema does not make this
configuration lane active. Broader implementation requires its own exact-source
and execution evidence. [INV] [ATM] [SCHEMA] [MIRROR] [VALIDATOR] [VALIDATOR-INDEX]

## What belongs here

Small, non-secret defaults, placeholder templates, profile references, and
configuration-facing examples for a named consumer may belong here. Synthetic
test overrides must remain isolated from production discovery. A migration note
may describe a real configuration transition, but the migration decision and
implementation remain with their responsible owners. [PARENT] [DIR]

Do not create a file just to reserve a future idea. Identify its consumer,
purpose, owner/review route, format, validation, failure behavior, and rollback.
Unimplemented binding or unsettled authority must be conspicuous. Safe isolated
authoring may proceed as **PROPOSED / TEST_ONLY**; operational activation is a
separate gate, not an implication of committing a template.

## What does not belong here

No credentials, tokens, cookies, private endpoints, workstation bindings,
production data, real sensor payloads, private station siting/access details,
or sensitive facility/network information. References must not disclose secrets
or sensitive geometry indirectly.

Do not put semantic contracts, machine schemas, executable policy, source
registries, station crosswalk authority, evidence/proof instances, lifecycle
payloads, release decisions, or published artifacts in this lane. Do not add
config-local source activation, automatic publication, alert thresholds, hidden
policy bypasses, or a competing `air` authority. [PARENT] [DIR]

## Inputs

A proposed payload needs a named consumer and exact intended load point; a stable
config ID/version; its purpose, parser/format, and allowed keys; accepted
reference targets or explicitly unresolved draft dependencies; non-sensitive
values; deterministic missing/invalid/override behavior; synthetic fixtures;
and a removal or rollback path.

When the consumer handles observations or derived products, its input contract
also needs the applicable source role, knowledge character, station identity,
units/method/quality, spatial support, time/freshness, rights, sensitivity,
provenance, and correction context. Public-bound use additionally requires
admissible evidence, policy, review, integrity, release, and rollback support.
A test-only input must not pretend those operational gates are satisfied.

## Outputs

**Current output: documentation only.** A future validated config may select an
already-governed consumer profile. It does not emit observations, merge station
identities, admit sources, resolve EvidenceBundles, decide policy, create proofs,
issue advisories, or approve release by itself.

Any consumer that writes an artifact must use its declared lifecycle and
accountability interfaces. Neither a config file nor its parser may hide a write
to a source registry, internal store, release record, or public carrier.

## Validation

### README-only review

Check the exact changed path, metadata identity/version/evidence pin, one H1,
unique H2 headings, retained navigation, balanced fences, valid Markdown links,
UTF-8/final newline, whitespace, and conflict-marker absence. Verify repository
links against pinned contents, not invented filesystem paths. Inspect claims
against their sources and retain the non-alert, non-secret, role, sensitivity,
evidence, and release boundaries.

From a real checkout, a reviewer can begin with:

```sh
git diff --check
git diff --name-only
```

These are hygiene/scope checks, not domain or operational tests. Record the exact
base/head, command, result, and limitation. Do not label unrun pytest, schema,
Rego, workflow, browser, or runtime checks as passing; a documentation update
cannot establish their execution.

### Future consumer-bound validation

The following is an acceptance plan, not a new implemented validator or wire enum.
Use the selected contract's actual outcomes and reason codes.

| Check family | Positive and negative coverage |
| --- | --- |
| Parsing and identity | Supported version, stable ID, duplicate/unknown keys, malformed input, unsupported version. |
| Binding and authority | Explicit load point; missing required file, unresolved profile, ambiguous precedence, scaffold-as-enforcement rejection. |
| Meaning | Units/method/averaging and station identity; AQI/concentration, AOD/PM2.5, model/observation, and advisory/alert substitution denial. |
| Time and support | Valid/sample/run intervals, timezone, stale/outage/partial states, wrong spatial or vertical support, missing climate baseline. |
| Rights and sensitivity | Unknown rights, restricted data, private coordinates, unsafe joins, secret-bearing values, and public-path bypass. |
| Correction | Supersession, advisory expiry, withdrawal, invalidation, rollback, and stale cached/AI output. |
| Isolation | Synthetic fixtures, deterministic no-network execution, and no implicit production discovery or writes. |

A passing fixture demonstrates only its tested profile. It is not evidence of
scientific accuracy, source admission, regulatory comparability, production
policy enforcement, public safety, or release readiness. [VALIDATOR] [VALIDATOR-INDEX]

## Review burden

CODEOWNERS supplies the verified GitHub route, not an assignment of scientific,
rights, policy, or release responsibility. Named accountable stewards and
independent review remain **NEEDS VERIFICATION**. [OWNERS]

README-only work needs proportionate configuration/domain review; terminology
or advisory changes also need the relevant source-role or safety-context review.
A behavior-bearing payload needs its consumer owner and applicable method,
station, temporal, rights/sensitivity, schema/policy, and rollback reviewers.
Do not allow a config author to self-certify policy-significant source approval,
release, or rollback. Record any bootstrap review limitation explicitly.

Current contributor controls and [issue #4024][INCIDENT] distinguish branch
writing, independent one-shot draft creation, and observation for an
incident-quarantined delivery path. A README update grants no ready, approval,
merge, settings, scheduler, source-admission, deployment, or release authority.

## Related folders

| Read next | Relationship |
| --- | --- |
| [Parent domain configuration](../README.md) | Shared non-secret, consumer-bound configuration boundary. |
| [Atmosphere domain guide](../../../docs/domains/atmosphere/README.md) | Domain scope, source distinctions, and responsibility-root navigation. |
| [Atmosphere validator index](../../../tools/validators/domains/atmosphere/README.md) | Bounded fixture checks and their limits; not a config loader. |
| [Air compatibility guardrail](../../../pipelines/domains/air/README.md) | Preserve compatibility without creating duplicate executable authority. |
| [Directory Rules](../../../docs/doctrine/directory-rules.md) and [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adopted placement basis. |
| [CODEOWNERS](../../../.github/CODEOWNERS) and [CONTRIBUTING](../../../CONTRIBUTING.md) | Review routing and current contribution/delivery controls. |

The [Atmosphere guide][ATM] is the navigation surface for related contracts,
policy, registry, lifecycle, application, and release lanes. This README does
not duplicate that inventory or imply every referenced lane is operational.

## ADRs and drift triggers

No ADR or migration is enacted here. Preserve accepted Directory Rules and the
existing responsibility split; [ADR-0001] remains proposed, not newly accepted.

| Topic | Current bounded disposition | Action before broader use |
| --- | --- | --- |
| `atmosphere` / `air` | Use the existing Atmosphere config lane; retain documented Air compatibility. | Verify affected consumers and an accepted mapping before aliasing, relocation, or retirement. |
| AirObservation schema pair | CamelCase is an explicit mirror of the lowercase profile. | Follow the declared reference; do not edit the mirror independently or normalize names heuristically. |
| Other object spellings | Not resolved by the one inspected pair. | Inspect each contract/schema and any migration before selecting it. |
| Source-registry layouts | This update does not select or migrate a registry authority. | Resolve the exact accepted descriptor/profile; do not create duplicate activation records. |
| Discovery or precedence | No general behavior is established here. | Implement an explicit consumer contract and tests; architecture-changing behavior needs the appropriate decision. |

Authority-changing placement, canonical vocabularies, precision policy,
scientific profiles, compatibility retirement, and public exposure require the
owning decision process. A draft may record a reversible proposal without
misrepresenting it as adoption or enabling the held behavior. [DIR] [MIRROR]

## Last reviewed

**2026-09-04**, using the immutable repository snapshot recorded above and
read-only Drive/Notion context. Repository evidence, document lineage, and
execution results are separate. Re-pin before a payload, loader, reference
migration, method/profile change, or public-bound use; this date does not certify
operational freshness, source terms, runtime health, or release readiness.

## Scope and bounded context

The supported subject matter remains air-quality observations and AQI reporting,
weather/station observations, smoke/aerosol/AOD context, climate baselines and
anomalies, atmospheric models and forecasts, and official-advisory referral.
This is not a reduction to a PM2.5-only lane. [ATM] [PDF]

The intended dependency order for a future consumer is:

```text
explicit config reference -> named consumer -> accepted governing profiles
-> applicable validation/evidence/policy/review/release checks
-> bounded result or fail-safe outcome
```

This describes a design boundary, not a verified runtime integration.

## Configuration classes

| Class | Boundary |
| --- | --- |
| Documentation or placeholder template | Inert; identify the intended consumer and unresolved dependencies. |
| Synthetic example or test override | Test-only; excluded from production discovery and live retrieval. |
| Accepted profile reference | Select a versioned owning profile; do not copy its authority into config. |
| Operational default | Requires demonstrated binding, validation, allowed overrides, safe failure, and rollback. |
| Compatibility mapping | Only an explicitly reviewed mapping with identity, scope, lifetime, and migration tests. |

No class permits policy-as-config, source admission, evidence truth, scientific
role upgrades, alert issuance, or automatic release.

## Minimum configuration contract

**PROPOSED design checklist, not a committed schema.** Use existing accepted
consumer conventions rather than inventing a second configuration schema home.

| Information | Required explanation |
| --- | --- |
| Identity and intent | Stable config ID/version, authoring status, purpose, consumer, responsible owner/review route. |
| Binding | Exact parser/load point, supported format/version, allowed keys, allowed override sources and keys. |
| Governing references | Exact profile IDs/versions and contract/schema/policy references; unresolved dependencies explicitly held. |
| Applicable domain context | Source role/knowledge character, station/method/unit/QA, time/freshness, spatial/vertical support, model/baseline, advisory referral, rights/sensitivity. |
| Safe failure | Missing file, malformed value, duplicate/unknown key, unsupported profile, conflicting override, stale/outage behavior. |
| Verification and recovery | Synthetic tests, safe observability, correction/invalidation, deactivation, prior known-good state, rollback. |

Mark inapplicable fields with a reason. Do not require a fictional station, live
source activation, or release decision merely to author an isolated test profile;
do require the relevant approvals before operational or public-bound use.

## Consumer binding, precedence, and discovery

No loader or universal precedence rule is established by this directory.
Implement an explicit allowlist or consumer-owned manifest; do not recursively
activate files based on extension, sort order, directory presence, or proximity.
Templates, examples, backups, compatibility copies, and deprecated profiles must
not become production inputs accidentally.

A future binding must state its parser, validation, defaults, permitted overrides,
conflict handling, and missing-file behavior. Environment variables, CLI values,
local files, deployment settings, and remote config must not outrank policy or
release controls implicitly. Reject or hold ambiguous authority; record only safe
identifiers and the provenance of attempted overrides. Rollback must disable or
restore the actual binding, not merely edit prose.

## Atmosphere object-family boundaries

| Families retained from the domain guide | Config may select | Config must not establish |
| --- | --- | --- |
| `AirStation`, `WeatherStation` | Approved identity-reference and public-display profiles. | Station identity, ownership, siting clearance, or current operation. |
| `AirObservation`, `PM25Observation`, `OzoneObservation` | Units, averaging, method/QA and caveat profiles. | Scientific validity, regulatory status, concentration from AQI, or health effects. |
| `WeatherObservation`, `WindField`, `PrecipitationObservation`, `TemperatureObservation` | Time, support, level and measurement profiles. | Model/observation equivalence, crop/flood impacts, or route/fire/aviation safety. |
| `SmokeContext`, `AODRaster` | Explicitly contextual or derived display profiles. | Surface concentration, personal exposure, diagnosis, or evacuation need. |
| `ClimateNormal`, `ClimateAnomaly`, `ForecastContext` | Baseline, model/run/member and validity profiles. | Current observations, deterministic local futures, or guaranteed outcomes. |
| `AdvisoryContext` | Issuer, validity and official-source referral presentation. | Issuance, amendment, cancellation, or protective-action authority. |

These fifteen families come from [ATM]. Listing a family does not prove its
schema, policy evaluator, config consumer, or released product is complete.

## Source role and knowledge character

Preserve distinctions among sensor observation, regulatory/archive record,
public AQI report, low-cost sensor, network/site metadata, remote-sensing
product, model/forecast/reanalysis/fusion product, climate baseline/anomaly,
advisory context, and aggregate/derived output. Rights, sensitivity, review,
fixture status, and release state are separate axes—not interchangeable source
roles or a new config enum. [ATM] [PDF]

Any transformation retains input/output roles, method/version, uncertainty,
evidence references, validation, and review/release lineage. A config cannot
upgrade a role. Unknown or conflicting meaning requires a bounded hold,
abstention, denial, or error under the applicable contract—not a guessed default.

## Station, network, and sensor identity

Preserve source/network and site IDs, operator, instrument/channel and method,
effective dates, relocation and replacement history, calibration/correction
version, coordinate precision/access posture, and approved alias/supersession
lineage where applicable.

Matching names or coordinates do not prove identity; nearby stations are not
interchangeable; relocation or instrument replacement does not automatically
preserve series comparability. Station presence is not current operation.
Aliases belong to an approved identity/crosswalk authority, not an unreviewed
config-local table. Do not expose private access or sensitive infrastructure
because a station point is otherwise available. [ATM] [PDF]

## Measurements, units, methods, averaging, and quality

Keep parameter/quantity identity, raw and canonical units, conversion method and
version, reference conditions where needed, sampling and averaging/accumulation
windows, instrument/method, QA flags, detection/quantitation limits, uncertainty,
correction/calibration, provisional/revised/final state, and vertical level.
Missing, suspect, invalid, and below-detection values require explicit handling.

A profile may select an accepted conversion, not invent its assumptions.
Gust and sustained wind, rate and accumulation, index and concentration, anomaly
and absolute value, and model analysis and sensor observation stay distinct.

Low-cost sensor use must retain correction/training/reference and colocation
lineage, firmware/instrument version, applicable meteorological effects,
uncertainty/confidence, limitations, drift, transferability, and disconnected
state. Fixture checks do not certify calibration accuracy or regulatory
comparability. [ATM] [PDF] [VALIDATOR-INDEX]

## Time, forecast cycle, freshness, and stale state

Preserve observation and sample intervals; advisory issue/effective/expiry times;
model initialization and valid intervals/lead time; retrieval, ingestion,
processing and release times; correction/supersession times; and climate
baseline periods where applicable. Model run and ensemble-member identity are
associated metadata, not substitutes for time.

Use explicit timezone/normalization rules. Do not guess naive timestamps, hide
accumulation windows, replace observation time with retrieval time, or combine
incompatible forecast cycles. Freshness must be product- and use-specific; this
README selects no threshold.

Stale does not necessarily mean false. Preserve last-known time and historical
use, but make delayed, partial, stale, corrected, superseded, expired, or
unavailable status visible. Never fabricate continuity, silently substitute a
model for a missing observation, or present an old forecast/advisory as current.
Recovery and invalidation must preserve lineage. [ATM] [PDF]

## Spatial support, resolution, height, and generalization

Distinguish station/instrument footprint, mobile observation, raster pixel,
model grid, smoke polygon, regional aggregate, atmospheric column, pressure
level, and height-above-ground support. Preserve CRS, extent, resolution,
vertical reference, interpolation/aggregation method, precision, and any
public-safe transformation with its reason and provenance.

A point does not establish county-wide conditions; a grid is not a local sensor;
a county aggregate cannot be silently downscaled to a site; plume intersection
is not exposure. Do not hide resampling or derive exact sensitive locations
through joins. Generalize, redact, quarantine, or deny before public delivery;
UI hiding alone is not a sensitivity control. [ATM] [PDF]

## AQI, concentration, AOD, PM2.5, and smoke boundaries

**AQI is an index/reporting product, not concentration.** Retain pollutant basis,
averaging, issuing/reporting authority, breakpoint/method version, supporting
inputs, valid/issue time, freshness, and caveats.

**AOD or smoke context is not observed surface PM2.5.** Any approved retrieval or
relationship needs method, meteorological/vertical context, model/run identity,
calibration/validation, uncertainty and use limitations; the result retains its
derived role. A config cannot perform an epistemic upgrade.

PM2.5 observations retain units, averaging, station/network identity, method/QA,
correction, time, source role and provisional/final state. Smoke masks, plumes,
hotspots, and modeled transport do not by themselves establish ground exposure,
indoor air, health outcome, fire behavior, regulatory exceedance, or evacuation
need. [ATM] [PDF]

## Models, forecasts, ensembles, and climate products

Keep provider/product and version, run/init cycle, analysis/forecast distinction,
lead/valid interval, grid and vertical level, assimilation/post-processing,
ensemble member/summary/spread, uncertainty, limitations, and superseding run.
Matching a sensor or being interpolated, validated, rendered, or summarized does
not turn modeled output into an observation. [VALIDATOR] [ATM]

Normals require metric, baseline period, aggregation method, station/grid support,
version and completeness/quality. Anomalies require the referenced baseline,
sign convention, period, method and uncertainty. Climate scenarios/projections
are not direct observations or deterministic local forecasts. [PDF]

## Advisory, alert, health, and life-safety boundary

Advisory context must preserve official issuer and identifier, geographic scope,
issue/effective/valid times, expiry/cancellation/supersession, retrieval time,
stale state, and an official-source reference. Make clear that KFM is not the
issuer. Coordinate KFM hazard context without assigning official powers to
Atmosphere, Hazards, configuration, or AI. [ATM]

Do not originate, alter, suppress, or cancel official guidance, infer an alert
from a threshold, or issue medical, exposure, evacuation, shelter, travel,
aviation, occupational, or fire-safety instructions. Health content remains
bounded official-source referral under applicable policy, not individualized
advice. Missing or expired support must not appear as active guidance.

## Cross-domain context and anti-authority

Atmosphere may provide governed weather, climate, smoke, precipitation, or dust
context. It does not thereby establish Agriculture crop/yield claims; Hydrology
flood/gauge truth; Soil properties/moisture; ecological occurrence/habitat;
asset operation/outages; road closure/navigation safety; geological source
attribution; or individual exposure, health, property, and ownership claims.

Cross-domain joins preserve each owner's claim, time, spatial support, role,
rights/sensitivity, evidence, review, and release state. Additional sensitive
inferences can require generalization or denial even when the inputs are
separately public. [ATM] [PDF]

## Source rights, attribution, quotas, and outages

Config may reference a reviewed source profile; it cannot activate a connector
or claim that its source is admitted. Source owners must establish current terms,
attribution, redistribution, retention/caching, access, quotas, cadence,
correction and outage obligations before the relevant use. This update performs
no live source or licensing verification. [PDF]

Keep keys and private endpoints outside committed examples. Quota exhaustion
or outage requires explicit degraded/unavailable state, not invented continuity.
Source replacement needs method, units, time, rights, and authority compatibility
review; similar labels do not prove interchangeability. Unresolved rights or
sensitivity block public exposure, not safe synthetic authoring.

## Logging, telemetry, caches, and derived indexes

Log public-safe IDs/versions, finite results, reason codes, and stale/outage
status—not secrets, private siting, restricted responses, unreviewed payloads,
misleading current-condition claims, or alert-like instructions.

Cache identity must prevent reuse across incompatible profile/source versions,
roles, parameters/units/methods, run/valid intervals, support/resolution/level,
and release/correction states. This is a requirement for a future consumer,
not a claimed implemented cache key.

Corrections, relocations, method changes, model reruns, advisory expiry,
rights changes, or withdrawal may invalidate tiles, layers, API payloads,
caches, search/vector indexes, graphs, reports/exports, dashboards, and AI
summaries/citations. Restore or withdraw dependent outputs through the owning
systems; changing configuration alone is insufficient. [PDF]

## Failure behavior

These are design obligations; exact outcome enums belong to the chosen contract.
Do not conflate work-state `HOLD`, a validation result, and an outward runtime
response.

| Condition | Required safe behavior |
| --- | --- |
| Missing optional file | Use only a documented conservative default; record that no override loaded. |
| Required file missing, malformed or unsupported | Reject or hold; no guessed binding or version. |
| Duplicate/unknown keys, ambiguous refs/precedence | Reject or hold unless the accepted contract defines an explicit safe alternative. |
| Unresolved source/station/units/time/rights | Preserve uncertainty; withhold unsupported interpretation or public use. |
| Role collapse, sensitive exposure, policy/release bypass | Deny or error; a warning while behavior continues is insufficient. |
| Stale/outage/partial or expired advisory | Label accurately or withhold; no fabricated current state or source substitution. |
| Missing evidence or public release support | No authoritative public-bound output. |
| Incomplete correction/rollback | Keep affected outputs held/withdrawn and complete downstream invalidation. |

## Governed AI and generated language

AI is interpretive, not root truth. Use scope -> admissible evidence ->
`EvidenceBundle` -> applicable rights/sensitivity/policy/review/release checks ->
cited, bounded answer or abstention/denial/error. Generated text cannot supply
missing authority, approval, source freshness, or scientific validation. [ATM]

Do not infer observations from models, exposure from smoke, current conditions
from stale data, or official instructions from a config threshold. Preserve
units, time, role, uncertainty, caveats, and correction state in maps, reports,
search and AI. Withdrawn support must not survive as an authoritative cached
answer or embedding-derived claim.

## Migration and anti-bypass posture

For a real consumer change, pin the old binding and IDs; identify affected
readers/writers and exact reference mappings; obtain necessary authority; change
the owning implementation plus tests; verify stale/correction/rollback behavior;
and retire an old binding only after consumer/reference closure. Preserve
compatibility and auditable supersession.

Do not normalize filenames to select authority, load both `air` and `atmosphere`
by default, treat an empty schema or a TODO workflow as enforcement, use directory
names as release proof, hide stale state, omit official referral, or leave
corrected outputs active. The explicit AirObservation mirror is evidence for
that pair only. [MIRROR] [AIR]

## Rollback, correction, supersession, and invalidation

**README-only rollback:** leave the isolated branch unintegrated, or prepare a
reviewed non-force revert of this change. Never rewrite shared history or
implicitly revert an already-merged PR because its lifecycle was unexpected.

**Future behavior rollback:** identify config/consumer/version and affected
exposure window; disable the binding or restore an accepted prior version; rerun
relevant checks; invalidate or withdraw dependent outputs; preserve receipts
and correction lineage; and verify that consumers no longer use the unsafe
state. Record correction, withdrawal, and rollback in their owning homes.

A Git revert does not retract already published, cached, exported, indexed, or
summarized information. Preserve prior observations, advisories, model runs,
source rights, and transformations as auditable history rather than silently
overwriting them.

## Definition of done for the first payload

**Authoring gate:** one justified named-consumer purpose; correct responsibility
root; explicit draft/test-only status where appropriate; stable identity/version;
non-secret values; no production discovery or live effects; a reviewable dependency
list; synthetic tests; and reversible removal. Unresolved scientific, source,
policy, or release dependencies remain visible and cannot authorize use.

**Binding gate:** demonstrate the exact parser/load point, supported keys and
version, deterministic precedence, required/optional handling, accepted reference
mapping, safe observability, relevant positive/negative tests, and rollback.
Profiles covering units, station identity, time, models, climate, advisories,
rights and sensitivity apply only where the consumer actually needs them.

**Operational/public-use gate:** independently establish applicable source
admission, identity, rights, sensitivity, validation, provenance, integrity,
receipts/proofs, policy, review, release, correction, and rollback closure.
Public APIs, maps, exports, and AI remain downstream of this gate. A first
synthetic config test cannot satisfy it by declaration.

## Verification backlog

| Open question | Status and next evidence |
| --- | --- |
| Consumer/load/precedence behavior | UNKNOWN; identify exact code and a tested explicit binding before activation. |
| Broader schema/validator maturity | NEEDS VERIFICATION; inspect and execute each selected profile with its dependencies. |
| Source-registry topology and admission | NEEDS VERIFICATION; use exact accepted descriptors and migration evidence, not copied registries. |
| Remaining spelling/slug compatibility | NEEDS VERIFICATION; do not generalize from AirObservation or retire Air documentation automatically. |
| Scientific profiles and freshness budgets | NEEDS VERIFICATION; method, station, spatial/vertical, temporal and use-specific review. |
| Rights, sensitive joins and public precision | NEEDS VERIFICATION; source terms and transformation/access evidence before exposure. |
| Independent review and stewardship | NEEDS VERIFICATION; CODEOWNERS proves routing only. |
| Policy/runtime, CI enforcement and release closure | UNKNOWN in this update; obtain exact execution and decision records before claiming readiness. |
| Correction/invalidation/rollback | NEEDS VERIFICATION for any real consumer and downstream artifacts. |

These items do not block safe, isolated documentation or synthetic test authoring.
They do constrain the behavior or transition that depends on the missing evidence.

## Safe language rules

| Avoid | Prefer |
| --- | --- |
| “Atmosphere is entirely scaffolded.” | “This config lane is README-only; inspected schema/validator surfaces have bounded implementation.” |
| “The validator passed.” | “Source was inspected; execution was not established by that inspection.” |
| “All schema casing is resolved.” | “AirObservation has an explicit mirror; other families require individual verification.” |
| “air and atmosphere are interchangeable.” | “Atmosphere is the current lane; Air documentation preserves compatibility and migration constraints.” |
| “The config is active / the source is admitted.” | “An explicit binding/admission record must be verified separately.” |
| “AQI concentration / observed AOD PM2.5 / smoke exposure.” | “Index, remote-sensing, or smoke context with its actual support and limitations.” |
| “The model observed / normal current weather.” | “Modeled result or baseline-relative climate product for the stated time and method.” |
| “KFM issued this alert.” | “Official-source advisory context; KFM is not the issuing authority.” |
| “Reviewed and release-ready.” | “Review routing, independent review, validation, and release are separately evidenced.” |

## Evidence ledger

Repository references below are pinned to the evidence commit, not to moving
`main`. They support the stated bounded findings only. Tool/session identifiers
are intentionally not used as durable repository citations.

| ID | Source and identity | Supports / limits |
| --- | --- | --- |
| INV | [Exact directory contents][INV]; prior README blob `6379c8123a278723f89b3bb3913f0371eff95f8b`. | One tracked README, no subdirectory; not external-file absence. |
| PARENT | [Parent configuration README][PARENT]; blob `c497e41466f3aaf934aeca4b9976a2fa8516ff21`. | Configuration responsibility; its inventories remain dated. |
| DIR / ADR-0029 | [Adopted rules][DIR], blob `fd49a0b83e55cef52c1124281f093e263526898d`; [accepted adoption record][ADR-0029]. | Placement authority, not operational enforcement. |
| ADR-0001 | [Schema-home ADR][ADR-0001]; blob `ed6f258f8d9ea152996570768a31666953e4a809`. | Still proposed; not ratified here. |
| ATM | [Atmosphere domain guide][ATM]; blob `7e7a96a3f22547fd12afcce5dc7ccd82ddd226af`. | Domain meaning, mixed maturity and compatibility guidance; not test execution. |
| AIR | [Air pipeline guardrail][AIR]; blob `2717874d4f489248a145bb8df82d4c65258b1972`. | Documentation-only compatibility intent; historical maturity details need rechecking. |
| SCHEMA / MIRROR | [Lowercase profile][SCHEMA], blob `84e88b8f0149e679e1addf23e6b9074c4c70592d`; [mirror][MIRROR], blob `4df22268a660d8d2ff1af2ad6e5e3c121b224a0c`. | Inspected draft shape and explicit reference direction; not whole-domain acceptance. |
| VALIDATOR | [Observed/modeled source][VALIDATOR]; blob `bdabf478fb2ec19395ac98a1e91895d991f9941a`. | Inspected bounded profile/field checks, not execution or scientific fitness. |
| VALIDATOR-INDEX | [Validator README][VALIDATOR-INDEX]; blob `64680d31a964d4052b4cf444700982a9d3a9e579`. | Documentary index of fixture checks; broader re-audit not claimed. |
| OWNERS | [CODEOWNERS][OWNERS]; blob `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61`. | Verified review route; no independent approval or stewardship assignment. |
| PDF | [Atmosphere / Air report, 2026-04-21][PDF]; Drive ID `1gHk6Jp3fGfrPTgvczwxyNXxvNopiKgRw`. | Read-only design lineage. Its no-mounted-repo finding describes that historical session, not this repository. No current source-rights claim. |

**Revision continuity:** v0.2 established the boundary; v0.3 expanded the station,
measurement, time, source-role, sensitivity and recovery safeguards. v0.4 retains
those safeguards while consolidating repetition, replacing stale all-scaffold
claims, recognizing the inspected schema mirror, and separating reversible
authoring from activation/release gates. Existing H2 navigation is retained.
The prior text remains recoverable through the recorded Git blob/history.

## Status summary

This directory remains a README-only, non-secret, non-authoritative configuration
lane. Atmosphere implementation outside it is mixed, not uniformly absent and
not demonstrated production-ready. The update changes documentation only:
no payload, schema, policy, source, validator, fixture, test, workflow, renderer,
API, model, scheduler, release, deployment, or published artifact is modified.

[Back to top](#top)

[INV]: https://api.github.com/repos/bartytime4life/Kansas-Frontier-Matrix/contents/configs/domains/atmosphere?ref=700570cbcf191038aa20a030174c2dd08cf93675
[PARENT]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/700570cbcf191038aa20a030174c2dd08cf93675/configs/domains/README.md
[DIR]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/700570cbcf191038aa20a030174c2dd08cf93675/docs/doctrine/directory-rules.md
[ADR-0029]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/700570cbcf191038aa20a030174c2dd08cf93675/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[ADR-0001]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/700570cbcf191038aa20a030174c2dd08cf93675/docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
[ATM]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/700570cbcf191038aa20a030174c2dd08cf93675/docs/domains/atmosphere/README.md
[AIR]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/700570cbcf191038aa20a030174c2dd08cf93675/pipelines/domains/air/README.md
[SCHEMA]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/700570cbcf191038aa20a030174c2dd08cf93675/schemas/contracts/v1/domains/atmosphere/air_observation.schema.json
[MIRROR]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/700570cbcf191038aa20a030174c2dd08cf93675/schemas/contracts/v1/domains/atmosphere/AirObservation.schema.json
[VALIDATOR]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/700570cbcf191038aa20a030174c2dd08cf93675/tools/validators/domains/atmosphere/validate_observed_modeled_separation.py
[VALIDATOR-INDEX]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/700570cbcf191038aa20a030174c2dd08cf93675/tools/validators/domains/atmosphere/README.md
[OWNERS]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/700570cbcf191038aa20a030174c2dd08cf93675/.github/CODEOWNERS
[INCIDENT]: https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024
[PDF]: https://drive.google.com/file/d/1gHk6Jp3fGfrPTgvczwxyNXxvNopiKgRw/view
