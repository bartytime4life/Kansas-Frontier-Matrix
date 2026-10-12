# Composed Claim Dependency Closure Fixtures

Synthetic, public-safe fixtures for `kfm.composed-claim-dependency-closure.v1`.

| Lane | Purpose |
|---|---|
| `valid/` | Eight schema-valid, semantically valid records covering `SUPPORTED`, `QUALIFIED`, `ABSTAIN`, `DENY`, and `ERROR`. |
| `semantic_invalid/` | Schema-valid records with exact expected semantic finding codes. |
| `invalid/` | Closed-schema authority and enum violations that must fail before semantic evaluation. |

The fixtures use non-joinable identifiers and perform no network request, EvidenceRef resolution, policy decision, review, promotion, release, deployment, publication, or public use.

Validation:

```bash
python tools/validators/validate_composed_claim_dependency_closure.py --fixtures
```
