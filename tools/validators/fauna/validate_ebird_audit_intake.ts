#!/usr/bin/env -S node
import fs from 'fs';
const path=process.argv[2]; if(!path){console.error('usage: validate_ebird_audit_intake <json>');process.exit(2)}
const t=fs.readFileSync(path,'utf8');
const denied=['decimalLatitude','decimalLongitude','suppression_receipt_path','suppressed_group_hash'];
for(const d of denied){if(t.includes(d)){console.error(`denied field: ${d}`);process.exit(1)}}
console.log(JSON.stringify({validator:'validate_ebird_audit_intake',status:'pass'}));
