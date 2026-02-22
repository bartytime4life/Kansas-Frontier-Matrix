# Pull Request

<!--
KFM defaults:
- Map-first • Time-aware • Governed • Evidence-first • Cite-or-abstain
- Keep this PR description crisp. Prefer links to source-of-truth docs, ADRs, run receipts, and EvidenceBundles.
- Delete sections that are not applicable.
-->

**Purpose (one line):** <!-- e.g., "Add governed API endpoint for Story Node search" -->
**Status:** <!-- Draft | Ready for review -->
**Owners:** <!-- @team or @person -->

---

## Quick links
- [Summary](#summary)
- [Linked work](#linked-work)
- [Governance and evidence](#governance-and-evidence)
- [Risk and rollback](#risk-and-rollback)
- [Testing](#testing)
- [Deployment notes](#deployment-notes)
- [Definition of done](#definition-of-done)

---

## Summary
### What changed
<!-- Bullet the key changes. -->
- 
- 

### Why
<!-- What problem does this solve? What outcome are we aiming for? -->
- 

### How to review
<!-- Give reviewers the fastest possible path. -->
- Start here:
- Key files:
- Non-obvious decisions:

### Screenshots / recordings (if UI/Map/Story changes)
<!-- Prefer before/after. -->
- 

---

## Linked work
- **Issue(s):** <!-- e.g., #123 -->
- **ADR(s):** <!-- link(s) -->
- **Story Node(s):** <!-- link(s) / IDs -->
- **Dataset(s) / DatasetVersion(s):** <!-- IDs + versions -->
- **Related PRs:** <!-- link(s) -->

---

## Change type
- [ ] Bug fix
- [ ] Feature
- [ ] Refactor / Cleanup
- [ ] Docs / Documentation only
- [ ] Data / Pipeline / Catalog / Provenance
- [ ] API / Contract (OpenAPI / GraphQL)
- [ ] UI / Map / Story UX
- [ ] Infrastructure / DevOps
- [ ] Security / Privacy / Governance

---

## Governance and evidence

### Evidence (cite-or-abstain)
<!--
If you are asserting a fact, decision, or claim that matters, link the evidence.
If you cannot cite it, label it clearly as an assumption.
-->
- **EvidenceBundle / EvidenceRef(s):** 
- **Primary source-of-truth link(s):** 
- **Assumptions (explicit):** 
- **Open questions / Unknowns:** 

### Policy, sensitivity, and safe location handling
<!-- Default-deny for sensitive locations / private individuals / vulnerable infrastructure. Prefer generalization. -->
- **Policy labels applied (if any):** 
- **Redactions/generalizations performed (if any):** 
- **Contains precise locations?** <!-- Yes/No. If yes, justify + review note. -->
- **CARE/FAIR considerations (if relevant):** 

### Time-awareness (required when applicable)
<!-- Use explicit dates (YYYY-MM-DD) when describing “recent”, “today”, “yesterday”, etc. -->
- **Event time vs valid time vs transaction time impacted?** <!-- Yes/No -->
- **Time semantics documented/verified?** <!-- link -->

---

## Data and pipeline changes (fill out if applicable)

### Data lifecycle zone(s) touched
- [ ] RAW (immutable acquisition)
- [ ] WORK / QUARANTINE (intermediate transforms)
- [ ] PROCESSED (publishable)
- [ ] CATALOG / TRIPLET (DCAT + STAC + PROV)
- [ ] PUBLISHED (governed runtime)

### Promotion Contract (must be satisfied for promotion)
- **Inputs (with checksums or immutable refs):**
- **Outputs (artifacts + checksums):**
- **License(s) verified:**
- **Provenance recorded (PROV / lineage):**
- **Validation rules & results:**
- **Run receipt / audit record:** <!-- link -->

<details>
<summary><strong>Data promotion checklist</strong></summary>

- [ ] Source identified, permissions/license confirmed, and citation recorded
- [ ] Sensitivity classification applied; restricted fields redacted/generalized as required
- [ ] Schema documented (including spatial + temporal extent, units, CRS/geometry types)
- [ ] Deterministic IDs/hashes implemented where required
- [ ] QA gates run (schema checks, null/dup rules, geometry validity, range checks, etc.)
- [ ] Provenance emitted (inputs/outputs/params + checksums + actor + timestamps)
- [ ] Artifacts written only to the correct zone(s); no “side writes”
- [ ] Promotion is reversible (rollback plan and versioned artifacts)
- [ ] Catalog updated (DCAT/STAC/PROV pointers, metadata completeness)

</details>

---

## API / contract changes (fill out if applicable)
- **Contract updated:** <!-- OpenAPI/GraphQL link(s) -->
- **Backward compatibility:** <!-- None | Compatible | Breaking -->
- **Breaking change details & migration path:** 
- **Authn/Authz changes:** 
- **Rate limits / quotas impacted:** 
- **Error model impacted (codes, shape, semantics):** 
- **Auditing / logging:** <!-- what’s recorded; any PII considerations -->

<details>
<summary><strong>Trust membrane checklist (API layer boundaries)</strong></summary>

- [ ] Frontend/external clients do NOT access storage directly; all access via governed APIs
- [ ] Core logic does NOT bypass repository interfaces to talk to storage
- [ ] Policy checks occur at the boundary (authz + redaction/generalization as needed)
- [ ] Any new endpoint includes audit fields (who/what/when/why) where required

</details>

---

## UI / Map / Story UX changes (fill out if applicable)
- **User-facing behavior changes (map/story interactions):**
- **A11y checks done:** <!-- keyboard nav, contrast, labels, focus order -->
- **Performance impact:** <!-- loading, tile rendering, query latency -->
- **Evidence-first UX:** <!-- how does UI expose evidence/citations? -->
- **Telemetry/analytics changes (if any):**

---

## Security and privacy
- **Threat model updated/considered:** <!-- link or notes -->
- **Secrets handling:** <!-- none | updated; confirm no secrets in repo -->
- **PII/PHI handling:** <!-- none | fields touched; mitigation -->
- **Dependency risk:** <!-- new deps? versions? -->

---

## Risk and rollback
- **Impact surface:** <!-- who/what is affected -->
- **Risk level:** <!-- Low | Medium | High -->
- **Failure modes to watch:** 
- **Rollback plan:** <!-- steps + what “rollback complete” means -->
- **Feature flag(s):** <!-- if used -->

---

## Testing
- **Unit tests:** <!-- what + link to results -->
- **Integration tests:** 
- **E2E tests (UI/API):** 
- **Data validation runs (if data changed):** 
- **Reproduction steps (local):** 
- **CI status:** <!-- paste summary, not walls of logs -->

---

## Deployment notes
- **Config changes:** 
- **Migrations:** <!-- DB/data migrations + reversibility -->
- **Infrastructure changes:** 
- **Observability:** <!-- logs/metrics/traces/alerts -->
- **Post-deploy checks:** <!-- explicit checklist -->

---

## Definition of done
- [ ] Scope matches linked issue/story node(s)
- [ ] Governance/evidence documented (cite-or-abstain)
- [ ] Tests added/updated and passing
- [ ] Docs updated where behavior changed
- [ ] Rollback plan exists and is plausible
- [ ] No sensitive data leaked; redaction/generalization applied where required
- [ ] Required reviewers added (e.g., governance / security / data steward as applicable)

<!-- Optional: a short release note for changelog -->
### Release note (optional)
- 
