---
title: "🧾 Kansas Frontier Matrix — Governance Assertions (E2E Regression) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "tests/e2e/web-app/regression/governance/assertions/README.md"

version: "v11.2.6"
last_updated: "2025-12-14"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous Systems Oversight · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Testing Utility Guide"
header_profile: "standard"
footer_profile: "standard"
intent: "tests-e2e-web-app-regression-governance-assertions"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

semantic_document_id: "kfm-tests-e2e-web-app-regression-governance-assertions-readme"
doc_uuid: "urn:kfm:tests:e2e:web-app:regression:governance:assertions:readme:v11.2.6"
event_source_id: "ledger:tests/e2e/web-app/regression/governance/assertions/README.md"
immutability_status: "version-pinned"
machine_extractable: true

classification: "Public Document"
sensitivity: "Low"
public_exposure_risk: "Low"
fair_category: "F1-A1-I2-R3"
care_label: "Public · Low-Risk"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../../releases/v11.2.6/tests-e2e-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/tests-e2e-v11.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ttl_policy: "6-month review"
sunset_policy: "Superseded upon next v12 E2E framework update"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
  - "sensitive-coordinate-disclosure"
  - "pii-insertion"
  - "secret-insertion"

provenance_chain:
  - "tests/e2e/web-app/regression/governance/assertions/README.md@v11.2.6"
---

<div align="center">

# 🧾 **Governance Assertions (E2E Regression) (v11 LTS)**
`tests/e2e/web-app/regression/governance/assertions/README.md`

**Purpose**  
Define the **canonical assertion layer** used by governance regression E2E suites to verify:
- FAIR+CARE routing (tiers, labels, gating),
- sovereignty masking invariants (no precision leaks),
- restricted-state UX behavior (redacted/masked/blocked),
- provenance/telemetry surfaces (IDs, hashes, safe artifacts).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Surface-Web%20App%20E2E-blueviolet" />
<img src="https://img.shields.io/badge/Governance-FAIR%2BCARE-orange" />
<img src="https://img.shields.io/badge/Policy-Assertion%20Layer-informational" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

[⬅️ Governance Regression](../README.md) ·
[🧰 Governance Utils](../utils/README.md) ·
[🕵️ Leak Checks](../utils/leak_checks/README.md) ·
[🧭 E2E Guide](../../../README.md)

</div>

---

## 📘 Overview

Governance assertions are **shared, high-signal checks** that make policy regressions obvious and merge-blocking.

They exist to prevent two common failure modes:
- **Policy drift**: UI behavior subtly changes and stops enforcing governance constraints.
- **Assertion drift**: specs scatter one-off checks that become inconsistent, flaky, or unsafe.

### What belongs in this folder

This folder SHOULD contain assertion helpers for:

- **CARE tier UI**: tier labels, gating banners, routing messages.
- **Sovereignty masking UI**: “masked/generalized” indicators, redaction states.
- **Restricted UX**: blocked panels, safe fallbacks, no “expand to raw payload” paths.
- **Provenance surfaces**: evidence chips, IDs/hashes, safe links (no full payload dumps).
- **Leak invariants**: “no coordinate-like precision appears anywhere” (often delegates to leak checks).
- **Telemetry invariants**: required test facets are emitted in safe shapes (summary-only).

### What does *not* belong here

- Full fixture payloads (use `../utils/fixtures/` or scenario fixtures).
- Network request mocking (use `../utils/navigation/` and runner-level interception).
- Snapshot storage (use `../artifacts/` templates and redaction workflow).

---

## 🗂️ Directory Layout

~~~text
📁 tests/
└── 📁 e2e/
    └── 📁 web-app/
        └── 📁 regression/
            └── 📁 governance/
                ├── 📁 assertions/
                │   ├── 📄 README.md                          — This guide (assertion conventions)
                │   ├── 📄 index.ts                           — Public export surface for assertions
                │   │
                │   ├── 📄 care.assertions.ts                 — CARE tier labels, gating, routing assertions
                │   ├── 📄 sovereignty.assertions.ts          — Masking/generalization/restricted-state assertions
                │   ├── 📄 provenance.assertions.ts           — Evidence chips, IDs/hashes, safe linking
                │   ├── 📄 telemetry.assertions.ts            — Telemetry facets + safe summary checks
                │   ├── 📄 ui_safety.assertions.ts            — “No unsafe expansions / no raw payload UI” checks
                │   │
                │   └── 📁 __tests__/                         — Unit tests for assertion utilities (optional)
                │       └── 📄 assertions.spec.ts
                │
                ├── 📁 utils/                                 — Navigation/parsing/selectors/waits/leak checks
                └── 📁 artifacts/                             — Report templates + redaction workflow
~~~

Notes:
- Filenames above represent the **canonical intent**; repo language and naming may vary.
- Keep `index.ts` stable: E2E specs should import from a single surface where possible.

---

## 🧭 Context

### Assertion design rules (deterministic + auditable)

Assertions MUST:
- be deterministic (no dependence on “now” unless time is injected),
- be event-driven (wait for a specific UI-ready state, not arbitrary sleeps),
- fail with actionable messages (include scenario ID, selector anchor, expected vs actual),
- avoid collecting or logging full raw payloads.

