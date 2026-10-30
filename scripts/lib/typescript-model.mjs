import { readFile } from 'node:fs/promises';
import { resolve, dirname, extname } from 'node:path';
import { pathToFileURL } from 'node:url';
import ts from 'typescript';
// Direct Node inspection of the same extensionless TypeScript models used by the app.
const modules = new Map();
export async function modelUrl(file) {
  file = resolve(file);
  if (modules.has(file)) return modules.get(file);
  let js = ts.transpileModule(await readFile(file, 'utf8'), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  for (const match of [...js.matchAll(/from ["'](\.[^"']+)["']/g)]) {
    const target = resolve(dirname(file), match[1]);
    const url = extname(target) && extname(target) !== '.ts' ? pathToFileURL(target).href : await modelUrl(extname(target) ? target : target + '.ts');
    js = js.replace(match[0], `from ${JSON.stringify(url)}`);
  }
  const url = `data:text/javascript;base64,${Buffer.from(js).toString('base64')}`;
  modules.set(file, url);
  return url;
}
