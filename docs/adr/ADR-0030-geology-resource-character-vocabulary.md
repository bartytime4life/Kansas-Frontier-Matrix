<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0030
title: Define the minimum Geology resource-character vocabulary
type: architecture-decision-record
version: v0.1
status: proposed
owners:
  - Architecture steward
  - Geology domain steward
  - Natural-resources steward
  - Source steward
  - Evidence steward
  - Schema steward
created: 2026-08-03
updated: 2026-08-03
policy_label: public; proposed; documentation-only; non-authoritative
truth_posture: cite-or-abstain
responsibility_root: docs/
supersedes: []
superseded_by: []
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - contracts/domains/geology/MineralOccurrence.md
  - contracts/domains/geology/ResourceDeposit.md
  - contracts/domains/geology/ResourceEstimate.md
  - schemas/contracts/v1/domains/geology/mineral_occurrence.schema.json
  - schemas/contracts/v1/domains/geology/resource_deposit.schema.json
  - schemas/contracts/v1/domains/geology/resource_estimate.schema.json
  - docs/domains/geology/SOURCE_ROLE_MATRIX.md
  - docs/intake/exploratory/geology-natural-resources-architecture-source-map.md
  - fixtures/domains/geology/resource_class/README.md
  - tools/validators/domains/geology/validate_resource_class_distinction.py
tags: [kfm, adr, geology, natural-resources, resource-character, vocabulary, anti-collapse, source-role, evidence, schema]
notes:
  - "This record is proposed and non-binding. File presence or merge does not accept the decision."
  - "The vocabulary identifies claim character; it does not certify any occurrence, deposit, estimate, reserve, production, permit, or modeled potential."
  - "This proposal admits no source, changes no policy, activates no pipeline, and authorizes no release or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0030: Define the minimum Geology resource-character vocabulary

| Field | Value |
| --- | --- |
| Status | `proposed` — not binding |
| Date | 2026-08-03 |
| Decision scope | Minimum cross-contract vocabulary and anti-collapse semantics |
| Directory Rules trigger | Non-§2.4 cross-component semantic decision; ADR used to preserve rationale before schema hardening |
| Affected implementation | Follow-on only; this proposal changes documentation and provenance records only |
| Acceptance authority | Explicit review by the named architecture, domain, source, evidence, and schema stewards |

> [!IMPORTANT]
> This ADR is a proposal. It defines the decision that reviewers are being asked
> to accept; it does not itself make the vocabulary canonical, admit a source,
> validate a real-world resource claim, alter policy, or authorize promotion,
> release, or publication.

## 1. Context

Current repository evidence already carries the load-bearing distinction:

- `MineralOccurrence` is a source-supported reported presence, not a deposit or estimate.
- `ResourceDeposit` is a named or delineated body with characterization, not a quantity, reserve, permit, or production fact.
- `ResourceEstimate` is a modeled or compiled quantity/classification claim with method and assumptions, not direct observation and not a reserve by default.
- source roles (`observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic`) describe how evidence was produced; they are not resource classes.
- permit, production, reserve, and modeled-potential claims must not be relabeled as occurrence, deposit, or estimate truth.

