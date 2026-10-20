// A navigation invalidates paused requests from its predecessor. Never hide
// current-document errors or other protocol failures behind that cancellation.
export function isStaleInterceptionCancellation(error, requestNavigation, navigation) {
  if (!(requestNavigation < navigation)) return false;
  try {
    const protocolError = JSON.parse(error.message);
    return protocolError?.code === -32602 && protocolError.message === "Invalid InterceptionId.";
  } catch {
    return false;
  }
}
