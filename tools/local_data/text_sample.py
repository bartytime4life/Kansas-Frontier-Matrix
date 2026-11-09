"""Bounded, in-memory first-member samples of gzip-compressed UTF-8 text."""
import codecs
import hashlib
import os
import zlib

from tools.local_data.file_io import open_regular

VERSION = "gzip-text-prefix-v1"
COMPRESSED_LIMIT = 256 * 1024
EXPANDED_LIMIT = 48 * 1024
TEXT_LIMIT = 6000
CHUNK_BYTES = 16 * 1024


def gzip_text(path):
    """Never unpack to disk, follow names, traverse members, or expand unboundedly."""
    info = {"version":VERSION,"method":"gzip UTF-8 first-member prefix",
        "compressed_byte_limit":COMPRESSED_LIMIT,"expanded_byte_limit":EXPANDED_LIMIT,
        "text_character_limit":TEXT_LIMIT,"compressed_bytes_read":0,"expanded_bytes":0,
        "text_characters":0,"first_member_complete":False,"whole_file_complete":False,
        "crc_validated":False,"stop_reason":"","issues":[]}
    output = bytearray()
    decoder = zlib.decompressobj(16 + zlib.MAX_WBITS)
    fd = open_regular(path)
    with os.fdopen(fd,"rb") as source:
        size = os.fstat(source.fileno()).st_size
        try:
            while len(output) < EXPANDED_LIMIT and info["compressed_bytes_read"] < COMPRESSED_LIMIT:
                chunk = source.read(min(CHUNK_BYTES,COMPRESSED_LIMIT-info["compressed_bytes_read"]))
                if not chunk:
                    info["stop_reason"] = "incomplete_stream"
                    info["issues"].append("GZIP_INVALID_OR_TRUNCATED")
                    break
                info["compressed_bytes_read"] += len(chunk)
                output.extend(decoder.decompress(chunk,EXPANDED_LIMIT-len(output)))
                if decoder.eof:
                    info["first_member_complete"] = info["crc_validated"] = True
                    info["whole_file_complete"] = not decoder.unused_data and info["compressed_bytes_read"] == size
                    info["stop_reason"] = "end_of_member"
                    if not info["whole_file_complete"]:
                        info["issues"].append("GZIP_TRAILING_MEMBERS_OR_DATA_NOT_INSPECTED")
                    break
            else:
                info["stop_reason"] = "expanded_limit" if len(output) >= EXPANDED_LIMIT else "compressed_limit"
        except zlib.error:
            info["stop_reason"] = "invalid_stream"
            info["issues"].append("GZIP_INVALID_OR_TRUNCATED")
    info["expanded_bytes"] = len(output)
    # An incremental decoder avoids treating a code point cut by our byte limit
    # as corrupt. Actual invalid UTF-8 and binary controls still cause a hold.
    text = codecs.getincrementaldecoder("utf-8")("replace").decode(bytes(output),final=info["first_member_complete"])
    decoded_length = len(text)
    info["decode_replacements"] = text.count("\ufffd")
    controls = sum(ord(c)<32 and c not in "\t\n\r\f" for c in text)
    if "\0" in text or text.count("\ufffd") > max(1,len(text)//100) or controls > max(1,len(text)//100):
        info["issues"].append("GZIP_TEXT_NOT_PLAINTEXT_UTF8")
        text = ""
    text = text[:TEXT_LIMIT]
    if not text.strip():
        info["issues"].append("GZIP_TEXT_EMPTY")
    info["text_characters"] = len(text)
    info["text_truncated"] = not info["whole_file_complete"] or len(text) < decoded_length
    info["text_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    return {"text":text,"inspection":info}
