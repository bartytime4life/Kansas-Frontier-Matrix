import { CARD_PIPELINE_BINDINGS, PIPELINE_DEFINITIONS } from '../card-pipelines';
import { cardSnapshot } from '../../server/card-pipeline-health.mjs';
import PipelineDashboard from './workspace';
export default function PipelinesPage() {
  return <PipelineDashboard initial={cardSnapshot(CARD_PIPELINE_BINDINGS, PIPELINE_DEFINITIONS)} />;
}
