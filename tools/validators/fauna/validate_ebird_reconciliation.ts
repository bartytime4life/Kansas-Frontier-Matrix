#!/usr/bin/env -S node
import fs from 'fs';
const p = process.argv[2];
if (!p) { console.error('usage: validate_ebird_reconciliation <report.json>'); process.exit(2); }
const j = JSON.parse(fs.readFileSync(p,'utf8'));
if (j.object_type !== 'EbirdGlobalInvariantReport') { console.error('invalid object_type'); process.exit(2); }
if (!Array.isArray(j.invariants) || j.invariants.length < 40) { console.error('missing invariants'); process.exit(2); }
console.log('ok');
