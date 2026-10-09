# Kansas history and archive library

Open **Data & downloads → History & archives**, `/downloads#history`.
The 17 supplied URLs are retained in `public/history/sources.json` with access,
coverage, rights, checked time, source evidence and size findings. Two malformed
combined links were split into four individual URLs. Source guides and GIS
searches are discovery links, not claims that their holdings have been captured.

## Included material and storage

- Prentis, *A history of Kansas* (1909): the original 757,514-byte archival OCR
  is bundled unchanged. `/history/prentis-1909` searches all 4,338 passages and
  renders 16 at a time. Paragraph identifiers are not printed page numbers.
  SHA-256 is verified when loading. The downloadable provenance JSON records
  original and resolved URLs, official SHA1, local SHA-256, and reuse evidence.
- Prentis PDF: 26,261,072 bytes. The exact supplied Internet Archive host/file
  agrees with official item metadata. The provider SHA1 is retained as metadata;
  local capture receipts do not claim provider-checksum verification.
- Anna Estelle Arnold PDF: 24,602,998 bytes. Title/author and 246 PDF pages were
  identified by bounded range reads. The exact edition/year and redistribution
  terms remain unverified. A 2014 scan date is not a publication year.
- The two PDFs total 50,864,070 bytes (48.51 MiB). They are optional private local
  originals, not repository or hosted deployment assets. Unknown collection
  totals remain unknown; no background bulk crawl is introduced.

The reader labels period biases, omissions and OCR errors. It does not turn
historical narrative into governed facts or map layers. Institutional holdings
can include licensed databases, restricted records and item-specific copyrights.
Legends of Kansas is linked, not reproduced or embedded.

## Download behavior and trust boundary

PDF transfers reuse the existing local operator and its Activity/My library
workflow. The user selects a file, sees its size, sets a maximum in MiB, and
starts the transfer. Browser saves directly from provider links are outside KFM
tracking. Both curated URLs are pinned exactly in `HISTORY_FILES`; no wildcard
archive/mirror hostname is permitted. Redirects, HTML masquerading as PDF,
changed lengths, unsafe paths and transfers exceeding the selected maximum are
rejected by existing capture guards. Authentication, Origin/Host controls,
loopback binding, single-transfer concurrency and protected local paths remain.

Catalog refresh/reconciliation adds the two selected book records without
claiming a collection discovery or granting source admission, redistribution,
map display or release. Books are excluded from Maps & geology. Historical
publication dates are not encoded as map dates.

The existing same-Site audience and DB/R2 bindings remain unchanged. This work
starts from owner-private Site v197, source `a35bad43ca68f1eaee6f33176b8d992d05eab326`.
Deployment, GitHub review, local installation and captured-file evidence are
recorded separately in the delivery record.
