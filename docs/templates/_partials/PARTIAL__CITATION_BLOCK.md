<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/9a3a27a8-3a9e-4c88-9e6e-0f67e9a7a0b9
title: PARTIAL Citation Block
type: standard
version: v1
status: draft
owners: ["@Kansas-Frontier-Matrix/core"]
created: 2026-03-04
updated: 2026-03-04
policy_label: public
related: []
tags: ["kfm","template","partial","citations","evidence","provenance"]
notes: ["Drop-in evidence + citations block for Story Nodes, reports, and Focus Mode outputs."]
[/KFM_META_BLOCK_V2] -->

<!--
FILE: docs/templates/_partials/PARTIAL__CITATION_BLOCK.md

PURPOSE
- Provide a consistent, auditable “evidence boundary” for any KFM user-facing output.
- Support “cite-or-abstain” and “every meaningful claim gets a status label.”

USAGE
- Paste/include this block at the end of any Story Node / report / Focus Mode answer.
- Fill placeholders. If you cannot cite, mark claims UNKNOWN and list the smallest verification steps.
-->

## Evidence & citations

> **Rule (KFM):** Every meaningful claim must be labeled **CONFIRMED**, **PROPOSED**, or **UNKNOWN**.  
> If **UNKNOWN**, list the smallest verification steps to make it **CONFIRMED**.

### Context

| field | value |
|---|---|
| doc_ref | <!-- e.g., docs/stories/FOO.md or kfm://story/<id> --> |
| output_kind | <!-- Story Node / Focus Mode answer / QA report / ADR / etc. --> |
| generated_by | <!-- human / Focus Mode / pipeline --> |
| generated_at | <!-- ISO 8601, e.g., 2026-03-04T18:22:00Z --> |
| audit_ref | <!-- REQUIRED: kfm://audit/<id> OR CI run URL OR trace/span id --> |
| commit_sha | <!-- git SHA for the generating code/content --> |
| policy_ref | <!-- policy bundle/version, e.g., kfm://policy/<id> or policy/commit --> |
| policy_label | <!-- public / restricted / internal --> |
| sensitivity | <!-- public / low / moderate / high / needs_governance_review --> |
| redactions_applied | <!-- none / yes (link to redaction report) --> |

### Minimum completion checklist

- [ ] Each **CONFIRMED** claim maps to at least **one** source in **Sources cited**.
- [ ] Each **UNKNOWN** claim has **verification_steps_if_unknown** filled.
- [ ] `audit_ref` is present (or explicitly **UNKNOWN** with a concrete “how to get it” step).
- [ ] `policy_label` + `sensitivity` are filled (or marked **needs_governance_review**).
- [ ] Any derived artifacts include **sha256** (or are explicitly out-of-scope).

---

### Claim register

<details>
<summary><strong>Claims, status, and evidence mapping</strong></summary>

| claim_id | claim | status | evidence_refs | verification_steps_if_unknown | notes |
|---|---|---|---|---|---|
| C-001 | <!-- Claim text (atomic, testable) --> | CONFIRMED | <!-- e.g., S-001 p.12; D-003; STAC:item:foo --> | <!-- if UNKNOWN: “open S-001; confirm X; record page” --> | <!-- optional --> |
| C-002 | <!-- ... --> | PROPOSED | <!-- sources backing the proposal/rationale --> | <!-- if UNKNOWN --> | |
| C-003 | <!-- ... --> | UNKNOWN | <!-- empty or partial refs --> | <!-- smallest steps to confirm --> | |

</details>

---

### Sources cited

<details>
<summary><strong>Source list</strong></summary>

> **How to fill**  
> - Prefer authoritative, original sources.  
> - Include a stable locator and a precise pointer (page/section/line/time range).  
> - Record license and integrity (checksum/etag) when feasible.

| source_id | citation | locator | accessed_at | license | checksum_or_etag | notes |
|---|---|---|---|---|---|---|
| S-001 | <!-- Author/Org. Title. Publisher, date. --> | <!-- URL OR repo-relative path; add page/section --> | <!-- YYYY-MM-DD --> | <!-- SPDX or text --> | <!-- sha256/etag if known --> | |
| S-002 | <!-- ... --> | <!-- ... --> | <!-- ... --> | <!-- ... --> | <!-- ... --> | |

</details>

---

### Catalog & provenance links

<details>
<summary><strong>Catalog triplet and run lineage</strong></summary>

> **Goal:** Make “what the user sees” traceable to catalogs and provenance artifacts.

- **STAC** (items/collection): <!-- e.g., data/<dataset>/stac/collection.json -->
- **DCAT** (dataset/distributions): <!-- e.g., data/<dataset>/dcat/dataset.jsonld -->
- **PROV** (run provenance): <!-- e.g., data/<dataset>/prov/run-<id>.jsonld -->
- **Run / build record**: <!-- CI URL, run_id, trace id -->

</details>

---

### Artifacts and digests

<details>
<summary><strong>Artifacts referenced by this output</strong></summary>

| artifact_id | artifact | role | uri | sha256 | produced_by | notes |
|---|---|---|---|---|---|---|
| A-001 | <!-- file name --> | data | <!-- oci://…@sha256:… OR s3://… OR path --> | <!-- sha256:… --> | <!-- prov:Activity / run --> | |
| A-002 | <!-- ... --> | evidence | <!-- ... --> | <!-- ... --> | <!-- ... --> | |

</details>

---

### Policy decisions and constraints

<details>
<summary><strong>Policy decisions applied to this output</strong></summary>

| decision_id | decision | rationale | policy_ref | applied_to | notes |
|---|---|---|---|---|---|
| P-001 | <!-- e.g., “Redacted precise coordinates” --> | <!-- why; risk/sensitivity --> | <!-- docs/governance/... --> | <!-- section/field --> | |
| P-002 | <!-- ... --> | <!-- ... --> | <!-- ... --> | <!-- ... --> | |

</details>

---

### Verification TODOs

> Use this section to convert **UNKNOWN → CONFIRMED** with minimal, concrete steps.

- [ ] TODO-001: <!-- e.g., “Locate primary source for X; add S-003 with page pointer; update C-003.” -->
- [ ] TODO-002: <!-- ... -->

---

[Back to top](#evidence--citations)

<!-- END PARTIAL -->
