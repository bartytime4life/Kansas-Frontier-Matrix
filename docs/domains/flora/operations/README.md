[Back to top](#flora-operations--domain-operational-index)

---

## Sensitivity and rare flora

Rare, protected, and culturally sensitive flora carry **public-safety and stewardship obligations** that operations must respect. The default posture is **fail-safe**:

- **Exact location** for sensitive taxa is **not** a public surface. Public outputs use **generalized geometry** with a recorded redaction lineage.
- **Controlled-access** sources (steward terms, license terms, agency restrictions) are not promoted to public layers; they may inform internal review only.
- **Unknown rights / unknown sensitivity** **fail closed** and ABSTAIN until resolved.
- **Steward review** can lift quarantine or authorize controlled internal use; it does not by itself authorize public release.
- **Generalized public surfaces** are explicit derivatives — a generalized polygon is not an occurrence point and must not be displayed as one.

Source roles drive admissibility (`source_role` is a first-class field):

| Source role                  | Trust use                                                         | Default publication posture                                  |
| ---------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------ |
| `official`                   | Anchors official status / regulation / authoritative spatial layer | Publish only after rights, sensitivity, and review are clear |
| `institutional`              | Strong evidence for specimen / collection facts                   | Public-safe metadata; respect license & precision            |
| `steward_reviewed`           | Curated by responsible steward / heritage program                 | Public only with explicit release approval                   |
| `corroborative`              | Support, not controlling authority                                | Usually aggregate / generalize                               |
| `community_observation`      | Useful with quality / reviewer / license labels                   | Publish only if license and sensitivity allow                |
| `controlled_access`          | Terms / license / steward approval required                       | **Deny** public exact publication                            |
| `derived_model`              | Contextual / interpretive only                                    | Publish with model card; never as observation truth          |
| `generalized_public_surface` | Public-safe geometry derived from internal details                 | Publishable when transform lineage, sensitivity, and rights are recorded |

> [!WARNING]
> The architecture explicitly forbids collapsing observed occurrence, specimen, steward-reviewed, modeled, generalized-public, and AI-generated content into a single truth surface. **A model output is not an observation. A range map is not a specimen. A generalized public polygon is not an internal sensitive occurrence point. An AI answer is not source evidence.**

[Back to top](#flora-operations--domain-operational-index)

---

## Definition of Done

Use this checklist to decide whether an operational change in the flora lane is releasable. Items below are **gates**, not preferences. If a gate cannot be evidenced, mark the change `ABSTAIN` or `DENY` and record the reason.

- [ ] Source descriptor exists, validates, and includes `rights_license_terms`, `sensitivity_posture`, `source_role`, `cadence_update_behavior`.
- [ ] Run receipt emitted for every fetch / normalize / validate / diff step.
- [ ] All payloads validate against current schemas at recorded `spec_hash`.
- [ ] `source_refs` and `evidence_refs` resolve; `EvidenceRef → EvidenceBundle` resolves for consequential claims.
- [ ] Geometry, CRS, and precision pass deterministic checks; canonical CRS recorded; public layers declare display CRS.
- [ ] Taxon normalization preserves raw text; accepted taxon present where required; ambiguities recorded.
- [ ] Duplicates / conflicting identities reconciled or quarantined with reason.
- [ ] Rights / license state explicit; controlled-access obligations enforced; unknown rights fail closed.
- [ ] No exact coordinates, restricted IDs, or internal refs leak into public payloads; redaction receipt emitted where generalization applied.
- [ ] Catalog closure (STAC / DCAT / PROV / manifest / proof / runtime refs) closes; digests align.
- [ ] Steward review recorded for steward-gated paths; release approval recorded for `steward_reviewed` public release.
- [ ] `PromotionDecision`, `ReleaseManifest`, and (where applicable) `rollback_card` / `correction_notice` linked.
- [ ] Public-facing changes traceable end-to-end; rollback target named.
- [ ] Docs updated where behavior changed materially; ADR cited where doctrine moves.

[Back to top](#flora-operations--domain-operational-index)

---

## FAQ

**Q. Why is this an index instead of a runbook?**
Runbooks are operational procedures and live under `docs/runbooks/`. Putting procedures here would create a second runbook home and fragment the lifecycle. The index reduces drift by linking, not duplicating.

**Q. Can I add a new operational document under `operations/`?**
Prefer extending the canonical home (`PIPELINES_AND_LIFECYCLE.md`, `PUBLICATION_AND_POLICY.md`, or a runbook). If the content is genuinely flora-operational, narrowly scoped, and has no canonical home, add it here with a clear status label and a back-link from the canonical home so anti-fragmentation review can find it.

**Q. Where do operational metrics, dashboards, and oncall references go?**
Dashboards and runtime telemetry are **NEEDS VERIFICATION** in the current corpus — no dashboard or oncall convention is confirmed. When the convention exists, link from here; do not host it here.

**Q. Why are so many things marked PROPOSED?**
The Flora Architecture Blueprint is doctrinally CONFIRMED but its repository realization is UNKNOWN in this session — no mounted repo, tests, workflows, or runtime were inspectable. Status will tighten as ADRs land and homes are confirmed.

**Q. Can the AI answer flora questions directly?**
Only as **interpretive output subordinate to evidence, policy, review, and release state**. The `DecisionEnvelope` outcome may be `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` — and `ABSTAIN` is the right answer when evidence is missing or sensitivity is unresolved. AI summaries are not sovereign truth.

[Back to top](#flora-operations--domain-operational-index)

---

## Appendix

<details>
<summary><b>A. Cross-reference: where to update what</b></summary>

| If you change…                                  | Update / cite                                                                          |
| ----------------------------------------------- | -------------------------------------------------------------------------------------- |
| A source's URL / cadence / rights / sensitivity | `data/registry/flora/sources.yaml`, the relevant ADR, runbook, and source descriptor   |
| A schema field on a flora object                | `schemas/contracts/v1/domains/flora/<object>.schema.json`, fixtures, validators, ADR if shape moves |
| A policy rule                                   | `policy/domains/flora/<area>.rego` + tests + decision envelope reasons                 |
| A pipeline step                                 | `pipelines/flora/`, `pipeline_specs/flora/`, `flora_run_receipt` shape if changed      |
| Public layer eligibility                        | `data/registry/flora/layer_registry.yaml`, `ADR-flora-public-layer-strategy.md`        |
| Sensitive-flora generalization rules            | `ADR-flora-sensitive-location-policy.md`, `policy/.../sensitivity.rego`, redaction receipt schema |
| A release / promotion / rollback decision       | `release/<…>/`, `ReleaseManifest`, `PromotionDecision`, `rollback_card`, `correction_notice` |

</details>

<details>
<summary><b>B. Glossary (operational subset)</b></summary>

- **EvidenceBundle** — resolved evidence list + policy state + review state + artifact digests; the inspectable unit a public claim resolves to.
- **DecisionEnvelope** — finite-outcome wrapper (`ANSWER` / `ABSTAIN` / `DENY` / `ERROR`) with reasons, obligations, and references.
- **RunReceipt** — process memory; what ran, against what spec, with what result. Not a proof.
- **PromotionDecision** — governed state transition record; promotion is not a file move.
- **ReleaseManifest** — release-state binding of catalog closure, proof, policy, digests.
- **RollbackCard** — reversal authority + scope + supersession linkage.
- **RedactionReceipt** — lineage of generalization or withholding for sensitive flora.
- **Source role** — `official` / `institutional` / `steward_reviewed` / `corroborative` / `community_observation` / `controlled_access` / `derived_model` / `generalized_public_surface`.
- **Cite-or-abstain** — default truth posture; if a claim cannot cite admissible evidence, abstain.
- **Spec hash** — stable hash of schema / spec / process identity (not a timestamp, not a policy).

</details>

<details>
<summary><b>C. Verification backlog (for this README)</b></summary>

Open items pending evidence:

- Confirm whether `docs/domains/flora/operations/` is acceptable in this repo or whether content should fold into `PIPELINES_AND_LIFECYCLE.md` and `PUBLICATION_AND_POLICY.md`. **PROPOSED · NEEDS VERIFICATION**.
- Resolve `contracts/flora/` vs `schemas/contracts/v1/domains/flora/` placement (`ADR-flora-schema-home.md`). **PROPOSED · UNKNOWN**.
- Resolve `policy/flora/` vs `policy/domains/flora/` placement. **PROPOSED · UNKNOWN**.
- Confirm `release/` subfolder layout for flora candidates / manifests / decisions / rollback cards. **PROPOSED · UNKNOWN**.
- Verify owner / steward identities; replace `TBD` placeholders. **PROPOSED · UNKNOWN**.
- Confirm presence of dashboards, telemetry, and oncall conventions; if present, link from here. **NEEDS VERIFICATION**.
- Confirm CI workflow names (`flora-ci.yml`, `flora-promotion.yml`) and replace badge placeholders with real targets. **NEEDS VERIFICATION**.

</details>

<details>
<summary><b>D. Sources cited in this index</b></summary>

- *KFM Flora Architecture — PDF-Only Implementation Blueprint* (attached project corpus). Lifecycle, source roles, descriptor fields, fail-closed policy gates, file/folder proposal.
- *KFM Directory Rules* (attached project corpus). Authority of root folders; domains under `docs/domains/<domain>/`; canonical homes for contracts / schemas / policy / data / release; warning against parallel homes without an ADR.
- *KFM Components Pass 18* — biodiversity & rare-species geoprivacy (CORPUS-CONFIRMED doctrine).
- *KFM Components Pass 19* — `spec_hash`, `run_receipt`, `EvidenceBundle`, `DecisionEnvelope`, `ReleaseManifest`, `CatalogMatrix`, finite outcomes (CORPUS-CONFIRMED doctrine).

</details>

[Back to top](#flora-operations--domain-operational-index)
