"""Bounded image-header checks for pinned private document previews."""
import struct


def image_metadata(raw: bytes, suffix: str):
    """Check format and declared dimensions without decoding or transforming pixels.

    Browser decoding remains separate from these structural checks. JPEG supports
    the wider publisher map sheet while retaining the PNG reader's pixel budget.
    """
    if suffix == '.png':
        if len(raw) < 33 or raw[:16] != b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR':
            raise ValueError('REVIEW_IMAGE_INVALID')
        width, height = struct.unpack('>II', raw[16:24])
        edge, media = 4096, 'image/png'
    elif suffix in {'.jpg', '.jpeg'}:
        if not raw.startswith(b'\xff\xd8') or not raw.endswith(b'\xff\xd9'):
            raise ValueError('REVIEW_IMAGE_INVALID')
        width = height = None
        offset = 2
        for _ in range(128):
            if offset + 4 > min(len(raw), 1024 * 1024) or raw[offset] != 0xFF:
                raise ValueError('REVIEW_IMAGE_INVALID')
            marker = raw[offset + 1]
            length = int.from_bytes(raw[offset + 2:offset + 4], 'big')
            end = offset + 2 + length
            if length < 2 or end > min(len(raw), 1024 * 1024):
                raise ValueError('REVIEW_IMAGE_INVALID')
            if marker in {0xC0, 0xC2}:
                if width is not None or length < 8:
                    raise ValueError('REVIEW_IMAGE_INVALID')
                depth, height, width, components = struct.unpack('>BHHB', raw[offset + 4:offset + 10])
                if depth != 8 or components not in {1, 3} or length != 8 + 3 * components:
                    raise ValueError('REVIEW_IMAGE_INVALID')
            elif marker == 0xDA:
                if width is None or length < 6:
                    raise ValueError('REVIEW_IMAGE_INVALID')
                break
            elif marker not in {0xC4, 0xDB, 0xDD, 0xFE, *range(0xE0, 0xF0)}:
                raise ValueError('REVIEW_IMAGE_INVALID')
            offset = end
        else:
            raise ValueError('REVIEW_IMAGE_INVALID')
        edge, media = 8192, 'image/jpeg'
    else:
        raise ValueError('REVIEW_IMAGE_INVALID')
    if not 1 <= width <= edge or not 1 <= height <= edge or width * height > 16_000_000:
        raise ValueError('REVIEW_IMAGE_LIMIT')
    return {'width': width, 'height': height, 'media_type': media}
