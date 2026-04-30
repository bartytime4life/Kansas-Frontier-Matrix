export function canViewStewardDetails(role) {
  return role === "steward" || role === "reviewer";
}
