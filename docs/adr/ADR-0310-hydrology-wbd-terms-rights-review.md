<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION-ADR-0310-HYDROLOGY-WBD-TERMS-RIGHTS
title: ADR-0310: Hydrology WBD Terms and Rights Review
type: standard
version: v1.0-review
status: review
owners: TODO: hydrology domain steward; documentation steward; policy steward; rights reviewer
created: NEEDS-VERIFICATION
updated: 2026-05-06
policy_label: restricted-draft
related: [./README.md, ./ADR-0305-hydrology-source-documentation-verification.md, ./ADR-0307-hydrology-wbd-metadata-probe.md, ../domains/hydrology/README.md, ../../data/registry/crosswalk/sources.yaml, ../../schemas/contracts/v1/source/source_activation_decision.schema.json, ../../fixtures/source/hydrology/source_activation_decision.wbd.verified_inactive.valid.json, ../../release/dry_runs/hydrology_wbd_terms_rights_gate.json, ../../data/receipts/source_verification/hydrology/activation_decisions/SAD-WBD-ABSTAIN-001.json]
tags: [kfm, adr, hydrology, wbd, huc12, rights, terms, source-activation, verified-inactive, public-release, fail-closed]
notes: [
  Preserves the existing ADR-0310 short-form decision: terms/rights hardening keeps WBD VERIFIED_INACTIVE and non-public.
  This ADR distinguishes external public-domain source status from KFM publication eligibility.
  External USGS source facts were checked on 2026-05-06, but KFM publication remains blocked until repo-native source descriptors, attribution text, validation receipts, policy gates, release manifests, and rollback references are accepted.
  Owners, created date, policy steward, legal/risk reviewer, CI enforcement, and full activation-review workflow remain NEEDS VERIFICATION.
]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0310: Hydrology WBD Terms and Rights Review

<p align="center">
  <strong>Public-domain source material is not the same thing as KFM public-release eligibility.</strong>
</p>

<p align="center">
  <img alt="ADR status: review" src="https://img.shields.io/badge/ADR-review-blue">
  <img alt="source state: verified inactive" src="https://img.shields.io/badge/source-VERIFIED__INACTIVE-orange">
  <img alt="public release: no" src="https://img.shields.io/badge/public%20release-no-red">
  <img alt="policy decision: deny" src="https://img.shields.io/badge/policy-DENY-red">
  <img alt="rights: needs verification" src="https://img.shields.io/badge/rights-NEEDS%20VERIFICATION-yellow">
</p>

<p align="center">
  <a href="#decision-summary">Decision</a> ·
  <a href="#why-this-adr-exists">Why</a> ·
  <a href="#evidence-boundary">Evidence</a> ·
  <a href="#terms-and-rights-determination">Terms & rights</a> ·
  <a href="#state-model">State model</a> ·
  <a href="#release-controls">Release controls</a> ·
  <a href="#acceptance-criteria">Acceptance</a> ·
  <a href="#rollback-and-supersession">Rollback</a>
</p>

> [!IMPORTANT]
> **Preserved decision:** Terms and rights hardening keeps the WBD/HUC12 source candidate in `VERIFIED_INACTIVE` state and keeps WBD-derived KFM material **non-public** until KFM-specific review, attribution, source-descriptor, validation, policy, release, and rollback gates are accepted.
>
> **Meaning of “non-public” here:** KFM must not publish WBD geometry, WBD feature attributes, public aliases, map layers, API payloads, Evidence Drawer payloads, or Focus Mode answers from this source candidate merely because the source is publicly accessible or public domain.

> [!NOTE]
> This ADR does **not** say WBD is legally private. Official USGS material indicates WBD is a public-domain/public-access source family. This ADR says KFM has not yet completed the governed release burden required to expose WBD-derived artifacts through KFM public surfaces.

---

## Decision summary

