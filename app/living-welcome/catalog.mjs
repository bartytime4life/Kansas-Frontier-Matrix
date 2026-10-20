import { motionClip } from './motion-catalog.mjs';
import kansasHistory from './kansas-history.json' with { type: 'json' };
// Public presentation metadata only. No observations or connection credentials.
export const SCENES = {
  "weather": [
    "Clouds building & travelling",
    "Rain striking the ground",
    "Wind moving through grass",
    "A storm grows from above",
    "A rotating tornado"
  ],
  "rivers": [
    "Water finding its way downstream",
    "Water released from a dam",
    "Water put to work",
    "The hidden water supply"
  ],
  "science": [
    "Roots exploring their surroundings",
    "A plant opens toward the light",
    "Seeing the invisible"
  ],
  "underground": [
    "Drilling to learn what lies below",
    "A water well takes shape",
    "Groundwater viewed from space"
  ],
  "history": kansasHistory.map(chapter => chapter.title),
  "transport": [
    "A train crosses the landscape",
    "Roads that connect us",
    "Rush-hour rhythms"
  ],
  "farming": [
    "Tractors working the fields",
    "Harvest in motion",
    "From field to grain"
  ],
  "government": [
    "Restoring public landmarks",
    "People in public places",
    "Public works in motion"
  ]
};
export const CATEGORY_IDS = Object.keys(SCENES);
export const HISTORY_ERAS = ['1854–1861','Lawrence · 1863','Mine Creek · 1864','Nicodemus · 1877','Dust Bowl · 1930s','Brown · 1954'];
export function sceneArt(id,index=0){return motionClip(id,index).poster;}
