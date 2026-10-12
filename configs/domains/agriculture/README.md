<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-domains-agriculture-readme
title: configs/domains/agriculture/ — Governed Agriculture Configuration Boundary
type: readme
version: v0.4
status: draft; repository-grounded; documentation-only; no-config-binding
owners: "NEEDS VERIFICATION — specialist configuration, Agriculture, privacy, source, validation, policy, and release stewards"
review_route: "@bartytime4life via /configs/ CODEOWNERS; routing is not independent approval"
created: 2026-07-13
updated: 2026-09-04
policy_label: "public; non-secret; non-authoritative; no-live-binding; no-field-truth; no-operator-identification; no-advice; no-release-authority"
current_path: configs/domains/agriculture/README.md
owning_root: configs/
root_class: canonical
scope_id: agriculture
readme_profile: BOUNDARY_COMPACT
responsibility: "Explain the Agriculture configuration boundary without owning domain meaning, policy, source admission, evidence, or release."
truth_posture: >-
  CONFIRMED tracked README-only inventory, inherited configuration boundary,
  current workflow source, and selected schema/validator documentation /
  PROPOSED future consumer-bound configuration requirements /
  UNKNOWN dynamic or external consumers, runtime, deployment, and publication /
  NEEDS VERIFICATION first-payload schema, binding, specialist review, and operational tests
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 700570cbcf191038aa20a030174c2dd08cf93675
  source_read_commit: bb3eb695e6068b38453ca3ded8f1394a8fdebc20
  prior_blob: 99032995f37f46d4692c908092f9d7f3d7ce68fe
  prior_bytes: 82823
  tracked_files: 1
  tracked_configuration_payloads: 0
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  method: "Exact GitHub directory/file reads and bounded indexed consumer search; no full checkout or runtime execution."
related:
  - ../README.md
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../docs/domains/agriculture/README.md
  - ../../../tools/validators/domains/agriculture/README.md
  - ../../../.github/workflows/domain-agriculture.yml
  - ../../../schemas/contracts/v1/domains/agriculture/aggregation_receipt.schema.json
notes:
  - "v0.4 replaces stale July-wide scaffold claims with a bounded September source review; executable configuration remains absent from this tracked lane."
  - "Existing H1, document identity, and H2 navigation topics are preserved; repeated controls and historical inventory prose are condensed."
  - "Workflow source inspection is not a test result or proof that the workflow consumes this directory."
  - "No executable configuration, source activation, policy threshold, schema, consumer, workflow, release, or publication is changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Agriculture Domain Configuration

`configs/domains/agriculture/` is the Agriculture-specific boundary inside KFM's
[commit-safe configuration root](../../README.md). It currently contains **this
README only**. There is no tracked Agriculture configuration payload to load.

**Documentation:** draft v0.4 · **Configuration maturity:** documentation-only ·
**Domain implementation:** mixed, with bounded fixture-based validation ·
**Activation and release:** not established by this directory.

