/** Presentation navigation only: these entries never activate sources or send AI requests. */
export const WELCOME_FEATURES = [
  { id: 'roads', status: 'Explore', description: 'Explore Kansas roads, bridges and rail corridors.', destination: 'transport' },
  { id: 'farming', status: 'Explore', description: 'Find crop, soil and water tools for agricultural questions.', destination: 'agriculture' },
  { id: 'government', status: 'Explore', description: 'Browse county boundaries and public-land context.', destination: 'land' },
  { id: 'weather', status: 'Explore', description: 'Inspect weather sources with their own dates and limits.', destination: 'weather' },
  { id: 'history', status: 'Discover', description: 'Follow Kansas history and dated map editions.', destination: 'history' },
  { id: 'sources', status: 'Coming', description: 'More reviewed records arrive as source coverage grows.', destination: 'sources' },
] as const;
export type WelcomeFeatureDestination = typeof WELCOME_FEATURES[number]['destination'];
