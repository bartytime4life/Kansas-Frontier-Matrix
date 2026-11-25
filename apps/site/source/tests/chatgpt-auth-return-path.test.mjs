import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const compile = source => `data:text/javascript;base64,${Buffer.from(ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText).toString("base64")}`;
const headersUrl = compile("export async function headers() { return new Headers(); }");
const navigationUrl = compile("export function redirect(path) { throw new Error(`redirect ${path}`); }");
const source = (await readFile(new URL("../app/chatgpt-auth.ts", import.meta.url), "utf8"))
  .replace('"next/headers"', JSON.stringify(headersUrl)).replace('"next/navigation"', JSON.stringify(navigationUrl));
const { chatGPTSignInPath, chatGPTSignOutPath } = await import(compile(source));
const returnTo = path => new URL(path, "https://site.example").searchParams.get("return_to");

test("sign-in and sign-out return paths stay on this Site after URL normalization", () => {
  // Dot segments and backslashes normalize to a protocol-relative "//host" path.
  for (const value of ["//evil.example", "/\\evil.example", "/.//evil.example", "/a/..//evil.example", "/%2e//evil.example", "/./\\evil.example", "/\t/evil.example", "https://evil.example/", "relative"]) {
    for (const path of [chatGPTSignInPath(value), chatGPTSignOutPath(value)]) {
      const target = returnTo(path);
      assert.equal(target, "/", `${JSON.stringify(value)} -> ${JSON.stringify(target)}`);
      assert.equal(new URL(target, "https://site.example").origin, "https://site.example");
    }
  }
});

test("ordinary same-site return paths keep their path, query and fragment", () => {
  assert.equal(returnTo(chatGPTSignInPath("/data?source=usgs-streamflow")), "/data?source=usgs-streamflow");
  assert.equal(returnTo(chatGPTSignInPath("/governed/water-release")), "/governed/water-release");
  assert.equal(returnTo(chatGPTSignInPath("/a/./b/../c?x=1#top")), "/a/c?x=1#top");
  assert.equal(returnTo(chatGPTSignInPath("/signin-with-chatgpt")), "/", "auth endpoints never become return targets");
});
