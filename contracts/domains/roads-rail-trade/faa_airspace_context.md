<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/transport/faa-airspace-context
title: FAA airspace and aviation context profile
type: contract
version: v0.2
status: proposed
owners: ["@bartytime4life"]
created: 2026-10-22
updated: 2026-10-24
owning_root: contracts/
responsibility: Meaning and display limits of the Kansas airspace, airport and airway context product.
truth_posture: PROPOSED profile; implemented pipeline and Site display context; no KFM release.
policy_label: public
[/KFM_META_BLOCK_V2] -->

# FAA airspace and aviation context profile

`kfm.aviation-kansas-context/v2` is **external display context**
(`evidence_role: EXTERNAL_CONTEXT_ONLY`), the same role the Site gives NOAA
radar or basemap carriers. It is not a KFM-released record, EvidenceBundle or
reportable claim, and it does not replace or advance the held APT candidate in
`faa_airport_candidate.md`. That lane, its release profile requirement and its
public hold decision are unchanged.

Machine shape: `schemas/contracts/v1/domains/roads-rail-trade/faa_airspace_context.schema.json`.
Producer: `pipelines/domains/roads-rail-trade/faa_airspace.py`.
Consumer: the Site specialty layer (`apps/site/source/app/aviation-*.ts`).

## Edition and identity

One product binds exactly one FAA NASR 28-day cycle. `valid_from` is the cycle
effective date and `valid_to_exclusive` is 28 days later. Airspace, airport and
airway inputs must carry the same cycle or the run fails. The consumer reports
`PREVIEW` before `valid_from` and `EXPIRED` from `valid_to_exclusive`; a cached
cycle is never presented as current outside its window. `source` records each
upstream package name, version and npm integrity plus SHA-256 digests of the
three data files. `product_id` seals the whole payload (RFC 8785 canonical JSON).
A volume `id` is a digest of its type, identifiers, limits and rings, so any
boundary or limit change yields a new identity.

## Vertical semantics

Every limit keeps its source reference: `SFC` (value 0), `AGL` or `MSL`, in
feet. `inclusive: false` marks "up to but not including" (for example, Class E
and MOA ceilings below FL180). No AGL value is converted to MSL. A
`ground_reference` (associated airport elevation for Class B/C/D/E2–E4,
otherwise the nearest open non-heliport facility, public or private use, with
its distance) exists only so a
display can draw heights above ground; consumers must label official limits
from `floor`/`ceiling`, never from drawn heights.

Class A is carried as one region-level bound pair. ARTCC strata are excluded.
Features are kept whole when their envelope touches the region
(-102.3, 36.7, -94.3, 40.3); nothing is clipped.

## Airports and airways

Airports are every open NASR facility in the region, public and private use,
each with a `use` flag (`PUBLIC` or `PRIVATE`), runway end points, surface,
lighting, CTAF and the ASOS/AWOS type parsed from the frequency use field;
`airport_counts` reports both totals. Frequency remarks, contacts and
owner/manager names are not projected. A private-use facility requires the
owner's permission to use; listing it grants nothing. Heliports are listed but
never used as nearest-ground anchors, because their published elevation can be
a rooftop. v2 replaced v1's `withheld.private_use_airports` count (v1 projected
public-use facilities only) on owner direction, 2026-10-24. Airway segments
(Victor, Jet, RNAV T and Q) touching the region carry the leg's MEA and MAA
from its first waypoint.

## Drone and manned-flight rules

Rules are not stored in the product. The Site derives them from type and
limits and cites 14 CFR / 49 U.S.C. text: restricted and prohibited areas
reaching below 400 ft AGL need agency permission (107.45); controlled airspace
reaching the surface needs ATC authorization (107.41, 44809(a)(5)); otherwise
Class G permits flight to 400 ft AGL (107.51(b)). UAS Facility Map ceilings,
TFRs and NOTAM activation are absent, so a derived rule is guidance context
only.

## Not claimed

No navigation, flight-planning, LAANC, current-activation, traffic-count,
aircraft-identity or legal-advice claim arises from this profile. Live
positions from public receiver networks (adsb.lol, adsb.fi) are Site display
context only, attributed per provider terms: never ingested, stored or admitted
as evidence; OpenSky stays denied
(`connectors/faa/capture.py:surveillance_decision`).
