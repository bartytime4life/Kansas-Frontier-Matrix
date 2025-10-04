<div align="center">

# 🧪 Kansas Frontier Matrix — Testing & Validation Standards  
`docs/standards/testing.md`

**Purpose:** Establish unified **testing, validation, and quality assurance standards**  
for all code, data, metadata, and workflows in the **Kansas Frontier Matrix (KFM)** — ensuring  
that every function, dataset, and system component meets **MCP compliance** for reproducibility  
and provenance-based auditing.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-blue)](../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue)](../../LICENSE)

</div>

---

## 📚 Overview

Testing and validation are the foundation of **KFM’s reproducible architecture**.  
All pipelines, datasets, and web systems undergo continuous verification to ensure:
- ✅ Deterministic, reproducible outputs  
- 🧾 Provenance and integrity documentation  
- 🔍 Automated CI/CD validation  
- 🧠 Compliance with open data and metadata standards  
- 🧩 Full traceability from raw inputs to published results  

Testing operates at multiple levels — **unit, integration, data validation, and system testing** —  
and is enforced by both manual review and automated workflows.

---

## 🧩 Testing Framework Overview

```mermaid
graph TD
  A["🧱 Unit Tests\n(src/tests/)"] --> B["⚙️ Integration Tests\n(pipelines + APIs)"]
  B --> C["🧾 Data Validation Tests\n(checksums, metadata)"]
  C --> D["🧠 System & CI/CD Tests\n(GitHub Actions)"]
  D --> E["✅ QA & Governance Review\n(manual audit)"]

  style A fill:#eef7ff,stroke:#0077cc
  style B fill:#fff0f5,stroke:#cc0088
  style C fill:#ecf9f0,stroke:#33aa33
  style D fill:#fffbea,stroke:#e8a500
  style E fill:#f0e8ff,stroke:#8844cc
````

<!-- END OF MERMAID -->

---

## 🧱 Test Levels & Requirements

| Level                 | Purpose                                              | Tool / Framework                          | Required? |
| :-------------------- | :--------------------------------------------------- | :---------------------------------------- | :-------- |
| **Unit Tests**        | Validate individual functions and modules.           | `pytest`, `unittest`                      | ✅         |
| **Integration Tests** | Test multi-component workflows and ETL sequences.    | `pytest`, `make test-pipeline`            | ✅         |
| **Data Validation**   | Confirm data, metadata, and schema integrity.        | `jsonschema`, `stac-validator`, `hashlib` | ✅         |
| **Performance Tests** | Assess runtime efficiency and scalability.           | Custom profiling, logging                 | Optional  |
| **Security Tests**    | Detect vulnerabilities and access violations.        | `CodeQL`, `Trivy`, `Bandit`               | ✅         |
| **CI/CD Tests**       | Validate automated workflows and builds.             | GitHub Actions                            | ✅         |
| **QA Review**         | Manual validation of output quality and consistency. | Governance checklist                      | ✅         |

---

## ⚙️ Unit Testing Standards

| Requirement    | Description                                      | Example                            |
| :------------- | :----------------------------------------------- | :--------------------------------- |
| **Framework**  | All unit tests use `pytest`.                     | `pytest src/tests/`                |
| **Naming**     | Test files prefixed with `test_`.                | `test_terrain_pipeline.py`         |
| **Coverage**   | Minimum 90% of code lines.                       | Enforced by CI/CD.                 |
| **Assertions** | Use explicit comparison (`assert`) statements.   | `assert dem.shape == (1000, 1000)` |
| **Fixtures**   | Use for reusable inputs.                         | Temporary files, mock datasets.    |
| **Logs**       | Tests output logs under `data/work/logs/tests/`. | Recorded automatically.            |

### Example Unit Test

```python
def test_checksum_integrity(tmp_path):
    """Validate checksum generator produces correct hash."""
    from utils.checksum import sha256_file
    file = tmp_path / "test.txt"
    file.write_text("Kansas Frontier Matrix")
    hash_value = sha256_file(file)
    assert len(hash_value) == 64
