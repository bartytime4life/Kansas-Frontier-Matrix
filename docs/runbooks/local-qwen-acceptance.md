<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/local-qwen-acceptance
title: Local Qwen smart acceptance in Working Data
type: runbook
version: v1
status: implemented; local verification
owners: ["@bartytime4life"]
created: 2026-11-08
updated: 2026-11-08
policy_label: public-documentation
owning_root: docs/
responsibility: Explain admin-requested local AI descriptions, batch acceptance, attribution and resumable processing.
truth_posture: CONFIRMED implementation and bounded local tests; AI descriptions remain generated interpretations, not factual source admission.
[/KFM_META_BLOCK_V2] -->

# Review and accept private files with local Qwen

In the combined Intake Studio, open **Working Data** and find **Smart acceptance
with local Qwen**. Enter the requesting admin's name, select up to 100, 500, or
all matching pending files, then click **Review & accept locally**. The existing
domain, format, lane, text and map filters choose the batch. The status filter
must be Any status or Needs review; uncaptured inbox files need capture first.

The button explicitly authorizes AI-assisted private-use decisions for that
saved selection. It does not start during page load. Current human-reviewed
files are not replaced. Suitable high-confidence recommendations become
**Reviewed · local** through the existing digest-bound operator-review code.
Uncertain, sensitive, blocked, unrecognized or context-changed files remain for
admin review. Unknown sharing rights remain unknown. AI cannot choose public
acceptance, clear capture restrictions, admit sources, upload or publish data.

## What Qwen sees and produces

The reviewer receives a bounded evidence packet: profiled format/structure,
extent and time metadata, declared provenance, flags, and a bounded text sample
where supported. Files sent from Studio include the verified saved review and
available OCR. Images/PDFs without extracted content require separate review.
For `.txt.gz` files identified as gzip, a streaming in-memory reader inspects the
first member. It reads at most 256 KiB compressed, expands at most 48 KiB, and
supplies at most 6,000 text characters in numbered evidence blocks. It writes no
unpacked files and does not traverse archives or execute contents. Empty, binary,
corrupt/truncated streams and trailing members/data retain admin holds. Other
archives use metadata only. Archives without an inspected text sample are held, including
when Qwen recommends acceptance with high confidence. Metadata-only descriptions
can contain unsupported filename-based interpretations and need admin checking.
This is not full-content or record-by-record dataset validation.

