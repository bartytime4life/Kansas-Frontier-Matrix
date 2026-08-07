<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/web-delta-profile
title: License-Respectful Web Delta Profile
type: semantic-contract; source-event-profile; pre-raw
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-network; non-operational
owners: OWNER_TBD — Source steward · Rights steward · Contract steward · Schema steward · Validation steward
created: 2026-08-07
updated: 2026-08-07
policy_label: internal; source-edge; web-delta; license-aware; fixture-only; no-authority
related:
  - ./source_event_envelope.md
  - ./source_activation_decision.md
  - ../../schemas/contracts/v1/source/web_delta_profile.schema.json
  - ../../fixtures/contracts/v1/source/web_delta_profile/cases-*.json
  - ../../tools/validators/validate_web_delta_profile.py
  - ../../tests/validators/test_validate_web_delta_profile.py
  - ../../docs/intake/exploratory/new-ideas-12-29-25-web-delta-source-map.md
tags: [kfm, web-delta, source-event, license, conditional-get, metadata-only, heartbeat, deterministic, fixture-first]
notes:
  - "Adapts the license-respectful Web-to-Typed-CloudEvents pattern from New Ideas 12-29-2025.docx.pdf."
  - "Reuses SourceEventEnvelopeCandidate instead of creating a parallel event schema, queue, pipeline root, or source authority."
  - "No live page is fetched, parsed, stored, cataloged, graphed, released, or published by this profile."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# License-Respectful Web Delta Profile

> A closed, fixture-only payload profile for representing a possible change on a human-readable web source inside the existing `SourceEventEnvelopeCandidate`, while keeping unknown or restrictive license posture metadata-only and fail-closed.

## Status and authority boundary

| Field | Value |
|---|---|
| Contract state | `PROPOSED` / fixture-first / no-network |
| Owning semantic lane | `contracts/source/` |
| Base object | `SourceEventEnvelopeCandidate` |
| Machine profile | `schemas/contracts/v1/source/web_delta_profile.schema.json` |
| Execution mode | Fixed to `FIXTURE_ONLY` by the base envelope |
| CloudEvents posture | Core-shaped base attributes only; no conformance claim |
| Source activation, RAW write, release, public use | Denied |

This profile implements the smallest dependency-closed part of the attached pattern: a deterministic envelope profile, explicit HTTP change state, source-family schema reference, content digest bindings, license-aware payload mode, no-change heartbeat semantics, exact positive/negative fixtures, and no-network validation.

It does **not** implement HTTP fetching, conditional-request storage, JSON-LD/Microdata/RDFa/HTML extraction, RFC 6902 patch production, live source configuration, queues, connectors, policy execution, signing, attestations, STAC/DCAT/PROV emission, graph mutation, Story Nodes, release, or publication.

## Directory Rules basis

The accepted Directory Governance Standard v2 routes each artifact by responsibility:

| Responsibility | Home |
|---|---|
| Human-readable source-profile meaning | `contracts/source/web_delta_profile.md` |
| Machine shape of profile attributes | `schemas/contracts/v1/source/web_delta_profile.schema.json` |
| Synthetic conformance records | `fixtures/contracts/v1/source/web_delta_profile/cases-*.json` |
| Reusable deterministic validation | `tools/validators/validate_web_delta_profile.py` |
| Enforceability proof | `tests/validators/test_validate_web_delta_profile.py` |
| Hosted orchestration | `.github/workflows/source-web-delta-profile.yml` |
| Source adaptation record | `docs/intake/exploratory/new-ideas-12-29-25-web-delta-source-map.md` |
| AI authoring provenance | `data/receipts/generated/genrec-source-web-delta-profile-20260807.json` |

No new root or parallel source, schema, policy, receipt, proof, catalog, release, or publication authority is created.

## Base-object reuse

The profile is intentionally an extension of the existing source-edge candidate:

```text
SourceDescriptor reference
  -> SourceEventEnvelopeCandidate
       -> payload.attributes validated as kfm.web_delta.v1
       -> NO_ACTION | PROPOSE_SOURCE_ADMISSION | PROPOSE_QUARANTINE
       -> later independent SourceActivationDecision review, if any
```

The base envelope continues to own deterministic event identity, RFC 8785/JCS payload hashing, source-role reference binding, event timing, finite source-edge routing, and explicit no-authority flags. This profile cannot weaken those checks.

