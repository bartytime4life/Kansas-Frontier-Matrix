export function resolve(specifier, context, nextResolve) {
  if (specifier === "cloudflare:workers") return { url: "data:text/javascript,export const env = globalThis.__KFM_TEST_BINDINGS ??= {};", shortCircuit: true };
  return nextResolve(specifier, context);
}
