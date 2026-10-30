"""Pinned road-map documents retain dates, source bytes and review boundaries."""
import copy
import json
from pathlib import Path
import struct
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from tools.local_data import historical_roads as roads
from tools.local_data.file_io import write_new
from tools.local_data.manage import init_store
from tools.local_data.review_packages import ReviewPackages


class HistoricalRoadsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name); self.archive = self.base/'archive'; self.root = self.base/'working'
        init_store(self.root)
        self.pdf = b'%PDF-1.7\nsynthetic one-page fixture\n%%EOF\n'
        self.png = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + struct.pack('>II', 3600, 2330) + b'\x08\x02' + b'\0'*7
        self.recipe = dict(roads.RECIPE, version='26.05.0')
        write_new(self.archive/roads.SOURCE, self.pdf)
        self.record = {'id': 'kfm:map-document:'+roads.RECORD_ID, 'collection': 'Kansas Road Maps',
                       'edition_start_year': 1918, 'edition_end_year': 1918, 'filename_conflict': False,
                       'published': False, 'released': False, 'review_state': 'PENDING',
                       'rights': 'SOURCE_SPECIFIC_REVIEW_REQUIRED', 'sensitivity': 'INFRASTRUCTURE_CONTEXT_REVIEW_REQUIRED',
                       'sha256': roads.digest(self.pdf), 'bytes': len(self.pdf), 'source_path': '/unrelated/old/PC/1918 Kansas.pdf',
                       'ocr_text': 'Approved August 7, 1918', 'pdf_metadata': {'creation_date': '2025-09-14'}}
        self.manifest = {'profile': 'kfm-map-document-review/v1', 'review_state': 'PENDING', 'published': False,
                         'released': False, 'rights': self.record['rights'], 'sensitivity': self.record['sensitivity']}
        self.q = {'schema': 'kfm-historical-reference-qualification/v1', 'state': 'QUALIFIED_FOR_PRIVATE_DOCUMENT_PREPARATION',
                  'titleOnSheet': 'Official Map, Kansas State Roads', 'issuingBodyOnSheet': 'Kansas Highway Commission',
                  'printedApprovalDate': '1918-08-07', 'printedDateText': 'Approved August 7, 1918',
                  'authority': dict(roads.AUTHORITY), 'georeferencingVerified': False, 'geometry': None,
                  'sourceObservationInterval': None, 'featureConstructionDates': None,
                  'rights': self.record['rights'], 'sensitivity': self.record['sensitivity'],
                  'providerChecksumVerified': False, 'originalAcquisitionUrl': None,
                  'source': {'path': '/unrelated/source.pdf', 'sha256': roads.digest(self.pdf), 'bytes': len(self.pdf)},
                  'render': {'path': '/unrelated/render.png', 'sha256': roads.digest(self.png), 'bytes': len(self.png)},
                  'renderRecipe': dict(self.recipe, dimensions=[3600,2330])}
        self.qpath = self.base/'qualification.json'
        self.pin_all()
        self.renderer = patch.object(roads, 'render_pdf', return_value=(self.png, self.recipe)).start()
        self.addCleanup(patch.stopall)

    def pin_all(self):
        record = roads.canonical(self.record); path = self.archive/roads.PACKAGE/roads.RECORD
        path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(record)
        self.manifest['outputs'] = [{'file': str(roads.RECORD), 'sha256': roads.digest(record), 'bytes': len(record)}]
        manifest = roads.canonical(self.manifest)
        (self.archive/roads.PACKAGE/'review-manifest.json').write_bytes(manifest)
        self.q['sourceRecord'] = {'sha256': roads.digest(record)}
        self.q['sourceReviewManifest'] = {'sha256': roads.digest(manifest)}
        self.pin_q()

    def pin_q(self):
        raw = roads.canonical(self.q); self.qpath.write_bytes(raw); self.qpin = roads.digest(raw)

    def derive(self, root=None):
        return roads.derive(self.archive, root or self.root, self.qpath, self.qpin)

    def test_offline_idempotent_package_retains_source_and_private_date_limits(self):
        originals = {str(p):p.read_bytes() for p in self.archive.rglob('*') if p.is_file()}
        with patch('socket.socket.connect', side_effect=AssertionError('network forbidden')):
            result = self.derive(); self.assertEqual(result, self.derive())
        directory = (self.root/result['binding'].split('@')[0]).parent
        self.assertEqual((directory/'retained/source-map.pdf').read_bytes(), self.pdf)
        self.assertEqual((directory/'source-record.json').read_bytes(), roads.canonical(self.record))
        model = ReviewPackages(self.root, [result['binding']]); package = model.catalog()['packages'][0]
        self.assertEqual(package['title'], 'Historical Kansas road map')
        self.assertFalse(any(m['name'].endswith('.pdf') for m in package['members']))
        member = next(m for m in package['members'] if m['name']=='page-1.png')
        self.assertEqual(model.preview(package['id'], member['id']), (self.png, 'image/png'))
        with self.assertRaisesRegex(ValueError, 'MEMBER_UNKNOWN'):
            model.preview(package['id'], '0'*64)
        coverage = json.loads((directory/'coverage.json').read_bytes())
        self.assertEqual(coverage['printed_map_approval_date'], '1918-08-07')
        for key in ('source_observation_interval','feature_construction_dates','geometry','original_acquisition_url'):
            self.assertIsNone(coverage[key])
        self.assertFalse(coverage['georeferencing_verified']); self.assertFalse(coverage['provider_checksum_verified'])
        self.assertFalse(any(coverage['authority'].values()))
        self.assertEqual(originals, {str(p):p.read_bytes() for p in self.archive.rglob('*') if p.is_file()})

    def test_rehashed_qualification_cannot_change_date_rights_or_authority(self):
        old = copy.deepcopy(self.q)
        for key, value in [('printedApprovalDate','2025-09-14'), ('rights','PUBLIC'), ('providerChecksumVerified', True),
                           ('geometry', {'type':'Point'}), ('authority',dict(roads.AUTHORITY, publication=True))]:
            with self.subTest(key=key):
                self.q = copy.deepcopy(old); self.q[key] = value; self.pin_q()
                with self.assertRaisesRegex(ValueError, 'QUALIFICATION_INVALID'): self.derive()
        self.renderer.assert_not_called()

    def test_record_must_be_bound_and_keep_archived_review_holds(self):
        self.q['sourceRecord']['sha256'] = '0'*64; self.pin_q()
        with self.assertRaisesRegex(ValueError, 'RECORD_NOT_BOUND'): self.derive()
        self.pin_all(); self.record['filename_conflict'] = True; self.pin_all()
        with self.assertRaisesRegex(ValueError, 'SOURCE_RECORD_INVALID'): self.derive()
        self.record['filename_conflict'] = False; self.manifest['released'] = True; self.pin_all()
        with self.assertRaisesRegex(ValueError, 'ARCHIVE_REVIEW_STATE'): self.derive()
        self.assertFalse((self.root/'data/work/roads_rail_trade').exists())

    def test_changed_input_pins_fail_before_rendering_or_writing(self):
        for path in (self.archive/roads.SOURCE, self.archive/roads.PACKAGE/roads.RECORD,
                     self.archive/roads.PACKAGE/'review-manifest.json', self.qpath):
            raw = path.read_bytes(); path.write_bytes(raw+b'\n')
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, 'PIN_CHANGED'): self.derive()
            path.write_bytes(raw)
        self.renderer.assert_not_called()

    def test_render_bytes_or_version_mismatch_never_writes_package(self):
        for image, recipe in ((self.png+b'changed', self.recipe), (self.png, dict(self.recipe, version='other'))):
            self.renderer.return_value = (image, recipe)
            with self.assertRaisesRegex(ValueError, 'RENDER_REPLAY_MISMATCH'): self.derive()
        self.assertFalse((self.root/'data/work/roads_rail_trade').exists())

    def test_separate_roots_symlinks_and_output_corruption_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'SEPARATE_DESTINATION'): self.derive(self.archive)
        path = self.archive/roads.SOURCE; path.rename(path.with_suffix('.saved')); path.symlink_to(path.with_suffix('.saved'))
        with self.assertRaisesRegex(ValueError, 'SYMLINK'): self.derive()
        path.unlink(); path.with_suffix('.saved').rename(path)
        result = self.derive(); directory = (self.root/result['binding'].split('@')[0]).parent
        extra = directory/'retained/extra.pdf'; extra.write_bytes(b'extra')
        with self.assertRaisesRegex(ValueError, 'CLOSURE_CHANGED'): self.derive()
        extra.unlink(); (directory/'retained/source-map.pdf').write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError, 'OUTPUT_CHANGED'): self.derive()


