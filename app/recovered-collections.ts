import catalog from '../scripts/local-data/recovered-catalog.json' with {type:'json'};
import type { TopicId } from './layer-workspaces';
import { recoveredTitle, recoveredTopics as topicsOf, recoveredMapId, recoveredMapUrl as mapUrl } from './recovered-topics.mjs';

export const RECOVERED_COLLECTIONS = catalog.map(collection => ({...collection, title: recoveredTitle(collection.title)}));
export const recoveredCollection = (id: string) => RECOVERED_COLLECTIONS.find(c=>c.id===id);
export const recoveredTopics = (id: string): readonly TopicId[] => topicsOf(id) as TopicId[];
export { recoveredMapId };
export const recoveredMapUrl = (ids: readonly string[]) => mapUrl([...ids], (id: string) => Boolean(recoveredCollection(id)?.geometry));
