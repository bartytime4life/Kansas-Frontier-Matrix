"""Recovery regressions: surviving schemas, resumable work and atomic revisions."""
from contextlib import redirect_stdout
import csv
import gzip
import importlib
import io
import json
from pathlib import Path
import sqlite3
import unittest
from unittest.mock import patch

from tests.local_data.test_sql_feeds import FeedCase
from tools.local_data import sql_feeds as core
from tools.local_data import sql_feed_deeptime as deep, sql_feed_places as places
from tools.local_data import sql_feed_wikidata_plss as grid, sql_feed_bulk as bulk
from tools.local_data import sql_feed_institutions as institutions


class SurvivingSchemaTests(unittest.TestCase):
    def test_all_rebuilt_tables_match_the_surviving_database(self):
        fixture = json.loads(Path(__file__).with_name('fixtures').joinpath('recovered-feed-schema.json').read_text())
        for name, tables in fixture['modules'].items():
            module = importlib.import_module('tools.local_data.sql_feed_' + name)
            with sqlite3.connect(':memory:') as db:
                for key, value in vars(module).items():
                    if key.endswith('_DDL') and isinstance(value, str):
                        db.executescript(value)
                for table, expected in tables.items():
                    with self.subTest(module=name, table=table):
                        self.assertEqual([list(r) for r in db.execute(f'PRAGMA table_info("{table}")')], expected['columns'])
                        indexes = []
                        for _, idx, unique, origin, partial in db.execute(f'PRAGMA index_list("{table}")'):
                            indexes.append({'name': idx, 'unique': unique, 'origin': origin, 'partial': partial,
                                            'columns': [r[2] for r in db.execute(f'PRAGMA index_info("{idx}")')]})
                        self.assertEqual(sorted(indexes, key=lambda x: x['name']), expected['indexes'])

    def test_recovered_registry_entries_resolve(self):
        expected = ('airports obstacles dams mines grade-crossings rail-lines gnis-names post-offices '
                    'county-boundaries ceded-lands railroads-history congress-kansas nps-places nrhp '
                    'pbdb macrostrat radiocarbon neotoma idigbio-fossils banks exempt-orgs museums-libraries '
                    'schools historical-topo-maps usgs-samples wikidata-kansas plss-grid bridges '
                    'epa-facilities newspaper-text osm-kansas').split()
        self.assertEqual(len(expected), 31)
        for feed in expected:
            with self.subTest(feed=feed):
                self.assertTrue(callable(core.resolve(feed)))


