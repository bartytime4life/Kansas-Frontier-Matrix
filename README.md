# Kansas Frontier Matrix branch recovery archive

This archive preserves all 5,315 branch names and their exact commit IDs from
before the October 26, 2026 cleanup. Every commit reachable from those branch
heads is retained through the ancestry of this archive tag.

The default branch, hosted website branch, and open phone-layout fix remain
active. The cleanup does not merge application code or deploy a website.

## Restore one branch

Fetch `refs/tags/archive/branches-before-cleanup-20261026` from the repository.
Look up the original branch name in `branches.json`, under
`original_branch_heads`. Create a branch at that exact commit ID, then push
the restored branch if needed. Do not overwrite a branch that has advanced.

This tag is a recovery index with an archive-only file tree. Do not merge the
archive commit into an application branch. Recover the individual original
commit from the manifest instead. Its code and original history are preserved.

Unmerged work remains unreviewed. Archiving it does not establish correctness,
security, current deployment status, or suitability for release.

A separate full Git bundle and this manifest are also saved in the Codex
workspace under `/workspace/branch-backups/Kansas-Frontier-Matrix-2026-10-26`.
The remote archive tag provides recovery without that workspace.
