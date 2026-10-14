"""Pure, source-bound envelope for preserved land export bytes; no I/O."""
from .land_records import MAX_BYTES, SOURCES, canonical, digest, instant, source_url


def capture_export(source, raw, *, url, retrieved_at, format, documents=()):
    """Shared envelope for already obtained official bytes. No source role inference.

    Browser text is a rendered derivative; a mapped CSV may be a transcription
    or export and must be checked against its attached original document.
    """
    source_url(source, url)
    instant(retrieved_at)
    if format not in SOURCES[source]["formats"] or not isinstance(raw, bytes) or not 0 < len(raw) <= MAX_BYTES:
        raise ValueError("CAPTURE_FORMAT_OR_SIZE_INVALID")
    objects = {digest(raw): raw}
    attachments = []
    total = len(raw)
    if len(documents) > 10:
        raise ValueError("DOCUMENT_COUNT_LIMIT")
    for document_url, content in documents:
        source_url(source, document_url)
        if not isinstance(content, bytes) or not 0 < len(content) <= MAX_BYTES:
            raise ValueError("DOCUMENT_SIZE_LIMIT")
        total += len(content)
        if total > MAX_BYTES:
            raise ValueError("CAPTURE_TOTAL_BYTE_LIMIT")
        sha = digest(content)
        objects[sha] = content
        attachments.append({"source_url": document_url, "sha256": sha, "bytes": len(content)})
    manifest = {"profile": "kfm.land-records-capture/v1", "source_id": source, "source_url": url,
                "retrieved_at": retrieved_at, "format": format, "capture_method": "BROWSER_DOM_TEXT" if format == "glo-text" else "EXPLICIT_EXPORT_OR_TRANSCRIPTION",
                "payload_sha256": digest(raw), "bytes": len(raw), "documents": attachments,
                "total_bytes": total, "source_admission": "PENDING", "release_state": "UNRELEASED"}
    manifest["capture_id"] = digest(canonical(manifest))
    return manifest, objects
