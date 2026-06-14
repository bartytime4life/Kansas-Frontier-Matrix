# Flora Geoprivacy Transformer

Status: PROPOSED implementation package README  
Owning responsibility root: `packages/`  
Requested path: `packages/domains/flora/geoprivacy_transformer/README.md`  
Domain lane: `flora`  
Package role: deterministic public-safety transform helper for Flora geometry and location-bearing payloads

---

## 1. Purpose

`geoprivacy_transformer` is the Flora domain package responsible for turning internal, sensitive, or precision-bearing Flora location information into public-safe geometry and location descriptors before any public layer, governed API payload, Evidence Drawer projection, Focus Mode answer, export, or release artifact can use it.

The package exists to prevent exact sensitive Flora locations from leaking through maps, API responses, logs, screenshots, tiles, public fixtures, generated summaries, or downstream artifacts.

It is not a source of truth. It is a deterministic transform and receipt helper that sits behind KFM evidence, policy, review, and release controls.

---

## 2. Directory placement and authority boundary

This README documents a package under the implementation responsibility root:

```text
packages/domains/flora/geoprivacy_transformer/
```

This package may contain reusable implementation code, package-local docs, and package-local helper types. It must not become a parallel authority for schemas, policy, source registries, release decisions, receipts, proofs, or lifecycle data.

Canonical homes remain separate:

| Concern | Canonical home | This package may do |
|---|---|---|
| Object meaning | `contracts/` | Import or reference semantic contracts; do not redefine them. |
| Machine-readable shape | `schemas/contracts/v1/...` | Validate against schemas; do not create a competing schema home. |
| Allow / deny / restrict / abstain policy | `policy/` | Execute or consume policy decisions; do not own policy authority. |
| Source identity, role, rights, sensitivity | `data/registry/` and policy surfaces | Consume source and sensitivity context; do not create source truth. |
| Test fixtures | `fixtures/` or `tests/fixtures/` | Use no-live-network fixtures; keep public fixtures synthetic or already public-safe. |
| Validators | `tools/validators/` and tests | Provide helper functions; repo validators remain under the validator root. |
| Receipts / proofs / release decisions | `data/receipts/`, `data/proofs/`, `release/` | Emit receipt payloads for the owning pipeline to persist; do not publish directly. |
| Public UI/API | `apps/`, `web/`, `ui/`, governed API surfaces | Return public-safe payloads only; never bypass governed interfaces. |

If this package needs a schema, policy rule, source descriptor, fixture, validator, release object, or receipt persistence location, add or update that file in the proper responsibility root rather than placing it inside this package.

---

## 3. KFM trust boundary

This package preserves the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The transformer operates only after source payloads have been admitted into a governed processing path and before public-safe candidates are promoted or served. It must never read directly from public clients, raw source systems, unpublished candidate stores, or internal canonical stores as a public shortcut.

Public clients should receive only released, public-safe artifacts through governed APIs, released tiles, catalog records, EvidenceBundle-backed payloads, and release manifests.

---

## 4. What the transformer does

The transformer accepts a Flora location-bearing candidate plus its source, sensitivity, rights, review, policy, and evidence context. It returns one finite outcome:

- `ANSWER` — a public-safe geometry or location descriptor was produced.
- `ABSTAIN` — evidence, rights, review, or sensitivity context is insufficient to transform safely.
- `DENY` — the candidate must not be publicized under the requested release profile.
- `ERROR` — the transform could not be completed because of malformed input, schema failure, missing required fields, or internal failure.

The transformer may produce:

- generalized public geometry,
- withheld geometry with a safe location descriptor,
- coarsened administrative or ecological region references,
- precision bucket metadata,
- transform reason codes,
- digest-linked geoprivacy receipts,
- review obligations for steward approval,
- denial or abstention reason codes.

The transformer must not produce:

- exact sensitive point coordinates in public payloads,
- raw internal geometry in logs or error messages,
- public tiles from unpublished candidates,
- AI-ready exact sensitive coordinates,
- policy-free release candidates,
- generalized geometry without transform lineage,
- model-generated “safe” locations without evidence and policy support.

---

## 5. Non-goals

This package does not:

