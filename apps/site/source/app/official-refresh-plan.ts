/** A selected source is a request candidate only at the operational-present frame. */
export function planOfficialRefresh(
  sources: readonly { id: string; apiPath?: string }[],
  selected: Readonly<Record<string, boolean>>,
  frame: number,
  presentFrame: number,
  streamflowArchiveDay: boolean,
  archivedDays: Readonly<Record<string, string | undefined>> = {},
) {
  const empty = { feeds: [] as string[], radar: false, satellite: false, lightning: false, streamflow: false, hydrology: false, count: 0 };
  if (frame !== presentFrame) return { ...empty, reason: "historical" as const };
  const feeds = sources.filter((source) => source.apiPath && selected[source.id] && !archivedDays[source.id]).map((source) => source.id);
  const radar = Boolean(selected["nws-radar"]);
  const satellite = Boolean(selected["noaa-goes-geocolor"]);
  const lightning = Boolean(selected["noaa-lightning-density"]);
  const streamflow = Boolean(selected["usgs-streamflow"]) && !streamflowArchiveDay;
  const hydrology = Boolean(selected["noaa-nwps-gauges"]);
  const count = feeds.length + Number(radar) + Number(satellite) + Number(lightning) + Number(streamflow) + Number(hydrology);
  return { feeds, radar, satellite, lightning, streamflow, hydrology, count, reason: count ? null : "none" as const };
}
