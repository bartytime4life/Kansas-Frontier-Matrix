# Governance tests

`tests/governance/` contains deterministic tests for bounded governance
validators, routing helpers, and read-only issue-inventory projections. These
tests verify repository code and fixtures at the checked-out commit. They do
not create governance authority, approve review, admit a source, close
evidence, mutate GitHub, release, deploy, or publish.

## Suite inventory

| Test module | Confirmed coverage |
| --- | --- |
| [`test_briefing_signal.py`](test_briefing_signal.py) | Closed `1.2.0` schema, fixture polarity, deterministic identity, parser safety, examples, false-authority denial, value-minimized CLI output, and active network denial |
| [`test_briefing_signal_dedup.py`](test_briefing_signal_dedup.py) | Cluster stability, replay, collision detection, duplicate classification, input-order invariance, dry-run-only output, and active network denial |
| [`test_briefing_signal_materiality.py`](test_briefing_signal_materiality.py) | Exact materiality thresholds, mandatory overrides, six finite route profiles, schema-valid semantic negatives, deterministic reporting, and active network denial |
| [`test_briefing_signal_issue_inventory.py`](test_briefing_signal_issue_inventory.py) | Closed issue-inventory projections, existing-target binding, missing/closed/ambiguous target holds, invalid-inventory precedence, deterministic reports, and absence of mutation clients |
| [`test_briefing_signal_live_issue_inventory.py`](test_briefing_signal_live_issue_inventory.py) | Binding a stored GitHub issue-read receipt to BriefingSignal routing, identity reproduction, freshness and `as_of` requirements, fixture/live-input separation, and active network denial |
| [`test_github_issue_inventory_read.py`](test_github_issue_inventory_read.py) | Fixture-backed issue-read schema, repository/ref binding, pull-request exclusion, rate-limit holds, explicit staleness, and deterministic identity |

The “live” binding test uses the committed read receipt under
[`fixtures/contracts/v1/governance/github_issue_inventory_read/`](../../fixtures/contracts/v1/governance/github_issue_inventory_read/).
It does not query GitHub during the test.

## Run locally

From the repository root, run the complete directory:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m unittest discover \
  --start-directory tests/governance \
  --pattern 'test_*.py' \
  --verbose
```

To match the two hosted workflow boundaries separately:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m unittest discover \
  --start-directory tests/governance \
  --pattern 'test_briefing_signal*.py' \
  --verbose

KFM_NO_NETWORK=1 python -m pytest \
  tests/governance/test_github_issue_inventory_read.py \
  -q --strict-config --strict-markers
```

The environment flag records the intended execution posture. The five
`test_briefing_signal*.py` modules also patch socket and
`urllib.request` access so a network attempt fails the suite. The standalone
issue-read test exercises stored fixture data and pure projection behavior.

## Hosted workflow bindings

- [Briefing Integration](../../.github/workflows/briefing-integration.yml)
  watches `tests/governance/**` and directly runs every
  `test_briefing_signal*.py` module.
- [GitHub Issue Inventory Read](../../.github/workflows/github-issue-inventory-read.yml)
  watches and directly runs `test_github_issue_inventory_read.py`.

No dedicated Make target is claimed for this directory. A passing local
command does not prove that a hosted check is required, current, or successful
at another commit.

## Interpret results

- Expected rejection of an invalid fixture is a passing negative test, not a
  validator failure.
- `HOLD`, stale, missing-target, closed-target, ambiguous-target, and
  rate-limit outcomes are bounded domain results when the fixture expects
  them; they are not approval or mutation instructions.
- Import, collection, dependency, or unexpected-network failures mean the
  suite did not establish its behavioral claims.
- A valid BriefingSignal, issue projection, or read receipt remains a
  non-authoritative candidate. It does not prove the underlying claim, issue
  state at another time, accountable review, or permission to write to GitHub.

## Maintenance

When this directory changes:

1. update the inventory and complete-directory command in the same change;
2. keep fixture-backed and externally acquired evidence clearly distinct;
3. preserve exact invalid-fixture findings and finite outcomes;
4. link a workflow only when its current YAML directly invokes the test; and
5. keep validation, review, GitHub mutation, release, deployment, promotion,
   and publication as separate states.
