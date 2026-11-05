import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {archiveSearch,searchExpression,SNIPPET_OPEN,SNIPPET_CLOSE,TOTAL_CAP} from '../scripts/local-data/texts.mjs';
import {DATASETS} from '../scripts/local-data/datasets.mjs';
import {LOCAL_DATA_ROUTES} from '../scripts/local-data/protocol.mjs';

// The bulk database's shape for the two text feeds: content tables with an INTEGER PRIMARY KEY and
// an external-content FTS5 index over the text column, as tools/local_data/sql_feed_bulk.py and
// sql_feed_texts.py write them.
function fixture(t,{fts=true}={}){
 const db=new DatabaseSync(':memory:');t.after(()=>db.close());
 db.exec(`
  CREATE TABLE kfm_newspaper_pages (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, page_rowid INTEGER PRIMARY KEY,
   lccn TEXT NOT NULL, issue_date TEXT NOT NULL, edition INTEGER NOT NULL, sequence INTEGER NOT NULL, page_url TEXT NOT NULL, ocr_text TEXT NOT NULL, char_count INTEGER NOT NULL);
  CREATE TABLE kfm_newspaper_titles (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, lccn TEXT NOT NULL, title TEXT, place TEXT, location_json TEXT, PRIMARY KEY(file_id,row_number));
  INSERT INTO kfm_newspaper_titles VALUES(1,1,'sn84029386','Abilene Weekly Reflector (Abilene, Kan.) 1888-1935','Abilene, Kansas','{"latlong":[38.9173235,-97.2139196]}'),
   (1,2,'ca06001655','The Indian Leader (Lawrence, Kan.) 1897-????','Lawrence, Kansas','{"latlong":["38.97","-95.24"]}'),(1,3,'sn85032585','The Wichita Searchlight','Wichita, Kansas','not json');
  INSERT INTO kfm_newspaper_pages VALUES
   (2,1,11,'sn84029386','1903-05-28',1,12,'https://chroniclingamerica.loc.gov/lccn/sn84029386/1903-05-28/ed-1/seq-12/','TERRIBLE TORNADO. Southern Nebraska visited by a tornado; the cyclone wrecked barns.',90),
   (2,2,12,'sn84029386','1918-04-25',1,4,'https://chroniclingamerica.loc.gov/lccn/sn84029386/1918-04-25/ed-1/seq-4/','For every $100 bond you subscribe. Railroad conference in Chicago.',70),
   (2,3,13,'ca06001655','1904-03-25',1,4,'https://chroniclingamerica.loc.gov/lccn/ca06001655/1904-03-25/ed-1/seq-4/','The grasshopper people were once much larger. A tornado is mentioned once.',80),
   (2,4,14,'sn85032585','1907-05-04',1,1,'https://chroniclingamerica.loc.gov/lccn/sn85032585/1907-05-04/ed-1/seq-1/','Wichita University at Wichita, Kans. Haskell lost.',55);
  CREATE TABLE kfm_ia_items (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, identifier TEXT NOT NULL, title TEXT, creator TEXT, date TEXT, year INTEGER, publisher TEXT, PRIMARY KEY(file_id,row_number));
  INSERT INTO kfm_ia_items VALUES(3,1,'speechofhonsadou00doug','Speech of Hon. S. A. Douglas','Douglas, Stephen A.','1854-01-01T00:00:00Z',1854,'Washington'),(3,2,'laws1868kans','General laws of Kansas 1868',NULL,NULL,1868,NULL);
  CREATE TABLE kfm_ia_texts (file_id INTEGER NOT NULL, row_number INTEGER NOT NULL, text_rowid INTEGER PRIMARY KEY, identifier TEXT NOT NULL, file_name TEXT NOT NULL, part INTEGER NOT NULL, text TEXT NOT NULL, char_count INTEGER NOT NULL);
  INSERT INTO kfm_ia_texts VALUES(4,1,21,'speechofhonsadou00doug','speech_djvu.txt',1,'It is true that, in the midst of the tornado which swept over the land.',70),
   (4,2,22,'laws1868kans','laws_djvu.txt',3,'An act concerning railroad bonds and county bonds.',50),(4,3,23,'laws1868kans','laws_djvu.txt',4,'Nothing of note here.',21);`);
 if(fts)db.exec(`
  CREATE VIRTUAL TABLE kfm_newspaper_pages_fts USING fts5(ocr_text, content='kfm_newspaper_pages', content_rowid='page_rowid');
  INSERT INTO kfm_newspaper_pages_fts(rowid,ocr_text) SELECT page_rowid,ocr_text FROM kfm_newspaper_pages;
  CREATE VIRTUAL TABLE kfm_ia_texts_fts USING fts5(text, content='kfm_ia_texts', content_rowid='text_rowid');
  INSERT INTO kfm_ia_texts_fts(rowid,text) SELECT text_rowid,text FROM kfm_ia_texts;`);
 return db;
}
const run=(db,input)=>archiveSearch.run(db,archiveSearch.parse(input),{cache:new Map()});

