<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-fauna-readme
title: tools/validators/domains/fauna README
type: README
version: v0.2.1
status: draft
owner: TODO-tooling-qa-owner-plus-fauna-steward-plus-sensitive-species-reviewer-plus-geoprivacy-reviewer-plus-policy-steward-plus-evidence-steward
created: 2026-07-07
updated: 2026-07-25
policy_label: repository-facing; per-domain-validator-index; fauna; sensitive-species; geoprivacy; fail-closed; non-authoritative
owning_root: tools/
responsibility: proposed per-domain Fauna validator index for occurrence, sensitive-site, geoprivacy, taxon/status, range, migration, mortality, disease, invasive-species, evidence, policy, release, correction, rollback, and public-surface denial checks while deferring Fauna meaning, proof records, policy decisions, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../README.md
  - ../../biodiversity/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../../../../docs/domains/fauna/README.md
  - ../../../../../docs/domains/fauna/IDENTITY_MODEL.md
  - ../../../../../docs/domains/fauna/FILE_SYSTEM_PLAN.md
  - ../../../../../docs/runbooks/fauna/PROMOTION_RUNBOOK.md
  - ../../../../../docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md
  - ../../../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../../../contracts/domains/fauna/
  - ../../../../../schemas/contracts/v1/domains/fauna/
  - ../../../../../policy/domains/fauna/
  - ../../../../../policy/sensitivity/fauna/
  - ../../../../../data/registry/sources/fauna/
  - ../../../../../data/proofs/fauna/
  - ../../../../../data/receipts/
  - ../../../../../release/
  - ../../../../fixtures/domains/fauna/
  - ../../../../tests/domains/fauna/test_fauna_smoke.py
  - ../../../../.github/workflows/domain-fauna.yml
