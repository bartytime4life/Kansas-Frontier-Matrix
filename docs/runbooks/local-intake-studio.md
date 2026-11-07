<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-runbooks-local-intake-studio
title: Local photo and PDF intake review
type: runbook
version: v1.1
status: implementation-candidate
owners: ["@bartytime4life"]
created: 2026-11-06
updated: 2026-11-07
policy_label: public
owning_root: docs/
responsibility: Explain private preparation and governed capture handoff.
truth_posture: CONFIRMED targeted local regressions and synthetic Chromium review flow; NEEDS VERIFICATION native extraction on this revision, camera and owner-PC acceptance; no admission or publication.
[/KFM_META_BLOCK_V2] -->

# Review photos and PDFs on your development PC

**Status:** repository implementation candidate, locally tested on Linux. This
studio prepares private placement proposals. It does not embed content in the
Explorer, admit sources, activate data, or publish the website.
An explicitly configured **Send to KFM** action captures reviewed originals and
review snapshots into the private Working Data store and indexes them there.

## Start here

From the KFM checkout, run:

```bash
./tools/local_data/intake_studio/start-local.sh
```

Open <http://127.0.0.1:8776/>. The launcher opens the browser and starts an
on-demand process; it does not install a login service. `--no-open` starts without
opening a browser. The launcher reuses an existing studio only when its code
fingerprint matches this copy. An older copy, a missing fingerprint or a mismatch
stops startup with an explanation; it preserves the existing process, PID record
and inbox. Close the inspected older instance before replacing it, or use the
separate-port trial below. The desktop sidebar shows a short local version;
`/api/session` reports the full `sourceFingerprint`. This identifies bundled
server, worker, launcher and client bytes, not OCR dependencies, approval or
public readiness. A running server retains its startup fingerprint.

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
5. Choose **Send to KFM** to capture a saved ready review into Working Data.
   Optional ZIP exports still include the original, extracted text, preview,
   review history and SHA-256 checksums.

A proposed product destination remains a suggestion after private capture. Keyword matching is
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

1. Complete source, rights, sensitivity, reviewer, domain and destination fields.
   Save **Ready for integration review**. Unsaved edits, missing context, failed
   extraction and sensitivity holds prevent sending.
2. Click **Send to KFM**. The server checks the saved revision and original hash,
   captures the original using `manage.sync_store`, verifies the capture, and
   profiles/indexes just that file using the existing intake primitives. Other
   catalog entries remain intact. The preparation record stays in Studio.
3. The original becomes a source-bound quarantine object. The exact review,
   history, extracted text, optional preview, manifest and receipt are preserved
   under `data/work/intake-studio/RECORD_ID/REVIEW_SHA256/`. Sharing rights remain
   unknown in the capture declaration; the Studio rights assertion stays in the
   review snapshot. Sending does not approve redistribution or publication.
4. Open **Working Data** from the success message. Repeated clicks and retries
   after interrupted capture/index/save reuse the same saved-revision capture.
   Different uploads retain separate source provenance. Editing a sent review
   reopens review; a later approved send creates a separate immutable snapshot.

Operators enable the action with an explicit initialized private store:

```bash
/usr/bin/python3 tools/local_data/intake_studio/intake_server.py \
  --store "$HOME/.local/share/kfm-intake-studio" \
  --kfm-root "$KFM_DATA_ROOT" \
  --pipeline-lock /private/pipeline.lock \
  --store-check /private/check-data-mount.py \
  --working-connection /private/working-data.json
```

The lock, trusted Python volume-check script, and private connection JSON are
operator configuration, never browser inputs. The connection JSON comes from
`intake_service.py --connection-file` and supplies a loopback capability link.
Configure the same pipeline lock used by feeds and scheduled analysis. With no
`--kfm-root`, the button explains that Working Data is not connected; uploads,
reviews and ZIP exports remain available.

