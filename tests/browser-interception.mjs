// Navigation or a matching Network.loadingFailed(canceled=true) event can
// invalidate a paused request. Never hide an unconfirmed current-request error
// or another protocol failure behind that cancellation.
export function isStaleInterceptionCancellation(error, requestNavigation, navigation, canceled = false) {
  if (!(requestNavigation < navigation) && canceled !== true) return false;
  try {
    const protocolError = JSON.parse(error.message);
    return protocolError?.code === -32602 && protocolError.message === "Invalid InterceptionId.";
  } catch {
    return false;
  }
}