Merged PR [#1926](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/1926)
made a narrow synthetic fixture profile executable. Its profile-local
`resource_character` values are `MINERAL_OCCURRENCE`, `RESOURCE_DEPOSIT`, and
`RESOURCE_ESTIMATE`. The validator deliberately rejects reserve, permit,
production, modeled-potential, direct-observation, and sensitive-location
collapse. It explicitly does not declare its vocabulary canonical.

The three paired JSON Schemas remain permissive scaffolds with empty
`properties`, `additionalProperties: true`, and lower-case `x-kfm.contract_doc`
pointers that do not resolve to the tracked PascalCase contract paths. The
contracts also contain broader proposed class lists, but those lists do not
settle a shared machine vocabulary or admit a record family.

Without one reviewed vocabulary, a later schema or consumer could independently
interpret `reserve_estimate`, `model_derived_estimate`, permit status, production
figures, or prospectivity as stronger resource truth. The decision must separate
claim character, source role, object identity, and source-native classification
before schemas are tightened.

## 2. Decision

If accepted, KFM will use `resource_character` as the machine field that states
the kind of natural-resource claim represented by a record. Its minimum
canonical token set will be:

```text
MINERAL_OCCURRENCE
RESOURCE_DEPOSIT
RESOURCE_ESTIMATE
RESERVE
PRODUCTION
PERMIT
MODELED_POTENTIAL
```

The vocabulary is intentionally small. It prevents semantic collapse; it is not
a scientific reporting standard, reserve code, legal status code, commodity
taxonomy, economic classification, source role, or release decision.

### 2.1 Four orthogonal axes

Every future schema or validator using this decision must keep these axes
separate:

| Axis | Question answered | Examples |
| --- | --- | --- |
| `resource_character` | What kind of claim is this? | `RESOURCE_DEPOSIT`, `PERMIT` |
| `object_family` | Which semantic contract owns the record? | `MineralOccurrence`, `ResourceEstimate` |
| `source_role` | How was the supporting knowledge produced? | `observed`, `modeled`, `regulatory` |
| `classification_scheme_ref` | Which source-native scientific, economic, or legal scheme defines a class? | A versioned scheme reference; no scheme is adopted here |

`observed` therefore remains a source role, not an eighth resource-character
token. Observation-level mineral presence is represented by
`resource_character: MINERAL_OCCURRENCE` and an evidence-supported source role,
commonly `observed`. An aggregate or administrative occurrence source may still
support a `MINERAL_OCCURRENCE` record while preserving its non-observed role.

### 2.2 Minimum meanings and non-implications

| Concept | Canonical representation | Minimum meaning | Must not imply |
| --- | --- | --- | --- |
| Observation / occurrence | `MINERAL_OCCURRENCE` with `object_family: MineralOccurrence`; `source_role: observed` only when direct evidence supports it | Reported mineral or material presence | Deposit identity, quantity, reserve, economic viability, permit, production, or ownership |
| Deposit | `RESOURCE_DEPOSIT` with `object_family: ResourceDeposit` | Source-supported named or delineated body with characterization | Quantity, reserve, economics, permit, production, title, or operation |
| Resource estimate | `RESOURCE_ESTIMATE` with `object_family: ResourceEstimate` | Modeled or compiled quantity/classification under an explicit scheme, method, date, units, confidence, and assumptions | Direct observation, deposit identity, reserve by default, production, permit, or economic/legal status |
| Reserve | `RESERVE`; no current canonical object-family admission | Explicit source-classified reserve assertion under a cited scheme and effective assumptions | Mere estimate, deposit, occurrence, permit, production, ownership, or KFM certification |
| Production | `PRODUCTION`; no current canonical Geology object-family admission | Time-bounded reported production record from an appropriate administrative, regulatory, or observed evidence chain | Deposit, reserve, estimate, permit validity, current operation, or ownership |
| Permit | `PERMIT`; no current canonical Geology object-family admission | Issuer- and jurisdiction-bound regulatory authorization record with scope and effective interval | Resource existence, extraction, production, ownership, reserve, or compliance |
| Modeled potential | `MODELED_POTENTIAL`; no current canonical object-family admission | Model-derived prospectivity or potential with versioned inputs, method, uncertainty, and limitations | Occurrence, deposit, estimate quantity, reserve, permit, production, or economic viability |

Recognition of a token is not schema admission. Until a separately reviewed
contract and schema own `RESERVE`, `PRODUCTION`, `PERMIT`, or
`MODELED_POTENTIAL`, current geology object schemas must not accept those values
as one of the three existing object families.

### 2.3 Normative anti-collapse rules

If this ADR is accepted, follow-on implementations:

1. **MUST** carry exactly one `resource_character` per resource claim record.
2. **MUST NOT** infer `resource_character` solely from `source_role`, filename, UI label, free text, or a linked object.
3. **MUST** preserve the source-native label and its scheme reference separately from the normalized token.
4. **MUST NOT** treat `RESOURCE_ESTIMATE` as `RESERVE` without explicit reserve classification evidence and the future stewarded reserve contract.
5. **MUST NOT** treat modeled potential as mineral occurrence or deposit evidence without independent evidence supporting that separate record.
6. **MUST NOT** treat permit or production records as proof of a deposit, estimate, reserve, ownership, current operation, or one another.
7. **MUST** keep cross-character links explicit, evidence-bound, time-aware, and non-identifying; links never make the records equal.
8. **MUST** fail closed on unknown tokens or unsupported character/object-family pairings.
9. **MUST NOT** derive public eligibility, policy disposition, promotion, or release state from this vocabulary.

This ADR does not choose the runtime envelope or error code for unsupported
records. Existing finite outcomes and precedence remain owned by their current
contracts and policy/runtime surfaces.

## 3. Stewardship and source-evidence requirements

### 3.1 Stewardship

| Responsibility | Required stewardship |
| --- | --- |
| Token stability, versioning, and cross-root compatibility | Architecture steward plus schema steward |
| `MINERAL_OCCURRENCE` and `RESOURCE_DEPOSIT` meanings | Geology domain steward plus natural-resources steward |
| `RESOURCE_ESTIMATE` method and classification support | Natural-resources steward plus an identified estimate-method/classification steward |
| `RESERVE` admission | Natural-resources steward plus an identified reserve-classification steward; source and evidence stewards also required |
| `PRODUCTION` admission | Source steward plus the future owning production-domain or regulatory-data steward |
| `PERMIT` admission | Source steward plus the future owning regulatory/legal steward |
| `MODELED_POTENTIAL` admission | Model steward plus geology and natural-resources stewards |
| Source identity, role, rights, authority limits, and freshness | Source steward through `SourceDescriptor` evidence |
| Evidence linkage, correction, supersession, and temporal consistency | Evidence steward |
| Exact/detail resource geometry | Sensitivity reviewer; this ADR creates no exposure rule |
| Policy, review, promotion, and release | Existing owning stewards and contracts; unchanged by this ADR |

Placeholder or missing steward identities block admission. CODEOWNERS routing or
the presence of this ADR cannot substitute for a review record or delegated
scientific, economic, legal, source, or evidence authority.

### 3.2 Common source-evidence floor

Any future admitted record using the vocabulary must carry or resolve:

- `source_descriptor_ref` and `source_record_ref`;
- the preserved `source_role` and source authority limits;
- `evidence_refs`, with EvidenceBundle resolution before governed downstream use;
- source-native labels plus normalized vocabulary mappings;
- source/assertion time, retrieval time, and applicable valid or effective time;
- rights, attribution, redistribution, and sensitivity posture;
- commodity/material context and source-native terminology;
- geometry or aggregation posture with uncertainty and precision;
- correction, supersession, and stale-state lineage.

This floor does not admit a source. Live records remain blocked until the source
registry and evidence paths close under their own authority.

### 3.3 Character-specific evidence

| Character | Additional minimum evidence |
| --- | --- |
| `MINERAL_OCCURRENCE` | Reported material/commodity, observation or compilation basis, place/area and precision, observed/source time where supported, uncertainty, and occurrence identity |
| `RESOURCE_DEPOSIT` | Deposit identity/name, delineation or characterization basis, commodity set, geometry fingerprint, temporal validity, and explicit links to supporting occurrences or observations |
| `RESOURCE_ESTIMATE` | Classification scheme and source label, method/model, estimate date, aggregation unit, quantity and units when present, confidence, assumptions, and estimate identity |
| `RESERVE` | Explicit reserve label, versioned reporting scheme, effective date, method, technical/economic assumptions, qualified review authority, and lineage to any supporting estimate; no KFM certification inferred |
| `PRODUCTION` | Reporting period, quantity and units, reporting site/facility/well context, issuer, source revision, and correction lineage |
| `PERMIT` | Issuer, jurisdiction, permit identifier, regulated scope, source-native status, effective interval, and update/correction lineage |
| `MODELED_POTENTIAL` | Model and run identities, input and specification hashes, method/version, execution or effective date, uncertainty, limitations, and a model/reality-boundary receipt when required by current contracts |

## 4. Compatibility and migration impact

### 4.1 Current contracts and schemas

- The three draft semantic contracts remain unchanged and keep their current
  meaning. Their first three object families map one-to-one to the first three
  tokens.
- The three permissive scaffold schemas remain unchanged by this proposal.
- Their lower-case `x-kfm.contract_doc` targets remain a documented path/casing
  defect to correct in the follow-on schema slice.
- No schema is created here for reserve, production, permit, or modeled
  potential. Their canonical ownership remains **NEEDS VERIFICATION**.

### 4.2 PR #1926 fixture profile

- The profile's three `resource_character` spellings match the proposed tokens,
  so its accepted positive fixtures need no token rewrite.
- Its fixed source-role pairings remain profile-local proof values, not universal
  character-to-role rules.
- Its negative reserve, permit, production, modeled-potential, observation, and
  sensitive-location cases remain correct. Acceptance of this ADR would not turn
  any current negative fixture into a positive fixture.
- New vocabulary coverage must extend the profile or create a successor profile;
  historical fixture meanings and expected findings must not be silently changed.

### 4.3 Existing proposed class labels

- `reserve_estimate` under `ResourceEstimate` remains a source-native or local
  estimate class. It does not become `RESERVE` without the reserve evidence and
  stewardship floor above.
- A quantified `model_derived_estimate` may remain `RESOURCE_ESTIMATE` when it
  satisfies the estimate contract. Unquantified prospectivity or favorability is
  `MODELED_POTENTIAL`, not a deposit or estimate quantity.
- `classification_label` and `source_classification_label` remain separate from
  `resource_character`; migration must preserve both.

### 4.4 Consumers and stored records

No stored data, API, graph, pipeline, registry, or public client is migrated by
this ADR. A later implementation must inventory existing values, preserve raw
source labels, map only reviewed exact matches, route unknown or ambiguous values
to fail-closed review, and avoid rewriting immutable source or historical
receipt records.

The change is additive for the first three profile tokens and intentionally
non-admitting for the other four. A future token rename or semantic change
requires a schema version change, compatibility fixtures, migration evidence,
and an ADR successor or reviewed amendment consistent with ADR conventions.

## 5. Smallest follow-on schema-hardening slice

After this ADR is accepted, the smallest dependency-closed implementation should:

1. add one shared schema fragment at
   `schemas/contracts/v1/domains/geology/resource_character.schema.json` with
   exactly the seven tokens above;
2. correct the `x-kfm.contract_doc` casing in the three existing schemas;
3. minimally harden only `mineral_occurrence.schema.json`,
   `resource_deposit.schema.json`, and `resource_estimate.schema.json` to require
   `object_family`, `resource_character`, `source_role`,
   `source_descriptor_ref`, and non-empty `evidence_refs`;
4. bind the first three schemas with exact object-family/resource-character
   constants while retaining `additionalProperties: true` for compatibility;
5. add deterministic valid and exact-negative fixtures proving unknown tokens,
   cross-family tokens, estimate-as-observed, modeled-potential-as-deposit,
   reserve-as-estimate, permit-as-deposit, and production-as-deposit fail closed;
6. validate the shared fragment and all three schemas through the existing
   no-network schema runner and Geology regression lane; and
7. add a generated receipt while leaving sources, policy, pipelines, lifecycle
   data, APIs, release, and publication untouched.

The four non-admitted characters should appear in the shared enum and negative
compatibility fixtures only. Creating schemas or contracts for them is a later
ownership and evidence decision, not part of the first hardening slice.

## 6. Consequences

### Positive

- The repository gains one reviewable vocabulary for anti-collapse checks.
- Source role, object identity, classification scheme, and resource character
  become explicitly separate.
- PR #1926 can remain stable while schemas gain a narrow future discriminator.
- Unknown and unsupported characters can fail closed without pretending that a
  real resource status has been assessed.

### Negative

- Four tokens are recognized before their record homes are admitted; consumers
  must preserve the distinction between vocabulary recognition and schema
  admission.
- Reserve classification and permit/production ownership remain unresolved and
  require specialized stewards.
- The schema casing defect and permissive field shapes remain until a follow-on
  PR is reviewed.

### Accepted tradeoffs

The proposal favors a small stable vocabulary and an incremental schema ratchet
over a complete resource/reserve reporting model. That keeps the first follow-on
reviewable and avoids importing an external classification standard without
source, version, rights, and stewardship evidence.

## 7. Alternatives considered

### Use `source_role` as the resource class

Rejected because `observed`, `modeled`, `regulatory`, and `aggregate` describe
evidence production, not occurrence, deposit, estimate, reserve, production, or
permit identity.

### Treat reserve as a `ResourceEstimate` synonym

Rejected because reserve status requires explicit source classification,
effective assumptions, and specialized review; an estimate is not a reserve by
default.

### Treat modeled potential as a deposit subtype

Rejected because model output cannot establish a physical deposit without
independent deposit evidence.

### Create seven complete object schemas now

Rejected for the first slice because reserve, production, permit, and modeled
potential do not yet have settled ownership, contracts, source admission, or
steward authority.

### Adopt one external resource/reserve standard as KFM's vocabulary

Deferred. External standards may be preserved through
`classification_scheme_ref`, but no standard, edition, license, or mapping has
been reviewed as universal KFM authority.

### Keep the vocabulary fixture-local

Rejected as the long-term state because schemas and consumers need stable
cross-component names. The current fixture remains the compatibility baseline,
not the authority that accepts this proposal.

## 8. Evidence and references

- [`MineralOccurrence` contract](../../contracts/domains/geology/MineralOccurrence.md)
- [`ResourceDeposit` contract](../../contracts/domains/geology/ResourceDeposit.md)
- [`ResourceEstimate` contract](../../contracts/domains/geology/ResourceEstimate.md)
- [Mineral occurrence schema scaffold](../../schemas/contracts/v1/domains/geology/mineral_occurrence.schema.json)
- [Resource deposit schema scaffold](../../schemas/contracts/v1/domains/geology/resource_deposit.schema.json)
- [Resource estimate schema scaffold](../../schemas/contracts/v1/domains/geology/resource_estimate.schema.json)
- [Geology source-role matrix](../domains/geology/SOURCE_ROLE_MATRIX.md)
- [PR #1926 governed source map](../intake/exploratory/geology-natural-resources-architecture-source-map.md)
- [Bounded resource-class fixture profile](../../fixtures/domains/geology/resource_class/README.md)
- [Fixture validator](../../tools/validators/domains/geology/validate_resource_class_distinction.py)
- [ADR operating contract](./README.md)
- [Canonical ADR index](./INDEX.md)
- [Accepted Directory Rules decision](./ADR-0029-adopt-directory-governance-standard-v2.md)

## 9. Migration plan

### Phase 0 — Proposal

- Add this `proposed` ADR, synchronized ADR indexes, and generated provenance receipt.
- Run the ADR coherence checks and documentation link checks.
- Make no contract, schema, source, policy, fixture, validator, pipeline, data,
  release, or publication change.

### Phase 1 — Review and acceptance

- Resolve the open stewardship and ownership questions below.
- Obtain explicit review from all named owners.
- Transition the ADR and canonical index together only if accepted.

### Phase 2 — Minimal schema ratchet

- Implement the bounded slice in §5 on a separate branch and pull request.
- Preserve current positive fixture behavior and exact negative polarity.
- Record compatibility and rollback evidence before any wider consumer work.

### Phase 3 — Character-specific contracts

- Propose separate ownership and schemas for reserve, production, permit, and
  modeled potential only when source, evidence, stewardship, and compatibility
  dependencies close.

## 10. Rollback plan

Before acceptance, revert or close the proposal and remove its index row; no
runtime or data rollback is required. After acceptance, preserve this record and
use a successor ADR to change or reverse the vocabulary. A follow-on schema PR
must carry its own rollback plan and must not rewrite historical source payloads,
fixtures, or receipts.

## 11. Open questions

- Which named steward has authority to review reserve classification and scheme mappings?
- Which responsibility root and contract own production records?
- Which responsibility root and contract own permit records and status history?
- Does modeled potential require a dedicated object family or a general model-output contract with a geology projection?
- Which source-native resource/reserve schemes and editions may be admitted, and how are mappings versioned?
- Should the three PascalCase contract paths remain canonical, and should the schema pointers be corrected without a compatibility alias?
- Which source-role/resource-character pairings are universally invalid beyond the minimum anti-collapse rules in this ADR?
- Should public DTOs expose `resource_character`, or only a governed public-safe projection of it?

## 12. Acceptance gates

- [ ] Architecture, geology, natural-resources, source, evidence, and schema steward reviews are recorded.
- [ ] Reserve-classification, permit, production, and model stewardship owners are identified or those record admissions remain explicitly held.
- [ ] The seven-token set is reviewed as claim character, not as a source role or external classification standard.
- [ ] Current contract semantics and PR #1926 fixture behavior remain compatible.
- [ ] The schema-hardening slice remains bounded to the three existing schemas plus a shared vocabulary fragment and exact fixtures.
- [ ] No source admission, policy, pipeline, lifecycle, release, publication, or repository-setting authority is inferred.

## 13. Non-effects

This proposal does not:

- assert that any real mineral occurrence, deposit, estimate, reserve,
  production record, permit, or modeled potential exists or is valid;
- admit, retrieve, endorse, or activate a source;
- change a contract, JSON Schema, source descriptor, policy, validator, fixture,
  workflow, pipeline, lifecycle record, API, graph, UI, proof, or release object;
- evaluate rights, sensitivity, economics, legal status, regulatory compliance,
  evidence resolution, promotion eligibility, or publication safety; or
- mark an ADR accepted, request review, merge, release, deploy, publish, or alter
  repository settings.

## 14. Change history

| Date | Status | Change | PR |
| --- | --- | --- | --- |
| 2026-08-03 | proposed | Initial minimum vocabulary, stewardship, compatibility, and schema-hardening proposal | pending |

[Back to top](#top)
