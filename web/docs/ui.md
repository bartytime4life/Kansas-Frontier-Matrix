# Web UI Behavior

## Sidebar
- Lists all layers by category.
- Toggle visibility + adjust opacity.
- Color coding from `categories.json`.

## Timeline
- Filters features by layer `time` metadata.
- Supports step, loop, fps (configurable via `time_config.json`).

## Popups
- Configurable per layer with `popup: [field1, field2, ...]`.
- Uses `window.attachPopup` if defined in `app.js`.

## Legend
- Uses `window.LegendControl` if defined.
- Reads `legend.json`.

## Accessibility
- Use ARIA roles for controls:contentReference[oaicite:12]{index=12}.