1. decide whether a source is admissible;
2. decide whether rights allow redistribution;
3. replace steward review;
4. publish data;
5. write release manifests;
6. persist canonical observations;
7. create catalog records by itself;
8. replace sensitivity policy;
9. transform RAW data outside the governed lifecycle;
10. serve public API responses directly;
11. generate AI explanations as truth;
12. turn modeled habitat/range products into occurrence evidence.

---

## 6. Input contract expectations

The exact schema names are repository-dependent and must be verified against the current schema home before implementation. At minimum, a transform request should carry the following fields or resolvable references:

| Field family | Required purpose |
|---|---|
| `candidate_id` | Stable identifier for the Flora occurrence, specimen, plot, survey, or location-bearing candidate. |
| `source_id` | Source descriptor reference for role, rights, update cadence, and citation context. |
| `evidence_refs` | Evidence references that can resolve to EvidenceBundles before publication. |
| `internal_geometry_ref` | Internal geometry reference or encrypted/access-controlled geometry pointer. Public payloads must not echo it. |
| `geometry_precision` | Stated or inferred precision of the source geometry. |
| `taxon_context` | Accepted taxon, raw taxon text, status, synonym/crosswalk state, and uncertainty flags. |
| `sensitivity_context` | Rare/protected/culturally sensitive/steward-reviewed flags and source-specific controls. |
| `rights_context` | Redistribution class, license, terms, and public release eligibility. |
| `review_context` | Review record reference, steward approval state, and release scope. |
| `policy_decision` | Prior or inline policy result for the requested transform profile. |
| `release_profile` | Intended output profile, such as public web map, researcher export, steward review, or internal QA. |
| `requested_transform` | Requested transform strategy, or `auto` when policy selects the safest valid option. |
| `run_context` | Run ID, transform version, spec hash, actor/service ID, and timestamp. |

Malformed requests should return `ERROR`. Requests lacking rights, evidence, review, or sensitivity context should return `ABSTAIN` or `DENY` depending on policy.

---

## 7. Output contract expectations

A successful transform should return a public-safe envelope shaped like this at the semantic level:

```yaml
outcome: ANSWER
candidate_id: <stable candidate id>
public_geometry:
  kind: generalized | withheld | region | grid | county | huc | ecoregion | none
  geometry_ref: <public-safe geometry ref or null>
  precision_bucket: <bucket id>
  coordinate_exposure: none | generalized | public_exact_allowed
location_descriptor:
  label: <safe human-readable location label>
  basis: <county | huc | grid | ecoregion | stewardship_area | withheld>
transform:
  method: <method id>
  version: <semver or digest>
  reason_codes: [<reason code>]
  input_digest: <digest of internal input or pointer envelope>
  output_digest: <digest of public-safe output>
policy:
  decision_id: <policy decision id>
  obligations: [<required obligations>]
review:
  review_record_id: <review id or null>
  review_required: true | false
receipts:
  geoprivacy_receipt_id: <receipt id>
  run_receipt_id: <run receipt id>
```

The transformer should preserve enough lineage for a reviewer to reconstruct why the public geometry is safe without exposing the internal sensitive geometry.

---

## 8. Transform strategies

Supported strategies should be deterministic, policy-selected, and receipt-bearing.

| Strategy | Intended use | Public output |
|---|---|---|
| `pass_through_public_eligible` | Non-sensitive records explicitly approved for public exact display. | Exact or source-provided public geometry only when policy and review allow it. |
| `generalize_grid` | Sensitive or uncertain points that can safely be generalized to a grid. | Grid cell polygon or centroid-free cell identifier. |
| `generalize_county` | County-level public map or low-precision public display. | County polygon or county label. |
| `generalize_huc` | Hydrology-linked Flora context where watershed aggregation is safer and meaningful. | HUC polygon or HUC label. |
| `generalize_ecoregion` | Ecological context where ecoregion aggregation is safer and meaningful. | Ecoregion polygon or label. |
| `buffer_and_simplify` | Public-safe approximate area when buffer radius and simplification are policy-approved. | Generalized polygon with precision bucket. |
| `withhold_geometry` | Source may be described but geometry cannot be public. | No geometry; safe descriptor and reason code only. |
| `deny_publication` | Publication is not safe or not allowed. | `DENY`, no public geometry. |
| `abstain_pending_review` | Review, rights, or evidence is incomplete. | `ABSTAIN`, no public geometry. |

