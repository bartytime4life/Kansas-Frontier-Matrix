# Heritage Rights and Sensitivity Rules

Scope: publication and review rules for copyright/reuse, quote safety, culturally sensitive material, and exact-location exposure in the heritage lane.

## Rights and reuse controls

| Control area | Heritage-lane rule |
|---|---|
| Copyright / reuse | Record rights posture before extraction or publication; unresolved rights fails closed. |
| Redistribution limits | Respect item-level or collection-level restrictions; derivative publication may be narrower than access rights. |
| Quote safety | Quotes require locator trace and policy-safe excerpt behavior. |
| Excerpt policy | Prefer minimal excerpts tied to source context over decontextualized copy blocks. |
| Derivative summaries | Must stay linked to inspectable evidence and marked as derived. |

## Sensitivity controls

| Sensitivity class | Typical handling |
|---|---|
| Culturally sensitive material | Steward review required before publication; default to restricted or withheld if unresolved. |
| Exact-location-sensitive sites | Generalize geography for public outputs; precise geometry stays steward-only or withheld. |
| Living-person-linked records | Narrow place/time and personal detail by default; no direct public precision release. |
| Burial / memorial precision | Treat plot/row exactness as restricted unless explicit policy basis permits release. |

## Publication precision policy

- `public_safe`: generalized, non-reidentifying representation only.
- `generalized`: visible narrowing (place/time/detail) with explanation.
- `steward_only`: precise or sensitive view restricted to authorized reviewers.
- `restricted_precise`: exact detail retained internally under governance.
- `withheld`: no publication; may expose only withholding rationale.

## Steward review requirements

Minimum steward review triggers:

1. unresolved rights or derivative-use ambiguity
2. culturally sensitive context uncertainty
3. exact-location exposure risk
4. living-person or descendant risk
5. contested interpretation with policy impact

## Public-safe vs steward-only outputs

| Field type | Public-safe default | Steward-only allowance |
|---|---|---|
| Place | County/state/country or coarse bucket | Exact site/address/plot where policy allows |
| Time | Year or bounded range | Exact dates/timestamps where policy allows |
| Personal detail | Minimal context | Extended detail under controlled access |
| Source excerpt | Short, contextualized, policy-safe excerpt | Broader excerpt where rights permit |

## Unknowns and verification flags

- **NEEDS VERIFICATION:** quote-length enforcement location in policy/tests.
- **UNKNOWN:** complete steward authorization workflow implementation path.
- **NEEDS VERIFICATION:** established rights vocabulary and enum set in machine contracts.

