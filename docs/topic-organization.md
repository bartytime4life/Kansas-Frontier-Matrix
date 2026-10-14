# Subject organization

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
