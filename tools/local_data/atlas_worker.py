#!/usr/bin/env python3
"""Isolated, bounded local spatial reader. Input is selected by Atlas, not a browser path.

Runs in an operator-selected Python environment with rasterio, numpy and pyshp.
Only GeoTIFF rasters and shapefiles are opened. Remote/VRT drivers are not used.
"""
from __future__ import annotations
import base64
import io
import json
import math
import os
from pathlib import Path, PurePosixPath
import resource
import stat
import sys
import zipfile

MAX_MEMBER = 64 * 1024**2
FEATURES = 5000


def regular(path):
    path = Path(path)
    if not path.is_absolute() or ".." in path.parts:
        raise ValueError("ATLAS_PATH_INVALID")
    for p in (path, *path.parents):
        mode = p.lstat().st_mode
        if stat.S_ISLNK(mode) or (p != path and not stat.S_ISDIR(mode)):
            raise ValueError("ATLAS_PATH_INVALID")
    if not stat.S_ISREG(path.lstat().st_mode):
        raise ValueError("ATLAS_PATH_INVALID")
    return path


def archive_members(z):
    infos = z.infolist()
    if len(infos) > 20000:
        raise ValueError("ATLAS_ARCHIVE_MEMBER_LIMIT")
    for i in infos:
        p = PurePosixPath(i.filename)
        if p.is_absolute() or ".." in p.parts or "\\" in i.filename or i.flag_bits & 1 or stat.S_ISLNK(i.external_attr >> 16):
            raise ValueError("ATLAS_ARCHIVE_UNSAFE")
    return infos


def raster(path, band):
    import numpy as np
    import rasterio
    from rasterio.enums import Resampling
    from rasterio.transform import from_bounds
    from rasterio.vrt import WarpedVRT
    from rasterio.warp import transform_bounds
    from rasterio.io import MemoryFile
    location = str(path)
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as z:
            members = [m for m in archive_members(z) if m.filename.lower().endswith(('.tif', '.tiff'))]
            if len(members) != 1:
                raise ValueError("ATLAS_ARCHIVE_SELECT_SINGLE_RASTER")
            m = members[0]
            if m.file_size > 32 * 1024**3 or m.file_size / max(1, m.compress_size) > 1000:
                raise ValueError("ATLAS_ARCHIVE_RASTER_LIMIT")
            location = '/vsizip/' + str(path) + '/' + m.filename
    # No auxiliary-file search, network projection grids, plugins, or remote raster drivers.
    with rasterio.Env(GDAL_CACHEMAX=64 * 1024**2, GDAL_DISABLE_READDIR_ON_OPEN='EMPTY_DIR', PROJ_NETWORK='OFF'):
        with rasterio.open(location, driver='GTiff') as src:
            if not src.crs or not 1 <= band <= src.count or not 0 < src.width * src.height <= 500_000_000_000:
                raise ValueError("ATLAS_RASTER_CRS_OR_BAND_INVALID")
            wgs = transform_bounds(src.crs, 'EPSG:4326', *src.bounds, densify_pts=21)
            # Kansas-first preview: intersect the source with the Kansas envelope, not a
            # stretched thumbnail. Global grids do not force the browser to read the globe.
            west, south, east, north = max(wgs[0], -102.1), max(wgs[1], 36.9), min(wgs[2], -94.5), min(wgs[3], 40.1)
            if not west < east or not south < north:
                raise ValueError("ATLAS_RASTER_OUTSIDE_KANSAS")
            merc = transform_bounds('EPSG:4326', 'EPSG:3857', west, south, east, north)
            dx, dy = merc[2] - merc[0], merc[3] - merc[1]
            width, height = (768, max(1, round(768 * dy / dx))) if dx >= dy else (max(1, round(768 * dx / dy)), 768)
            transform = from_bounds(*merc, width, height)
            with WarpedVRT(src, crs='EPSG:3857', transform=transform, width=width, height=height,
                           resampling=Resampling.nearest, add_alpha=True, warp_mem_limit=64) as vrt:
                values = vrt.read(band).astype('float64')
                valid = (vrt.read(vrt.count) > 0) & np.isfinite(values)
            nodata = src.nodata if src.nodata is not None and math.isfinite(src.nodata) else None
            if nodata is not None:
                valid &= values != nodata
            color_map = None
            try:
                color_map = src.colormap(band)
            except ValueError:
                pass
            if not color_map:
                values = values * src.scales[band-1] + src.offsets[band-1]
            valid &= np.isfinite(values)
            rgba = np.zeros((4, height, width), dtype='uint8')
            low = float(values[valid].min()) if valid.any() else None
            high = float(values[valid].max()) if valid.any() else None
            legend = []
            if color_map:
                # Palette entries are classes, never interpolate a numeric color ramp.
                classes = np.unique(values[valid]).tolist()
                if len(classes) > 256:
                    raise ValueError('ATLAS_RASTER_CLASS_LIMIT')
                for k in classes:
                    color = color_map.get(int(k), (128, 128, 128, 255))
                    mask = valid & (values == k)
                    for ch in range(4):
                        rgba[ch, mask] = color[ch]
                    legend.append({'value': k, 'color': '#%02x%02x%02x' % tuple(color[:3])})
            elif low is not None:
                t = np.zeros_like(values) if low == high else np.clip((np.where(valid, values, low)-low)/(high-low), 0, 1)
                # Cyan-light to deep blue; endpoints supplied to the UI's legend.
                for ch, (a,b) in enumerate(zip((220, 246, 239), (17, 85, 130))):
                    rgba[ch] = (a + t * (b-a)).astype('uint8')
                rgba[3, valid] = 220
            with MemoryFile() as memory:
                with memory.open(driver='PNG', width=width, height=height, count=4, dtype='uint8') as png:
                    png.write(rgba)
                encoded = base64.b64encode(memory.read()).decode('ascii')
            if len(encoded) > 2 * 1024**2:
                raise ValueError("ATLAS_RASTER_IMAGE_LIMIT")
            return {'data': {'imageDataUrl': 'data:image/png;base64,' + encoded,
                    'coordinates': [[west,north],[east,north],[east,south],[west,south]],
                    'width': width, 'height': height, 'sourceWidth': src.width, 'sourceHeight': src.height, 'min': low, 'max': high, 'band': band, 'nodata': nodata,
                    'paletteType': 'categorical' if color_map else 'continuous', 'colorMap': legend,
                    'colors': ['#dcf6ef', '#115582'], 'units': src.units[band-1]},
                    'bounds': [west,south,east,north], 'displayedCount': int(valid.sum()),
                    'totalCount': None, 'truncated': width != src.width or height != src.height or tuple(wgs) != (west,south,east,north),
                    'numericFields': [], 'valueField': None}


