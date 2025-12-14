---
title: "🧬 KFM — Release Validation Provenance (v<semver>) · PROV-O · OpenLineage · Audit Links"
path: "docs/analyses/remote-sensing/validation/reports/releases/v<semver>/provenance/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing Board · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Index + Policy"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

intent: "remote-sensing-validation-release-provenance"
audience:
  - "Remote Sensing Engineering"
  - "Science QA Reviewers"
  - "Data Engineering"
  - "Reliability Engineering"
  - "Governance Reviewers"

classification: "Public"
sensitivity: "General (non-sensitive) unless overridden by dataset labels"
sensitivity_level: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "Remote Sensing Board · FAIR+CARE Council"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

release_semver: "v<semver>"
release_commit_sha: "<release-commit-sha>"

doc_uuid: "urn:kfm:doc:analyses:remote-sensing:validation:reports:releases:v<semver>:provenance:index:v11.2.6"
semantic_document_id: "kfm-remote-sensing-validation-release-provenance-v<semver>"
event_source_id: "ledger:docs/analyses/remote-sensing/validation/reports/releases/v<semver>/provenance/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "diagram-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🧬 **KFM — Release Validation Provenance**
`docs/analyses/remote-sensing/validation/reports/releases/v<semver>/provenance/README.md`

**Purpose**  
This folder provides the **provenance pointers** and (optionally) **in-repo provenance bundles**
that prove how the release validation package for **v<semver>** was produced:
inputs used, activities executed, agents involved, and outputs generated.

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Reports Releases" src="https://img.shields.io/badge/Reports-Releases-blue" />
<img alt="Provenance PROV OpenLineage" src="https://img.shields.io/badge/Provenance-PROV%20%2B%20OpenLineage-informational" />
<img alt="Status Active Enforced" src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />
<img alt="FAIR+CARE Policy Aware" src="https://img.shields.io/badge/FAIR%2BCARE-Policy--Aware-gold" />

</div>

---

## 📘 Overview

Release provenance is used to:

- prove **what** was validated (inputs, versions, digests),
- prove **how** it was validated (activities, parameters, configs),
- prove **who/what** did it (agents: runners, CI, reviewers),
- prove **what** was generated (summaries, manifests, evidence).

This folder SHOULD remain **small** and **safe**. If full provenance bundles are large or sensitive, store them as governed assets and reference them here by stable id + digest.

---

## 🗂️ Directory Layout

~~~text
📁 docs/analyses/remote-sensing/validation/reports/releases/v<semver>/provenance/      — Release provenance pointers and (optional) bundles
├── 📄 README.md                                                                      — This policy/index
├── 🧾 provenance.index.json                                                          — Pointer registry (ids + digests) (recommended)
├── 🧾 prov.bundle.jsonld                                                             — Consolidated PROV-O bundle (optional; keep small)
├── 🧾 openlineage.events.json                                                        — Consolidated OpenLineage events (optional; keep small)
├── 🧾 slsa.attestation.json                                                          — SLSA provenance attestation (optional; if in-repo)
└── 📁 signatures/                                                                    — Detached signatures (optional)
    ├── 📄 README.md                                                                  — Signature notes and verification guidance
    └── 🧾 <artifact>.sig                                                             — Detached signature files (example)
~~~

Notes:

- Filenames are illustrative. Include only what the release produces.
- If provenance is stored elsewhere (preferred for large bundles), `provenance.index.json` should reference those artifacts by stable identifier + digest.

---

## ✅ What belongs here

Release provenance artifacts SHOULD be:

- pointers to PROV/OpenLineage bundles,
- small, consolidated provenance bundles when safe,
- attestation references (SLSA) and signature references (if used),
- deterministic ids and digests that bind the release report to its lineage.

Recommended minimum pointers:

- PROV-O JSON-LD bundle reference (or stable id)
- OpenLineage run id(s)
- validation config snapshot digest
- input pack manifest digest
- output manifest digest

---

## ⛔ What must NOT be committed here

Do NOT include:

- secrets (tokens, credentials, private endpoints),
- signed URLs,
- raw data payloads,
- precise coordinates or restricted location descriptors,
- massive logs or full trace dumps.

If provenance includes restricted context:

- store it as a governed artifact outside public docs,
- reference only via stable id + digest,
- record redaction/suppression outcomes in the release summary.

---

## 🧾 Recommended index: `provenance.index.json`

This file SHOULD enumerate provenance references for the release bundle.

Illustrative shape:

