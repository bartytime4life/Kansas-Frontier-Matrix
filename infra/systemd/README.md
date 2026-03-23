<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-VERIFY-UUID
title: infra/systemd
type: standard
version: v1
status: draft
owners: TODO-VERIFY-OWNERS
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: TODO-VERIFY-POLICY-LABEL
related: [TODO-VERIFY-RELATED-PATHS]
tags: [kfm, infra, systemd, linux, ubuntu, operations]
notes: [Target path was user-provided; mounted repo tree was not directly visible in this session, so path fit, owners, dates, and related links require verification.]
[/KFM_META_BLOCK_V2] -->

# infra/systemd
Ubuntu/systemd host wiring, unit families, and hardening notes for the KFM phase-one runtime.

> **Status:** experimental  
> **Owners:** `TODO-VERIFY-OWNERS`  
> ![Status: experimental](https://img.shields.io/badge/status-experimental-orange) ![Evidence: pdf-only](https://img.shields.io/badge/evidence-pdf--only-blue) ![Linux: Ubuntu LTS](https://img.shields.io/badge/linux-Ubuntu%20LTS-6f42c1) ![Init: systemd](https://img.shields.io/badge/init-systemd-1f6feb)  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> This README is intentionally source-bounded. The March 2026 KFM corpus confirms that `infra/` is reserved for environment wiring and delivery mechanics, and that the phase-one Linux runtime is systemd-first on Ubuntu. The mounted workspace available in this session did **not** expose a live repo checkout or live unit files, so filenames, owners, sibling links, and install wiring below remain **PROPOSED** or **NEEDS VERIFICATION** until the actual tree is inspected.

## Scope

This directory is the host-wiring layer for KFM services that are meant to run as native systemd-managed processes on Ubuntu. It is where unit files, override snippets, environment-file examples, and operational notes should live **when systemd is the selected runtime envelope**.

The strongest project doctrine behind this directory is simple:

- keep public clients behind the governed API,
- keep PostgreSQL/PostGIS, Ollama, and canonical artifact roots off the public network,
- prefer loopback and Unix-socket boundaries in phase one,
- treat service identity, write scope, restart behavior, and logging as part of the trust system.

| Evidence posture | Meaning inside this README |
| --- | --- |
| **CONFIRMED** | KFM favors **systemd-first** packaging for the thinnest credible phase-one Ubuntu runtime, and `infra/` is reserved for environment wiring rather than business logic. |
| **INFERRED** | `infra/systemd/` is a systemd-specific specialization of the broader `infra/systemd-or-compose/` slot named in the March 2026 repo skeleton. |
| **PROPOSED** | The exact file layout, unit filenames in the repo, install helpers, and sibling README links shown here. |
| **UNKNOWN** | Whether the mounted repo already contains this directory, these unit files, or matching workflow/tests. |

## Repo fit

**Path:** `infra/systemd/`

This README assumes the repo has split Linux/systemd host wiring into a dedicated directory rather than leaving it under the broader `infra/systemd-or-compose/` slot described in the replacement-grade repo skeleton.

| Fit | Notes |
| --- | --- |
| **Role in repo** | Environment wiring and delivery mechanics for a native Ubuntu/systemd deployment path. |
| **Upstream inputs** | `apps/` binaries or entrypoints, `configs/`, `policy/`, published-scope storage rules, and service account expectations. **NEEDS VERIFICATION** against the mounted repo. |
| **Sibling infra** | [`../local/`](../local/) and [`../hosted/`](../hosted/) are the most likely adjacent surfaces if the March 2026 skeleton was followed. **INFERRED** only. |
| **Downstream targets** | `/etc/systemd/system/`, `/etc/kfm/*.env`, journald, runtime/state/cache/log directories, and host firewall / VPN / loopback binding decisions. |

## Inputs

What belongs here:

| Input class | Examples | Why it belongs |
| --- | --- | --- |
| Unit files | `kfm-api.service`, `kfm-ingest@.service`, `kfm-build@.service`, `kfm-publish@.service`, `kfm-project@.service` | These are the systemd family names explicitly proposed in the current KFM Ubuntu guidance. |
| Override snippets | `ollama.service.d/override.conf` | KFM’s Linux guidance explicitly calls for a local-only Ollama override surface. |
| Environment examples | `env/kfm-api.env.example`, `env/kfm-worker.env.example`, `env/kfm-publish.env.example`, `env/ollama.override.env.example` | The docs name the host-side `/etc/kfm/*.env` pattern; repo copies should stay sanitized and example-only. |
| Operational notes | install, reload, verify, journal, rollback, and host-hardening instructions | This directory is where host wiring becomes inspectable and reviewable. |

## Exclusions

What does **not** belong here:

| Keep out of `infra/systemd/` | Put it here instead | Why |
| --- | --- | --- |
| Policy rules and decision logic | `policy/` | Policy is shared law, not host glue. |
| Schemas, OpenAPI, vocabularies, fixtures | `contracts/` | Contract surfaces need independent versioning and review. |
| App code, domain logic, workers’ business rules | `apps/` or `packages/` | Infra should not become the place where unexplained business behavior hides. |
| Canonical datasets, receipts, published artifacts | `data/` lifecycle zones | Host units may mount or reference these zones, but they do not define them. |
| Real secrets and live credentials | host-only `/etc/kfm/*.env` or approved secret mechanism | The repo may hold examples, never live values. |
| Ad hoc convenience scripts that own real domain behavior | promote into a package or worker | The March 2026 KFM manuals explicitly warn against scripts turning into silent authority. |

## Directory tree

**PROPOSED starter shape** aligned to the current KFM systemd guidance:

```text
infra/systemd/
├── README.md
├── kfm-api.service
├── kfm-ingest@.service
├── kfm-build@.service
├── kfm-publish@.service
├── kfm-project@.service
├── env/
│   ├── kfm-api.env.example
│   ├── kfm-worker.env.example
│   ├── kfm-publish.env.example
│   └── ollama.override.env.example
└── ollama.service.d/
    └── override.conf
```

A lean tree is a feature here. This directory should stay legible enough that a reviewer can answer three questions quickly:

1. Which services exist?
2. What is allowed to start, write, and restart?
3. Which host-only files must exist outside Git for the units to become real?

## Quickstart

### 1) Verify that this README matches the real repo

```bash
# REVIEW ONLY
find infra/systemd -maxdepth 2 -type f | sort
```

If the repo still uses `infra/systemd-or-compose/`, decide whether this README should move there or whether the tree is intentionally splitting the Linux/systemd branch from a compose-based local path.

### 2) Validate unit syntax before install

```bash
# REVIEW ONLY
systemd-analyze verify infra/systemd/*.service
```

### 3) Install example units on a host

```bash
# EXAMPLE ONLY — adjust paths, users, and ExecStart values before use
sudo install -m 0644 infra/systemd/*.service /etc/systemd/system/
sudo install -d -m 0750 /etc/kfm
sudo install -m 0640 infra/systemd/env/*.env.example /etc/kfm/
sudo mkdir -p /etc/systemd/system/ollama.service.d
sudo install -m 0644 infra/systemd/ollama.service.d/override.conf \
  /etc/systemd/system/ollama.service.d/override.conf
sudo systemctl daemon-reload
sudo systemctl enable --now kfm-api.service
```

### 4) Inspect live status and logs

```bash
# REVIEW / OPERATIONS
systemctl status kfm-api.service
journalctl -u kfm-api.service -f
```

## Usage

### Unit strategy

Use long-running units for stable runtime surfaces and templated one-shot units for bounded jobs.

- **Long-running:** governed API, optional reverse proxy, and any continuously running support daemon.
- **One-shot or controlled batch:** ingest, build, publish, and projection-style work where a run should either complete cleanly or fail closed with diagnosable evidence.

### Network posture

Phase-one KFM is explicitly **not** a “just open the port” design.

- Bind the governed API to loopback unless an approved edge or VPN layer exists.
- Keep PostgreSQL/PostGIS local-only.
- Keep Ollama local-only.
- Keep direct access to RAW / WORK / QUARANTINE and artifact roots off the public network.

### Environment and secret boundary

The repo may store examples, but the live service environment should resolve from host-owned files such as:

- `/etc/kfm/kfm-api.env`
- `/etc/kfm/kfm-worker.env`
- `/etc/kfm/kfm-publish.env`
- `/etc/kfm/ollama.override.env`

Treat these as root-owned, tightly permissioned, and outside casual operator read by default.

### Hardening profile

The current doctrine strongly favors managed writable directories and explicit write scope over broad filesystem access.

Recommended defaults for many units:

- `NoNewPrivileges=yes`
- `PrivateTmp=yes`
- `ProtectSystem=strict`
- `ProtectHome=read-only`
- `ReadWritePaths=` limited to required locations only
- `RuntimeDirectory=`, `StateDirectory=`, and `LogsDirectory=` where appropriate
- `RestrictSUIDSGID=yes`
- `ProtectKernelLogs=yes` where compatible

> [!CAUTION]
> `PrivateNetwork=` is **not** a safe blanket default for KFM services that still need host loopback communication.

### Restart and rollback mindset

- Long-running services should generally prefer `Restart=on-failure`.
- One-shot jobs should not enter blind restart loops.
- Runtime rollback and public correction are distinct actions in KFM: a failed deploy may need a service rollback, while a public semantic change may need a correction artifact or withdrawal.

## Diagram

```mermaid
flowchart TB
  subgraph Repo[Repository]
    R1[infra/systemd/]
    R2[Unit files]
    R3[Env examples]
    R4[Override snippets]
  end

  subgraph Host[Ubuntu host]
    H1[/etc/systemd/system/]
    H2[/etc/kfm/*.env]
    H3[journald]
  end

  R1 --> R2 --> H1
  R1 --> R3 --> H2
  R1 --> R4 --> H1

  H1 --> A[kfm-api.service]
  H1 --> B[kfm-ingest@.service]
  H1 --> C[kfm-build@.service]
  H1 --> D[kfm-publish@.service]
  H1 --> E[kfm-project@.service]

  A --> F[Governed API\n127.0.0.1 only]
  F --> G[(PostgreSQL/PostGIS)]
  F --> H[/srv/kfm/published]
  B --> I[/srv/kfm/raw → work/quarantine]
  C --> J[/processed → catalog]
  D --> K[/catalog → published]
  E --> L[Derived rebuilds only]
  M[Local Ollama\n127.0.0.1:11434] --> F
  A --> H3
  B --> H3
  C --> H3
  D --> H3
  E --> H3
```

## Tables

### Unit family matrix

| Unit family | Service shape | Purpose | Expected write scope | Posture |
| --- | --- | --- | --- | --- |
| `kfm-api.service` | long-running | governed API | runtime state, logs, limited published/catalog reads | **PROPOSED** filename; doctrine **CONFIRMED** |
| `kfm-ingest@.service` | templated one-shot | source-edge intake | stage-specific `raw/` and `work/` writes only | **PROPOSED** |
| `kfm-build@.service` | templated one-shot | build / projection work | `processed/` and `catalog/`-adjacent writes as required | **PROPOSED** |
| `kfm-publish@.service` | controlled batch | catalog closure and publication movement | `catalog/` and `published/` only | **PROPOSED** |
| `kfm-project@.service` | templated one-shot | derived-layer rebuilds | derived stores only | **PROPOSED** |

### Service dependency law

| Order | Why it matters |
| --- | --- |
| Database before governed API | The API should not advertise readiness against a missing canonical store. |
| Artifact mounts before workers | Intake/build jobs need known paths before they start. |
| Policy/config readable before API readiness | KFM does not treat policy as optional decoration. |
| Local model runtime before AI-enabled answer path | AI support is subordinate, but if enabled it should be reachable through the governed adapter. |
| Projection rebuilds only after a published release exists | Derived layers must trail release-bearing truth, not race ahead of it. |

### Environment and managed directories

| Surface | Example | Notes |
| --- | --- | --- |
| Environment file | `/etc/kfm/kfm-api.env` | host-owned, not committed with live values |
| Runtime directory | `RuntimeDirectory=kfm-api` | for sockets, pid-ish scratch, and transient runtime files |
| State directory | `StateDirectory=kfm-api` | for durable service-owned state when needed |
| Logs directory | `LogsDirectory=kfm-api` | pair with journald-driven service inspection |
| Explicit writes | `ReadWritePaths=/run/kfm /var/lib/kfm-api /srv/kfm/published /srv/kfm/catalog` | narrow write scope is preferred over broad ownership |

## Task list

| Gate | Done when | Evidence to capture |
| --- | --- | --- |
| Path fit | The actual repo confirms whether `infra/systemd/` is the right path, or the README is moved to the verified location. | repo tree snapshot or PR diff |
| Ownership | `TODO-VERIFY-OWNERS` is replaced with the real team or names. | README update |
| Unit realism | Every `ExecStart`, `WorkingDirectory`, user, and group maps to a real service binary and real host path. | `systemd-analyze verify`, reviewed unit files |
| Secret boundary | Live values are outside Git and repo copies are example-only. | host file permissions + sanitized examples |
| Loopback discipline | API, DB, and Ollama exposure match the approved host boundary. | bind config + firewall / VPN review |
| Least privilege | Service users and `ReadWritePaths=` reflect stage-specific rights. | unit review + filesystem permissions |
| Logging | Operators can inspect service health and failures via journald without guesswork. | `systemctl status` and `journalctl` checks |
| Rollback readiness | Disable/stop/reload steps exist and do not depend on tribal knowledge. | runbook note or PR checklist |

### Definition of done

- [ ] Repo path and sibling links verified against the mounted tree.
- [ ] Owners, dates, and related links replaced with real values.
- [ ] Unit names, paths, and environment examples aligned to real binaries and directories.
- [ ] Host-only env files and service users documented with verified permissions.
- [ ] At least one long-running unit and one one-shot template verified end to end.
- [ ] Journald inspection and rollback steps exercised once on a non-production host.

## FAQ

### Why systemd here instead of a container-first README?

Because the current KFM Linux guidance treats **systemd-first packaging** as the thinnest credible phase-one start on Ubuntu. That keeps loopback and Unix-socket boundaries simple while the governed path is still being proven.

### Why keep real secrets out of this directory?

Because this repo surface is for reviewable host wiring. Live credentials belong on the host, not in Git. This directory should carry sanitized examples and clear installation rules, not operational leakage.

### Why are PostgreSQL/PostGIS and Ollama treated so cautiously?

Because KFM’s trust membrane depends on keeping canonical stores and model runtimes behind the governed API. Direct client access collapses the boundary the rest of the architecture is trying to preserve.

### What if the repo still uses `systemd-or-compose/`?

Then either move this README there, or keep this file only if the repo is intentionally specializing the Linux/systemd branch. The content here is written to survive either choice, but the final path should be decided by the actual mounted tree.

## Appendix

<details>
<summary><strong>Illustrative skeleton unit — <code>kfm-api.service</code></strong></summary>

```ini
[Unit]
Description=KFM Governed API
After=network-online.target postgresql.service
Wants=network-online.target
Requires=postgresql.service

[Service]
User=kfm-api
Group=kfm-api
WorkingDirectory=/opt/kfm/api
EnvironmentFile=/etc/kfm/kfm-api.env
ExecStart=/path/to/actual-kfm-api-binary --bind 127.0.0.1:8080
Restart=on-failure
RestartSec=5

RuntimeDirectory=kfm-api
StateDirectory=kfm-api
LogsDirectory=kfm-api

NoNewPrivileges=yes
PrivateTmp=yes
ProtectSystem=strict
ProtectHome=read-only
ReadWritePaths=/run/kfm /var/lib/kfm-api /srv/kfm/published /srv/kfm/catalog
RestrictSUIDSGID=yes
ProtectKernelLogs=yes
UMask=0027

[Install]
WantedBy=multi-user.target
```

</details>

<details>
<summary><strong>Illustrative Ollama override — local-only bind</strong></summary>

```ini
[Service]
Environment="OLLAMA_HOST=127.0.0.1:11434"
Environment="OLLAMA_MODELS=/var/lib/ollama/models"
```

</details>

[Back to top](#infrasystemd)
