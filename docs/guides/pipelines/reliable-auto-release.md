---
title: "🔁 Kansas Frontier Matrix — Reliable Auto-Release Pipeline (Watchers, Idempotency, and Governance) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/reliable-auto-release.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.4.x/sbom.spdx.json"
manifest_ref: "../../releases/v10.4.x/manifest.zip"
telemetry_ref: "../../releases/v10.4.x/pipeline-telemetry.json"
telemetry_schema: "../../schemas/telemetry/reliable-auto-release-v1.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "reliable-pipelines"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R1-E1"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 🔁 **Reliable Auto-Release Pipeline — Watchers, Idempotency, and Governance**  
`docs/guides/pipelines/reliable-auto-release.md`

**Purpose:**  
Provide a **ready-to-run pattern** for continuously watching upstream sources, deterministically transforming data,  
**bumping SemVer**, generating **CHANGELOG + manifest**, and **publishing** a PR or tagged **Release** — with  
**idempotency, safety, and governance** baked in.

**Scope:**  
This guide standardizes watchers (webhooks/cron), HTTP conditional fetches (ETag/Last-Modified), schema validation,  
deterministic transforms, artifact stamping, CI/CD concurrency, retries, and notifications.

</div>

---

## ✅ Outcomes

- **Zero-duplicate** runs with **idempotent artifacts** and **deterministic versioning**  
- **Auditable** changes with `CHANGELOG.md`, SBOM, STAC/DCAT manifests, and governance links  
- **Safe** publishes gated by validation, concurrency locks, and dry-runs  
- **Observable** pipeline with run IDs, diffs, and telemetry events

---

## 🧩 Canonical Components (KFM-Standard)

- **Watcher:** HTTP webhook (preferred) or `cron` (`*/15 * * * *`)  
- **Fetcher:** Conditional GET using **ETag / If-None-Match** and **If-Modified-Since**  
- **Validator:** Schema + rules (JSON Schema, STAC, FAIR+CARE checks)  
- **Transformer:** Pure, deterministic functions (same input → same output)  
- **Versioner:** Deterministic SemVer bump (**patch/minor/major**) from classified diffs  
- **Publisher:** Pull Request or Git Tag + GitHub Release (with assets)  
- **Notifier:** Slack webhook with `run_id`, diff summary, and links  
- **Observability:** Telemetry events, run ledger, artifact fingerprints  
- **Governance:** SBOM (SPDX), manifests, attestation, CI policy gates  

---

## 🧠 Idempotency & Reliability Rules

- **Single-flight execution:** Use a **concurrency group/lock** per pipeline name + source.  
- **Deterministic run identity:**  
  `run_id = sha256(source_url + content_hash + period)`  
- **Short-circuit:** If identical artifact exists, **skip** publish; mark as **NOOP**.  
- **Bounded retries:** Exponential backoff, request timeouts, and circuit-breaker for upstream flakiness.  
- **Checkpointing:** Persist phase markers so re-runs **resume** safely.  
- **Full dry-run path:** Every phase runnable in `--dry-run` with identical logs and previews.

---

## 🗂️ Directory Layout (Excerpt, Canonical)

~~~text
.github/workflows/
└── reliable-auto-release.yml                  # CI workflow wiring watcher → pipeline

src/
└── pipelines/
    └── reliable_auto_release/                 # Python pipeline entrypoints
        ├── watcher.py                         # Detects upstream changes, emits changed/no-change
        ├── fetch.py                           # Conditional GET (ETag/Last-Modified)
        ├── validate.py                        # Schema + FAIR+CARE validation
        ├── transform.py                       # Deterministic transform (e.g., CSV → Parquet)
        ├── diff_classify.py                   # Row/column diff + change classification
        ├── versioner.py                       # SemVer bump decision (patch/minor/major)
        ├── publish.py                         # PR/Release creation + asset staging
        ├── notify.py                          # Slack (or other) notifications
        └── telemetry.py                       # Telemetry emission for runs

