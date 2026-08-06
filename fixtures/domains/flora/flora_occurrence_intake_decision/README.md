# `FloraOccurrenceIntakeDecision` synthetic fixtures

This fixture family is no-network and contains no real protected locality, source credential, legal-rights decision, source-admission decision, or public release.

Finite valid decisions cover:

- `ACCEPT_FOR_WORK` for an explicitly mapped open license with no source sensitivity hint;
- `QUARANTINE` for missing and conditional license text;
- `HOLD_FOR_REVIEW` when source generalization/withholding hints accompany internal exact geometry; and
- `DEDUPLICATE` through primary institution/catalog identity and the bounded spatiotemporal/taxon fallback.

Error fixtures cover candidate hash drift, governance overclaim, and a peer set that contains the candidate itself. `expected_outcomes.json` binds each case to its exact outcome, finding-code set, and expected decision object where applicable.

The `../flora_occurrence_candidate/` references intentionally make this a stacked fixture slice over the candidate-normalizer PR. A passing replay proves only deterministic intake classification; no lifecycle transition is executed.
