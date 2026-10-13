// Server-only compatibility for scalar configuration. D1 and R2 are not
// provisioned by Node hosting; routes retain their existing unavailable states
// until explicit storage adapters and a reversible migration are configured.
export const env: Record<string, unknown> = { ...process.env, DB: undefined, BUCKET: undefined };
