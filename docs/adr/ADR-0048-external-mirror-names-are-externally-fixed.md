<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0048
adr_id: ADR-0048
title: "ADR-0048 — Names in a receipt-pinned external byte mirror count as externally fixed under Directory Rules §13.2"
type: adr
version: v2.1
status: accepted
effective_decision_status: accepted
accepted_on: 2026-10-12
owners: ["@bartytime4life"]
reviewers_required:
  - Directory governance steward
  - apps/ root owner
created: 2026-10-12
updated: 2026-10-12
policy_label: public
truth_posture: "CONFIRMED owner acceptance on 2026-10-12, the validator implementation, and the Directory Rules digest pins as of main@4fee3f97; PROPOSED literal §13.2 text for the next Directory Rules revision"
owning_root: docs/
responsibility_root: docs/
responsibility: "Decide that file names of upstream-backed entries in a receipt-pinned external byte mirror count as externally fixed under Directory Rules §13.2, scope the decision to the uppercase grammar, and carry the literal §13.2 wording to the next reviewed Directory Rules revision."
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
  - "Accepted by the repository owner on 2026-10-12 as the interpretation of Directory Rules §13.2's externally fixed clause for receipt-pinned external byte mirrors; this is the authority for the topology validator's mirror exemption, replacing reliance on a root README alone."
  - "Acceptance does not change docs/doctrine/directory-rules.md bytes, its adopted digest, or ADR-0029. The literal §13.2 bullet below is carried to the next reviewed Directory Rules revision and digest re-pin."
  - "v2.0 also narrows the exemption to receipt entries that exist upstream and states that the receipt pins content (REVIEW_ONLY), not human review acceptance, after review on #5064."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0048 — Names in a receipt-pinned external byte mirror count as externally fixed under Directory Rules §13.2

**Status:** ACCEPTED (2026-10-12, @bartytime4life)  
**Supersedes:** no existing decision  
**Interprets:** [Directory Rules](../doctrine/directory-rules.md) §13.2 *Safe path grammar* ("externally fixed"), under [ADR-0029](./ADR-0029-adopt-directory-governance-standard-v2.md)  
**Carries to the next doctrine revision:** the literal §13.2 bullet in §3

## 1. Status and authority

This record is **accepted**. It is the decision that interprets §13.2's existing allowance for "externally fixed" names, and that interpretation governs now.

