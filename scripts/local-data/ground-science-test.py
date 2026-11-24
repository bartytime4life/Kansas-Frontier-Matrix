#!/usr/bin/env python3
"""Synthetic analytic raster checks; never substitutes for provider/field evidence."""
import importlib.util,unittest,sys
from pathlib import Path
import numpy as np
from rasterio.io import MemoryFile
from rasterio.transform import from_bounds
path=Path(sys.argv.pop(1)) if len(sys.argv)>1 and sys.argv[1].endswith('.py') else Path(__file__).with_name('ground-decode.py')
spec=importlib.util.spec_from_file_location('ground_decode',path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
B=[-10836952.428725181,4534318.652568046,-10835839.23381725,4535725.296459141]
def raster(a,crs='EPSG:3857',nodata=None,transform=None):
    with MemoryFile() as mem:
        with mem.open(driver='GTiff',width=a.shape[1],height=a.shape[0],count=1,dtype=a.dtype,crs=crs,transform=transform or from_bounds(*B,a.shape[1],a.shape[0]),nodata=nodata) as ds: ds.write(a,1)
        return mem.read()
class GroundScience(unittest.TestCase):
    def test_exact_float32_values_and_north_to_south_row_order(self):
        a=(np.arange(9216,dtype=np.float32).reshape(96,96)/np.float32(37))+np.float32(300)
        v=module.decode(raster(a),B)
        self.assertEqual(v['ground'],[float(n) for n in a.ravel()]);self.assertEqual(v['ground'][96],float(a[1,0]));self.assertEqual(v['bounds3857'],B)
    def test_mask_is_gap_not_zero(self):
        a=np.full((96,96),np.float32(300));a[1,2]=-9999
        v=module.decode(raster(a,nodata=-9999),B);self.assertIsNone(v['ground'][98]);self.assertEqual(v['ground'][97],300);self.assertEqual(v['excludedValues'],0)
    def test_nonfinite_out_of_range_and_legal_negative_values(self):
        a=np.full((96,96),np.float32(300));a[0,:4]=[np.nan,np.inf,9001,-5]
        v=module.decode(raster(a),B);self.assertEqual(v['ground'][:4],[None,None,None,-5.0]);self.assertEqual(v['excludedValues'],3)
    def test_geographic_bbox_is_not_accepted_as_mercator_geometry(self):
        with self.assertRaisesRegex(ValueError,'RASTER_GEOMETRY'):module.decode(raster(np.zeros((96,96),dtype=np.float32)),[-97.35,37.68,-97.34,37.69])
    def test_wrong_crs_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'RASTER_SCHEMA'):module.decode(raster(np.zeros((96,96),dtype=np.float32),crs='EPSG:4326'),B)
    def test_stretched_byte_image_is_not_elevation(self):
        with self.assertRaisesRegex(ValueError,'RASTER_SCHEMA'):module.decode(raster(np.zeros((96,96),dtype=np.uint8)),B)
    def test_wrong_size_or_rotated_pixel_geometry_is_rejected(self):
        from affine import Affine
        with self.assertRaisesRegex(ValueError,'RASTER_SCHEMA'):module.decode(raster(np.zeros((64,64),dtype=np.float32)),B)
        t=from_bounds(*B,96,96)*Affine.rotation(.01)
        with self.assertRaisesRegex(ValueError,'RASTER_GEOMETRY'):module.decode(raster(np.zeros((96,96),dtype=np.float32),transform=t),B)
if __name__=='__main__':unittest.main()