```

---

## 🔗 Integration Testing Standards

| Area                  | Focus                                                | Example Test                                           |
| :-------------------- | :--------------------------------------------------- | :----------------------------------------------------- |
| **Pipeline Workflow** | Test end-to-end ETL process.                         | `make terrain` followed by checksum + STAC validation. |
| **Data Provenance**   | Verify lineage consistency across metadata and STAC. | STAC links match source manifests.                     |
| **File Outputs**      | Confirm expected directory structure and naming.     | Output files exist and validated by CI/CD.             |
| **API / Web**         | Test API endpoints and layer rendering.              | Validate responses in `api/v1/` routes.                |

Integration tests should use **test datasets** stored under:

```
data/tests/
├── terrain/
├── hydrology/
└── climate/
```

---

## 🧾 Data Validation & Integrity Testing

### 1️⃣ Checksum Validation

Ensure all data products match their integrity hashes.

```bash
make checksums
sha256sum -c data/checksums/**/*.sha256
```

### 2️⃣ Metadata Validation

Validate STAC metadata against schema.

```bash
make stac-validate
stac-validator data/stac/terrain/ks_1m_dem_2018_2020.json
```

### 3️⃣ Schema Validation

Confirm JSON and CSV files follow proper schemas.

```bash
python -m jsonschema -i data/processed/tabular/census_population_1860_2020.json schema/tabular_schema.json
```

---

## 🧮 System & End-to-End Testing

System testing validates full workflows and deployments:

* Data ingestion → processing → STAC metadata → web deployment.
* Executes via **Makefile orchestration** and CI/CD.

**Example Command:**

```bash
make all
pytest --maxfail=1 --disable-warnings -q
```

**Validation Checks:**

| Category             | Verification                                     |
| :------------------- | :----------------------------------------------- |
| **ETL Output**       | All processed datasets exist and pass checksums. |
| **STAC Validation**  | All metadata validated.                          |
| **CI/CD Logs**       | Workflows completed successfully.                |
| **Web Viewer Build** | Map layers render correctly.                     |

---

## 🧰 Security & CI/CD Validation

| Tool                       | Function                                    | Frequency        |
| :------------------------- | :------------------------------------------ | :--------------- |
| **CodeQL**                 | Static code analysis                        | Weekly           |
| **Trivy**                  | Dependency and container vulnerability scan | Weekly           |
| **Bandit**                 | Python security linting                     | On PR            |
| **Pre-Commit Hooks**       | Linting, formatting, YAML validation        | Every commit     |
| **STAC Validate Workflow** | Metadata and checksum testing               | On push and PR   |
| **Site Deploy Workflow**   | Web and docs build verification             | On merge to main |

---

## 🧾 Governance & QA Testing

Manual QA ensures MCP compliance and quality assurance.

| Area                     | Reviewer         | Validation Tool                |
| :----------------------- | :--------------- | :----------------------------- |
| **Data Provenance**      | Data Steward     | `docs/templates/provenance.md` |
| **Metadata Consistency** | Metadata Curator | `stac-validator`               |
| **ETL Accuracy**         | Data Engineer    | Pipeline logs                  |
| **Documentation**        | Technical Writer | `docs/templates/checklist.md`  |
| **Web Visualization**    | UI/UX Reviewer   | MapLibre Test Instance         |

Results must be logged under:

```
data/work/logs/qa/<dataset>_review.log
```

---

## 🧠 MCP Compliance Summary

| MCP Principle           | Implementation                                               |
| :---------------------- | :----------------------------------------------------------- |
| **Documentation-first** | All test cases and results documented before approval.       |
| **Reproducibility**     | Deterministic test environments and reproducible builds.     |
| **Open Standards**      | All tools open-source (pytest, STAC validator, JSON Schema). |
| **Provenance**          | Tests capture dataset lineage, logs, and commit references.  |
| **Auditability**        | Validation evidence stored in logs and CI/CD artifacts.      |

---

## 📎 Related Documentation

| File                                  | Description                                                  |
| :------------------------------------ | :----------------------------------------------------------- |
| `docs/standards/coding.md`            | Coding standards and best practices for testing integration. |
| `docs/standards/validation.md`        | Validation rules and criteria for datasets and metadata.     |
| `docs/templates/checklist.md`         | Template for QA and MCP compliance review.                   |
| `.github/workflows/stac-validate.yml` | Metadata and integrity validation workflow.                  |
| `.github/workflows/codeql.yml`        | Code security testing workflow.                              |

---

## 📅 Version History

| Version | Date       | Author                        | Summary                                                     |
| :------ | :--------- | :---------------------------- | :---------------------------------------------------------- |
| v1.0    | 2025-10-04 | KFM QA & Data Governance Team | Initial comprehensive testing standards for MCP compliance. |

---

<div align="center">

**Kansas Frontier Matrix** — *“Every Test Logged. Every Validation Proven.”*
📍 [`docs/standards/testing.md`](.) · Official testing and validation standards under the Master Coder Protocol.

</div>
