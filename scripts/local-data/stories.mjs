// The relay's read of the story bundles the pipeline builds (tools/local_data/sql_feed_stories.py). One primary-key
// lookup, one row. Held in PENDING_DATASETS: the website does not serve it until the owner approves publication.
import {only,fail} from './query.mjs';

const STORY_ID=/^[a-z0-9]+(?:-[a-z0-9]+)*$/;

export const storyBundles={
 id:'stories',db:'observations',title:'The Kansas record: story bundles',indexes:[],
 source:{provider:'Kansas Frontier Matrix pipeline',url:'/',
  coverage:'Aggregates built from public source tables. Each bundle lists its own sources, licences, observed range and limits.',
  notes:'Built on the pipeline PC from its SQL feeds; values carry the limits of their sources.'},
 params:{story:'story id, e.g. iron-horse'},
 parse(input){
  only(input,['story']);
  const story=input.story;
  if(typeof story!=='string'||story.length>64||!STORY_ID.test(story))throw fail();
  return {story};
 },
 run(db,q){
  if(!db.prepare("SELECT 1 FROM sqlite_master WHERE type='table' AND name='kfm_story_bundles'").get())return {total:0,rows:[]};
  const row=db.prepare('SELECT story_id,version,built_at,sha256,bytes,bundle_json FROM kfm_story_bundles WHERE story_id=?').get(q.story);
  if(!row)return {total:0,rows:[]};
  const {bundle_json,...about}=row;
  return {total:1,rows:[{...about,bundle:JSON.parse(bundle_json)}]};
 },
};
