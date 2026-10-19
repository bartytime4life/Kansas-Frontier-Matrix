"""Synthetic, offline regression tests for restricted candidate storage."""
import contextlib
import gzip
import importlib.util
import io
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import types
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    'subsurface', Path(__file__).resolve().parents[1] / 'scripts/prepare-subsurface.py')
SUBSURFACE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SUBSURFACE)
PYPROJ = types.SimpleNamespace(__version__='3.7.1', proj_version_str='synthetic',
    Transformer=types.SimpleNamespace(from_pipeline=lambda _: None))
ROWS = {
    'wwc5_wells': [{'WELL_ID': '000', 'NAD83_LONGITUDE': '-99', 'NAD83_LATITUDE': '38',
        'WELL_DEPTH': '10', 'LONG_LAT_TYPE': 'GPS', 'COMPLE_DATE': '10-Jul-1978',
        'COUNTY': 'Synthetic'}],
    'wwc5_lith_log': [{'WELL_ID': '000', 'TOP': '0', 'BOTTOM': '10', 'LOG': 'synthetic shale'}],
    'interpreted_logs': [], 'coreLib': [],
}


class RestrictedStorageTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='kfm-private-output-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.inputs = self.root / 'cache'
        self.output = self.root / 'quarantine' / 'candidate'
        self.downloads = 0
        old_umask = os.umask(0o022)
        self.addCleanup(os.umask, old_umask)

    def build(self, output=None, during_download=None):
        def download(*_):
            self.downloads += 1
            if self.downloads == 1 and during_download:
                during_download()
        with patch.dict('sys.modules', {'pyproj': PYPROJ}), \
                patch.object(SUBSURFACE, 'pinned_download', side_effect=download), \
                patch.object(SUBSURFACE, 'rows', side_effect=lambda _, name, stats: iter(ROWS[name])), \
                contextlib.redirect_stdout(io.StringIO()):
            SUBSURFACE.build(self.inputs, output or self.output)

    def reject_before_download(self, output):
        with self.assertRaises(ValueError):
            self.build(output)
        self.assertEqual(self.downloads, 0)
        self.assertFalse(self.inputs.exists())

    def test_external_empty_directory_symlink_is_rejected(self):
        target = self.root / 'elsewhere'
        target.mkdir(mode=0o700)
        alias = self.root / 'alias'
        alias.symlink_to(target, target_is_directory=True)
        self.reject_before_download(alias)
        self.assertEqual(list(target.iterdir()), [])

    def test_dangling_output_symlink_is_rejected(self):
        alias = self.root / 'alias'
        alias.symlink_to(self.root / 'missing', target_is_directory=True)
        self.reject_before_download(alias)
        self.assertFalse((self.root / 'missing').exists())

    def test_symlink_ancestor_is_rejected(self):
        target = self.root / 'elsewhere'
        target.mkdir(mode=0o700)
        alias = self.root / 'alias'
        alias.symlink_to(target, target_is_directory=True)
        self.reject_before_download(alias / 'nested' / 'candidate')
        self.assertEqual(list(target.iterdir()), [])

    def test_permissive_parents_are_rejected_without_chmod(self):
        for mode in (0o755, 0o770, 0o777):
            with self.subTest(mode=oct(mode)):
                parent = self.root / str(mode)
                parent.mkdir()
                parent.chmod(mode)
                self.reject_before_download(parent / 'candidate')
                self.assertEqual(stat.S_IMODE(parent.stat().st_mode), mode)

    def test_permissive_empty_output_is_rejected_without_chmod(self):
        output = self.root / 'candidate'
        output.mkdir(mode=0o755)
        self.reject_before_download(output)
        self.assertEqual(stat.S_IMODE(output.stat().st_mode), 0o755)

    def test_foreign_owned_parent_is_rejected(self):
        original_fstat = os.fstat
        identity = self.root.stat()
        def foreign_owner(descriptor):
            info = original_fstat(descriptor)
            if (info.st_dev, info.st_ino) == (identity.st_dev, identity.st_ino):
                values = list(info)
                values[4] = os.geteuid() + 1
                return os.stat_result(values)
            return info
        with patch.object(os, 'fstat', side_effect=foreign_owner):
            self.reject_before_download(self.root / 'candidate')

    def test_foreign_owned_empty_output_is_rejected(self):
        self.output.mkdir(parents=True, mode=0o700)
        self.output.parent.chmod(0o700)
        original_fstat = os.fstat
        identity = self.output.stat()
        def foreign_owner(descriptor):
            info = original_fstat(descriptor)
            if (info.st_dev, info.st_ino) == (identity.st_dev, identity.st_ino):
                values = list(info)
                values[4] = os.geteuid() + 1
                return os.stat_result(values)
            return info
        with patch.object(os, 'fstat', side_effect=foreign_owner):
            self.reject_before_download(self.output)

    def test_cli_rejects_external_symlink_before_dependencies_or_downloads(self):
        target = self.root / 'elsewhere'
        target.mkdir(mode=0o700)
        alias = self.root / 'alias'
        alias.symlink_to(target, target_is_directory=True)
        result = subprocess.run([sys.executable, '-B', str(SPEC.origin),
            '--input-dir', str(self.inputs), '--output-dir', str(alias)],
            capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn('without symlinks', result.stderr)
        self.assertFalse(self.inputs.exists())
        self.assertEqual(list(target.iterdir()), [])

    def test_unsupported_platform_fails_closed(self):
        with patch.object(os, 'supports_dir_fd', set()):
            self.reject_before_download(self.output)

    def test_nonempty_output_and_regular_file_are_rejected(self):
        output = self.root / 'candidate'
        output.mkdir(mode=0o700)
        sentinel = output / 'keep'
        sentinel.write_bytes(b'unchanged')
        self.reject_before_download(output)
        self.reject_before_download(sentinel)
        self.assertEqual(sentinel.read_bytes(), b'unchanged')

    def test_validation_is_nonmutating(self):
        SUBSURFACE.validate_storage(self.inputs, self.output)
        self.assertFalse(self.inputs.exists())
        self.assertFalse(self.output.parent.exists())

    def test_private_nested_and_existing_empty_outputs_preserve_bytes_and_modes(self):
        self.build()
        second = self.root / 'existing'
        second.mkdir(mode=0o700)
        self.build(second)
        for directory in (self.output.parent, self.output, second):
            self.assertEqual(stat.S_IMODE(directory.stat().st_mode), 0o700)
        first_files = {file.name: file.read_bytes() for file in self.output.iterdir()}
        self.assertEqual(first_files, {file.name: file.read_bytes() for file in second.iterdir()})
        for file in (*self.output.iterdir(), *second.iterdir()):
            self.assertEqual(stat.S_IMODE(file.stat().st_mode), 0o600)
        manifest = json.loads(first_files['manifest.json'])
        self.assertEqual(manifest['status'], 'RESTRICTED_REVIEW_REQUIRED')
        self.assertEqual(manifest['locator']['url'], 'locator.json.gz')
        self.assertEqual(manifest['totals']['wellCount'], 1)
        for tile in manifest['tiles']:
            data = first_files[tile['url']]
            self.assertEqual(SUBSURFACE.digest(data), tile['sha256'])
            self.assertEqual(len(data), tile['bytes'])
            self.assertEqual(json.loads(gzip.decompress(data))[0]['intervals'],
                [{'top': 0.0, 'bottom': 10.0, 'description': 'synthetic shale'}])

    def test_relative_private_output_remains_supported(self):
        previous = Path.cwd()
        try:
            os.chdir(self.root)
            self.build(Path('quarantine/candidate'))
        finally:
            os.chdir(previous)
        self.assertTrue((self.output / 'manifest.json').is_file())

    def test_output_replacement_during_download_cannot_redirect_artifacts(self):
        target = self.root / 'elsewhere'
        target.mkdir(mode=0o700)
        original = self.root / 'original'
        def replace():
            self.output.mkdir(parents=True, exist_ok=True, mode=0o700)
            self.output.rename(original)
            self.output.symlink_to(target, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.build(during_download=replace)
        self.assertEqual(list(target.iterdir()), [])
        self.assertFalse((original / 'manifest.json').exists())

    def test_ancestor_replacement_cannot_redirect_artifacts(self):
        target = self.root / 'elsewhere'
        target.mkdir(mode=0o700)
        (target / 'candidate').mkdir(mode=0o700)
        original = self.root / 'original'
        def replace():
            self.output.mkdir(parents=True, exist_ok=True, mode=0o700)
            self.output.parent.rename(original)
            self.output.parent.symlink_to(target, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.build(during_download=replace)
        self.assertEqual(list((target / 'candidate').iterdir()), [])
        self.assertFalse((original / 'candidate' / 'manifest.json').exists())

    def test_replacement_with_real_directory_is_detected_before_manifest(self):
        original = self.root / 'original'
        def replace():
            self.output.rename(original)
            self.output.mkdir(mode=0o700)
        with self.assertRaisesRegex(ValueError, 'changed during preparation'):
            self.build(during_download=replace)
        self.assertEqual(list(self.output.iterdir()), [])
        self.assertFalse((original / 'manifest.json').exists())

    def test_child_links_and_existing_files_are_never_overwritten(self):
        for name in ('tile-162-256.json.gz', 'locator.json.gz', 'manifest.json'):
            for kind in ('symlink', 'hardlink', 'file', 'directory', 'fifo'):
                with self.subTest(name=name, kind=kind):
                    output = self.root / (name + '-' + kind)
                    target = self.root / ('keep-' + name + '-' + kind)
                    target.write_bytes(b'unchanged')
                    self.downloads = 0
                    def insert():
                        output.mkdir(mode=0o700, exist_ok=True)
                        child = output / name
                        if kind == 'symlink':
                            child.symlink_to(target)
                        elif kind == 'hardlink':
                            os.link(target, child)
                        elif kind == 'directory':
                            child.mkdir()
                        elif kind == 'fifo':
                            os.mkfifo(child)
                        else:
                            child.write_bytes(b'unchanged')
                    with self.assertRaises((ValueError, OSError)):
                        self.build(output, during_download=insert)
                    self.assertEqual(target.read_bytes(), b'unchanged')
                    if kind in ('symlink', 'hardlink', 'file'):
                        self.assertEqual((output / name).read_bytes(), b'unchanged')


if __name__ == '__main__':
    unittest.main(verbosity=2)