Do not use random jitter as a default public-safety method. Jitter can imply false precision and may be reversible if attackers compare releases. Any noise-based method requires an explicit policy rule, threat model, transform receipt, and reviewer approval.

---

## 9. Reason codes

Reason codes should be stable, machine-readable, and suitable for policy tests, release gates, and Evidence Drawer explanations.

### Deny / abstain reason codes

- `precise_sensitive_location_denied`
- `controlled_access_publication_denied`
- `unknown_rights`
- `missing_source_id`
- `missing_evidence_bundle`
- `review_required`
- `steward_review_missing`
- `public_geometry_not_generalized`
- `invalid_geometry`
- `ambiguous_taxon_identity`
- `accepted_taxon_required`
- `knowledge_character_mismatch`
- `model_as_observation`
- `public_payload_exposes_internal_ref`
- `catalog_matrix_not_closed`
- `proof_bundle_incomplete`
- `ai_missing_evidence_bundle_or_citations`

### Transform reason codes

- `public_exact_allowed_by_policy`
- `generalized_for_sensitive_flora`
- `generalized_for_coordinate_uncertainty`
- `generalized_for_license_constraint`
- `generalized_for_review_scope`
- `withheld_for_stewardship_policy`
- `withheld_for_rights_uncertainty`
- `withheld_for_cultural_sensitivity`
- `withheld_for_source_terms`
- `withheld_until_release_state_exists`

---

## 10. Precision buckets

Precision buckets should be explicit and should not overstate accuracy.

| Bucket | Meaning |
|---|---|
| `internal_exact_restricted` | Exact geometry exists but is internal only. |
| `source_exact_public_allowed` | Exact public geometry allowed by source rights, policy, and review. |
| `source_uncertain` | Source coordinates are uncertain or precision is unresolved. |
| `generalized_1km` | Public output generalized to about 1 km or an equivalent grid. |
| `generalized_5km` | Public output generalized to about 5 km or an equivalent grid. |
| `generalized_10km` | Public output generalized to about 10 km or an equivalent grid. |
| `county_level` | Public output only identifies the county. |
| `huc_level` | Public output only identifies the watershed unit. |
| `ecoregion_level` | Public output only identifies the ecological region. |
| `withheld` | No public geometry is provided. |
| `denied` | No public payload may be produced. |

The selected bucket must appear in the transform receipt.

---

## 11. Logging and error handling

The transformer must be safe by default:

- Do not log raw coordinates for sensitive or unreviewed records.
- Do not include raw geometry in exception strings.
- Do not print source-native restricted IDs into public logs.
- Do not echo internal geometry pointers into public payloads.
- Do not write rejected candidates into public fixtures.
- Do not expose before/after coordinate pairs in public QA reports.
- Use redacted diagnostic IDs and digests for debugging.
- Treat missing sensitivity context as unsafe, not as public.
- Treat missing rights context as unsafe, not as public.

Errors should return finite `ERROR` outcomes with safe reason codes and remediation hints.

---

## 12. Determinism and receipts

Every transform must be deterministic for the same input payload, transform version, policy version, review state, and release profile.

A geoprivacy receipt should record:

- `geoprivacy_receipt_id`,
- source candidate reference,
- evidence reference(s),
- transform method and version,
- policy decision ID and policy version,
- review record ID when applicable,
- input digest,
- output digest,
- public precision bucket,
- reason codes,
- actor/service ID,
- run receipt ID,
- timestamp,
- rollback target or prior release reference when applicable.

Receipt persistence belongs outside this package, under the proper receipt/proof/release responsibility root. This package should emit receipt payloads to the owning pipeline or service.

---

## 13. Integration points

Expected upstream callers:

- Flora normalization pipeline,
- Flora promotion candidate builder,
- Flora layer manifest builder,
- governed API Flora feature/detail resolver,
- Evidence Drawer payload builder,
- Focus Mode evidence preprocessor,
- release validation job,
- steward review console.

Expected downstream consumers:

- public-safe Flora layer descriptors,
- public-safe MapLibre source/layer payloads,
- EvidenceBundle projections,
- Evidence Drawer display payloads,
- ReleaseManifest support objects,
- geoprivacy receipts,
- policy and validation reports.

This package must never be called by a public client as a way to transform internal data on demand.

---

## 14. Test expectations

Minimum tests for this package:

