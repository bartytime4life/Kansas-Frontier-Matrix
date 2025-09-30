<div align="center">

# 🌾 Kansas-Frontier-Matrix — Code of Conduct

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../.github/workflows/trivy.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../.github/workflows/automerge.yml)

**Mission:** Foster a welcoming, respectful, and collaborative  
community in line with the **Contributor Covenant v2.1**.

[Contributor Covenant v2.1 — Full Text](https://www.contributor-covenant.org/version/2/1/code_of_conduct/)

</div>

---

## 🤝 Our Standards

- Be respectful and inclusive — no harassment or discrimination  
- Assume good intent; provide constructive feedback  
- Accept critique gracefully; disagree without hostility  
- Collaborate openly and transparently  
- Recognize contributions from all community members  

---

## 🚫 Unacceptable Behavior

- Harassment, insults, or derogatory comments  
- Discriminatory language or exclusionary behavior  
- Public or private intimidation, stalking, or threats  
- Disruptive trolling or deliberate derailment of discussions  
- Sharing sensitive information without consent  

---

## 📑 Community Expectations

Kansas-Frontier-Matrix has additional norms rooted in our **Master Coder Protocol (MCP)** and project culture:

- **Reproducibility first** → every dataset, experiment, or workflow must be documented and reproducible  
- **Documentation-driven development** → README files, SOPs, and schemas are living lab notebooks, not afterthoughts  
- **Provenance matters** → checksums, STAC metadata, and logs ensure traceability across time and space  
- **Transparency in decisions** → roadmap, governance, and design discussions are captured in issues/PRs  
- **Respect for history & culture** → Indigenous perspectives, oral traditions, and archival integrity are treated with care  
- **Collaboration over competition** → reviewers, maintainers, and contributors work as peers in a shared knowledge hub  

---

## 🔄 Enforcement Lifecycle

```mermaid
flowchart TD
  A["Behavior observed"] --> B["📩 Report privately\n(security@kansasfrontier.org or maintainer DM)"]
  B --> C["🔎 Maintainer review\nassess context + intent"]
  C --> D["⚖️ Action taken\nwarning · mediation · removal if needed"]
  D --> E["📢 Feedback loop\ncommunicate decision to reporter + involved parties"]

<!-- END OF MERMAID -->



⸻

🛡️ Enforcement Responsibilities
	•	Maintainers are responsible for clarifying and enforcing standards
	•	They may remove, edit, or reject contributions that violate this code
	•	Maintainers may issue warnings, impose temporary restrictions, or remove violators from the project

⸻

📬 Reporting
	•	Preferred contact: 📧 security@kansasfrontier.org
	•	Alternatively: Direct message a project maintainer privately
	•	Reports are handled confidentially; reporter identities are protected

⸻

⚖️ Consequences

Depending on severity, maintainers may:
	•	Issue a private or public warning
	•	Request an apology or corrective action
	•	Temporarily restrict participation in the project
	•	Remove access or ban from participation

⸻

🧭 Maintainer Guidelines

Maintainers are expected to model MCP values in addition to enforcing conduct:
	•	Documentation-first → every new feature, workflow, or dataset must include or update a README/schema
	•	Reproducibility → ensure changes can be regenerated from make targets; avoid one-off/manual work
	•	Provenance → all new data requires checksums, STAC items, or metadata sidecars
	•	CI hygiene → workflows must be pinned, least-privilege, and artifact outputs must be validated
	•	Transparency → design and governance decisions logged in issues/PRs, not in private chats
	•	Mentorship → guide contributors in MCP practices (schemas, provenance, docs)
	•	Consistency → enforce branch protection, review rigor, and coding/documentation standards

By following these guidelines, maintainers uphold both the social trust and the technical integrity of the project.

⸻

⚙️ How This Links to CI

Contributor behavior and MCP alignment are tied directly to automation:
	•	Respectful, well-documented contributions → faster reviews and smoother merges
	•	Reproducibility and provenance → fewer CI failures (STAC validate, schema checks, provenance hashes)
	•	CI hygiene → automerge eligibility once all required checks pass
	•	Transparency in PRs → better roadmap syncing and milestone tracking

👉 In short: good conduct = smoother pipelines = faster integration.

⸻

🌍 Attribution

This Code of Conduct is adapted from the Contributor Covenant v2.1.

⸻

✅ Summary

Kansas-Frontier-Matrix is committed to a safe, respectful, reproducible, and inclusive environment.
Contributors and maintainers alike share responsibility for upholding these values and practicing MCP principles.