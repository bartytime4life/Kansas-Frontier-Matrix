import assert from 'node:assert/strict';
import test from 'node:test';
import {z} from 'zod';
import {fromZodError} from 'zod-validation-error';

// Tiny local collections expose the upstream early-size-gate regression without
// generating resource exhaustion or submitting data to any application server.
for(const bound of ['max','length']){
 test(`Zod array ${bound} rejects oversize before parsing any element`,()=>{
  let visited=0;
  const element=z.preprocess(value=>{visited++;return value;},z.string());
  const schema=z.array(element)[bound](2),result=schema.safeParse(['a','b','c']);
  assert.equal(result.success,false);assert.equal(result.error.issues.length,1);
  assert.equal(result.error.issues[0].code,'too_big');assert.equal(visited,0);
 });
}
test('Zod Set max rejects oversize before parsing any element',()=>{
 let visited=0;
 const element=z.preprocess(value=>{visited++;return value;},z.string());
 const result=z.set(element).max(1).safeParse(new Set(['a','b']));
 assert.equal(result.success,false);assert.equal(result.error.issues.length,1);
 assert.equal(result.error.issues[0].code,'too_big');assert.equal(visited,0);
});
test('Zod Map max rejects oversize before parsing keys or values',()=>{
 let visited=0;
 const element=z.preprocess(value=>{visited++;return value;},z.string());
 const result=z.map(element,element).max(1).safeParse(new Map([['a','x'],['b','y']]));
 assert.equal(result.success,false);assert.equal(result.error.issues.length,1);
 assert.equal(result.error.issues[0].code,'too_big');assert.equal(visited,0);
});
test('ordinary constrained collections retain their values',()=>{
 assert.deepEqual(z.array(z.string()).max(2).parse(['a','b']),['a','b']);
 assert.deepEqual([...z.set(z.string()).max(2).parse(new Set(['a','b']))],['a','b']);
 assert.deepEqual([...z.map(z.string(),z.number()).max(2).parse(new Map([['a',1]]))],[['a',1]]);
});
test('nested errors remain compatible with the existing error formatter',()=>{
 const result=z.object({tags:z.array(z.string()).max(2)}).safeParse({tags:['a',42]});
 assert.equal(result.success,false);assert.deepEqual(result.error.issues[0].path,['tags',1]);
 assert.match(fromZodError(result.error).message,/tags/);
});
