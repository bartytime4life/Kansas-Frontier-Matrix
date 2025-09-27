### `web/docs/schema.md`
```markdown
# JSON Schema — Web Config

The viewer ingests a merged config (`app.config.json`).

## Structure
- `version`: semantic version
- `generated`: ISO timestamp
- `title`, `subtitle`
- `style`: basemap style URL
- `center`, `zoom`: map defaults
- `time`: { `min`, `max` }
- `defaults`: fallback layer params
- `layers`: array of layer objects

For authoritative schema see `web/config/schema.json`.