The decision does not change Directory Rules bytes. The doctrine is digest-pinned, so its text and the digest change only through the next reviewed revision (§4). Until then, this ADR is the authority for:
- the topology validator's exemption;
- the [apps/ root naming decision](../../apps/README.md#root-naming-decision-external-site-mirror);
- the `control_plane/external_mirror_register.yaml` projection.

Review of the earlier proposed text on #5064 noted that a root README alone cannot expand §13.2 (`DIR-AUTH-003`). This acceptance answers that concern.

## 2. Context

`apps/site/source/` mirrors the external site source:
- A generated mirror receipt pins the mirrored file set and per-file digests, and records each entry's comparison state.
- The receipt is `REVIEW_ONLY`: it pins content but records no human review acceptance.
- `tools/qa/site_mirror.py --check` enforces content parity with that receipt and reports review acceptance as not evaluated. The water-pilot workflow runs the check.
- Most entries are upstream-backed (`identical`, or overlays of an upstream path). Some are repository-only overlays with no upstream name.

PR #5057 mirrored three upstream files with uppercase names, which broke the topology ratchet. The baseline can only shrink, so the drift could not be waived, and renaming the files in place would break mirror parity. PR #5060 exempted the mirror from the uppercase rule and shrank the uppercase waiver by the ten mirror paths it held. PR #5064 and this decision give that exemption an explicit basis and a narrower scope.

## 3. Decision

1. **Interpretation (effective 2026-10-12).** A file name counts as *externally fixed* under §13.2 when all of the following hold:
   - the file sits in a registered byte mirror of an external source;
   - the file's entry in the mirror's pinned receipt shows that the path **exists upstream** (it carries an upstream digest);
   - an enforced parity check verifies the mirror against that receipt.

   The allowance covers **casing only**. Unsafe-path and nonportable-punctuation rules still apply.
2. **Repository-only entries are not covered.** A receipt entry with no upstream path, or a file absent from the receipt, follows the default lowercase grammar even inside a registered mirror.
3. **Renames.** Covered names change only upstream and arrive through a mirror sync with a fresh receipt. They are never renamed in place.
4. **Literal doctrine text (next revision).** At the next reviewed Directory Rules revision, add this bullet to §13.2 after the lowercase rule:

   > - treat a file name inside a registered byte mirror of an external source as externally fixed when the mirror's pinned receipt shows the path exists upstream and an enforced parity check verifies the mirror against that receipt; such names change only upstream and arrive through a mirror sync, never by an in-place rename; the allowance covers casing only, and unsafe-path and nonportable-punctuation rules still apply.

### Qualifying conditions and current instance

| Condition | Current instance (`apps/site/source/`) |
|---|---|
| The mirror copies a named external source | The external site source; `site_candidate_commit` is recorded per receipt |
| A generated receipt pins the file set, digests and upstream presence | The receipt pinned by `RECEIPT` in `tools/qa/site_mirror.py` (it changes with each mirror sync); `REVIEW_ONLY`, so it pins content, not human acceptance |
| An enforced parity check fails on drift | `tools/qa/site_mirror.py --check` (water-pilot workflow) |
| The mirror is registered with its receipt, check and relaxed rule | `mirror.apps-site-source` in `control_plane/external_mirror_register.yaml` |
| The validator relaxes only the uppercase rule, only for upstream-backed receipt entries | `_external_mirror_prefixes` / `_external_mirror_exempt_paths` in `validate_repository_topology.py` |

## 4. Consequences

- The exemption rests on an accepted decision rather than a root README.
- Repository-only overlays cannot use the mirror to bypass the lowercase grammar.
- When a mirror sync replaces the pinned receipt, the register's `receipt_path` must follow it. A test asserts that it matches `site_mirror.py`.
- **Re-pinning cost at the next doctrine revision.** The Directory Rules digest `sha256:44f7e943…` (blob `fd49a0b8…`) is pinned in:
  - five validators: `validate_root_registry.py`, `validate_repository_topology.py`, `validate_domain_lane_register.py`, `validate_cross_domain_seam_register.py` and `path_alias_model.py`;
  - `control_plane/root_registry.yaml`;
  - the control-plane registers, including the external mirror register;
  - about 747 rows of `control_plane/verification_backlog.yaml`;
  - many README evidence snapshots;
  - ADR-0029's adoption binding.

  Bundle the §13.2 text with other pending doctrine edits so the re-pin happens once.

## 5. Alternatives considered

| Option | Outcome |
|---|---|
| Rely on the apps/ root README decision only | Rejected after review: a root README cannot expand §13.2 (`DIR-AUTH-003`). |
| Amend §13.2 bytes now | Deferred to the next revision: that needs the full digest re-pin, and acceptance alone settles the interpretation. |
| Exempt the whole mirror prefix | Rejected after review: repository-only overlays have no upstream name, so exempting them would bypass the grammar. |
| List each mirror path in Directory Rules | Rejected: it couples doctrine to implementation paths. |
| Rename mirrored files to lowercase | Rejected: this breaks mirror parity and the receipt, and the next sync reintroduces the names. |
| Exempt the mirror from all path-grammar rules | Rejected: unsafe and nonportable names stay hazardous whatever their origin. |

## 6. Validation

- The topology validator raises on a malformed or digest-unbound register. It relaxes nothing for an absent register, a `RETIRED` entry, an untracked receipt or parity check, or a receipt entry without an upstream digest.
- The tests cover each of these cases, plus a live check that the register's `receipt_path` equals `site_mirror.py`'s pinned receipt.
- The doctrine revision that adds the §4 text must re-pin every digest reference and keep the topology, root-registry, path-alias, domain-lane, cross-domain-seam and governance-parity checks green.

## 7. Rollback and supersession

Supersede this ADR with a new accepted decision. Removing the exemption would then require renaming the affected names upstream first, or another reviewed approach, because the topology baseline cannot grow.

## 8. Open questions

| ID | Question | Owner |
|---|---|---|
| OQ-ADR-0048-01 | **Resolved 2026-10-12 (owner):** mirrors are listed in `control_plane/external_mirror_register.yaml`, which the topology validator reads. The topology run context (v3) also records the register as an indexed governance input, under successor authoring receipt `genrec-topology-mirror-register-context-20261012`. | Directory governance steward |
| OQ-ADR-0048-02 | Which other pending Directory Rules edits should share the §13.2 revision, to pay the re-pin cost once? | Directory governance steward |

## 9. Change history

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-10-12 | Proposed (owner-requested) after #5060 and the apps/ root naming decision. |
| v1.1 | 2026-10-12 | OQ-ADR-0048-01 resolved: the mirror is listed in `control_plane/external_mirror_register.yaml`. |
| v2.1 | 2026-10-12 | Topology execution context v3 records `external_mirror_register` among its indexed governance inputs (successor receipt `genrec-topology-mirror-register-context-20261012`). |
| v2.0 | 2026-10-12 | Accepted by @bartytime4life as the operative interpretation of §13.2, in response to review on #5064. Scope narrowed to upstream-backed receipt entries, and the receipt described as content-pinned (`REVIEW_ONLY`), not human-reviewed. |

<p align="right"><a href="#top">Back to top</a></p>