**Start here:** [Current evidence](#status) · [Permitted content](#what-belongs-here) ·
[Consumer binding](#consumer-binding-precedence-and-discovery) ·
[Validation](#validation) · [First payload](#definition-of-done-for-the-first-payload) ·
[Rollback](#rollback-correction-and-deactivation).

> [!IMPORTANT]
> Agriculture has executable validation elsewhere; that does not make this
> configuration lane implemented or consumed. A configuration value may select
> an already-governed profile. It cannot establish crop or field truth, identify
> an operator, remove suppression, admit a source, approve advice, or release data.

> [!CAUTION]
> Never commit credentials, private endpoints or live bindings, exact protected
> field/facility geometry, operator-linked records, confidential statistics, or
> data that reconstructs private operations. Public clients use governed APIs
> and released public-safe artifacts, not this directory or internal stores.

## Purpose

Keep Agriculture configuration discoverable, non-secret, explicitly bound, and
reviewable. Inherit common rules from the [domain configuration parent](../README.md)
rather than maintaining another general configuration standard. This document
adds Agriculture-specific identity, time, statistical-disclosure, and source-role
constraints for maintainers and prospective consumer owners.

## Authority level

The owning responsibility root is `configs/`; `agriculture` is a scope segment,
not a new authority root. [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the exact [Directory Rules](../../../docs/doctrine/directory-rules.md)
bytes, including the boundary-README, compatibility, and migration rules.
The adopted artifact retains its historical draft label; that label does not
undo the accepted, exact-byte adoption decision.

Meaning belongs to contracts, machine shape to schemas, admissibility to policy,
source identity and admission to governed registries, evidence to its owning
families, and release decisions to `release/`. Configuration supports a named
consumer; it cannot replace any of those responsibilities.

## Status

### Evidence snapshot

All snapshot claims below are bounded to `main@700570cbcf191038aa20a030174c2dd08cf93675`
on **2026-09-04**. Sources were read at `bb3eb695e6068b38453ca3ded8f1394a8fdebc20`
and revalidated by an exact base comparison: only the unrelated catalog triplet
README changed. The preimage of this README is Git blob
`99032995f37f46d4692c908092f9d7f3d7ce68fe`.

```text
configs/domains/agriculture/
└── README.md    # Configuration boundary; no executable payload
```

The exact directory response contains one regular file and no child directories,
placeholders, or configuration payloads. This closes the tracked inventory for
this lane, not ignored, untracked, generated, externally mounted, or hosted files.
A bounded indexed search for the literal path outside Markdown returned zero
matches; dynamically constructed and external consumers remain unverified.

### Confirmed repository surfaces

| Surface inspected | Current source evidence | Limit |
|---|---|---|
| This configuration lane | One README; zero configuration payloads | No loader, binding, precedence, or active consumer established |
| Configuration parents | `configs/` v0.5; `configs/domains/` v0.6 | Their historical inventory snapshots are not live counts |
| [Agriculture domain orientation](../../../docs/domains/agriculture/README.md) | v0.3, updated 2026-08-28; mixed-maturity domain | Documentation is not runtime or source-admission proof |
| [Domain workflow](../../../.github/workflows/domain-agriculture.yml) | Readiness checks, public-safe carrier fixture validation/tests, and fixture-only CDL watcher tests are wired | Source inspected; no exact-head execution result asserted here |
| Dedicated NDVI and vegetation checks | Domain workflow names separately owned, path-filtered NDVI delta, HLS materiality, NDVI readiness, and vegetation connectivity workflows | Listing a workflow is not evidence that it ran for a documentation change |
| [Per-domain validator index](../../../tools/validators/domains/agriculture/README.md) | Existing narrower edge/cross-lane index, distinct from broad `tools/validators/agriculture/` scope | Its July maturity narrative also needs current executable evidence |
| [AggregationReceipt scaffold](../../../schemas/contracts/v1/domains/agriculture/aggregation_receipt.schema.json) | Still `PROPOSED`, with empty `properties` and `additionalProperties: true` | Not an Agriculture configuration schema or meaningful disclosure validation |

### Maturity matrix

**CONFIRMED source wiring / PARTIAL Agriculture validation / NOT IMPLEMENTED in
this tracked configuration lane.** The earlier blanket statement that Agriculture
CI is only TODO echo jobs is obsolete. Conversely, the current workflow explicitly
retains broader validation, proof-production, and release-readiness holds.
Neither a held job nor a successful inventory check proves an operating pipeline.

### Current conflicts and drift

The domain orientation discourages a parallel `tools/validators/domains/agriculture/`
home, while the current workflow explicitly references that existing subtree and
its dedicated validators. The per-domain index describes a narrower edge-specific
scope. Preserve that documentation/implementation tension; use exact current code
and workflow evidence for behavior, not this config README to reclassify or move it.

The v0.3 preimage also recorded short-versus-segmented contract/schema paths,
`aggregation_receipt` versus `aggregation-receipt`, receipt-root versus `receipts/`
placement, and three source-registry orderings. Their complete disposition was
**not re-audited** here. A future binding must resolve its exact object's authority
and aliases; do not repeat old conflicts as newly verified global findings.

## What belongs here

This README and, after bounded review, small non-secret defaults, templates,
examples, or profile selectors for an exact named consumer. Templates and examples
remain synthetic and inactive by presence. Profile selectors reference accepted
IDs and versions rather than duplicate crop crosswalks, methods, suppression
thresholds, sensitivity rules, or release decisions.

A config-local key migration note may accompany a real consumer transition.
Authority-changing migration records remain in their owning governance/migration
homes. Do not add empty scaffolding merely to illustrate a future tree.

## What does not belong here

No source payloads, survey extracts or microdata, imagery, statistical records,
field/parcel/facility data, operator or living-person records, financial transactions,
private endpoints, signed URLs, credentials, workstation-specific values, or live
deployment bindings. No contracts, schemas, policy rules, source descriptors,
registries, receipts, proofs, catalog/triplet objects, release records, or published
products. No settings that weaken evidence, rights, suppression, review, or release.

## Inputs

A proposed payload needs a named consumer and owner, declared class and parser,
explicit binding, applicable authority references, synthetic safe values, relevant
source/time/spatial/method context, validation, failure behavior, and rollback.
Missing operational evidence may remain explicit in an isolated draft; it must not
be converted into a claim of active consumption or permission for exposure.

## Outputs

Currently, documentation only. A future consumer may use validated configuration
to select governed behavior. Parsing must not itself query a live source, initiate
imagery processing, infer field/operator identity, emit trust objects, or publish.
Promotion remains a governed transition, not a file move or a configuration toggle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

## Validation

### Validation matrix

For **this README**, check metadata, a single H1, retained anchors, relative links,
tables, fences, final newline, whitespace, exact changed paths, and generation
provenance. Report the actual results in the branch/PR handoff and receipt; the
presence of this checklist is not a passing result.

For a **future consumed payload**, require deterministic parsing and a meaningful
consumer-owned schema/format contract; known-key handling; binding and precedence;
missing/stale/withdrawn-input behavior; source-role and support preservation; crop
identity, time, revision, units, uncertainty, disclosure controls, and rights checks;
no-network synthetic tests; safe diagnostics; and correction/deactivation/rollback.
Exercise both accepted and rejected cases. Use the actual owning contract's outcomes.

### Configuration-review outcomes

`PASS`, `RESTRICT`, `HOLD`, `ABSTAIN`, `DENY`, and `ERROR` are explanatory review
terms here, not a newly implemented enum or parser API. `QUARANTINE` denotes a
controlled handling/lifecycle action where applicable. Do not collapse these into
one wire-level status family. Passing a check is neither review approval nor merge,
activation, release, or publication authorization.

### Existing domain checks are not config checks

The following commands are copied from the inspected domain workflow. They are
**reference commands for a prepared checkout**, not commands executed by this
README and not proof of consumer binding:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 \
  python tools/validators/domains/agriculture/validate_public_safe_map_feature.py --fixtures
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 \
  python -m pytest -q tests/domains/agriculture/test_public_safe*.py
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest tests.ingest.cdl_watch.test_cdl_watch --verbose
```

The workflow supplies its own declared dependencies. An environment-variable name
alone does not prove network isolation. No Agriculture config-validator command is
invented; the permissive AggregationReceipt scaffold must not be repurposed as one.

## Review burden

### Minimum review posture

[CODEOWNERS](../../../.github/CODEOWNERS) routes `/configs/` to `@bartytime4life`.
That is a verified review route, not specialist stewardship, required approval,
independent review, or evidence that review occurred.

README changes need configuration/docs and Agriculture review. Payloads additionally
need their consumer and validation owners. Source changes add rights/source review;
field/operator, aggregation, and public-output changes add privacy, statistical,
policy, evidence, release, and affected-domain review. Loader or authority changes
need proportional architecture review. Generation and approval stay separate.

### Change budget

Prefer one coherent concern: this README; one bound template with its required
tests; one profile-reference update; or one reversible key migration. Do not bundle
source activation, policy changes, data migration, or release into documentation work.

## Related folders

Use the [parent configuration index](../README.md) for common defaults and override
boundaries, the [configuration root](../../README.md) for repository placement, and
[Agriculture orientation](../../../docs/domains/agriculture/README.md) for the domain
map. Consult the [per-domain validator index](../../../tools/validators/domains/agriculture/README.md)
and [actual workflow](../../../.github/workflows/domain-agriculture.yml) together;
resolve their differing scope/maturity narratives before implementation.

For object-specific contracts, schemas, policy, fixtures, registries, receipts,
proofs, catalogs, and releases, follow the owning domain references and inspect the
exact target. A directory link does not accept a schema, activate a source, or create
a route. Root-level `catalog/` remains a deprecated compatibility surface, not a
new place to store Agriculture truth.

## ADRs and drift triggers

This revision accepts no ADR, creates no alias, and changes no authority owner.
ADR-0029 is the placement basis. New or moved authority homes, parallel writable
contracts/schemas/registries, or general discovery/precedence architecture require
an accepted decision before dependent structural implementation. Ordinary documentation and
safe branch-local drafts do not require a new ADR merely to exist.

### Drift triggers

Escalate undeclared consumers, overlapping config scopes, contradictory authority
references, duplicate descriptors, field/operator-sensitive keys without review,
public reads of internal stores, and released-output changes without correction
lineage. Preserve the exact evidence and scope rather than silently choosing a winner.

## Last reviewed

**2026-09-04**, at the base commit in [Status](#status). Human review is pending.
Re-review when the first payload or consumer appears, a loader/schema/profile changes,
a sensitive or public-facing selector is proposed, an authority/alias decision changes,
a validation or ownership boundary changes, or correction/withdrawal/rollback occurs.
Use an explicitly assigned risk-based interval, not the old blanket six-month timer.

## Scope and bounded context

The retained Agriculture vocabulary includes `CropObservation`, `FieldCandidate`,
`CropRotation`, `YieldObservation`, `IrrigationLink`, `ConservationPractice`,
`SoilCropSuitability`, `AgriculturalEconomyObservation`, `SupplyChainNode`,
`DroughtStressIndicator`, `PestStressIndicator`, and `AggregationReceipt`.
These are domain concepts and potential consumers' concerns, **not configuration
keys or a claim that every family is implemented or accepted**.

## Configuration classes

Templates, examples, development/test/review defaults, public-safe profile selectors,
source-profile selectors, model/method selectors, and time-bounded compatibility
mappings may be proposed for a named consumer. These remain descriptive classes
until its contract defines exact values. Real production bindings belong to the
approved deployment/secret system, not this tracked lane. No class activates itself.

## Minimum configuration contract

This is a **PROPOSED design checklist**, not a published config schema. A consumer's
actual contract owns field names and supported values.

| Concern | Required declaration before use |
|---|---|
| Identity and scope | Config ID/version, class, `agriculture` scope, owner, reviewers, review date |
| Reader and format | Exact consumer/version, file path, parser/version, format and canonicalization |
| Selection | Explicit binding; included files; merge/replace and key precedence; substitution/coercion rules |
| Authorities | Exact contract, schema, policy, registry, profile, receipt, and applicable decision references |
| Source support | Source/product/profile IDs and claim-relative roles; no credentials or admission decisions |
| Space and time | Support unit, crop/survey/reference period, acquisition/observation/valid times, revision and freshness |
| Measurement | Unit, denominator, sample frame, method/model/run/version, resolution, QA and uncertainty |
| Privacy and rights | Audience, accepted aggregation/suppression/generalization references, attribution and redistribution limits |
| Execution | No network or side effects during parsing/core validation; separate authorized live execution |
| Failure and diagnostics | Unknown/missing/deprecated keys, partial load, stale/withdrawn profile handling, redacted diagnostics |
| Validation and retirement | Positive/negative tests, deprecation/sunset, deactivation, correction/invalidation and rollback references |

Do not store policy-significant values here to avoid review of their owning policy.

## Consumer binding, precedence, and discovery

### Explicit binding

No consumer is established for this lane. A future reader must select an exact file;
recursive discovery, first-match wins, or loading every YAML file is not authorized
by a folder name or this README.

### No implicit precedence

Define and test included files, replacement versus merge, key-level order,
environment substitution, type coercion, unknown keys, absent files, partial loads,
stale/deprecated profiles, safe logging, cache invalidation, and rollback selection.
No universal defaults-to-environment-to-local-to-CLI order is established here.

### Safe failure

Missing or invalid configuration must not activate sources, broaden audience,
unmask protected detail, upcast models/candidates/estimates, bypass review, provide
advice, or keep serving a withdrawn public profile through permissive fallback.

## Agriculture object-family boundaries

| Keep distinct | Do not infer |
|---|---|
| Crop observation / classified pixel / survey estimate / model | Direct observation from a classification or aggregate |
| Field candidate / cadastral parcel / CLU / farm / operator / facility | Identity, title, control, management, or public permission from overlap |
| Rotation / repeated class sequence / management record | Farm-management continuity from imagery alone |
| Measured yield / modeled yield / aggregate estimate / operator record | Field or operator performance from county statistics |
| Irrigation context / water right / pumping / allocation | Use, entitlement, or compliance from a link |
| Conservation context / program participation / field verification | Practice adoption, effectiveness, payment, or compliance from administration |
| Suitability or stress / recommendation / loss or diagnosis | Operational advice or a regulatory/insurance decision from an indicator |
| Economy aggregate / transaction; supply-chain context / operations | Private business performance, inventory, security, or real-time status |
| Receipt / EvidenceBundle / policy decision / proof / release | Approval or truth from process provenance |

## Source role and knowledge character

Preserve claim-relative observed, regulatory, administrative, modeled/classified,
aggregate, candidate, contextual, and synthetic distinctions using the exact governing
profile. Preserve restricted-access and sensitivity posture as well; do not invent
or collapse machine fields from this explanatory vocabulary. A source family can
support different roles for different products. Configuration cannot assign a more
authoritative role or turn synthetic material into observation.

## Field, parcel, operator, and facility identity

Overlap, centroids, matching acreage, address proximity, repeated crop classes, or
persistence do not prove field/parcel/operator equivalence. Preserve boundary method,
uncertainty, source, vintage, splits/merges, and revision lineage. Administrative
records do not establish title, tenancy, management, or current use. Public IDs must
not encode private identity or enable reverse lookup; hidden operator/parcel/facility
crosswalks are prohibited.

## Spatial unit, aggregation, suppression, and reconstruction

### Spatial/support units

Keep state, crop-reporting district, county, HUC/watershed, administrative region,
grid, pixel, generalized tile, field candidate, parcel-adjacent feature, facility,
and network support distinct. Thresholds and methods do not transfer across them
without an accepted transformation.

### Aggregation rules

Use accepted versioned profiles and preserve geography, denominator/population,
frame, time window, role, method, uncertainty, suppression, and revision. Never copy
an aggregate onto fields/operators as an observation; resampling and zonal statistics
do not create field truth.

### Suppression and disclosure control

Never undo source suppression, reconstruct cells from totals/categories or time
slices, expose sparse groups, lower thresholds/delays, or combine map/API/search/export
views to reveal private operations. Jitter or aggregation alone is not a privacy proof.

### Transform evidence

Require the applicable aggregation, redaction, generalization, or transform evidence
and receipts. A profile selector cannot fabricate, approve, or replace them.

## Crop year, survey year, time, and revision state

Distinguish crop year, survey/reference period, acquisition, observation, valid
interval, retrieval, upstream publication, KFM release, correction, and freshness.
Preserve source-specific preliminary/revised/final/superseded/withdrawn states.
New retrieval does not make an old season current; revisions need explicit lineage,
not silent replacement. Operationally time-sensitive context must show staleness.

## Units, methods, denominators, quality, and uncertainty

Carry measure, unit, numerator/denominator, area/weight/count/volume basis,
commodity/class, geography, period, instrument/method, sample frame, model/run/version,
resolution, QA, confidence/error/uncertainty, suppression, revision, and fitness-for-use
where material. Classified acreage is not observed planted acreage; production is
not operator output; a price index is not a transaction price; pixel confidence is
not field certainty. Normalization cannot make missing support valid.

## Classified imagery, remote sensing, and model products

For classified imagery, vegetation indices, evapotranspiration, yield, or stress
products, retain product/version, scene/granule/tile/run identity, acquisition and
processing time, resolution, native classes/crosswalk version, training/reference
and validation support, QA/cloud/masks, method, uncertainty, limitations, evidence,
and release references. Repeated classification is not rotation proof, a vegetation
signal is not a diagnosis, and an extracted field candidate is not a confirmed parcel.

## Suitability, stress, and advice boundary

Method-specific suitability, moisture/heat/drought/pest stress, erosion/conservation,
productivity, and restoration context must retain input, scale, time, uncertainty,
limitations, and evidence. Configuration cannot authorize planting/spraying/irrigation,
fertilizer/harvest/grazing, veterinary/pesticide, engineering/safety, insurance/lending,
appraisal/tax, market/investment, legal/title/water-right, compliance, or emergency
advice. Missing support calls for narrowing, abstention, or hold.

## Irrigation, conservation, regulatory, and compliance context

Keep Hydrology-owned observations and People/Land rights context separate from
Agriculture interpretation. Planning, technical assistance, program records,
remote sensing, self-report, and field verification are not interchangeable.
Regulatory, disease/quarantine, inspection, pesticide, animal-health, contamination,
or enforcement information may be sensitive and time-bound. No config may bypass
review, redaction, retention, delay, audience restrictions, or correction.

## Agricultural economy and supply-chain context

Preserve statistical support, reference period, commodity, price/quantity/value and
inflation/index basis, method, uncertainty, suppression, and finality. Do not expose
or infer individual revenues, costs, debt, taxes, insurance, transactions, contracts,
customers/workers, performance, buyer/seller relationships, facility inventory,
capacity, vulnerability, access, schedules, routes, or live operations. No trading
signals or financial recommendations follow from a profile selector.

## Cross-domain joins

Soil retains soil units, horizons, survey identity, and properties; Hydrology retains
water observations; Atmosphere retains weather/climate observations and forecasts;
Hazards retains hazard-event semantics; People/DNA/Land retains protected person,
parcel, title, ownership, and consent context. Habitat/Flora/Fauna retain ecological
and taxonomic truth; Geology retains lithology/stratigraphy/resources;
Settlements/Infrastructure retains facility context; Roads/Rail/Trade retains routes.

Every join preserves its owning claims, evidence, source role, time, scale, rights,
sensitivity, policy, transform receipts, release, correction, and rollback. Neither
geometry overlap nor combined layers may reveal protected people, sites, species,
private operations, or infrastructure vulnerabilities.

## Source rights, attribution, and redistribution

Before use, resolve publisher/product identity, permitted access and automation,
terms/license, attribution/redistribution and derivative limits, audience,
confidentiality, cadence, vintage/revision, coverage, role, stale/supersession behavior,
and review ownership. No current endpoint, license, or source admission is certified
by this documentation revision. Missing rights block the affected use or exposure.

## Logging, telemetry, and observability

Diagnostics must not become an export of credentials, private paths/endpoints,
field/facility geometry, operator/person/business identity, unsuppressed cells,
confidential records, payloads, or protected prompt/model text. Prefer public-safe
config/consumer/parser/validator IDs and digests, support/period, redacted error/reason
codes, and permissible evidence/policy/receipt/release references.

## Failure behavior

Reject or hold malformed, incomplete, unknown-key, incompatible, unresolved,
stale/withdrawn, role-upcasting, disclosure-unsafe, or authority-bypassing inputs.
Preserve the governing consumer's finite outcomes and distinguish review state from
runtime response and lifecycle action. No silent fallback may broaden access,
remove suppression, fabricate support, or release a derivative.

## Governed AI and generated language

Follow scope -> admissible evidence -> `EvidenceRef` -> `EvidenceBundle` -> rights,
sensitivity, disclosure, policy, review, release/audience checks -> cited bounded
answer or abstention/denial. AI cannot treat configuration as evidence, invent facts,
identify private operations, erase caveats, or leak through prose what a map hides.
Maps, tiles, indexes, graphs, screenshots, reports, and AI remain downstream carriers.

## Migration and anti-bypass posture

Freeze identities, blobs, consumers, and affected releases; contain secrets and
sensitive material without erasing audit evidence; classify by owning responsibility;
obtain the applicable decision before authority-changing cutover; update explicit
bindings with compatibility, negative tests, and rollback. Correct affected
published derivatives through their owners. No silent rename, copied descriptor,
second schema/policy home, or config-to-catalog/release write is permitted.

### Anti-bypass matrix

Source activation, live credentials, exact protected data, local suppression policy,
direct public internal-store reads, role upcasts, missing evidence/receipt/review,
automatic publication, operational advice, and canonical writes into compatibility
paths all require rejection or controlled containment—not a convenient config flag.

## Rollback, correction, and deactivation

### Rollback triggers

Wrong role/profile/class/time/revision/unit, privacy or suppression regression,
reconstruction risk, rights/attribution failure, authority conflict, advice leakage,
broken evidence/release links, or undocumented consumer behavior requires correction.

### Required rollback sequence

Disable the exact binding; enter a safe state; restore a reviewed config; stop or
quarantine affected jobs/candidates; invalidate caches, tiles, exports, search,
graph/vector indexes, and AI context; identify affected periods/geographies/releases;
preserve safe provenance; issue governing correction/withdrawal/rollback records;
rerun applicable negative and positive tests. Correct distributed/static copies through
their correction channel rather than claiming every screenshot can be recalled.

For this documentation-only change, preserve the branch or use a reviewed forward
revert to the preimage recorded in metadata. Do not force-push shared history or
claim a runtime rollback drill. Generation receipts retain their historical meaning;
different artifact bytes require matching provenance, not silent receipt reuse.

## Definition of done for the first payload

Before a payload is treated as consumed, verify its exact owner/consumer, format,
meaningful schema, explicit binding/precedence/fallback, relevant authority and source
references, privacy/rights review, positive/negative tests, safe diagnostics, and
reversible deactivation. Apply the identity, time, measurement, model, cross-domain,
and disclosure checks above wherever the consumer's actual scope makes them material.

Before any public effect, additionally close evidence, policy, review, transform
receipts/proofs, release, correction, and rollback. An isolated synthetic draft is
not an active payload; unresolved gates must travel with it explicitly. Do not use
later publication gates as a blanket ban on safe reversible authoring.

## Verification backlog

| Question | Status / next evidence needed |
|---|---|
| Tracked lane inventory | CONFIRMED: README only at the pinned base |
| Direct config consumer, schema, parser, precedence | UNKNOWN / not established; inspect and test the first exact reader |
| Dynamic, external, untracked, or deployed reads | UNKNOWN; indexed search is not exhaustive consumer closure |
| Agriculture CI maturity | CONFIRMED source-level partial execution; exact-run results remain separate |
| AggregationReceipt completeness | CONFIRMED permissive scaffold; no privacy/config validation implied |
| Validator documentation scope discrepancy | NEEDS VERIFICATION; reconcile owning docs against exact implementation without creating another lane |
| Historical contract/schema/registry aliases | NEEDS VERIFICATION for each selected family; no global migration decision made |
| Source roles, rights, profile thresholds and admission | NEEDS VERIFICATION before affected use; no live source check performed |
| Specialist stewardship and independent review | NEEDS VERIFICATION; CODEOWNERS is routing only |
| Runtime, public exposure, release and operational rollback | UNKNOWN / NOT INSPECTED |

## Safe language rules

Say **“no tracked config payload”**, not “Agriculture has no implementation.” Say
**“the workflow wires fixture-based checks”**, not “CI proves this config is consumed.”
Say **“this AggregationReceipt file is permissive”**, not “all Agriculture schemas
are empty.” Say **“field candidate,” “aggregate estimate,” “method-specific indicator,”**
and **“claim-relative source role”** unless stronger evidence supports stronger words.
Never equate a parse, test, receipt, merge, map, or generated answer with approval.

## Evidence ledger

| Evidence at the pinned base | Use / limitation |
|---|---|
| `configs/domains/agriculture/` exact Contents response; target preimage | Complete tracked leaf inventory and v0.3 lineage; no external inventory |
| `configs/README.md`; `configs/domains/README.md` | Inherited non-secret, non-authoritative configuration responsibility |
| Directory Rules blob `fd49a0b83e55cef52c1124281f093e263526898d`; accepted ADR-0029 | Adopted placement and boundary/migration rules; not runtime proof |
| `.github/CODEOWNERS` blob `dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61` | Verified review routing, not approval |
| `.github/workflows/domain-agriculture.yml` | Current executable wiring and explicit broader holds; not an observed run |
| `docs/domains/agriculture/README.md`; `tools/validators/domains/agriculture/README.md` | Domain and narrower validator scope; differing historical descriptions remain visible |
| AggregationReceipt blob `16c55157c07d3115bfb540b2064e0401bc71b564` | Exact still-permissive scaffold; does not characterize every schema |
| Literal-path code search excluding Markdown | Zero indexed matches at review; cannot exclude computed or external reads |
| Drive Directory Rules; Notion Agriculture builder record | Read-only lineage/coordination; their older checkpoints do not override GitHub |

The full v0.3 preimage remains in Git history. v0.4 preserves document identity,
H1/H2 navigation topics, agricultural distinctions, privacy/disclosure controls,
source/time/method limits, cross-domain ownership, and correction/rollback. It
condenses repeated lists, replaces stale global scaffold claims, and keeps prior
alias findings as unclosed lineage rather than pretending to reverify them.

## Status summary

**README-only configuration, not TODO-only Agriculture.** This revision updates
navigation and the source-evidence boundary without adding a config payload,
changing executable behavior, accepting a source or policy, resolving authority
aliases, activating a consumer, or granting merge/release/publication authority.
Review and delivery evidence belongs in the accompanying handoff and generated
receipt; operational readiness must be demonstrated separately.

[Back to top](#top)
