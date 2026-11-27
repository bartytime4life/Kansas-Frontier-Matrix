"use client";

import { useEffect, useState } from "react";
import { readBoundedJson } from "./bounded-json";
import { phasesAfter, PHASE_NAMES } from "./moon";
import { centralOffset } from "./sun-chart";
import { frostLine, type FrostDates } from "./frost-dates";
import { pairedSeasons, yieldHistory } from "./yield-history";
import { rainBaseline, validOutlook, type RainOutlook } from "./rain-normal";

const GRAIN_PATH = "/api/curated/usda-kansas-grain-bids";
const USDA_REPORT = "https://www.ams.usda.gov/mnreports/ams_2886.pdf";
const futuresReferences: Readonly<Partial<Record<string,string>>> = {
  Corn: "https://www.cmegroup.com/markets/agriculture/grains/corn",
  Soybeans: "https://www.cmegroup.com/markets/agriculture/oilseeds/soybean",
  "Hard red winter wheat": "https://www.cmegroup.com/markets/agriculture/grains/kc-wheat",
};
const crops = ["Corn", "Sorghum", "Soybeans", "Hard red winter wheat"];
type Bid = { crop:string; region:string; low:number; high:number; average:number };
type Grain = { releaseId:string; reportDate:string; retrievedAt:string; approvalExpiresAt:string; rows:Bid[] };
type Point = { lon:number; lat:number };
const usd = new Intl.NumberFormat("en-US",{style:"currency",currency:"USD"});

function validGrain(value: unknown): value is Grain {
  const v = value as Grain & {state?:string; sourceId?:string; format?:string; sourceUrl?:string; unit?:string; payloadSha256?:string};
  return v?.state === "available" && v.sourceId === "usda-kansas-grain-bids" && v.format === "kfm-kansas-grain-bids-v1" &&
    v.sourceUrl === USDA_REPORT && v.unit === "USD/bu" && /^[a-f0-9]{64}$/.test(v.releaseId) &&
    /^[a-f0-9]{64}$/.test(v.payloadSha256 ?? "") && /^\d{4}-\d\d-\d\d$/.test(v.reportDate) &&
    Number.isFinite(Date.parse(v.reportDate)) && new Date(v.reportDate).toISOString().slice(0,10) === v.reportDate &&
    Number.isFinite(Date.parse(v.retrievedAt)) && v.reportDate <= v.retrievedAt.slice(0,10) &&
    Date.parse(v.retrievedAt) <= Date.now()+60000 && Date.parse(v.approvalExpiresAt) > Date.now() &&
    Array.isArray(v.rows) && v.rows.length > 0 && v.rows.length <= 36 &&
    new Set(v.rows.map(r=>r?.crop+"/"+r?.region)).size === v.rows.length &&
    v.rows.every(r => r && crops.includes(r.crop) && /^(Northwest|North|Northeast|West|Central|East|Southwest|South|Southeast)$/.test(r.region) &&
      [r.low,r.high,r.average].every(n=>typeof n==="number" && Number.isFinite(n) && n>0 && n<1000) && r.low<=r.average && r.average<=r.high);
}

