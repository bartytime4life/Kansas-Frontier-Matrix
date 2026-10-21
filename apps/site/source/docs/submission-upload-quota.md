# Submission upload quota

Data and land uploads share 20 slots per authenticated owner. A conditional D1
insert reserves a slot before multipart body reads or R2 writes. Recent completed
submissions (all sources and review states, inclusive rolling 24-hour cutoff) and
all unfinished uploads consume capacity. Finalization inserts the submission and
removes its reservation in one D1 batch transaction. Land replay releases its
temporary slot without another object or submission.

Deploy migration `0011_submission_uploads` before the corresponding source. It
adds only a reservation table and index; it does not rewrite existing data or
change DB/R2 bindings. Old workers do not reserve slots, so retire them before
considering the quota enforced. Missing schema fails closed with HTTP 503.

On ordinary validation or storage failure, cleanup deletes any attempted object
before releasing its slot. An ambiguous D1 commit is checked before deletion so
that completed submissions retain their objects. If cleanup or this check fails,
the slot stays charged and logs `KFM_INTAKE_UPLOAD_CLEANUP_PENDING`. A terminated
request may likewise leave a reservation. No timer expires reservations: a slow
or uncertain writer could still persist an object after a timer released its slot.

To recover a stranded slot, an authorized operator must first ensure its original
writer cannot resume (quiesce uploads and retire the relevant worker instances).
Inspect the reservation ID, matching `data_submissions.id`, and R2 key
`quarantine/{owner_key}/{id}` in the existing private stores. Preserve objects for
completed submissions; otherwise confirm deletion of the request's object.
Only then delete that reservation. Do not run a blanket age-based purge.

The limit bounds per-owner concurrent uploads as well as recent submissions. It
does not introduce a new global storage budget or remove historical submissions.
Those are separate policy decisions. Source validation, review, admission,
release state, authentication and the private audience remain unchanged.
