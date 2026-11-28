# Local Qwen intake automation

`tools.local_data.smart_intake` runs the existing private intake review engine in
resumable batches. It uses a pinned model from loopback Ollama, bounded text
inspection, saved provider metadata, and the native file and catalog writer
guards. It creates descriptions and review receipts without changing originals.

Run it with a trusted runtime configuration beside the existing
`storage-identity.json` and `check-data-mount.py`:

```sh
python3 -m tools.local_data.smart_intake --config /path/to/runtime/smart-intake.json
```

The configuration selects `model`, its exact `model_digest`, `batch_limit`,
`max_batches`, and `max_run_seconds`. An operational deployment should serialize
backups with this worker, bind it to Intake Studio so it stops before a store
move, and make scheduled full catalog analysis yield while a Qwen worker owns
the review lock. The worker resolves the current store from the runtime identity
file at each start. Maintenance and restart pauses preserve completed work.
The deployed Studio and scheduled worker both check backup unit states before
accepting data. Backup services stop the scheduled workers and wait for the
kernel Qwen review lock, allowing any in-flight workspace review to save its
draft and yield before files are copied.

Ordinary new files pass the existing AI acceptance gates. A one-time owner request
can additionally authorize **private reference retention** for an exact selection.
Its content-addressed policy binds item IDs, source SHA256 values, and complete
review contexts. It cannot apply to changed files or later reopened reviews.
Known capture restrictions, corrupt streams, and native blocking issues still
reject acceptance. Model uncertainty and recommendations remain recorded when
the owner authorizes retention of a weak-OCR or unresolved-subject reference.

The optional Studio `--automation-config` argument shares the pinned model and
the same worker policy with the web controls. An admin Pause or Stop remains in
effect across timer runs. Resume uses the same review engine, including the
original owner-bound scope. The configuration is an operator file, not uploaded
source material.

Within the active store, `data/work/intake/smart-catalog/` contains:

- `catalog.sqlite` and `CATALOG.csv`: supplementary metadata indexes.
- `by-domain/`: reference manifests pointing to original native paths.
- `records/`: descriptions, exact evidence, model fingerprints and review receipts.

The native Working Data index remains authoritative. Original files, older AI
results, and immutable receipts are retained. Accepted private references retain
sharing holds; they do not imply source admission, publication rights, factual
certification, or validation of every page or record. Provider titles and OCR
transcriptions are labeled separately from independently established facts.

## Optional metadata preparation

`tools.local_data.prepare_intake` prepares an owner-bound selection in a local runtime cache while drive maintenance blocks acceptance. It opens the current catalog read-only, checks the source digest and context, and writes results to the runtime disk. It does not accept files. The native worker can later reuse exact prepared inputs and responses; source checks and the model pin still run before acceptance, and the original generation time is retained. Cache entries are bound to the item, digest, complete review context, model digest and prompt version. Modified or stale entries are rejected.

## Resolving an existing held selection

Keep an earlier `owner_policy` when its original verification or recovery job
still depends on it. `additional_owner_policies` accepts operator-installed
objects with `sha256` and `source` fields. Every policy is independently checked
against its content hash and the current native review context. Uploaded
documents cannot supply these configuration fields or authorize acceptance.

Set `resolution_policy` to one installed policy's hash to process that exact
selection before ordinary new arrivals. `resolution_priority` may list IDs
already bound by that policy, for example the owner's two Studio uploads.
`batch_limit`, `max_batches` and `max_run_seconds` still bound each invocation;
completed batches survive restarts, backup pauses and timer runs. Items already
attempted under this prompt and policy are not retried indefinitely. Changed
contexts, native blockers, known restrictions and failed archive checks require
a separate resolution. An optional `resolution_status` path writes aggregate
selection, accepted and remaining counts after each batch. Studio displays these
counts alongside the current batch and the admin's Pause/Stop controls.

An optional `recorded_review_cache` supplies an operator-audited SQLite cache
with `path` and a `trusted_prompts` list of exact `version`/`sha256` pairs. Its
`reviews` table contains `id`, `sha`, `context`, `body_sha` and `body`; each JSON
body contains the native held `result` and original `packet`. Before reuse the
worker checks the current source bytes and context, pinned model, trusted
prompt, cache digest and immutable native input/response hashes. It reconstructs
the description from the actual saved Qwen response and compares it with the
recorded review. A forged description, missing receipt or changed source fails
closed. This cache is a local operational artifact and belongs outside Git.

Reuse preserves the original generation time, model, prompt, batch and raw
response credit. A new acceptance batch, owner authorization and acceptance time
are recorded separately. Studio labels the reused generation. Existing held
metadata and receipts remain immutable; a changed acceptance record receives a
hash-qualified filename. An interruption after acceptance resumes metadata
organization without adding a duplicate operator review.

## Bounded PRISM raster archive descriptions

The v6 acceptance prompt distinguishes `.tar.gz` BIL archives from gzip UTF-8
text (`.txt`, `.csv`, `.tsv`, `.json`, `.jsonl`, `.ndjson` and `.geojson` followed
by `.gz`). Other gzip names remain uninspected. The declared capture name selects
the reader, while only the native content-addressed payload is opened.
`raster_archive.py` checks a single complete gzip member, CRC, tar member
types and paths, matching BIL/HDR files, float32 shape, byte order, grid spacing,
nodata and finite stored cell values. It never extracts archive paths to disk.
Bounds are 16 MiB compressed, 64 MiB expanded, 24 members, 16 KiB per metadata
sidecar and eight million cells. Unsupported, malformed or excessive archives
remain held.

Descriptions identify saved provider metadata separately from inspected grid
properties. PRISM variable meanings and units come from the documented code
dictionary; they are not inferred from the magnitude of a pixel. Projection WKT
is retained as declared, and header-derived bounds are not labeled as a WGS84
certification. A valid all-zero precipitation grid remains recorded zeros.
Integrity and shape checks do not establish meteorological correctness, source
admission or public-use rights. An empty gzip text capture is labeled as an
inspection-availability result rather than quoted as source text.

The raster dictionary references the provider's
[dataset documentation](https://prism.oregonstate.edu/documents/PRISM_datasets.pdf)
and [FAQ](https://prism.oregonstate.edu/faq/). All review evidence comes from the
saved local file; no live provider request occurs during acceptance.
