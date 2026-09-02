# Synthetic SMAP L4 anti-collapse fixtures

This directory contains a closed, fixture-only profile for testing one narrow
boundary: a modeled SMAP L4 grid candidate must not be presented as a raw
observation, station reading, field fact, silently merged in-situ product, or
released artifact.

The vocabulary is profile-local and noncanonical. These files do not activate
NASA access, assert a production product identifier or resolution, define a
schema or policy, admit a source, or authorize publication.

Inventory is closed:

- `valid/` contains one surface NRT candidate and one root-zone standard-quality
  candidate.
- `invalid/` contains eight single-purpose denials. Every JSON file has a
  same-stem `.expected_error.txt` sidecar containing sorted
  `CODE<TAB>JSON_PATH` findings.

Every fixture binds the frozen profile identifier
`kfm-smap-l4-anti-collapse-fixture-v1` with the SHA-256 of that exact UTF-8
string:

```text
sha256:d0545d945f8f425bbce408002273b71725da27595e6a89831ab5cab7ebf82cd9
```

The validator rejects alternate, malformed, placeholder, or zero digests.

Run from the repository root:

```bash
python tests/domains/soil/test_smap_l4_anti_collapse.py --verbose
```

The validator is offline and non-publishing. It only emits deterministic
PASS/FAIL JSON lines without echoing candidate values.
