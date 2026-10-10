# Kansas people and history research index

Open **Data & downloads → History & archives → People, events & historical context**,
or `/history/people-events`. This source-discovery page links 15 supplied pages to
KFM's reviewed-knowledge search without admitting their claims or resolving identities.

The selected scope is all observable records on the supplied pages, with linked
pages read only when needed to verify Kansas connections or conflicting dates.
It includes complete observed indexes and compact factual metadata from narrative
articles. It does not claim to reproduce every sentence or acquire off-page collections.

## Inventory

| Source | Records | Coverage |
|---|---:|---|
| National FFA Organization | 84 | 81 timeline entries and three archive links |
| KSNT | 0 | Access blocked |
| Kansas Reflector | 45 | Article people, events, topics and reference metadata |
| HISTORY | 73 | Article facts, events and links |
| OnThisDay | 0 | Access blocked |
| kansashistory.us | 0 | Access blocked |
| Kansas Oral History Project | 14 | 13 interview cards and one related interview |
| Wikipedia | 641 | All observed main-list bullets, including 24 fictional entries |
| Find a Grave | 0 | Access blocked |
| EBSCO | 74 | Historical facts, statistics and reference metadata |
| Historic American Indians in Kansas | 94 | Homepage topics, people, events and links |
| Ranker | 6 | Six seed entries; publisher declares 583; off-page results not acquired |
| Kansas Tourism | 80 | 75 people and five related article/index links |
| Kansas Historical Society | 37 | 25 notable people, 11 selection-panel members and one event index |
| Legends of Kansas | 300 | 296 alphabetical entries and four related indexes |

There are **1,448 source entries**, not 1,448 unique people or independently verified
facts. Repeat names remain separate assertions. Search covers names, places, dates,
source metadata and themes; filters and 30-entry pages keep the display bounded.
All 15 source cards remain visible, including the four blocked sources.

## Evidence and reuse

`public/history/people-events.json` retains exact supplied URLs, fetch times,
resolved destinations, source counts, methods, available body hashes, locators,
completeness and individual flags. Hashes for failed HTTP responses identify error
bodies, not acquired articles. Web-reader hashes identify extracted text, not original
HTML. Wikipedia and Kansas Tourism were readable through the normal web reader
while direct HTTP returned 403; their cached-copy limits are explicit.

Wikipedia revision **1361123532** is credited under CC BY-SA 4.0. Its index retains
names, source categories, biographical year labels and coarse place mentions; prose
descriptions are omitted. Other sources retain factual/index metadata and publisher
links, not article prose, transcripts, photographs, audio or video. The Kansas Oral
History footer's CC BY-NC-ND link is recorded without treating it as permission to
adapt interviews. Original copyright and item-specific permissions still apply.

The downloadable JSON preserves more provenance than the compact CSV. Regenerate
the CSV with `node scripts/export-history-research.mjs`; the exporter escapes CSV
syntax and prefixes formula-like fields so spreadsheet programs treat them as text.

## Curation distinctions

- FFA's Jan 09/Jan 10 interface labels are not event dates. Timeline records use
  year precision. Early Kansas City, Missouri events remain regional context.
- The Reflector's Little Bighorn date, HISTORY's Westport location context,
  Abilene founding date and Brown ruling/remedy chronology retain original
  assertions alongside separate NPS/local institutional correction evidence.
- Ranker's Mira Sorvino entry does not establish a Kansas connection.
- Fictional entries remain explicitly fictional; their fictional dates and places
  are not projected into historical geography.
- Interview dates are interview metadata. Biographical year labels do not establish
  current living/deceased status. Kansas Historical Society selection-panel members
  are distinct from the 25 selected notable people.
- Indigenous-history sources retain their publisher perspectives. Mention does not
  establish cultural affiliation, tribal authority, consent, territory or sacred sites.

## KFM linkage and lifecycle

“Search reviewed KFM” opens `/knowledge?term=` with the entry title. Existing
knowledge-release checks remain authoritative; the destination may have no matching
released record. This search is not an identity or spatial join. No source assertions
are inserted into the governed knowledge store, map layers, local acquisition operator,
AI context, source registry or synthetic historical-resolution fixtures.

People/interview indexes provide research context for People/DNA/Land; FFA for
agriculture and education; place mentions for settlement history; Indigenous-history
sources for cultural context. Actual identity, event and place joins need separate
authority evidence, rights/sensitivity review and applicable release decisions.

The catalogue loads only from this Site with a 3 MiB limit, schema/reference/count
checks and HTTP(S)-only navigation. External pages are never fetched by a new server
proxy or embedded as HTML. The existing audience and DB/BUCKET bindings stay intact.
The data remains `NOT_ADMITTED`, review `PENDING`, map activation `NONE`.

Rollback reverts these additive source-reference files and navigation link. There is
no database, stored-user-data or local-download migration to reverse.