def vector(path):
    import shapefile
    from rasterio.warp import transform_geom
    from rasterio.crs import CRS
    handles = []
    if zipfile.is_zipfile(path):
        z = zipfile.ZipFile(path)
        handles.append(z)
        members = archive_members(z)
        shapes = [m for m in members if m.filename.lower().endswith('.shp')]
        if len(shapes) != 1:
            raise ValueError("ATLAS_ARCHIVE_SELECT_SINGLE_VECTOR")
        stem = shapes[0].filename[:-4]
        selected = {}
        for ext in ['shp','dbf','shx','prj']:
            matches = [m for m in members if m.filename.lower() == (stem+'.'+ext).lower()]
            if not matches or matches[0].file_size > MAX_MEMBER:
                raise ValueError("ATLAS_SHAPEFILE_MEMBER_MISSING_OR_LIMIT")
            selected[ext] = z.read(matches[0])
        prj = selected.pop('prj').decode('utf-8-sig')
        reader = shapefile.Reader(**{k: io.BytesIO(v) for k,v in selected.items()}, encodingErrors='replace')
    else:
        for ext in ['.shp','.shx','.dbf','.prj']:
            member = regular(path.with_suffix(ext))
            if member.stat().st_size > MAX_MEMBER:
                raise ValueError("ATLAS_SHAPEFILE_MEMBER_LIMIT")
        prj = path.with_suffix('.prj').read_text()
        reader = shapefile.Reader(str(path), encodingErrors='replace')
    crs = CRS.from_wkt(prj)
    features, count, vertices = [], len(reader), 0
    try:
        for i, row in enumerate(reader.iterShapeRecords()):
            if i >= FEATURES:
                break
            vertices += len(row.shape.points)
            if vertices > 180000:
                break
            g = transform_geom(crs, 'EPSG:4326', row.shape.__geo_interface__, precision=7)
            props = dict(row.record.as_dict())
            for key, v in list(props.items()):
                if not isinstance(v, (str,int,float,bool,type(None))):
                    props[key] = str(v)
                elif isinstance(v,float) and not math.isfinite(v):
                    props[key] = None
            features.append({'type':'Feature','geometry':g,'properties':props})
    finally:
        reader.close()
        for h in handles:
            h.close()
    return {'features':features,'total':count,'limitations':['Original shapefile CRS transformed offline to WGS84. Datum-grid downloads disabled; fine positional work needs source-appropriate accuracy review.']}


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (25, 26))
    resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (0, 0))
    try:
        request = json.loads(sys.stdin.read(4097))
        path = regular(request['path'])
        result = raster(path, request['band']) if request['kind'] == 'raster' else vector(path)
        encoded = json.dumps(result, allow_nan=False, separators=(',',':'))
        if len(encoded.encode()) > 12 * 1024**2:
            raise ValueError('ATLAS_RESPONSE_LIMIT')
        print(encoded)
    except Exception as error:
        message = str(error)
        print(json.dumps({'error': message if message.startswith('ATLAS_') and message.replace('_','').isalnum() else 'ATLAS_SPATIAL_READER_FAILED'}))

if __name__ == '__main__':
    main()
