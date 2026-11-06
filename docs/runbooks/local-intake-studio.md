<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-runbooks-local-intake-studio
title: Local photo and PDF intake review
type: runbook
version: v1
status: implementation-candidate
owners: ["@bartytime4life"]
created: 2026-11-06
updated: 2026-11-06
policy_label: public
owning_root: docs/
responsibility: Explain private preparation and governed capture handoff.
truth_posture: CONFIRMED targeted local regressions; NEEDS VERIFICATION camera and browser acceptance; no admission or publication.
[/KFM_META_BLOCK_V2] -->

# Review photos and PDFs on your development PC

**Status:** repository implementation candidate, locally tested on Linux. This
studio prepares private placement proposals. It does not embed content in the
Explorer, admit sources, activate data, or publish the website.

## Start here

From the KFM checkout, run:

```bash
./tools/local_data/intake_studio/start-local.sh
```

Open <http://127.0.0.1:8776/>. The launcher opens the browser and starts an
on-demand process; it does not install a login service. `--no-open` starts without
opening a browser. If an existing studio occupies that port, the launcher reuses
it; that does **not** establish that the running copy matches this checkout.

For a separately testable foreground instance, with a disposable private inbox:

```bash
/usr/bin/python3 tools/local_data/intake_studio/intake_server.py \
  --port 8777 --store "$HOME/.local/share/kfm-intake-studio-trial"
```

Stop a foreground instance with Ctrl+C. For the launcher, inspect the process
recorded in `~/.local/state/kfm-intake-studio/server.pid` before stopping it; a stale
PID must not be treated as authority to stop an unrelated process.

## Add, understand, and propose

1. Choose a PDF or photo, drag files into the inbox, or choose **Take a photo**
   followed by **Start camera**. Camera use is explicit, video-only, and stops on
   close or capture. A phone photo can also be copied to the PC and selected.
2. Inspect the original, preview, extracted text, warnings and matching excerpts.
   Add a description when the photograph contains little text.
3. Record its source, rights, sensitivity, observation date, location and reviewer.
   Choose a proposed domain and destination, such as a reference-library entry,
   map evidence attachment, dataset documentation, timeline or story context.
4. Save **Needs review**, **Keep quarantined**, or **Ready for integration review**.
   Unknown/restricted rights, unknown/nonpublic sensitivity, missing provenance,
   failed extraction, or sensitivity flags prevent a ready decision. Changing
   previously ready inputs reopens review.
5. Export a private ZIP containing the original, extracted text, preview, review
   history and SHA-256 checksums. The proposal explicitly retains the release hold.

A destination is a suggestion, not a working import route. Keyword matching is
not AI verification, geolocation, identification of people, or scene recognition.
The domain inventory follows KFM's **PROPOSED** domain-lane projection, not a new
adopted registry. Inspect the original before relying on OCR numbers or names.

## Dependencies and limits

The server uses Python's standard library. Extraction currently targets Linux
with `/usr/bin/python3` and Pillow, `/usr/bin/bwrap`, `/usr/bin/prlimit`, and
Poppler's `pdfinfo`, `pdftoppm`, and `pdftotext`. English Tesseract and its libraries
must be provisioned in the private runtime layout below:

```text
~/.local/share/kfm-intake-runtime/root/usr/bin/tesseract
~/.local/share/kfm-intake-runtime/root/usr/lib/x86_64-linux-gnu/
~/.local/share/kfm-intake-runtime/root/usr/share/tesseract-ocr/5/tessdata/eng.traineddata
```

`--runtime` selects a different runtime parent containing `root/`. This repository
does not download or install packages. Use maintained, trusted distribution
packages; the private runtime must be refreshed separately from repository code.
The session endpoint reports dependency presence, not a successful sandbox probe.
Run the native tests below to check the complete installed chain. Missing tools,
disabled user namespaces, invalid files or timeouts leave extraction failed and
held; there is no unsandboxed fallback. Windows/macOS setup is unverified.

Supported bytes: PDF, JPEG, PNG, WebP and TIFF, up to **25 MiB per file**. HEIC must
first be converted to JPEG/PNG. PDF text covers at most 30 pages; scanned-PDF OCR
covers at most three pages. Image OCR covers the first frame. Mixed scanned/text
PDFs can omit regions. Text is capped at 250,000 characters. Previews show the
first page/frame and strip metadata; originals retain their bytes and possibly
sensitive EXIF. Extraction has a 100-second wall limit and bounded CPU, memory and
output. It is not a malware safety attestation.

