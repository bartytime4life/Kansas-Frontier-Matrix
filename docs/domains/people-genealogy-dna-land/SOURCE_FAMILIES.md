# Source Families and Role Boundaries

## Purpose
Define what each source family may support, and what it must not claim by itself.

## Families

| Family | Role key | Can support | Must not be treated as |
|---|---|---|---|
| Documentary records (vital/census/probate/court/etc.) | `people_documentary` | Person/event/place assertions with citations | Automatic canonical truth |
| Genealogy tree packages (GEDCOM/GEDZip/overlay) | `genealogy_tree` | Candidate relationships and life events | Verified relationship truth without review |
| DNA exports (match/segments/triangulation) | `dna_restricted` | Restricted hypotheses and review queues | Public-facing proof by default |
| Land instruments (deed/mortgage/lien/easement/etc.) | `land_instrument` | Time-scoped ownership-interest events | Unconditional current ownership without time context |
| Assessor/tax rolls | `assessor_tax` | Assessor facts and tax/admin context | Chain-of-title truth |
| Survey/legal-description/geometry sources | `geometry_or_description` | Spatial context and legal-description support | Boundary precision proof without role-qualified evidence |

## Required metadata (minimum)
Every admitted source should track:
- source family and role key;
- rights/terms posture;
- sensitivity label;
- jurisdiction and temporal coverage;
- citation text and retrieval/provenance hash;
- steward owner and review expectations.

## Prohibited shortcuts
- No DNA raw identifiers in public docs.
- No “owner” claim from assessor row without instrument support.
- No boundary certainty claim from map geometry alone.
