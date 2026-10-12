<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0048
adr_id: ADR-0048
title: "ADR-0048 — Names in a receipt-pinned external byte mirror count as externally fixed under Directory Rules §13.2"
type: adr
version: v1.1
status: proposed
owners:
  - "NEEDS VERIFICATION — directory governance steward"
  - "NEEDS VERIFICATION — apps/ root owner"
reviewers_required:
  - Directory governance steward
  - apps/ root owner
  - Docs steward
created: 2026-10-12
updated: 2026-10-12
policy_label: public
truth_posture: "PROPOSED doctrine wording; CONFIRMED current validator exemption, apps/ root naming decision, and digest pins as of main@d9887c7e"
owning_root: docs/
responsibility_root: docs/
responsibility: "Propose explicit Directory Rules §13.2 wording that treats file names inside a receipt-pinned byte mirror of an external source as externally fixed, for adoption at the next Directory Rules revision; until then the apps/ root naming decision governs."
current_path: docs/adr/ADR-0048-external-mirror-names-are-externally-fixed.md
supersedes: []
related:
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - apps/README.md
  - apps/site/README.md
  - tools/qa/site_mirror.py
  - tools/validators/directory_governance/validate_repository_topology.py
  - control_plane/external_mirror_register.yaml
tags: [kfm, adr, directory-governance, path-grammar, mirror, apps]
notes:
  - "Proposed only. It does not change docs/doctrine/directory-rules.md bytes, its adopted digest, or ADR-0029; the wording below takes effect only through an accepted ADR and a reviewed Directory Rules revision."
  - "The behavior it describes is already implemented narrowly: the topology validator's apps/site/source/ uppercase exemption (#5060) and the apps/ root naming decision (apps/README.md v0.10)."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0048 — Names in a receipt-pinned external byte mirror count as externally fixed under Directory Rules §13.2

**Status:** PROPOSED (2026-10-12)  
**Supersedes:** no existing decision  
**Amends, if accepted:** [Directory Rules](../doctrine/directory-rules.md) §13.2 *Safe path grammar*, at its next reviewed revision under [ADR-0029](./ADR-0029-adopt-directory-governance-standard-v2.md)

## 1. Status and authority

This record is **proposed**. It does not amend Directory Rules. Under Directory Rules §2.3 and `DIR-AUTH-001`, a proposed ADR cannot change placement doctrine.