class RevisionTests(FeedCase):
    def test_multitable_revision_and_reinstatement_are_atomic(self):
        for loader in (deep.load_tables, places._load_tables):
            with self.subTest(loader=loader.__module__):
                db = core.open_db(self.ctx)
                db.executescript('CREATE TABLE IF NOT EXISTS first(file_id, row_number, value);'
                                 'CREATE TABLE IF NOT EXISTS second(file_id, row_number, value);'
                                 'DELETE FROM first; DELETE FROM second; DELETE FROM kfm_sql_sources;')
                def load(version, bad=False):
                    path, digest = core.store_raw(self.ctx, 'revision', version + '.txt', version.encode(),
                                                  url='https://example.test/data', extra={'key': 'part'})
                    rows = [('first', [(version,)], 1), ('second', [(version, 'extra') if bad else (version,)], 1)]
                    if loader is places._load_tables:
                        rows = [(table, width, values) for table, values, width in rows]
                    return loader(db, self.ctx, source_id='test', key='part', path=path, digest=digest,
                                  url='https://example.test/data', tables=rows)
                self.assertEqual(load('A')['rows'], 2)
                with self.assertRaisesRegex(core.FeedError, 'ROW_SHAPE'):
                    load('B', bad=True)
                for table in ('first', 'second'):
                    self.assertEqual(db.execute(f'SELECT value FROM {table}').fetchall(), [('A',)])
                self.assertEqual(load('B')['superseded'], 1)
                self.assertEqual(load('A')['state'], 'reinstated')
                self.assertEqual(load('A')['state'], 'unchanged')
                for table in ('first', 'second'):
                    self.assertEqual(db.execute(f'SELECT value FROM {table}').fetchall(), [('A',)])
                with self.assertRaises(sqlite3.OperationalError):
                    deep.retire_all(db, 'test', 'part', ['first', 'missing_table'])
                self.assertEqual(db.execute('SELECT value FROM first').fetchall(), [('A',)])
                self.assertEqual(deep.retire_all(db, 'test', 'part', ['first', 'second']), 1)
                self.assertEqual(db.execute('SELECT count(*) FROM first').fetchone()[0], 0)
                self.assertEqual(db.execute('SELECT count(*) FROM second').fetchone()[0], 0)
                db.close()

    def test_bulk_feeds_refuse_observations_and_cli_routes_to_the_other_database(self):
        with self.assertRaisesRegex(core.FeedError, 'BULK_DATABASE_REQUIRED'):
            bulk.open_bulk_db(self.ctx)
        target = self.root / 'bulk/kfm-bulk.sqlite'
        seen = []
        def feed(ctx):
            seen.append(ctx.db_path)
            db = bulk.open_bulk_db(ctx)
            db.execute('CREATE TABLE bulk_marker(value)')
            db.execute("INSERT INTO bulk_marker VALUES ('bulk only')")
            db.close()
            return {'loaded': 1}
        with patch.object(core, 'resolve', return_value=feed), redirect_stdout(io.StringIO()):
            self.assertEqual(core.main(['--root', str(self.root), '--db', str(self.db_path),
                                        '--bulk-db', str(target), 'run', 'bridges']), 0)
        self.assertEqual(seen, [target])
        self.assertEqual(self.q("SELECT name FROM sqlite_master WHERE name='bulk_marker'"), [])
        with sqlite3.connect(target) as db:
            self.assertEqual(db.execute('SELECT value FROM bulk_marker').fetchall(), [('bulk only',)])

    def test_disk_ceiling_does_not_double_count_a_shared_catalog(self):
        self.ctx.shared_dirs = [self.db_path.parent, self.db_path.parent]
        self.ctx.catalogs = [self.db_path, self.db_path]
        used = sum(p.stat().st_size for p in self.db_path.parent.iterdir() if p.is_file())
        with patch.object(core, 'CAP', used + core.RESERVE + 1):
            core.guard(self.ctx)
        with patch.object(core, 'CAP', used + core.RESERVE):
            with self.assertRaisesRegex(core.FeedError, 'CEILING_85GB'):
                core.guard(self.ctx)
        # The owner's standing instruction: no ceiling unless CAP is set again.
        self.assertIsNone(core.CAP)
        core.guard(self.ctx)

    def test_newspaper_fulltext_index_tracks_replacements_and_deletions(self):
        db = core.open_db(self.ctx)
        db.executescript(bulk.NEWSPAPER_DDL)
        db.execute('INSERT INTO kfm_newspaper_pages VALUES (1,1,NULL,?,?,?,?,?,?,?)',
                   ('test', '1900-01-01', 1, 1, 'https://example.test', 'wheat harvest', 13))
        self.assertEqual(db.execute("SELECT count(*) FROM kfm_newspaper_pages_fts WHERE kfm_newspaper_pages_fts MATCH 'wheat'").fetchone()[0], 1)
        db.execute("UPDATE kfm_newspaper_pages SET ocr_text='corn harvest' WHERE file_id=1")
        self.assertEqual(db.execute("SELECT count(*) FROM kfm_newspaper_pages_fts WHERE kfm_newspaper_pages_fts MATCH 'wheat'").fetchone()[0], 0)
        self.assertEqual(db.execute("SELECT count(*) FROM kfm_newspaper_pages_fts WHERE kfm_newspaper_pages_fts MATCH 'corn'").fetchone()[0], 1)
        db.execute('DELETE FROM kfm_newspaper_pages WHERE file_id=1')
        self.assertEqual(db.execute("SELECT count(*) FROM kfm_newspaper_pages_fts WHERE kfm_newspaper_pages_fts MATCH 'corn'").fetchone()[0], 0)
        db.close()


