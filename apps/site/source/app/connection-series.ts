export const TIME_COLUMNS=["DATE","date","mapDate","Activity_StartDate","valid","period","DateObserved","date_local"];
export const VALUE_COLUMNS:Record<string,string[]>={
 "noaa-ncei":["TMAX","TMIN","TAVG","PRCP","SNOW","DLY-TMAX-NORMAL","DLY-TMIN-NORMAL","MLY-TMAX-NORMAL","MLY-TMIN-NORMAL","MLY-PRCP-NORMAL","ANN-TMAX-NORMAL","ANN-TMIN-NORMAL","ANN-PRCP-NORMAL"],
 "usdm-statistics":["none","d0","d1","d2","d3","d4"],"usgs-transect":["elevationM"],"nrcs-scan":["value"],"water-quality-portal":["Result_Measure"],"air-quality":["AQI","arithmetic_mean"],"iem-asos":["tmpf","sknt","drct"],"eia-electricity":["generation"],"usda-sda":["awc_r","om_r","ph1to1h2o_r","ksat_r"],"nass-quick-stats":["Value"],"census-acs":["B01003_001E","B01003_001M","B19013_001E","B19013_001M"]
};
export function nativeUnit(source:string,column:string,row:Record<string,unknown>){
 if(source==="usdm-statistics")return "% area";
 if(source==="usgs-transect")return "m · "+String(row.datum??"datum unknown");
 if(source==="nrcs-scan")return String(row.storedUnitCode??"unknown unit")+" at "+row.heightDepth+" in depth";
 if(source==="water-quality-portal")return String(row.Result_MeasureUnit??"unknown unit");
 if(source==="air-quality")return column==="AQI"?"AQI category index":String(row.units_of_measure??"unknown unit");
 if(source==="iem-asos")return ({tmpf:"°F",sknt:"knots",drct:"degrees"} as Record<string,string>)[column]??"unknown unit";
 if(source==="eia-electricity")return String(row["generation-units"]??"unknown unit")+" · "+String(row.fuelTypeDescription??row.fueltypeid??"");
 if(source==="nass-quick-stats")return String(row.unit_desc??"unknown unit")+" · "+String(row.short_desc??"");
 if(source==="usda-sda")return ({awc_r:"cm/cm",om_r:"%",ph1to1h2o_r:"pH (water, 1:1)",ksat_r:"µm/s"} as Record<string,string>)[column]??"unknown unit";
 if(source==="noaa-ncei")return /T(?:MAX|MIN|AVG)/.test(column)?"°F":/PRCP|SNOW/.test(column)?"inches":"unknown unit";
 if(source==="census-acs")return column.startsWith("B01003")?"people":"USD";
 return "unknown unit";
}
/** Display native values only: no interpolation, zero filling, or aggregation. */
export function series(source:string,rows:Record<string,unknown>[],column:string){
 const groups=new Map<string,{label:string;points:{label:string;value:number;native:string}[]}>();
 for(const row of rows){
  const raw=row[column];if(raw===null||raw===undefined||raw===""||typeof raw!=="string"&&typeof raw!=="number")continue;
  const token=String(raw).replaceAll(",","");
  if(!/^-?\d+(?:\.\d+)?$/.test(token)||!Number.isFinite(Number(token))||Number(token)<=-100000000)continue;
  if(source==="water-quality-portal"&&(row.Result_ResultDetectionCondition||row.Result_MeasureQualifierCode))continue;
  if(source==="nrcs-scan"&&row.qcFlag!=="V")continue;
  const label=String(TIME_COLUMNS.map(key=>row[key]).find(x=>typeof x==="string"&&x)||row.NAME||row.county_name||row.compname||"record");
  const unit=nativeUnit(source,column,row),group=groups.get(unit)??{label:unit,points:[]};
  group.points.push({label,value:Number(token),native:String(raw)});groups.set(unit,group);
 }
 return [...groups.values()].map(group=>({...group,points:group.points.slice(0,1000)}));
}