## Profile fields

All fields live inside `payload.attributes`; values remain scalar because the base candidate deliberately admits a bounded flat attribute map.

| Field group | Required meaning |
|---|---|
| Identity | `web.profile`, canonical HTTPS URL, source pointer, source-family schema reference, canonicalizer version |
| HTTP state | Status `200` or `304`, ETag/Last-Modified presence flags |
| Extraction | `jsonld`, `microdata`, `rdfa`, `heuristic_tables`, or `none` for a 304 heartbeat |
| Rights | License state: `permissive`, `restrictive`, `ambiguous`, or `unknown` |
| Payload | `contentful`, `metadata_only`, or `heartbeat` |
| Change | `created`, `updated`, or `unchanged`; severity `none`, `low`, `medium`, or `high` |
| Integrity | Raw, previous, canonical-new, diff, and manifest SHA-256 references as applicable |
| Disclosure | Sorted `notice_fields` for metadata-only records; no contentful canonical or diff digest |
| Transform trace | Nonnegative lossy-transform count and an explicit reason when greater than zero |

The profile stores no extracted page values. Digests and field names are process metadata, not evidence that a web claim is true or reusable.

## Finite behavior

| Source condition | Required profile behavior | Base routing |
|---|---|---|
| HTTP `304` with a validator | `heartbeat`, `unchanged`, severity `none`, no new raw/canonical/diff digest | `NO_ACTION` with `HTTP_NOT_MODIFIED` and `NO_MATERIAL_CHANGE` |
| HTTP `200`, permissive license, changed canonical object | `contentful`, digest-bound raw/canonical/diff/manifest, review required | `PROPOSE_SOURCE_ADMISSION` |
| HTTP `200`, restrictive license | `metadata_only`; field names and pointer only | `PROPOSE_QUARANTINE` |
| HTTP `200`, ambiguous or unknown license | `metadata_only`; rights remain conflicted or unknown | `PROPOSE_QUARANTINE` plus `RIGHTS_UNRESOLVED` |
| Invalid URL, digest, binding, routing, or disclosure state | Fail closed with stable finding codes | No operational transition |

A schema-valid or validator-passing record remains a proposal for later review. It does not activate the source, admit bytes to RAW, resolve evidence, decide rights, authorize reuse, or create a release.

## Semantic invariants

The validator enforces that:

1. the complete base `SourceEventEnvelopeCandidate` passes first;
2. the canonical URL, source pointer, and base subject reference are identical;
3. only safe HTTPS URLs without credentials, fragments, localhost, or unsafe literal addresses are admitted;
4. ETag and Last-Modified presence flags match the base subject;
5. license state and base rights state agree;
6. all non-null digests are non-placeholder SHA-256 values;
7. a `304` is a no-action heartbeat and carries no new content digest;
8. contentful events require a permissive license, canonical/diff integrity, policy/evidence references, and review routing;
9. restrictive, ambiguous, and unknown licenses remain metadata-only and quarantined;
10. metadata-only records contain sorted field names and no canonical-new or diff digest;
11. created records have no prior canonical reference and updated records do;
12. lossy transforms are visible through an explicit reason code;
13. diagnostics contain stable codes and paths rather than source values; and
14. validation performs no network, queue, source, lifecycle, release, or publication mutation.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_web_delta_profile.py' \
  --verbose

KFM_NO_NETWORK=1 \
python tools/validators/validate_web_delta_profile.py --fixtures
```

A green result proves only the bounded synthetic profile, exact fixture polarity, base-envelope integrity, and no-network boundary.

## Compatibility and future work

A later operational profile requires separate review for:

- source-specific extraction schemas and stable IDs;
- actual conditional GET and raw-capture receipts;
- deterministic patch generation and materiality assessment;
- source rights and license policy execution;
- signed manifests and attestations;
- source activation and lifecycle persistence;
- catalog, graph, API, MapLibre, and correction propagation; and
- replay, retention, observability, rollback, and incident handling.

Do not activate those capabilities by editing this fixture profile in place.

## Rollback

Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the bounded feature commit or merge commit. No live source, lifecycle record, policy decision, evidence object, queue, database, cache, release, deployment, or public artifact requires restoration.

<p align="right"><a href="#top">Back to top</a></p>
