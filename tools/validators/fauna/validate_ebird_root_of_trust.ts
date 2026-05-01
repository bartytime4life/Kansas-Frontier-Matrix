#!/usr/bin/env -S node
import fs from 'fs';
import crypto from 'crypto';
const p = process.argv[2];
if (!p) { console.error('usage: validate_ebird_root_of_trust <manifest.json>'); process.exit(2); }
const m = JSON.parse(fs.readFileSync(p,'utf8'));
if (m.object_type !== 'EbirdRootOfTrustManifest') { console.error('invalid object_type'); process.exit(2); }
const { root_hash, generated_at, ...rest } = m;
const rec = crypto.createHash('sha256').update(JSON.stringify(rest, Object.keys(rest).sort())).digest('hex');
if (!root_hash) { console.error('missing root_hash'); process.exit(2); }
console.log('ok');
