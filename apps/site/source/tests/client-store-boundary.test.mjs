import assert from "node:assert/strict";
import { readFile, readdir, stat } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import ts from "typescript";

const appRoot = fileURLToPath(new URL("../app/", import.meta.url));
const sourceRoot = path.dirname(appRoot);
const codeExtensions = [".ts", ".tsx", ".js", ".mjs"];
const serverModule = /(?:^|\/)(?:db\.[cm]?[jt]s|[^/]+-server\.[cm]?[jt]sx?|route\.[cm]?[jt]s)$/;

async function codeFiles(directory) {
  const files = [];
  for (const entry of await readdir(directory, { withFileTypes: true })) {
    const name = path.join(directory, entry.name);
    if (entry.isDirectory()) files.push(...await codeFiles(name));
    else if (codeExtensions.some((extension) => name.endsWith(extension)) && !name.endsWith(".d.ts")) files.push(name);
  }
  return files;
}

function parsed(file, source) {
  return ts.createSourceFile(file, source, ts.ScriptTarget.Latest, true,
    file.endsWith(".tsx") ? ts.ScriptKind.TSX : ts.ScriptKind.TS);
}

function runtimeImports(tree) {
  const imports = [];
  for (const statement of tree.statements) {
    if (ts.isImportDeclaration(statement) && !statement.importClause?.isTypeOnly) imports.push(statement.moduleSpecifier.text);
    if (ts.isExportDeclaration(statement) && statement.moduleSpecifier && !statement.isTypeOnly) imports.push(statement.moduleSpecifier.text);
  }
  const visit = (node) => {
    if (ts.isCallExpression(node) && node.expression.kind === ts.SyntaxKind.ImportKeyword) {
      assert.ok(node.arguments.length === 1 && ts.isStringLiteral(node.arguments[0]),
        `${tree.fileName}: browser dynamic import must use a literal module path`);
      imports.push(node.arguments[0].text);
    }
    ts.forEachChild(node, visit);
  };
  ts.forEachChild(tree, visit);
  return imports;
}

async function resolveLocal(from, specifier) {
  const base = path.resolve(path.dirname(from), specifier);
  for (const candidate of [base, ...codeExtensions.map((extension) => base + extension),
    ...codeExtensions.map((extension) => path.join(base, `index${extension}`))]) {
    try { if ((await stat(candidate)).isFile()) return candidate; } catch { /* Try the next extension. */ }
  }
  assert.fail(`${from}: unresolved browser import ${specifier}`);
}

test("boundary scan follows runtime imports and ignores type-only imports", () => {
  const tree = parsed("fixture.ts", [
    'import type { Row } from "./types";',
    'import { value } from "./db";',
    'export { other } from "./other";',
    'void import("./dynamic");',
  ].join("\n"));
  assert.deepEqual(runtimeImports(tree), ["./db", "./other", "./dynamic"]);
  assert.throws(() => runtimeImports(parsed("fixture.ts", "void import(target);")), /literal module path/);
  for (const file of ["/site/db.ts", "/site/app/governed-water-server.ts", "/site/app/api/governed/v1/route.ts"]) {
    assert.match(file, serverModule);
  }
});

test("current Site client graph cannot import server stores or route handlers", async () => {
  const files = await codeFiles(appRoot);
  const roots = [];
  for (const file of files) {
    const tree = parsed(file, await readFile(file, "utf8"));
    if (tree.statements.some((statement) => ts.isExpressionStatement(statement)
      && ts.isStringLiteral(statement.expression) && statement.expression.text === "use client")) roots.push(file);
  }
  assert.ok(roots.length >= 20, "Expected the current Site client entrypoints, not an empty retired shell");
  const queue = [...roots], visited = new Set();
  while (queue.length) {
    const file = queue.pop();
    if (visited.has(file)) continue;
    visited.add(file);
    assert.ok(file.startsWith(sourceRoot + path.sep), `Client import leaves Site source: ${file}`);
    assert.doesNotMatch(file, serverModule,
      `Server store or route is reachable from a Site client: ${file}`);
    const tree = parsed(file, await readFile(file, "utf8"));
    for (const specifier of runtimeImports(tree)) {
      assert.doesNotMatch(specifier, /^(?:cloudflare:|node:|server-only$|next\/(?:headers|server)$)/,
        `Server capability is reachable from a Site client: ${file} -> ${specifier}`);
      if (specifier.startsWith(".")) queue.push(await resolveLocal(file, specifier));
    }
  }
  assert.ok(visited.size >= roots.length);
});
