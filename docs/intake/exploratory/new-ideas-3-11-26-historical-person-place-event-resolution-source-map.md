<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/new-ideas-3-11-26-historical-person-place-event-resolution
title: New Ideas 3-11-26 — Historical Person-Place-Event Resolution Source Map
type: exploratory-source-map
version: v0.1.0
status: implemented-as-bounded-fixture-candidate; source-not-canon
created: 2026-08-06
updated: 2026-08-06
policy_label: public; exploratory; provenance; no-publish
[/KFM_META_BLOCK_V2] -->

# New Ideas 3-11-26 — Historical Person-Place-Event Resolution Source Map

## Source-derived idea

*New Ideas 3-11-26.pdf*, pages 25–28, proposes an audit-ready historical
person-place-event scorecard:

- `+3` for an authority-ID match across sources;
- `+2` for at least three independent same-county/time source families;
- `+2` for an exact GLO township/range/section anchor;
- `-3` for strong negative evidence;
- `high` at score `>=5`, `medium` at `2..4`, and `low` below `2`;
- retained source references, rights labels, and minimal scan IDs;
- happy, conflict, and weak fixture polarities.

## Repository assay

**CONFIRMED at base `eeaafb0877c7739d8be26b85ac6fc141c1c4fde1`:**

- `docs/architecture/people-place-joins.md` already establishes event-first,
  evidence-backed, time-scoped people-place joins.
- People/DNA/Land has contract and schema responsibility lanes.
- The exact GLO/co-mention/negative-evidence scorecard was not found in the searched
  repository or open pull requests.

## Adaptations made

The implementation is deliberately narrower than the source packet:

1. **Synthetic only.** No live LCNAF, VIAF, ISNI, Wikidata, SNAC, GLO, census,
   newspaper, county-history, or archive calls.
2. **Current authority ladder preserved.** LCNAF, VIAF, ISNI, and Wikidata may earn
   the authority signal. SNAC is corroborative only and cannot become primary in this
   profile without a later accepted decision.
3. **No real geography.** `99999`, `Synthetic County`, and `T00S/R00W/S00` are
   required sentinels.
4. **No public state.** Every accepted candidate remains `not_released`,
   `promotion_eligible=false`, and `public_exposure=false`.
5. **Sensitive fields denied.** Living-person, raw-DNA, private-parcel, address, and
   coordinate fields fail closed.

## Implemented artifact set

- `contracts/domains/people-dna-land/historical_person_place_event_resolution.md`
- `schemas/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution.schema.json`
- `fixtures/contracts/v1/domains/people-dna-land/historical_person_place_event_resolution/`
- `tools/validators/validate_historical_person_place_event_resolution.py`
- `tests/validators/test_validate_historical_person_place_event_resolution.py`
- `.github/workflows/historical-person-place-event-resolution.yml`

The change does not implement a production identity resolver, live source adapters, a
canonical person store, title reasoning, public API, map layer, graph projection, release,
or publication.
