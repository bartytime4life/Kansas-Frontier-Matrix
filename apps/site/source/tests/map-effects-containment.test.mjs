import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import postcss from 'postcss';
const source = await readFile('app/page.tsx','utf8');
const tree = ts.createSourceFile('page.tsx',source,ts.ScriptTarget.Latest,true,ts.ScriptKind.TSX);
const css = postcss.parse(await readFile('app/globals.css','utf8'));
function className(node) { return node.attributes.properties.find(p=>ts.isJsxAttribute(p)&&p.name.getText(tree)==='className')?.initializer?.text; }
function nodesOfClass(name) { const matches=[]; const visit=node=>{if(ts.isJsxOpeningElement(node)&&className(node)===name)matches.push(node.parent);if(ts.isJsxSelfClosingElement(node)&&className(node)===name)matches.push(node);ts.forEachChild(node,visit)};visit(tree);return matches; }
function values(selector,mobile=false,reduced=false) {
  const styles={};css.walkRules(rule=>{if(!rule.selectors.includes(selector))return;
    for(let p=rule.parent;p&&p.type!=='root';p=p.parent)if(p.type==='atrule'&&p.name==='media'){
      if(p.params.includes('prefers-reduced-motion')&&!reduced)return;
      if(p.params.includes('max-width')&&!mobile)return;
      if(p.params.includes('pointer:coarse')||p.params.includes('pointer: coarse'))return;
    }
    rule.walkDecls(decl=>styles[decl.prop]=decl.value);
  });return styles;
}
test('water, wind and hover positions share a clipped map-local surface instead of covering the panel',()=>{
  const [effects]=nodesOfClass('map-effects');assert.ok(effects);
  for(const c of ['wind-arrow-canvas','water-motion-canvas','wind-arrow-hover']) {
    const [node]=nodesOfClass(c);assert.ok(node);let parent=node.parent;while(parent&&parent!==effects)parent=parent.parent;assert.equal(parent,effects,`${c} must be contained`);
  }
  const style=values('.map-effects');assert.equal(style.overflow,'hidden');assert.equal(style.isolation,'isolate');assert.equal(style['pointer-events'],'none');assert.equal(style['z-index'],'1');
  const map=values('.map-canvas');assert.equal(map.overflow,'hidden');assert.equal(map.isolation,'isolate');assert.equal(map['z-index'],'0');
});
test('effects track the desktop/mobile locator bounds and reduced-motion transition exactly',()=>{
  for(const mobile of [false,true])for(const reduced of [false,true]){
    const map=values('.map-stage[data-underground="true"] .map-canvas',mobile,reduced),effects=values('.map-stage[data-underground="true"] .map-effects',mobile,reduced);
    for(const field of ['top','bottom','transition'])assert.equal(effects[field],map[field],`${field}: mobile=${mobile}, reduced=${reduced}`);
  }
});