| Field | Determination |
|---|---|
| ADR path | `docs/adr/ADR-0310-hydrology-wbd-terms-rights-review.md` |
| Decision | Keep WBD/HUC12 source candidate `VERIFIED_INACTIVE` and not eligible for public release. |
| Source family | USGS Watershed Boundary Dataset / HUC12 |
| KFM source candidate | `SRC-HYD-WBD-CANDIDATE` |
| Source role | `HYDROLOGIC_BOUNDARY` / hydrologic-unit boundary and watershed packaging context |
| Runtime decision | `ABSTAIN` for source activation until review closes |
| Policy decision | `DENY` for public publication until KFM release gates pass |
| Release posture | `DRAFT`; no public release, no public alias, no live source ingestion |
| Data handling posture | No WBD geometry or WBD feature attributes stored by this ADR |
| Rights posture | External public-domain support exists; KFM rights and attribution review remains `NEEDS VERIFICATION` for publication |
| Rollback target | `release/dry_runs/hydrology_wbd_metadata_probe_gate.json` |
| Correction route | `contracts/correction/correction_notice.md` |
| Public-surface rule | Governed API, MapLibre, Evidence Drawer, and Focus Mode must not expose WBD-derived KFM outputs until a later accepted release decision permits it. |

**Final decision:** WBD may be documented and reviewed as a high-value hydrology source candidate, but WBD-derived KFM outputs remain internal review material only until a later promotion decision proves rights, terms, attribution, validation, evidence closure, release state, and rollback.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Why this ADR exists

WBD/HUC12 is an attractive first hydrology proof source because it provides hydrologic-unit boundaries and a clear HUC hierarchy. That also makes it easy to over-promote.

KFM must prevent three different ideas from collapsing into one:

| Thing | What it means | What it does **not** mean |
|---|---|---|
| External source accessibility | USGS WBD can be found through official source pages, data catalog entries, downloads, or services. | KFM can publish derived geometry immediately. |
| External rights posture | Official USGS pages indicate public-domain/public-access status and credit expectations. | KFM attribution, source descriptor, release, policy, and rollback gates are complete. |
| KFM source activation | KFM has admitted a source into a governed lifecycle state. | A public map/API/AI answer can expose it without release proof. |

This ADR prevents “public domain” from becoming a shortcut around KFM’s trust membrane.

### Protected boundary

```text
official WBD source documentation
→ KFM source documentation review
→ inactive SourceDescriptor candidate
→ no-network fixture and metadata probe
→ rights and attribution review
→ validation and policy
→ EvidenceBundle / ReleaseManifest
→ governed public surface
```

Any shortcut from official source documentation directly to public KFM surface is a `DENY`, `ABSTAIN`, or `ERROR`.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Evidence boundary

This ADR is grounded in current repository evidence and current official USGS source checks, but it does not claim full CI or policy enforcement unless linked artifacts prove that enforcement.

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Existing ADR-0310 file | `CONFIRMED` | Existing short-form decision: WBD remains `VERIFIED_INACTIVE` and non-public after terms/rights hardening. | Full rationale, owners, acceptance, workflow enforcement, or release readiness. |
| ADR-0305 source documentation verification | `CONFIRMED repo doc` | Source documentation review is prerequisite support only and must not become claim evidence. | Connector activation or public publication. |
| ADR-0308 WBD metadata probe | `CONFIRMED repo doc` | Metadata-only probing must not activate public-safe release by itself. | Terms/rights closure or live ingestion approval. |
| Hydrology domain README | `CONFIRMED repo doc / draft` | Hydrology is first proof lane; WBD/HUC is hydrologic-unit framing; fixture-first/no-network posture. | That all adjacent hydrology paths, owners, or commands are enforced. |
| Source activation decision schema | `CONFIRMED repo schema` | `VERIFIED_INACTIVE` is an allowed source activation state; finite decisions are `ALLOW`, `ABSTAIN`, `DENY`, `ERROR`. | That all consumers enforce the schema. |
| WBD verified-inactive fixture | `CONFIRMED repo fixture` | The WBD source candidate has a valid `ABSTAIN` + `VERIFIED_INACTIVE` fixture. | Public-release eligibility. |
| WBD terms/rights dry run | `CONFIRMED repo artifact` | Records `no_public_release`, `policy_decision: DENY`, `rights_status: UNKNOWN`, and `activation_decision: VERIFIED_INACTIVE`. | That CI enforces this dry run. |
| Source registry crosswalk entry | `CONFIRMED repo registry` | Lists `usgs_wbd_huc12` as high-trust, public-default, hydrologic boundary source. | KFM publication eligibility or final rights review. |
| Official USGS WBD and policy pages | `EXTERNALLY CHECKED` | WBD source meaning, public-domain/public-access support, credit expectations. | KFM-specific source activation or release acceptance. |

