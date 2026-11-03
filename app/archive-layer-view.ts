import { archiveLayer } from './archive-layer-catalog';

export type ArchiveView = { month: string; variable: string; from: string; to: string; area: string };
export type ArchiveViews = Record<string, ArchiveView>;
export function defaultArchiveView(now = new Date()): ArchiveView {
  const previous = new Date(now); previous.setUTCDate(1); previous.setUTCMonth(previous.getUTCMonth()-1);
  return { month: previous.toISOString().slice(0,7), variable:'ppt', from:`${now.getUTCFullYear()}-01-01`, to:now.toISOString().slice(0,10), area:'' };
}
const day = (value: unknown): value is string => typeof value==='string' && /^\d{4}-\d{2}-\d{2}$/.test(value) && Number.isFinite(Date.parse(value)) && new Date(value).toISOString().slice(0,10)===value;
export function parseArchiveViews(raw: string | null): ArchiveViews {
  const views: ArchiveViews = {};
  if(!raw || raw.length>16000)return views;
  try {
    const input=JSON.parse(raw);
    if(!input||typeof input!=='object'||Array.isArray(input))return views;
    for(const [id,v] of Object.entries(input)) {
      if(!archiveLayer(id)||!Array.isArray(v)||v.length!==5)continue;
      const [month,variable,from,to,area]=v;
      if(typeof month!=='string'||!/^\d{4}-(0[1-9]|1[0-2])$/.test(month)||!['ppt','tmax','tmin','tmean','tdmean','vpdmin','vpdmax','soltotal','solslope'].includes(variable)||!day(from)||!day(to)||from>to||typeof area!=='string')continue;
      if(area) {
        const a=area.split(',').map(Number);
        if(a.length!==4||!a.every(Number.isFinite)||a[0]<-103.5||a[2]>-93.5||a[1]<35.5||a[3]>41.5||Math.abs(a[2]-a[0]-1)>.0001||Math.abs(a[3]-a[1]-1)>.0001)continue;
      }
      views[id]={month,variable,from,to,area};
    }
  } catch { /* An invalid shared URL never grants a query. */ }
  return views;
}
/** Share the applied query, not unsubmitted form edits. Reopening reloads the first page. */
export function serializeArchiveViews(selected: readonly string[], views: ArchiveViews, redactLocation: boolean): string {
  return JSON.stringify(Object.fromEntries(selected.flatMap(id=>{
    const v=views[id];
    return archiveLayer(id)&&v?[[id,[v.month,v.variable,v.from,v.to,redactLocation?'':v.area]]]:[];
  })));
}
