"""Build a reviewed, static query allowlist from the read-only recovery inventory.

Usage: python3 scripts/local-data/build-recovered-catalog.py INVENTORY_JSON
The generated file contains schema, never database paths or observation values.
"""
import json, pathlib, re, sys

inventory = json.loads(pathlib.Path(sys.argv[1]).read_text())
excluded = {'kfm_sql_sources', 'kfm_sql_build', 'kfm_feed_state'}
collections = []
for database in ('observations', 'bulk'):
    for table in inventory[database]['tables']:
        name = table['name']
        if name in excluded or '_fts' in name or not name.startswith('kfm_'):
            continue
        columns = [c['name'] for c in table['columns'] if c['name'] not in ('source_path', 'manifest_json')]
        keys = [c['name'] for c in sorted(table['columns'], key=lambda c: c['pk']) if c['pk']]
        assert keys and set(keys) <= set(columns), name
        assert all(re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]*', c) for c in [name, *columns])
        short = name.removeprefix('kfm_')
        collections.append(dict(id=database+'-'+short.replace('_','-'), database=database,
            table=name, title=short.replace('_',' '), columns=columns, keys=keys,
            geometry='geometry_geojson' if 'geometry_geojson' in columns else None))
target = pathlib.Path(__file__).with_name('recovered-catalog.json')
target.write_text('[\n'+',\n'.join('  '+json.dumps(c, separators=(',',':')) for c in collections)+'\n]\n')
print(json.dumps({'collections':len(collections), 'geometryCollections':sum(bool(c['geometry']) for c in collections)}))
