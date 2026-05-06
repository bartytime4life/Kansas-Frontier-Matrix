export function toFiniteFocusOutcome(runtimeResponse) {
  return runtimeResponse?.outcome ?? "ABSTAIN";
}