data/
└── work/
    └── reliable_auto_release/                 # Ephemeral working directory for pipeline
        ├── cache/                             # ETag / Last-Modified cache, content hashes
        ├── checkpoints/                       # Phase markers for resuming jobs
        ├── input.dat                          # Latest fetched raw input
        ├── output.parquet                     # Latest transform output
        └── logs/                              # Fetch/validate/transform logs

releases/
└── reliable_auto_release/                     # Series-specific releases (if using dedicated folder)
    ├── manifest.zip                           # Release manifest bundle
    ├── sbom.spdx.json                         # SBOM for pipeline runtime/tooling
    └── CHANGELOG.md                           # Aggregate changelog for this series

docs/
└── guides/
    └── pipelines/
        └── reliable-auto-release.md           # This guide

schemas/
└── reliable-auto-release/                     # Schema contracts for pipeline validation
    ├── dataset.schema.json                    # Data schema
    └── diff.schema.json                       # Diff / SemVer decision schema

telemetry/
└── reliable-auto-release-v1.json              # Telemetry event schema for this pipeline
~~~

---

## 🧭 Flow (High-Level)

### Description

The watcher triggers on upstream change or on schedule.  
The fetcher issues a **conditional request**; **304 Not Modified** yields a NOOP.  
If new content arrives, the validator checks schemas and rules; transform runs deterministically;  
diffs are classified into **SemVer bump**; the system builds `CHANGELOG` and `manifest`, then opens a PR  
or publishes a **tagged Release**. Slack receives a summary with `run_id` and artifact links.

### Diagram

```mermaid
flowchart TD

  %% -------------------------------
  %% Subgraphs (Logical Phases)
  %% -------------------------------

  subgraph TRIGGER["Trigger & Watch"]
    W["Watcher<br/>webhook or cron"]
  end

  subgraph FETCH["Fetch & Idempotency"]
    F["Fetch<br/>ETag / Last-Modified"]
    N["NOOP<br/>short-circuit"]
    W --> F
    F -->|304 NOT_MODIFIED| N
  end

  subgraph VALIDATE["Validation"]
    V["Validate<br/>schemas & rules"]
    F -->|200 OK| V
  end

  subgraph TRANSFORM["Deterministic Transform"]
    T["Transform<br/>deterministic"]
    V --> T
  end

  subgraph DIFF_SEMVER["Diff & SemVer"]
    D["Diff classifier<br/>row / column deltas"]
    S["SemVer bump<br/>major / minor / patch"]
    T --> D
    D --> S
  end

  subgraph ARTIFACTS["Artifacts"]
    C["Changelog + manifest<br/>generate artifacts"]
    S --> C
  end

  subgraph PUBLISHING["Publish"]
    P["Publish<br/>PR or Release"]
    C --> P
  end

  subgraph LEDGER_AND_TELEMETRY["Ledger & Telemetry"]
    L["Ledger + telemetry<br/>run_id · hashes · status"]
    N --> L
    P --> L
  end

  subgraph NOTIFY["Notify"]
    H["Notify<br/>Slack webhook"]
    P --> H
  end

  %% -------------------------------
  %% Class Definitions (KFM Styling)
  %% -------------------------------

  classDef triggerPhase fill:#edf2ff,stroke:#4c6fff,stroke-width:1px,color:#1a2b6c;
  classDef fetchPhase fill:#f0fff4,stroke:#2f855a,stroke-width:1px,color:#22543d;
  classDef validatePhase fill:#fffaf0,stroke:#dd6b20,stroke-width:1px,color:#7b341e;
  classDef transformPhase fill:#f7fafc,stroke:#4a5568,stroke-width:1px,color:#2d3748;
  classDef diffPhase fill:#ebf8ff,stroke:#3182ce,stroke-width:1px,color:#2b6cb0;
  classDef artifactsPhase fill:#faf5ff,stroke:#805ad5,stroke-width:1px,color:#44337a;
  classDef publishPhase fill:#f0fff4,stroke:#38a169,stroke-width:1px,color:#22543d;
  classDef ledgerPhase fill:#fffff0,stroke:#b7791f,stroke-width:1px,color:#744210;
  classDef notifyPhase fill:#fff5f5,stroke:#e53e3e,stroke-width:1px,color:#742a2a;
  classDef noopPhase fill:#e2e8f0,stroke:#4a5568,stroke-width:1px,color:#1a202c;

  class TRIGGER triggerPhase;
  class FETCH fetchPhase;
  class VALIDATE validatePhase;
  class TRANSFORM transformPhase;
  class DIFF_SEMVER diffPhase;
  class ARTIFACTS artifactsPhase;
  class PUBLISHING publishPhase;
  class LEDGER_AND_TELEMETRY ledgerPhase;
  class NOTIFY notifyPhase;
  class N noopPhase;

````

---

## ⚙️ GitHub Actions — Workflow Skeleton

```yaml
name: reliable-auto-release

