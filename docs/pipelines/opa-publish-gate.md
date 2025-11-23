---
title: "🔏 KFM v11 — OPA Publish-Gate Policy Standard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/pipelines/opa-publish-gate.md"
version: "v11.1.0"
last_updated: "2025-11-23"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/pipelines-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-opa-gate-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active · Enforced"
doc_kind: "Pipeline Governance Standard"
semantic_document_id: "kfm-opa-publish-gate-v11"
doc_uuid: "urn:kfm:standards:pipelines:opa-publish-gate:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🔏 **KFM v11 — OPA Publish-Gate Policy Standard**  
`docs/standards/pipelines/opa-publish-gate.md`

**Purpose:**  
Define the mandatory OPA (Open Policy Agent) **publish-gate** that controls dataset promotion  
from **staging → published** within the Kansas Frontier Matrix.  
Promotion is only allowed when **all** metadata, provenance, lineage, ethics, and compliance gates  
return `allow = true`.

</div>

---

# 📘 1. Overview

The KFM v11 OPA publish-gate is the enforcement layer ensuring:

- FAIR+CARE ethics  
- STAC / DCAT validity  
- Provenance completeness (SLSA + OpenLineage)  
- SBOM + checksum registry coherence  
- Data-steward & governance approvals  
- Vertical Axis / CRS compliance  
- No promotion without accountability  

This gate is **non-bypassable**. CI/CD halts if any `deny` rule triggers.

---

# 🧩 2. Required OPA Input Schema

Pipelines MUST supply the following JSON structure to OPA:

~~~json
{
  "dataset": {
    "id": "",
    "license": ""
  },
  "approvals": {
    "data_steward": false,
    "governance_council": false
  },
  "attestations": {
    "slsa": true,
    "sbom_spdx": ""
  },
  "checksums": {
    "manifest_zip": "",
    "primary_tar": ""
  },
  "faircare": {
    "ethics_pass": false
  }
}
~~~

Fields may be **extended**, never removed.

---

# 🔐 3. Rego Policy (data.kfm.publish)

OPA policy MUST be stored at:

```
policy/kfm_publish.rego
```

And MUST follow this canonical implementation:

~~~rego
package kfm.publish

default allow = false

deny[msg] {
  input.dataset.license != "CC-BY-4.0"
  msg := "license not approved"
}

deny[msg] {
  not input.approvals["data_steward"]
  msg := "missing steward approval"
}

deny[msg] {
  not input.approvals["governance_council"]
  msg := "missing governance council approval"
}

deny[msg] {
  not input.attestations["slsa"]
  msg := "missing SLSA attestation"
}

deny[msg] {
  not input.attestations["sbom_spdx"]
  msg := "missing SPDX SBOM"
}

deny[msg] {
  failed := {k | some k; input.checksums[k] == null}
  count(failed) > 0
  msg := "checksum registry incomplete"
}

deny[msg] {
  not input.faircare["ethics_pass"]
  msg := "FAIR+CARE ethics screen failed"
}

allow {
  not deny[_]
}
~~~

---

# ⚙️ 4. CI/CD Integration (v11)

## 4.1 Evaluate Policy

~~~bash
opa eval --format=json \
  --data policy/kfm_publish.rego \
  --input ci/publish_input.json \
  'data.kfm.publish'
~~~

## 4.2 Fail Build on Denial

~~~bash
result=$(opa eval -f values -d policy/kfm_publish.rego -i ci/publish_input.json 'data.kfm.publish.allow')
[ "$result" = "true" ] || { echo "Publish blocked"; exit 1; }
~~~

## 4.3 Display Human-Readable Denials

~~~bash
opa eval -f values -d policy/kfm_publish.rego -i ci/publish_input.json 'data.kfm.publish.deny'
~~~

---

# 📁 5. Recommended Repository Layout

```text
policy/
  kfm_publish.rego

ci/
  publish_input.json

.github/workflows/
  publish.yml
```

---

# 🚀 6. Minimal GitHub Actions Workflow

~~~yaml
name: publish
on: [workflow_dispatch]

jobs:
  gate:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: open-policy-agent/setup-opa@v2

    - name: Evaluate policy
      run: |
        opa eval -f values \
          -d policy/kfm_publish.rego \
          -i ci/publish_input.json \
          'data.kfm.publish.deny' > denies.txt

        if [ -s denies.txt ]; then
          echo "::error::Publish blocked"
          cat denies.txt
          exit 1
        fi

    - name: Promote
      run: ./scripts/promote.sh
~~~

---

# 🔮 7. KFM-Specific Extensions (v11.x Roadmap)

Future KFM minor releases may extend this policy with:

- STAC structural gating  
- Vertical Axis / CF Z-axis validation  
- H3 generalization checks for archaeology  
- Carbon & energy telemetry gating  
- Story Node v3 metadata completeness  
- Focus Mode v3 safe-narrative gates  
- AI bias / risk / drift gating  
- SBOM → SLSA → checksum equivalence gates  
- Lineage depth checks

All follow the `deny[…]` pattern.

---

# 🧭 8. Responsibilities

- **Pipeline owners** must populate publish_input.json  
- **Governance Council** must document and approve gating rules  
- **Security team** maintains Rego logic + CI integration  
- **FAIR+CARE team** ensures ethics results are correctly passed  
- **Release managers** ensure promotion is blocked if OPA denies

---

# 🕰 9. Version History

- **v11.1.0 (2025-11-23)** — Upgraded to KFM-MDP v11 format, added minor clarifications.  
- **v11.0.0** — Initial version.

---

<div align="center">

**Kansas Frontier Matrix — OPA Publish-Gate (v11)**  
*Deterministic · Governed · FAIR+CARE-Aligned*

</div>

---

### 🔗 Footer  
[⬅ Back to Standards](../../README.md) · [🛡 Security Standards](../security/README.md) · [🏛 Governance](../governance/ROOT-GOVERNANCE.md)
