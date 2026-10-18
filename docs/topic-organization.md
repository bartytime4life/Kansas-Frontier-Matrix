# Subject organization

## Purpose-based map starters

The layer browser now includes **Start with a purpose**, a native selector with
six small public-context stacks: Land & water, Field science, Learning Kansas,
Historical landscape, Infrastructure and Community planning. Choosing a name
previews its description, source status, source dates and limits; **Use starter**
applies its three or four configured sources. This is independent of visual
Appearance presets and topic/search filters. Categories describe tasks rather
than infer the visitor's profession.

Starters reference only the existing `OFFICIAL_CONTEXT_SOURCES` public allowlist.
Source availability is not inferred from atlas seed cards or repository maturity.
Unknown identities, non-context roles, missing eligibility, failed sources and
time/Globe holds are skipped and disclosed. If none can be selected, the action
is disabled and existing choices remain. Idle means available to request, not a
verified live response. Sources below their display zoom may be selected with
zoom guidance; presets do not move the camera to force visibility. Failed
sources retain the existing individual retry workflow.

Applying a starter replaces only public context selections. Reviewed packages,
imagery, registry layers, dates, opacity, map camera, timeline, projection and
release state keep their existing owners. Individual switches remain editable;
the control reports when the context stack differs from the previewed starter.
**Clear context layers** resets that public stack to empty without resetting the
map. Unchanged selections receive no owner calls, retaining in-flight requests
and cached payloads. Removed sources use the existing cancellation/hide path.
Presets add no fetch endpoint, background poller, account or publication action.

**Remember my context layers on this device** is off by default. With opt-in,
the bounded `kfm.public-context-selection.v1` localStorage record stores only
`{ version: 1, ids: [...] }` for public context identities. No camera, area,
source records, profession, personal details, source dates or credentials enter
this record. Existing Places/history storage remains separate. Explicit `ctx`
in a shared link or tab history, including an empty stack, takes precedence over
the saved preference. Otherwise saved IDs are intersected with the current
allowlist; existing runtime time, projection and source gates still apply.
Writing waits for URL restoration. Custom switches and the empty reset are saved
while enabled. Uncheck to delete this preference; blocked storage leaves session
controls usable and reports failure. This option does not add the preference
record to an upload, telemetry event, report or export; existing map sharing may
still include the selected public layer IDs.

`app/map-starters.ts` owns UI recipes and bounded preference helpers;
`app/map-starters-control.tsx` owns accessible native controls and opt-in storage;
`app/page.tsx` revalidates application at the existing context owner. The same
control is inside the existing scrolling layer panel on desktop and mobile.
Named labels, source text, a polite live status, visible focus and 44 px control
targets support keyboard and touch interaction without a new modal or toolbar.

The existing `apps/site/source/{app,tests,docs}` projection is retained under the
deployable `apps/` responsibility root, per Directory Rules PDF, accepted
ADR-0029 and `docs/doctrine/directory-rules.md` (DIR-ROOT-001, root responsibility
table and DIR-EXEC-001). No parallel catalog, policy, schema or source home is
created. Tests stay with the established Site test owner. Rollback reverts the
bounded UI/helpers/tests and this documentation; the optional preference key can
be removed through its checkbox or browser site-data controls. No DB migration,
native Site save, deployment, audience change or data promotion is included.
Repository validation does not prove hosted behavior or human acceptance.

`tests/map-starters.test.mjs` exercises real allowlist membership, source
restrictions, actual page selection/eligibility callbacks, no-op reselection,
customization/reset, link precedence, persistence bounds/storage failures, and
the control's executable label/status and selection interactions. Browser,
device WebGL and provider availability checks are separate evidence.

## Existing subject navigation

The Explorer organizes map layers, investigations, functions and repository
feature families into 17 subjects in four groups. Engineering, science,
weather, history, land ownership/purpose and people are explicit subjects;
water, groundwater, geology, terrain, ecology, agriculture, transportation,
hazards, places, sky and evidence tools provide related context.

`app/layer-workspaces.ts` owns this application navigation projection. It defines
stable topic IDs, groups, subtopics, coverage limits and links to existing tools.
Provider source identity determines layer membership. A source may appear in
several subjects while retaining one renderer, selection and source record.
Weather and hazards now have distinct filters; the prior `disaster`, `land`,
`transport`, `water`, `terrain`, `places`, `groundwater` and `all` IDs remain valid.

The `/topics` index lists configured provider context, imagery catalogue entries
and pinned repository feature families by subject. These counts do not prove
provider availability, imagery installation, source admission or release.
Map layers, the starting-investigation library and repository function/feature
views use the same grouped selector. Existing area and maturity filters still
apply independently. Topic titles are searchable. `?topic=<id>` opens the map
layer browser; `&layerView=imagery` opens its imagery tab. Unknown topic IDs
fall back to all subjects. Tab history retains topic and layer-tab navigation.

Layer filtering never writes visibility, opacity, source time, ordering,
playback, saved-workspace records or admission state. Existing specialist
controls remain mounted under their original persistent wrappers. Tool buttons
inside a topic guide invoke the existing map-tool owner without replacing the
map’s selections. No new source fetch, data store or lifecycle transition is
introduced.

Land ownership is an organizational subject with an explicit coverage gap:
BLM PLSS is survey reference and MLRS records are lease-case context, neither
ownership proof nor parcel geometry. People uses aggregate Census context and
attributed historical research, without exposing personal identities or DNA.
Ecology uses land-cover and water-network context, without inventing species or
habitat inventories. History links existing research and map tools; archival
accounts remain separate from admitted evidence. Repository feature maturity
and operational handoff labels are preserved.

## Placement and authority

Directory Rules v2 (`docs/doctrine/directory-rules.md` in the KFM repository),
accepted ADR-0029 and this Site’s `AGENTS.md`/`SITE_PRESERVATION.md` establish the
placement basis: deployable behavior belongs to `apps/`, human guidance to
`docs/`, and domains are lanes rather than new responsibility roots.
In this preserved standalone Site, the existing `app/`, `tests/` and `docs/`
homes are used; the monorepo projection would remain inside `apps/site/source/`.
The new `app/topics/` directory owns a working application route. This is an
application view model, not a second domain registry, semantic contract,
schema, policy or release home. It does not activate canonical domain lanes.
No files under the ChatGPT project’s synced `sources/` are edited.

## Validation and rollback

`tests/topic-organization.test.mjs` checks requested subjects, route targets,
complete current inventories, cross-disciplinary membership, coverage limits,
unknown identity handling, immutable filtering and rendered selector/index
behavior. The existing layer-explorer tests exercise the actual page catalogue
projection and continued specialist mounting. Production build, full Site
tests and rendered browser checks are separate validation evidence.

Rollback is the previous saved same-Site version or a revert of these source
changes. There is no database, data asset or saved-workspace migration. The
owner-private audience and DB/BUCKET bindings must remain unchanged. Source
publication does not promote the referenced data or certify scientific,
engineering, legal, historical or personal claims.
