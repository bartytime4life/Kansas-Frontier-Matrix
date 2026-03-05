<!--
PARTIAL__EVIDENCE_REF_BLOCK.md

Purpose
- A drop-in, fill-in block for attaching **resolvable** evidence (EvidenceRefs → EvidenceBundles) to
  a claim, decision, or narrative sentence.

Rules of use
- Every non-trivial claim MUST declare `claim_status`: CONFIRMED / PROPOSED / UNKNOWN.
- If you cannot provide resolvable EvidenceRefs, set `claim_status: UNKNOWN` and list the smallest
  verification steps needed to make it CONFIRMED.
- Do not paste raw restricted content. Only include policy-safe references + metadata.
-->

---

**Evidence references (required)**

Citations in KFM are not “URLs in prose.” A citation must resolve to an **immutable dataset version**
and an **evidence span** (via an EvidenceRef) so a reviewer can open the Evidence drawer and inspect
license/rights, policy, provenance, and checksums.

<!-- Duplicate this block per claim/decision as needed. Keep it close to the claim it supports. -->

| Field | Value |
| --- | --- |
| claim_status | `CONFIRMED` / `PROPOSED` / `UNKNOWN` |
| claim | `TBD` (1 sentence; no hedging if CONFIRMED) |
| evidence_refs | `TBD` (one per line; MUST be resolvable when CONFIRMED) |
| evidence_bundle_id(s) | `TBD` (e.g., `sha256:bundle...`) |
| dataset_version_id(s) | `TBD` (immutable IDs) |
| license + attribution | `TBD` (SPDX + required attribution text) |
| policy_label | `TBD` (e.g., `public`, `restricted`) |
| obligations_applied | `TBD` (redactions/generalizations applied) |
| freshness | `TBD` (last run timestamp OR source publication date) |
| provenance_run_id | `TBD` (e.g., `kfm://run/...`) |
| audit_ref | `TBD` (e.g., `kfm://audit/...`) |
| validation | `TBD` (catalog_valid, links_ok, etc.) |

**EvidenceRef scheme examples** (use project canonical IDs; parseable without network calls)

- `doc://sha256:<ocr_text_digest>#page=<N>&span=<start>:<end>`
- `dcat://<dataset_id>@<dataset_version_id>`
- `stac://<collection_or_item_id>#asset=<asset_key>`
- `prov://<run_or_activity_id>`
- `graph://<entity_or_claim_id>`

<details>
<summary>Optional: machine-readable snippet (copy/paste)</summary>

~~~yaml
claim_id: "<optional stable id>"
claim_status: "CONFIRMED"
claim: "<one sentence>"

evidence_refs:
  - "doc://sha256:...#page=12&span=1832:1935"

# If you have a resolved EvidenceBundle, capture its stable IDs here.
resolved_evidence:
  bundle_id: "sha256:bundle..."
  dataset_version_id: "<dataset_version_id>"
  policy:
    decision: "allow"        # allow | deny
    policy_label: "public"   # public | restricted | ...
    obligations_applied: []   # e.g., geometry_generalized, text_redacted
  license:
    spdx: "CC-BY-4.0"
    attribution: "<required attribution text>"
  provenance:
    run_id: "kfm://run/..."
  artifacts:
    - href: "<policy-allowed href or redacted>"
      digest: "sha256:..."
      media_type: "<mime>"
  checks:
    catalog_valid: true
    links_ok: true
  audit_ref: "kfm://audit/..."

verification_steps_if_unknown:
  - "<smallest step to make this CONFIRMED>"
  - "<what evidence you expect to produce (EvidenceRef type + where)>"
~~~

</details>

**If `claim_status: UNKNOWN`**

List the *smallest* verification steps to make the claim CONFIRMED (and what evidence you expect).

- [ ] `TBD`
