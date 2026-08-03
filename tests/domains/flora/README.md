<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-flora-readme
title: Tests — Flora Domain
class: test-readme
version: v0.2.0
status: repository-grounded draft; one bounded executable slice established
truth_posture: CONFIRMED focused synthetic fixture suite / PROPOSED broader Flora coverage / UNKNOWN operational completeness
owner: NEEDS VERIFICATION — Flora steward, test steward, sensitivity/geoprivacy reviewer
created: 2026-07-05
updated: 2026-08-03
policy_label: public; no-network; fixture-only; fail-closed
related:
  - ../../../fixtures/domains/flora/README.md
  - ../../../tools/validators/domains/flora/README.md
  - ../../../.github/workflows/domain-flora.yml
  - ../../../docs/domains/flora/README.md
notes:
  - "The focused smoke module validates synthetic public-safe fixture conformance only."
  - "Proof and release readiness remain separate explicit holds."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tests/domains/flora/` — Flora Tests

[![Status: bounded executable](https://img.shields.io/badge/status-bounded%20executable-1a7f37?style=flat-square)](#implemented-slice)
[![Network: blocked](https://img.shields.io/badge/network-blocked-b42318?style=flat-square)](#no-network-contract)
[![Data: synthetic only](https://img.shields.io/badge/data-synthetic%20only-0969da?style=flat-square)](#fixture-contract)
[![Authority: conformance only](https://img.shields.io/badge/authority-conformance%20only-6e7781?style=flat-square)](#limits)

> **Purpose.** Provide deterministic executable checks for Flora behavior without accessing live sources or treating tests as botanical, policy, proof, release, or publication authority.

## Implemented slice

`test_flora_smoke.py` exercises the bounded validator at:

```text
tools/validators/domains/flora/validate_public_safe_fixture.py
```

The suite proves:

- one explicit positive fixture inventory;
- six explicit negative fixtures and exact error sidecars;
- closed object shapes and stable sorted findings;
- strict source-role, taxon-state, rights, sensitivity, review, release, and promotion posture;
- case-insensitive rejection of exact-location aliases and transform-secret fields;
- rejection of URLs, coordinate-like strings, WKT-like strings, and numeric values;
- bounded UTF-8 JSON parsing with duplicate-key, size, depth, node, integer, and non-finite-number rejection;
- regular-file-only input handling;
- machine-readable CLI output and exit codes `0`, `1`, and `2`;
- no candidate-value echoing;
- no socket, DNS, HTTP, or other live-network use by the validator path.

## Fixture contract

The focused suite consumes only:

```text
fixtures/domains/flora/valid/public_safe_occurrence.json
fixtures/domains/flora/invalid/*.json
fixtures/domains/flora/invalid/*.expected_error.txt
```

All examples are synthetic. They contain no real taxa, occurrence coordinates, private-land records, access directions, collection clues, credentials, restricted source payloads, URLs, or geoprivacy transform parameters.

## No-network contract

The unit suite patches common socket and `urllib.request.urlopen` entry points. The validator itself uses only standard-library file, JSON, path, and CLI functionality. CI also sets `KFM_NO_NETWORK=1` and `PYTHONDONTWRITEBYTECODE=1`.

Run from repository root:

```bash
python -m unittest discover \
  --start-directory tests/domains/flora \
  --pattern 'test_flora_smoke.py' \
  --verbose
```

## Limits

Passing this slice does **not** prove:

- botanical identity or occurrence truth;
- accepted Flora contracts or schemas;
- source admission, rights clearance, or source freshness;
- policy, sensitivity, stewardship, or sovereignty approval;
- execution of a public-safe geoprivacy transform;
- EvidenceBundle or proof construction;
- release readiness, deployment, publication, or public serving.

The `domain-flora` proof and release jobs remain explicit holds.

## Broader coverage

Existing Flora test modules and sublane READMEs remain useful planning and compatibility surfaces. Their presence must not be interpreted as complete domain enforcement. Future slices should be admitted independently with exact fixtures, finite outcomes, no-network tests, documentation, provenance, and rollback.

[Back to top](#top)
