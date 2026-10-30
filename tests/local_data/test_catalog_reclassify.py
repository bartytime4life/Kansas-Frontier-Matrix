"""Classifier regressions and transactional catalog repair using synthetic rows."""
import copy
import hashlib
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from tools.local_data import catalog_reclassify as repair, intake, intake_route
from tools.local_data.intake_profile import classification_hints


class ClassifierTests(unittest.TestCase):
    def test_station_codes_and_place_names_do_not_become_domains(self):
        for path, expected in (
            ('ftp.ncdc.noaa.gov/download/ghcndex-stn-beta-20260919/stn-indices/CDD/US1SCDL0004_CDD.txt', 'atmosphere'),
            ('ftp.ncdc.noaa.gov/data/asos-fivemin/6401-2000/64010KGSO200001.dat', 'atmosphere'),
            ('KFM Urban Roadways/Wellington.pdf', 'roads-rail-trade'),
            ('US1SCDL0004.txt', None), ('64010KGSO200001.dat', None),
            ('scoring/soil.csv', 'soil'), ('Las Vegas.pdf', None),
        ):
            with self.subTest(path=path):
                self.assertEqual(classification_hints(path, {}, [])['domain'], expected)

    def test_real_keywords_fields_and_declarations_survive(self):
        for path, fields, domain in (
            ('ks_CDL_2020.tif', [], 'agriculture'), ('KGS/M118-geology.jpg', [], 'geology'),
            ('data.csv', ['well_depth', 'core_id'], 'geology'), ('wells.csv', [], 'geology'),
            ('streamflow.csv', [], 'hydrology'), ('gas.csv', [], 'geology'),
        ):
            hints = classification_hints(path, {'fields': fields}, [])
            self.assertEqual(hints['domain'], domain)
            self.assertTrue(all(hints['domain_candidates'][0]['matches']))
        hints = classification_hints('ftp.ncdc.noaa.gov/data/asos-fivemin/station.dat', {}, [], 'hydrology')
        self.assertEqual((hints['domain'], hints['domain_basis']), ('hydrology', 'declared'))

    def test_source_hints_are_component_bounded_and_review_flags_retained(self):
        self.assertIsNone(classification_hints('fakeftp.ncdc.noaa.gov/data/asos-fivemin/x.dat', {}, [])['domain'])
        hints = classification_hints('KFM Urban Roadways/Wellington.pdf', {'fields': ['owner_email']}, ['photo_exact_location'])
        self.assertIn('possible_living_persons', hints['review_flags'])
        self.assertIn('exact_location', hints['review_flags'])


class RepairTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.db = self.root / 'index.sqlite'
        with sqlite3.connect(self.db) as conn:
            conn.executescript(intake.SCHEMA_SQL)
            for identity in ('first', 'second'):
                item = dict(id=identity, lane='raw', relative_path='KFM Urban Roadways/Wellington.pdf',
                            store_path='data/raw/KFM Urban Roadways/Wellington.pdf', size_bytes=100, declared=None)
                profile = dict(schema='kfm-intake-profile/v1', analyzer_version='1',
                               hints=dict(domain='geology', review_flags=[]), format=dict(family='document'),
                               structure={}, issues=[], spatial=dict(kansas='unknown'), temporal={})
                decision = intake_route.decide(item, profile, intake_route.load_budget())
                row = dict(item, mtime_ns=1000, sha256='a'*64, declared_json=None,
                           profile_json=json.dumps(profile), decision_json=json.dumps(decision), family='document',
                           kind='pdf', domain='geology', status=decision['status'], kansas='unknown',
                           time_start=None, time_end=None, analyzer_version='1', analyzed_at='2026-10-10',
                           run_id='original', present=1)
                del row['declared']
                conn.execute(f"INSERT INTO items ({','.join(row)}) VALUES ({','.join('?' * len(row))})", tuple(row.values()))
        self.value = repair.plan(self.db, ['first', 'second'])
        self.plan = self.root / 'plan.json'
        self.raw = repair.canonical(self.value)
        self.plan.write_bytes(self.raw)
        self.pin = hashlib.sha256(self.raw).hexdigest()

    def rows(self):
        with sqlite3.connect(self.db) as conn:
            conn.row_factory = sqlite3.Row
            return [dict(row) for row in conn.execute('SELECT * FROM items ORDER BY id')]

    def test_apply_restore_preserves_holds_profiles_and_exact_original_rows(self):
        before = self.rows()
        result = repair.apply(self.db, self.plan, self.pin, self.root/'recovery.json')
        self.assertEqual(result['rows'], 2)
        after = self.rows()
        for old, new in zip(before, after):
            self.assertEqual(new['domain'], 'roads-rail-trade')
            for key in set(old) - set(repair.EDIT_COLUMNS):
                self.assertEqual(old[key], new[key])
            a, b = json.loads(old['decision_json']), json.loads(new['decision_json'])
            for key in ('holds', 'status', 'authority', 'review_flags'):
                self.assertEqual(a[key], b[key])
            self.assertIn('/roads-rail-trade/', b['placements'][2]['target'])
            a, b = json.loads(old['profile_json']), json.loads(new['profile_json'])
            a.pop('hints'); b.pop('hints'); self.assertEqual(a, b)
        repair.apply(self.db, self.root/'recovery.json', self.pin, self.root/'restore-journal.json', restore=True)
        self.assertEqual(self.rows(), before)

    def test_later_row_conflict_rolls_back_first_and_no_recovery_written(self):
        with sqlite3.connect(self.db) as conn:
            conn.execute("UPDATE items SET sha256='new' WHERE id='second'")
        before = self.rows()
        with self.assertRaisesRegex(ValueError, 'ROW_CHANGED'):
            repair.apply(self.db, self.plan, self.pin, self.root/'recovery.json')
        self.assertEqual(self.rows(), before)
        self.assertFalse((self.root/'recovery.json').exists())

    def test_restore_refuses_to_erase_later_changes(self):
        repair.apply(self.db, self.plan, self.pin, self.root/'recovery.json')
        with sqlite3.connect(self.db) as conn:
            conn.execute("UPDATE items SET status='changed' WHERE id='second'")
        before = self.rows()
        with self.assertRaisesRegex(ValueError, 'ROW_CHANGED'):
            repair.apply(self.db, self.plan, self.pin, self.root/'restore.json', restore=True)
        self.assertEqual(self.rows(), before)

    def test_journal_failure_rolls_back(self):
        before = self.rows()
        with patch.object(repair, 'write_new', side_effect=OSError('disk full')):
            with self.assertRaises(OSError):
                repair.apply(self.db, self.plan, self.pin, self.root/'recovery.json')
        self.assertEqual(self.rows(), before)

    def test_changed_pin_and_forged_authority_are_rejected(self):
        before = self.rows()
        with self.assertRaisesRegex(ValueError, 'PIN_CHANGED'):
            repair.apply(self.db, self.plan, '0'*64, self.root/'recovery.json')
        value = copy.deepcopy(self.value)
        value['changes'][0]['after']['status'] = 'ready'
        raw = repair.canonical(value); self.plan.write_bytes(raw)
        with self.assertRaisesRegex(ValueError, 'NOT_REPRODUCIBLE'):
            repair.apply(self.db, self.plan, hashlib.sha256(raw).hexdigest(), self.root/'recovery.json')
        self.assertEqual(self.rows(), before)

    def test_selection_limits_missing_items_and_sensitive_changes_fail(self):
        for ids in ([], ['first', 'first'], ['first']*1001, ['missing']):
            with self.assertRaises(ValueError):
                repair.plan(self.db, ids)
        row = self.rows()[0]
        row['relative_path'] = 'archaeology.csv'
        with self.assertRaisesRegex(ValueError, 'REVIEW_CHANGE'):
            repair.replacement(row)


if __name__ == '__main__':
    unittest.main()
