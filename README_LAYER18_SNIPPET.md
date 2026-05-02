## Layer 18 — Compliance Control Mapping + OSCAL Assurance Pack Compiler

### CLI examples
```bash
python soilgrids_assurance_pack.py --assurance-spec assurance/assurance_spec.json --output-root assurance_packs --mode catalog-only
python soilgrids_assurance_pack.py --assurance-spec assurance/assurance_spec.json --evidence-corpus evidence_crates/<crate_id>/evidence_corpus.json --output-root assurance_packs --mode map-evidence
python soilgrids_assurance_pack.py --assurance-spec assurance/assurance_spec.json --evidence-corpus evidence_crates/<crate_id>/evidence_corpus.json --output-root assurance_packs --mode assess
python soilgrids_assurance_pack.py --assurance-spec assurance/assurance_spec.json --evidence-corpus evidence_crates/<crate_id>/evidence_corpus.json --output-root assurance_packs --mode oscal-export
python soilgrids_assurance_pack.py --assurance-spec assurance/assurance_spec.json --evidence-corpus evidence_crates/<crate_id>/evidence_corpus.json --output-root assurance_packs --mode certify-assurance
```

### Output summary
- ControlCatalog.v1 / ControlProfile.v1 / ControlImplementationMatrix.v1
- ControlEvidenceMap.v1 / AssessmentResults.v1 / RiskRegister.v1 / GapAnalysisReport.v1 / CorrectiveActionPlan.v1 / AssuranceGateReport.v1
- AssuranceNarrative.v1
- OSCAL-style JSON in `oscal/`
- AssurancePackManifest.v1 + AssurancePackReceipt.v1 + `checksums.sha256`

### Exit codes
- `0` success
- `5` dry-run success
- `10` warning
- `20` gate fail
- `30..100` typed failures (input/evidence/catalog/assessment/oscal/opa/safety/internal)

> This layer builds an assurance package only. It does **not** mutate source evidence and does **not** provide legal certification claims.
