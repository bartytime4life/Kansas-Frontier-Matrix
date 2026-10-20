/** Presentation navigation only: these entries never activate sources or send AI requests. */
export const WELCOME_FEATURES = [
  { id: 'roads', status: 'Explore', description: 'Explore Kansas roads & rail.', destination: 'transport' },
  { id: 'farming', status: 'Explore', description: 'Discover crop, soil & water tools.', destination: 'agriculture' },
  { id: 'government', status: 'Explore', description: 'Find counties & public-land maps.', destination: 'land' },
  { id: 'weather', status: 'Explore', description: 'Follow weather, dates & sources.', destination: 'weather' },
  { id: 'history', status: 'Discover', description: 'Discover Kansas history & maps.', destination: 'history' },
  { id: 'sources', status: 'Coming', description: 'More reviewed records are coming.', destination: 'sources' },
] as const;
export type WelcomeFeatureDestination = typeof WELCOME_FEATURES[number]['destination'];