### Truth labels used here

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from current repository evidence or official external source checks during this revision. |
| `EXTERNALLY CHECKED` | Checked against official source pages in this session; still version-sensitive over time. |
| `PROPOSED` | Rule, gate, path, checklist, or implementation step not proven as enforced. |
| `NEEDS VERIFICATION` | Checkable item still requiring maintainer, rights, policy, CI, source, or release evidence. |
| `UNKNOWN` | Not verified strongly enough in this session. |
| `DENY` | Safe negative outcome when policy blocks publication or activation. |
| `ABSTAIN` | Safe negative outcome when source support or release eligibility is not complete enough to answer/activate. |
| `ERROR` | Required artifact or validation state is missing or malformed. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Terms and rights determination

Official source checks support a strong **external** starting posture:

- USGS WBD is an official national hydrologic-unit dataset.
- WBD/HUC boundaries are hydrologic units arranged in a nested hierarchy and complete nationally to the 12-digit unit.
- USGS pages identify WBD media/source usage as public domain.
- The USGS Science Data Catalog lists WBD access as public and license as the USA.gov public-domain label.
- USGS asks users to provide appropriate credit when using USGS information.

KFM still keeps WBD `VERIFIED_INACTIVE` because KFM publication requires more than external public-domain status.

### KFM release burden still open

| Required closure item | Current ADR posture | Required before publication |
|---|---|---|
| Official source citation | `NEEDS VERIFICATION` | Exact citation text and source page(s) recorded in SourceDescriptor or release notes. |
| Attribution text | `NEEDS VERIFICATION` | Display/metadata attribution pattern accepted by documentation and policy stewards. |
| Terms snapshot | `NEEDS VERIFICATION` | Review timestamp, source URLs, and rights summary preserved. |
| SourceDescriptor | `PROPOSED / NEEDS VERIFICATION` | Inactive descriptor with source role, rights, terms, cadence, caveats, scope, and steward. |
| Data snapshot identity | `NEEDS VERIFICATION` | Download/service endpoint, snapshot date/version, digest, and retrieval receipt. |
| Geometry storage decision | `DENY for this ADR` | Later PR must decide whether and where WBD geometry may be captured. |
| Feature attribute storage decision | `DENY for this ADR` | Later PR must decide allowed attributes, minimization, and release class. |
| Public layer eligibility | `DENY` | Requires ReleaseManifest, policy pass, catalog/provenance closure, and rollback target. |
| API/UI eligibility | `DENY` | Requires governed API payloads downstream of released artifacts only. |
| AI/Focus Mode eligibility | `DENY` | Requires EvidenceBundle resolution and citation validation; no direct model-client path. |

### Rights decision table

| Question | Answer for ADR-0310 |
|---|---|
| Can WBD remain in the source registry as a candidate hydrologic boundary source? | Yes. |
| Can WBD be called public domain in KFM docs? | Only with official-source citation and review timestamp. |
| Can KFM treat WBD as public-release-ready because it is public domain? | No. |
| Can this ADR store WBD geometry? | No. |
| Can this ADR store WBD feature attributes? | No. |
| Can this ADR create a public map layer or public alias? | No. |
| Can this ADR support a future inactive SourceDescriptor update? | Yes. |
| Can this ADR activate live WBD ingestion? | No. |
| Can this ADR support public claims through EvidenceBundle? | No; a later release decision must do that. |

