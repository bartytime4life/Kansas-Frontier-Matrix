#!/usr/bin/env -S node
import fs from 'fs';
const path=process.argv[2]; if(!path){console.error('usage: validate_ebird_audit_response <json>');process.exit(2)}
const t=fs.readFileSync(path,'utf8');
if(t.includes('population trend') && !t.includes('not a population trend')){console.error('unsupported inference claim');process.exit(1)}
if(t.includes('restricted/')||t.includes('/quarantine/')){console.error('restricted path leaked');process.exit(1)}
console.log(JSON.stringify({validator:'validate_ebird_audit_response',status:'pass'}));
