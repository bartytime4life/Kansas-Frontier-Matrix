export const dynamic = "force-dynamic";

const REPOSITORY = "bartytime4life/Kansas-Frontier-Matrix";
const REF = "main";
const BRANCH_URL = `https://api.github.com/repos/${REPOSITORY}/branches/${REF}`;
const MAX_RESPONSE_BYTES = 512 * 1024;
const CACHE_TTL_MS = 60_000;

type JsonRecord = Record<string, unknown>;
type CachedRepositoryStatus = Readonly<{
  expiresAt: number;
  payload: Readonly<{
    state: "ready";
    repository: typeof REPOSITORY;
    ref: typeof REF;
    commit: string;
    shortCommit: string;
    commitDate: string | null;
    message: string | null;
    observedAt: string;
    source: typeof BRANCH_URL;
    mode: "READ_ONLY_PUBLIC_METADATA";
    synchronization: "SITE_SOURCE_SEPARATE";
  }>;
}>;

let cachedStatus: CachedRepositoryStatus | null = null;

const isRecord = (value: unknown): value is JsonRecord => Boolean(value) && typeof value === "object" && !Array.isArray(value);
const asString = (value: unknown) => typeof value === "string" ? value : null;

const readBoundedJson = async (response: Response): Promise<unknown> => {
  const declaredLength = Number(response.headers.get("content-length") ?? "0");
  if (declaredLength > MAX_RESPONSE_BYTES) throw new Error("GitHub response exceeded the bounded adapter limit.");
  const body = await response.arrayBuffer();
  if (body.byteLength > MAX_RESPONSE_BYTES) throw new Error("GitHub response exceeded the bounded adapter limit.");
  return JSON.parse(new TextDecoder().decode(body)) as unknown;
};

export async function GET() {
  if (cachedStatus && cachedStatus.expiresAt > Date.now()) {
    return Response.json(cachedStatus.payload, {
      headers: { "cache-control": "public, max-age=60, stale-while-revalidate=300" },
    });
  }

  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 10_000);

  try {
    const response = await fetch(BRANCH_URL, {
      cache: "no-store",
      headers: {
        accept: "application/vnd.github+json",
        "user-agent": "KansasFrontierMatrixExplorer/1.0",
        "x-github-api-version": "2022-11-28",
      },
      signal: controller.signal,
    });
    if (!response.ok) throw new Error(`GitHub returned HTTP ${response.status}.`);

    const parsed = await readBoundedJson(response);
    const commit = isRecord(parsed) && isRecord(parsed.commit) ? parsed.commit : null;
    if (!commit) throw new Error("GitHub omitted main commit metadata.");
    const sha = asString(commit.sha);
    if (!sha || !/^[0-9a-f]{40}$/i.test(sha)) throw new Error("GitHub omitted a valid main commit identity.");

    const nestedCommit = isRecord(commit.commit) ? commit.commit : null;
    const committer = nestedCommit && isRecord(nestedCommit.committer) ? nestedCommit.committer : null;
    const rawMessage = nestedCommit ? asString(nestedCommit.message) : null;
    const payload: CachedRepositoryStatus["payload"] = {
      state: "ready",
      repository: REPOSITORY,
      ref: REF,
      commit: sha.toLowerCase(),
      shortCommit: sha.slice(0, 7).toLowerCase(),
      commitDate: committer ? asString(committer.date) : null,
      message: rawMessage?.split("\n", 1)[0]?.slice(0, 180) ?? null,
      observedAt: new Date().toISOString(),
      source: BRANCH_URL,
      mode: "READ_ONLY_PUBLIC_METADATA",
      synchronization: "SITE_SOURCE_SEPARATE",
    };
    cachedStatus = { expiresAt: Date.now() + CACHE_TTL_MS, payload };
    return Response.json(payload, {
      headers: { "cache-control": "public, max-age=60, stale-while-revalidate=300" },
    });
  } catch (error) {
    const timedOut = error instanceof Error && error.name === "AbortError";
    return Response.json({
      state: "error",
      repository: REPOSITORY,
      ref: REF,
      message: timedOut ? "The read-only GitHub check timed out." : "The read-only GitHub check is temporarily unavailable.",
      mode: "READ_ONLY_PUBLIC_METADATA",
      synchronization: "SITE_SOURCE_SEPARATE",
    }, {
      status: 502,
      headers: { "cache-control": "no-store" },
    });
  } finally {
    clearTimeout(timeout);
  }
}
