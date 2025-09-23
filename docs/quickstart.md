# Quickstart

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
make fetch cogs terrain stac
kgt validate-stac stac/items --no-strict
kgt render-config --stac stac/items --output web/app.config.json --pretty
python -m http.server -d web 8080
