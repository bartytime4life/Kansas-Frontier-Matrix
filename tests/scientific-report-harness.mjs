import {readFile} from 'node:fs/promises';
import ts from 'typescript';
const url = code => `data:text/javascript;base64,${Buffer.from(code).toString('base64')}`;
const compile = async name => ts.transpileModule(await readFile(new URL(`../app/${name}.ts`, import.meta.url), 'utf8'), {compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const materials = url(await compile('subsurface-materials'));
const subsurface = url((await compile('subsurface-model')).replace('"./subsurface-materials"',JSON.stringify(materials)));
const outline = url(await compile('kansas-orientation'));
export const scientific = await import(url((await compile('scientific-report')).replace('"./kansas-orientation"',JSON.stringify(outline)).replace('"./subsurface-model"',JSON.stringify(subsurface))));