> [!CAUTION]
> A source can be legally reusable and still be blocked from KFM publication if KFM has not recorded source role, attribution, snapshot identity, validation, policy, release, correction, and rollback state.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Decision details

### 1. Preserve `VERIFIED_INACTIVE`

The WBD source candidate remains:

```json
{
  "source_id": "SRC-HYD-WBD-CANDIDATE",
  "decision": "ABSTAIN",
  "source_activation_state": "VERIFIED_INACTIVE"
}
```

This state means the source candidate has enough review structure to be tracked, but not enough release closure to become active for public use.

### 2. Keep publication blocked

For this ADR:

```json
{
  "no_live_source_ingestion": true,
  "no_wbd_geometry_stored": true,
  "no_wbd_feature_attributes_stored": true,
  "no_public_release": true,
  "publication_eligibility_decision": "NOT_ELIGIBLE",
  "policy_decision": "DENY"
}
```

### 3. Treat registry `rights_default: public` as a starting hint, not release proof

The crosswalk source registry may identify `usgs_wbd_huc12` as public-default and high trust. That does not supersede the dry-run release gate. For public-facing KFM use, the stricter release artifact wins until a later accepted decision says otherwise.

### 4. Keep source docs out of claim evidence

Source pages and terms checks may support source documentation review and SourceDescriptor drafting. They do not support public hydrologic claims.

### 5. Require explicit attribution handling

Before public release, KFM must decide where USGS credit appears:

| Surface | Required attribution behavior |
|---|---|
| SourceDescriptor | Human-readable source and rights/credit summary. |
| Catalog metadata | Source citation, publisher, access, license, and retrieval/snapshot fields. |
| LayerManifest | Attribution string or reference to a shared attribution entry. |
| Map UI | Trust-visible source chip or attribution panel if the layer is published. |
| Evidence Drawer | Source role, source citation, limitations, and release state. |
| Export/download | Attribution and license/public-domain notice when public export is allowed. |
| ReleaseManifest | Explicit rights/attribution review status and reviewer trace. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## State model

```mermaid
stateDiagram-v2
  [*] --> CANDIDATE
  CANDIDATE --> DRAFT: source docs identified
  DRAFT --> VERIFIED_INACTIVE: terms/rights review structured
  VERIFIED_INACTIVE --> ACTIVE_INTERNAL_ONLY: later PR with inactive descriptor + fixture + rights review + policy pass
  ACTIVE_INTERNAL_ONLY --> ACTIVE_PUBLIC_SAFE: later promotion with ReleaseManifest + rollback + public attribution
  VERIFIED_INACTIVE --> SUSPENDED: source terms or source identity unresolved
  ACTIVE_INTERNAL_ONLY --> SUSPENDED: source terms change or validation fails
  ACTIVE_PUBLIC_SAFE --> SUSPENDED: public release withdrawn
  SUSPENDED --> RETIRED: superseded source or deprecated use
  VERIFIED_INACTIVE --> RETIRED: candidate rejected or replaced

  note right of VERIFIED_INACTIVE
    Current ADR-0310 state.
    No public release.
    No live ingestion.
    No WBD geometry or feature attributes stored.
  end note
```

### Allowed transitions from `VERIFIED_INACTIVE`

| Transition | Allowed by this ADR? | Required evidence |
|---|---:|---|
| `VERIFIED_INACTIVE` → `ACTIVE_INTERNAL_ONLY` | No; later PR only | Inactive SourceDescriptor, no-network fixture, source terms packet, attribution plan, validation report, policy decision, rollback target. |
| `VERIFIED_INACTIVE` → `ACTIVE_PUBLIC_SAFE` | No | Must pass `ACTIVE_INTERNAL_ONLY` first, then promotion/release. |
| `VERIFIED_INACTIVE` → `SUSPENDED` | Yes | Source terms changed, source identity unclear, attribution cannot be resolved, or reviewer blocks use. |
| `VERIFIED_INACTIVE` → `RETIRED` | Yes | Candidate rejected, source superseded, or hydrology source strategy changes. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Release controls

