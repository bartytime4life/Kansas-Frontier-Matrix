import { readBoundedJson } from "./bounded-json";
import { parseWindArrowResponse, windArrowRequest, type WindArrowFrame } from "./wind-arrow-data";

export type WindFlowTransport = "site" | "direct-provider";

/** Recover only the provider's rate limit on the shared Site egress address.
 * The viewer then requests the same fixed grid directly from Open-Meteo and
 * validates every sample against the same model and time contract. */
export async function loadWindFlowFrame(
  bbox: string,
  signal: AbortSignal,
  fetcher: typeof fetch = fetch,
  now: () => number = Date.now,
): Promise<{ frame: WindArrowFrame; transport: WindFlowTransport }> {
  const path = `/api/wind-arrows?bbox=${encodeURIComponent(bbox)}`;
  const response = await fetcher(path, { signal, cache: "no-store" });
  if (response.ok) {
    const frame = await readBoundedJson(response, 160_000) as WindArrowFrame;
    if (!Array.isArray(frame.samples) || frame.samples.length !== 16 || typeof frame.validTimeUtc !== "string") throw new Error("Incomplete wind grid.");
    return { frame, transport: "site" };
  }
  const problem = await readBoundedJson(response, 1024) as { code?: string };
  if (problem.code !== "MODEL_HTTP_429") throw new Error("Wind model unavailable.");
  const grid = windArrowRequest(new URL(path, "https://kfm.example"));
  const provider = await fetcher(grid.url, { signal, cache: "no-store", mode: "cors" });
  if (!provider.ok || !(provider.headers.get("content-type") ?? "").includes("application/json")) throw new Error("Direct wind model unavailable.");
  const frame = parseWindArrowResponse(await readBoundedJson(provider, 160_000), grid.coordinates, now());
  return { frame, transport: "direct-provider" };
}
