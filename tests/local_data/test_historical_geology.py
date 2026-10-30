"""Archived geology is a dated document, not inferred measurement or map geometry."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tests.local_data.test_review_images import jpeg
from tools.local_data.file_io import write_new
from tools.local_data.historical_geology import derive, canonical, digest, NAME, URL, RECORD, ASSET
from tools.local_data.manage import init_store
from tools.local_data.review_packages import ReviewPackages


class HistoricalGeologyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.source = Path(self.temp.name) / 'archive'; self.root = Path(self.temp.name) / 'working'; init_store(self.root)
        self.job_id = '1' * 32
        self.directory = self.source / 'data/raw/public-maps' / RECORD / self.job_id
        self.raw = jpeg(); write_new(self.directory / NAME, self.raw)
        self.record = {'record': {'id': RECORD, 'title': 'Surficial Geology of Kansas — KGS M-118', 'publisher': 'KGS',
                                  'mapYear': 2008, 'scale': '1:500,000', 'rights': {'status': 'held'}},
                       'asset': {'id': ASSET, 'format': 'JPEG', 'url': URL, 'expectedBytes': len(self.raw)}}
        self.receipt = {'schema': 'kfm-public-map-download-receipt/v1', 'admission': 'NOT_ADMITTED', 'release': 'NOT_RELEASED',
                        'review': 'UNREVIEWED', 'providerChecksumVerified': False,
                        'job': {'id': self.job_id, 'assetId': ASSET, 'state': 'downloaded', 'mapReady': False,
                                'bytes': len(self.raw), 'expectedBytes': len(self.raw), 'sha256': digest(self.raw),
                                'updatedAt': '2026-10-09T14:10:51Z', 'destination': '/unrelated/old/PC'},
                        'files': [{'name': NAME, 'bytes': len(self.raw), 'complete': True, 'sha256': digest(self.raw)}]}
        self.receipt_path = self.source / 'data/receipts/ingest/public-maps' / (self.job_id + '.json')
        self.receipt_path.parent.mkdir(parents=True)
        self.pin()

    def pin(self):
        self.receipt_path.write_bytes(canonical(self.receipt))
        (self.directory / 'source.json').write_bytes(canonical(self.record))
        self.receipt_pin = digest(self.receipt_path.read_bytes()); self.source_pin = digest((self.directory / 'source.json').read_bytes())

    def run_derivation(self, root=None):
        return derive(self.source, root or self.root, self.job_id, self.receipt_pin, self.source_pin)

    def test_offline_idempotent_copy_preserves_originals_dates_scale_and_holds(self):
        before = {str(p): p.read_bytes() for p in self.source.rglob('*') if p.is_file()}
        with patch('socket.socket.connect', side_effect=AssertionError('network forbidden')):
            result = self.run_derivation(); self.assertEqual(result, self.run_derivation())
        model = ReviewPackages(self.root, [result['binding']]); package = model.catalog()['packages'][0]
        member = next(m for m in package['members'] if m['name'] == 'source-map.jpg')
        self.assertEqual(member['kind'], 'image')
        self.assertEqual(model.preview(package['id'], member['id']), (self.raw, 'image/jpeg'))
        member = next(m for m in package['members'] if m['name'] == 'coverage.json')
        coverage = json.loads(model.preview(package['id'], member['id'])[0]['text'])
        self.assertEqual((coverage['map_edition_year'], coverage['scale_denominator']), (2008, 500000))
        self.assertIsNone(coverage['source_observation_interval']); self.assertIsNone(coverage['geometry'])
        self.assertFalse(coverage['georeferencing_verified']); self.assertFalse(coverage['provider_checksum_verified'])
        self.assertFalse(any(coverage['authority'].values()))
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.source.rglob('*') if p.is_file()})

    def test_rehashed_receipt_cannot_admit_partial_or_released_bytes(self):
        for field, value in [('state', 'cancelled'), ('mapReady', True), ('expectedBytes', 99999)]:
            old = self.receipt['job'][field]; self.receipt['job'][field] = value; self.pin()
            with self.subTest(field=field), self.assertRaises(ValueError): self.run_derivation()
            self.receipt['job'][field] = old
        self.receipt['release'] = 'RELEASED'; self.pin()
        with self.assertRaises(ValueError): self.run_derivation()
        self.assertFalse((self.root / 'data/work/geology').exists())

    def test_rehashed_wrong_source_edition_and_url_fail(self):
        self.record['record']['mapYear'] = 2026; self.pin()
        with self.assertRaisesRegex(ValueError, 'SOURCE_IDENTITY'): self.run_derivation()
        self.record['record']['mapYear'] = 2008; self.record['asset']['url'] = 'https://example.com/map.jpg'; self.pin()
        with self.assertRaisesRegex(ValueError, 'SOURCE_IDENTITY'): self.run_derivation()

    def test_raw_source_and_receipt_pins_reject_mutation(self):
        (self.directory / NAME).write_bytes(b'corrupt')
        with self.assertRaisesRegex(ValueError, 'PIN_CHANGED'): self.run_derivation()
        (self.directory / NAME).write_bytes(self.raw); (self.directory / 'source.json').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'PIN_CHANGED'): self.run_derivation()
        self.pin(); self.receipt_path.write_text('{}')
        with self.assertRaisesRegex(ValueError, 'PIN_CHANGED'): self.run_derivation()

    def test_unsafe_inputs_and_symlinks_fail_before_output(self):
        with self.assertRaisesRegex(ValueError, 'SEPARATE_DESTINATION'): self.run_derivation(self.source)
        with self.assertRaisesRegex(ValueError, 'JOB_INVALID'):
            derive(self.source, self.root, '../outside', self.receipt_pin, self.source_pin)
        path = self.directory / NAME; path.rename(self.directory / 'saved.jpg'); path.symlink_to(self.directory / 'saved.jpg')
        with self.assertRaisesRegex(ValueError, 'SYMLINK'): self.run_derivation()

    def test_immutable_output_rejects_changes_and_extra_members(self):
        result = self.run_derivation(); directory = (self.root / result['binding'].split('@')[0]).parent
        extra = directory / 'unexpected.txt'; extra.write_text('extra')
        with self.assertRaisesRegex(ValueError, 'CLOSURE_CHANGED'): self.run_derivation()
        extra.unlink(); (directory / 'source-map.jpg').write_bytes(b'corrupt')
        with self.assertRaisesRegex(ValueError, 'OUTPUT_CHANGED'): self.run_derivation()


if __name__ == '__main__':
    unittest.main()