### Blocking controls

| Control | Required behavior | Failure outcome |
|---|---|---|
| Live ingestion guard | No live WBD fetch or scheduled connector from this ADR. | `DENY` |
| Geometry guard | No WBD geometry stored by this ADR. | `DENY` |
| Attribute guard | No WBD feature attributes stored by this ADR. | `DENY` |
| Publication guard | No public alias, published artifact, API payload, tile, or map layer. | `DENY` |
| Attribution guard | No publication without exact attribution/citation plan. | `DENY` |
| Source-descriptor guard | No activation without inactive SourceDescriptor and review state. | `DENY` or `ERROR` |
| Evidence guard | Source docs cannot be used as hydrologic claim evidence. | `DENY` |
| AI guard | No direct model-client use and no uncited Focus Mode answer. | `DENY` |
| Rollback guard | No release without rollback target and correction route. | `ERROR` |
| Stale terms guard | Terms/rights source checks must be refreshed before activation. | `ABSTAIN` |

### Public-surface denial matrix

| Surface | Current state | Reason |
|---|---|---|
| Public MapLibre WBD layer | Blocked | No ReleaseManifest or public attribution plan. |
| Public governed API WBD endpoint | Blocked | No public-safe release decision. |
| Evidence Drawer WBD feature payload | Blocked | No EvidenceBundle closure for public use. |
| Focus Mode WBD answer | Blocked | No public EvidenceBundle + citation validation path. |
| Download/export bundle | Blocked | No release, attribution, or distribution manifest. |
| Internal review packet | Allowed | Must remain non-public/restricted-draft unless policy steward changes label. |
| Source registry candidate | Allowed | Must not imply activation. |
| Dry-run release gate | Allowed | Must remain `DRAFT` and non-public. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Required fields for the next SourceDescriptor review

A later PR may advance the WBD candidate only by adding or updating an inactive source descriptor with the fields below.

| Field | Requirement |
|---|---|
| `source_id` | `SRC-HYD-WBD-CANDIDATE` or accepted successor ID. |
| `publisher` | U.S. Geological Survey / National Geospatial Technical Operations Center, as verified. |
| `source_family` | `WBD_HUC12` or accepted hydrology source-family enum. |
| `source_role` | Hydrologic unit boundary; not observation, flood event, or regulatory hazard claim. |
| `external_rights_status` | Public-domain/public-access support, with official source URLs and retrieval date. |
| `kfm_rights_review_status` | `NEEDS_VERIFICATION`, `ABSTAIN`, or accepted equivalent until reviewer closes. |
| `attribution_text` | Exact proposed USGS credit text. |
| `license_or_terms_refs` | Official source rights/credit links. |
| `access_method` | Download/service path and whether it is a snapshot, service, or metadata-only probe. |
| `snapshot_or_version` | Snapshot identifier, publication date, metadata date, or service version if used. |
| `retrieval_receipt` | Required before any actual data capture. |
| `geometry_policy` | Whether geometry capture is allowed, restricted, generalized, or blocked. |
| `attribute_policy` | Which attributes may be captured, minimized, or blocked. |
| `public_release_class` | Must remain `not_eligible` until ReleaseManifest exists. |
| `activation_state` | Must remain `VERIFIED_INACTIVE` unless a later accepted decision changes it. |
| `reviewers` | Hydrology, documentation, policy, and rights reviewers or explicit placeholders. |
| `rollback_target` | Existing dry-run gate or successor rollback artifact. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Accepted inputs and exclusions

### Accepted by this ADR

