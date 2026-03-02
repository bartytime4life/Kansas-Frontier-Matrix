<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/c40181cc-432b-41d1-a5fd-3f54104c9ccf
title: Mermaid C4 Context Diagram Template
type: standard
version: v1
status: draft
owners: TODO
created: 2026-03-02
updated: 2026-03-02
policy_label: public
related:
  - docs/diagrams/README.md
  - docs/diagrams/templates/mermaid/
tags: [kfm, diagram, mermaid, c4]
notes:
  - Template for C4 context diagrams using Mermaid's C4 syntax.
  - Replace all placeholders wrapped in {{double_curly_braces}}.
[/KFM_META_BLOCK_V2] -->

# Mermaid C4 Context Diagram Template

**Purpose:** A copy/paste template for creating **C4 System Context** diagrams in Mermaid.  
**Use when:** You want to show **people + the system-of-interest + external systems** and the **major relationships** between them.

![diagram](https://img.shields.io/badge/diagram-C4_Context-blue)
![format](https://img.shields.io/badge/format-Mermaid-ff69b4)
![status](https://img.shields.io/badge/status-template-lightgrey)

---

## Quick links

- [Usage](#usage)
- [Template](#template)
- [KFM conventions](#kfm-conventions)
- [Checklist](#checklist)
- [Appendix: snippet library](#appendix-snippet-library)

---

## Usage

1. Copy this file to a new diagram doc (recommended):
   - `docs/diagrams/{{area}}/{{diagram_slug}}.md`
2. Replace placeholders like `{{SYSTEM_NAME}}`.
3. Render Mermaid in your Markdown viewer (GitHub, MkDocs, VS Code extension, etc.).

> TIP: Keep context diagrams **small**: ~5–15 elements is usually enough.

---

## Template

Paste the diagram block below into your doc and replace placeholders.

```mermaid
C4Context
title {{TITLE}}

%% People (actors)
Person(user, "{{PRIMARY_PERSON_NAME}}", "{{PRIMARY_PERSON_DESCRIPTION}}")

%% System under discussion
System(system, "{{SYSTEM_NAME}}", "{{SYSTEM_DESCRIPTION}}")

%% External systems (things outside the system boundary)
System_Ext(ext_upstream, "{{EXT_UPSTREAM_SYSTEM}}", "{{WHAT_IT_PROVIDES}}")
System_Ext(ext_idp, "{{EXT_IDENTITY_PROVIDER}}", "{{AUTHN_AUTHZ_DESCRIPTION}}")
System_Ext(ext_observability, "{{EXT_OBSERVABILITY}}", "{{LOGS_METRICS_TRACES}}")

%% Relationships (keep labels short; add protocol/format only if it matters)
Rel(user, system, "{{USER_DOES}}")
Rel(system, ext_upstream, "{{CONSUMES_OR_PUBLISHES}}", "{{PROTOCOL_OR_FORMAT}}")
Rel(system, ext_idp, "{{VALIDATES_TOKENS_OR_GETS_IDENTITY}}", "{{OIDC_OAUTH_SAML}}")
Rel(system, ext_observability, "{{EMITS_TELEMETRY}}", "{{OTLP_PROMETHEUS_ETC}}")

%% Optional layout tuning
UpdateLayoutConfig($c4ShapeInRow="3", $c4BoundaryInRow="1")
```

---

## KFM conventions

These are **project conventions** for KFM diagrams. If your diagram is not for KFM, you can ignore this section.

### Naming and IDs

- Mermaid element IDs should be `snake_case` (e.g., `kfm_api`, `usgs_nwis`).
- Display names should be **human-readable** and stable.
- Prefer one system-of-interest per context diagram.

### Relationships

- Use relationship labels that are **verbs**: “Queries”, “Publishes”, “Validates”, “Streams”.
- If the relationship crosses a governance boundary, call it out (e.g., “Policy-enforced query”).

### Trust membrane hint

If your diagram touches access control or governance, prefer showing **clients calling a governed API**
instead of direct storage access (that is, keep “storage” behind the policy boundary).  

> NOTE: In KFM, this is part of the “trust membrane” posture: UI/clients do not access storage directly;
> access should go through governed APIs and policy enforcement. (See KFM governance/design guide.)  

---

## Checklist

Use this quick checklist before merging a diagram doc:

- [ ] Title describes **what** and **which boundary** (“System Context for …”).
- [ ] Every external dependency is clearly labeled as **external** (`System_Ext`).
- [ ] Each relationship is directional and uses a short verb phrase.
- [ ] No sensitive details are exposed (e.g., internal hostnames, credentials, or precise coordinates for vulnerable sites).
- [ ] If governance is relevant, the policy boundary is not bypassed in the picture.

---

## Appendix: snippet library

### Minimal (smallest useful context diagram)

```mermaid
C4Context
title {{TITLE}}

Person(user, "{{PERSON}}", "{{ROLE}}")
System(system, "{{SYSTEM}}", "{{WHAT_IT_DOES}}")
System_Ext(ext, "{{EXTERNAL_SYSTEM}}", "{{WHY_ITS_EXTERNAL}}")

Rel(user, system, "{{USES}}")
Rel(system, ext, "{{INTEGRATES_WITH}}", "{{PROTO}}")
```

### Optional: use an enterprise boundary

Use this when you want to show a *platform* boundary that contains multiple systems, while still staying
at “context” granularity.

```mermaid
C4Context
title {{TITLE}}

Person(user, "{{PERSON}}", "{{ROLE}}")

Enterprise_Boundary(org, "{{ORG_OR_PROGRAM_NAME}}") {
  System(system_a, "{{SYSTEM_A}}", "{{DESC_A}}")
  System(system_b, "{{SYSTEM_B}}", "{{DESC_B}}")
}

System_Ext(ext, "{{EXTERNAL_SYSTEM}}", "{{DESC}}")

Rel(user, system_a, "{{USES}}")
Rel(system_a, system_b, "{{CALLS}}", "{{PROTO}}")
Rel(system_b, ext, "{{CONSUMES}}", "{{PROTO}}")
```

---

### Notes on Mermaid compatibility

Mermaid C4 support depends on your renderer/version.
If your renderer does not support `C4Context`, you have two options:

1. Switch to a renderer that supports Mermaid C4 (recommended).
2. Fall back to a standard Mermaid flowchart and keep the same semantics (people, system, externals).
