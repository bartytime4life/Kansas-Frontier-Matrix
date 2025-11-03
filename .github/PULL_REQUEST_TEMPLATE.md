---
title: "🔀 Kansas Frontier Matrix — Pull Request Template (FAIR+CARE / MCP-DL v6.3 Compliant)"
path: ".github/PULL_REQUEST_TEMPLATE.md"
version: "v9.6.0"
last_updated: "2025-11-03"
review_cycle: "Continuous / Autonomous"
governance_ref: "../docs/standards/governance/DATA-GOVERNANCE.md"
license: "MIT"
---

# 🔀 Kansas Frontier Matrix — **Pull Request Template**
This PR template enforces FAIR+CARE ethics, governance traceability, and reproducibility in all changes submitted to the Kansas Frontier Matrix (KFM) repository.  
Please complete each section carefully. Every PR undergoes automated FAIR+CARE validation, checksum verification, and provenance ledger registration.

---

## 🧾 Summary
**Describe the purpose of this pull request.**  
Explain what functionality, data, or documentation this update introduces or modifies.

> _Example: Adds new climate ETL transformation logic and FAIR+CARE schema validation pipeline._

---

## 🧩 Type of Change
Select all that apply (mark with `x`):

- [ ] 🧠 Feature (new pipeline, tool, or dataset)
- [ ] 🧰 Refactor (non-breaking code improvements)
- [ ] 🧪 Validation (schema, FAIR+CARE, or checksum)
- [ ] ⚙️ Governance (provenance, ledger, or SBOM update)
- [ ] 🧾 Documentation (MCP-DL or Markdown updates)
- [ ] ♻️ Sustainability / Telemetry (ISO or carbon tracking)
- [ ] 🧱 Infrastructure / CI-CD (workflow or GitHub Actions)

---

## ⚙️ Related Issues / References
_Link to existing issues, data contracts, or documentation affected._

- Related Issue(s): `#<issue-number>`
- Affected Data Contracts:  
  - [ ] `docs/contracts/data-contract-v3.json`
  - [ ] `schemas/telemetry/*`
- Associated Governance Records:  
  - [ ] `reports/audit/*`
  - [ ] `reports/fair/*`

---

## 🧠 FAIR+CARE Compliance
**Confirm this contribution upholds the FAIR+CARE ethical standards.**  
For details, see [FAIR+CARE Validation Guide](../docs/standards/faircare-validation.md).

| Principle | Compliance | Notes |
|------------|-------------|-------|
| **Findable** | ✅ / ⚠️ / ❌ | _Indexed and documented properly?_ |
| **Accessible** | ✅ / ⚠️ / ❌ | _Open format and license alignment?_ |
| **Interoperable** | ✅ / ⚠️ / ❌ | _Schema and metadata compliant?_ |
| **Reusable** | ✅ / ⚠️ / ❌ | _Versioned, reproducible, and documented?_ |
| **Collective Benefit** | ✅ / ⚠️ / ❌ | _Ethical use and community impact verified?_ |
| **Authority to Control** | ✅ / ⚠️ / ❌ | _FAIR+CARE Council approval or review needed?_ |
| **Responsibility** | ✅ / ⚠️ / ❌ | _Transparent and traceable workflow?_ |
| **Ethics** | ✅ / ⚠️ / ❌ | _Non-bias, inclusion, and consent maintained?_ |

---

## 🔍 Validation Checklist
Ensure all required validation and governance checks are complete before requesting review.

- [ ] ✅ **Pre-commit validation:** `make pre-commit`
- [ ] ✅ **Schema validation:** `make validate-schema`
- [ ] ✅ **Checksum verification:** `make checksum-verify`
- [ ] ✅ **FAIR+CARE audit:** `make faircare-validate`
- [ ] ✅ **Governance sync:** `make governance-ledger`
- [ ] ✅ **Telemetry update:** `make telemetry-report`
- [ ] ✅ **Documentation review:** `make docs-validate`

---

## ⚖️ Governance & Provenance
Provide references for provenance and governance registration related to this update.

| Record Type | Reference Path |
|--------------|----------------|
| Provenance Ledger | `reports/audit/data_provenance_ledger.json` |
| FAIR+CARE Audit | `reports/fair/data_care_assessment.json` |
| Manifest / SBOM | `releases/v9.6.0/manifest.zip` |
| Telemetry Metrics | `releases/v9.6.0/focus-telemetry.json` |

---

## 🧩 Reviewer Assignments
| Reviewer | Area | Role |
|-----------|------|------|
| @kfm-data | Data Pipelines | Technical Review |
| @kfm-fair | FAIR+CARE Council | Ethics Review |
| @kfm-governance | Provenance & Ledger | Governance Validation |
| @kfm-security | CI/CD & Security | Security Compliance |
| @kfm-architecture | Docs & Design | MCP-DL Conformance |

---

## 🧾 Post-Merge Actions
After approval and merge, ensure the following tasks are completed:

- [ ] Update provenance and manifest (`make governance-ledger`)
- [ ] Publish SBOM and checksum manifest (`make checksum-publish`)
- [ ] Update telemetry metrics (`make telemetry-report`)
- [ ] Notify FAIR+CARE Council if new ethics review required
- [ ] Announce in project changelog (`CHANGELOG.md`)

---

### 🪶 Sign-Off

By submitting this pull request, I certify that:
- All code and data align with FAIR+CARE governance and MCP-DL v6.3 standards.
- No private, sensitive, or proprietary data are included.
- All changes are documented, traceable, and ethically validated.

**Contributor:**  
`@<github-username>`  
**Date:** `<YYYY-MM-DD>`  
**Affiliation:** `Kansas Frontier Matrix / Open FAIR+CARE Network`

---

<div align="center">

**Kansas Frontier Matrix** · *Open Science × Ethical AI × Provenance Governance*  
[🔗 Repository](https://github.com/bartytime4life/Kansas-Frontier-Matrix) • [🧭 Docs Portal](../docs/) • [⚖️ Governance Ledger](../docs/standards/governance/)

</div>