test('the search language is rebuilt from validated terms, never passed through to FTS5',()=>{
 assert.equal(searchExpression('tornado'),'"tornado"');
 assert.equal(searchExpression('  dust   storm '),'"dust" AND "storm"');
 assert.equal(searchExpression('"dust storm" railroad'),'"dust storm" AND "railroad"');
 assert.equal(searchExpression('“dust  storm”'),'"dust storm"');
 assert.equal(searchExpression('wich* NOT university'),'"wich"* NOT "university"');
 assert.equal(searchExpression('cyclone or Tornado and 1903'),'"cyclone" OR "Tornado" AND "1903"');
 assert.equal(searchExpression("o'neill ’tis"),'"o\'neill" AND "’tis"');
 for(const bad of ['','   ','ocr_text:tornado','NEAR(a b)','(tornado)','tornado OR','AND tornado','a OR OR b','ab*','"a"','""','t"ornado','x'.repeat(201),'a b c d e f g h i','tornado;','--',"'",'"- -"','\u0007','{col} : x','word^2','a, b','"unterminated'])
  assert.throws(()=>searchExpression(bad),{code:'QUERY_INVALID'},JSON.stringify(bad));
});

test('parse bounds every parameter and the catalog names the route',()=>{
 assert.equal(DATASETS.get('archive-search'),archiveSearch);
 assert.equal(LOCAL_DATA_ROUTES.get('/v1/data/archive-search'),'POST');
 const q=archiveSearch.parse({q:'tornado',source:'Newspapers',from:'1900',to:'1905-06-30',title:'SN84029386',facets:'1',limit:'5'});
 assert.deepEqual(q,{q:'tornado',match:'"tornado"',source:'newspapers',from:'1900-01-01',to:'1905-06-30',title:'sn84029386',facets:true,limit:5,offset:0});
 assert.deepEqual(archiveSearch.parse({q:'bonds',source:'texts',to:'1870',title:'laws1868kans'}),{q:'bonds',match:'"bonds"',source:'texts',from:'1700-01-01',to:'1870-12-31',title:'laws1868kans',facets:false,limit:20,offset:0});
 for(const bad of [{q:'tornado'},{source:'newspapers'},{q:'tornado',source:'both'},{q:'tornado',source:'newspapers',limit:'51'},{q:'tornado',source:'newspapers',offset:'1001'},
  {q:'tornado',source:'newspapers',from:'1905',to:'1900'},{q:'tornado',source:'newspapers',title:'sn8402938'},{q:'tornado',source:'texts',title:'a b'},{q:'tornado',source:'newspapers',sql:'1'},{q:'tornado',source:'newspapers',from:'18'}])
  assert.throws(()=>archiveSearch.parse(bad),{code:'QUERY_INVALID'},JSON.stringify(bad));
});

