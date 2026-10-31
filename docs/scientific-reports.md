# Scientific reports

Reports are free device-local drafts with a visual preview and self-contained
HTML download. The same rendered content drives the map report preview,
standalone download, and map-report print view. Markdown and JSON exports remain
available under **Edit report**. Opening or downloading a report does not publish
it or change source admission.

## Choose a report

| Report | Starting point | What it can show |
| --- | --- | --- |
| Scientific overview | Explorer → Reports | Saved map locator, narrative, eligible evidence composition, source details, limitations |
| Place brief | Report layout → Place brief | The same captured map plus a place dossier, when captured: nearby records, source times, distances and coverage |
| Source comparison | Report layout → Source comparison | Included source references and their scope, periods, support and limitations, followed by the complete report |
| People and events | Reports → People & events reports | A filtered catalog page (up to 30 entries) or one entry, with source composition, chronology and original source assertions |

**Reports** resumes the saved report draft. To create a fresh map report, restore
a saved place if desired, then use **Compose → Create evidence report** from the
map. The report states its capture time. Restoring a place does not rewrite an
existing report. Captured fire and underground context remain available when
present; underground reports embed the recorded-depth diagram and retain its
source gaps. Interval CSV and section SVG downloads remain in the editor.

Use **Edit report** to write the title, question and narrative or change included
evidence, then **Dashboard** to preview. Changing the layout does not rewrite the
draft or invent additional observations. The visual layout selection lasts for
the current workspace session; the draft content uses the existing local save.

On the people-and-events page, filter by name, topic, source or entry kind, then
choose **Build report for this page** or **Build entry report**. Reports explicitly
state the chosen page, filters and count. Back to entries preserves those filters
and page. The preview freezes that selection; download it before leaving to keep
it. Repeated names stay separate source assertions rather than silently merging
identities.

## Visual and data boundaries

- The map is an offline Kansas locator using the bundled 2017 Census cartographic
  boundary. Its marker is the saved camera center. It does not replay provider
  overlays, terrain, selected geometry or observations. Withheld camera locations
  get no marker; out-of-state centers are not plotted on the Kansas locator.
- Bar charts count captured inputs from a zero baseline. They are not quality
  scores, environmental measurements, unique-person counts or verified facts.
  Empty evidence is explained, not filled with demonstration observations.
- Historical chronology accepts four-digit years and valid `YYYY-MM-DD` dates.
  Year-only entries precede precise dates within that year without inventing a
  month or day. Original date meaning and source notes are retained. Other date
  statements, ranges and missing dates remain separate in catalog order.
- Captured source periods and retrieval dates remain distinct from map time.
  Draft status, policy posture, provenance, coverage and uncertainty travel with
  the exported report. No source is admitted or released by report generation.
- Downloaded HTML includes its styles and SVG visuals, has no scripts or remote
  image/font dependencies, and blocks automatic network loads via its CSP.
  Source links remain available for deliberate navigation. Provider and author
  text is escaped; only credential-free HTTP(S) citation links are emitted.

Open **Download visual HTML** in a browser to view it offline or use the browser's
Print / Save as PDF. Browser print formatting and physical printers vary; this
feature does not provide a separate server-generated PDF.