The current rule comes from two places:
- §13.2 already allows uppercase for "externally fixed standards or repository entrypoint filenames".
- The [apps/ root naming decision](../../apps/README.md#root-naming-decision-external-site-mirror) applies that allowance to `apps/site/source/`. Directory Rules §2.3 makes this a root README decision.

## 2. Context

`apps/site/source/` is a byte mirror of the external site source:
- The reviewed mirror receipt pins its file set and per-file digests.
- `tools/qa/site_mirror.py --check` enforces that the mirror matches the receipt. The water-pilot workflow runs this check.

PR #5057 mirrored three upstream files whose names are uppercase (`docs/LAYER_BROWSER_VALIDATION_2026-10-11.md` and two siblings). That broke the topology ratchet on `main`. The baseline may only shrink, so the drift could not be waived. Renaming the files in the repository would also have broken mirror parity and made the receipt's `identical` claims false.

PR #5060 fixed `main` by exempting `apps/site/source/` from the uppercase path-grammar check only. Doing so shrank the uppercase waiver by the ten mirror paths it held. The behavior is justified by §13.2's "externally fixed" clause, but that clause does not mention mirrors. A reader of Directory Rules alone cannot tell that mirrored names qualify, or under what conditions.

## 3. Decision (proposed)

At the next reviewed Directory Rules revision, add this bullet to §13.2, after the lowercase rule:

> - treat file names inside a registered byte mirror of an external source as externally fixed when a reviewed receipt pins the mirror's file set and an enforced parity check verifies it; such names change only upstream and arrive through a reviewed mirror sync, never by an in-place rename; the allowance covers casing only, and unsafe-path and nonportable-punctuation rules still apply.

The record also proposes these conditions for any mirror to qualify:

| Condition | Current instance (`apps/site/source/`) |
|---|---|
| The mirror is a one-way byte copy of a named external source | The external site source; `site_candidate_commit` is recorded per receipt |
| A reviewed receipt pins the file set and digests | `data/receipts/generated/site-v246-underground-browser-review-20261011.json` and its successors |
| An enforced parity check fails on drift | `tools/qa/site_mirror.py --check` (water-pilot workflow) |
| The owning root records the decision | `apps/README.md` §Root naming decision |
| The mirror is registered, and the validator relaxes only the listed rule for that prefix | `mirror.apps-site-source` in `control_plane/external_mirror_register.yaml`, read by `validate_repository_topology.py` (`_external_mirror_prefixes`) |

A new mirror that does not meet every condition follows the default lowercase grammar.

## 4. Consequences

- Directory Rules will state the mirror case explicitly instead of relying on a root README to interpret §13.2.
- **Re-pinning cost on adoption.** The Directory Rules digest `sha256:44f7e943…` (blob `fd49a0b8…`) is pinned in:
  - five validators: `validate_root_registry.py`, `validate_repository_topology.py`, `validate_domain_lane_register.py`, `validate_cross_domain_seam_register.py` and `path_alias_model.py`;
  - `control_plane/root_registry.yaml`;
  - the control-plane registers;
  - about 747 rows of `control_plane/verification_backlog.yaml`;
  - many README evidence snapshots;
  - ADR-0029's adoption binding.

  Adoption must re-pin these in one reviewed change, following the Directory Rules adoption steps (record the adopting decision, approvers, effective date, content digest and supersession targets).
- Bundling this wording with other pending Directory Rules edits would avoid paying the re-pin cost twice.

## 5. Alternatives considered

| Option | Outcome |
|---|---|
| Keep the root README decision only (status quo) | Works today, but the doctrine stays silent and each new mirror needs its own interpretation. |
| Amend §13.2 directly without an ADR | Rejected: §2.3 and `DIR-AUTH-001` require an accepted decision for a rule change, and the digest pins would break. |
| List each mirror path in Directory Rules | Rejected: it couples doctrine to implementation paths and would need a doctrine revision for every new mirror. |
| Rename mirrored files to lowercase | Rejected: this breaks mirror parity and the receipt, and the next sync reintroduces the names. Renames belong upstream. |
| Exempt the mirror from all path-grammar rules | Rejected: unsafe and nonportable names stay hazardous whatever their origin. |

## 6. Validation and acceptance

Acceptance requires:
- review by the directory governance steward and the apps/ root owner;
- a Directory Rules revision that applies the wording and re-pins every digest reference;
- green topology, root-registry, path-alias, domain-lane, cross-domain-seam and governance-parity checks on that revision.

Until then, `validate_repository_topology.py`'s scoped exemption and `apps/README.md` remain the operative record.

## 7. Rollback and supersession

If this ADR is rejected:
- §13.2 stays as written.
- The apps/ root naming decision continues to govern `apps/site/source/` as a root-level interpretation.
- Removing the validator exemption would need the mirror's uppercase names to be renamed upstream first, or a new reviewed waiver approach, because the baseline cannot grow.

## 8. Open questions

| ID | Question | Owner |
|---|---|---|
| OQ-ADR-0048-01 | ~~Should qualifying mirrors be listed in a machine register instead of as a validator prefix constant?~~ **Resolved 2026-10-12 (owner):** yes. `control_plane/external_mirror_register.yaml` lists them, and the validator reads it and fails closed. The register projects the current §13.2 interpretation and the apps/ root decision; it does not adopt this ADR. Follow-up: the topology run context (`render_repository_topology_diagnostics.py`, receipt-pinned) does not yet record this register's digest among its indexed governance inputs. | Directory governance steward |
| OQ-ADR-0048-02 | Which other pending Directory Rules edits should share the same re-adoption, to pay the re-pin cost once? | Directory governance steward |

## 9. Change history

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-10-12 | Proposed (owner-requested) after #5060 and the apps/ root naming decision. |
| v1.1 | 2026-10-12 | OQ-ADR-0048-01 resolved: the mirror is listed in `control_plane/external_mirror_register.yaml`, which the topology validator reads. Status remains proposed. |

<p align="right"><a href="#top">Back to top</a></p>
