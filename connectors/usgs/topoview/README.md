# USGS topoView capture

`fetch_sheet.py` accepts one Kansas sheet request returned by the Site queue.
It searches the official TNM product API, requires a unique GeoTIFF match for
the scan ID, edition, name and scale, then streams the unmodified source bytes
to the worker, which writes the RAW original and retrieval receipt. It rejects redirects,
unexpected media, oversize or incomplete downloads, non-Kansas requests, and
ambiguous matches. It never creates an activated Site layer.

The request record comes from the Site's exact-ID topoView lookup, not from an
untrusted download URL. Store captures outside this checkout and preserve
them for verification and rollback. The GeoTIFF may include map collar beyond
its catalog footprint; the transformation keeps the full source image.