class GridRecoveryTests(FeedCase):
    def test_wikidata_scalar_dates_and_coordinates_preserve_the_existing_conventions(self):
        record = {'claims': {'P625': [[-102.5, 39], [-98, 38]]},
                  'dates': {'P571': [{'time': '1861-01-29T00:00:00Z', 'precision': 11}]}}
        self.assertEqual(grid._first_date(record, 'P571'), ('1861-01-29', 11))
        record['dates']['P571'][0]['precision'] = 9
        self.assertEqual(grid._first_date(record, 'P571'), ('1861', 9))
        record['dates']['P571'][0]['precision'] = 10
        self.assertEqual(grid._first_date(record, 'P571'), ('1861-01', 10))
        with patch.object(grid, 'county_at', side_effect=[None, '20001']):
            lon, lat, geometry, geoid = grid._point(record, [])
        self.assertEqual((lon, lat, geoid), (-102.5, 39, '20001'))
        self.assertEqual(json.loads(geometry)['coordinates'], [[-102.5, 39], [-98, 38]])

    def test_plss_points_and_polygons_have_the_existing_table_width(self):
        for layer in grid.LAYERS:
            geometry = {'type': 'Point', 'coordinates': [-98, 38]} if not layer.bbox else {
                'type': 'Polygon', 'coordinates': [[[-98, 38], [-97, 38], [-97, 39], [-98, 38]]]}
            feature = {'type': 'Feature', 'geometry': geometry, 'properties': {k: None for k in layer.fields}}
            path = self.root / (layer.name + '.jsonl.gz')
            path.write_bytes(gzip.compress((json.dumps(feature) + '\n').encode()))
            row = list(grid._plss_rows(path, layer))[0]
            with self.subTest(layer=layer.name):
                self.assertEqual(len(row), layer.width)
                if layer.bbox:
                    self.assertEqual(row[-4:], (-98, 38, -97, 39))

    def test_wikidata_resumes_groups_not_yet_indexed_after_a_budget_stop(self):
        self.ctx.tiger = self.root / 'fixture.gpkg'
        db = core.open_db(self.ctx)
        state = {'cycle': {'started': '2026-11-03', 'complete': False, 'done': ['places/Q0-Q10']},
                 'items': {'places': 1}, 'ranges': {'places': [[0, 10]]}}
        core.set_state(db, self.ctx, 'wikidata-kansas', state)
        db.close()
        indexed, filled = [], []
        def index(ctx, budget, group):
            indexed.append(group.name)
            return {1 if group.name == 'places' else 20: {'P131'}}
        def fill(ctx, db, budget, group, *args):
            filled.append(group.name)
            return {'state': 'loaded', 'rows': 1}
        with patch.object(grid, 'kansas_counties', return_value=[]), patch.object(grid, '_index', side_effect=index), \
                patch.object(grid, '_fill_range', side_effect=fill):
            result = grid.wikidata_kansas(self.ctx)
        self.assertEqual(set(filled), {g.name for g in grid.GROUPS} - {'places'})
        self.assertNotIn('stopped', result)
        db = core.open_db(self.ctx)
        saved = core.get_state(db, 'wikidata-kansas')
        db.close()
        self.assertTrue(saved['cycle']['complete'])
        self.assertEqual(set(saved['ranges']), {g.name for g in grid.GROUPS})


    def test_wikidata_waits_out_a_throttled_query_before_giving_up(self):
        answers = [self.refusal(grid.SPARQL, retry_after=12), self.refusal(grid.SPARQL)]

        def fetch(url, **_):
            if answers:
                raise answers.pop(0)
            return core.Fetched(url, b'{"results": {"bindings": []}}')
        self.ctx.fetch = fetch
        budget = grid._Budget(10, 0, core.Throttle(self.ctx, 'wikidata-kansas'))
        _, bindings = grid._sparql(self.ctx, budget, 'SELECT ?item WHERE {}')
        self.assertEqual((bindings, budget.used, self.sleeps), ([], 3, [12.0, 120.0]), 'the query sent again after each wait counts against the cap')
        self.assertEqual(budget.throttle.summary(), {'throttled': 2, 'waited_seconds': 132})
        # A Retry-After beyond the run's budget, or no throttle at all, stops the run as before.
        refused = self.refusal(grid.SPARQL, retry_after=3000)

        def refuse(url, **_):
            raise refused
        self.ctx.fetch = refuse
        with self.assertRaisesRegex(core.FeedError, '^WIKIDATA_RATE_LIMITED$'):
            grid._sparql(self.ctx, budget, 'SELECT ?item WHERE {}')
        with self.assertRaisesRegex(core.FeedError, '^WIKIDATA_RATE_LIMITED$'):
            grid._sparql(self.ctx, grid._Budget(10, 0), 'SELECT ?item WHERE {}')
        self.assertEqual(self.sleeps, [12.0, 120.0])


