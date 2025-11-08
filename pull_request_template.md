<div align="center">

# 🚀 Kansas Frontier Matrix — Pull Request Template
`/.github/pull_request_template.md`

**Purpose:** Ensure all contributions meet KFM standards for reproducibility, provenance, FAIR/CARE ethics, and documentation-first workflows.

</div>

---

## 📌 Summary

<!-- Provide a short summary of the PR's purpose and changes -->

- 
- 

---

## ✅ Checklist

- [ ] Follows [MCP documentation-first protocol](../docs/standards/mcp.md)
- [ ] Updates/additions are documented in `/docs` (architecture, models, SOPs, etc.)
- [ ] All code changes include relevant unit/integration tests
- [ ] Metadata updated (e.g., `data/sources/*.json`, `model_card.md`, `stac/*.json`)
- [ ] Passed `make docs-validate`, `make test`, or CI checks locally
- [ ] For sensitive or Indigenous data: reviewed for [FAIR+CARE](../docs/standards/faircare.md)

---

## 🧠 Description of Changes

<!-- Bullet point major changes made. Include what files/modules were affected. -->

- 
- 

---

## 🧪 How to Test

<!-- Explain how a reviewer can test this PR locally -->

```bash
# Example:
make setup && make serve
# or
python -m pipelines.etl.noaa_climate.run
```

---

## 📂 Affected Areas

- [ ] `src/etl/`
- [ ] `src/graph/`
- [ ] `src/ai/models/`
- [ ] `src/api/`
- [ ] `web/`
- [ ] `data/`
- [ ] `docs/`
- [ ] Other:

---

## 📚 Related Issues / Linked Docs

Closes: #123  
Related: [docs/architecture/data-architecture.md](../docs/architecture/data-architecture.md)

---

## 🧬 Metadata (If Applicable)

- STAC Item(s): updated [yes/no]
- DCAT Dataset(s): linked [yes/no]
- Model Card: [yes/no] — updated `docs/models/model_card.md`
- CARE Review: [yes/no] — reviewer: `@tribal-reviewer` or `@ethics-admin`

---

## 📝 Notes for Reviewers

<!-- Anything reviewers should focus on, be aware of, or questions you have -->

> ℹ️ Example: "Does this new STAC extension schema align with our v1.0?"

---

## 📜 Version History

| Version | Date       | Author       | Notes                    |
|---------|------------|--------------|--------------------------|
| v0.1.0  | 2025-11-08 | @yourhandle  | Initial PR template push |

