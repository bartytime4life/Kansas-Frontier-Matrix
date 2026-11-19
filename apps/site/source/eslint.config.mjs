import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
    // Installed, pinned third-party browser decoder; not application source.
    "public/vendor/h5wasm/**",
  ]),
  {
    rules: {
      // `const { secret: _secret, ...safe } = row` and `_unused` parameters are
      // deliberate omissions; report every other unused binding.
      "@typescript-eslint/no-unused-vars": ["warn", { argsIgnorePattern: "^_", ignoreRestSiblings: true }],
    },
  },
]);

export default eslintConfig;