1. sensitive exact Flora point returns `DENY` unless policy and review explicitly allow a safe transform;
2. missing rights returns `ABSTAIN` or `DENY`;
3. missing evidence reference blocks consequential publication;
4. missing review blocks review-required taxa or source classes;
5. generalized output does not include raw coordinates;
6. logs and errors do not include raw coordinates;
7. output digest changes when transform version changes;
8. same input and same transform version produce the same output digest;
9. invalid geometry returns safe `ERROR`;
10. modeled range cannot be emitted as an occurrence;
11. public fixture data remains synthetic or already public-safe;
12. generated receipt contains method, version, reason code, input digest, output digest, policy decision, and review status;
13. public layer payload contains no internal refs;
14. Focus Mode payload cannot expose exact sensitive coordinates;
15. Evidence Drawer payload can explain withholding without exposing restricted details.

Tests should run without live network access.

---

## 15. Example safe transform narrative

A rare plant occurrence enters the Flora processing lane with an exact internal coordinate and a valid EvidenceRef. The source descriptor says the record is controlled access. The sensitivity policy marks the taxon as steward-reviewed. Review has not approved public exact display.

The transformer must not emit the point. It should either generalize to an approved public region or withhold geometry entirely. It should return a finite outcome, reason codes, and a geoprivacy receipt payload. Public UI can then say that the location is withheld or generalized for stewardship and public-safety reasons without revealing the internal coordinate.

---

## 16. Implementation notes

Recommended internal module boundaries:

```text
geoprivacy_transformer/
  README.md
  __init__.py
  decision.py
  geometry.py
  precision.py
  reason_codes.py
  receipts.py
  transforms.py
  validators.py
```

These filenames are implementation suggestions, not authority roots. Keep package internals small and reversible. Promote shared helpers only when more than one domain needs them; cross-domain geoprivacy logic belongs under the lowest common implementation responsibility root, not inside Flora by convenience.

---

## 17. Rollback and correction

A transform can be corrected by issuing a new transform receipt and a superseding release candidate. Do not overwrite old receipts silently.

Rollback should use:

- prior ReleaseManifest,
- prior geoprivacy receipt,
- prior output digest,
- correction reason,
- reviewer/steward decision where required,
- stale-state rule for affected public artifacts.

If an exact sensitive location is exposed, treat it as an incident: withdraw affected artifacts, invalidate caches/tiles where possible, record the incident, notify maintainers/stewards according to policy, and publish only a corrected public-safe artifact after review.

---

## 18. Acceptance checklist

Before this package is considered ready for a PR:

- [ ] Directory placement is confirmed against current repo state.
- [ ] No schema, policy, release, source registry, receipt, or proof authority is duplicated inside the package.
- [ ] Reason codes are synchronized with policy and schema contracts.
- [ ] No-live-network tests pass.
- [ ] Synthetic fixtures cover sensitive and non-sensitive cases.
- [ ] Logs and errors are coordinate-safe.
- [ ] Transform receipts include input and output digests.
- [ ] Public payload tests prove no internal refs or exact sensitive coordinates escape.
- [ ] Evidence Drawer and Focus Mode integration tests return finite outcomes only.
- [ ] Rollback/correction behavior is documented.
- [ ] Steward review requirements are represented in tests.

---

## 19. Open verification items

- Confirm the actual package manager and package import style in the mounted repository.
- Confirm whether `packages/domains/flora/` already exists and whether this folder should be a Python package, TypeScript package, or language-neutral spec folder.
- Confirm current schema names for Flora occurrence, public-safe geometry, EvidenceBundle, DecisionEnvelope, redaction receipt, and ReleaseManifest.
- Confirm current policy engine and test runner.
- Confirm steward-approved public geometry thresholds for rare/protected/culturally sensitive Flora.
- Confirm source-specific rights for any real Flora source before activating a live connector.
- Confirm the release path for geoprivacy receipts and public-safe layer manifests.

---

## 20. Maintainer rule

When uncertain, this package must choose the safer result:

```text
ABSTAIN when evidence is insufficient.
DENY when policy, rights, sensitivity, review state, or release state blocks public output.
ERROR only for malformed input or system failure.
ANSWER only when the output is public-safe, evidence-bound, policy-supported, review-compatible, and receipt-bearing.
```

