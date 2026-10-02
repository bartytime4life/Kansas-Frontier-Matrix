import type { WaterResponse } from "./governed-water";

export type WaterBrowserState = "not-checked" | "checking" | "received" | "no-release" | "withheld" | "unavailable";

/** Classify the response observed by this browser; never infer a release from a transport failure. */
export function waterBrowserStateForResponse(value: WaterResponse | null, httpOk: boolean): WaterBrowserState {
  if (!httpOk || !value?.envelope) return "unavailable";
  if (value.envelope.outcome === "ANSWER") {
    return Array.isArray(value.data?.stations) && Array.isArray(value.data?.observations) ? "received" : "withheld";
  }
  return value.envelope.reason_code === "NO_APPROVED_SNAPSHOT" ? "no-release" : "withheld";
}

export function waterBrowserLabel(state: WaterBrowserState): string {
  switch (state) {
    case "not-checked": return "Not checked";
    case "checking": return "Checking";
    case "received": return "Received";
    case "no-release": return "No reviewed release active";
    case "withheld": return "Withheld";
    case "unavailable": return "Unavailable";
  }
}
