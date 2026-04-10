# Heritage Entity and Evidence Model

Scope: domain entities, evidence objects, and trust-critical object families used to keep heritage claims inspectable and correction-ready.

## Entity families (domain-facing)

| Entity family | Role in heritage lane |
|---|---|
| Place / site / district / route | Spatial anchor for documentary records and derived interpretations. |
| Collection | Archival grouping and provenance container for documentary materials. |
| Narrative object | Structured claim-bearing narrative unit with explicit evidence linkage. |
| Documentary evidence object | Source-native artifact or faithful representation with locator and rights context. |
| Event | Time-scoped occurrence tied to evidence and uncertainty posture. |
| Claim / assertion | Interpreted statement that must remain evidence-linked and reviewable. |
| Governance object | Policy/review decision with auditable rationale and scope. |
| Source descriptor | Intake boundary object defining source identity and handling posture. |
| Evidence bundle | Runtime-facing support package for trust-visible surfaces. |
| Review / decision / correction objects | Lifecycle objects for approvals, denials, supersession, and withdrawal. |

## Trust artifact expectations (lane mapping)

| Artifact family | Heritage-lane status | Note |
|---|---|---|
| SourceDescriptor | INFERRED | Named consistently in architecture/contracts docs; heritage should use it explicitly. |
| IngestReceipt | INFERRED | Required to preserve intake trace for documentary sources. |
| ValidationReport | INFERRED | Needed for parse/rights/sensitivity gate visibility. |
| DatasetVersion | INFERRED | Needed to anchor released heritage derivatives. |
| CatalogClosure | INFERRED | Needed for release-scoped discoverability and lineage. |
| DecisionEnvelope | INFERRED | Needed for explicit allow/generalize/withhold decisions. |
| ReviewRecord | INFERRED | Needed for steward action trace and separation-of-duty posture. |
| ReleaseManifest / proof pack | PROPOSED | Mentioned doctrinally; exact heritage implementation path unverified. |
| EvidenceBundle | INFERRED | Trust-critical for dossier/story/focus evidence resolution. |
| RuntimeResponseEnvelope | INFERRED | Needed for finite runtime outcomes and citation-governed responses. |
| CorrectionNotice | INFERRED | Needed for supersession/withdrawal visibility across surfaces. |

## Model constraints

1. Documentary evidence objects remain distinct from derived narrative objects.
2. Claim objects must carry evidence references and confidence/uncertainty signals.
3. Governance objects must be legible at point-of-use for sensitive publication decisions.
4. Correction objects must propagate to every downstream surface that displayed superseded output.

## Open unknowns

- **UNKNOWN:** exact contract/schema file paths for all artifacts listed above.
- **NEEDS VERIFICATION:** object field-level compatibility with existing repo schemas/contracts.
- **PROPOSED:** heritage-specific object examples under `docs/domains/heritage/examples/` and schema fixtures.

