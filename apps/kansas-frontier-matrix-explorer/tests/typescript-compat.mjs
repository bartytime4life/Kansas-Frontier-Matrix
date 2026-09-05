import { spawnSync } from "node:child_process";
import { existsSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { basename, join } from "node:path";
import { fileURLToPath } from "node:url";

// TypeScript 7 intentionally moved the classic compiler API away from the
// package root. Existing Explorer tests only need the old transpileModule
// subset, so keep that compatibility local to this test package and drive the
// app-declared TypeScript 7 CLI instead of pinning a second compiler.
export const ModuleKind = Object.freeze({ ESNext: "ESNext" });
export const ScriptTarget = Object.freeze({ ES2022: "ES2022" });
export const JsxEmit = Object.freeze({ ReactJSX: "react-jsx" });
export const DiagnosticCategory = Object.freeze({ Error: 1 });

const tscPath = fileURLToPath(
  new URL("../node_modules/typescript/bin/tsc", import.meta.url),
);

function emittedName(fileName) {
  return basename(fileName).replace(/\.(?:tsx?|mts|cts)$/u, ".js");
}

function failureDiagnostic(child) {
  const detail = [child.stderr, child.stdout]
    .filter((value) => typeof value === "string" && value.trim())
    .join("\n")
    .trim();
  return {
    category: DiagnosticCategory.Error,
    messageText: detail || `TypeScript CLI transpile exited ${child.status ?? "without status"}`,
  };
}

export function transpileModule(source, options = {}) {
  if (typeof source !== "string") {
    throw new TypeError("transpileModule source must be a string");
  }

  const compilerOptions = options.compilerOptions ?? {};
  const moduleKind = compilerOptions.module ?? ModuleKind.ESNext;
  const target = compilerOptions.target ?? ScriptTarget.ES2022;
  const jsx = compilerOptions.jsx;

  if (moduleKind !== ModuleKind.ESNext) {
    throw new Error(`unsupported test module kind: ${String(moduleKind)}`);
  }
  if (target !== ScriptTarget.ES2022) {
    throw new Error(`unsupported test script target: ${String(target)}`);
  }
  if (jsx !== undefined && jsx !== JsxEmit.ReactJSX) {
    throw new Error(`unsupported test JSX mode: ${String(jsx)}`);
  }
  if (!existsSync(tscPath)) {
    throw new Error(`app-local TypeScript CLI is unavailable at ${tscPath}`);
  }

  const directory = mkdtempSync(join(tmpdir(), "kfm-explorer-ts7-transpile-"));
  try {
    const fileName = basename(options.fileName ?? "module.ts");
    const inputPath = join(directory, fileName);
    const outputPath = join(directory, emittedName(fileName));
    writeFileSync(inputPath, source, "utf8");

    const args = [
      tscPath,
      "--pretty",
      "false",
      "--noCheck",
      "--isolatedModules",
      "--module",
      "ESNext",
      "--target",
      "ES2022",
      "--moduleResolution",
      "Bundler",
      "--skipLibCheck",
      "--rootDir",
      directory,
      "--outDir",
      directory,
    ];
    if (jsx === JsxEmit.ReactJSX) {
      args.push("--jsx", "react-jsx");
    }
    args.push(inputPath);

    const child = spawnSync(process.execPath, args, {
      encoding: "utf8",
      env: { ...process.env, NO_COLOR: "1" },
    });

    if (child.status !== 0 || !existsSync(outputPath)) {
      return {
        outputText: "",
        diagnostics: [failureDiagnostic(child)],
      };
    }

    return {
      outputText: readFileSync(outputPath, "utf8"),
      diagnostics: [],
    };
  } finally {
    rmSync(directory, { recursive: true, force: true });
  }
}
