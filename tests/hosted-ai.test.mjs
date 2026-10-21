import test from 'node:test';
import assert from 'node:assert/strict';

test('continuation novelty distinguishes repeated paragraphs from new detail about the same subject',async()=>{
 const {repeatsPriorReply}=await import('../server/hosted-ai.mjs');
 const prior='A map legend explains the symbols and colors that appear on a map. Read its units and source date before comparing two displays. Missing coverage is unknown and does not prove that a feature is absent.';
 assert.equal(repeatsPriorReply(prior.toUpperCase().replaceAll('.', '!'),prior),true);
 assert.equal(repeatsPriorReply('The map legend explains the symbols and colors that appear on a map. Read its units and source date before comparing two displays. Missing coverage is unknown and does not prove that a feature is absent.',prior),true);
 assert.equal(repeatsPriorReply('For a practical comparison, first choose matching dates. Next examine the provider notes and the numeric interval boundaries. A display animation should retain gaps rather than suggesting an observation where none exists.',prior),false);
 assert.equal(repeatsPriorReply('A map legend explains the symbols and colors that appear on a map. An uncertainty key can use separate marks for missing samples, approximate boundaries and withdrawn records; open each source to inspect its precise limitations.',prior),false);
 assert.equal(repeatsPriorReply('Read its units.',prior),false);assert.equal(repeatsPriorReply(prior,undefined),false);
});
