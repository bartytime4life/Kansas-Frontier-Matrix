<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/documentation-maintenance
title: Maintain KFM documentation
type: runbook
version: v1.0
status: source-grounded; review-required; documentation-only
owners: ["@bartytime4life"]
created: 2026-11-11
updated: 2026-11-11
policy_label: public-documentation
owning_root: docs/
responsibility: source-bound documentation maintenance and reproducible local QA
truth_posture: CONFIRMED command definitions at main@d4d84171653a2f2582b48ece511dc010857fde15; QA does not establish factual, review or publication acceptance
related:
  - ../README.md
  - ../../CONTRIBUTING.md
  - ../../tools/validators/docs/README.md
[/KFM_META_BLOCK_V2] -->

# Maintain KFM documentation

Use this procedure when implementation, configuration, source identity or reader
navigation changes. Begin with the [documentation map](../README.md) and
[currentness review](../reports/documentation-currentness-review-20261111.md).

## Preserve identity before editing

Record the checkout, branch, base and unfinished changes. Use an isolated branch
or worktree. Inspect the implementation and relevant folder guidance before
changing a factual claim. Keep monorepo, public Node, preserved Site, installed
runtime, browser, CI and deployment evidence separate.

Update active guidance in place and link one current explanation from the entry
points. Keep dated qualification reports, media manifests, adopted document bytes
and append-only receipts bound to their original inputs. Archive metadata and
indexes may receive verified navigation corrections under the
[archive boundary](../archive/README.md#mutability-and-retention); archived records
retain their historical claims. An unknown original creation date remains unknown.

## Run checks for the changed documents

Use Python 3.12. During editing, pass the explicit changed files to each tool;
`--git-diff` only sees committed revisions. After committing a review branch,
run from the repository root:

```bash
base_sha="$(git merge-base origin/main HEAD)"
python3.12 tools/validators/docs/link-check/check_links.py --repo-root . --git-diff "${base_sha}...HEAD" --format text
python3.12 tools/validators/docs/meta-block/check_meta_blocks.py --repo-root . --profile present --registry control_plane/document_registry.yaml --git-diff "${base_sha}...HEAD" README.md docs tools/validators/docs
python3.12 tools/validators/docs/document-graph/check_document_graph.py --repo-root . --entrypoint README.md --entrypoint docs/README.md --registry control_plane/document_registry.yaml --git-diff "${base_sha}...HEAD" README.md docs tools/validators/docs
python3.12 tools/validators/docs/stale-scan/check_stale_docs.py --repo-root . --as-of 2026-11-11 --profile advisory --review-window-days 365 --placeholder-grace-days 90 --git-diff "${base_sha}...HEAD" README.md docs tools/validators/docs
python3.12 tools/validators/docs/critical-structure/check_critical_structure.py --repo-root . --format text CONTRIBUTING.md
git diff --check
```

Replace the freshness date with the declared review date and record that date
and timezone in the results. Run the relevant existing validator tests when changing their
contract or relying on unfamiliar behavior. The
[workflow definitions](../../.github/workflows/README.md) specify each CI scope.
Root npm scripts and the documentation generator/preview lanes retain their
explicit holds; a green readiness job is not a rendered documentation build.

## Audit the tracked Markdown set

Do not recursively sweep ignored `node_modules`, local runtime state or private
working files. This standard-library command passes tracked Markdown paths,
including names with spaces, directly to the no-network checker:

```python
import json
import subprocess
import sys

paths = [p for p in subprocess.check_output(
    ["git", "ls-files", "-z"], text=True).split("\0")
    if p.lower().endswith((".md", ".markdown"))]
result = subprocess.run([
    sys.executable, "tools/validators/docs/link-check/check_links.py",
    "--repo-root", ".", "--format", "json", *paths,
], capture_output=True, text=True)
report = json.loads(result.stdout)
print({k: v for k, v in report.items() if k != "findings"})
for finding in report.get("findings", []):
    if finding["outcome"] != "EXTERNAL_TARGET_UNVERIFIED":
        print(finding)
raise SystemExit(result.returncode)
```

Local Markdown file/fragment resolution, metadata shape, graph reachability,
freshness signals and factual correctness are different checks. External URLs
are not requested; inline HTML links and other stated parser limitations need
separate review. Preserve and classify baseline findings. Do not create empty
targets, invented dates, substitute document identities or relaxed gates to
turn an unresolved finding into a pass.

## Mirror, wiki and review handoff

Documentation inside `apps/site/source/` changes the selected mirror inventory.
Append a successor receipt, retain every predecessor and review hold, update
the selector and corresponding QA, and run strict current-byte parity plus
mirror tests. A documentation receipt is content accounting, not hosted parity.
The [mirror naming ADR](../adr/ADR-0048-external-mirror-names-are-externally-fixed.md)
and [Site preservation record](../../apps/site/source/docs/SITE_PRESERVATION.md)
continue to apply.

Keep wiki source links compatible with the explicit
[projection helper](../../tools/docs/wiki/README.md). Run its contract tests;
native wiki synchronization is a separate reviewed action. Record the exact PR
head, performed checks, inherited findings, pending acceptance and rollback.
Revert an erroneous guide with its navigation and generated-inventory support
as one unit; never rewrite prior evidence to match the new prose.