notes:
  - "One executable is accepted: validate_public_safe_fixture.py, limited to synthetic fixture safety and explicitly not production occurrence validation."
  - "The bounded executable is hardened against declared coordinate/location aliases, numeric values under location-like keys, malformed caveat containers, normalized URL-like strings, control characters, and coordinate-pair-shaped free text."
  - "The broad tools/validators/fauna/README.md and source_role/ child README exist; this path remains the per-domain home for the bounded executable."
  - "Fauna sensitive taxa, exact occurrences, nests, dens, roosts, hibernacula, spawning sites, breeding/aggregation sites, steward-controlled records, and reverse-engineerable derivatives are deny-by-default unless geoprivacy, review, policy, evidence, release, correction, and rollback support authorize a public-safe derivative."
  - "Validators enforce declared contracts, schemas, and policy. They do not define Fauna meaning, create EvidenceBundles, make stewardship decisions, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/fauna

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-fauna--validators-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-deny--by--default-red)
![authority](https://img.shields.io/badge/authority-checker--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/fauna/` is the per-domain Fauna validator lane for bounded fail-closed checks. Its accepted executable validates only a closed synthetic fixture profile; it is not production `OccurrencePublic` validation.

---

## Purpose

`tools/validators/domains/fauna/` organizes Fauna validators under the durable `tools/validators/` responsibility root.

The durable KFM question for this lane is:

> Does a declared Fauna candidate preserve taxonomic identity, source-role posture, sensitive-species geoprivacy, evidence and review state, policy boundaries, release holds, correction paths, rollback support, and public-surface denial for the exact validation scope—or must it fail closed?

The lane must not create Fauna truth, taxonomic authority, stewardship decisions, EvidenceBundles, geoprivacy transforms, PolicyDecisions, release decisions, public map layers, API payloads, or AI answers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/fauna/README.md` | **CONFIRMED** | This README records the bounded executable and its authority limits. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` remains minimal; this file keeps the Fauna boundary explicit. |
| Broad `tools/validators/fauna/README.md` | **CONFIRMED routing README** | Broad routing only; this path remains the per-domain executable home. |
| Fauna doctrine and deny-by-default ADR | **CONFIRMED repository evidence / draft** | They require sensitive occurrence and reverse-engineering risk to fail closed. |
| Accepted executable | **CONFIRMED bounded slice** | `validate_public_safe_fixture.py`; standard library, deterministic, no network, fixture-only. |
| Accepted fixture/test inventory | **CONFIRMED bounded slice** | One valid and five invalid JSON fixtures feed seven tests in `test_fauna_smoke.py`. |
| Current CI scope | **CONFIRMED bounded slice** | Only `validate-fauna` runs the accepted module; proof and release-dry-run remain held. |
| Production schemas, source descriptors, policy runtime, receipts, proof, release, and public behavior | **NEEDS VERIFICATION / held** | The bounded executable creates no production authority. |

[Back to top](#top)

---

## Accepted bounded executable

`validate_public_safe_fixture.py` accepts only candidates that are explicitly:

- synthetic and fixture-only;
- referenced by bounded `fixture:` identifiers;
- `source_role: synthetic`;
- rights-scoped to fixture use;
- location-withheld;
- no-network;
- not released;
- not eligible for promotion; and
- explicit about fixture-only evidence, review, correction, and rollback state.

It additionally fails closed on:

- undeclared top-level, spatial, or governance fields;
- exact or aliased location-bearing keys;
- finite numeric values beneath location-like keys;
- malformed or nested `public_caveats`, more than 16 caveats, or caveat strings longer than 512 characters;
- URL-like strings after whitespace and Unicode-format-marker normalization, including embedded HTTP(S), scheme-relative, and `www.` forms;
- control characters in strings;
- coordinate-pair-shaped free text; and
- cyclic, deeper-than-64-level, or more-than-4,096-node in-memory structures;
- fixture files larger than 1,000,000 bytes, integer tokens over 512 digits, or JSON values Python cannot parse safely; and
- unsupported synthetic identifier shapes.

These checks reduce accidental leakage in future fixtures. They do not determine whether a real occurrence is public-safe.

Structural cycle, depth, or node-limit findings stop further field inspection so malformed in-memory candidates cannot force unbounded secondary findings.

[Back to top](#top)

---

## Child lanes

No child README lane is accepted as an executable authority by this bounded slice.

Possible future children remain **PROPOSED** until separately verified:

- `occurrence/` for occurrence evidence, restriction, and public-safe derivatives;
- `geoprivacy/` for redaction, generalization, buffering, gridding, and aggregation checks;
- `sensitive-site/` for nests, dens, roosts, hibernacula, spawning, breeding, and aggregation sites;
- `taxon-status/` for taxon identity, crosswalk, conservation, and legal-status posture;
- `range-migration/` for range polygons, seasonal ranges, and migration claims; and
- `disease-mortality/` for mortality and disease observation boundaries.

A child lane requires accepted contracts, schemas, policy posture, synthetic fixtures, report semantics, receipts where appropriate, and explicit non-authority language.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Fauna validator implementation and index | `tools/validators/domains/fauna/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain ecology/biodiversity checks | `tools/validators/biodiversity/`, `tools/validators/cross-domain-joins/` |
| Fauna domain meaning | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| Fauna schemas | `schemas/contracts/v1/domains/fauna/` or an ADR-selected home |
| Fauna policy rules | `policy/domains/fauna/`, `policy/sensitivity/fauna/` |
| Source descriptors | `data/registry/sources/fauna/` or an accepted source-registry home |
| Evidence and proof support | `data/proofs/fauna/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, corrections, withdrawal, rollback | `release/` |
| Tests and fixtures | `tests/domains/fauna/`, `fixtures/domains/fauna/` |

A validator pass means only that the declared checks passed for the declared object and scope. It is not source admission, evidence closure, policy approval, review approval, release approval, or publication authority.

[Back to top](#top)

---

## What belongs here

Good fits include:

- this validator-lane README;
- deterministic validators that enforce declared, externally owned semantics;
- optional parent runners that delegate without redefining rules;
- stable finding codes and non-sensitive paths;
- fixture references and test-surface guidance; and
- documentation that explains checker scope without becoming Fauna doctrine.

## What does not belong here

| Do not put here | Correct home |
|---|---|
| Shared plumbing | `tools/validators/_common/` |
| Fauna domain docs and contracts | `docs/domains/fauna/`, `contracts/domains/fauna/` |
| Schemas | `schemas/contracts/v1/...` |
| Policy and sensitivity rules | `policy/...` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | governed `data/` lifecycle roots |
| EvidenceBundles, proofs, or trust-bearing receipts | `data/proofs/`, `data/receipts/` |
| Release manifests and decisions | `release/` |
| Tests and reusable fixtures | `tests/`, `fixtures/` |
| Public API, UI, map, tile, export, search, graph, Focus Mode, or AI runtime | governed application/runtime roots |

[Back to top](#top)

---

## Fauna validator posture

Fauna validators must fail closed, deny, abstain, or route to authorized review when a candidate:

- lacks evidence, source, source-role, taxon, rights, or review support;
- collapses restricted occurrences, public derivatives, sensitive sites, ranges, migration routes, mortality, disease, or invasive-species records;
- exposes sensitive taxa, exact or aliased occurrence geometry, or reverse-engineerable derivatives;
- lacks a required geoprivacy transform, receipt, PolicyDecision, ReviewRecord, ReleaseManifest, correction path, or rollback target;
- permits map, tile, search, graph, export, Focus Mode, or AI exposure beyond an approved public-safe derivative;
- offers operational wildlife guidance outside accepted authority; or
- treats validator output as promotion, release, or publication approval.

The lifecycle invariant remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Stable bounded findings

The accepted fixture-only validator may emit stable findings including:

| Finding family | Meaning |
|---|---|
| `*_MISSING`, `*_INVALID`, `*_UNRESOLVED` | Required synthetic fixture state is absent or invalid. |
| `UNDECLARED_*_FIELD` | The closed fixture profile contains an undeclared field. |
| `PRECISE_LOCATION_FIELD_FORBIDDEN` | A location-bearing key or declared alias appears. |
| `LOCATION_NUMERIC_VALUE_FORBIDDEN` | A finite numeric value appears beneath a location-bearing key. |
| `LIVE_URL_FORBIDDEN` | A URL-like string appears in the fixture. |
| `COORDINATE_PATTERN_FORBIDDEN` | Free text resembles a coordinate pair. |
| `CONTROL_CHARACTER_FORBIDDEN` | A string contains disallowed control characters. |
| `PUBLIC_CAVEATS_INVALID` / `PUBLIC_CAVEAT_INVALID` / `PUBLIC_CAVEATS_TOO_MANY` / `PUBLIC_CAVEAT_TOO_LONG` | Caveats are not a non-empty list of at most 16 non-empty strings, each at most 512 characters. |
| `DOCUMENT_CYCLE_FORBIDDEN` / `DOCUMENT_DEPTH_EXCEEDED` / `DOCUMENT_NODE_LIMIT_EXCEEDED` | An in-memory candidate exceeds the bounded structure profile. |
| `FIXTURE_TOO_LARGE` / `FIXTURE_JSON_INVALID` | A fixture file exceeds the byte cap or cannot be parsed safely as JSON. |
| `RELEASE_STATE_NOT_HELD` / `PROMOTION_STATE_NOT_HELD` | The fixture is not explicitly unreleased and promotion-ineligible. |
| `ERROR`-class CLI failure | The fixture could not be safely loaded or checked. |

Finding paths identify the field but never print its value.

[Back to top](#top)

---

## Validation

Accepted command:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m unittest discover \
  --start-directory tests/domains/fauna \
  --pattern 'test_fauna_smoke.py' \
  --verbose
```

Accepted profile:

- one synthetic positive fixture;
- five synthetic fail-closed fixtures;
- seven deterministic standard-library tests;
- explicit socket and URL-opening denial in the test boundary;
- no real taxon, occurrence, place, live URL destination, private-land clue, or usable coordinate;
- proof and release-dry-run jobs unchanged and held; and
- no contract, schema, policy, source, lifecycle, proof, release, or public-surface mutation.

This command is not an `OccurrencePublic` validator, schema promotion, source-admission check, policy-engine evaluation, geoprivacy transform verifier, evidence/proof closure check, release gate, promotion path, or publication path.

[Back to top](#top)

---

## Review checklist

- [ ] Validator rules remain limited to the declared synthetic fixture profile.
- [ ] Sensitive taxa and exact or reverse-engineerable location details fail closed.
- [ ] Location aliases and encoded free-form clues are covered by deterministic negative tests.
- [ ] Finding output reports paths and codes without printing protected values.
- [ ] Evidence, review, policy, release, rollback, and correction state remain explicit.
- [ ] Map, tile, search, graph, export, Focus Mode, and AI surfaces gain no authority.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, review, release, publication, or Directory Rules approval.
- [ ] Tests use only public-safe synthetic fixtures and remain no-network.
- [ ] Executable claims are backed by current repository evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-25 |
| Review state | Bounded synthetic fixture-safety hardening validated locally; human review and repository-native CI pending. |
| Current accepted scope | One valid and five invalid fixtures; seven deterministic tests; fixture-only validator. |
| Next smallest safe change | Review the focused hardening diff and keep production schema, source, policy, evidence, proof, release, promotion, and publication work separate. |
