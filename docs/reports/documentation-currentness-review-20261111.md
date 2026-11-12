<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/reports/documentation-currentness-review-20261111
title: Repository documentation currentness review
type: review-report
version: v1.0
status: source-grounded; review-required; documentation-only
owners: ["@bartytime4life"]
created: 2026-11-11
updated: 2026-11-11
policy_label: public-documentation
owning_root: docs/
responsibility: record documentation scope, source identity, validation and unresolved debt
truth_posture: CONFIRMED repository and recorded validation for the declared revisions; NEEDS VERIFICATION remaining metadata, source, browser, deployment and publication acceptance
related:
  - ../README.md
  - ../installation.md
  - ../runbooks/documentation-maintenance.md
  - ../../apps/site/README.md
[/KFM_META_BLOCK_V2] -->

# Repository documentation review — November 11, 2026

The current repository Explorer includes the recovery and replay corrections
merged through [PR #5822](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5822).
This review updates active reader paths and scans the tracked Markdown set.
It does not assert that every historical/domain claim has been independently
requalified or that every documentation metadata/graph finding is resolved.

## Source and validation identities

| Surface | Exact identity and evidence | Limit |
|---|---|---|
| Documentation base | main `d4d84171653a2f2582b48ece511dc010857fde15` | Repository source, not a deployed version |
| Latest application correction | PR #5822 head `8a532b34eb691c06a53325ef553ea248ebbb11d5` | Its tree equals the inspected merge tree |
| Recorded local application checks | Node 22.13.1, clean exact-lock install, build/containment, nonincremental types, 1,804 Site tests | Recorded correction evidence; not a new execution caused by these prose edits |
| Recorded lint | Zero errors and 77 inherited warnings | No claim of warning-free lint |
| Recorded conformance | 380 checks, including 79 mirror checks | Bounded selected suites, not every monorepo test |
| Recorded local route smoke | 110 checks across 79 routes; 14 provider-only routes unexercised | Disposable local state, no live-provider acceptance |
| Submitted-head CI for #5822 | 52 successful workflows and one skip at November 11 readback | Exact correction head; documentation-PR CI is separate |
| Browser acceptance | Interval-load browser acceptance pending; tool could not create a usable test tab | Native Node loopback HTTP tests are transport evidence only |
| Earlier public Node qualification | October 27 source `bbcec824fe57e6be0409ba1e35d737fa99581560` | Historical 1,934 pass/19 skip result; not the repository mirror's count |
| Showcase media | Source `974d3b340e619effc91d8da98cf9e67d95119df9` | Existing October renderer derivatives; not new screenshots or live observations |

The [October showcase qualification](documentation-showcase-qualification-20261027.md)
and prior correction notes retain their original hashes, dates and results.
The public website, preserved private Site, local installation and monorepo
have separate source and storage histories. No fresh deployment or provider/model
operation is established by this documentation update.

## Documentation closure

- Root README, documentation map, installation, contribution guidance and wiki
  orientation now route readers to the current repository Explorer workflow.
- The [Explorer index](../../apps/site/source/docs/README.md) links every Markdown
  guide in that directory, separating topic guides, preservation/integration
  references and dated implementation notes.
- The [Observatory guide](../../apps/site/source/docs/observatory-replay.md)
  describes interval selection, source clocks, committed-record inspection,
  follow-today refresh, per-read deadlines, local fallback and retry.
- Archive, domain and runbook navigation repairs address 22 of the initial
  23 broken local targets. One catalog anchor is held by the frozen-root rule,
  as described below. Absent outline sections are marked unmaterialized rather
  than replaced with empty targets.
- Twenty app documentation envelopes receive missing ownership/responsibility/
  truth-posture fields or a bounded type token. Their historical implementation
  narratives and runtime qualification are not promoted by this metadata repair.
- Four navigation guides replace unassigned ID placeholders with distinct,
  path-based review candidates. Their exact previous metadata envelopes remain
  quoted from the base revision. Current relationships receive verified path/case
  corrections; 22 retired or unmaterialized pointers remain explicitly labeled
  `unresolved_related`. They are not silently rebound to another contract or
  treated as existing implementation.
- The [maintenance runbook](../runbooks/documentation-maintenance.md) supplies
  reproducible changed-file checks and a whole-tree tracked Markdown audit.

## Whole-tree audit and remaining work

The baseline inventory contains **5,071 tracked Markdown files**. The no-network
link checker inspected **121,367 local targets**, finding twenty missing anchors
and three missing paths. It classified **13,449 external targets as unverified**
without requesting them. The parser's inline HTML and other stated exclusions
remain separate from these results.

The broader metadata, graph and freshness workbench used **2,009 tracked files**
in README, docs, apps and the documentation-validator lane. Explicit tracked
paths avoid ignored runtime/dependency directories. Baseline results:

| Check | Observed baseline | Disposition |
|---|---|---|
| Metadata, present profile | 62 failure findings; 512 invalid envelopes; warning/report limits also apply | Repair routine app-envelope omissions; retain explicit remaining debt |
| Freshness, advisory as of November 11 | 17 invalid-date failures plus warning signals | Unknown original dates remain unknown; review is not proof of creation provenance |
| Document graph | 722 failure findings in a bounded 1,000-finding report | Unresolved related paths/IDs and other graph debt need source/identity review; no automatic rebinding |

The remaining metadata findings include nested historical envelope structures
outside the parser's bounded profile and template/ADR material. Adopted/frozen
authority bytes, source IDs and historical creation dates are not rewritten to
appease a validator. A fresh `updated` field is not whole-document factual
acceptance. The graph report is bounded and is not a complete defect census.

The final tracked set contains **5,075 Markdown files**. A broad candidate link
scan passed, but the subsequent topology check identified one correction inside
the frozen catalog root. After preserving that file's original bytes, the final
whole-tree link disposition is **PARTIAL: one inherited anchor remains held**.
The 51 updated documents receive a separate final local-target check.

Current scoped metadata, graph and freshness checks complete with warnings and
zero failures; all 34 present metadata envelopes in that scope are valid. The
17 other updated documents retain their own non-v2 format. Raw registry-coupled
metadata scanning also reports seven findings in the unchanged machine register;
those findings are not repaired or relabeled as a clean whole-tree registry.
The existing documentation/wiki/artwork validator selection passes 148 tests and
249 subtests. Current mirror QA passes 80 checks, and strict parity accounts for
951 files with all 262 withheld carriers absent. Final submitted-head CI remains
separate. The application suite/build are not repeated for prose-only edits.

A changed-file pass does not erase the whole-tree findings. External-link health,
every semantic cross-reference, full accessibility/rendering and independent
domain stewardship remain outside this local audit.

## Frozen catalog navigation proposal

`catalog/domain/settlements-infrastructure/README.md` links to
`#appendix-a--no-loss-preservation`, but its existing detail section lacks that
explicit anchor. The minimal proposal adds the following immediately before
that section's existing `<details>` element:

```html
<a id="appendix-a--no-loss-preservation"></a>
```

The unchanged base blob is `17f0824ba92dbdfe169df29b7abafbce5e10c489`; the proposed
anchor-only blob is `4dec0416c132c99fb3a55bd0a085dfb79f3a8a37`. This patch is
proposed only. KFM-TOPO-004 freezes the catalog tree, and
[ADR-0038](../adr/ADR-0038-trusted-base-topology-correction-transitions.md)
requires a separately accepted trusted-base exact transition. Its documented
acceptance/binding/consumer sequence is not established for this change. The
catalog file and topology baseline therefore remain byte-for-byte unchanged.
No same-change exception, expanded waiver or automatic restore is introduced.

## Inventory, authority and rollback

Documentation changes inside the Site mirror receive an append-only successor
to the interval-recovery receipt. Current-byte parity is checked against that
successor. Original Site identity, historical receipts, source mappings, all
262 withheld carriers and pending source/overlay review remain. Human acceptance
and hosted equivalence remain false.

Directory Rules v2 as adopted by ADR-0029 retains existing responsibility roots:
human guides and review under docs, application guides in the Site mirror,
generated inventory under data/receipts/generated, selector under tools/qa and
regression under tests/qa. Archive navigation edits follow its versioned
metadata/index allowance; no archived lineage record is changed.

Revert erroneous prose, navigation and its successor selector/QA as one unit,
retaining historical receipts. No application behavior, dependency, operational
store, source admission, activation, access, deployment or publication changes.
Native wiki synchronization remains separate from this reviewable source packet.
