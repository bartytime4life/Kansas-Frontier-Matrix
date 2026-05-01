export function validateEbirdFixity(doc:any){
  if(doc?.object_type==='KfmEbirdFixityScanReport' && doc?.status==='pass' && (doc?.summary?.hash_mismatches||0)>0) throw new Error('pass with hash mismatch denied')
  return true
}
