import catalog from './motion-clips.json' with { type: 'json' };
export const MOTION_CLIPS=catalog;
export function motionClip(category,index=0){const list=catalog[category]||catalog.weather;return list[((index%list.length)+list.length)%list.length];}
