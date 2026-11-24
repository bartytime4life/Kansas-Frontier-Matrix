"""Private, bounded native EPT readback and same-survey analysis.

The Node actor supplies locally captured, hash-checked files, never a visitor path.
No network or provider credentials are used by this process.
"""
import sys,json,math,os,pathlib,hashlib,datetime
import numpy as np
import laspy
from rasterio.warp import transform,transform_bounds
from scipy.spatial import cKDTree,ConvexHull,QhullError

REVIEW={'status':'pending','source_admitted':False,'released':False,'scientific_accuracy_verified':False}
COLUMNS=['x','y','z','intensity','classification','returnNumber','numberOfReturns','classFlags','gpsTime','asset','record']
def analysis_support_bounds(query):
 crs='EPSG:32614'if(query['bbox'][0]+query['bbox'][2])/2<-96 else'EPSG:32615'
 bounds=list(transform_bounds('EPSG:4326',crs,*query['bbox'],densify_pts=21))
 side=max(bounds[2]-bounds[0],bounds[3]-bounds[1])/64
 radius=min(75.,max(5.,4*side))
 # Expand the actual UTM analysis rectangle, not an angular approximation.
 # Densification includes curved projected edges; 1m guards numerical edges.
 support=[bounds[0]-radius-1,bounds[1]-radius-1,bounds[2]+radius+1,bounds[3]+radius+1]
 mercator=list(transform_bounds(crs,'EPSG:3857',*support,densify_pts=21))
 return {'analysisCrs':crs,'boundsUTM':bounds,'support3857':mercator,'groundRadiusM':radius}
def eligible(a):
 return ((a[:,7].astype(np.uint8)&5)==0)&~np.isin(a[:,4],[7,18])
def inside_polygon(points,polygon):
 points=np.asarray(points);x,y=points[:,0],points[:,1];result=np.zeros(len(points),dtype=bool)
 for i in range(len(polygon)):
  a,b=polygon[i],polygon[i-1]
  crosses=(a[1]>y)!=(b[1]>y)
  if a[1]!=b[1]:result^=crosses&(x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0])
 return result
def fit_ground(ground,tree,center,radius):
 """Distance-weighted local plane; no extrapolation outside source support."""
 if len(ground)<3:return None
 d,i=tree.query(center,k=min(32,len(ground)),distance_upper_bound=radius,eps=0,workers=1)
 keep=np.isfinite(d)&(i<len(ground));d,i=np.atleast_1d(d)[keep],np.atleast_1d(i)[keep]
 if len(i)<3:return None
 selected=ground[i];delta=selected[:,:2]-center;A=np.column_stack([delta,np.ones(len(i))]);w=1/np.maximum(d,.1)**2
 weighted=A*np.sqrt(w)[:,None]
 if np.linalg.matrix_rank(weighted)<3 or np.linalg.cond(weighted)>1e8:return None
 try:polygon=selected[ConvexHull(selected[:,:2]).vertices,:2]
 except QhullError:return None
 if not inside_polygon(np.asarray([center]),polygon)[0]:return None
 coefficients=np.linalg.lstsq(weighted,selected[:,2]*np.sqrt(w),rcond=None)[0]
 residual=math.sqrt(float(np.average((A@coefficients-selected[:,2])**2,weights=w)))
 return coefficients,residual,polygon
