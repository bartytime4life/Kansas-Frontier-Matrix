# Heritage Sources and Source-Role Discipline

Scope: lane-specific source-role semantics and minimum evidence handling expectations for heritage materials.

## Status posture

- **CONFIRMED:** heritage lane must preserve documentary context, provenance, and source-role distinctions.
- **INFERRED:** source-role tables below align with existing KFM domain and architecture docs.
- **NEEDS VERIFICATION:** exact repo path(s) for machine-enforced source-role validation.

## Source-role matrix

| Source role | Allowed claims in heritage lane | Not allowed without escalation |
|---|---|---|
| Documentary / archival | “Source X records Y at locator Z.” | Flattening archival record into unsupported contemporary fact claims. |
| Community-contributed | “Contributor report states Y, pending corroboration/review.” | Treating single contribution as authoritative heritage fact. |
| Statutory / administrative | “Registry/designation contains Y under authority A.” | Conflating legal designation with full historical narrative certainty. |
| Direct observational / field | “Steward field observation records condition/time/place under protocol P.” | Publishing precise sensitive locations without rights/sensitivity clearance. |
| Modeled / derived | “Derived output summarizes source corpus under method M.” | Presenting OCR/extraction/summaries as if they were primary records. |
| Mirror / discovery service | “Mirror index points to origin source at locator L.” | Using mirror content as final authority when origin records are available. |

## Representative source families (current lane context)

| Source family | Role tendency | Lane handling note |
|---|---|---|
| Kansas Historical Society / Kansas Memory | Documentary / archival | Preserve item-level context, rights fields, and citation locators. |
| Chronicling America / newspaper corpora | Documentary / archival + mirror | Treat OCR as derived convenience; keep issue/date/page anchors. |
| Oral history programs | Documentary / archival + community-contributed | Keep transcript/audio identity aligned and quote-safe. |
| Heritage registers | Statutory / administrative | Keep designation scope separate from interpretation claims. |
| Local archive mirrors | Mirror / discovery service | Use for discovery, then resolve to origin authority when possible. |

## Intake checklist for source notes

- Source role assigned.
- Origin authority and mirror status recorded.
- Quote-safe locator recorded (page/timecode/item-id/etc.).
- Rights/reuse/quote constraints attached.
- Sensitivity class assigned.
- Claim extraction status marked as derived where applicable.

## Open unknowns

- **UNKNOWN:** complete machine-readable source-role enum currently enforced in this repo.
- **NEEDS VERIFICATION:** source registry completeness for heritage families.
- **NEEDS VERIFICATION:** test fixtures that prove mirror-vs-origin handling behavior.

