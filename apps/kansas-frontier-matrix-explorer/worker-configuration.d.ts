/**
 * Narrow host bridge for the Sites/Vinext application.
 *
 * This repository does not currently commit a Wrangler configuration for this
 * Sites-derived app, so `wrangler types` cannot yet bind runtime APIs to an
 * exact compatibility date and binding set. Keep the injected environment
 * opaque here and narrow individual bindings at their use sites. When a real
 * Wrangler config becomes repository authority, replace this bridge with the
 * generated `wrangler types` output rather than growing hand-authored runtime
 * declarations.
 */
declare module "cloudflare:workers" {
  export const env: Readonly<Record<string, unknown>>;
}
