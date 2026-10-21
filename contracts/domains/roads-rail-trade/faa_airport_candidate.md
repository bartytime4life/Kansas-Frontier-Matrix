<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/transport/faa-airport-candidate
title: FAA airport candidate profile
type: contract
version: v0.1
status: proposed
owners: ["@bartytime4life"]
created: 2026-10-21
updated: 2026-10-21
owning_root: contracts/
responsibility: Meaning and non-release constraints for FAA airport candidates.
truth_posture: PROPOSED profile; implemented private preparation only.
policy_label: public
[/KFM_META_BLOCK_V2] -->

# FAA airport candidate profile

This proposed profile specializes existing EvidenceRef and EvidenceBundle
objects. It does not define another evidence authority, source registry,
policy engine or release decision. Machine validation remains in the existing
`schemas/contracts/v1/` home; migrations describe storage rather than meaning.

Entity identity is `faa:site:<SITE_NO>:<SITE_TYPE_CODE>`. A revision additionally
binds edition and the digest of allowlisted original values. FAA location ID,
ICAO ID, IATA, registration, callsign and transponder address are distinct
namespaces. No cross-source join is asserted. Source county association is
not a Census GEOID or a point-in-polygon county assignment.

Source effective date is retained independently from retrieval, unknown source
publication time and absent KFM release time. Validity ends exclusively at
the next 28-day cycle boundary; a future effective edition is held. A prior
edition may be historical reference, never current merely because cached.
Airport `ELEV` is feet MSL, distinct from geometric/barometric aircraft altitude,
AGL and runway-end elevation. Decimal coordinates retain their original values;
the horizontal datum is unverified and blocks public map promotion.

The raw ZIP is private and may include contact data. Only APT_BASE is parsed;
contacts, personal addresses/phones and aircraft identifiers never enter this
candidate projection. Invalid rows retain allowlisted original values, their
digest, source row number and quarantine reason. Whole raw provenance stays
available privately. Duplicate entities make coverage partial; they are not
silently counted as a second facility. Open public-use nonmilitary facilities
are only public *candidates*. This boolean is neither rights clearance nor
release authorization.

Selection chain: revision ID -> EvidenceRef (`kind=record`) -> existing
EvidenceBundle shape -> source citation and original-capture digest. Bundles
remain quarantine. Rendering, a SQL row, or a passing schema does not resolve
evidence under policy. The existing release policy and verification-history
replay must gain an independently reviewed aviation profile before any public
ANSWER, report, export, embedding or AI context can carry these records.

Follow-on logical entities (not approved new table names):

| Entity | Required separation and current state |
|---|---|
| Source/product/version/retrieval | FAA APT exact edition and digest implemented; ADDS exact items held |
| Airport revision | Implemented candidate; no deletion of prior editions |
| Runway/nav/fix/airspace/route | Separate product/schema/vertical reference; not yet implemented |
| Aircraft metadata | Identifier validity and provider-specific rights; disabled |
| Surveillance observation | observation time, last contact, capture time, position source, separate altitude kinds/units; disabled |
| Trajectory segment | derived from observations, method/version/gaps and uncertain continuity; disabled |
| Coverage/aggregate | interval, area, receiver support, numerator/denominator, incomplete tracks; disabled |
| Release/correction/withdrawal | Existing KFM release authority, no new approval store; held |

Observation tools must distinguish no returned observations from no aircraft
activity. No ownership, identity, mission, emergency, origin/destination, noise,
emissions or causal claims arise from this profile. Typed read-only queries use
fixed field allowlists, bounded county/edition/area/rows and prepared parameters;
model-generated SQL, writes, arbitrary upstreams and filesystem reads are denied.

Recovery preserves immutable captures and revision identities. A correction
creates a new candidate/revision and supersession lineage; no candidate update
may mutate an already cited revision. Withdrawal is enforced by existing release
bindings, not deleting source evidence. This first slice creates no released
binding and therefore cannot perform a public correction or withdrawal.
