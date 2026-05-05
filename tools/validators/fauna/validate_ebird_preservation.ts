export function validateEbirdPreservation(doc:any){
  const txt=JSON.stringify(doc||{}).toLowerCase();
  if(txt.includes('delete_archive')||txt.includes('external archive api')) throw new Error('unsafe preservation recommendation')
  return true
}
