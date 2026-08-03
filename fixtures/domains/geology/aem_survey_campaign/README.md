# GMD 3 AEM announcement-bound campaign-candidate fixture profile

This lane contains one frozen, document-specific `AemSurveyCampaign` candidate
and exact negative cases for
`tools/validators/domains/geology/validate_aem_campaign.py`.

Profile ID:

    kfm-geology-gmd3-aem-campaign-candidate-fixture-v1

The positive fixture records that a KU News document published 2026-05-11
reported a GMD 3 AEM campaign as planned. It separately records current
campaign state as unknown and acquisition evidence as not bound to this
profile. It does not assert whether acquisition occurred.

The fixture contains no county coverage, target or achieved depth, current
schedule, raw acquisition, processing, inversion, datum, resistivity,
uncertainty, frequency-system, footprint-geometry, or product identity.

`supporting_reference_candidates` contains one exact typed fixture reference.
The validator checks its frozen identity but does not resolve an `EvidenceRef`
or `EvidenceBundle`; passing does not establish evidence binding or closure.

The linked document-specific `SourceDescriptor` fixture is citation-only,
candidate-only, rights-unresolved, restricted, connector-disabled,
review-required, proposed, and not released. Its exact bytes are pinned so
prose, endpoint, credential, connector, source-head, release-condition, and
claim-role drift fails closed. It is fixture input, not source-registry
authority. The broader domain-first compatibility registry YAML uses a
different source ID and is not read or endorsed by this profile.

## Inventory

`valid/valid_1.json` is the one positive case.

`invalid/` contains exact cases for:

- acquisition-evidence upcast;
- current-campaign-state upcast;
- correction reference outside the typed namespace;
- downstream-stage field leakage;
- false release state;
- absent and wrongly typed supporting references;
- missing required limitation;
- silent and self-referential correction lineage;
- an ambiguous unscoped planning field.

Every invalid JSON file has one sorted `.expected_error.txt` sidecar containing
only a stable finding code and JSON path.

## Run

    PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
      python tests/domains/geology/test_aem_campaign.py --verbose

Passing proves only deterministic behavior for these repository fixtures. It
does not prove current campaign state, acquisition, product existence,
scientific fitness, rights, evidence, policy, review approval, source
activation, release, or publication.

Rollback is a focused revert. No source, lifecycle, proof, release, or
published state is created by this profile.
