- Example:  
`feat(nlp): add date range normalization for 19th-century diaries`

### Pull Requests
- Must pass CI checks (lint, tests, schema validation).
- Must link to an **issue** or **roadmap milestone**.
- Include a **short summary** + screenshots (if UI).

---

## 3. Data Handling

- **Raw data** → `data/raw/`
- **Processed data** → `data/processed/`
- **STAC Items** → `stac/items/`

### Conventions
- All rasters must be converted to **COG (Cloud-Optimized GeoTIFF)**.
- All vectors must be **GeoJSON in EPSG:4326**.
- Every artifact must have a **`.sha256` checksum sidecar**.
- Provenance metadata must include:
- Source URL or citation
- Ingest date
- Checksum
- CRS and schema details

---

## 4. Code Quality

- **Python**:  
- Use `black`, `ruff`, and `mypy` (checked in pre-commit + CI).
- Docstrings required for public classes and functions.
- **Web**:  
- Config-driven (no hard-coded styles).
- Validate configs with JSON schema (`web/config/*.schema.json`).
- **Tests**:  
- Every new module must include at least one `pytest` unit test.
- Target: **80%+ coverage** on core ingestion + NLP logic.

---

## 5. Documentation

- Every new feature requires:
- Update to relevant `README.md`.
- If substantial, an addition to `docs/`.
- Use **Mermaid diagrams** for flows (data ingest, graph building, etc.).
- Keep all docs **Markdown-only** for GitHub readability.

---

## 6. CI/CD & Automation

- GitHub Actions workflows in `.github/workflows/`:
- **CI**: lint, test, build.
- **stac-validate**: validate STAC collections/items.
- **site.yml**: build + deploy MapLibre site.
- Pre-commit hooks must pass locally before pushing.
- Dependabot auto-updates dependencies weekly.

---

## 7. Security & Ethics

- No sensitive or restricted data should be committed.
- All datasets must be **open license (CC0/CC-BY)** or documented.
- Follow CARE principles for Indigenous data governance.
- Ensure visualizations avoid misrepresentation of sensitive sites.

---

## 8. Release Process

1. Update `VERSION` and `CHANGELOG.md`.
2. Ensure all tests + CI pass.
3. Create GitHub Release with:
 - Tag `vX.Y.Z`
 - Summary of changes
 - Links to docs
4. Deployment to GitHub Pages triggers automatically.

---

## 9. Emergency Procedures

- **Broken main branch**:  
- Revert to last passing commit.  
- File an incident issue tagged `critical`.
- **Corrupted data**:  
- Mark dataset as deprecated in STAC collection.  
- Replace with corrected artifact.  
- Update checksums and provenance.

---

## 10. Contact & Governance

- Maintainers: [Project Core Team]
- Issues: GitHub Issues (`bug`, `feature`, `question` labels).
- Roadmap: `.github/roadmap/roadmap.yaml`

---

✅ **Mission-grade principle**:  
Every commit, dataset, and visualization must be **traceable, reproducible, and ethically sound**.
