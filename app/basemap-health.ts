/** Display health only: no provider requests, source admission or retry timers. */
export const BASEMAP_TILE_WARNING = "Some basemap tiles are unavailable. Gaps are unknown; choose another basemap or retry. Map controls and records remain available.";
export const BASEMAP_SOURCE_WARNING = "A basemap source reported an error. Coverage is unknown; choose another basemap or retry. Map controls and records remain available.";

const record = (value: unknown): Record<string, unknown> | null => value !== null && typeof value === "object" ? value as Record<string, unknown> : null;
const tiled = new Set(["raster", "raster-dem", "vector"]);

/** Compare request/decoder identity, never exception text. Values stay local. */
export function basemapSourceIdentity(value: unknown): string | null {
  const source = record(value);
  if (!source || typeof source.type !== "string") return null;
  const tiles = Array.isArray(source.tiles) && source.tiles.every(tile => typeof tile === "string") ? source.tiles : null;
  const url = typeof source.url === "string" ? source.url : null;
  if (!tiles && !url) return null;
  return JSON.stringify([source.type, url, tiles, source.encoding ?? null, source.tileSize ?? null, source.scheme ?? null]);
}

/** Internal correlation key; never include geographic tile coordinates in receipts. */
export function basemapTileKey(value: unknown): string | null {
  const event = record(value), tile = record(event?.tile);
  const id = record(tile?.tileID) ?? record(event?.coord), canonical = record(id?.canonical);
  if (!canonical || ![canonical.z, canonical.x, canonical.y].every(n => typeof n === "number" && Number.isInteger(n) && n >= 0)) return null;
  const { z, x, y } = canonical as { z: number; x: number; y: number };
  if (z > 30 || x >= 2 ** z || y >= 2 ** z) return null;
  return `${z}/${x}/${y}/${typeof id?.wrap === "number" ? id.wrap : 0}/${typeof id?.overscaledZ === "number" ? id.overscaledZ : z}`;
}

export type BasemapHealthInput = { sourceId: string; sourceInstance?: object; sourceSpec: unknown; event: unknown };
export type BasemapErrorKind = "tile" | "source" | "stale" | "cancelled" | "unrelated";

export function classifyBasemapError(input: BasemapHealthInput): BasemapErrorKind {
  const event = record(input.event), source = record(input.sourceSpec);
  const current = basemapSourceIdentity(source), origin = basemapSourceIdentity(event?.source);
  // Missing provenance is unknown, not proof of a stale event.
  if (current && origin && current !== origin) return "stale";
  if (!source || !tiled.has(String(source.type))) return "unrelated";
  if (record(event?.error)?.name === "AbortError") return "cancelled";
  return basemapTileKey(event) ? "tile" : "source";
}

export function createBasemapHealth(maxFailures = 128) {
  if (!Number.isInteger(maxFailures) || maxFailures < 1) throw new RangeError("Invalid basemap health bound");
  type Failure = { sourceId: string; sourceInstance?: object; identity: string | null; tile: string | null; kind: "tile" | "source" };
  const failures: Failure[] = [];
  let generation = 0, overflowed = false;
  return {
    generation: () => generation,
    // Called BEFORE setStyle. Retire only the abandoned style's display state;
    // the opt-in trace independently retains its original first failure.
    beginStyle() { generation++; failures.length = 0; overflowed = false; },
    error(input: BasemapHealthInput): BasemapErrorKind {
      const kind = classifyBasemapError(input);
      if (kind !== "tile" && kind !== "source") return kind;
      const tile = kind === "tile" ? basemapTileKey(input.event) : null;
      const identity = basemapSourceIdentity(record(input.event)?.source) ?? basemapSourceIdentity(input.sourceSpec);
      if (!failures.some(f => f.sourceId === input.sourceId && f.sourceInstance === input.sourceInstance && f.identity === identity && f.tile === tile)) {
        if (failures.length === maxFailures) overflowed = true;
        else failures.push({ sourceId: input.sourceId, sourceInstance: input.sourceInstance, identity, tile, kind });
      }
      return kind;
    },
    loaded(input: BasemapHealthInput) {
      const event = record(input.event);
      if (record(event?.tile)?.state !== "loaded" || !input.sourceInstance) return;
      const tile = basemapTileKey(event), identity = basemapSourceIdentity(event?.source);
      // Settlement (isSourceLoaded/idle) also includes errored tiles. Only a
      // matching, positively loaded tile from the same current source recovers.
      if (!tile || !identity || identity !== basemapSourceIdentity(input.sourceSpec)) return;
      for (let i = failures.length - 1; i >= 0; i--) {
        const f = failures[i];
        if (f.kind === "tile" && f.tile === tile && f.sourceId === input.sourceId
          && f.sourceInstance === input.sourceInstance && f.identity === identity) failures.splice(i, 1);
      }
    },
    warning(): string | null {
      if (overflowed) return "Basemap failures exceeded the health tracking bound. Coverage remains unknown; choose another basemap or retry. Map controls and records remain available.";
      return failures.some(f => f.kind === "tile") ? BASEMAP_TILE_WARNING : failures.length ? BASEMAP_SOURCE_WARNING : null;
    },
  };
}
