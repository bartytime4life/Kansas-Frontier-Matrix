# DrinkingWaterAdvisory fixtures

This fixture family contains synthetic public-water-system identifiers,
authority references, source outcomes, service-area references, and advisory
times only. It contains no real advisory, address, person, health claim,
credential, source locator, restricted payload, or public guidance.

The semantic validator also rejects RFC 3339 `-00:00` unknown-offset markers
for source-check, issue, effective, expiry, and rescission timestamps. Such
values are never treated as exact UTC evidence for derived temporal findings.
The marker is recognized only on a schema-valid aware date-time; a malformed
string that merely ends in `-00:00` cannot satisfy rescission requirements.
Semantic ordering accepts the same RFC 3339 date-time grammar and aware-offset
suffix as the schema, including lowercase `t`, and does not derive ordering
claims from schema-invalid timestamp syntax.
Ordering denials bind to the corrective timestamp field so downstream
consumers do not need to infer which value violated the governed sequence.
An unknown intermediate timestamp suppresses only comparisons that require
it; independently knowable issue, check, expiry, and rescission bounds remain
enforced.
Input validation opens every directory and the final regular file through
no-follow descriptors, then sizes and reads that same final descriptor. Leaf,
ancestor, and cyclic symlinks fail closed, while a rename or symlink swap after
directory admission cannot redirect the fixture-only validator to another
file. The final descriptor is opened nonblocking before its regular-file check,
so a FIFO or other nonregular input cannot stall validation while waiting for
another process. An ordinary file used as a directory component remains a
`FILE_NOT_FOUND` error; only a confirmed symlink receives
`INPUT_SYMLINK_DENIED`. The final descriptor is read with a byte limit as well
as a pre-read size check, so growth after admission cannot bypass the bounded
carrier limit.

The command interface keeps fixture replay distinct from explicit carrier
validation: only exact, single-use `--fixtures` selects replay, it cannot be
combined with input paths, and `-- --fixtures` remains an ordinary literal
filename.

`PASS` proves local profile coherence only. It does not establish a current
advisory, safe drinking water, source admission, evidence closure, policy or
health review, alert authority, release, publication, or public use.
