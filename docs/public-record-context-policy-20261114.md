# Public records as context: November 14, 2026 correction

## Decision

Public registries and public-domain sources are eligible KFM sources. A public
administrative reference, contract number, program payment rate or expiration
date is **not automatically sensitive**. Free text is not automatically
ineligible either. Assess the information and intended use, not merely the
field name or its administrative origin.

Publicly accessible is not the same as legally public domain or unrestricted
reuse. Preserve attribution, source dates, source access restrictions, applicable
terms and ordinary evidence/admission controls. This change does not confer a
license on any source, add arbitrary external URLs, or admit public records as
verified KFM evidence.

## WIHA correction

The former `CONTRACTID`/`NOTES` exclusions in PRs
[#5835](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5835) and
[#5837](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5837), mirrored
by [#5838](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5838) and
recorded by [#5839](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5839),
were conservative project choices, not evidence that KDWP declared those
administrative details confidential. This decision supersedes the blanket
exclusion, without erasing that release history or claiming a legal violation.

The fixed [KDWP public WIHA layer](https://services1.arcgis.com/q2CglofYX6ACNEeu/arcgis/rest/services/24_25_7_29/FeatureServer/0)
now supplies a bounded `contractReference` and `notes`, alongside existing tract
fields. Display them as **Public contract reference** and **KDWP public note**,
not as verified owner identity, property ownership or permission to enter land.
`notesStatus` distinguishes missing, shortened and review-held notes. Notes are
limited to 240 displayed characters; the full incoming value is screened first.
Notes over 4096 input characters are held with a size-limit status rather than
running unbounded pattern matching.
Existing KDWP source attribution, retrieval time and `EXTERNAL_CONTEXT_ONLY`
role remain. No owner lookup, cross-registry join or movement-history feature is
introduced.

## Anti-doxing and living-person tracking remain out of scope

Do not use public records to expose private-person contact details, compile
home/family dossiers, infer a person's whereabouts, follow a living person's
movements or join tract references to personal identities for targeting.
Public accessibility alone does not remove those risks.

This WIHA adapter uses explicit requested/output fields. Unexpected owner,
phone, email and address fields are discarded, even if the provider returns
them. Query parameters cannot select arbitrary providers, fields, identities or
history. Public tract polygons remain, because program access geography is not
itself a person's location history.

The shared projection screens the complete note and each species field before
shortening. Screening normalizes common Unicode and obfuscated-contact forms;
the display retains the provider's bounded text. Detected personal contact,
identifier, residence and movement details hold the whole affected field.
Probable names with surname, possessive or legal-description context and family
residence details still need review. Ownership/payment wording, billing words,
marking instructions and geographic names alone do not establish a personal
target. Historical-reference handling is local to that reference; it does not
exempt a different personal detail elsewhere in the note. Wildlife observations
are distinct from a person's last-seen location.

County output is limited to the canonical 105 Kansas names already in the
application's county inventory. All five species slots independently use the
same bounded contact/identifier/residence/tracking screen, with basic
species-label checks. A name-like biological label (for example Ross's goose
or Virginia rail) requires additional person-role or tract context before
a name guess can hold it. Unfamiliar harmless labels remain eligible because
the source supplies no controlled taxonomy; an unmarked bare personal name in
such a field remains semantically ambiguous. `fieldsStatus` exposes omitted-field review status without copying
their raw values. The route derives names only from that projected county and
does not copy original county/species strings around the screen. GeoJSON,
drawer/report attributes and automatically derived assistant summaries consume
this projection. Ordinary WIHA assistant summaries do not include note text.

Opaque numeric administrative references are not automatically phones. A
reference that duplicates a detected held phone in any of the selected note,
county or species fields is instead held for review. Payment amounts, contract references and dates remain eligible.
Unverified contact text stays review-held even if a note calls it a public
office contact; that assertion cannot authenticate a contact's provenance.

These rules supersede PR #5852's unconditional given-name/ownership holds. Its
reported 21-of-823 live-note result is historical contributor evidence, not an
independent acceptance result for this candidate. Synthetic regressions cover
public payment/expiry text and identifying fragments across API, GeoJSON,
report and assistant-prompt projections. No real personal notes are included.
The heuristics are defense in depth, not exhaustive detection or a legal
classification: uncommon names, indirect inferences and unusual encodings may
still require record-specific review. No live-provider cleanliness, rendered
browser acceptance, actual-model behavior or public deployment is established
by these source-level checks.

## Publication and scope

This source change does not deploy or backfill anything. Verify the current
provider item/service usage terms and current branch/runtime before publication;
a blank copyright field or a successful public query is not a license grant.
Read-only metadata on 2026-11-14 identified publicly shared ArcGIS item
`5fa91f6851ba4ac996f1be92d9b6b152` (2026–2027 WIHA Access), with blank item
license/attribution and service copyright fields. [ArcGIS terms](https://doc.esri.com/en/arcgis-online/latest/reference/terms-of-use.html)
describe public sharing as granting reuse subject to supplied constraints; this is not a
public-domain determination. Confirm any parent-map terms and authoritative
attribution requirements before unrestricted/commercial publication claims.
KDWP's indexed photo/graphics/logo restriction is separate from administrative
record facts. Current KDWP page retrieval was blocked during that review, so
its continuing scope was not freshly established. No new publication right is
conferred by this patch.
Use a reviewed source change if a later schema or terms change affects admission.

The correction applies to the hosted WIHA adapter. It does not silently replace
monorepo governance scaffolds, remove NPS provider restriction flags, change
Tribal/cultural-site handling, alter DNA/living-person review lanes, or open a
general-purpose data upload/import path. Broader registry additions still need
source-specific provenance, purpose and field review, not a blanket presumption
that all public facts are forbidden or that all public data are unrestricted.

## Validation and rollback

Synthetic-only tests cover permitted administrative notes, missing/long notes,
obvious personal-data indicators, field projection, drawer visibility, paging,
geometry, attribution and rejection of arbitrary person/provider queries.
Revert the source patch to roll back. No database migration or data deletion is
part of this change.
