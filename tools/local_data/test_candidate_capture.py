"""The connector output boundary never writes a released or repository path."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.local_data.candidate_capture import REPOSITORY, create_candidate, write_candidate


class CandidateCaptureTests(unittest.TestCase):
    def test_external_immutable_private_capture(self):
        with TemporaryDirectory() as folder:
            directory = Path(folder) / "candidate"
            create_candidate(directory)
            write_candidate(directory, "source.geojson", b"captured bytes")
            self.assertEqual((directory / "source.geojson").read_bytes(), b"captured bytes")
            self.assertEqual(directory.stat().st_mode & 0o077, 0)
            with self.assertRaises(FileExistsError):
                write_candidate(directory, "source.geojson", b"replacement")
            with self.assertRaises(ValueError):
                write_candidate(directory, "../released.json", b"bad")

    def test_repository_and_symlink_targets_denied(self):
        with self.assertRaisesRegex(ValueError, "CANDIDATE_INSIDE_REPOSITORY"):
            create_candidate(REPOSITORY / "data" / "published" / "candidate")
        with TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "link").symlink_to(root, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "DIRECTORY_SYMLINK_OR_SPECIAL"):
                create_candidate(root / "link" / "candidate")


if __name__ == "__main__":
    unittest.main()
