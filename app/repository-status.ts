/** Device-visible observation validity; this is not repository or release authority. */
export const REPOSITORY_STATUS_TTL_MS = 60_000;

export type RepositoryConnection = Readonly<{
  state: "idle" | "loading" | "ready" | "stale" | "error";
  liveCommit?: string;
  shortCommit?: string;
  commitDate?: string | null;
  message?: string | null;
  observedAt?: string;
  expiresAt?: number;
}>;

export function parseRepositoryObservation(payload: unknown, now = Date.now()): RepositoryConnection {
  if (!payload || typeof payload !== "object" || Array.isArray(payload)) throw new Error("Invalid repository observation");
  const value = payload as Record<string, unknown>;
  const observed = typeof value.observedAt === "string" ? Date.parse(value.observedAt) : NaN;
  if (value.state !== "ready" || value.repository !== "bartytime4life/Kansas-Frontier-Matrix"
    || value.ref !== "main" || value.mode !== "READ_ONLY_PUBLIC_METADATA"
    || value.synchronization !== "SITE_SOURCE_SEPARATE"
    || typeof value.commit !== "string" || !/^[0-9a-f]{40}$/i.test(value.commit)
    || !Number.isFinite(now) || !Number.isFinite(observed) || observed > now) {
    throw new Error("Invalid repository observation");
  }
  const commit = value.commit.toLowerCase();
  const expiresAt = observed + REPOSITORY_STATUS_TTL_MS;
  return {
    state: now < expiresAt ? "ready" : "stale",
    liveCommit: commit,
    shortCommit: commit.slice(0, 7),
    commitDate: typeof value.commitDate === "string" && Number.isFinite(Date.parse(value.commitDate)) ? value.commitDate : null,
    message: typeof value.message === "string" ? value.message.slice(0, 180) : null,
    observedAt: new Date(observed).toISOString(),
    expiresAt,
  };
}