test('newspaper hits come ranked with marked snippets, the title\'s place, source links and a bounded total',t=>{
 const db=fixture(t),a=run(db,{q:'tornado',source:'newspapers',facets:'1'});
 assert.equal(a.total,2);assert.equal(a.totalCapped,false);assert.equal(a.rows.length,2);
 assert.equal(a.rows[0].lccn,'sn84029386');// two mentions outrank one
 assert.deepEqual(Object.keys(a.rows[0]),['id','source','lccn','title','place','lat','lon','issueDate','edition','sequence','pageUrl','characters','snippet','rank']);
 assert.equal(a.rows[0].id,'page:11');assert.equal(a.rows[0].place,'Abilene, Kansas');assert.equal(a.rows[0].lat,38.9173235);assert.equal(a.rows[0].lon,-97.2139196);
 assert.match(a.rows[0].pageUrl,/^https:\/\/chroniclingamerica\.loc\.gov\//);
 assert.ok(a.rows[0].snippet.includes(SNIPPET_OPEN+'TORNADO'+SNIPPET_CLOSE)||a.rows[0].snippet.includes(SNIPPET_OPEN+'tornado'+SNIPPET_CLOSE));
 assert.ok(a.rows[0].rank<a.rows[1].rank);
 // String coordinates in the directory still decode; unparseable location JSON leaves them null.
 assert.equal(a.rows[1].lat,38.97);
 assert.deepEqual(a.facets.years,[{year:1903,hits:1},{year:1904,hits:1}]);
 assert.deepEqual(a.facets.titles,[{id:'ca06001655',title:'The Indian Leader (Lawrence, Kan.) 1897-????',place:'Lawrence, Kansas',hits:1},{id:'sn84029386',title:'Abilene Weekly Reflector (Abilene, Kan.) 1888-1935',place:'Abilene, Kansas',hits:1}]);
 const w=run(db,{q:'wichita',source:'newspapers'});assert.equal(w.rows[0].lat,null);assert.equal(w.rows[0].place,'Wichita, Kansas');
 assert.equal(run(db,{q:'nothing-here-xyz',source:'newspapers',facets:'1'}).total,0);
});

test('date, title, phrase, prefix and operator filters narrow newspaper hits; offset pages through them',t=>{
 const db=fixture(t);
 assert.deepEqual(run(db,{q:'tornado',source:'newspapers',from:'1904',to:'1904'}).rows.map(r=>r.issueDate),['1904-03-25']);
 assert.deepEqual(run(db,{q:'tornado',source:'newspapers',from:'1903-05-28',to:'1903-05-28'}).rows.map(r=>r.issueDate),['1903-05-28']);
 assert.equal(run(db,{q:'tornado',source:'newspapers',title:'ca06001655'}).rows[0].id,'page:13');
 assert.equal(run(db,{q:'"terrible tornado"',source:'newspapers'}).total,1);
 assert.equal(run(db,{q:'"tornado terrible"',source:'newspapers'}).total,0);
 assert.equal(run(db,{q:'grassh*',source:'newspapers'}).total,1);
 assert.equal(run(db,{q:'tornado NOT cyclone',source:'newspapers'}).rows[0].id,'page:13');
 assert.equal(run(db,{q:'cyclone OR bond',source:'newspapers'}).total,2);
 assert.equal(run(db,{q:'tornado',source:'newspapers',limit:'1',offset:'1'}).rows[0].id,'page:13');
 assert.deepEqual(run(db,{q:'tornado',source:'newspapers',limit:'1',offset:'5'}).rows,[]);
});

test('archive texts search their item record, publication year and archive.org link',t=>{
 const db=fixture(t),a=run(db,{q:'bonds',source:'texts',facets:'1'});
 assert.equal(a.total,1);assert.equal(a.rows[0].id,'text:22');assert.equal(a.rows[0].identifier,'laws1868kans');assert.equal(a.rows[0].part,3);
 assert.equal(a.rows[0].itemUrl,'https://archive.org/details/laws1868kans');assert.equal(a.rows[0].title,'General laws of Kansas 1868');assert.equal(a.rows[0].creator,null);
 assert.ok(a.rows[0].snippet.includes(SNIPPET_OPEN+'bonds'+SNIPPET_CLOSE));
 assert.deepEqual(a.facets,{years:[{year:1868,hits:1}],titles:[{id:'laws1868kans',title:'General laws of Kansas 1868',place:null,hits:1}]});
 assert.equal(run(db,{q:'tornado',source:'texts'}).rows[0].year,1854);
 assert.equal(run(db,{q:'tornado',source:'texts',from:'1860'}).total,0);
 assert.equal(run(db,{q:'tornado',source:'texts',title:'laws1868kans'}).total,0);
});

test('the count stops at the cap and the dataset is refused without its FTS index',t=>{
 const db=fixture(t);
 const insert=db.prepare('INSERT INTO kfm_newspaper_pages VALUES(9,?,?,?,?,1,1,?,?,20)'),fts=db.prepare('INSERT INTO kfm_newspaper_pages_fts(rowid,ocr_text) VALUES(?,?)');
 for(let i=0;i<TOTAL_CAP+5;i++){const id=1000+i;insert.run(i,id,'sn84029386','1920-01-01','https://example.org/'+id,'flood level');fts.run(id,'flood level');}
 const a=run(db,{q:'flood',source:'newspapers',limit:'50'});
 assert.equal(a.total,TOTAL_CAP);assert.equal(a.totalCapped,true);assert.equal(a.rows.length,50);
 assert.throws(()=>run(fixture(t,{fts:false}),{q:'flood',source:'newspapers'}),{code:'DATASET_NOT_READY'});
 assert.throws(()=>run(fixture(t,{fts:false}),{q:'flood',source:'texts'}),{code:'DATASET_NOT_READY'});
});

test('catalogs held between questions refresh when the feed adds or replaces rows',t=>{
 const db=fixture(t),cache=new Map();
 const ask=input=>archiveSearch.run(db,archiveSearch.parse(input),{cache});
 assert.equal(ask({q:'tornado',source:'newspapers',from:'1950'}).total,0);
 db.exec(`INSERT INTO kfm_newspaper_pages VALUES(5,1,15,'sn84029386','1955-06-01',1,2,'https://example.org/15','A tornado in 1955.',18);INSERT INTO kfm_newspaper_pages_fts(rowid,ocr_text) VALUES(15,'A tornado in 1955.');`);
 assert.deepEqual(ask({q:'tornado',source:'newspapers',from:'1950'}).rows.map(r=>r.id),['page:15']);
 assert.equal(ask({q:'tornado',source:'newspapers',from:'1950'}).rows[0].place,'Abilene, Kansas');
 db.exec(`DELETE FROM kfm_newspaper_titles WHERE lccn='sn84029386';INSERT INTO kfm_newspaper_titles VALUES(6,1,'sn84029386','Abilene Reflector','Abilene, Kansas','{"latlong":[38.9,-97.2]}');`);
 assert.equal(ask({q:'tornado',source:'newspapers',from:'1950'}).rows[0].title,'Abilene Reflector');
 // A page the feed removed stays out even while its FTS entry lingers.
 db.exec(`DELETE FROM kfm_newspaper_pages WHERE page_rowid=15;`);
 assert.equal(ask({q:'tornado',source:'newspapers',from:'1950'}).total,0);
});

test('search terms are bound values: quoting, SQL and FTS syntax in a term cannot change the statement',t=>{
 const db=fixture(t);
 assert.throws(()=>run(db,{q:"tornado' OR 1=1 --",source:'newspapers'}),{code:'QUERY_INVALID'});
 assert.throws(()=>run(db,{q:'tornado"',source:'newspapers'}),{code:'QUERY_INVALID'});
 assert.throws(()=>run(db,{q:'"drop table kfm_newspaper_pages"',source:'newspapers'}),{code:'QUERY_INVALID'});
 assert.equal(run(db,{q:'"drop table newspaper pages"',source:'newspapers'}).total,0);
 assert.equal(run(db,{q:'tornado OR "0 OR 1"',source:'newspapers'}).total,2);
 assert.equal(db.prepare('SELECT COUNT(*) n FROM kfm_newspaper_pages').get().n,4);
});
