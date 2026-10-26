import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';

const source=ts.transpileModule(await readFile('app/measurement-format.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const {formatMeasuredArea}=await import(`data:text/javascript;base64,${Buffer.from(source).toString('base64')}`);

test('measured areas read in acres or hectares below one square unit',()=>{
 assert.equal(formatMeasuredArea(0.25,false),'160 acres approximate','a quarter section');
 assert.equal(formatMeasuredArea(0.005,false),'3.2 acres approximate','small plots keep a decimal');
 assert.equal(formatMeasuredArea(1,false),'1.0 sq mi (640 acres) approximate','a PLSS section');
 assert.equal(formatMeasuredArea(36,false),'36.0 sq mi (23,040 acres) approximate','a survey township');
 assert.equal(formatMeasuredArea(0.25,true),'65 ha approximate','a quarter section in hectares');
 assert.equal(formatMeasuredArea(0.01,true),'2.6 ha approximate');
 assert.equal(formatMeasuredArea(1,true),'2.6 km² (259 ha) approximate');
});

test('the Explorer measurement label uses it for polygons',async()=>{
 const page=await readFile('app/page.tsx','utf8');
 assert.match(page,/return formatMeasuredArea\(areaSquareMiles\(coordinates\), unit === "metric"\);/);
});
