# 🔒🧪 Integrity Artifacts (Experiment Report Template)

> **Goal:** make every result in this example report **provable, reproducible, and tamper-evident** — so reviewers can *trust but verify*.

This directory captures the “receipts” for the experiment report: hashes, manifests, policy outputs, provenance, and (optionally) cryptographic signatures. It follows KFM’s **contract-first + provenance-first** rule: anything that shows up in the UI or AI outputs must be traceable to cataloged sources and provable processing, with **no mystery layers**.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## ✅ What “Integrity” means here

Integrity in this template is **multi-layered**:

- **Byte integrity**: hashes prove files weren’t altered.
- **Process integrity**: run manifests + deterministic pipelines prove *how* outputs were generated (and can be regenerated).  [oai_citation:1‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Governance integrity**: policy gates enforce “must-have” rules (FAIR/CARE, citations, sensitivity propagation, secrets scanning) and fail closed.  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **Narrative integrity**: any human-facing narrative or AI output must carry citations/evidence, or refuse.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 📦 Suggested folder structure (recommended)

```text
mcp/dev_prov/examples/10_experiment_report_template/(example_report_tree)/
└─ artifacts/
   └─ integrity/
      ├─ README.md
      ├─ manifests/
      │  ├─ run_manifest.json
      │  ├─ provenance.prov.jsonld
      │  ├─ evidence_manifest.(yml|json)
      │  ├─ sbom.spdx.json                # optional (recommended)
      │  └─ slsa.provenance.json          # optional (recommended)
      ├─ checksums/
      │  ├─ SHA256SUMS.txt
      │  └─ checksums.json                # optional (structured)
      ├─ policy/
      │  ├─ conftest_report.json
      │  └─ policy_snapshot/              # frozen policy inputs used to verify
      ├─ signatures/
      │  ├─ cosign.bundle.json            # optional (keyless)
      │  └─ attestations/                 # optional (referrers, SBOMs)
      ├─ oci/
      │  └─ distribution.oci.json         # optional (if artifacts stored in OCI)
      └─ health/
         ├─ graph_health_summary.md       # optional (if graph-backed)
         └─ graph_health_index.csv        # optional (trend log)
```

---

## 🧾 Core artifacts (minimum bar)

### 1) `manifests/run_manifest.json`
A run manifest is the experiment’s **single source of truth**: who/what/when, inputs, outputs, tool versions, counts, errors, etc. (KFM treats these manifests as audit ledger artifacts).  [oai_citation:4‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

**Strongly recommended:** canonicalize JSON and embed a SHA-256 self-fingerprint (`canonical_digest`) so the manifest becomes an immutable identifier.  [oai_citation:5‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 2) `checksums/SHA256SUMS.txt`
A flat list of `sha256` hashes for every artifact in the report bundle.

### 3) `manifests/provenance.prov.jsonld`
A PROV record that links:
- raw inputs → transforms → outputs
- agents (human + automation) → activities
- parameters/configs → results

KFM’s “boundary artifacts” philosophy expects PROV lineage as part of “publishable” outputs.  [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 4) `policy/conftest_report.json`
A frozen copy of governance checks (OPA/Conftest) run against the report and its metadata. Policy packs make governance machine-checkable and enforceable.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧠 Evidence manifests (for narratives + AI outputs)

If the report contains conclusions, story text, charts, or model-driven statements, include an **evidence manifest**. This is the pattern used for KFM narratives (including Pulse Threads): each cited fact links to source datasets/queries, and a manifest captures the raw references underpinning the narrative.  [oai_citation:8‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

**Rule of thumb:** if a human would ask “how do we know?”, the answer belongs in `evidence_manifest.*`.

---

## 🧰 Verification checklist (how to validate locally)

### A) Verify hashes ✅
```bash
cd mcp/dev_prov/examples/10_experiment_report_template/(example_report_tree)/artifacts/integrity
sha256sum -c checksums/SHA256SUMS.txt
```

### B) Verify manifest self-hash ✅
- Canonicalize `run_manifest.json` (RFC 8785 JCS) and confirm the computed SHA-256 equals `canonical_digest`.  [oai_citation:9‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

> Tip: if you don’t have a JCS tool handy, treat this as a CI responsibility and still store the digest + the tool/version used to compute it (inside the manifest).

### C) Run policy gates ✅
OPA + Conftest policies are intended to block merges when required fields / citations / classifications are missing.  [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

```bash
# Example (paths vary by repo conventions)
conftest test -p policy/policy_snapshot manifests/ checksums/ --output json > policy/conftest_report.json
```

### D) (Optional) Verify signatures ✅
If artifacts are distributed via OCI, use ORAS + Cosign:
- OCI gives immutable digests and tags; digest pinning guarantees exact bytes.  [oai_citation:11‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- Cosign signatures provide cryptographic integrity + origin verification.  [oai_citation:12‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

```bash
# Pull by digest (preferred) via ORAS
oras pull oci://<registry>/<repo>@sha256:<digest>

# Verify signature (example; exact flags depend on your policy)
cosign verify --keyless oci://<registry>/<repo>@sha256:<digest>
```

Catalog-side, OCI distributions can be referenced in metadata (e.g., `distribution.oci`) with registry/repo/tag/digest and links to referrers for signatures/SBOMs.  [oai_citation:13‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🩺 (Optional) Graph integrity health checks (if graph-backed)

If your experiment writes to or depends on a knowledge graph, you can snapshot “graph health” as integrity artifacts. KFM proposes weekly graph health checks that act like unit tests for the graph (counts deltas, constraints/index integrity, orphan detection, schema drift, backup verification), with outputs stored as timestamped artifacts and a `summary.md` linking to details.  [oai_citation:14‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

Put those outputs in `health/` so the experiment report can be audited *end-to-end*.

---

## 🧭 How this ties back to KFM design principles

### Provenance-first pipelines 🧬
- Raw data treated as immutable evidence; changes happen downstream in controlled stages.  [oai_citation:15‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- Deterministic, config-driven processing supports reproducibility and idempotence.  [oai_citation:16‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  

### Policy as code ⚖️
Governance rules (FAIR/CARE, security, citations, sensitivity propagation) are expressed in OPA/Rego and enforced in CI with Conftest.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### AI integrity 🤖
Focus Mode-style AI must **always cite sources**, and must refuse or express uncertainty if it cannot ground an answer in data.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### UI transparency 🗺️
KFM’s mapping/UI roadmap includes a “Layer Provenance” concept—surfacing sources, license info, and provenance summaries per active layer—so integrity artifacts aren’t hidden from users.  [oai_citation:19‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 🧩 Why this matters even more for “future-KFM” features

As KFM evolves toward time-aware 4D exploration and immersive interfaces (digital twins, AR overlays, etc.), integrity artifacts become the *trust anchor* for what users see and “time-travel” through.  [oai_citation:20‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

---

## 🧷 “Done means…” (acceptance criteria)

✅ This `integrity/` folder is considered complete when:

- [ ] `checksums/SHA256SUMS.txt` exists and validates cleanly
- [ ] `manifests/run_manifest.json` exists and includes tool versions + digest (recommended)  [oai_citation:21‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- [ ] `manifests/provenance.prov.jsonld` exists (or equivalent provenance bundle)  [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] `policy/conftest_report.json` exists and indicates pass (or includes explicit waivers)
- [ ] If narratives/claims exist → `evidence_manifest.*` exists and citations resolve  [oai_citation:23‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- [ ] If distributed artifacts exist → OCI digest pinned + signature verification path documented  [oai_citation:24‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 📚 Project library touchpoints (used by this template)

> These docs shaped the integrity rules and examples captured here:

- 🧭🤖 **AI System Overview** (AI must cite + refuse if ungrounded)  [oai_citation:25‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- 📥 **Data Intake Guide** (immutability, deterministic ETL, provenance-first publishing)  [oai_citation:26‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- 🏗️ **Architecture / Governance** (OPA+Conftest policy packs + automated gates)  [oai_citation:27‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- 🧾 **Run manifests + canonical hashing** (RFC 8785 + SHA-256 self-fingerprint)  [oai_citation:28‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- 📦 **OCI artifacts + ORAS + Cosign** (digest pinning + signature verification)  [oai_citation:29‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- 🩺 **Graph health checks** (summary.md + index.csv + saved artifacts)  [oai_citation:30‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- 🗺️ **UI transparency / provenance panel idea**  [oai_citation:31‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
- 🧱 **Contract-first + no mystery layers**  [oai_citation:32‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- 🧠 **Evidence manifests for narratives (Pulse Threads / Story Nodes)**  [oai_citation:33‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
- 🕰️ **Future-facing 4D/AR concepts** (integrity becomes even more important)  [oai_citation:34‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  

### 📎 Included reference bundles (portfolios / libraries)
These are part of the project’s broader knowledge base and are intentionally carried alongside the template:

- 📦 AI Concepts portfolio  [oai_citation:35‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)  
- 🌍 Maps / WebGL / geospatial visualization portfolio  [oai_citation:36‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  
- 🧰 Programming languages & resources portfolio  [oai_citation:37‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  
- 🗄️ Data management / data science portfolio  [oai_citation:38‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  
- 🧭 Geospatial analysis cookbook excerpt (example of reproducible geospatial pipelines)  [oai_citation:39‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)  

---

## 🛠️ Troubleshooting (quick hits)

- **Hash mismatch:** rebuild artifacts from the pinned inputs; do not “hotfix” outputs (immutability boundary).  [oai_citation:40‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- **Policy failure:** treat like a failing unit test; fix metadata/citations/classification rather than bypassing.  [oai_citation:41‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- **Missing citations:** AI/narratives must refuse or be marked uncertain; add evidence manifest or remove the claim.  [oai_citation:42‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  

---

### 🧠✨ Motto
**No receipts, no results.**