class PreservedRecordTests(FeedCase):
    def test_osm_line_selection_checks_segments_instead_of_only_their_envelope(self):
        box = (0, 0, 10, 10)
        self.assertFalse(bulk._line_intersects_box([[-5, 9], [1, 15]], box))
        self.assertTrue(bulk._line_intersects_box([[-5, 5], [15, 5]], box))
        self.assertFalse(bulk._line_intersects_box([[-5, 11], [15, 11]], box))
        self.assertTrue(bulk._line_intersects_box([[5, 5]], box))

    def test_osm_nested_relations_follow_retained_geometry_in_any_order(self):
        def relation(ident, members, tags=None):
            return bulk._element('relation', ident, 1, None, {'type': 'route'} if tags is None else tags, members=members)
        rows = [relation(1, [['relation', 2, '']]), relation(2, [['way', 10, '']]),
                relation(3, [['way', 99, '']]), relation(4, [['node', 1, '']]),
                relation(5, [['relation', 6, '']]), relation(6, [['relation', 5, '']]),
                relation(7, [['relation', 8, '']]), relation(8, [['way', 10, '']], {})]
        kept = list(bulk._kansas_relations(rows, [1], [38_000_000_000], [-98_000_000_000], [10]))
        self.assertEqual([r[1] for r in kept], [1, 2, 4, 7])

    def test_legislative_terms_keep_the_original_one_based_indexes(self):
        record = {'id': {'bioguide': 'test'}, 'terms': [{'state': 'NE'}, {'state': 'KS'}, {'state': 'KS'}]}
        self.assertEqual([row[1] for row in places._term_rows(record)], [2, 3])

    def test_epa_quoted_newlines_are_one_record_and_malformed_records_are_retained(self):
        member = 'KS_CONTACT_FILE'
        header = bulk.FRS_TABLES[member][1]
        values = [''] * len(header)
        values[0], values[1] = '123', 'First line\nSecond line'
        content = io.StringIO(newline='')
        writer = csv.writer(content)
        writer.writerows([header, values, ['malformed', 'record']])
        parsed = list(bulk._frs_records(io.StringIO(content.getvalue(), newline=''), member))
        self.assertEqual(len(parsed), 2)
        self.assertEqual(parsed[0][1], 'First line\nSecond line')
        self.assertIsNone(parsed[0][-1])
        self.assertEqual(parsed[1][-1], 'malformed,record')
        self.assertTrue(all(v is None for v in parsed[1][:-1]))

    def test_bank_rows_load_into_the_legacy_shape_and_keep_the_complete_record(self):
        record = {'CERT': 1, 'NAME': 'Example bank', 'STALP': 'KS', 'ESTYMD': '1/2/1900', 'EXTRA_FIELD': 'preserved'}
        path = self.root / 'banks.jsonl.gz'
        path.write_bytes(gzip.compress((json.dumps(record) + '\n').encode()))
        values = next(institutions._fdic_rows(path, 'institutions'))
        db = core.open_db(self.ctx)
        db.executescript(institutions.FDIC_DDL)
        db.execute('INSERT INTO kfm_fdic_institutions VALUES (' + ','.join('?' for _ in range(len(values) + 2)) + ')', (1, 1, *values))
        actual = db.execute('SELECT name, established, record_json FROM kfm_fdic_institutions').fetchone()
        self.assertEqual(actual[:2], ('Example bank', '1900-01-02'))
        self.assertEqual(json.loads(actual[2]), record)
        db.close()

    def test_nrhp_blank_optional_fields_remain_null(self):
        content = 'ref,prefix,acreage_of_property,external_link\n123,,,\n'
        path = self.root / 'nrhp.csv.gz'
        path.write_bytes(gzip.compress(content.encode()))
        row = dict(zip(places.PROPERTY_COLUMNS, next(places._property_rows(path, 'everything'))))
        self.assertEqual(row['ref'], '123')
        self.assertIsNone(row['prefix'])
        self.assertIsNone(row['acreage_of_property'])
        self.assertIsNone(row['external_link'])


if __name__ == '__main__':
    unittest.main()
