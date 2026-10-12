"""Tiny synthetic geospatial files for intake tests; no Kansas data is embedded."""
from __future__ import annotations

import io
import struct
import zipfile


def geotiff(width=10, height=20, *, origin=(-98.0, 39.0), pixel=(0.01, 0.01), epsg=4326, geographic=True) -> bytes:
    """Little-endian single-strip GeoTIFF with tiepoint, pixel scale and GeoKeys."""
    pixels = bytes(width * height)
    keys = [1, 1, 0, 3, 1024, 0, 1, 2 if geographic else 1, 1025, 0, 1, 1,
            2048 if geographic else 3072, 0, 1, epsg]
    entries = [
        (256, 3, 1, struct.pack("<H", width)), (257, 3, 1, struct.pack("<H", height)),
        (258, 3, 1, struct.pack("<H", 8)), (259, 3, 1, struct.pack("<H", 1)),
        (262, 3, 1, struct.pack("<H", 1)), (273, 4, 1, None), (277, 3, 1, struct.pack("<H", 1)),
        (278, 3, 1, struct.pack("<H", height)), (279, 4, 1, struct.pack("<I", len(pixels))),
        (306, 2, 20, b"2024:05:01 12:00:00\0"),
        (33550, 12, 3, struct.pack("<3d", pixel[0], pixel[1], 0.0)),
        (33922, 12, 6, struct.pack("<6d", 0, 0, 0, origin[0], origin[1], 0)),
        (34735, 3, len(keys), struct.pack("<%dH" % len(keys), *keys)),
    ]
    ifd_offset = 8
    data_offset = ifd_offset + 2 + 12 * len(entries) + 4
    blobs, body = [], b""
    for tag, typ, count, value in entries:
        if value is not None and len(value) > 4:
            blobs.append((tag, data_offset + len(body)))
            body += value + (b"\0" if len(value) % 2 else b"")
    strip_offset = data_offset + len(body)
    out = b"II*\0" + struct.pack("<I", ifd_offset) + struct.pack("<H", len(entries))
    pointers = dict(blobs)
    for tag, typ, count, value in entries:
        if tag == 273:
            field = struct.pack("<I", strip_offset)
        elif tag in pointers:
            field = struct.pack("<I", pointers[tag])
        else:
            field = value.ljust(4, b"\0")
        out += struct.pack("<HHI", tag, typ, count) + field
    return out + b"\0\0\0\0" + body + pixels


def shapefile_zip(*, bbox=(-99.5, 37.5, -97.0, 39.5), prj='GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983"]]',
                  fields=("WELL_ID", "DEPTH_FT", "DATE_DRILL"), records=3, stem="kgs_wells") -> bytes:
    shp = struct.pack(">i", 9994) + bytes(20) + struct.pack(">i", 50) + struct.pack("<ii", 1000, 1) + struct.pack("<4d", *bbox) + bytes(32)
    header_len = 32 + 32 * len(fields) + 1
    dbf = bytes([3, 124, 1, 1]) + struct.pack("<IHH", records, header_len, 11) + bytes(20)
    for name in fields:
        dbf += name.encode().ljust(11, b"\0") + b"C" + bytes(4) + bytes([10, 0]) + bytes(14)
    dbf += b"\x0d"
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr(stem + ".shp", shp)
        archive.writestr(stem + ".dbf", dbf)
        if prj is not None:
            archive.writestr(stem + ".prj", prj)
    return buffer.getvalue()


def las(bbox=(-98.2, 38.1, -98.1, 38.2), points=1234) -> bytes:
    head = bytearray(227)
    head[0:4] = b"LASF"
    head[24], head[25] = 1, 2
    head[107:111] = struct.pack("<I", points)
    head[179:227] = struct.pack("<6d", bbox[2], bbox[0], bbox[3], bbox[1], 400.0, 300.0)
    return bytes(head)


def pmtiles(bbox=(-102.0, 37.0, -94.6, 40.0)) -> bytes:
    head = bytearray(127)
    head[0:7] = b"PMTiles"
    head[7] = 3
    head[99], head[100], head[101] = 1, 0, 12
    head[102:118] = struct.pack("<4i", *(round(v * 1e7) for v in bbox))
    return bytes(head)


def jpeg_with_gps(lon=-97.3375, lat=37.6922) -> bytes:
    """Minimal JPEG with an EXIF GPS IFD and DateTimeOriginal (not a decodable image)."""
    def dms(value):
        value = abs(value)
        d = int(value)
        m = int((value - d) * 60)
        s = round(((value - d) * 60 - m) * 60 * 1000)
        return struct.pack("<6I", d, 1, m, 1, s, 1000)
    # TIFF header, IFD0 (2 entries) at 8, ExifIFD at 38, GPS IFD at 56, data after.
    ifd0 = 8
    exif_ifd = ifd0 + 2 + 2 * 12 + 4
    gps_ifd = exif_ifd + 2 + 12 + 4
    data = gps_ifd + 2 + 4 * 12 + 4
    when = b"2019:06:02 10:30:00\0"
    lat_at, lon_at, when_at = data, data + 24, data + 48
    t = b"II*\0" + struct.pack("<I", ifd0)
    t += struct.pack("<H", 2) + struct.pack("<HHII", 0x8769, 4, 1, exif_ifd) + struct.pack("<HHII", 0x8825, 4, 1, gps_ifd) + bytes(4)
    t += struct.pack("<H", 1) + struct.pack("<HHII", 0x9003, 2, len(when), when_at) + bytes(4)
    t += struct.pack("<H", 4)
    t += struct.pack("<HHI", 1, 2, 2) + (b"N" if lat >= 0 else b"S") + bytes(3)
    t += struct.pack("<HHII", 2, 5, 3, lat_at)
    t += struct.pack("<HHI", 3, 2, 2) + (b"E" if lon >= 0 else b"W") + bytes(3)
    t += struct.pack("<HHII", 4, 5, 3, lon_at) + bytes(4)
    t += dms(lat) + dms(lon) + when
    app1 = b"Exif\0\0" + t
    return b"\xff\xd8" + b"\xff\xe1" + struct.pack(">H", len(app1) + 2) + app1 + b"\xff\xc0" + struct.pack(">HBHH", 11, 8, 480, 640) + b"\x01\x01\x11\x00" + b"\xff\xd9"


GEOJSON = b"""{"type":"FeatureCollection","features":[
{"type":"Feature","properties":{"site":"gauge 1","obs_date":"2021-03-04","discharge_cfs":120},"geometry":{"type":"Point","coordinates":[-97.5,38.2]}},
{"type":"Feature","properties":{"site":"gauge 2","obs_date":"2023-08-09","discharge_cfs":95},"geometry":{"type":"Point","coordinates":[-96.1,39.4]}}]}"""

CSV = b"station,latitude,longitude,date,precip_in\nA,38.5,-98.0,1951-01-01,0.1\nB,39.1,-95.7,2020-12-31,0.0\nC,bad,-95.7,not-a-date,\n"

PDF = b"%PDF-1.7\n1 0 obj << /Type /Pages /Kids [] /Count 12 >> endobj\n2 0 obj << /CreationDate (D:19980315000000) >> endobj\n%%EOF\n"

KML = b'<?xml version="1.0"?><kml xmlns="http://www.opengis.net/kml/2.2"><Document><Placemark><when>1870-05-01</when><Point><coordinates>-97.6,38.8,0</coordinates></Point></Placemark><Placemark><LineString><coordinates>-98.0,38.0 -97.0,39.0</coordinates></LineString></Placemark></Document></kml>'