Assertions SHOULD:
- be minimal and composable (“one assertion = one invariant”),
- accept a `scenario_id` (or equivalent) for diagnostics,
- delegate leak-pattern checks to `../utils/leak_checks/` rather than duplicating regexes.

### Safety rules (non-negotiable)

Assertions MUST NOT:
- print full network responses into CI logs,
- embed real-looking coordinates in expected values,
- write unredacted artifacts to `reports/` or `artifacts/`,
- create allowlist bypasses for convenience.

If an assertion needs to capture evidence:
- capture a **hash** of the content and a **small redacted snippet** (optional),
- rely on the redaction pipeline under `../artifacts/redaction/`.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Spec selects scenario"] --> B["Navigate and wait for ready state"]
  B --> C["Run governance assertions"]
  C --> D["Run leak checks (if required)"]
  D --> E["Write redacted artifacts"]
  E --> F["Emit telemetry summary"]
  F --> G["CI gate: pass or block"]
~~~

Interpretation:
- Governance assertions are placed after readiness, before artifact publishing, and they integrate with leak checks and redaction.

---

## 🧪 Validation & CI/CD

Governance assertions are expected to be **merge-blocking** when they fail.

Recommended usage pattern:
- `@governance` suites call:
  - CARE assertions,
  - sovereignty/masking assertions,
  - restricted-state assertions,
  - provenance presence assertions,
  - leak checks (block severity).

### Flake policy (strict)

- If assertions are flaky, fix waits/readiness logic in `../utils/waits/`.
- Do not “stabilize” by loosening assertions or adding broad allowlists.
- Retries are discouraged for governance suites unless explicitly tracked and approved.

### Assertion coverage requirements (recommended minimum)

Governance regression SHOULD include at least:
- 1 CARE tier scenario (Tier A/B/C simulation as appropriate)
- 1 masked/generalized scenario (H3-safe behavior)
- 1 restricted scenario (blocked/redacted UX)
- 1 provenance presence scenario (IDs/hashes visible; no raw payload)

---

## 📦 Data & Metadata

### Canonical assertion interface (recommended)

Keep assertion helpers consistent and easy to compose.

~~~ts
export type GovernanceAssertionContext = {
  scenarioId: string;
  pageName: string;
  runId?: string;
};

export async function assertCareTierBadge(
  ctx: GovernanceAssertionContext,
  args: { expectedTier: "Tier A" | "Tier B" | "Tier C" }
): Promise<void> {
  // implementation in care.assertions.ts
}
~~~

### Recommended assertion groups

- `assertCareTierBadge(...)`
- `assertSovereigntyFlagVisible(...)`
- `assertMaskedPrecisionInvariant(...)` (often delegates to leak checks)
- `assertRestrictedStateFallback(...)`
- `assertProvenanceChipsPresent(...)`
- `assertTelemetryFacetSummary(...)`

### What to log on failure (safe diagnostics)

Failures SHOULD include:
- `scenarioId`
- a stable selector or page object anchor
- expected vs actual (non-sensitive)
- artifact reference paths (redacted artifacts only)

Failures MUST NOT include:
- raw coordinates
- raw geometry dumps
- full response bodies
- secrets, tokens, headers

---

## 🌐 STAC, DCAT & PROV Alignment

Assertions produce test outcomes (not datasets).

- **DCAT**: assertion reports can be treated as `dcat:Distribution` artifacts (`mediaType: application/json`).
- **STAC**: if represented, use non-spatial STAC Items (`geometry: null`) with assets pointing to redacted reports.
- **PROV-O**:
  - an assertion run is a `prov:Activity` in the E2E run chain,
  - assertion utilities and rules are `prov:Entity`,
  - CI runner and maintainers are `prov:Agent`.

---

## 🧱 Architecture

### Where assertions sit in the governance stack

Governance E2E enforcement is layered:

1. **Selectors & waits** (stable UX readiness)
2. **Assertions** (semantic invariants: tiers, badges, restricted UX)
3. **Leak checks** (pattern-based invariants: “no precision leakage”)
4. **Redaction** (artifact safety boundary)
5. **Telemetry** (summary signals for dashboards and audits)

Assertions should remain small and focused on semantic invariants, while leak checks focus on pattern detection.

---

## ⚖ FAIR+CARE & Governance

Governance assertions uphold:

- **Authority to Control**: verifies restricted states stay restricted and precision never leaks.
- **Responsibility**: prevents unsafe regressions from merging “because tests passed.”
- **Ethics**: ensures public-facing narrative/governance surfaces remain safe and respectful.
- **Collective Benefit**: makes compliance observable and consistent across teams.

If a governance assertion fails:
- treat it as a **stop-ship** for affected governed surfaces,
- fix UI/API enforcement first,
- keep assertions strict and deterministic (do not weaken them as a shortcut).

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v11.2.6 | 2025-12-14 | Initial governance assertions guide aligned to KFM‑MDP v11.2.6 (deterministic, safe diagnostics, integrates with leak checks + redaction). |

<div align="center">

[🏛️ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT License  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>

