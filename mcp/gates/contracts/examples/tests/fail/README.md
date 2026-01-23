# ❌ Fail Fixtures — Gate Contract Negative Tests

![Policy](https://img.shields.io/badge/policy-fail--closed-critical) ![Suite](https://img.shields.io/badge/suite-negative%20fixtures-important) ![Contracts](https://img.shields.io/badge/contracts-contract--first-blue) ![Provenance](https://img.shields.io/badge/provenance-required-informational) ![Governance](https://img.shields.io/badge/governance-enforced-brightgreen) ![Security](https://img.shields.io/badge/security-supply%20chain%20aware-yellow)

> [!WARNING]
> Everything in this folder is **supposed to fail**.  
> If something in `fail/` passes a gate, that’s a **bug** 🐛 (or the contract/policy got weakened).

---

## 🧭 What this folder is

This directory contains **negative (failing) fixtures** used to prove our gates are real gates — not suggestions.

- ✅ `pass/` = “known-good” examples that must always pass  
- ❌ `fail/` (this folder) = “known-bad” examples that must always fail

📌 The goal: **make regressions loud**. If someone loosens a rule (accidentally or otherwise), these tests should catch it immediately.

🔗 Related:
- `../pass/README.md` (positive fixtures)
- `../../README.md` (gate runner overview, if present)
- `../../policy/` (OPA/Rego + other policy logic, if present)

---

## 🧱 Gate philosophy this suite enforces

These failing fixtures are designed around KFM’s core invariants:

- ⛓ **Provenance-first**: no “mystery layers” / no untraceable outputs  
- 🧾 **Contract-first**: schemas & contracts are non-negotiable  
- 🧪 **Evidence-first**: “show your work” metadata is required  
- 🧠 **AI-with-citations**: Focus Mode outputs must carry citations + pass governance checks  
- 🧑‍⚖️ **FAIR+CARE**: sensitive/cultural data requires special handling  
- 🔐 **Secure-by-default**: supply-chain & attestation checks can block promotion  
- 🧬 **Graph integrity**: Neo4j & linked metadata must remain consistent

So this folder includes failure cases across:
📥 intake • 🗺 UI/story • 🧠 AI • 🔐 security • 🧬 graph • 🧑‍🤝‍🧑 CARE/sensitivity • 📦 artifact delivery

---

## 📁 Folder layout

```text
mcp/
└── 🚪 gates/
    └── 📜 contracts/
        └── 🧪 examples/
            └── 🧫 tests/
                ├── ✅ pass/                     # ✅ Fixtures that MUST pass (baseline compliant examples)
                │   └── 📄 README.md             # 📘 What “pass” covers + how to add new passing cases safely
                └── ❌ fail/                     # ❌ Fixtures that MUST fail (proves deny rules work)
                    ├── 📄 README.md             # 👈 you are here 📌 How fail fixtures are structured + expected findings/codes
                    ├── 🧩 fixtures/             # (optional) Organize failing inputs by domain (data/prov/ai/ui/security)
                    └── 🧾 cases.*               # (optional) Case manifest/index (runner-specific: yml/json/toml)
```

---

## ▶️ How to run (typical patterns)

Your exact runner may differ, but **fail fixtures should run in CI** and locally.

### Option A — OPA / Conftest style
```bash
# Example shape (adjust paths):
conftest test . \
  --policy ../../policy \
  --all-namespaces
```

### Option B — pytest / custom harness
```bash
pytest -q mcp/gates/contracts/examples/tests -k "fail"
```

### Expected behavior ✅
- Running `fail/` alone should produce a **non-zero exit code**
- Running the whole suite should treat `fail/` as **expected failures**:
  - pass fixtures must pass ✅
  - fail fixtures must fail ❌ (and preferably with expected violation codes)

---

## 🧩 Fixture conventions (recommended)

Keep negative tests **small, deterministic, and single-purpose**.

### ✅ Naming pattern
Use names that instantly tell you **what broke**:
```text
<domain>__<rule>__<case>__v<major>.<ext>
```

Examples:
- `metadata__license_required__missing_license__v1.dcat.json`
- `prov__chain_required__missing_activity__v1.prov.json`
- `ai__citations_required__no_citations__v1.answer.json`
- `ui__storynode_valid__missing_mapstate__v1.story.json`

### ✅ “Expected violation” sidecar (strongly encouraged)
Pair each bad fixture with a minimal expected output file:
```text
<fixture> + <fixture>.expect.json
```

Example:
```text
ai__citations_required__no_citations__v1.answer.json
ai__citations_required__no_citations__v1.answer.json.expect.json
```

Suggested `.expect.json` shape:
```json
{
  "must_fail": true,
  "must_include_codes": ["AI_CITATIONS_REQUIRED"],
  "must_not_include_codes": ["INTERNAL_ERROR"],
  "notes": "Focus Mode answer lacks citations."
}
```

🎯 Why we do this:
- prevents false positives (fixture failing for the wrong reason)
- makes contract drift obvious (codes changed? intentional?)
- keeps error messaging stable enough to trust

---

## 🧨 Curated failure cases (what MUST be blocked)

> [!TIP]
> Keep each fixture focused on **one rule**.  
> If you break 5 rules at once, the failure is less diagnostic.

### 📥 Data Intake & Metadata Contracts
| What we’re testing | Example fixture | Typical failure signal |
|---|---|---|
| Missing required license | `metadata__license_required__missing_license__v1.dcat.json` | `LICENSE_MISSING` |
| Missing spatial/temporal extent | `metadata__extent_required__missing_extent__v1.dcat.json` | `EXTENT_MISSING` |
| Invalid STAC geometry/bbox | `stac__geometry_valid__bad_bbox__v1.stac-item.json` | `STAC_INVALID_GEOMETRY` |
| Raw bytes changed (immutability breach) | `raw__immutable__hash_mismatch__v1.manifest.json` | `RAW_HASH_MISMATCH` |
| Non-deterministic / “hand-edited” processed output | `etl__deterministic__missing_run_manifest__v1.run.json` | `RUN_MANIFEST_REQUIRED` |

### ⛓ Provenance (STAC/DCAT/PROV Alignment)
| What we’re testing | Example fixture | Typical failure signal |
|---|---|---|
| Missing PROV activity/agent link | `prov__chain_required__missing_activity__v1.prov.json` | `PROV_ACTIVITY_MISSING` |
| Broken cross-links between catalogs | `linkage__crosslayer__dangling_dataset_ref__v1.json` | `REF_NOT_FOUND` |
| Unverifiable processing step | `prov__step_required__no_processing_steps__v1.prov.json` | `PROV_STEPS_MISSING` |

### 🧠 Focus Mode / AI Governance
| What we’re testing | Example fixture | Typical failure signal |
|---|---|---|
| AI answer has claims but no citations | `ai__citations_required__no_citations__v1.answer.json` | `AI_CITATIONS_REQUIRED` |
| Prompt injection attempt not neutralized | `ai__prompt_gate__injection_payload__v1.prompt.txt` | `PROMPT_INJECTION_BLOCKED` |
| Output missing governance ledger metadata | `ai__ledger_required__no_ledger_entry__v1.answer.json` | `GOV_LEDGER_REQUIRED` |
| Bias / sensitive language rule breach | `ai__guardrails__sensitive_output__v1.answer.json` | `AI_SAFETY_RULE_VIOLATION` |
| Drift check regression (low citation coverage) | `ai__drift__citation_coverage_low__v1.metrics.json` | `DRIFT_ALERT` |

### 🗺 UI / Story Nodes / “Map Behind the Map”
| What we’re testing | Example fixture | Typical failure signal |
|---|---|---|
| Story folder missing required JSON config | `ui__storynode_valid__missing_config__v1/` | `STORY_CONFIG_REQUIRED` |
| Story JSON references missing layer ID | `ui__storynode_refs__missing_layer__v1.story.json` | `LAYER_REF_NOT_FOUND` |
| Narrative contains unsafe HTML / injection | `ui__story_md_safe__html_injection__v1.md` | `UNSAFE_MARKDOWN` |
| Layer has no attribution / license | `ui__layer_attrib_required__missing_source__v1.layer.json` | `ATTRIBUTION_REQUIRED` |

### 🔐 Supply Chain / Artifact Integrity
| What we’re testing | Example fixture | Typical failure signal |
|---|---|---|
| OCI digest mismatch | `artifact__oci__digest_mismatch__v1.oci.json` | `OCI_DIGEST_MISMATCH` |
| Missing Cosign signature | `artifact__cosign__missing_signature__v1.oci.json` | `SIGNATURE_REQUIRED` |
| Missing SBOM / SLSA attestation | `artifact__slsa__missing_attestation__v1.att.json` | `ATTESTATION_REQUIRED` |

### 🧬 Graph Integrity (Neo4j “Health Check” style)
| What we’re testing | Example fixture | Typical failure signal |
|---|---|---|
| Orphaned metadata nodes | `graph__integrity__orphaned_nodes__v1.cypher.json` | `GRAPH_ORPHAN_FOUND` |
| Constraint violation (duplicate IDs) | `graph__constraints__duplicate_ids__v1.cypher.json` | `GRAPH_CONSTRAINT_VIOLATED` |
| Index offline / missing | `graph__indexes__index_offline__v1.cypher.json` | `GRAPH_INDEX_OFFLINE` |

### 🧑‍🤝‍🧑 CARE / Sensitive Data Handling & Privacy
| What we’re testing | Example fixture | Typical failure signal |
|---|---|---|
| Sensitive site exact coords exposed publicly | `care__sensitive__exact_coords_public__v1.geojson` | `SENSITIVE_COORDS_BLOCKED` |
| Missing cultural protocol labels / authority info | `care__authority__missing_labels__v1.metadata.json` | `CARE_LABEL_REQUIRED` |
| Query output violates k-anon / inference controls | `privacy__query_audit__inference_risk__v1.query.json` | `QUERY_DENIED_PRIVACY` |

### 🤖 Agent Parity (Watcher–Planner–Executor)
| What we’re testing | Example fixture | Typical failure signal |
|---|---|---|
| “Agent PR” tries to bypass normal gates | `agent__parity__missing_prov__v1.pr.json` | `AGENT_PARITY_VIOLATION` |
| Missing idempotency key / commit seed | `agent__idempotent__missing_idempotency__v1.event.json` | `IDEMPOTENCY_REQUIRED` |
| Kill-switch ignored | `agent__killswitch__ignored__v1.run.json` | `AGENT_ACTION_BLOCKED` |

---

## ✅ Definition of Done for a new `fail/` case

When you add a new failing fixture, it’s “done” when:

- [ ] It fails **for one reason** (one primary rule) 🎯  
- [ ] It has an `.expect.json` with stable violation code(s) 🧾  
- [ ] It contains **no real secrets** / credentials / PII 🔒  
- [ ] It is minimal (small file, small diff, no massive binaries) 🪶  
- [ ] It fails consistently (no network calls, no time dependence) ⏱️  
- [ ] CI proves the gate remains **fail-closed** 🚪❌

---

## 🧯 If a fail fixture passes…

> [!IMPORTANT]
> If `fail/` passes, treat it like a **security bug** or **trust regression**.

Checklist:
1. ✅ Confirm the gate runner is pointing at the right policies/contracts
2. ✅ Ensure the fixture is actually being executed (test discovery)
3. ✅ Confirm the contract version is correct (v1 vs v2 drift)
4. ✅ If policy changed intentionally, update the `.expect.json` **with a short justification**
5. ✅ If policy changed unintentionally, revert + add a regression test

---

## 📚 Reference docs used to shape these failure cases

These gates reflect the broader project design across intake, UI, AI governance, ethics, and supply chain.

- 📘 KFM architecture & contract-first rules
- 📥 KFM data intake + CI gate philosophy
- 🗺 UI story nodes + provenance surfacing
- 🧠 AI Focus Mode governance / citations / prompt security
- 🧑‍⚖️ FAIR+CARE + sovereignty & sensitive data handling
- 📦 Artifact integrity (OCI/ORAS/Cosign) + graph health checks
- 🧰 Tooling libraries (AI concepts, mapping/WebGL, data management, programming resources)

(If you move/rename the docs folder, update links here 🔁)

---