def analysis_grid(a,bounds,crs,width=64,height=64):
 """All coordinates in local projected metres, rows use native LAS attributes."""
 assert 1<=width<=64 and 1<=height<=64
 west,south,east,north=bounds;dx,dy=(east-west)/width,(north-south)/height
 n=width*height;ground=[None]*n;surface=[None]*n;canopy=[None]*n;residual=[None]*n
 counts=[np.zeros(n,dtype=np.int64)for _ in range(3)]
 good=eligible(a)&np.isfinite(a[:,:3]).all(axis=1)
 class_ground=a[good&(a[:,4]==2),:3];tree=cKDTree(class_ground[:,:2])if len(class_ground)else None
 col=np.floor((a[:,0]-west)/dx).astype(np.int64);row=np.floor((north-a[:,1])/dy).astype(np.int64)
 within=good&(col>=0)&(col<width)&(row>=0)&(row<height);cell=row*width+col
 for kind,mask in enumerate([within&(a[:,4]==2),within&(a[:,5]==1),within&np.isin(a[:,4],[3,4,5])]):
  np.add.at(counts[kind],cell[mask],1)
 first=np.flatnonzero(within&(a[:,5]==1));tops=np.full(n,-np.inf)
 if len(first):np.maximum.at(tops,cell[first],a[first,2])
 surface=[float(v)if np.isfinite(v)else None for v in tops]
 vegetation={}
 for idx in np.flatnonzero(within&np.isin(a[:,4],[3,4,5])):vegetation.setdefault(int(cell[idx]),[]).append(int(idx))
 radius=min(75.,max(5.,4*max(dx,dy)))
 for j in range(n):
  center=np.array([west+(j%width+.5)*dx,north-(j//width+.5)*dy])
  fit=fit_ground(class_ground,tree,center,radius)if tree is not None else None
  if fit is None:continue
  coeff,rmse,polygon=fit;ground[j]=float(coeff[2]);residual[j]=rmse
  indices=vegetation.get(j,[])
  if indices:
   points=a[indices];supported=inside_polygon(points[:,:2],polygon)
   if supported.any():
    points=points[supported];predicted=(points[:,:2]-center)@coeff[:2]+coeff[2]
    canopy[j]=float(np.max(points[:,2]-predicted))
 # Native counts, including unsupported vegetation, are retained independently.
 corners=[]
 xx,yy=np.meshgrid(np.linspace(west,east,width+1),np.linspace(north,south,height+1))
 lon,lat=transform(crs,'EPSG:4326',xx.ravel().tolist(),yy.ravel().tolist())
 corners=[[float(x),float(y)]for x,y in zip(lon,lat)]
 return {'width':width,'height':height,'analysisCrs':crs,'bounds':bounds,'cellSizeM':[dx,dy],'cornersWgs84':corners,'ground':ground,'surface':surface,'canopy':canopy,'groundCounts':counts[0].tolist(),'surfaceCounts':counts[1].tolist(),'vegetationCounts':counts[2].tolist(),'groundResidualM':residual}
def encode(v):return(json.dumps(v,separators=(',',':'),allow_nan=False)+'\n').encode()
def save(directory,name,value):
 b=encode(value);assert len(b)<=900000
 p=directory/name;fd=os.open(p,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
 with os.fdopen(fd,'wb')as f:f.write(b);f.flush();os.fsync(f.fileno())
 assert p.read_bytes()==b
 return {'bytes':len(b),'sha256':'sha256:'+hashlib.sha256(b).hexdigest()}
def run(job):
 out=pathlib.Path(job['output']);assert out.is_absolute()and out.is_dir()and not out.is_symlink()and(out.stat().st_mode&0o777)==0o700
 assert len(job['assets'])<=128 and len(job['requestKey'])==64
 arrays=[];assets=[];decoded=0;outside_display=0;crop=job['crop3857']
 for index,asset in enumerate(job['assets']):
  p=pathlib.Path(asset['path']);assert p.is_absolute()and not p.is_symlink()and p.is_file()and(p.stat().st_mode&0o777)==0o600 and p.stat().st_uid==os.getuid()and p.stat().st_nlink==1
  raw=p.read_bytes();assert len(raw)==asset['bytes']and'sha256:'+hashlib.sha256(raw).hexdigest()==asset['sha256']
  cloud=laspy.read(p);assert len(cloud.points)==asset['pointCount'];decoded+=len(cloud.points);assert decoded<=2000000
  dims=set(cloud.point_format.dimension_names);assert {'X','Y','Z','intensity','classification','return_number','number_of_returns'}<=dims
  x,y,z=np.asarray(cloud.x),np.asarray(cloud.y),np.asarray(cloud.z)
  legacy=np.asarray(cloud.synthetic,dtype=np.uint8)|(np.asarray(cloud.key_point,dtype=np.uint8)<<1)|(np.asarray(cloud.withheld,dtype=np.uint8)<<2)
  if 'overlap'in dims:legacy|=np.asarray(cloud.overlap,dtype=np.uint8)<<3
  if 'ClassFlags'in dims:
   flags=np.asarray(cloud['ClassFlags'],dtype=np.uint8);assert(flags<=15).all()and np.array_equal(flags&7,legacy&7)
  else:flags=legacy
  has_gps='gps_time'in dims;gps=np.asarray(cloud.gps_time)if has_gps else np.full(len(x),np.nan)
  gps_type=('adjusted-standard'if int(cloud.header.global_encoding.gps_time_type)==1 else'week')if has_gps else'absent'
  receipt={k:asset[k]for k in ['url','sha256','bytes','pointCount','project','eptUrl','acquisition','verticalReference']}
  receipt.update(id=index,coordinateEncodingM=[float(v)for v in cloud.header.scales],gpsTimeType=gps_type);assets.append(receipt)
  assert all(0<v<=1 for v in receipt['coordinateEncodingM'])
  finite=np.isfinite(x)&np.isfinite(y)&np.isfinite(z)
  within=finite&(x>=crop[0])&(x<=crop[2])&(y>=crop[1])&(y<=crop[3])
  plausible=(z>=-12000)&(z<=9000);outside_display+=int(np.count_nonzero(within&~plausible))
  ids=np.flatnonzero(within&plausible)
  if has_gps:assert np.isfinite(gps[ids]).all()
  if len(ids):arrays.append(np.column_stack([x[ids],y[ids],z[ids],np.asarray(cloud.intensity)[ids],np.asarray(cloud.classification)[ids],np.asarray(cloud.return_number)[ids],np.asarray(cloud.number_of_returns)[ids],flags[ids],gps[ids],np.full(len(ids),index),ids]))
 a=np.concatenate(arrays)if arrays else np.empty((0,11));created=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='milliseconds').replace('+00:00','Z')
 grid=None
 if job.get('analysisComplete')and job.get('analysisProject'):
  chosen=[i for i,asset in enumerate(assets)if asset['project']==job['analysisProject']]
  analysis=a[np.isin(a[:,9],chosen)].copy();q=job['query'];support=analysis_support_bounds(q);crs=support['analysisCrs']
  if len(analysis):
   X,Y=transform('EPSG:3857',crs,analysis[:,0].tolist(),analysis[:,1].tolist());analysis[:,0],analysis[:,1]=X,Y
   bounds=support['boundsUTM']
   assert(bounds[2]-bounds[0])*(bounds[3]-bounds[1])<=1050000
   grid=analysis_grid(analysis,bounds,crs)
   grid_assets=[{**assets[i],'id':j}for j,i in enumerate(chosen)]
   grid.update(format='kfm-lidar-grid-v1',requestKey=job['requestKey'],generatedAt=created,source={'project':job['analysisProject'],'eptUrl':grid_assets[0]['eptUrl'],'acquisition':grid_assets[0]['acquisition'],'verticalReference':grid_assets[0]['verticalReference'],'assets':grid_assets},review=REVIEW,method={'completeNativeSupport':True,'ground':'Distance-weighted least-squares plane from up to32 nearby valid class2 returns; source convex-hull support required.','surface':'Maximum valid first-return native elevation per cell; buildings and wires may be present.','canopy':'Maximum classified-vegetation(3/4/5) return height above the same-survey supported local ground plane; not all unclassified objects.','support':'Ground neighbor radius min(75m,max(5m,4*largest cell side)); rank3 and condition<=1e8; no plane extrapolation beyond ground-neighbor convex hull.','limitations':['Complete selected-survey hierarchy support is distinct from field accuracy and actual pulse coverage. NoData stays null.','Vegetation classes are required. Class1 is unclassified and does not prove vegetation; absent canopy is not zero canopy.','Synthetic/withheld flags and classes7/18 noise are excluded from analysis.','Ground residual is weighted model-fit RMSE, not independent measurement uncertainty.','Source acquisition/vertical accuracy and registration to displayed terrain remain unverified. Negative normalized heights are preserved for review.']})
   save(out,'grid.json',grid)
 # Point display crop is the exact requested view, independent of buffered analysis.
 exact=job['viewBounds3857'];a=a[(a[:,0]>=exact[0])&(a[:,0]<=exact[2])&(a[:,1]>=exact[1])&(a[:,1]<=exact[3])]
 original=len(a);a=a[np.linspace(0,len(a)-1,100000,dtype=np.int64)]if len(a)>100000 else a
 m=None
 if len(a):
  rows=[]
  for r in a:
   row=[float(r[0]),float(r[1]),float(r[2]),int(r[3]),int(r[4]),int(r[5]),int(r[6]),int(r[7]),None if assets[int(r[9])]['gpsTimeType']=='absent'else float(r[8]),int(r[9]),int(r[10])];rows.append(row)
  assert len({(r[9],r[10])for r in rows})==len(rows)
  parts=[]
  for start in range(0,len(rows),6500):
   i=len(parts);value={'format':'kfm-lidar-points-chunk-v2','captureId':'view-'+job['requestKey'],'chunkId':i,'points':rows[start:start+6500]};assert i<16
   receipt=save(out,f'chunk-{i}.json',value);parts.append({'id':i,'pointCount':len(value['points']),**receipt})
  m={'format':'kfm-lidar-points-manifest-v2','captureId':'view-'+job['requestKey'],'generatedAt':created,'source':{'provider':'USGS','project':'Kansas viewport','eptUrl':'https://usgs.entwine.io/','horizontalCrs':'EPSG:3857','verticalReference':'Per-asset native references retained; mixed-project vertical registration and independent accuracy are unverified.','acquisition':'Per-project identifier labels are retained per asset; verified calendar flight intervals are not inferred.','coordinateEncodingM':[min(s['coordinateEncodingM'][i]for s in assets)for i in range(3)],'selection':f"Viewport-cropped native additive EPT nodes; {original} captured rows before deterministic source-order display thinning to {len(rows)}. Display LOD may omit hierarchy levels and does not establish full native density.",'assets':assets,'notes':[f'{outside_display} finite native records outside the display elevation budget[-12000,9000]m were omitted from this derived package; original LAZ bytes are retained.','Native source XYZ/attributes and original EPT node record indices are preserved, without coordinate rounding.','Synthetic, withheld and noise records remain inspectable but are filtered from default measured-return rendering.','Asset SHA256 values are local captured-byte hashes, not provider-published expected digests.','Per-asset GPS encoding is retained; no missing GPS or calendar flight date is invented.','Sparse displayLOD is never used to generate surface or canopy analysis.']},'review':REVIEW,'pointCount':len(rows),'bounds3857':[float(a[:,0].min()),float(a[:,1].min()),float(a[:,0].max()),float(a[:,1].max())],'heightRange':[float(a[:,2].min()),float(a[:,2].max())],'chunks':parts,'columns':COLUMNS}
  assert len(encode(m))<=256000;save(out,'manifest.json',m)
 summary={'createdAt':created,'manifest':m,'grid':None if grid is None else {'format':grid['format'],'width':grid['width'],'height':grid['height'],'sourceProject':grid['source']['project']},'gridValidCells':None if grid is None else {k:sum(v is not None for v in grid[k])for k in ['ground','surface','canopy']},'decodedNativeRecords':decoded,'viewportNativeRecords':original,'displayRecords':len(a),'rejectedDisplayElevations':outside_display}
 save(out,'decode-summary.json',summary)
 return {k:v for k,v in summary.items()if k!='manifest'}
if __name__=='__main__':
 if len(sys.argv)!=2:raise SystemExit('One private job file is required')
 job_path=pathlib.Path(sys.argv[1]);assert job_path.is_absolute()and job_path.stat().st_size<=256000
 job=json.loads(job_path.read_text())
 print(json.dumps(analysis_support_bounds(job['query'])if job.get('mode')=='bounds'else run(job)))
