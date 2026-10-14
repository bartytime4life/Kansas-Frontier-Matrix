"use client";
import "maplibre-gl/dist/maplibre-gl.css";
import {useEffect,useRef} from "react";
import type {View,Receipt} from "./connections-types";
import type {Map as MapLibreMap} from "maplibre-gl";
export default function ConnectionMap({view,receipt}:{view:View;receipt:Receipt}){
 const container=useRef<HTMLDivElement>(null),map=useRef<MapLibreMap|null>(null);
 useEffect(()=>{let disposed=false;const current=container.current;if(!current)return;
  void import("maplibre-gl").then(ml=>{
   if(disposed)return;
   const instance=new ml.Map({container:current,style:{version:8,sources:{},layers:[{id:"background",type:"background",paint:{"background-color":"#142338"}}]},center:[-97.34,38.5],zoom:5,attributionControl:{compact:true},maxZoom:16});
   map.current=instance;instance.addControl(new ml.NavigationControl(),"top-right");
   instance.on("load",()=>{
    if(disposed)return;
    if(view.features?.length){
     instance.addSource("records",{type:"geojson",data:{type:"FeatureCollection",features:view.features} as never});
     instance.addLayer({id:"polygons",type:"fill",source:"records",filter:["==",["geometry-type"],"Polygon"],paint:{"fill-color":"#44d5b4","fill-opacity":0.25}});
     instance.addLayer({id:"lines",type:"line",source:"records",paint:{"line-color":"#71e3ca","line-width":2}});
     instance.addLayer({id:"points",type:"circle",source:"records",filter:["==",["geometry-type"],"Point"],paint:{"circle-radius":5,"circle-color":"#71e3ca","circle-stroke-color":"#0a1726","circle-stroke-width":1}});
     instance.on("click",["points","lines","polygons"],e=>{const p=e.features?.[0]?.properties;if(p)new ml.Popup().setLngLat(e.lngLat).setText(JSON.stringify(p).slice(0,1500)).addTo(instance);});
     const bounds=new ml.LngLatBounds();
     const add=(c:unknown):void=>{if(!Array.isArray(c))return;if(typeof c[0]==="number"&&typeof c[1]==="number")bounds.extend([c[0],c[1]]);else c.forEach(add);};
     view.features.forEach(f=>add(f.geometry?.coordinates));if(!bounds.isEmpty())instance.fitBounds(bounds,{padding:45,maxZoom:13,duration:0});
    }
    if(view.raster){const [w,s,e,n]=view.raster.bbox;instance.addSource("raster",{type:"image",url:"/api/connections?action=entity&id="+receipt.captureId,coordinates:[[w,n],[e,n],[e,s],[w,s]]});instance.addLayer({id:"raster",source:"raster",type:"raster",paint:{"raster-opacity":1}});instance.fitBounds([[w,s],[e,n]],{padding:20,duration:0});}
   });
  }).catch(()=>{if(current)current.textContent="Map renderer unavailable. Source records remain in the table.";});
  return()=>{disposed=true;map.current?.remove();map.current=null;};
 },[view,receipt]);
 return <figure className="connection-map"><div ref={container} aria-label="Captured source geometry review map" role="region"/><figcaption>Source geometry in geographic context. Dark background carries no additional measurements. {view.raster?view.raster.vintage+" · actual per-pixel acquisition date unknown.":"No interpolation or inferred terrain."}</figcaption></figure>;
}
