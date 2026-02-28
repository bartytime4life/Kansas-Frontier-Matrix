import type { ViewState } from './view_state';

export function toQueryParams(state: ViewState): URLSearchParams {
  const params = new URLSearchParams();

  if (state.bbox) {
    params.set('bbox', state.bbox.join(','));
  }

  if (state.time) {
    params.set('time', state.time);
  }

  if (state.layers.length > 0) {
    params.set('layers', state.layers.join(','));
  }

  Object.entries(state.filters).forEach(([key, value]) => {
    params.set(`filter.${key}`, String(value));
  });

  return params;
}
