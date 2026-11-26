/** A one-season-ahead trailing mean. Only consecutive, observed harvests can form a forecast. */
export function yieldHistory(text:string, lastHarvest:number) {
  if (text.length > 3000) return null;
  const lines=text.trim().split(/\r?\n/);
  if (lines.length<5 || lines.length>60) return null;
  const years=new Map<number,number>();
  for (const line of lines) {
    const match=/^\s*(\d{4})\s*[,\t]\s*(\d+(?:\.\d+)?)\s*$/.exec(line);
    if (!match) return null;
    const year=Number(match[1]), amount=Number(match[2]);
    if (year<1900 || year>lastHarvest || amount>1000 || years.has(year)) return null;
    years.set(year,amount);
  }
  const input=[...years.keys()].sort((a,b)=>a-b);
  const nextYear=input[input.length-1]+1;
  const estimate=(target:number)=>{
    let sum=0;
    for (let i=1;i<=5;i++) {
      const observed=years.get(target-i);
      if (observed===undefined) return null;
      sum+=observed;
    }
    return sum/5;
  };
  const value=estimate(nextYear);
  if (value===null) return null;
  let error=0, persistenceError=0, trials=0;
  for (const target of input) {
    const predicted=estimate(target);
    if (predicted===null) continue;
    const actual=years.get(target)!;
    error+=Math.abs(predicted-actual);
    persistenceError+=Math.abs(years.get(target-1)!-actual);
    trials++;
  }
  return {observations:years,nextYear,value,trials,mae:trials?error/trials:null,previousMae:trials?persistenceError/trials:null};
}


export function pairedSeasons(yields:ReadonlyMap<number,number>, rain:readonly {year:number; inches:number|null}[]) {
  const rows=rain.flatMap(r=>r.inches!==null && yields.has(r.year)?[{year:r.year,rain:r.inches,yield:yields.get(r.year)!}]:[]);
  if (rows.length<5) return {rows,correlation:null};
  const mean=(key:"rain"|"yield")=>rows.reduce((sum,r)=>sum+r[key],0)/rows.length;
  const x=mean("rain"), y=mean("yield");
  let xx=0, yy=0, xy=0;
  for (const r of rows) { xx+=(r.rain-x)**2; yy+=(r.yield-y)**2; xy+=(r.rain-x)*(r.yield-y); }
  return {rows,correlation:xx>0 && yy>0?Math.max(-1,Math.min(1,xy/Math.sqrt(xx*yy))):null};
}
