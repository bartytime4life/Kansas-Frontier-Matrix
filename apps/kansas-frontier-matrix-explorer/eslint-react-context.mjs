/**
 * Bridge only the ESLint 10 context metadata API removed from the React plugin.
 * This is not an AST/rule rewrite, a dependency patch, or a rule suppression.
 * SourceCode, visitors, reports, settings, options, and exceptions stay original.
 * Remove after the locked React plugin supports ESLint 10 and parity tests pass.
 * API reference: https://eslint.org/docs/latest/use/migrate-to-10.0.0
 */
const replacements = new WeakMap();

export function withESLint10ReactContext(plugin) {
  if (replacements.has(plugin)) return replacements.get(plugin);
  const rules = Object.fromEntries(Object.entries(plugin.rules).map(([name, rule]) => {
    if (typeof rule.create !== "function") {
      throw new TypeError(`Unsupported React rule definition: ${name}`);
    }
    return [name, {
      ...rule,
      create(context) {
        if (typeof context.getFilename === "function") {
          return rule.create.call(rule, context);
        }
        const bridge = Object.create(context);
        Object.defineProperties(bridge, {
          getFilename: { value: () => context.filename, enumerable: true },
          getPhysicalFilename: { value: () => context.physicalFilename, enumerable: true },
          getCwd: { value: () => context.cwd, enumerable: true },
          getSourceCode: { value: () => context.sourceCode, enumerable: true },
          parserOptions: { value: context.languageOptions.parserOptions, enumerable: true },
        });
        return rule.create.call(rule, Object.freeze(bridge));
      },
    }];
  }));
  const replacement = { ...plugin, rules };
  replacements.set(plugin, replacement);
  replacements.set(replacement, replacement);
  return replacement;
}