class RendererTests(unittest.TestCase):
    def test_fixed_command_reads_temporary_pinned_copy_and_cleans_up(self):
        seen = []
        def run(command, **kwargs):
            if command[-1] == '-v':
                return SimpleNamespace(stdout=b'', stderr=b'pdftoppm version 26.05.0\n')
            seen.append(command)
            self.assertEqual(command[1:7], ['-f','1','-singlefile','-scale-to','3600','-png'])
            self.assertEqual(Path(command[-2]).read_bytes(), b'%PDF-test')
            self.assertEqual(kwargs['timeout'], 45)
            Path(command[-1]+'.png').write_bytes(b'png output')
        with patch.object(roads.shutil, 'which', return_value='/installed/pdftoppm'), patch.object(roads.subprocess, 'run', side_effect=run):
            raw, recipe = roads.render_pdf(b'%PDF-test')
        self.assertEqual(raw, b'png output'); self.assertEqual(recipe['version'], '26.05.0')
        self.assertFalse(Path(seen[0][-2]).exists())

    def test_missing_renderer_and_render_timeout_fail(self):
        with patch.object(roads.shutil, 'which', return_value=None):
            with self.assertRaisesRegex(ValueError, 'UNAVAILABLE'): roads.render_pdf(b'%PDF-test')
        with patch.object(roads.shutil, 'which', return_value='/installed/pdftoppm'), patch.object(
                roads.subprocess, 'run', side_effect=subprocess.TimeoutExpired('pdftoppm', 5)):
            with self.assertRaises(subprocess.TimeoutExpired): roads.render_pdf(b'%PDF-test')


if __name__ == '__main__':
    unittest.main()
