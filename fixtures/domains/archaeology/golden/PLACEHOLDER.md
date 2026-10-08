<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/archaeology/golden/authoring-guide
title: Archaeology golden fixture authoring guide
type: fixture-guide
version: v1
status: repository-grounded documentation; no new fixture payloads
owners: ["@bartytime4life"]
created: 2026-10-08
updated: 2026-10-08
policy_label: synthetic-public-safe-only; no-network; no-authority
current_path: fixtures/domains/archaeology/golden/PLACEHOLDER.md
owning_root: fixtures/
responsibility: Explain the actual archaeology golden inventory, authoring boundaries and existing consumer routes.
truth_posture: CONFIRMED inventory and code/test pointers inspected at main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; no new runtime acceptance claimed.
related:
  - ../../../README.md
  - ../../../../tests/domains/archaeology/test_candidate_not_site.py
[/KFM_META_BLOCK_V2] -->

# Archaeology: golden fixture guide

Store reviewed, deterministic expected outputs for named synthetic inputs and an identified consumer. A golden is a regression expectation, not a factual reference dataset.

## Current inventory

This directory contains documentation only at the inspected source revision; it has no executable golden payloads. It does not provide golden fixture coverage merely because the lane or this file exists. Concrete sibling families below have their own consumers and must be evaluated separately.

The filename is retained for existing path references and workflow checks. This page replaces its former one-line marker with operational guidance; it does not create payloads or change test coverage.

## Domain rules to preserve

The current candidate-feature slice treats a synthetic candidate as a candidate rather than a discovered archaeological site. The candidate tests cover vocabulary, references, evidence binding, correction state and sensitive/location-bearing inputs. Separate no-network projection tests install a startup network guard; successful fixture replay grants no cultural review or excavation/publication authority.

Freeze the bounded candidate or public-safe projection result together with its exact synthetic input, expected decision and no-location output. Include an explicit denied/withheld case to show that a stable serialization cannot become a site-confirmation or publication receipt.

## Author or revise a case

1. Choose a concrete family and one deterministic input. Record its consumer, source revision and normalization rules.
2. Derive the expected result from the documented contract, then review it independently of the function that produced it. Preserve status, finding codes, evidence obligations and uncertainty.
3. Add an exact replay assertion and an explicit inventory entry where that family uses a manifest. Include a relevant negative/held case so a regression cannot silently gain authority.
4. When behavior intentionally changes, review the semantic diff before replacing expected bytes. Do not refresh snapshots solely to make a failing check green.

## Existing evidence and consumers

- [fixtures/domains/archaeology/synthetic_candidate_feature/valid.json](../synthetic_candidate_feature/valid.json)
- [fixtures/domains/archaeology/synthetic_candidate_feature/sensitive_geometry_deny.json](../synthetic_candidate_feature/sensitive_geometry_deny.json)
- [fixtures/domains/archaeology/synthetic_candidate_feature/superseded_without_correction_deny.json](../synthetic_candidate_feature/superseded_without_correction_deny.json)
- [Primary bounded test](../../../../tests/domains/archaeology/test_candidate_not_site.py)
- [Related regression coverage](../../../../tests/domains/archaeology/test_no_network_fixtures.py)

After installing the repository's declared test dependencies, run the relevant existing tests from the repository root:

```bash
KFM_NO_NETWORK=1 PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider tests/domains/archaeology/test_candidate_not_site.py tests/domains/archaeology/test_no_network_fixtures.py
```

This command exercises the linked families, not an empty directory or every domain promise. It is provided as a contributor workflow and was not run for this documentation-only edit. Inspect the test assertions before extending their scope; README names and schema-file syntax checks do not establish behavioral coverage.

## Review boundary

Use only small synthetic, public-safe examples under this public fixture root. Keep real provider captures and sensitive records in their governed data lanes. Passing a fixture proves the named implementation's response to those bytes only; admission, policy decisions, source activation, release, deployment and publication remain separate.

Placement and owner routing follow [the reusable fixture-root guide](../../../README.md) and [CODEOWNERS](../../../../.github/CODEOWNERS). The existing [domain fixture index](../README.md) supplies broader context; this guide does not move any source, contract, policy or release responsibility.