- Terms and rights review notes.
- Official source-documentation references.
- Attribution draft text.
- Source activation decision fixtures.
- Dry-run release gate records.
- Review checklists.
- Rollback/supersession notes.
- Non-public source-descriptor drafts.

### Excluded by this ADR

| Excluded material | Where it belongs instead |
|---|---|
| WBD geometry | Later governed source-ingest PR after terms, receipt, and storage policy approval. |
| WBD feature attributes | Later governed source-ingest PR with attribute minimization and schema review. |
| Public WBD PMTiles or vector tiles | Later release candidate with LayerManifest and ReleaseManifest. |
| Public API route | Later governed API PR after release eligibility. |
| MapLibre source/layer registration | Later UI/map PR after release eligibility. |
| Evidence Drawer public payload | Later release/UI PR after EvidenceBundle closure. |
| Focus Mode public answer | Later governed AI/API PR after EvidenceBundle and citation validation. |
| Live connector | Later activation ADR or source-activation decision. |
| Emergency or life-safety guidance | Out of scope; KFM is not an emergency alert system. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Acceptance criteria

ADR-0310 may move beyond `review` only when the following are true.

- [ ] ADR index lists ADR-0310 with status and decision summary.
- [ ] Owners/stewards for hydrology, documentation, policy, and rights review are named or explicitly placeholdered.
- [ ] Source activation decision schema is referenced by the ADR and any fixtures validate against it.
- [ ] WBD verified-inactive fixture remains valid and uses `ABSTAIN` + `VERIFIED_INACTIVE`.
- [ ] WBD terms/rights dry-run artifact remains `DRAFT`, non-public, and policy-denied unless superseded by a later accepted release decision.
- [ ] Source registry language distinguishes `rights_default: public` from KFM public-release eligibility.
- [ ] Official source rights/credit pages are recorded with retrieval date.
- [ ] Exact USGS attribution text is proposed and reviewed.
- [ ] No WBD geometry is added by this ADR.
- [ ] No WBD feature attributes are added by this ADR.
- [ ] No public aliases, tiles, API payloads, Evidence Drawer payloads, or Focus Mode answers are added by this ADR.
- [ ] Future activation path requires SourceDescriptor, retrieval receipt, no-network fixture, validation report, policy decision, ReleaseManifest, correction route, and rollback target.
- [ ] Documentation says source documentation and source rights review are not claim evidence.
- [ ] Any change to `VERIFIED_INACTIVE` state is handled in a later ADR, source activation decision, or release PR with validation evidence.

### Definition of done for this documentation revision

- [ ] Existing one-line decision is preserved and expanded, not replaced by generic rights language.
- [ ] External WBD public-domain/public-access status is acknowledged without weakening KFM release gates.
- [ ] Current repo artifacts are linked with relative paths.
- [ ] Remaining verification items are explicit.
- [ ] Rollback path is visible.
- [ ] No implementation enforcement is claimed unless backed by cited repo artifacts.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Change protocol

Any PR that changes WBD activation or publication status must include:

1. Updated ADR-0310 or successor decision.
2. Updated source activation decision record.
3. Updated SourceDescriptor or source registry entry.
4. Rights/terms review packet with source URLs and retrieval date.
5. Attribution text and display plan.
6. Retrieval receipt if data is fetched.
7. Geometry/attribute storage policy.
8. Validator and fixture updates.
9. Policy decision.
10. ReleaseManifest if anything becomes public.
11. Correction route and rollback target.
12. Notes explaining what remains non-public.

### State-change guard

```text
IF source_activation_state changes from VERIFIED_INACTIVE
THEN require explicit activation decision + policy pass + rollback target.

IF public_release changes from false to true
THEN require ReleaseManifest + attribution + EvidenceBundle closure + correction route.

IF WBD geometry or attributes are introduced
THEN require retrieval receipt + storage path + schema + minimization review + no-public-bypass assertion.
```

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Rollback and supersession

If this ADR is rolled back or superseded:

