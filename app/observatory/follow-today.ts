export const FOLLOW_TODAY_REFRESH_MS = 300_000;

/** Follow mode checks elapsed time when the page becomes visible or idle. */
export function shouldRefreshFollowToday(input: {
  following: boolean;
  hidden: boolean;
  busy: boolean;
  lastRefreshAt: number;
  now: number;
  displayedDay: string;
  today: string;
}): boolean {
  if (!input.following || input.hidden || input.busy || input.lastRefreshAt <= 0) return false;
  return input.displayedDay !== input.today
    || input.now < input.lastRefreshAt
    || input.now - input.lastRefreshAt >= FOLLOW_TODAY_REFRESH_MS;
}
