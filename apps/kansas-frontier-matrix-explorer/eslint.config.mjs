import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";
import { withESLint10ReactContext } from "./eslint-react-context.mjs";

const eslintConfig = defineConfig([
  ...nextVitals.map((config) => config.plugins?.react ? {
    ...config,
    plugins: { ...config.plugins, react: withESLint10ReactContext(config.plugins.react) },
  } : config),
  ...nextTs,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
  ]),
]);

export default eslintConfig;
