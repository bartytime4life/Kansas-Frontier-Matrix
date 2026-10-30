# Private historical Kansas road-map reference

The selected **Official Map, Kansas State Roads** bears the Kansas Highway
Commission seal and the printed statement **Approved August 7, 1918**. A visual
check of the full rendered sheet corroborated the archived OCR clue and filename.
This is the map's approval date. It does not date road construction, opening,
condition or surveys. The PDF's 2025 producer timestamp is a different clock.

## Evidence and replay

`tools.local_data.historical_roads` prepares this one qualified document without
network access or an archive scan. It accepts the archive root, a separate
initialized working store, and an explicit SHA-256-pinned qualification record.
The selected paths within the archive are fixed in the helper. Absolute paths
retained in old metadata are provenance only and are never followed.

The helper validates the qualification's date and review limits, the pinned
archived review manifest, its exact record member, and the original PDF bytes.
The manifest and record must retain their pending, unreleased, unpublished,
source-specific rights and infrastructure-context review states.

An installed Poppler `pdftoppm` renders page 1 of a temporary copy of the verified
bytes at a maximum edge of 3,600 pixels. The invocation has a 45-second timeout;
inputs and outputs have 16 MiB limits. It never edits the original PDF. The
renderer version, fixed recipe, dimensions, output size and full PNG hash must
match the previously inspected qualification. Different output requires a new
visual qualification, not silent acceptance. Missing renderer or failed replay
leaves the destination unprepared. Header checks are separate from visual review.

For this archive, Poppler 26.05.0 reproduced the inspected 3,600 x 2,330 image.
The PDF is 1,250,955 bytes with SHA-256
`45bd9bcd1d7ff71e6b74bf544a3c4db84604332d336ecb7691c89038670265b6`.
The PNG is 5,058,949 bytes with SHA-256
`8f23d75a1ec65aa5dd4b6e16241f86b9ff4e22602e1cad8fcb4813e33ef1a12f`.

```sh
python3 -m tools.local_data.historical_roads \
  --source-root /absolute/imported-archive \
  --root /absolute/initialized-working-store \
  --qualification-path /absolute/qualification.json \
  --qualification-sha256 EXACT_QUALIFICATION_SHA256
```

## Private package and installation

Run preparation under the PC's shared operation lock with scheduled writers
paused. The helper also holds the working-store lock. It writes an immutable
directory under `data/work/roads_rail_trade/historical-1918/`, identified by input
and implementation hashes. Repeating the same operation verifies existing files;
changed files or unexpected members are refused. The manifest is written last.

Eight preview members contain the rendered page, original source record and
review manifest, qualification, coverage, retention inventory, validation and
README. The source PDF is preserved separately as `retained/source-map.pdf`,
listed in `retained_sources` and `source-retention.json`. It is included in
working-store backup/restore, but is excluded from the review member allowlist.
The existing reader still refuses raw PDF browser previews. `output_bytes`
describes only the eight preview members; retained source bytes are additional.

Before adding the returned review binding, verify the working backup and restored
copy contain all ten package files, including the retained PDF and manifest,
with matching hashes. Save runtime and binding preimages, install the new helper
and review profile, append the one binding, and restart the private intake desk.
Confirm authenticated PNG/metadata responses, anonymous denial and browser image
decoding. Restore scheduled timers even if a step fails.

The new collection sits alongside the existing private water, climate and geology
references. It adds no raw-intake rows or live feeds. Review metadata preserves
noisy OCR as search clues, with no verified transcription or georeferenced road
geometry. The original acquisition URL, provider checksum and redistribution
permission remain unverified. Source admission, activation, release, publication,
rights and infrastructure-context review remain pending.
