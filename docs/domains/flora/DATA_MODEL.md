# Flora Data Model (Domain-Level)

## Object families
| Object | Purpose |
| --- | --- |
| `FloraSourceDescriptor` | Defines source role, rights, cadence, and sensitivity constraints. |
| `FloraTaxon` | Stable taxon identity with accepted name and crosswalk references. |
| `TaxonCrosswalk` | Links raw names/IDs to normalized taxon identifiers. |
| `OccurrenceEvidenceObject` | Source-traceable plant occurrence support. |
| `SpecimenRecord` | Herbarium/institutional specimen context and uncertainty. |
| `StatusAssertion` | Jurisdiction-scoped status claims with as-of dates. |
| `VegetationProduct` | Derived vegetation/phenology/index artifacts and uncertainty metadata. |
| `SensitivityTransformReceipt` | Proof of redaction/generalization for public-safe output. |
| `EvidenceBundle` | Resolved evidence package for claims and UI payloads. |
| `DecisionEnvelope` | Finite decision outcomes (`ANSWER`, `ABSTAIN`, `DENY`, `ERROR`). |
| `ReleaseManifest` | Promotion-time artifact inventory and rollback target. |

## Modeling rules
- Taxon identity, occurrence evidence, and derived products must remain distinct object families.
- Time fields must separate event time, retrieval time, and publication time.
- Geometry precision and uncertainty are explicit, never implied.
- Public-safe derivatives require transform receipts when precision is reduced.
