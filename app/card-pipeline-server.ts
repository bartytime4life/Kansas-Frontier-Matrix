import { CARD_PIPELINE_BINDINGS, PIPELINE_DEFINITIONS } from './card-pipelines';
import { PC_CAPTURE_IDS } from './pipeline-catalog.mjs';
import { cardSnapshot, publicSourceHealth } from '../server/card-pipeline-health.mjs';
import { getPipelineStore } from '../server/pipeline-store.mjs';
import { publicContext } from '../server/pipeline-handler.mjs';

/** Check the existing serving gates on every request; never publish local worker diagnostics. */
export async function getCardPipelineSnapshot({
  environment = process.env, storeFactory = getPipelineStore, readContext = publicContext, now = Date.now(),
} = {}) {
  if (environment.KFM_PIPELINE_ENABLED !== 'true' || environment.KFM_RUNTIME_ROLE !== 'published') {
    return cardSnapshot(CARD_PIPELINE_BINDINGS, PIPELINE_DEFINITIONS, [], { now });
  }
  try {
    const store = await storeFactory(environment);
    let failed = false;
    const sources = await Promise.all(PC_CAPTURE_IDS.map(async sourceId => {
      try { return publicSourceHealth(sourceId, await readContext(sourceId, { store, environment, now })); }
      catch {
        failed = true;
        return { ...publicSourceHealth(sourceId, null), state: 'unavailable' };
      }
    }));
    return cardSnapshot(CARD_PIPELINE_BINDINGS, PIPELINE_DEFINITIONS, sources, { now, state: failed ? 'degraded' : 'checked' });
  } catch {
    return cardSnapshot(CARD_PIPELINE_BINDINGS, PIPELINE_DEFINITIONS,
      PC_CAPTURE_IDS.map(sourceId => ({ ...publicSourceHealth(sourceId, null), state: 'unavailable' })), { now, state: 'degraded' });
  }
}
