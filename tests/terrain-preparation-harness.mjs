import {readFile} from 'node:fs/promises';
import ts from 'typescript';
export const compileTerrain=source=>ts.transpileModule(source,{compilerOptions:{target:ts.ScriptTarget.ES2022,module:ts.ModuleKind.CommonJS}}).outputText;
const modules={};
for(const file of ['native-lidar','kansas-ground','kansas-terrain-analysis','kansas-lidar-grid-layer','terrain-preparation-model','terrain-insights','visitor-terrain-policy','terrain-transect','terrain-report']){
 const exports={};new Function('exports','require',compileTerrain(await readFile('app/'+file+'.ts','utf8')))(exports,name=>name==='./native-lidar-layer'?{createLidarGeometryLayer:g=>g}:modules[name.slice(2)]);modules[file]=exports;
}
export const terrainModules=modules;
