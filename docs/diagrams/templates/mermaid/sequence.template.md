<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: Mermaid Sequence Diagram Template
type: standard
version: v1
status: draft
owners: <team or names>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public
related:
  - docs/diagrams/README.md
  - docs/architecture/README.md
  - contracts/openapi/
  - policy/
  - data/
tags: [kfm, diagram, mermaid, sequence]
notes:
  - Copy this file, replace <uuid> and dates, then edit the diagram blocks.
[/KFM_META_BLOCK_V2] -->

# Mermaid sequence diagram template

Status: **draft template**  
Owners: **<team or names>**

Use this template to document **end-to-end interactions** across KFM layers (UI → governed APIs → policy boundary → data/cat/provenance → storage/indexing), and to make **gates, evidence, and audit** explicit.

## Navigation

- [Template rules](#template-rules)
- [Placeholders](#placeholders)
- [Template A: Governed runtime request](#template-a-governed-runtime-request)
- [Template B: Ingest and promotion flow](#template-b-ingest-and-promotion-flow)
- [Checklist](#checklist)

## Template rules

- **Sequence diagrams show responsibility boundaries.** Use them when you need to prove that clients do not bypass governed APIs, and that policy + evidence are enforced.
- **Make policy decisions observable.** Include the policy boundary actor and show allow/deny and obligations.
- **Make the truth path visible.** If the diagram involves data movement, show the zone transitions (RAW → WORK → PROCESSED → CATALOG → PUBLISHED).
- **Attach evidence, not vibes.** When the flow produces a user-facing claim, show where citations are resolved and returned.
- **Prefer short participant names.** Avoid punctuation-heavy labels.

## Placeholders

Replace these tokens when you copy the template:

- `PROJECT`: system or feature name
- `SCENARIO`: short scenario description
- `UI_NAME`: the UI surface, e.g. Map UI, Story UI, Focus Mode
- `API_NAME`: the governed API service
- `PEP_NAME`: policy enforcement point name
- `PDP_NAME`: policy decision point name
- `DATASET`: dataset or layer identifier
- `EVIDENCE_KIND`: citation type, e.g. doc, dataset, run_receipt

Tip: keep placeholders as plain words so Mermaid does not break.

---

## Template A: Governed runtime request

Use when you need to document the **trust membrane**: client requests go through the governed API, policy is evaluated, obligations are applied, and evidence is returned.

```mermaid
sequenceDiagram
  autonumber
  actor User as User
  participant UI as UI_NAME
  participant API as API_NAME
  participant PEP as PEP_NAME
  participant PDP as PDP_NAME
  participant Catalog as Catalog
  participant Evidence as EvidenceResolver
  participant Store as PublishedStore
  participant Audit as AuditLedger

  Note over User,UI: PROJECT - SCENARIO

  User->>UI: Submit request
  UI->>API: HTTP request

  API->>PEP: Build policy context
  PEP->>PDP: Evaluate policy

  alt Policy allow
    PDP-->>PEP: allow + obligations
    PEP-->>API: allow + obligations

    API->>Catalog: Resolve datasets and query plan
    Catalog->>Store: Query data for DATASET
    Store-->>Catalog: Results + EvidenceRefs

    Catalog->>Evidence: Resolve EvidenceBundle and apply redactions
    Evidence-->>Catalog: EvidenceBundle

    Catalog-->>API: Answer payload + citations
    API-->>UI: 200 OK + claims + citations
    UI-->>User: Render answer with citations

    API->>Audit: Append audit event

  else Policy deny
    PDP-->>PEP: deny + obligations
    PEP-->>API: deny + obligations
    API-->>UI: 403 Forbidden + policy reason
    UI-->>User: Show denial and next steps

    API->>Audit: Append audit event
  end
```

### Notes to customize

- If the request is **time-aware**, add a note showing which time concept is used (event time, valid time, transaction time).
- If the request triggers **rebuildable** operations (tiles, indexes), add optional steps after `Catalog`.
- If the answer is **redacted/generalized**, make the obligation explicit:

```mermaid
sequenceDiagram
  participant PEP as PEP_NAME
  participant Evidence as EvidenceResolver
  Note right of PEP: obligation: redact
  Note right of Evidence: action: generalize geometry
```

---

## Template B: Ingest and promotion flow

Use when you need to document **data movement** across zones and the **promotion contract**.

```mermaid
sequenceDiagram
  autonumber
  participant Upstream as UpstreamSource
  participant Ingest as IngestWorker
  participant Raw as RAWStore
  participant Work as WORKQuarantine
  participant Proc as ProcessedStore
  participant Cat as CatalogBuilder
  participant Pub as PublishedStore
  participant Policy as PolicyTests
  participant Audit as AuditLedger

  Note over Upstream,Pub: PROJECT - SCENARIO

  Upstream-->>Ingest: Provide source payload
  Ingest->>Raw: Write immutable artifact
  Ingest->>Audit: Emit run receipt

  Ingest->>Work: Normalize and validate

  alt Validation pass
    Work-->>Ingest: Validated artifact

    Ingest->>Proc: Produce publishable outputs
    Ingest->>Audit: Emit checksums and lineage

    Ingest->>Cat: Build STAC DCAT PROV
    Cat->>Policy: Run catalog and policy tests

    alt Gates pass
      Policy-->>Cat: pass
      Cat->>Pub: Promote to PUBLISHED
      Cat->>Audit: Append promotion record
    else Gates fail
      Policy-->>Cat: fail
      Cat->>Audit: Append failure record
      Note right of Cat: Do not promote
    end

  else Validation fail
    Work-->>Ingest: Errors and diagnostics
    Ingest->>Audit: Append failure receipt
    Note right of Ingest: Remain in WORK
  end
```

### Notes to customize

- Add explicit gates as needed:
  - license check
  - sensitivity classification
  - schema validation
  - link integrity
- If there is a human approval step, include it as an `actor` and place it **before** promotion.

---

## Checklist

Before you commit a new sequence diagram derived from this template:

- [ ] Every client access goes through a governed API (no direct storage access shown).
- [ ] Policy evaluation is shown with an allow/deny branch.
- [ ] Obligations are either applied (redaction/generalization) or explicitly marked as not applicable.
- [ ] Evidence resolution is shown when user-facing claims are returned.
- [ ] Data movement (if any) shows the zone transitions and where promotion can fail closed.
- [ ] Audit events are included for success and failure.
