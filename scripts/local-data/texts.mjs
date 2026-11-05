// Full-text search over the bulk archive's digitised texts: Chronicling America newspaper pages
// (Kansas titles, OCR) and Internet Archive public-domain Kansas texts. Both tables already carry
// an FTS5 index written by the PC's feeds (kfm_newspaper_pages_fts, kfm_ia_texts_fts); this
// dataset is the first question that uses them. The same pages and texts are already public, one
// record page at a time, through recovered-bulk (owner authorization 2026-11-03); search adds
// ranking, snippets and counts over them, never new fields. No dependencies.
//
// Cost model, measured on the PC's spinning data disk: a page's OCR row is about 20 KB, so a join
// from every match to its page row costs one random read per match (a common word matches 30,000
// pages: nearly two minutes cold). Ranking therefore uses the FTS index alone; dates, titles and
// places come from small catalogs held in memory per database (refreshed when the tables change);
// only the rows on the returned page are read from disk, for their snippets.
import {only,text,oneOf,day,ordered,flag,page,num,str,fail} from './query.mjs';

export const SEARCH_SOURCES=Object.freeze(['newspapers','texts']);
// Marks around each matched term in a snippet, so a reader can highlight without re-matching.
export const SNIPPET_OPEN='⟦',SNIPPET_CLOSE='⟧';
// The count stops here: a query matching more pages than this reports the cap, not every match.
export const TOTAL_CAP=10000;
const MAX_TERMS=8,MAX_QUERY_CHARS=200,FACET_TITLES=100;
const WORD=/^[\p{L}\p{N}'’-]{1,40}$/u,PHRASE=/^[\p{L}\p{N}'’-]{1,40}(?: [\p{L}\p{N}'’-]{1,40}){1,7}$/u,LETTER=/[\p{L}\p{N}]/u;
const OPERATORS=new Set(['AND','OR','NOT']);
const LCCN=/^[A-Z]{2}\d{8}$/,IDENTIFIER=/^[A-Za-z0-9._-]{1,100}$/;
const notReady=()=>Object.assign(new Error('DATASET_NOT_READY'),{code:'DATASET_NOT_READY'});

/**
 * Turns a visitor's search into an FTS5 MATCH expression built only from validated pieces:
 * words, "quoted phrases", a trailing * on words of three or more characters, and AND, OR,
 * NOT between terms. Column filters, NEAR, parentheses and bare punctuation are refused, so the
 * expression can neither error inside SQLite nor reach a column the catalog does not name.
 */
export function searchExpression(input){
 if(typeof input!=='string')throw fail();
 const q=input.replace(/[“”]/g,'"').trim();
 if(!q||q.length>MAX_QUERY_CHARS||/[\x00-\x1f\x7f]/.test(q))throw fail();
 const parts=[];let terms=0,expectTerm=true;
 const tokens=q.match(/"[^"]*"|\S+/g)??[];
 for(const token of tokens){
  const upper=token.toUpperCase();
  if(OPERATORS.has(upper)){
   if(expectTerm)throw fail();
   parts.push(upper);expectTerm=true;continue;
  }
  if(!expectTerm)parts.push('AND');
  if(token.startsWith('"')){
   const phrase=token.slice(1,-1).trim().replace(/\s+/g,' ');
   if(!PHRASE.test(phrase)||!LETTER.test(phrase))throw fail();
   parts.push('"'+phrase+'"');
  }else{
   const prefix=token.endsWith('*'),word=prefix?token.slice(0,-1):token;
   if(!WORD.test(word)||!LETTER.test(word)||prefix&&[...word].length<3)throw fail();
   parts.push('"'+word+'"'+(prefix?'*':''));
  }
  if(++terms>MAX_TERMS)throw fail();
  expectTerm=false;
 }
 if(expectTerm)throw fail();
 return parts.join(' ');
}

const SOURCE=Object.freeze({provider:'Library of Congress Chronicling America (Kansas titles) and Internet Archive public-domain Kansas texts',
 url:'/data-library',
 coverage:'Newspapers: OCR of the Kansas pages the PC\'s newspaper-text feed has loaded (1864–1960 at first release); texts: Internet Archive items whose text files have been loaded, oldest first. Not every Kansas newspaper or book; a missing match is not evidence of absence.',
 notes:'Ranked by SQLite FTS5 bm25 over the original OCR text, uncorrected: historical spellings, hyphenation and OCR errors affect matches. Snippets mark matched terms between ⟦ and ⟧. Counts stop at '+TOTAL_CAP+'. Newspaper coordinates are the title\'s place of publication, not where an event happened. Each page and text keeps its source link.'});

const dayOrYear=(v,fallback,{end=false}={})=>{
 if(v===undefined||v===null||v==='')return fallback;
 const s=String(v).trim();
 if(/^\d{4}$/.test(s))return day(s+(end?'-12-31':'-01-01'));
 return day(s);
};

/** A catalog built from one table, rebuilt only when the table's row count or last rowid changes. */
function catalog(db,cache,key,table,rowid,build){
 const stamp=db.prepare(`SELECT COUNT(*) AS n,MAX(${rowid}) AS m FROM ${table}`).get();
 const version=stamp.n+':'+stamp.m,held=cache.get('catalog:'+key);
 if(held&&held.version===version)return held.value;
 const value=build();
 cache.set('catalog:'+key,{version,value});
 return value;
}

function newspaperTitles(db,cache){
 return catalog(db,cache,'newspaper-titles','kfm_newspaper_titles','rowid',()=>{
  const titles=new Map();
  for(const r of db.prepare('SELECT lccn,title,place,location_json FROM kfm_newspaper_titles ORDER BY file_id,row_number').all()){
   let lat=null,lon=null;
   try{const ll=JSON.parse(r.location_json??'null')?.latlong;if(Array.isArray(ll)&&Number.isFinite(+ll[0])&&Number.isFinite(+ll[1])){lat=+ll[0];lon=+ll[1];}}catch{}
   titles.set(r.lccn,{title:str(r.title),place:str(r.place),lat,lon});
  }
  return titles;
 });
}
// page_rowid -> {lccn, issueDate}; read through the (lccn, issue_date, …) index, never the OCR rows.
const newspaperPages=(db,cache)=>catalog(db,cache,'newspaper-pages','kfm_newspaper_pages','page_rowid',()=>{
 const pages=new Map();
 for(const r of db.prepare('SELECT page_rowid AS id,lccn,issue_date AS issueDate FROM kfm_newspaper_pages').all())pages.set(r.id,{lccn:r.lccn,issueDate:r.issueDate});
 return pages;
});
const archiveTexts=(db,cache)=>catalog(db,cache,'ia-texts','kfm_ia_texts','text_rowid',()=>{
 const texts=new Map();
 for(const r of db.prepare('SELECT text_rowid AS id,identifier,part FROM kfm_ia_texts').all())texts.set(r.id,{identifier:r.identifier,part:r.part});
 return texts;
});
const archiveItems=(db,cache)=>catalog(db,cache,'ia-items','kfm_ia_items','rowid',()=>{
 const items=new Map();
 for(const r of db.prepare('SELECT identifier,title,creator,date,year,publisher FROM kfm_ia_items ORDER BY file_id,row_number').all())items.set(r.identifier,{title:str(r.title),creator:str(r.creator),date:str(r.date),year:num(r.year),publisher:str(r.publisher)});
 return items;
});

/** Ranked matches from the FTS index alone: [{id, rank}] in bm25 order. */
const ranked=(db,table,match)=>db.prepare(`SELECT rowid AS id,bm25(${table}) AS rank FROM ${table} WHERE ${table} MATCH ? ORDER BY rank`).all(match);
/** Snippets for the rows on one page: the only reads of the text rows themselves. */
function snippets(db,table,match,ids){
 if(!ids.length)return new Map();
 const rows=db.prepare(`SELECT rowid AS id,snippet(${table},0,?,?,'…',24) AS snippet FROM ${table} WHERE ${table} MATCH ? AND rowid IN (${ids.map(()=>'?').join(',')})`).all(SNIPPET_OPEN,SNIPPET_CLOSE,match,...ids);
 return new Map(rows.map(r=>[r.id,str(r.snippet)]));
}
function facetsOf(hits,meta,yearOf,titleOf){
 const years=new Map(),titles=new Map();
 for(const h of hits){const m=meta.get(h.id),y=yearOf(m),t=titleOf(m);years.set(y,(years.get(y)??0)+1);titles.set(t,(titles.get(t)??0)+1);}
 return {years:[...years].sort((a,b)=>a[0]-b[0]).map(([year,hits])=>({year,hits})),
  titles:[...titles].sort((a,b)=>b[1]-a[1]||(a[0]<b[0]?-1:1)).slice(0,FACET_TITLES).map(([id,hits])=>({id,hits}))};
}

export const archiveSearch={
 id:'archive-search',db:'bulk',freshness:{tables:['kfm_newspaper_pages','kfm_ia_texts']},title:'Archive text search',indexes:[],source:SOURCE,
 params:{q:'words, "quoted phrases", word* prefixes and AND/OR/NOT; at most 8 terms (required)',source:'newspapers or texts (required)',
  from:'YYYY or YYYY-MM-DD (newspapers: issue date; texts: publication year)',to:'YYYY or YYYY-MM-DD',
  title:'one title: newspaper LCCN (e.g. sn84029386) or Internet Archive identifier',facets:'1 adds hits by year and by title',limit:'1-50 (20)',offset:'0-1000'},
 parse(input){
  only(input,['q','source','from','to','title','facets','limit','offset']);
  const source=oneOf(input.source,SEARCH_SOURCES,{required:true});
  const q={q:String(input.q??'').trim(),match:searchExpression(input.q),source,from:dayOrYear(input.from,'1700-01-01'),to:dayOrYear(input.to,'2100-12-31',{end:true}),
   title:source==='newspapers'?text(input.title,LCCN)?.toLowerCase()??null:text(input.title,IDENTIFIER,{upper:false}),
   facets:flag(input.facets),...page(input,{max:50,fallback:20,maxOffset:1000})};
  ordered(q.from,q.to);return q;
 },
 run(db,q,{cache}){
  const table=q.source==='newspapers'?'kfm_newspaper_pages_fts':'kfm_ia_texts_fts';
  if(!cache.get('ready:'+table)){
   if(!db.prepare("SELECT 1 FROM sqlite_master WHERE type='table' AND name=?").get(table))throw notReady();
   cache.set('ready:'+table,true);
  }
  const dated=q.from!=='1700-01-01'||q.to!=='2100-12-31';
  const matches=ranked(db,table,q.match);
  if(q.source==='newspapers'){
   const pages=newspaperPages(db,cache),titles=newspaperTitles(db,cache);
   const hits=matches.filter(m=>{const p=pages.get(m.id);return p&&(!dated||p.issueDate>=q.from&&p.issueDate<=q.to)&&(!q.title||p.lccn===q.title);});
   const shown=hits.slice(q.offset,q.offset+q.limit),texts=snippets(db,table,q.match,shown.map(h=>h.id));
   const detail=db.prepare('SELECT page_rowid AS id,edition,sequence,page_url,char_count FROM kfm_newspaper_pages WHERE page_rowid=?');
   const answer={total:Math.min(hits.length,TOTAL_CAP),totalCapped:hits.length>TOTAL_CAP,
    rows:shown.map(h=>{const p=pages.get(h.id),t=titles.get(p.lccn)??{},d=detail.get(h.id)??{};
     return {id:'page:'+h.id,source:'newspapers',lccn:p.lccn,title:t.title??null,place:t.place??null,lat:t.lat??null,lon:t.lon??null,issueDate:p.issueDate,
      edition:num(d.edition),sequence:num(d.sequence),pageUrl:str(d.page_url),characters:num(d.char_count),snippet:texts.get(h.id)??null,rank:num(h.rank)};})};
   if(q.facets){
    const f=facetsOf(hits,pages,p=>+p.issueDate.slice(0,4),p=>p.lccn);
    answer.facets={years:f.years,titles:f.titles.map(t=>({id:t.id,title:titles.get(t.id)?.title??null,place:titles.get(t.id)?.place??null,hits:t.hits}))};
   }
   return answer;
  }
  const texts=archiveTexts(db,cache),items=archiveItems(db,cache);
  const hits=matches.filter(m=>{const x=texts.get(m.id);if(!x)return false;const year=items.get(x.identifier)?.year??null;
   return (!dated||year!==null&&year>=+q.from.slice(0,4)&&year<=+q.to.slice(0,4))&&(!q.title||x.identifier===q.title);});
  const shown=hits.slice(q.offset,q.offset+q.limit),parts=snippets(db,table,q.match,shown.map(h=>h.id));
  const detail=db.prepare('SELECT char_count FROM kfm_ia_texts WHERE text_rowid=?');
  const answer={total:Math.min(hits.length,TOTAL_CAP),totalCapped:hits.length>TOTAL_CAP,
   rows:shown.map(h=>{const x=texts.get(h.id),i=items.get(x.identifier)??{};
    return {id:'text:'+h.id,source:'texts',identifier:x.identifier,title:i.title??null,creator:i.creator??null,date:i.date??null,year:i.year??null,publisher:i.publisher??null,part:num(x.part),
     itemUrl:'https://archive.org/details/'+encodeURIComponent(x.identifier),characters:num(detail.get(h.id)?.char_count),snippet:parts.get(h.id)??null,rank:num(h.rank)};})};
  if(q.facets){
   const f=facetsOf(hits,texts,x=>items.get(x.identifier)?.year??null,x=>x.identifier);
   answer.facets={years:f.years,titles:f.titles.map(t=>({id:t.id,title:items.get(t.id)?.title??null,place:null,hits:t.hits}))};
  }
  return answer;
 },
};
