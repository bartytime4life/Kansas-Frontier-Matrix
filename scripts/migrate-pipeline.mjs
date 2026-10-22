import { readFile } from 'node:fs/promises';
import { sha, canonical } from '../server/pipeline-contract.mjs';
import { getPipelineStore } from '../server/pipeline-store.mjs';
const sql = await readFile(new URL('../server/pipeline-schema.sql', import.meta.url), 'utf8');
const digest = sha(sql);
if (!process.argv.includes('--apply')) console.log(canonical({ mode: 'review-only', sha256: digest, initialState: 'paused', sql }));
else {
  if (process.env.KFM_MIGRATION_SHA256 !== digest || process.env.KFM_PIPELINE_DATABASE_BACKUP_VERIFIED !== 'true') throw new Error('Exact SQL digest and verified shared-database backup required.');
  const store = await getPipelineStore();
  try {
    for (const query of sql.replace(/--[^\n]*/g, '').split(';').map(v => v.trim()).filter(Boolean)) await store.pool.query(query);
    await store.ready(); console.log(canonical({ state: 'schema-verified', paused: (await store.status()).paused }));
  } finally { await store.pool.end(); }
}
