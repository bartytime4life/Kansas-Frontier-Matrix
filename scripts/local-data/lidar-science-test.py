"""Analytic synthetic science tests; these are not survey/field accuracy claims."""
import pathlib,sys,types,unittest
import numpy as np
from scipy.spatial import cKDTree
path=pathlib.Path(sys.argv.pop(1)).resolve()
model=types.ModuleType('qualified_lidar_science')
exec(compile(path.read_bytes(),str(path),'exec'),model.__dict__)
class Science(unittest.TestCase):
 def plane(self):
  x,y=np.meshgrid(np.arange(-2,2.01,.5),np.arange(-2,2.01,.5));return np.column_stack([x.ravel(),y.ravel(),300+.1*x.ravel()+.2*y.ravel()])
 def records(self,ground=True):
  out=[]
  if ground:
   for x,y,z in self.plane():out.append([550000+x,4320000+y,z,100,2,1,1,0,100,0,len(out)])
  return out
 def point(self,x,y,height,kind=5,flags=0):return[550000+x,4320000+y,300+.1*x+.2*y+height,100,kind,1,1,flags,100,0,1000+kind+flags]
 def grid(self,rows):return model.analysis_grid(np.asarray(rows,dtype=float),[549998,4319998,550002,4320002],'EPSG:32614',1,1)
 def test_known_sloping_plane_and_residual(self):
  a=self.plane();fit=model.fit_ground(a,cKDTree(a[:,:2]),np.array([0.,0.]),3)
  self.assertIsNotNone(fit);np.testing.assert_allclose(fit[0],[.1,.2,300],atol=1e-10,rtol=0);self.assertLess(fit[1],1e-10)
 def test_no_extrapolation_or_collinear_plane(self):
  a=self.plane();self.assertIsNone(model.fit_ground(a,cKDTree(a[:,:2]),np.array([10.,10.]),30))
  line=np.array([[x,0,300+x]for x in range(-3,4)]);self.assertIsNone(model.fit_ground(line,cKDTree(line[:,:2]),np.array([0.,0.]),5))
 def test_buildings_unclassified_noise_and_flags_do_not_become_canopy(self):
  rows=self.records()+[self.point(0,0,12),self.point(.25,.25,50,6),self.point(.25,.25,80,1),self.point(0,0,1000,7),self.point(0,0,1100,18),self.point(0,0,500,5,4),self.point(0,0,600,5,1)]
  g=self.grid(rows);self.assertAlmostEqual(g['canopy'][0],12,places=9);self.assertAlmostEqual(g['surface'][0],380.075,places=9);self.assertAlmostEqual(g['ground'][0],300,places=9);self.assertEqual(g['vegetationCounts'][0],1)
 def test_missing_ground_and_missing_vegetation_stay_null(self):
  g=self.grid([self.point(0,0,10)]);self.assertIsNone(g['ground'][0]);self.assertIsNone(g['canopy'][0]);self.assertEqual(g['surface'][0],310)
  g=self.grid(self.records()+[self.point(0,0,80,1)]);self.assertIsNone(g['canopy'][0]);self.assertEqual(g['vegetationCounts'][0],0)
 def test_negative_normalized_height_is_preserved_for_review(self):
  g=self.grid(self.records()+[self.point(0,0,-2)]);self.assertAlmostEqual(g['canopy'][0],-2,places=9)
 def test_projected_grid_uses_ground_metres_and_transformed_corners(self):
  g=self.grid(self.records());self.assertEqual(g['cellSizeM'],[4,4]);self.assertEqual(len(g['cornersWgs84']),4)
  self.assertTrue(all(-102<lon<-94 and 36<lat<41 for lon,lat in g['cornersWgs84']))
  self.assertGreater(g['cornersWgs84'][0][1],g['cornersWgs84'][2][1])
if __name__=='__main__':unittest.main(verbosity=2)