1. Preserve this file as lineage.
2. Keep `SRC-HYD-WBD-CANDIDATE` `VERIFIED_INACTIVE` unless the successor decision explicitly changes it.
3. Keep public release denied unless a successor ReleaseManifest is accepted.
4. Preserve dry-run artifacts and activation-decision receipts.
5. Mark superseded rights or attribution reviews with a replacement reference.
6. Revoke public aliases if any were accidentally created.
7. Issue a CorrectionNotice if any public material escaped before release acceptance.
8. Update the ADR index and hydrology tracking docs.
9. Preserve old receipts/proofs/releases; do not delete audit history.

Rollback must protect the evidence chain and must not convert a terms review into a public release.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Open verification backlog

| Item | Status | Why it matters |
|---|---|---|
| Created date | `NEEDS VERIFICATION` | Existing file did not include metadata. |
| Owners/stewards | `NEEDS VERIFICATION` | Rights, hydrology, policy, and documentation review burden must be explicit. |
| ADR index status | `NEEDS VERIFICATION` | `docs/adr/README.md` should list ADR-0310. |
| Exact legal/risk reviewer | `NEEDS VERIFICATION` | This ADR is not legal advice; a reviewer must own final rights posture. |
| WBD source descriptor path | `NEEDS VERIFICATION` | Avoid parallel source-registry homes. |
| Exact attribution text | `NEEDS VERIFICATION` | Required before publication. |
| Exact source snapshot/version/digest | `NEEDS VERIFICATION` | Required before geometry/attribute capture. |
| Geometry storage policy | `NEEDS VERIFICATION` | Required before any WBD geometry enters lifecycle data. |
| Attribute minimization policy | `NEEDS VERIFICATION` | Required before any WBD feature attributes enter lifecycle data. |
| CI enforcement | `NEEDS VERIFICATION` | Do not claim workflow enforcement without current run evidence. |
| Policy implementation | `NEEDS VERIFICATION` | Dry-run JSON records policy posture; policy-as-code enforcement must be verified separately. |
| Public release class | `DENY until accepted` | Prevents public surface bypass. |
| ReleaseManifest successor | `UNKNOWN` | Needed before public map/API/UI/AI use. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Official references checked

These references support source-rights review only. They do not activate WBD in KFM.

| Reference | Use in this ADR |
|---|---|
| [USGS Watershed Boundary Dataset][usgs-wbd] | WBD description, HUC hierarchy, source/public-domain notes, authoritative snapshot note. |
| [USGS WBD Science Data Catalog entry][usgs-wbd-sdc] | Public access and public-domain license signal. |
| [USGS Copyrights and Credits][usgs-copyrights] | USGS public-domain and credit expectations. |
| [Acknowledging or Crediting USGS][usgs-crediting] | Example credit language and attribution patterns. |

[usgs-wbd]: https://www.usgs.gov/national-hydrography/watershed-boundary-dataset
[usgs-wbd-sdc]: https://data.usgs.gov/datacatalog/data/USGS%3A0101bc32-916e-481d-8654-db7f8509fd0c
[usgs-copyrights]: https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits
[usgs-crediting]: https://www.usgs.gov/information-policies-and-instructions/acknowledging-or-crediting-usgs

---

## Final decision

KFM keeps WBD/HUC12 in `VERIFIED_INACTIVE` state.

WBD may remain a high-trust hydrologic boundary source candidate, and official USGS source facts may support a future rights review. But this ADR does not publish WBD-derived material, does not store WBD geometry or attributes, does not activate a live connector, and does not allow public map/API/UI/AI exposure.

The safe current outcome is:

```text
decision: ABSTAIN
source_activation_state: VERIFIED_INACTIVE
policy_decision: DENY
publication_eligibility_decision: NOT_ELIGIBLE
public_release: false
```

A later promotion must prove the full KFM chain before any public use.

<p align="right"><a href="#top">Back to top ↑</a></p>
