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

The notes helper holds an entire note for review when it detects common email,
formatted phone, personal-ID or explicit home-address/location-targeting
indicators. It does **not** block payment amounts, contract references or dates
merely because they are administrative. These heuristics are limited defense in
depth, not a complete detector, a legal classification or an automated finding
that someone has been doxed. Ambiguous contact-looking text can be held; names,
unusual formats and indirect inferences may evade detection. Review the specific
record and source if reported, rather than blanket-blocking its registry. No raw
held note is copied into the response or test artifacts.

## Publication and scope

This source change does not deploy or backfill anything. Verify the current
provider item/service usage terms and current branch/runtime before publication;
a blank copyright field or a successful public query is not a license grant.
The applicable item-level reuse terms have not been established by this patch.
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
