# Mobile topic builder

Candidate implementation, 2026-11-03. This source change has not been published.

## Review findings

The Product Design audit used the existing KFM site and its 390 × 844 phone
layout. The core journey is choosing subjects, seeing their relevant layers on
one map, and revising that choice without starting over.

| Finding | Impact | Change |
| --- | --- | --- |
| Introductory controls put the first card near the bottom of a phone screen | High: the primary action is difficult to discover | Compact heading, optional place search and a searchable topic grid |
| Selecting a card immediately leaves the chooser | High: users cannot combine interests | Toggle cards, selection chips and one explicit Open my map action |
| Map entry opens a full-screen Layers panel | High: the promised map is concealed | Show the map first; expose selected layers through a compact Layers button |
| Optional preview and map entry share unclear navigation | Medium: users lose their place or expect a preview to activate data | Separate Preview & details action; Return restores the opening card and scroll |
| Retired renderers and styles remain beside the active flow | Medium: future changes can revive obsolete paths | Remove unused renderers and their exclusive styles/tests; retain current source records |

## Interaction contract

- Every canonical topic remains selectable. Search and group filters only change
  the visible cards; they never discard selections.
- Selecting a card toggles it without navigating. Preview & details is a separate
  action with a 44 px minimum target. Pressed state, text and a check mark identify
  selection without relying on color.
- A persistent tray offers the selected count, removal chips, Clear all and
  Open my map. Very short screens use a compact tray; cards still toggle choices.
  *Retired 2026-11-06:* the owner asked for the tray to go on every layout so
  the map keeps the screen. The toolbar's Open my map now carries the count
  (on phones it stands in for Explore freely while topics are ticked) and cards
  remove topics; see [Capability welcome](living-welcome.md), Desktop atlas.
  Empty selections cannot open a preset. The provider-credit strip stays clear.
- Combined maps use the union of the selected topics' canonical starter layers,
  overlays and tools. Duplicate sources activate once. The first selected topic
  supplies the initial view; Map style lets the user change that choice.
- Opening applies one setup transaction, clears the preceding setup's layer
  ownership and closes panels that would hide the map. Water + Weather enables
  river observations, radar and alerts. Removing Weather and applying again
  removes its radar and alert starters.
- Edit topics restores the applied choices. Selection changes take effect when
  the user opens the map again. Explore freely keeps the current working map.
- Preview map entry includes any topics already selected. Previewing alone never
  changes the working map's layers.
- Shared map links carry the topic choices alongside the existing explicit layer
  state. Existing single-topic links retain their compatibility behavior.

Source clocks, unavailable states, attribution and dataset limitations remain
visible. Reference context does not imply new observations or admitted data.
No provider credentials, databases, admission rules or hosting settings change.

## Cleanup and ownership

The active path remains `LivingWelcome` → `DomainStage` / `map-engine` for
previews and `combineCategoryMaps` → the Explorer's setup handler for map entry.
There is no additional page, router or second map implementation.

Removed unused `MapDemoPanel`, `MotionAtlas`, `MotionClip`, `ScenePreview` and
`sceneDirector` modules, obsolete player-specific tests and exclusive style
selectors. Current `CapabilityPreview`, canonical catalogs and media provenance
manifests remain: they still support recorded tours and source information.

Presentation lives in `app/`, regressions in `tests/` and this record in `docs/`,
following the existing composition's ownership boundaries. Earlier unpublished
scientific-preview work is retained. Recovery backups stay outside this tree.

## Validation boundaries

Focused tests cover selection, filtering, clearing, primary-style choice,
preview return, duplicate activation protection, all canonical topic unions,
the actual setup handler's combined layers and removal of deselected layers.
The existing browser regression definitions are updated for explicit map entry.
Manual browser checks use the development app and real provider availability;
they do not qualify every source or substitute for physical-device testing.

Production publication and final hosted acceptance are separate operations.
Rollback is a source revert; no stored data or preference migration is required.

Local results for this candidate:

- 144 focused/adjacent Node tests passed; TypeScript and the production build
  passed. Targeted ESLint reported no errors and 41 warnings.
- Browser checks covered 320 × 568, 390 × 844, 640 × 360 and 1280 × 900 layouts,
  search with no matches, group filtering, preview/return, combined map entry,
  editing choices and removing Weather from the Water + Weather map.
- The combined map selected three sources; removing Weather left one. River
  observations and alert areas were displayed. Radar rendered, then reported a
  provider failure while retaining imagery; source status remained explicit.
- The full standalone browser suite was not executed in this session. Its
  updated definitions passed a syntax check and still require CI execution.
