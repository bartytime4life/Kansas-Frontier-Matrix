"""Document headers retain bounded decode dimensions and a narrow format list."""
import struct
import unittest

from tools.local_data.review_images import image_metadata


def jpeg(width=5004, height=2880, marker=0xC0):
    frame = struct.pack('>BHHB', 8, height, width, 3) + b'\x01\x11\0\x02\x11\0\x03\x11\0'
    scan = b'\x03\x01\0\x02\x11\x03\x11\0\x3f\0'
    return b'\xff\xd8\xff' + bytes([marker]) + struct.pack('>H', len(frame) + 2) + frame + b'\xff\xda' + struct.pack('>H', len(scan) + 2) + scan + b'\0\xff\xd9'


class ReviewImageTests(unittest.TestCase):
    def test_baseline_and_progressive_document_headers_preserve_dimensions(self):
        for marker in (0xC0, 0xC2):
            self.assertEqual(image_metadata(jpeg(marker=marker), '.jpg'),
                             {'width': 5004, 'height': 2880, 'media_type': 'image/jpeg'})

    def test_dimension_and_total_pixel_budgets(self):
        for width, height in ((8193, 1), (5004, 4000), (1, 0), (0, 1)):
            with self.subTest(width=width, height=height), self.assertRaisesRegex(ValueError, 'IMAGE_LIMIT'):
                image_metadata(jpeg(width, height), '.jpeg')

    def test_truncated_wrong_media_and_unsupported_frame_are_rejected(self):
        for raw in (b'<svg></svg>', jpeg()[:-2], jpeg()[:10] + b'\xff\xd9', jpeg(marker=0xC3),
                    b'\xff\xd8\xff\xe0\x00\x01\xff\xd9', b'\xff\xd8\xff\xda\x00\x08' + bytes(6) + b'\xff\xd9'):
            with self.subTest(raw=raw[:12]), self.assertRaisesRegex(ValueError, 'IMAGE_INVALID'):
                image_metadata(raw, '.jpg')
        with self.assertRaisesRegex(ValueError, 'IMAGE_INVALID'):
            image_metadata(jpeg(), '.png')

    def test_segment_count_and_header_budget(self):
        segment = b'\xff\xfe\x00\x02'
        with self.assertRaisesRegex(ValueError, 'IMAGE_INVALID'):
            image_metadata(b'\xff\xd8' + segment * 129 + jpeg()[2:], '.jpg')
        segment = b'\xff\xfe\xff\xff' + bytes(65533)
        with self.assertRaisesRegex(ValueError, 'IMAGE_INVALID'):
            image_metadata(b'\xff\xd8' + segment * 17 + jpeg()[2:], '.jpg')


if __name__ == '__main__':
    unittest.main()