on:
  schedule:
    - cron: "*/15 * * * *"
  workflow_dispatch: {}
  repository_dispatch:
    types: [upstream_changed]   # For webhooks → Actions fan-in

concurrency:
  group: reliable-auto-release-${{ github.ref }}
  cancel-in-progress: false

permissions:
  contents: write
  pull-requests: write

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install deps
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt

      - name: Watch & Fetch (conditional)
        id: fetch
        run: |
          python -m src.pipelines.reliable_auto_release.watcher --emit-dispatch=false
          python -m src.pipelines.reliable_auto_release.fetch \
            --url "$SOURCE_URL" \
            --etag-cache data/work/reliable_auto_release/cache/etag.json \
            --out data/work/reliable_auto_release/input.dat \
            --log data/work/reliable_auto_release/fetch.log

      - name: Validate
        if: steps.fetch.outputs.changed == 'true'
        run: |
          python -m src.pipelines.reliable_auto_release.validate \
            --in data/work/reliable_auto_release/input.dat \
            --schemas schemas/ \
            --log data/work/reliable_auto_release/validate.log

      - name: Transform (deterministic)
        if: steps.fetch.outputs.changed == 'true'
        run: |
          python -m src.pipelines.reliable_auto_release.transform \
            --in data/work/reliable_auto_release/input.dat \
            --out data/work/reliable_auto_release/output.parquet \
            --log data/work/reliable_auto_release/transform.log

      - name: Diff & Version
        if: steps.fetch.outputs.changed == 'true'
        id: version
        run: |
          python -m src.pipelines.reliable_auto_release.diff_classify \
            --new data/work/reliable_auto_release/output.parquet \
            --old releases/latest/output.parquet || true
          python -m src.pipelines.reliable_auto_release.versioner \
            --strategy deterministic \
            --out .version

      - name: Artifacts (CHANGELOG, manifest, SBOM)
        if: steps.fetch.outputs.changed == 'true'
        run: |
          python -m src.pipelines.reliable_auto_release.publish \
            --version-file .version \
            --changelog releases/${{ steps.version.outputs.version }}/CHANGELOG.md \
            --manifest releases/${{ steps.version.outputs.version }}/manifest.zip \
            --sbom releases/${{ steps.version.outputs.version }}/sbom.spdx.json \
            --stage-only

      - name: Publish PR or Release
        if: steps.fetch.outputs.changed == 'true'
        run: |
          python -m src.pipelines.reliable_auto_release.publish --do-publish

      - name: Telemetry & Notify
        if: steps.fetch.outputs.changed == 'true'
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
        run: |
          python -m src.pipelines.reliable_auto_release.telemetry --emit
          python -m src.pipelines.reliable_auto_release.notify \
            --slack-webhook "$SLACK_WEBHOOK_URL"
