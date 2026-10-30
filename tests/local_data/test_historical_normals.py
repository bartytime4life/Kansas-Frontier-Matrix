"""Offline climate context retains period, missingness and private authority."""
import csv
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from connectors.noaa.src.noaa.climate_normals import INVENTORY_KEY
from connectors.noaa.src.noaa.climate_normals_capture import capture, canonical_bytes
from pipelines.domains.atmosphere.noaa_normals import normalize_capture
from tools.local_data.file_io import write_new
from tools.local_data.historical_normals import derive, digest, FIELDS, rows, TABLES
from tools.local_data.manage import init_store
from tools.local_data.review_packages import ReviewPackages


class HistoricalNormalsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.source = Path(self.temp.name) / 'archive'
        self.root = Path(self.temp.name) / 'working'
        init_store(self.root)
        ids = ['USC00140010', 'USC00140011']
        inventory = ('\n'.join(f'{sid:<11} {38.9267:8.4f} {-97.2128:9.4f} {361.8:6.1f} KS {"ABILENE":<30}'.ljust(85)
                               for sid in ids) + '\n').encode()
        def fetch(key, _limit):
            raw = inventory
            if key != INVENTORY_KEY:
                sid = key.split('/')[-1][:-4]
                fields = ['STATION', 'DATE', 'LATITUDE', 'LONGITUDE', 'NAME', 'month', 'MLY-PRCP-NORMAL',
                          'comp_flag_MLY-PRCP-NORMAL', 'years_MLY-PRCP-NORMAL']
                if sid == ids[0]:
                    fields += ['MLY-TAVG-NORMAL', 'comp_flag_MLY-TAVG-NORMAL', 'years_MLY-TAVG-NORMAL']
                out = io.StringIO(); writer = csv.DictWriter(out, fieldnames=fields); writer.writeheader()
                for month in range(1, 13):
                    row = dict(zip(fields[:6], [sid, f'{month:02d}', '38.9267', '-97.2128', 'ABILENE, KS US', f'{month:02d}']))
                    row.update({'MLY-PRCP-NORMAL': '0.86', 'comp_flag_MLY-PRCP-NORMAL': 'E', 'years_MLY-PRCP-NORMAL': '20'})
                    if sid == ids[0]:
                        row.update({'MLY-TAVG-NORMAL': '-9999' if month == 2 else '32.5',
                                    'comp_flag_MLY-TAVG-NORMAL': '' if month == 2 else 'S',
                                    'years_MLY-TAVG-NORMAL': '' if month == 2 else '27'})
                    writer.writerow(row)
                raw = out.getvalue().encode()
            return raw, {'status': 200, 'retrieved_at': '2026-10-01T16:24:30Z'}
        acquired = capture(fetcher=fetch)
        self.capture = acquired.manifest
        for sha, raw in acquired.objects.items():
            write_new(self.source / 'data/quarantine/noaa-climate-normals/objects/sha256' / sha[7:] / 'payload', raw)
        self.capture_path = self.source / 'data/quarantine/noaa-climate-normals/runs' / self.capture['capture_id'][7:] / 'manifest.json'
        write_new(self.capture_path, canonical_bytes(self.capture))
        self.capture_pin = digest(self.capture_path.read_bytes())
        candidate = normalize_capture(self.capture, acquired.objects)
        self.package = self.source / 'data/work/atmosphere/example'
        for variable in TABLES:
            out = io.StringIO(); writer = csv.DictWriter(out, fieldnames=FIELDS); writer.writeheader()
            writer.writerows(rows(candidate, self.capture, variable))
            write_new(self.package / 'tables' / (variable + '.csv'), out.getvalue().encode())
        write_new(self.package / 'rights-review.json', b'{"state":"PENDING"}')
        self.manifest = self.package / 'review-manifest.json'
        self.pin()

    def pin(self, **changes):
        records = [{'file': str(p.relative_to(self.package)), 'bytes': p.stat().st_size, 'sha256': digest(p.read_bytes())}
                   for p in sorted(self.package.rglob('*')) if p.is_file() and p != self.manifest]
        value = {'profile': 'kfm-private-collection-readiness/v1', 'review_state': 'PENDING', 'released': False,
                 'published': False, 'source_admitted': False, 'outputs': records, **changes}
        self.manifest.write_bytes(canonical_bytes(value)); self.manifest_pin = digest(self.manifest.read_bytes())

    def run_derivation(self, root=None):
        return derive(self.source, root or self.root, str(self.manifest.relative_to(self.source)), self.manifest_pin,
                      self.capture['capture_id'], self.capture_pin)

    def test_offline_idempotent_replay_preserves_missingness_period_flags_and_originals(self):
        before = {str(p): p.read_bytes() for p in self.source.rglob('*') if p.is_file()}
        with patch('socket.socket.connect', side_effect=AssertionError('network forbidden')):
            result = self.run_derivation()
            self.assertEqual(result, self.run_derivation())
        self.assertEqual(result['stations'], 2)
        self.assertEqual(result['variables']['temperature_f']['values_present'], 11)
        self.assertEqual(result['variables']['temperature_f']['element_not_published'], 12)
        self.assertEqual(result['variables']['temperature_f']['published_value_missing'], 1)
        self.assertEqual(result['variables']['precipitation_in']['completeness_flags']['E'], 24)
        self.assertFalse(any(result['authority'].values()))
        reader = ReviewPackages(self.root, [result['binding']]); package = reader.catalog()['packages'][0]
        member = next(m for m in package['members'] if m['name'] == 'coverage.json')
        preview, _ = reader.preview(package['id'], member['id']); coverage = json.loads(preview['text'])
        self.assertEqual(coverage['normal_period'], '1991-2020')
        self.assertEqual(coverage['native_coordinate_crs'], 'NAD83')
        self.assertFalse(any(m['name'].endswith('.geojson') for m in package['members']))
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.source.rglob('*') if p.is_file()})

    def test_rehashed_edited_table_fails_replay(self):
        table = self.package / 'tables/temperature_f.csv'
        table.write_bytes(table.read_bytes().replace(b'32.5', b'99.9')); self.pin()
        with self.assertRaisesRegex(ValueError, 'TABLE_REPLAY_MISMATCH'):
            self.run_derivation()
        self.assertFalse((self.root / 'data/work/atmosphere/historical-normals').exists())

    def test_pinned_manifest_and_source_member_changes_fail(self):
        self.manifest.write_text('{}')
        with self.assertRaisesRegex(ValueError, 'MANIFEST_CHANGED'):
            self.run_derivation()
        self.pin(); (self.package / 'rights-review.json').write_text('bad')
        with self.assertRaisesRegex(ValueError, 'SOURCE_MEMBER_CHANGED'):
            self.run_derivation()

    def test_raw_object_and_capture_identity_changes_fail(self):
        path = self.source / 'data/quarantine/noaa-climate-normals/objects/sha256' / self.capture['station_objects'][0]['sha256'][7:] / 'payload'
        path.write_bytes(b'corrupt')
        with self.assertRaisesRegex(ValueError, 'OBJECT_CHANGED_OR_LIMIT'):
            self.run_derivation()
        changed = {**self.capture, 'captured_at': '2099-01-01T00:00:00Z'}
        self.capture_path.write_bytes(canonical_bytes(changed)); self.capture_pin = digest(self.capture_path.read_bytes())
        with self.assertRaisesRegex(ValueError, 'CAPTURE_ID_INVALID'):
            self.run_derivation()

    def test_authority_and_overlapping_roots_rejected(self):
        self.pin(source_admitted=True)
        with self.assertRaisesRegex(ValueError, 'AUTHORITY_INVALID'):
            self.run_derivation()
        with self.assertRaisesRegex(ValueError, 'SEPARATE_DESTINATION'):
            self.run_derivation(self.source)

    def test_symlink_and_output_mutation_rejected(self):
        result = self.run_derivation()
        target = self.root / result['binding'].split('@')[0]
        (target.parent / 'coverage.json').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'OUTPUT_CHANGED'):
            self.run_derivation()
        table = self.package / 'tables/temperature_f.csv'
        saved = self.package / 'saved.csv'; table.rename(saved); table.symlink_to(saved)
        with self.assertRaisesRegex(ValueError, 'SYMLINK'):
            self.run_derivation()

    def test_limits_reject_unbounded_object_declarations(self):
        changed = json.loads(self.capture_path.read_bytes())
        changed['station_objects'][0]['bytes'] = 128 * 1024 + 1
        changed.pop('capture_id'); changed['capture_id'] = 'sha256:' + digest(canonical_bytes(changed))
        self.capture_path = self.capture_path.parent.parent / changed['capture_id'][7:] / 'manifest.json'
        write_new(self.capture_path, canonical_bytes(changed)); self.capture = changed; self.capture_pin = digest(self.capture_path.read_bytes())
        with self.assertRaisesRegex(ValueError, 'CAPTURE_LIMIT'):
            self.run_derivation()


if __name__ == '__main__':
    unittest.main()
