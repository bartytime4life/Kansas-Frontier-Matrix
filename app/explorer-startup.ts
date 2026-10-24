import { restoreTopic } from "./layer-workspaces";

/** View navigation only. A bypass never writes the device's guide preference. */
export function hasExplorerDestination(params: URLSearchParams, addressParams = params): boolean {
  const camera = addressParams.get("c")?.split(",");
  return restoreTopic(params.get("topic")) !== "all"
    || params.get("topic") === "all"
    || params.get("mapui") === "open"
    || params.get("layers") === "sources"
    || params.get("maptab") === "localAtlas"
    || params.get("layerView") === "imagery"
    || params.get("layerView") === "selected"
    || params.get("tm") === "comparison"
    || params.get("kfm-chat") === "1"
    // A shared camera in the address is intentional. The default camera saved
    // in every history entry must not silence welcome on a plain '/' reload.
    || (camera?.length === 2 && camera.every(value => value.trim() !== "" && Number.isFinite(Number(value))))
    || Boolean(params.get("f"));
}