The extraction record states byte/character limits and actual counts, sample
fingerprint, stop reason, text truncation, first-member completion and CRC scope.
CRC is validated only when the first gzip member's trailer is reached; bounded
prefixes do not validate the unprocessed remainder. Even a fully expanded member
may have only its first 6,000 characters supplied to Qwen. Source bytes remain
digest-checked before and after review. The implementation uses the documented
bounded streaming [Python zlib API](https://docs.python.org/3.14/library/zlib.html#zlib.Decompress.decompress),
without an unbounded decompression or flush call.

Qwen produces a title, description, proposed domain, private-use recommendation,
qualitative confidence, concerns and selected evidence IDs. KFM attaches exact
text from the selected input facts. Outputs must validate before use. Source
text is untrusted data and cannot supply operations, endpoints, paths or rights
changes. Deterministic file/context and sensitivity checks also apply.

Gzip text uses a stricter source-passage mode. Qwen selects numbered title and
passage IDs plus domain/recommendation/confidence and fixed concern codes. KFM
quotes those source passages with whitespace normalized and renders measured
scope/CRC text itself. Free historical interpretation and technical scope prose
are not accepted from the model. Numerical OCR headings are excluded from title
choices; dates and names within quotations remain explicitly unverified source
transcriptions. This prevents invented interpretation while retaining OCR errors
as visible source data; it does not repair a historical scan or certify its claims.

Attribution identifies **Qwen-selected source quotations; KFM-rendered scope**,
retains the original selection JSON, and fingerprints both the complete policy
and actual generation system prompt. The saved input and policy reproduce the
rendered title, source quotations, concern labels and scope exactly. Validation
rejects any change outside those deterministic renderings.

Generated descriptions appear in the file list and **Local Qwen review** in
the details drawer. They are AI-generated interpretations; confidence is the
model's self-assessment, not a calibrated probability or evidence certification.
Admins can inspect the evidence or make a separate human review decision.

## Attribution and persistence

Each completed AI review credits the actual local model and requesting admin
separately. Receipts include the pinned model digest, prompt version and hash,
generation settings, input and response fingerprints, batch, inspection scope,
and time. Exact bounded inputs and raw validated model JSON remain in private
`data/work/intake/ai-context/` and `ai-responses/`; receipts are under
`data/receipts/intake/ITEM_ID/`. AI review history retains previous results.

The existing private intake SQLite database stores jobs, tasks and cached
results. Existing auxiliary SQLite backups therefore include these tables;
normal file backups include the context/response artifacts and receipts. No
new database, public data binding or upload destination is required.

Large selections are snapshotted and paged beyond the 500-item browsing limit.
One worker processes one file at a time, with short catalog-writer locks only
for final decisions. Model inference does not hold the feed pipeline lock.
Unchanged completed AI holds are skipped unless **Re-review previous AI holds**
is checked. Changed files or profile/review context invalidate saved decisions.

**Pause after current file** preserves the queue. **Resume batch** continues it
after returning to the page or recovering from a process interruption. **Stop
batch** retains completed work and leaves remaining files unchanged. Closing
the browser does not stop a running server-side batch. A model outage pauses
the batch; model/prompt changes require verifying configuration and starting a
new batch. Valid drafts survive a busy catalog writer without another model call.

For a completed batch whose files are still pending, **Re-review same pending
files** uses the original saved IDs and order, independent of current filters and
new arrivals. It refuses the rerun if an original file changed or was already
accepted/reviewed. The private start request records the optional `sourceBatch`
identifier, alongside `filters: {}`, `retryHeld: true` and the original count.
When a completed batch has acceptances and holds, **Re-review N held files** uses
`sourceState: "held"` and the saved held count. The prior acceptances are excluded;
new arrivals do not alter the selection. A changed or human-reviewed original is
still refused rather than silently overwritten.
Prompt/extraction revisions invalidate older cached reviews; old results remain
in AI history. Changing the prompt does not silently resume an old paused batch.

## Local model configuration

The operator configures the combined server with an installed Qwen model and
its complete digest, alongside its existing private-store settings:

```bash
/usr/bin/python3 tools/local_data/intake_studio/intake_server.py \
  --store /private/KFM-intake-studio --kfm-root "$KFM_DATA_ROOT" \
  --qwen-model qwen3.5:4b --qwen-digest "$KFM_QWEN_DIGEST"
```

Requests use only literal `http://127.0.0.1:11434`, disable environment proxies,
reject redirects, and verify the installed model digest. There is no cloud
fallback or model download. The existing Ollama service must be running. The
model uses structured outputs with thinking disabled and temperature zero;
see the primary [Ollama API documentation](https://github.com/ollama/ollama/blob/main/docs/api.md).
No hosted inference profile, website relay or model weights are changed.

The capability and exact same-origin checks are inherited from the private
workspace; the requested-by name is audit attribution, not a separate login
system. Library remains immutable and refuses AI batch operations.

## Verification and rollback

`tests/local_data/test_ai_acceptance.py` checks guarded acceptance, attribution,
context changes, recovery, pause/resume, evidence, and selection beyond one
500-file page. Workspace tests cover the private HTTP boundary and Library
refusal. Real-model trials should use isolated synthetic stores first and
inspect both accepted and held outcomes; a finite trial does not qualify all
future sources or descriptions.

Rollback returns the service to its retained prior release. Completed local
decisions and their receipts are retained; rollback does not erase or silently
undo admin-requested review history.
