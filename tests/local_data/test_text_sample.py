"""Resource limits, corrupt input and scope reporting for gzip text samples."""
import gzip
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch

from tools.local_data import text_sample as sample


class TextSampleTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path=Path(self.temp.name)/'notes.txt.gz'

    def extract(self,content):
        self.path.write_bytes(content)
        return sample.gzip_text(self.path)

    def test_small_text_has_validated_first_member_and_exact_sample(self):
        text='Synthetic Kansas river notes.\nCafé, water, QA only.\n'
        value=self.extract(gzip.compress(text.encode()))
        self.assertEqual(value['text'],text)
        for key in ('first_member_complete','whole_file_complete','crc_validated'):
            self.assertTrue(value['inspection'][key])
        self.assertFalse(value['inspection']['text_truncated'])
        self.assertEqual(value['inspection']['issues'],[])

    def test_high_expansion_never_materializes_more_than_the_expanded_limit(self):
        value=self.extract(gzip.compress(b'water '*1_000_000))
        self.assertEqual(value['inspection']['expanded_bytes'],sample.EXPANDED_LIMIT)
        self.assertLessEqual(len(value['text']),sample.TEXT_LIMIT)
        self.assertEqual(value['inspection']['stop_reason'],'expanded_limit')
        self.assertFalse(value['inspection']['crc_validated'])
        self.assertTrue(value['inspection']['text_truncated'])

    def test_long_gzip_header_cannot_exceed_compressed_input_limit(self):
        # FNAME with no terminator in the allowed prefix produces no text.
        content=b'\x1f\x8b\x08\x08'+b'\0'*6+b'x'*(sample.COMPRESSED_LIMIT+100)
        value=self.extract(content)
        self.assertEqual(value['inspection']['compressed_bytes_read'],sample.COMPRESSED_LIMIT)
        self.assertEqual(value['inspection']['stop_reason'],'compressed_limit')
        self.assertEqual(value['text'],'')
        self.assertIn('GZIP_TEXT_EMPTY',value['inspection']['issues'])

    def test_invalid_header_truncation_and_bad_crc_are_reported(self):
        valid=gzip.compress(b'Synthetic water notes for local QA.')
        bad_crc=valid[:-8]+bytes([valid[-8]^255])+valid[-7:]
        for content in (b'not gzip',valid[:-5],bad_crc):
            with self.subTest(content=content[:10]):
                value=self.extract(content)
                self.assertIn('GZIP_INVALID_OR_TRUNCATED',value['inspection']['issues'])
                self.assertFalse(value['inspection']['crc_validated'])

    def test_concatenated_or_trailing_data_is_not_silently_treated_as_complete(self):
        first=gzip.compress(b'Visible QA water notes.')
        for tail in (gzip.compress(b'Hidden second member.'),b'trailing bytes'):
            value=self.extract(first+tail)
            self.assertEqual(value['text'],'Visible QA water notes.')
            self.assertTrue(value['inspection']['first_member_complete'])
            self.assertFalse(value['inspection']['whole_file_complete'])
            self.assertIn('GZIP_TRAILING_MEMBERS_OR_DATA_NOT_INSPECTED',value['inspection']['issues'])

    def test_binary_disguised_as_text_is_not_supplied_to_the_model(self):
        value=self.extract(gzip.compress(b'water\0\xff'*100))
        self.assertEqual(value['text'],'')
        self.assertIn('GZIP_TEXT_NOT_PLAINTEXT_UTF8',value['inspection']['issues'])

    def test_utf8_code_point_cut_at_the_output_bound_is_not_a_decode_error(self):
        with patch.object(sample,'EXPANDED_LIMIT',11):
            value=self.extract(gzip.compress(('水'*50).encode()))
        self.assertEqual(value['text'],'水'*3)
        self.assertEqual(value['inspection']['decode_replacements'],0)

    def test_symlink_is_refused(self):
        real=Path(self.temp.name)/'real.gz'
        real.write_bytes(gzip.compress(b'water notes'))
        self.path.symlink_to(real)
        with self.assertRaisesRegex(ValueError,'SYMLINK_OR_SPECIAL'):
            sample.gzip_text(self.path)


if __name__=='__main__':
    unittest.main()
