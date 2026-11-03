import test from 'node:test';
import assert from 'node:assert/strict';
import {RECOVERED_COLLECTIONS,recoveredObservations,recoveredBulk} from '../scripts/local-data/recovered.mjs';
import {c,fixture} from './recovered-fixtures.mjs';
test('all recovered domain tables are represented without publishing operational schemas',()=>{
 assert.equal(RECOVERED_COLLECTIONS.length,189);assert.equal(new Set(RECOVERED_COLLECTIONS.map(c=>c.id)).size,189);
 assert.equal(RECOVERED_COLLECTIONS.filter(c=>c.geometry).length,56);
 for(const c of RECOVERED_COLLECTIONS){assert.ok(c.keys.length);assert.ok(c.keys.every(k=>c.columns.includes(k)));assert.ok(!/kfm_sql_|kfm_feed_state|_fts/.test(c.table));assert.ok(!c.columns.includes('source_path'));}
 assert.ok(RECOVERED_COLLECTIONS.some(c=>c.table==='kfm_storm_event_fatalities'));
 assert.ok(RECOVERED_COLLECTIONS.some(c=>c.table==='kfm_newspaper_pages'));
});
test('primary-key pages cover large keys without overlap, offsets, truncation or fabricated totals',t=>{
 const db=fixture(t),a=recoveredObservations.run(db,recoveredObservations.parse({collection:c.id,limit:'2'}));
 assert.equal(a.total,null);assert.equal(a.hasMore,true);assert.equal(a.rows.length,2);
 const b=recoveredObservations.run(db,recoveredObservations.parse({collection:c.id,after:a.nextCursor,limit:'2'}));
 assert.equal(b.rows.length,1);assert.equal(b.rows[0].values.row_number,100000001);assert.equal(b.hasMore,false);assert.equal(b.nextCursor,null);
 assert.equal(Number(a.rows[0].values.quantity),0);assert.equal(a.rows[1].values.quantity,null);
 assert.equal(a.rows[0].provenance.source_id,'faa-obstacles');assert.ok(!JSON.stringify(a).includes('/private/'));
 const plan=db.prepare(`EXPLAIN QUERY PLAN SELECT city FROM ${c.table} WHERE (file_id,row_number)>(?,?) ORDER BY file_id,row_number LIMIT ?`).all(1,2,20);
 assert.match(plan.map(p=>p.detail).join(' '),/SEARCH.*PRIMARY KEY/);
 assert.doesNotMatch(plan.map(p=>p.detail).join(' '),/TEMP B-TREE/);
});
test('query boundary rejects arbitrary tables, SQL, cross-database collections and malformed cursors',()=>{
 for(const q of [{collection:'kfm_sql_sources'},{collection:c.id,table:c.table},{collection:c.id,sql:'DROP TABLE x'},{collection:c.id,limit:51},{collection:c.id,offset:100},{collection:c.id,after:'[null,1]'},{collection:c.id,after:'[1]'},{collection:c.id,after:'[1,{}]'},{collection:c.id,after:'x'},{collection:c.id,after:'[1,9007199254740992]'}])assert.throws(()=>recoveredObservations.parse(q),{code:'QUERY_INVALID'});
 assert.throws(()=>recoveredBulk.parse({collection:c.id}),{code:'QUERY_INVALID'});
});
test('cursor strings are bound values, never executable SQL',t=>{
 const db=fixture(t);const q=recoveredObservations.parse({collection:c.id,after:JSON.stringify(["1); DROP TABLE kfm_faa_obstacles; --",2])});
 recoveredObservations.run(db,q);assert.equal(db.prepare('SELECT COUNT(*) n FROM kfm_faa_obstacles').get().n,3);
});
test('a large text field stays accessible without blocking pagination or silently losing its content',t=>{
 const db=fixture(t),original='é🌾'.repeat(180000);
 db.prepare('UPDATE kfm_faa_obstacles SET city=? WHERE row_number=1').run(original);
 const a=recoveredObservations.run(db,recoveredObservations.parse({collection:c.id,limit:1}));
 assert.equal(a.rows[0].values.city.longField,true);assert.ok(Buffer.byteLength(JSON.stringify(a))<650000);assert.ok(a.nextCursor);
 let start=0,parts=[];
 do{const part=recoveredObservations.run(db,recoveredObservations.parse({collection:c.id,record:a.rows[0].id,field:'city',start}));parts.push(part.rows[0].values.city);start=part.fieldChunk.nextStart;}while(start!==null);
 assert.equal(parts.join(''),original);
 assert.throws(()=>recoveredObservations.parse({collection:c.id,record:a.rows[0].id,field:'source_path'}),{code:'QUERY_INVALID'});
});