## Storage, privacy, and existing KFM intake

The default private preparation inbox is `~/.local/share/kfm-intake-studio/`.
It contains SQLite review records and content-addressed original/derivative
objects. Identical bytes reuse storage but receive separate source and review
records; rights never transfer merely because hashes match. Browser clearing
does not erase this inbox. Back it up while stopped, or export individual records
while running. No automated deletion, retention budget or disk-space reserve is
implemented; monitor free space before large batches.

The server binds only `127.0.0.1`, enforces exact Host and same-origin requests,
and requires a fresh session token for data APIs. Uploaded documents are never
served as executable HTML/PDF content. Extraction has no network or home access.
The inbox is private preparation storage, **not** `KFM_DATA_ROOT`, a source
registry, canonical EvidenceBundle, release manifest or proof home. Do not put it
inside Git, a public directory, a shared folder or the governed store.

### Handoff to the existing governed workflow

1. Export and inspect the held proposal and verify its `checksums.json`.
2. Select the original into a private source-first downloads folder. Preserve the
   ZIP review history separately; do not treat extracted text as original truth.
3. Follow [Add downloaded maps, pictures, and documents](local-pc-data-store.md#add-downloaded-maps-pictures-and-documents)
   using `manage.py describe`, explicit manifest review, `plan`, `sync`, and
   `verify`. This is a separate owner action; the studio never calls these tools.
4. Use [raw-data intake](raw-data-intake.md) to profile captured material and
   review placement. Existing source-directory **and** digest bindings remain
   required. No digest-only rights inheritance or direct ZIP importer is added.
5. Subsequent WORK staging, evidence linkage, rights/sensitivity checks, review,
   release and public use remain governed transitions. A local pass proves none
   of those transitions. The public Explorer must never fetch this private inbox.

## Placement and migration note

Accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../doctrine/directory-rules.md). Section 10.1 places
repository operator tools under `tools/`; the existing `tools/local_data/`
operator and `intake_service.py` desk are the precedent. This bounded preparation
operator lives at `tools/local_data/intake_studio/`; human guidance belongs under
`docs/runbooks/`, and regressions under `tests/local_data/`. A future independently
deployed application would need its own placement review, not silent promotion
of this operator into a public service.

This imports the local companion's source into the established implementation
root. Existing installed copies under `~/.local/share/kfm-intake-app/` and their
inboxes are **not** overwritten or migrated by checkout changes. The separate
acceptance board remains separate: candidate revision, repository inspection,
automated browser tests, preview checks, merge and public behavior must retain
distinct evidence states. No board snapshots, private uploads or runtime binaries
are committed here. No new schema, policy, registry or proof authority is created.

## Validation and rollback

Standard-library regressions (synthetic extraction; native cases explicitly skip):

```bash
/usr/bin/python3 -m unittest tests.local_data.test_intake_studio -v
```

Installed Linux extraction regressions (actual sandbox, Pillow, PDF and OCR):

```bash
KFM_INTAKE_NATIVE_TESTS=1 /usr/bin/python3 -m unittest tests.local_data.test_intake_studio -v
```

Use `KFM_INTAKE_TEST_RUNTIME` for a nondefault runtime. Tests cover provenance
isolation, stale edits, review holds, persistence, export checksums, content
rejection and HTTP boundaries; native tests add photo OCR, scanned PDFs and
malformed-image handling. They use temporary synthetic files, not user uploads.
Camera hardware, cross-browser acceptance, source admission and public readiness
are separate unverified scopes. Existing acceptance-board tests do not qualify
this repository revision's browser behavior.

### Repository integration check — 2026-11-06

Base: `main@72c7aa14f0c1acfc0509896a3d58be05c6a08cab`.
The targeted intake/profile/review/studio suite completed with **84 passed,
3 skipped, 24 subtests passed**. The three skipped native cases were then covered
by a separate installed-runtime run: **14 studio tests passed** with real local
OCR/PDF extraction. Ten changed documents passed the local-link checker
(311 targets); both new document metadata blocks passed. JavaScript syntax and
Git whitespace checks passed. An initial broader-test command named a nonexistent
service test file and collected nothing; the corrected command used the existing
intake, review, limit, projection-limit and studio modules. No failures were hidden
or tests weakened. Fresh browser/camera acceptance, hosted CI and public behavior
were not established by these checks.

Rollback: stop the candidate instance and return to the prior checked-out or
installed copy. Preserve the private inbox and exported originals. No schema
migration, public deployment, production-data change or DNS rollback is needed.
