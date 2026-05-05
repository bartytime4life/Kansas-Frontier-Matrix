<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-register-fauna-geoprivacy
title: Fauna Geoprivacy and Public Geometry
type: standard
version: v1
status: draft
owners: TODO(fauna-domain-stewards)
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO(verify-public-or-restricted)
related: [docs/domains/fauna/README.md, docs/domains/fauna/VALIDATION.md]
tags: [kfm, fauna, geoprivacy, sensitivity]
notes: [Public geometry classes and fail-closed release rules for fauna lane.]
[/KFM_META_BLOCK_V2] -->

# Fauna Geoprivacy

## Default rule

If uncertainty exists around rights, species sensitivity, or publication policy, **do not publish exact geometry**.

## Public geometry classes

| Class | Description | Public exposure |
|---|---|---|
| `public_exact_allowed` | Exact coordinates permitted after full checks | Exact allowed |
| `public_generalized` | Precision reduced to approved geography | Generalized only |
| `restricted_precise` | Exact record held in restricted channels | No public geometry |
| `embargoed` | Temporarily blocked until conditions met | No public geometry |
| `steward_review_required` | Requires explicit steward decision | No publish until decision |
| `quarantine` | Missing/conflicting policy inputs | No publish |

## Mandatory redaction receipt fields

- Subject record key/hash
- Geometry transform class and parameters
- Before/after digest
- Policy version used
- Actor/run id
- Timestamp
- Evidence reference(s)

## Leak vectors to test

- API payloads and downloadable exports
- Vector/raster tiles and style expressions
- Popup text and Evidence Drawer snippets
- Search index and autocomplete payloads
- Graph projections and relationship endpoints
- Screenshots/docs/examples used in public channels

## Decision outcomes

| Condition | Outcome |
|---|---|
| Sensitive record + exact geometry requested | `DENY` |
| Unknown rights/sensitivity | `HOLD` or `QUARANTINE` |
| Safe generalized representation validated | `PASS` |
| Evidence unresolved for requested claim | `ABSTAIN` |

