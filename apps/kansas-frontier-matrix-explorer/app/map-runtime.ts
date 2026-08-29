export type BasemapKey = "midnight" | "prairie";

export type BasemapDescriptor = Readonly<{
  title: string;
  note: string;
}>;

export const BASEMAPS: Readonly<Record<BasemapKey, BasemapDescriptor>> = Object.freeze({
  midnight: Object.freeze({
    title: "Midnight navy",
    note: "Renderer-neutral high-contrast preference descriptor",
  }),
  prairie: Object.freeze({
    title: "Prairie dusk",
    note: "Renderer-neutral low-glare preference descriptor",
  }),
});
