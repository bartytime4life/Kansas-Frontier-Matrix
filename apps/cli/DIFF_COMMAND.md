<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://app/cli/diff-command
title: CLI diff command
type: app-guide
version: v0.1
status: draft
owner: TODO-cli-steward
created: 2026-09-25
updated: 2026-09-25
policy_label: public
owning_root: apps/
responsibility: checkout-local read-only comparison command
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - README.md
  - src/kfm_cli/__main__.py
  - src/kfm_cli/commands/diff.py
  - ../../tools/diff/README.md
  - ../../tests/cli/test_diff_command.py
[/KFM_META_BLOCK_V2] -->

# CLI diff command

From the repository root with Python 3, run:

```sh
PYTHONPATH=apps/cli/src python -m kfm_cli diff json --left before.json --right after.json
PYTHONPATH=apps/cli/src python -m kfm_cli diff release --left old-manifest.json --right new-manifest.json --fail-on-change
```

`json` delegates to [`stable_diff.py`](../../tools/diff/stable_diff.py), which compares top-level JSON object keys. `release` delegates to [`release_diff.py`](../../tools/diff/release_diff.py), which requires typed candidate ReleaseManifest objects and compares artifact references. Both accept `--output` and `--fail-on-change`; help is available with `diff json --help` or `diff release --help`. Exit codes are `0` for a valid comparison, `1` for changes when `--fail-on-change` is set, and `2` for invalid input or output errors. This command runs against a repository checkout and needs the adjacent `tools/diff/` directory.

Reports are comparison aids only. This command does not validate release readiness, decide policy, write lifecycle records, approve publication, or run the other CLI placeholder commands. The `json` comparator's output-path safety is inherited from that existing tool; do not point `--output` at either input file. The release comparator rejects colliding input/output paths and symbolic link outputs.

Verification: `python -m unittest discover -s tests/cli -p 'test_*.py' -v`.