Exporting a ZIP remains an optional manual handoff. The existing
[local capture procedure](local-pc-data-store.md#add-downloaded-maps-pictures-and-documents)
still works for other files. Subsequent WORK staging, evidence linkage, release
and public use remain separate governed transitions. The public Explorer must
never fetch this private inbox.

## Integrity and recovery

Original downloads, duplicate reuse and ZIP export verify both recorded size and
SHA-256 against the same bounded bytes being returned. A missing, replaced,
symlinked or damaged original is refused. A repeated upload never silently repairs
or relabels a damaged object, and no new duplicate record is created on failure.
Preserve the inbox for recovery and use a separately verified backup or original;
checksums detect changed bytes but do not prove that content is safe or correct.
The extraction sandbox mounts its original input read-only.

## Next improvements — proposed

- Add an explicit, versioned retry for failed extraction after dependencies are
  repaired. Reuploading currently reuses stored analysis, including failures.
- Fetch lightweight, paged inbox summaries. The current list sends every record,
  including text and history; large libraries need bounded loading.
- Prepare a reviewed capture manifest from a selected proposal, using the
  existing local-data tools and explicit owner action. Domain/surface choices
  still describe proposals; map attachment and public embedding are not wired.

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

### Recorded sensitivity holds

Sensitivity flags accumulate across saved description edits and review decisions.
Replacing sensitive text, selecting **Public**, or switching between **Needs
review** and **Keep quarantined** does not clear an earlier flag. Previously
flagged records cannot become **Ready for integration review** here. Clearance
requires separately authorized governed review outside this desk; no clearance
field, endpoint, or local override is provided. Export a held package for that
review and retain its private history.

On reopening an older inbox, flags erased by the original description-edit bug
are recovered from saved `review` and `previousReview` history snapshots. Current
descriptions and recorded flag snapshots also retain restrictions. List, detail
and export use the same conservative read projection: a legacy ready label with
a recovered flag is shown as **Needs review**. Reading or exporting does not
rewrite SQLite rows, prior history, original bytes or extraction objects. The
next explicit review save persists the retained hold, appends a `sensitivityFlags`
snapshot, and records the actual stored previous review. No schema migration or
automatic inbox rewrite is needed. Recovery cannot reconstruct history that was
never saved or was removed outside this application; a clean flag list is not
sensitivity clearance.

Standard-library regressions (synthetic extraction; native cases explicitly skip):

```bash
/usr/bin/python3 -m unittest tests.local_data.test_intake_studio -v
```

Sensitivity recovery and HTTP-security regressions:

```bash
python -m unittest tests.local_data.test_intake_studio_sensitivity \
  tests.local_data.test_intake_studio_security -v
```

The strict `make local-data-check` target keeps its Python no-network guard.
Socket-free header serialization tests run there; the two loopback HTTP tests
skip explicitly and must also be run separately using the commands above. No
guard exceptions or application authentication changes are introduced.

Opt-in browser acceptance, with Playwright and Chromium separately provisioned:

```bash
KFM_INTAKE_BROWSER_TESTS=1 python -m unittest \
  tests.local_data.test_intake_studio_browser -v
```

`KFM_INTAKE_TEST_CHROMIUM` may select an installed browser executable. An explicit
browser run fails if its dependency or browser is unavailable. It uses temporary
synthetic uploads and synthetic extraction, checks desktop and narrow viewports,
repeated edits, discarded unsaved changes, reload, a restarted server and inbox,
readiness denial, and downloaded-package hashes. It does not activate a camera
or qualify real OCR, a phone browser, or an installed copy on the owner's PC.

Installed Linux extraction regressions (actual sandbox, Pillow, PDF and OCR):

```bash
KFM_INTAKE_NATIVE_TESTS=1 /usr/bin/python3 -m unittest tests.local_data.test_intake_studio -v
```

Capture/index handoff regressions, including retry and provenance isolation:

```bash
/usr/bin/python3 -m unittest tests.local_data.test_intake_studio_handoff -v
```

Use `KFM_INTAKE_TEST_RUNTIME` for a nondefault runtime. Tests cover provenance
isolation, stale edits, review holds, persistence, export checksums, content
rejection and HTTP boundaries; native tests add photo OCR, scanned PDFs and
malformed-image handling. They use temporary synthetic files, not user uploads.
Camera hardware, cross-browser acceptance, source admission and public readiness
are separate unverified scopes. Existing acceptance-board tests do not qualify
this repository revision's browser behavior.

### Integrity and startup review — 2026-11-06

Base: `main@284ca2f93dba25f310264a1549f86de4febe550a`. A synthetic damaged
original was downloadable with HTTP 200 before correction, and a duplicate
upload reused it. Both now return an integrity error; healthy bytes remain exact.
The new integrity suite covers HTTP download/duplicate/export denial, original
identity and startup refusal for old copies without spawning replacements.

Validation in this review: **852 passed, 11 skipped, 590 subtests passed** in the
strict offline local-data target; separately **31 studio tests ran, 3 native
cases skipped**, and all **14 native OCR/PDF tests passed** with the installed
Linux runtime. The in-app browser saved a ready review in a disposable inbox,
downloaded the original with a matching SHA-256, and displayed the interface at
390×844. Camera and other browsers were not exercised. The existing installed
port-8776 studio remains an older copy; checkout changes do not update it.
Earlier PR #5746's failed offline check was followed by merged corrections;
PR #5758's local-data check passed. None of these results establish public use.

### Header-warning investigation — 2026-11-06

Inspection is pinned to `main@205e344ea8d05077414d3a0f8606512b66272be5`
and the PR #5746 draft and final heads. The initial draft responder at
`be3ae9c1ee5cc626833ad12d76a0a59c14859b74` lacked generic header sanitization;
the final head `ee0de9ddf290c2f3b8127f35d1ab256c8a48ef12` already includes it.

| CodeQL warning | Sink and current source path | Evidence and disposition |
|---|---|---|
| [650](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/code-scanning/650) | `Content-Type`; literal API types or MIME lookup on four allowlisted static asset paths | Current responder removes CR, LF and NUL. Five hostile delimiter inputs produce one HTTP response, one content-type line, no injected header and an intact body. No exploitable current route demonstrated. |
| [651](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/code-scanning/651) | Earlier `Content-Disposition` sink in the draft | The review thread is outdated. Production download names are generated from a regex-validated 32-hex ID plus a fixed suffix or signature-selected extension; uploaded filenames are not header inputs. The final head additionally sanitizes control characters and quotes. No exploitable current route demonstrated. |
| [652](https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/code-scanning/652) | Sanitized `Content-Disposition` sink in the final head | Serialized-header tests cover CR/LF response boundaries, every C0 filename control, DEL and quotes. Live loopback tests upload a hostile filename and confirm fixed original/export headers, CSP, no-store, nosniff and Host/Origin/token/fetch-site rejection. No exploitable current route demonstrated. |

These bounded source and negative-test findings do not establish that every
historical version or future caller is safe. The response handler, sanitizers,
CodeQL queries, alert settings and security headers are unchanged by this
correction; no warning is suppressed or dismissed. Hosted CodeQL at the PR head
and accountable sensitivity/security review remain separate evidence gates.

### Sensitivity correction validation — 2026-11-06

The original regression tests fail against the pinned main behavior (13 failed
assertions/subtests across the initial seven test methods). The corrected tests
also cover saved legacy ready labels, read-only recovery, audit-snapshot recovery,
interrupted persistence, stale-session retry, unknown clearance fields, unchanged
history/provenance/originals, and checksummed exports.

Targeted intake/review/limits/studio/security checks: **95 passed, 3 skipped,
48 subtests passed**. The complete strict local-data target: **844 passed,
13 skipped, 588 subtests passed**. Skips include optional native/runtime cases,
the opt-in browser flow and the two separately executed loopback HTTP tests.
Chromium Headless Shell 141.0.7390.37 with Playwright 1.56.0 passed the browser
flow at 1365×1000 and 390×844; no page-script errors or external page requests
were observed.

The installed Chromium launcher initially failed on a denied Unix socket; the
headless-shell fallback ran successfully. Native OCR/PDF acceptance was attempted
and failed because this command sandbox denies the `NETLINK_ROUTE` socket needed
by bubblewrap's network isolation. No sandbox protection was relaxed. Native
extraction, camera hardware, broader browser coverage, and the replacement
development PC's recovery and installation state remain unverified. No owner-PC
installation, operational-dataset change, source admission or publication occurred.

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
