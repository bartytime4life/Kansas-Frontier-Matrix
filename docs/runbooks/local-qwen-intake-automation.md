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
