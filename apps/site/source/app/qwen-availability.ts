/** Model installation and answered requests are separate observations. */
export type QwenBridgeState =
  | "checking" | "installed" | "local-answered" | "hosted-answered"
  | "not-configured" | "error";

export const shouldUseLocalQwen = (state: QwenBridgeState) =>
  state === "installed" || state === "local-answered";

export const successfulQwenState = (local: boolean): QwenBridgeState =>
  local ? "local-answered" : "hosted-answered";

export const qwenStatusLabel = (state: QwenBridgeState): string => {
  switch (state) {
    case "checking": return "CHECKING LOCAL MODEL";
    case "installed": return "LOCAL MODEL INSTALLED";
    case "local-answered": return "LOCAL MODEL ANSWERED";
    case "hosted-answered": return "HOSTED MODEL ANSWERED";
    case "not-configured": return "LOCAL BRIDGE UNAVAILABLE";
    case "error": return "LAST QWEN REQUEST FAILED";
  }
};
