# Validation and Release Gates

## Validation layers
1. **Schema validation** — object shape and enum constraints.
2. **Role validation** — source role supports the asserted claim type.
3. **Temporal validation** — effective/recording times and overlap checks.
4. **Evidence resolution** — EvidenceRef must resolve to bundle members.
5. **Policy validation** — final finite outcome (`ANSWER`, `ABSTAIN`, `DENY`, `ERROR`).

## Minimum negative tests
- living-person public output denied;
- DNA segment public output denied;
- assessor-only title truth denied or abstained;
- boundary precision claim without survey/deed evidence abstained;
- chain-of-title gap produces abstain with reason code.

## Release gate checklist
- ValidationReport exists and is current.
- PolicyDecision exists for the exact target surface.
- EvidenceBundle integrity references are present.
- ReviewRecord status is release-eligible.
- Correction lineage is linked when superseding prior output.