~~~json
{
  "index_kind": "release_provenance_index",
  "index_version": "v1",
  "release_version": "v<semver>",
  "release_commit_sha": "<sha>",
  "created_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "governance": {
    "care_gate_status": "allow|redact|deny",
    "sovereignty_gate": "clear|restricted|conflict|unknown",
    "redaction_summary": {"events_total": 0, "reasons": []}
  },
  "runs": [
    {
      "run_id": "urn:kfm:run:<...>",
      "openlineage_run_id": "urn:uuid:<...>",
      "prov_bundle_ref": "prov.bundle.jsonld|urn:kfm:prov:<...>",
      "prov_bundle_sha256": "<sha256>",
      "inputs_manifest_ref": "../manifests/input_pack.manifest.json",
      "config_snapshot_ref": "../manifests/config_snapshot.json"
    }
  ],
  "attestations": [
    {
      "kind": "slsa",
      "ref": "slsa.attestation.json|urn:kfm:attestation:<...>",
      "sha256": "<sha256>"
    }
  ],
  "agents": [
    {"agent_id": "urn:kfm:agent:ci", "type": "software"},
    {"agent_id": "urn:kfm:agent:reviewer:<...>", "type": "person"}
  ]
}
~~~

---

## 🔗 PROV-O expectations (release level)

If a consolidated `prov.bundle.jsonld` is stored here, it SHOULD include:

- `prov:Entity`:
  - input pack (declared inputs),
  - config snapshot,
  - output manifest,
  - release summary,
  - evidence index.
- `prov:Activity`:
  - validation run(s),
  - drift comparison to baseline (if applicable),
  - report assembly (release-level bundling).
- `prov:Agent`:
  - CI runner,
  - pipeline runner,
  - any human reviewers (as agents, if captured and governed).

Minimum relations:

- `prov:used` (activities used inputs/config)
- `prov:wasGeneratedBy` (outputs generated by activities)
- `prov:wasAssociatedWith` (activities associated with agents)
- `prov:wasDerivedFrom` (release outputs derived from inputs/baseline)

---

## 🔁 OpenLineage expectations (release level)

If `openlineage.events.json` is stored here, it SHOULD include:

- run id(s) linked to:
  - release version and commit,
  - job/task names for validation,
  - input datasets,
  - output artifacts.

If full OpenLineage events are stored elsewhere, this folder SHOULD instead include:

- stable pointers to those events (id + digest),
- minimal metadata to connect release summary ↔ OpenLineage run ids.

---

## 🎯 Determinism requirements (non-negotiable)

Provenance pointers MUST be reproducible:

- stable sorting (runs, agents, attestations),
- stable ids (urns) where possible,
- stable digests (sha256),
- no host-dependent paths, timestamps, or random ids beyond run ids.

If the provenance chain cannot be proven:

- release gate SHOULD fail closed unless governance override is recorded with signed justification.

---

## 🛡️ FAIR+CARE and sovereignty posture

Provenance can itself be a leakage vector.

Rules:

- do not include precise coordinates in provenance payloads stored in repo,
- do not include restricted dataset identifiers if policy forbids,
- treat agent metadata carefully (avoid personal emails; prefer urn identifiers),
- record redaction events as counts + reason codes.

---

## 🧪 CI/CD expectations (recommended)

CI MAY enforce:

- if `provenance.index.json` exists:
  - referenced files exist and digests match,
  - no forbidden patterns (secrets, signed URLs, coordinates),
  - required pointers exist (at minimum: run id(s), prov ref, config snapshot ref).
- if `prov.bundle.jsonld` exists:
  - validate against a PROV profile schema (when provided),
  - ensure it references release manifests and summary.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Initial governed policy for release validation provenance; defined pointer index expectations, PROV/OpenLineage conventions, determinism posture, and governance-safe publication rules. |

---

<div align="center">

<img alt="KFM-MDP v11.2.6" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img alt="Provenance PROV OpenLineage" src="https://img.shields.io/badge/Provenance-PROV%20%2B%20OpenLineage-informational" />

[⬅ Release Report](../README.md) ·
[🧾 Manifests](../manifests/README.md) ·
[📦 Evidence](../evidence/README.md) ·
[🏷 Releases Index](../../README.md) ·
[🧾 Reports Index](../../../README.md) ·
[🧩 Methods](../../../../methods/README.md) ·
[🏛️ Governance Charter](../../../../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⬅ Docs Index](../../../../../../../README.md)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
