<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-flora-botanicalsurvey-compat
title: BotanicalSurvey Compatibility Notice
type: compatibility-note
version: v0.1
status: draft; CONFLICTED; NEEDS VERIFICATION before removal or migration
owners: OWNER_TBD — Flora steward · Docs steward · Contract steward
created: 2026-06-21
updated: 2026-06-21
policy_label: public; compatibility; flora; path-drift; no-contract-authority
tags: [kfm, contracts, flora, botanical-survey, compatibility, path-drift, casing-conflict]
related:
  - ./botanical_survey.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../schemas/contracts/v1/domains/flora/botanical_survey.schema.json
notes:
  - "This mixed-case file exists in the repo, but the Flora path register and paired schema point to the lowercase botanical_survey.md contract."
  - "This file is intentionally a compatibility/drift notice, not a competing semantic contract."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# BotanicalSurvey Compatibility Notice

> This file exists only to prevent path/casing drift from becoming parallel contract authority.

<p>
  <img alt="Status: conflicted" src="https://img.shields.io/badge/status-CONFLICTED-orange">
  <img alt="Authority: compatibility only" src="https://img.shields.io/badge/authority-compatibility__only-lightgrey">
  <img alt="Canonical contract: botanical_survey.md" src="https://img.shields.io/badge/canonical-botanical__survey.md-blue">
</p>

`contracts/domains/flora/BotanicalSurvey.md`

## Canonical target

Use the lowercase contract instead:

- [`./botanical_survey.md`](./botanical_survey.md)

## Why this exists

Current repo evidence shows a mixed-case path and a lowercase path both exist:

- `contracts/domains/flora/BotanicalSurvey.md` — this compatibility/drift surface.
- `contracts/domains/flora/botanical_survey.md` — the semantic contract path aligned to the Flora path register and paired schema.
- `schemas/contracts/v1/domains/flora/botanical_survey.schema.json` — the paired schema points to `contracts/domains/flora/botanical_survey.md`.

## Rule

Do not add semantic contract content here. Do not link new docs to this file as the authoritative BotanicalSurvey contract.

## Required cleanup

- [ ] Confirm whether the mixed-case path should be deleted after downstream references are migrated.
- [ ] Confirm no links, docs, tests, fixtures, schemas, or release manifests reference this file as authority.
- [ ] If safe, remove this file with a migration note and rollback target.

## Rollback

Rollback target: prior scaffold blob SHA `9cd9af62d6dbd3ad6b14be2f288f0b3cb8ba751b`.

<p align="right"><a href="#top">Back to top</a></p>
