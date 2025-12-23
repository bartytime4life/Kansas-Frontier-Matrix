# Markdown Protocol Fixtures — Invalid

This directory contains **intentionally invalid** Markdown examples used to exercise the **Markdown protocol validator**.

- Files in this folder are expected to **fail** validation.
- Prefer **one failure mode per fixture**.
- Keep fixtures **small, deterministic, and non-sensitive** (no secrets, no PII, no external network dependencies).

## What “invalid” means here

A fixture is “invalid” if it violates one or more Markdown protocol requirements (for example: missing required front-matter, malformed front-matter, invalid required fields, broken citation markers, etc.).

> This `README.md` is itself intentionally invalid **if** the validator requires YAML front-matter for Markdown documents.

## Current fixtures

| File | Intentional violation | Notes |
|---|---|---|
| `README.md` | Missing YAML front-matter | Minimal invalid example + human-readable folder docs |

## Adding a new invalid fixture

1. Name the file for the failure mode (examples):
   - `missing_title.md`
   - `bad_last_updated.md`
   - `invalid_version_format.md`
   - `broken_citation_marker.md`
2. Put a short comment near the top describing what should fail and why.
3. Keep the fixture focused (avoid bundling multiple unrelated failures into one file unless a combined-case test is intended).

## Suggested structure

~~~text
📁 .github/
└── 📁 actions/
    └── 📁 fixtures/
        └── 📁 markdown_protocol/
            └── 📁 invalid/
                ├── 📄 README.md
                └── 📄 <your_invalid_fixture>.md
~~~
