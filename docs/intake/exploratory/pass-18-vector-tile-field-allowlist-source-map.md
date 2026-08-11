<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-vector-tile-field-allowlist-source-map
title: Pass 18 Vector-Tile Field Allowlist Source Map
type: source-reconciliation
version: v1.0.0
status: proposed; implementation companion; non-authoritative
owners: OWNER_TBD — Intake steward · Fauna steward · Map/UI steward · Policy steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; intake; pass-18; fauna; vector-tile; field-allowlist
responsibility: Reconcile supplied Pass 18 card KFM-P18-INV-400 and Drive discovery context with current repository evidence while preserving tile, evidence, policy-decision, review, release, and publication boundaries.
truth_posture: "CONFIRMED supplied-card text and current repo gap; PROPOSED inactive fixture implementation; UNKNOWN production vocabulary and build integration; NEEDS VERIFICATION human review and hosted CI"
[/KFM_META_BLOCK_V2] -->

# Pass 18 Vector-Tile Field Allowlist Source Map

## Source ledger

| Source | Confirmed contribution | Authority limit |
|---|---|---|
| Supplied `KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf`, printed pages 441–442 (PDF pages 444–445) | Card `KFM-P18-INV-400` proposes whitelisting attributes in public PMTiles/MVT/MLT outputs; it identifies cache inspection, sensitive/unsupported-field leakage, accessibility/Evidence Drawer tension, and a future build-gate direction. | Planning lineage only; the card labels implementation maturity `UNKNOWN`. |
| Google Drive: [`KFM_Full_Atlas_seed_cards`](https://docs.google.com/document/d/1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho/edit) | Candidate-discovery surface consulted before the repository gap assay. | No production field name or release state was imported from the Drive document. |
| `docs/domains/fauna/MAP_UI_CONTRACTS.md` | Requires an `evidence_ref_field`, names a Fauna PMTiles field-allowlist test, and rejects exact sensitive coordinates, observer identity, internal links, credentials/endpoints, and style-only protection on public surfaces. | Human domain guidance; not machine policy or a release decision. |
| `schemas/contracts/v1/data/layer_manifest.schema.json` and `tools/validators/data/validate_layer_manifest.py` | Current strict `LayerManifest` shape already carries `exposure.public_field_allowlist` and requires a non-empty list for public candidates. | Does not compare encoded tile properties with a domain policy profile. |
| Existing `policy/domains/fauna/tile_field_allowlist.yaml` and `tests/domains/fauna/test_tile_field_allowlist.py` at base `86145e882f1a0118c68b7f783816488ceb884694` | Both were placeholders, proving the planned path but not executable behavior. | Placeholder existence is not implementation or authority. |
| `tests/domains/fauna/tiles/README.md` | Already defines the intended test boundary: explicit allowlist, no style-only protection, synthetic/no-network fixtures, and downstream release posture. | The README explicitly reported executable tests, fixtures, validators, and CI as unverified before this slice. |

## Gap assay

| Question | Result |
|---|---|
| Is the source idea already implemented under another stable ID? | `CONFIRMED NO` for the current base: no contract, schema, validator, fixture replay, focused workflow, card-ID hit, open PR, or same-scope branch was found. |
| Does generic `LayerManifest` validation close the gap? | `CONFIRMED NO`: it validates a declared non-empty public allowlist but does not compare candidate encoded fields to a Fauna policy profile. |
| Can this slice safely inspect real tile artifacts? | `HOLD`: no approved production vocabulary, bound build artifact, byte-inspection implementation, or release/correction/rollback closure was verified. |
| Smallest dependency-closed implementation | Inactive semantic contract + policy schema/profile + name-only validator + synthetic exact-polarity fixtures + tests + focused CI + lane documentation. |

## Implemented interpretation

The implementation proves one narrow relation:

```text
required fixture fields ⊆ encoded property names
encoded property names ⊆ LayerManifest public_field_allowlist
LayerManifest public_field_allowlist ⊆ inactive Fauna policy allowlist
```

Every encoded or manifest-declared name is also checked against explicit deny names and bounded deny patterns. `style_only_protection: true` fails. Evidence, policy-decision, review, promotion, release, publication, and public-use claims remain fixed to `false`.

`feature_id` and `evidence_ref` are required only for this synthetic profile so click-to-evidence does not disappear from the fixture. The other allowlisted names remain review candidates. The profile does not approve a production property vocabulary.

## Path decision

| Artifact | Responsibility owner | Path | Rules outcome |
|---|---|---|---|
| Semantic meaning | Contract stewardship | `contracts/domains/fauna/tile_field_allowlist.md` | `PLACE` |
| Machine profile shape | Schema stewardship | `schemas/contracts/v1/domains/fauna/tile_field_allowlist.schema.json` | `PLACE` |
| Inactive allow/deny profile | Policy stewardship | `policy/domains/fauna/tile_field_allowlist.yaml` | `PLACE` |
| Repository validator | Validation tooling | `tools/validators/domains/fauna/tiles/` | `PLACE` |
| Synthetic layer-shaped cases | Fixture stewardship | `fixtures/domains/fauna/layers/tile_field_allowlist_cases.json` | `PLACE` |
| Executable conformance | Test stewardship | `tests/domains/fauna/test_tile_field_allowlist.py` and `tests/domains/fauna/tiles/` | `PLACE` |
| CI orchestration | GitHub platform integration | `.github/workflows/fauna-tile-field-allowlist.yml` | `PLACE` |
| Source reconciliation | Human intake documentation | This file | `PLACE` |

No new repository root, data lane, tile store, layer registry, evidence home, policy-decision home, release record, or public route is created.

## Open decisions held for reviewers

1. Which property names are approved for actual Fauna public layers, by layer and sensitivity class?
2. Are `feature_id` and `evidence_ref` always encoded in tiles, or may a public-safe opaque lookup key replace either one?
3. Which accessibility labels must be encoded versus resolved through a governed downstream surface?
4. Which byte-level inspector will enumerate properties from PMTiles/MVT/MLT artifacts before release?
5. How will tile-size budgets, TileArtifactManifest identity, correction, cache invalidation, and rollback bind to the gate?

Until those questions are resolved, production activation remains `HOLD` and the profile remains fixture-only.

## Rollback

Revert the additive packet and restore the two placeholders. No source, tile, layer, evidence object, policy decision, lifecycle state, release, cache, deployment, or public artifact requires cleanup.
