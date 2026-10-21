import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {spawnSync} from 'node:child_process';
import {isIP} from 'node:net';

// Run only the inventory's actual redactor, without collecting host inventory.
const script=readFileSync(new URL('../scripts/home-inference/inventory.sh',import.meta.url),'utf8');
const redactor=script.match(/^redact\(\) \{[\s\S]*?^\}/m)?.[0];
assert.ok(redactor,'inventory defines its redactor');
function redact(input){
 const result=spawnSync('bash',['-c','export LC_ALL=C\n'+redactor+'\nredact'],{input,encoding:'utf8'});
 assert.equal(result.status,0,result.stderr);return result.stdout;
}

test('inventory redacts compressed, expanded, scoped and mixed IPv6 in socket and DNS output',()=>{
 const cases=[
  ['[2001:db8::1234]:8787','[<ip6>]:8787'],
  ['Current DNS Server: ::2','Current DNS Server: <ip6>'],
  ['DNS Servers: ::abcd ::ffff','DNS Servers: <ip6> <ip6>'],
  ['DNS Servers: 2001:db8:0:1:2:3:4:5','DNS Servers: <ip6>'],
  ['DNS Servers: 20:01:0d:b8:00:00:00:01','DNS Servers: <ip6>'],
  ['[fe80::cafe%enp3s0]:53','[<ip6>%enp3s0]:53'],
  ['DNS Servers: fd12:3456:789a::/64','DNS Servers: <ip6>/64'],
  ['[::ffff:192.0.2.128]:443','[<ip6>]:443'],
  ['DNS Servers: ::1.2.3.4','DNS Servers: <ip6>'],
  ['DNS Servers: 0:0:0:0:0:ffff:192.0.2.128','DNS Servers: <ip6>'],
  ['DNS Servers: 2001:DB8::ABCD 2001:db8::','DNS Servers: <ip6> <ip6>'],
 ];
 assert.deepEqual(redact(cases.map(([input])=>input).join('\n')+'\n').trimEnd().split('\n'),cases.map(([,output])=>output));
});

test('inventory preserves loopback and wildcard listeners, ports and ordinary diagnostics',()=>{
 const lines=['[::1]:11434','[::]:8787','127.0.0.1:11434','0.0.0.0:8787','Current DNS Server: ::1','time 12:34:56','driver 550.54.14'];
 const output=redact([...lines,'host 192.0.2.5','mac aa:bb:cc:dd:ee:ff','UUID=12345678-abcd-1234-abcd-123456789abc','Serial Number: synthetic','API_TOKEN=synthetic'].join('\n')+'\n');
 const actual=output.trimEnd().split('\n');
 // The existing redactor normalizes a bare IPv6 loopback into bracket notation.
 assert.deepEqual(actual.slice(0,lines.length),[...lines.slice(0,4),'Current DNS Server: [::1]',...lines.slice(5)]);
 assert.deepEqual(actual.slice(lines.length),['host <ip>','mac <mac>','UUID: <redacted>','Serial Number: <redacted>','API_TOKEN=<redacted>']);
});

test('inventory covers every IPv6 zero-run position without leaking listener address fragments',()=>{
 const addresses=new Set();
 const hextets=['2001','db8','12','34','56','78','9abc','def0'];
 for(let start=0;start<8;start++)for(let length=1;length<=8-start;length++){
  if(length===8)continue; // The unspecified listener is intentionally preserved.
  const parts=hextets.map((part,i)=>i>=start&&i<start+length?'0':part);
  const expanded=parts.map(part=>part.padStart(4,'0')).join(':');
  const compressed=parts.slice(0,start).join(':')+'::'+parts.slice(start+length).join(':');
  addresses.add(expanded);addresses.add(compressed);addresses.add(compressed.toUpperCase());
 }
 for(const address of ['::192.0.2.128','::ffff:0:192.0.2.128','2001:db8::192.0.2.128','2001:db8:1:2:3:4:192.0.2.128'])addresses.add(address);
 for(const address of addresses)assert.equal(isIP(address),6,address);
 const input=[...addresses].map(address=>`[${address}]:8787`).join('\n')+'\n';
 assert.deepEqual(redact(input).trimEnd().split('\n'),[...addresses].map(()=>'[<ip6>]:8787'));
});
