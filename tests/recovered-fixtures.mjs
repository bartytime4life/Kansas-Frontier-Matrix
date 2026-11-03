import {DatabaseSync} from 'node:sqlite';
import {RECOVERED_COLLECTIONS} from '../scripts/local-data/recovered.mjs';
export const c=RECOVERED_COLLECTIONS.find(c=>c.id==='observations-faa-obstacles');

export function fixture(t){
 const db=new DatabaseSync(':memory:');t.after(()=>db.close());
 db.exec(`CREATE TABLE "${c.table}"(${c.columns.map(k=>`"${k}" ${c.keys.includes(k)?'INTEGER NOT NULL':'TEXT'}`).join(',')},PRIMARY KEY(${c.keys.join(',')})) WITHOUT ROWID;
 CREATE TABLE kfm_sql_sources(file_id INTEGER PRIMARY KEY,source_id TEXT,source_url TEXT,sha256 TEXT,source_path TEXT);
 INSERT INTO kfm_sql_sources VALUES(1,'faa-obstacles','https://example.org/public','hash','/private/operational/path');`);
 const insert=db.prepare(`INSERT INTO "${c.table}"(file_id,row_number,city,quantity,geometry_geojson) VALUES(?,?,?,?,?)`);
 insert.run(1,1,'Wichita',0,'{"type":"Point","coordinates":[-97.3,37.6]}');
 insert.run(1,2,'Salina',null,'{"type":"Point","coordinates":[-97.6,38.8]}');
 insert.run(1,100000001,'Dodge City',3,'{"type":"Point","coordinates":[-100,37.8]}');
 return db;
}
