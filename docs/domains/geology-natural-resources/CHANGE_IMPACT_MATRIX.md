# Geology & Natural Resources Change Impact Matrix

Use this matrix to identify required review and validation surfaces when making geology lane changes.

| Change type | Minimum review surfaces | Minimum validation surfaces |
| --- | --- | --- |
| Update source-role definitions | `README.md`, `SOURCE_INDEX.md`, policy docs | Source-role policy tests, schema fixtures for affected objects |
| Add/modify contract fields | `SCHEMA_INDEX.md`, contract docs, migration notes | Schema validation, invalid fixture tests, runtime proof checks |
| Change public-safe geometry rules | `README.md`, `DATASET_OR_LAYER_INDEX.md`, policy docs | Redaction/generalization tests, leakage deny tests |
| Introduce or alter cross-lane relation types | `CROSS_LANE_RELATIONS.md`, related lane docs | Relation validation tests, deny-rule tests |
| Update layer descriptor requirements | `DATASET_OR_LAYER_INDEX.md`, UI/API docs | Evidence lookup resolution tests, release-linkage checks |
| Change release or rollback expectations | `README.md`, runbook docs | Release manifest checks, proof/receipt completeness checks |

## Review trigger checklist

- [ ] Did this change alter source authority semantics?
- [ ] Did this change increase public exposure of exact geometry?
- [ ] Did this change require new invalid fixtures?
- [ ] Did this change alter cross-lane boundaries?
- [ ] Did this change require release or rollback procedure updates?