function useSource<T>(url:string | null, validate:(value:unknown)=>value is T, refresh:number, deadline:number) {
  const [result,setResult] = useState<{url:string;refresh:number;data:T|null}|null>(null);
  useEffect(()=>{
    if (!url) return;
    const request = new AbortController();
    let active = true;
    const timer = setTimeout(()=>request.abort(), deadline);
    (async()=>{
      try {
        const response = await fetch(url,{signal:request.signal,cache:"no-store"});
        if (!response.ok) throw new Error();
        const value = await readBoundedJson(response,64*1024,request.signal);
        if (!validate(value)) throw new Error();
        if (active) setResult({url,refresh,data:value});
      } catch { if (active) setResult({url,refresh,data:null}); }
      finally { clearTimeout(timer); }
    })();
    return ()=>{ active=false; clearTimeout(timer); request.abort(); };
    // The caller's validator is bound to the full request URL.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  },[url,refresh,deadline]);
  return url && result?.url === url && result.refresh === refresh ? result.data : undefined;
}

const decimal = (text:string) => /^\d+(?:\.\d+)?$/.test(text) && Number.isFinite(Number(text)) && Number(text)<=1000000 ? Number(text) : null;
export function farmBudget(yieldText:string, bidText:string, costs:readonly string[]) {
  const yieldBu=decimal(yieldText), bid=decimal(bidText), entries=costs.map(decimal);
  if (yieldBu===null || bid===null || entries.some(n=>n===null)) return null;
  const total=entries.reduce<number>((sum,n)=>sum+n!,0);
  return { total, breakEven:yieldBu>0?total/yieldBu:null, rows:[0.8,1,1.2].map(factor=>({
    yield:yieldBu*factor, margin:yieldBu*factor*bid-total,
  })) };
}

type DeliveredBid = {
  bid: string;
  hauling: string;
  drying: string;
  handling: string;
  storage: string;
  shrink: string;
};

const emptyDeliveredBid: DeliveredBid = { bid: "", hauling: "0", drying: "0", handling: "0", storage: "0", shrink: "0" };
const deliveredBidFields: ReadonlyArray<[keyof DeliveredBid, string]> = [
  ["bid", "Cash bid ($/paid bu)"],
  ["hauling", "Hauling ($/loaded bu)"],
  ["drying", "Drying ($/loaded bu)"],
  ["handling", "Handling ($/loaded bu)"],
  ["storage", "Storage ($/loaded bu)"],
  ["shrink", "Shrink (%)"],
];
const bidCurrency = new Intl.NumberFormat("en-US", {
  style: "currency", currency: "USD", minimumFractionDigits: 4, maximumFractionDigits: 4,
});

export function netDeliveredBid(offer: DeliveredBid) {
  const { bid, hauling, drying, handling, storage, shrink } = offer;
  const entries = [bid, hauling, drying, handling, storage, shrink];
  if (!entries.every(value => /^(?:\d{1,4}(?:\.\d{1,4})?|\.\d{1,4})$/.test(value))) return null;
  // Ten-thousandths keep the bid and adjustment exact until display rounding.
  const [price, freight, dry, handle, store, loss] = entries.map(value => Math.round(Number(value) * 10_000));
  const percentScale = 100 * 10_000;
  if (loss > percentScale || [price, freight, dry, handle, store].some(value => value > 1_000 * 10_000)) return null;
  const net = price * (percentScale - loss) - (freight + dry + handle + store) * percentScale;
  return (Math.sign(net) * Math.round(Math.abs(net) / percentScale) || 0) / 10_000;
}

function DeliveredBidComparison({ crop }: { crop: string }) {
  const [grade, setGrade] = useState("");
  const [delivery, setDelivery] = useState("");
  const [bidA, setBidA] = useState(emptyDeliveredBid);
  const [bidB, setBidB] = useState(emptyDeliveredBid);
  const netA = netDeliveredBid(bidA);
  const netB = netDeliveredBid(bidB);
  const ready = grade.trim() && delivery.trim() && netA !== null && netB !== null;
  return <details>
    <summary data-farm-delivered-bids>Compare two delivery offers</summary>
    <p>Use two {crop.toLowerCase()} offers with the same grade and delivery window. Your entries stay in this view.</p>
    <div className="field-inputs">
      <label>Shared grade<input value={grade} maxLength={80} onChange={event => setGrade(event.target.value)} /></label>
      <label>Shared delivery window<input value={delivery} maxLength={80} onChange={event => setDelivery(event.target.value)} /></label>
    </div>
    <p>Enter costs per bushel loaded before shrink. Use zero for costs or shrink already reflected in the bid.</p>
    {([["Offer A", bidA, setBidA], ["Offer B", bidB, setBidB]] as const).map(([label, offer, setOffer]) =>
      <fieldset key={label} className="field-delivery-offer">
        <legend>{label}</legend>
        <div className="field-inputs">{deliveredBidFields.map(([key, field]) => <label key={key}>{field}
          <input inputMode="decimal" maxLength={9} value={offer[key]} onChange={event => {
            const value = event.target.value;
            setOffer(previous => ({ ...previous, [key]: value }));
          }} />
        </label>)}</div>
      </fieldset>,
    )}
    <div role="status">{ready ? <>
      <table><caption>Net price per loaded bushel</caption><thead><tr><th scope="col">Offer</th><th scope="col">$/loaded bu</th></tr></thead>
        <tbody><tr><th scope="row">A</th><td>{bidCurrency.format(netA)}</td></tr><tr><th scope="row">B</th><td>{bidCurrency.format(netB)}</td></tr></tbody>
      </table>
      <p>{netA === netB ? "The offers return the same net price at this precision." :
        `Offer ${netA > netB ? "A" : "B"} returns ${bidCurrency.format(Math.abs(netA - netB))} more per loaded bushel.`}</p>
    </> : <p>Enter a shared grade and delivery window and both cash bids. Use values from 0 to 1,000 dollars or 0 to 100 percent, with up to four decimal places.</p>}</div>
  </details>;
}

function MarketBudget({harvests,setHarvests}:{harvests:string;setHarvests:(s:string)=>void}) {
  const [crop,setCrop]=useState(crops[0]), [region,setRegion]=useState(""), [manual,setManual]=useState("");
  const yieldEstimate=yieldHistory(harvests,new Date().getUTCFullYear());
  const [inputPrices,setInputPrices]=useState(["","","",""]);
  const [yieldText,setYield]=useState(""), [costs,setCosts]=useState(["0","0","0",""]);
  const [query,setQuery]=useState(0), [expiryTick,setExpiryTick]=useState(0);
  const grain=useSource(query ? GRAIN_PATH : null,validGrain,query,12000);
  useEffect(()=>{
    if (!grain) return;
    const left=Date.parse(grain.approvalExpiresAt)-Date.now();
    if (left<=0) return;
    const timer=setTimeout(()=>setExpiryTick(n=>n+1),Math.min(left+1,2147483647));
    return ()=>clearTimeout(timer);
  },[grain,expiryTick]);
  const report=grain && Date.parse(grain.approvalExpiresAt)>Date.now()?grain:null;
  const rows=report?.rows.filter(r=>r.crop===crop) ?? [];
  const selected=rows.find(r=>r.region===region);
  const budget=farmBudget(yieldText,region ? String(selected?.average ?? "") : manual,costs);
  return <details className="field-tool"><summary data-category-tool="farm-planning">Cash bids &amp; break-even</summary>
    <label>Crop<select value={crop} onChange={e=>{setCrop(e.target.value);setRegion("");setManual("");setHarvests("");setYield("");}}>{crops.map(c=><option key={c}>{c}</option>)}</select></label>
    <button type="button" className="category-map-dock-tool" onClick={()=>setQuery(n=>n+1)}>{query?"Refresh reviewed bids":"Load reviewed Kansas bids"}</button>
    <div role="status">{query>0 && (grain===undefined?"Checking the release…":report?
      <p>USDA AMS · {report.reportDate} · conventional country elevators, current truck delivery. {crop==="Hard red winter wheat"?"Ordinary protein.":""} {Date.now()-Date.parse(report.reportDate)>7*86400000?"Historical report.":""}</p>:
      <p>Reviewed bids unavailable. Use the USDA report or enter a local bid.</p>)}</div>
    <a href={USDA_REPORT} target="_blank" rel="noreferrer">Open USDA’s latest Kansas daily grain report ↗</a>
    {futuresReferences[crop] && <p><a href={futuresReferences[crop]} target="_blank" rel="noreferrer">View {crop.toLowerCase()} futures on CME ↗</a> · exchange quotes delayed at least 10 minutes. The budget uses a cash bid.</p>}
    {report && <><label>Price source<select value={region} onChange={e=>setRegion(e.target.value)}><option value="">My cash bid</option>{rows.map(r=><option key={r.region} value={r.region}>{r.region} · ${r.average.toFixed(4)}/bu</option>)}</select></label>
      {selected && <p>Reported range ${selected.low.toFixed(4)}–${selected.high.toFixed(4)}/bu. The scenario uses the reported average.</p>}
      <a href={GRAIN_PATH+"?release="+report.releaseId+"&download=1"}>Download the reviewed price data</a></>}
    {!region && <label>My cash bid ($/bu)<input type="number" min="0" step="any" value={manual} onChange={e=>setManual(e.target.value)}/></label>}
    {region && !selected && <button type="button" onClick={()=>setRegion("")}>Enter my own bid</button>}
    <details><summary>Estimate yield from past harvests</summary>
      <p>Use one crop, location and management practice. Paste one year and yield in bushels per harvested acre per line, separated by a comma or tab. Leave suppressed or missing years out. A measured zero counts.</p>
      <a href="https://www.nass.usda.gov/Quick_Stats/" target="_blank" rel="noreferrer">USDA NASS county yield records ↗</a>
      <label>Past {crop.toLowerCase()} harvests (year, bu/ac)<textarea rows={5} maxLength={3000} value={harvests} onChange={e=>setHarvests(e.target.value)} /></label>
      <div role="status">{yieldEstimate?<><strong>{yieldEstimate.nextYear} yield baseline · {yieldEstimate.value.toFixed(1)} bu/ac</strong>
        <p>Mean of the five preceding harvests. {yieldEstimate.trials ? `Across ${yieldEstimate.trials} earlier test seasons, mean absolute error was ${yieldEstimate.mae!.toFixed(1)} bu/ac. Using the previous harvest alone gave ${yieldEstimate.previousMae!.toFixed(1)} bu/ac.` : "More observations are needed to measure historical error."}</p>
        <button type="button" onClick={()=>setYield(String(Number(yieldEstimate.value.toFixed(2))))}>Copy baseline into expected yield</button></>:
        <p>Enter at least five consecutive final harvest years. Each year must be unique.</p>}</div>
    </details>
    <details><summary>Convert fuel and fertilizer to cost per acre</summary>
      <div className="field-inputs">{["Diesel ($/gal)","Diesel use (gal/ac)","Fertilizer ($/US short ton)","Product applied (lb/ac)"].map((label,i)=><label key={label}>{label}<input type="number" min="0" step="any" value={inputPrices[i]} onChange={e=>{const value=e.target.value;setInputPrices(old=>old.map((n,j)=>i===j?value:n));}}/></label>)}</div>
      {["fuel","fertilizer"].map((kind,i)=>{
        const price=decimal(inputPrices[i*2]), quantity=decimal(inputPrices[i*2+1]);
        const perAcre=price!==null && quantity!==null?price*quantity/(i===0?1:2000):null;
        return <button key={kind} type="button" disabled={perAcre===null || perAcre>1000000} onClick={()=>{if(perAcre!==null)setCosts(old=>old.map((n,j)=>j===i?perAcre.toFixed(2):n));}}>
          {perAcre===null?"Enter "+kind+" price and usage":"Use "+usd.format(perAcre)+"/ac for "+kind}</button>;
      })}
    </details>
    <div className="field-inputs"><label>Expected yield (bu/ac)<input type="number" min="0" step="any" value={yieldText} onChange={e=>setYield(e.target.value)}/></label>
    {["Fuel ($/ac)","Fertilizer ($/ac)","Insurance premium ($/ac)","Other costs ($/ac)"].map((label,i)=><label key={label}>{label}<input type="number" min="0" step="any" value={costs[i]} onChange={e=>{const value=e.target.value;setCosts(old=>old.map((n,j)=>j===i?value:n));}}/></label>)}</div>
    <p>Include seed, land, irrigation and other applicable costs. Enter zero for any excluded cost. Inputs stay in this view.</p>
    <div role="status">{budget?<><strong>Break-even {budget.breakEven===null?"unavailable at zero yield":usd.format(budget.breakEven)+"/bu"}</strong>
      <p>{usd.format(budget.total)}/ac entered costs</p>
      <table><caption>Return above entered costs at the selected bid</caption><thead><tr><th scope="col">Yield case</th><th scope="col">bu/ac</th><th scope="col">$/ac</th></tr></thead>
        <tbody>{budget.rows.map((r,i)=><tr key={i}><th scope="row">{["−20%","Expected","+20%"][i]}</th><td>{r.yield.toLocaleString("en-US",{maximumFractionDigits:2})}</td><td>{usd.format(r.margin)}</td></tr>)}</tbody></table></>:<p>Enter a bid, expected yield and costs to compare three yield scenarios.</p>}</div>
    <DeliveredBidComparison key={crop} crop={crop} />
    <details><summary>Costs, disasters &amp; transport sources</summary>
      <ul>{[
        ["Biweekly Illinois fertilizer benchmarks · USDA AMS","https://mymarketnews.ams.usda.gov/viewReport/3195"],
        ["Weekly Midwest on-highway diesel · EIA","https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?f=W&n=PET&s=EMD_EPD2D_PTE_R20_DPG"],
        ["Premium estimate by county and coverage · USDA RMA","https://ewebapp.rma.usda.gov/apps/costestimator/"],
        ["Kansas farm budgets · K-State","https://www.agmanager.info/farm-management-guides-0"],
        ["Kansas active alerts · National Weather Service","https://api.weather.gov/alerts/active?area=KS"],
        ["Grain transportation costs · USDA AMS","https://agtransport.usda.gov/d/8uye-ieij"],
        ["Kansas road conditions and detours · KDOT KanDrive","https://www.ksdot.gov/travel/travel-conditions/kandrive"],
      ].map(([label,href])=><li key={href}><a href={href} target="_blank" rel="noreferrer">{label} ↗</a></li>)}</ul>
    </details>
  </details>;
}

function StationOutlook({point,harvests}:{point:Point|null;harvests:string}) {
  const now=new Date();
  const nextSeason=now.getUTCFullYear()+(now.getUTCMonth()>=3?1:0);
  const [year,setYear]=useState(nextSeason), [query,setQuery]=useState(0);
  const lon=point?Number(point.lon.toFixed(5)):null, lat=point?Number(point.lat.toFixed(5)):null;
  const url=query && lon!==null && lat!==null?`/api/farming/rain-normal?lon=${lon}&lat=${lat}&year=${year}&outlook=1`:null;
  const result=useSource<RainOutlook>(url,(v):v is RainOutlook=>lon!==null && lat!==null && validOutlook(v,lon,lat,year),query,90000);
  const baseline=result && rainBaseline(result.history);
  const yields=yieldHistory(harvests,now.getUTCFullYear());
  const pairs=result && yields ? pairedSeasons(yields.observations,result.history) : null;
  return <details className="field-tool"><summary>Season rainfall outlook</summary>
    <p>Compare April–October precipitation at the nearest Kansas airport. Each estimate uses up to ten earlier seasons at that station.</p>
    <label>Target season<select value={year} onChange={e=>{setYear(Number(e.target.value));setQuery(0);}}>{Array.from({length:nextSeason-1999},(_,i)=>nextSeason-i).map(y=><option key={y}>{y}</option>)}</select></label>
    {!point?<p>Turn on USDA crops and select a field or use “Inspect crops &amp; season at map center”.</p>:<button type="button" className="category-map-dock-tool" onClick={()=>setQuery(n=>n+1)}>Compare station seasons</button>}
    <div role="status">{url && (result===undefined?"Reading station seasons…":result===null?"Station history unavailable. Choose another point or retry.":<>
      <p>{result.station.name} ({result.station.id}) · {result.station.km} km from the field</p>
      {baseline?<><strong>{year} planning baseline · {baseline.median.toFixed(2)} in</strong>
        <p>{baseline.count} complete seasons ranged from {baseline.min.toFixed(2)} to {baseline.max.toFixed(2)} in. The estimate is their median.</p>
        {baseline.mae!==null?<p>Earlier-year check · {baseline.hindcasts} held-out seasons, mean absolute error {baseline.mae.toFixed(2)} in.</p>:<p>Too few complete seasons for an earlier-year check.</p>}</>:<p>Fewer than five complete seasons. Estimate withheld.</p>}
      <details><summary>Annual totals and missing seasons</summary>
      <table><caption>Station precipitation · April 1–October 31</caption><thead><tr><th>Year</th><th colSpan={2}>Precipitation (in)</th></tr></thead><tbody>{result.history.map(r=><tr key={r.year}><th scope="row">{r.year}</th><td>{r.inches?.toFixed(2)??"Unavailable"}</td><td>{r.inches!==null && <meter aria-label={r.year+" precipitation in inches"} min={0} max={Math.max(1,...result.history.map(v=>v.inches??0))} value={r.inches}/>}</td></tr>)}</tbody></table></details>
      {pairs && <details><summary>Compare my harvests with station rain</summary>
        <p>{pairs.rows.length} matching years. Compare one field or county with a representative station. April–October covers only part of a winter-wheat crop cycle.</p>
        {pairs.rows.length>0 && <table><caption>Your yield and station rain by harvest year</caption><thead><tr><th>Year</th><th>bu/ac</th><th>in</th></tr></thead><tbody>{pairs.rows.map(r=><tr key={r.year}><th scope="row">{r.year}</th><td>{r.yield}</td><td>{r.rain.toFixed(2)}</td></tr>)}</tbody></table>}
        <p>{pairs.correlation===null?"Correlation requires five matching years and variation in both series.":`Pearson correlation ${pairs.correlation.toFixed(2)}. Irrigation, management, heat and trends can also affect this relationship.`}</p>
      </details>}
      <p>Historical station baseline. It does not estimate parcel yield or reflect a seasonal weather forecast. Retrieved {result.retrievedAt.slice(0,10)}.</p>
      <a href={"https://mesonet.agron.iastate.edu/sites/site.php?station="+encodeURIComponent(result.station.id)+"&network=KS_ASOS"} target="_blank" rel="noreferrer">Iowa Environmental Mesonet station ↗</a>
    </>)}</div>
  </details>;
}

type FieldFrost = Readonly<{ lon:number; lat:number; year:number; state:"ready"|"loading"|"failed"|"none"; data:FrostDates|null }>;
const chicagoDay = (ms:number) => new Date(ms + centralOffset(ms)*60_000).toISOString().slice(0,10);
const phaseDate = new Intl.DateTimeFormat("en-US",{timeZone:"America/Chicago",month:"short",day:"numeric"});

export function almanacPhases(month:string) {
  if (!/^\d{4}-(?:0[1-9]|1[0-2])$/.test(month) || month < "2005-01" || month > "2050-12") return [];
  const start = Date.parse(month+"-01T00:00:00Z");
  return phasesAfter(start,6).filter(phase=>chicagoDay(phase.at).startsWith(month));
}

function FieldAlmanac({point,year,frost}:{point:Point|null;year:number;frost:FieldFrost|null}) {
  const [month,setMonth]=useState("");
  const [opened,setOpened]=useState(false);
  const phases=opened ? almanacPhases(month) : [];
  const selected=point && frost && frost.year===year && frost.lon===Number(point.lon.toFixed(5)) && frost.lat===Number(point.lat.toFixed(5)) ? frost : null;
  let stationReading="Select a crop point to see the nearby station’s freeze dates.";
  if (point) {
    if (!selected || selected.state==="failed") stationReading="Station freeze observations are unavailable for this point and year.";
    else if (selected.state==="loading") stationReading="Reading the selected station…";
    else if (selected.state==="none") stationReading="No Kansas airport station within range.";
    else stationReading=(selected.data && frostLine(selected.data)) || "Station freeze observations unavailable.";
  }
  return <details className="field-tool" onToggle={event=>{
    const open=event.currentTarget.open;
    if (open && !opened && !month) setMonth(chicagoDay(Date.now()).slice(0,7));
    setOpened(open);
  }}>
    <summary data-category-tool="field-almanac">Farmers’ Almanac &amp; frost dates</summary>
    <p><strong>Observed freeze · {year}</strong></p><p role="status">{stationReading}</p>
    <p>Compare the station’s 32°F threshold with typical city frost dates. A field can freeze earlier or later.</p>
    <ul>
      <li><a href="https://www.farmersalmanac.com/average-frost-dates#:~:text=Kansas" target="_blank" rel="noreferrer">Farmers’ Almanac frost chart ↗</a> · choose Kansas for the five listed cities.</li>
      <li><a href="https://www.farmersalmanac.com/calendar/gardening" target="_blank" rel="noreferrer">Free planting calendar preview ↗</a> · the publisher’s traditional lunar calendar applies across growing zones.</li>
    </ul>
    <label>Moon phase month<input type="month" min="2005-01" max="2050-12" value={month} onChange={e=>setMonth(e.target.value)}/></label>
    {phases.length>0 ? <table><caption>KFM astronomical phases · Central time</caption><thead><tr><th scope="col">Phase</th><th scope="col">Date</th></tr></thead>
      <tbody>{phases.map(phase=><tr key={phase.at}><th scope="row">{PHASE_NAMES[phase.kind]}</th><td><time dateTime={chicagoDay(phase.at)}>{phaseDate.format(phase.at)}</time></td></tr>)}</tbody></table> :
      <p>Choose a month from 2005 through 2050.</p>}
  </details>;
}

export function FieldDecisionTools({point,year,frost}:{point:Point|null;year:number;frost:FieldFrost|null}) {
  const [harvests,setHarvests]=useState("");
  return <section className="field-decisions" aria-label="Farm planning">
    <MarketBudget harvests={harvests} setHarvests={setHarvests}/>
    <StationOutlook key={point?point.lon+","+point.lat:"no-point"} point={point} harvests={harvests}/>
    <FieldAlmanac point={point} year={year} frost={frost}/>
  </section>;
}
