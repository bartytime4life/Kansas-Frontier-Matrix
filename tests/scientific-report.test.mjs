import assert from 'node:assert/strict';
import test from 'node:test';
import {scientific as report} from './scientific-report-harness.mjs';
const snapshot={id:'captured',createdAt:'2026-10-31T18:00:00Z',area:{label:'Kansas study area'},camera:{center:[-98,38]},representation:'2D',committedTime:{label:'2026'},visibleLayers:[],policy:{outcome:'ABSTAIN',reason:'No released finding'}};
const draft={title:'Test report',researchQuestion:'What is supported?',updatedAt:snapshot.createdAt,snapshot,includedEvidenceIds:[],sections:{summary:'Summary text',observations:'Observation text',findings:'No finding established',limitations:'Limited coverage',openQuestions:'Unknown cause',sources:'Source notes'}};
const evidence=(id,trustState='SOURCE_BACKED')=>({id,title:`Evidence ${id}`,sourceOrganization:'Example source',sourceRole:'Primary',trustState,temporalExtent:{label:'2020–2021',uncertainty:'Date uncertainty retained'},spatialScope:'County',supports:'Only the stated observation',cannotProve:'No causation',caveat:'Incomplete sample',citation:'Citation',officialUrl:'https://example.org/source'});

test('all map layouts retain narrative, scope, evidence selection, and exact appendix',()=>{
 for(const layout of ['overview','place','sources']){
  const markup=report.scientificReportMarkup({...draft,includedEvidenceIds:['a']},[evidence('a'),evidence('b')],layout,'Original appendix & details');
  for(const value of Object.values(draft.sections))assert.ok(markup.includes(value));
  assert.match(markup,/Evidence a/);assert.doesNotMatch(markup,/Evidence b/);
  assert.match(markup,/SOURCE_BACKED: 1 included evidence records/);assert.match(markup,/bar baseline 0/);
  assert.match(markup,/Original appendix &amp; details/);assert.match(markup,/Date uncertainty retained/);
  assert.match(markup,/Marker: saved map center/);assert.match(markup,/DRAFT · NOT PUBLISHED/);
 }
});
test('empty evidence is explicit and never presented as a measured zero or quality score',()=>{
 const html=report.scientificReportMarkup(draft,[],'overview','');
 assert.match(html,/No included evidence records to chart/);assert.match(html,/Missing evidence is not a zero-valued observation/);
 assert.doesNotMatch(html,/class="sr-bar"/);assert.match(html,/0<\/strong><span>Evidence records included/);
});
test('withheld or out-of-state camera never draws a location marker or private place context',()=>{
 for(const center of ['WITHHELD_BROWSER_LOCATION',[-120,45]]){
  const html=report.scientificReportMarkup({...draft,snapshot:{...snapshot,camera:{center}},...(typeof center==='string'?{researchContext:{anchor:{title:'SECRET_ANCHOR'}},subsurfaceContext:{records:['SECRET_WELL']}}:{})},[],'place','Public notes');
  assert.doesNotMatch(html,/<circle|SECRET_ANCHOR|SECRET_WELL/);
  assert.match(html,typeof center==='string'?/camera withheld/:/outside this Kansas locator/);
 }
});
test('report text and links cannot inject executable markup into preview or downloaded document',()=>{
 const attack='</style><script>alert(1)</script><img src=x onerror="alert(2)">';
 const html=report.scientificReportMarkup({...draft,title:attack,sections:{...draft.sections,findings:attack},includedEvidenceIds:['x']},[{...evidence('x'),officialUrl:'javascript:alert(1)',citation:attack}],'sources',attack);
 const document=report.scientificReportDocument(attack,html);
 assert.doesNotMatch(document,/<script|<img src=x|href="javascript:/);assert.match(document,/&lt;script&gt;/);
 assert.match(document,/default-src 'none'/);assert.ok(document.endsWith(`<body>${html}</body></html>`));
 for(const url of ['data:text/html,bad','https://user:password@example.org','file:///tmp/private']){
  assert.doesNotMatch(report.scientificReportMarkup({...draft,includedEvidenceIds:['x']},[{...evidence('x'),officialUrl:url}],'sources',''),/href=/);
 }
});
test('place comparisons show captured coverage and distances with source times, not inferred associations',()=>{
 const context={anchor:{title:'Study anchor'},radiusMiles:25,total:9,capturedAt:'2026-10-31',coverage:[{state:'ready'},{state:'ready'},{state:'held'}],records:[{title:'Example gauge',sourceTitle:'Provider',sourceUrl:'https://example.org',evidenceLabel:'Context only',limitation:'Provisional',distanceMiles:2.46,sourceTime:'2026-10-30',retrievedAt:'2026-10-31'}]};
 const html=report.scientificReportMarkup({...draft,researchContext:context},[],'place','');
 assert.match(html,/1 of 9 available records/);assert.match(html,/2\.5<\/td>/);assert.match(html,/ready: 2 captured source checks/);assert.match(html,/held: 1 captured source checks/);assert.match(html,/not evidence of association/);assert.match(html,/2026-10-30/);
});
const source={id:'source',title:'Historical source',url:'https://example.org',publisher:'Publisher',access:'partial',checkedAt:'2026-10-01',accessNote:'Partial acquisition',completeness:'Incomplete',coverage:'Supplied entries only',rights:'Publisher rights retained'};
const entry=(id,date,kind='person')=>({id,date,kind,title:`Record ${id}`,sourceId:'source',relation:'Original assertion',place:'Kansas — context only',reviewNote:'Not independently resolved',sourceUrl:'https://example.org',targetUrl:'https://example.org/entry'});
const catalog={sources:[source],checkedAt:'2026-10-01',attribution:'Original authors',scope:'Source assertions only'};
test('historical report orders only exact years and retains ambiguous dates, identity and source limits',()=>{
 const html=report.historyReportMarkup(catalog,[entry('later','1928','event'),entry('earlier','1917','event'),entry('range','1900–1920'),entry('none',null),entry('fiction','1920','fictional')],'Filtered page 2 · 5 of 60 entries');
 assert.ok(html.indexOf('Record earlier')<html.indexOf('Record fiction'));assert.ok(html.indexOf('Record fiction')<html.indexOf('Record later'));
 assert.match(html,/3<\/strong><span>Entries with sortable dates/);assert.match(html,/Other date statements &amp; undated entries/);assert.match(html,/1900–1920/);assert.match(html,/Date not supplied/);
 assert.match(html,/fictional: 1 source entries/);assert.match(html,/Repeated names remain separate source assertions/);
 for(const text of ['Partial acquisition','Incomplete','Publisher rights retained','Not independently resolved','Filtered page 2 · 5 of 60 entries'])assert.ok(html.includes(text));
});
test('historical report preserves hostile source text as text and does not fetch remote images or fonts',()=>{
 const markup=report.historyReportMarkup(catalog,[{...entry('x','1900'),title:'<img src=x onerror=alert(1)>',sourceUrl:'javascript:alert(1)',targetUrl:'javascript:alert(1)'}],'<script>scope</script>');
 const html=report.scientificReportDocument('History',markup);
 assert.doesNotMatch(html,/<script|<img|<link|href="javascript:/);assert.match(html,/&lt;script&gt;scope/);assert.match(html,/&lt;img/);
});

test('historical chronology accepts real calendar dates without fabricating precision or accepting invalid dates',()=>{
 const html=report.historyReportMarkup(catalog,[entry('birth','1897-07-24'),entry('year','1897'),entry('earlier','1897-01-02'),entry('leap','2000-02-29'),entry('invalid-century','1900-02-29'),entry('invalid-day','2000-02-30'),entry('invalid-month','2000-13-01')],'Date precision check');
 assert.match(html,/4<\/strong><span>Entries with sortable dates/);
 assert.ok(html.indexOf('Record year')<html.indexOf('Record earlier'));assert.ok(html.indexOf('Record earlier')<html.indexOf('Record birth'));assert.ok(html.indexOf('Record birth')<html.indexOf('Record leap'));
 const remainder=html.slice(html.indexOf('Other date statements &amp; undated entries'));
 for(const date of ['1900-02-29','2000-02-30','2000-13-01'])assert.ok(remainder.includes(date));
 assert.match(html,/no month or day is inferred/);assert.match(html,/1897-07-24/);
});

test('fire and recorded-depth visuals preserve context boundaries and source timing',()=>{
 const captured='2026-10-31T18:00:00Z';
 const well={id:'well-test',sourceId:'kgs-wwc5',kind:'well',name:'Test well',coordinates:[-95,39],coordinateReference:'WGS84 display',locationMethod:'PLSS approximate',sourceUrl:'https://www.kgs.ku.edu/',sourceTime:'2000-01-01',depthUnit:'ft',depthReference:'land-surface',totalDepth:100,intervals:[{top:0,bottom:10,description:'sand'},{top:20,bottom:30,description:'clay'}]};
 const subsurfaceContext={version:1,capturedAt:captured,anchor:[-95,39],pinned:true,transect:[],depthRange:[0,100],display:'section',exaggeration:1,selectedSources:['kgs-wwc5'],sourceVersions:[{id:'kgs-wwc5',title:'KGS wells',url:'https://www.kgs.ku.edu/',retrievedAt:captured,sourceTime:'2026',limitation:'Approximate locations',sha256:'a'.repeat(64)}],recordIds:['well-test'],records:[well],coverage:['Loaded subset only']};
 const fireContext={title:'Provider fire record',observedAt:'2026-10-30',retrievedAt:captured,feedState:'ready',sourceUrl:'https://example.org/fire'};
 const html=report.scientificReportMarkup({...draft,subsurfaceContext,fireContext},[],'overview','Captured sources and intervals');
 assert.match(html,/Recorded-depth columns/);assert.match(html,/data:image\/svg\+xml;charset=utf-8,/);assert.match(html,/gaps are unknown/);
 assert.match(html,/Provider event \/ acquisition/);assert.match(html,/2026-10-30/);assert.match(html,/not matched incidents/);
 const svg=decodeURIComponent(html.match(/src="data:image\/svg\+xml;charset=utf-8,([^"]+)/)[1]);assert.match(svg,/well-test/);assert.match(svg,/Unknown between observations/);
});
