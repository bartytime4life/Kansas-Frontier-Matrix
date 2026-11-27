export const COMPARISON_PLACES = Object.freeze([
  { id: 'topeka', name: 'Topeka and Shawnee County', climateId: 'USW00013996', countyId: '20177', sunlightId: 'topeka' },
  { id: 'wichita', name: 'Wichita and Sedgwick County', climateId: 'USW00003928', countyId: '20173', sunlightId: 'wichita' },
  { id: 'dodge-city', name: 'Dodge City and Ford County', climateId: 'USW00013985', countyId: '20057', sunlightId: 'dodge-city' },
].map(place => Object.freeze(place)));

export const DEFAULT_COMPARISON_PLACE = 'topeka';

/** @param {string} id */
export function comparisonPlace(id) {
  return COMPARISON_PLACES.find(place => place.id === id);
}
