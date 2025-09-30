<div align="center">

# 🚀 Pull Request — Kansas-Frontier-Matrix

Thank you for contributing to **Kansas-Frontier-Matrix**!  
Please use this template to ensure your PR is **reproducible, documented, and MCP-compliant**.

</div>

---

## 📝 Summary

<!-- Describe your changes in 1–3 sentences. Focus on outcomes, not just files touched. -->

---

## 🔗 Related Issues / Roadmap

- Closes #<!-- issue ID -->  
- Relates to epic/milestone: <!-- e.g., m25q4, epic-web-v1 -->

---

## 📂 What Changed

<!-- High-level overview. Examples:
- Added new DEM source descriptors under `data/sources/dem/`
- Converted 1930s topo maps to COG + checksums
- Updated `roadmap.yaml` with milestone m25q4
-->

---

## ✅ Contributor Checklist

Before requesting review, confirm the following:

- [ ] **Docs updated** — added/updated `README.md` in affected directories  
- [ ] **Schemas validated** — ran `make prebuild` (schema + STAC + site config check)  
- [ ] **Provenance tracked** — checksums (`.sha256`) + STAC items added for new data  
- [ ] **Tests passing** — ran `pytest -q` locally (if applicable)  
- [ ] **Security posture** — no secrets committed; workflows least-privilege  
- [ ] **Roadmap alignment** — issue/epic/milestone referenced in `roadmap.yaml` (if applicable)  
- [ ] **Commit hygiene** — small, focused commits with imperative messages (`Closes #123`)  
- [ ] **Community standards** — Code of Conduct & MCP values observed (reproducibility, documentation-first, provenance)  

---

## 🔍 Reviewer Notes (for maintainers)

- CI must be ✅ (STAC validate, web config validate, CodeQL, Trivy, secret scanning)  
- Provenance checks (SHA-256, STAC metadata) in place for new/updated data  
- Docs & schemas consistent with project conventions  
- Roadmap & labels synced (`.github/roadmap/roadmap.yaml`, `.github/labels.yml`)  
- PR scope small and focused  

---

## 📖 References

- [Contributing Guide](./CONTRIBUTING.md)  
- [Code of Conduct](./CODE_OF_CONDUCT.md)  
- [Security Policy](./SECURITY.md)  
- [Roadmap](./roadmap/README.md)  