```

---

## 🧪 Determinism & Versioning

**Deterministic transforms**

* Pure functions (no global state, no time-dependent logic)
* Pinned dependencies
* Stable sorting (rows and columns)
* Fixed locale/timezone and encoding

**SemVer from diffs**

* `patch` — corrections, non-breaking fixes
* `minor` — additive columns or data, no contract change
* `major` — schema/contract changes, removed fields, breaking semantics

**Example CHANGELOG entry**

```text
## vX.Y.Z — 2025-11-16
- Type: minor
- Source: https://example.org/daily-stations.csv
- Diff: +1,243 records; schema unchanged
- Checks: schemas ✓  stac ✓  fair+care ✓  security ✓
- Artifacts: manifest.zip, sbom.spdx.json, telemetry.json
```

---

## 🛡️ Validation Gates (must pass)

* **Schema** — JSON Schema, STAC, or domain-specific contracts
* **FAIR+CARE** — metadata completeness, CARE alignment, consent signals
* **Security** — dependency and container scans (CodeQL, Trivy, etc.)
* **Accessibility** — where UI assets change, ensure docs + visual assets follow WCAG
* **Energy/Carbon** — optional: energy/CO₂ telemetry for each run (ISO 50001/14064 compatible)

---

## 📡 Telemetry & Run Ledger

Minimum fields in `reliable-auto-release-v1.json`:

* `run_id`, `pipeline`, `source_url`, `trigger` (`webhook|cron|manual`)
* `input_hash`, `artifact_hash`, `semver`, `diff_class`
* `status` (`noop|success|failed`)
* `duration_ms`, `attempt`, `retries`
* `energy_kwh_est`, `co2e_kg_est` (if enabled)
* `links` (PR, Release, CHANGELOG, SBOM, manifest)

These are appended to a **run ledger** and shipped as telemetry.

---

## 🔔 Slack Notification Template (JSON)

```json
{
  "text": "KFM Auto-Release",
  "blocks": [
    {
      "type": "header",
      "text": { "type": "plain_text", "text": "✅ KFM Auto-Release vX.Y.Z" }
    },
    {
      "type": "section",
      "fields": [
        { "type": "mrkdwn", "text": "*Pipeline:* reliable-auto-release" },
        { "type": "mrkdwn", "text": "*Run ID:* `{{run_id}}`" },
        { "type": "mrkdwn", "text": "*Diff:* {{diff_class}} ({{summary}})" },
        { "type": "mrkdwn", "text": "*Status:* {{status}}" }
      ]
    },
    {
      "type": "actions",
      "elements": [
        { "type": "button", "text": { "type": "plain_text", "text": "PR/Release" }, "url": "{{publish_url}}" },
        { "type": "button", "text": { "type": "plain_text", "text": "CHANGELOG" }, "url": "{{changelog_url}}" }
      ]
    }
  ]
}
```

---

## 🧰 Implementation Notes

* Prefer **ETag** and `If-None-Match` for content identity; use `Last-Modified` as advisory.
* Always compute a deterministic **SHA-256 content hash** over normalized bytes.
* Use stable row ordering + column ordering to avoid unnecessary SemVer bumps.
* Make additive columns nullable and document them in dataset metadata (STAC, DCAT, schemas).

---

## ✅ Checklist (For Pipeline Setup)

* [ ] Webhook or cron watcher configured
* [ ] Conditional fetch (ETag/Last-Modified) implemented
* [ ] Schema + FAIR+CARE validators wired into CI
* [ ] Deterministic transform implemented (pinned dependencies)
* [ ] Diff + SemVer classification logic in place
* [ ] CHANGELOG + manifest + SBOM generation wired
* [ ] Concurrency locks configured
* [ ] Retries + backoff + timeouts configured
* [ ] Dry-run path tested in CI
* [ ] Slack notifications validated
* [ ] Telemetry schema + dashboards configured

---

## 📜 Version History

| Version | Date       | Summary                                                                                  |
| ------: | ---------- | ---------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Added KFM-style canonical directory tree; aligned layout with KFM-MDP v10.4.x tree rules |
| v10.4.1 | 2025-11-16 | Initial KFM guide for reliable auto-release pipelines                                    |

---
