import { createTerrainTileService } from "../../terrain-tiles";
export const dynamic = "force-dynamic";
export const GET = createTerrainTileService({ edgeCache: () => (globalThis.caches as CacheStorage & { default?: Cache } | undefined)?.default });
