import { create3DepDemTileService } from "../../3dep-dem-tiles";

export const dynamic = "force-dynamic";
export const GET = create3DepDemTileService({ edgeCache: () => (globalThis.caches as CacheStorage & { default?: Cache } | undefined)?.default });
