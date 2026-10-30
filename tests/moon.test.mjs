import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import ts from 'typescript';
import {componentHarness, findNode} from './component-harness.mjs';

const compile=async(path,modules={})=>{const exports={};new Function('exports','require',ts.transpileModule(await readFile(path,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022}}).outputText)(exports,name=>{if(name in modules)return modules[name];throw new Error(`Unexpected import: ${name}`);});return exports;};
const orientation=await compile('app/kansas-orientation.ts');
const sun=await compile('app/sun-chart.ts',{'./kansas-orientation':orientation});
const moon=await compile('app/moon.ts',{'./sun-chart':sun});
const maps=await compile('app/category-maps.ts');
const page=await readFile('app/page.tsx','utf8');
const CENTRE={lat:38.498,lon:-98.698};

test('the principal phases match Meeus\'s worked examples to a second',()=>{
 // Astronomical Algorithms, example 49.a: the new moon of February 1977; example 49.b: the first quarter of January 2044.
 assert.ok(Math.abs(moon.phaseJde(-283)-2443192.65118)<1e-5);
 assert.ok(Math.abs(moon.phaseJde(544.75)-2467636.49186)<1e-5);
 assert.equal(Math.round(moon.deltaT(2026)),75);
});

test('the Moon\'s low-precision position agrees with Meeus\'s full theory, and each phase falls where the Sun and Moon say it should',()=>{
 // Example 47.a, 1992 April 12 0h TD: λ 133.162655°, β −3.229126°, distance 368,409.7 km (π 0.99199°).
 const p=moon.moonPosition((2448724.5-2440587.5)*86400000);
 assert.ok(Math.abs(p.longitude-133.162655)<0.3);assert.ok(Math.abs(p.latitude+3.229126)<0.2);assert.ok(Math.abs(p.parallax-0.99199)<0.003);
 // An independent check of the phase series: at each phase, the Moon–Sun elongation from the position series is 0°, 90°, 180° or 270°.
 const phases=moon.phasesAfter(Date.parse('2026-01-01T00:00:00Z'),100);
 assert.deepEqual(phases.slice(0,4).map(ph=>ph.kind).sort(),['first','full','last','new']);
 for(const ph of phases){
  const target={new:0,first:90,full:180,last:270}[ph.kind];
  const e=(moon.moonPosition(ph.at).longitude-moon.sunLongitude(ph.at)+360)%360;
  assert.ok(Math.abs(((e-target+540)%360)-180)<0.5,`${ph.kind} ${new Date(ph.at).toISOString()}: elongation ${e.toFixed(2)}°`);
 }
 assert.ok(phases.every((ph,i)=>i===0||ph.at>phases[i-1].at));
 const full=phases.find(ph=>ph.kind==='full'&&ph.at>Date.parse('2026-10-20T00:00:00Z'));
 assert.equal(new Date(full.at).toISOString().slice(0,16),'2026-10-26T04:11');
 assert.ok(moon.moonIllumination(full.at).fraction>0.99);
});

test('moonrise and moonset are where the Moon\'s centre stands at its horizon altitude, rising and falling',()=>{
 const midnight=moon.centralMidnight('2026-10-30');
 assert.equal(new Date(midnight).toISOString(),'2026-10-30T05:00:00.000Z');
 const {rise,set}=moon.moonEvents(midnight,moon.centralMidnight('2026-10-31'),CENTRE.lat,CENTRE.lon);
 for(const [t,dir] of [[rise,1],[set,-1]]){
  const a=moon.moonAltitude(t,CENTRE.lat,CENTRE.lon),later=moon.moonAltitude(t+60000,CENTRE.lat,CENTRE.lon);
  assert.ok(Math.abs(a.altitude-a.horizon)<1e-4);assert.ok(Math.sign(later.altitude-a.altitude)===dir);
 }
 assert.equal(moon.moonReading('2026-10-30',CENTRE.lat,CENTRE.lon),'Moon tonight: waning gibbous, 70% lit · sets 1:15 PM CDT, rises 10:34 PM CDT');
 assert.equal(moon.phaseList(Date.parse('2026-10-30T12:00:00Z')),'Last quarter Nov 1, 2:28 PM CST · New moon Nov 9, 1:02 AM CST · First quarter Nov 17, 5:48 AM CST · Full moon Nov 24, 8:53 AM CST');
 assert.equal(moon.phaseName(Date.parse('2026-10-26T04:11:00Z')),'Full moon');
});

test('a clock-change day starts and ends at its own local midnight, and lunar events stay within it',()=>{
 // Clocks spring forward on 2026-03-08 (2 AM CST to 3 AM CDT) and fall back on 2026-11-01 (2 AM CDT to 1 AM CST).
 assert.equal(new Date(moon.centralMidnight('2026-03-08')).toISOString(),'2026-03-08T06:00:00.000Z','CST still at midnight');
 assert.equal(new Date(moon.centralMidnight('2026-03-09')).toISOString(),'2026-03-09T05:00:00.000Z','CDT after the change');
 assert.equal(new Date(moon.centralMidnight('2026-11-01')).toISOString(),'2026-11-01T05:00:00.000Z','CDT at midnight before the fall-back');
 assert.equal(new Date(moon.localInstant('2026-03-08',21)).toISOString(),'2026-03-09T02:00:00.000Z','9 PM CDT on the spring-forward day');
 for(const day of ['2026-03-07','2026-03-08','2026-03-09','2026-10-31','2026-11-01','2026-11-02']){
  const from=moon.centralMidnight(day),until=moon.centralMidnight(moon.addDays(day,1));
  const {rise,set}=moon.moonEvents(from,until,CENTRE.lat,CENTRE.lon);
  for(const t of [rise,set].filter(x=>x!==null))assert.ok(t>=from&&t<until,`${day}: event ${new Date(t).toISOString()} is outside its own day`);
 }
 // Codex on #5600: the previous day's 11:15 PM CST moonrise was reported as 2026-03-08's.
 assert.doesNotMatch(moon.moonReading('2026-03-08',CENTRE.lat,CENTRE.lon),/11:15 PM/);
 assert.match(moon.moonReading('2026-03-07',CENTRE.lat,CENTRE.lon),/rises 11:15 PM CST/,'the rise belongs to March 7');
 const strip=moon.moonStrip('2026-03-07');
 assert.deepEqual([strip.discs[0].date,strip.discs[1].date,strip.discs[29].date],['2026-03-07','2026-03-08','2026-04-05'],'a date per evening, no doubled or skipped day across the change');
});

test('a disc is lit on the right while waxing and on the left while waning, its terminator bowing the right way',()=>{
 const sweeps=d=>[...d.matchAll(/ 0 0 ([01]) /g)].map(m=>Number(m[1]));
 assert.deepEqual(sweeps(moon.moonDiscPath(10,10,5,0.25,true)),[1,0],'waxing crescent: right limb, terminator bowing right');
 assert.deepEqual(sweeps(moon.moonDiscPath(10,10,5,0.75,true)),[1,1],'waxing gibbous: terminator bowing left');
 assert.deepEqual(sweeps(moon.moonDiscPath(10,10,5,0.25,false)),[0,1]);
 assert.deepEqual(sweeps(moon.moonDiscPath(10,10,5,0.75,false)),[0,0]);
 assert.match(moon.moonDiscPath(10,10,5,0.25,true),/A2\.50,5\.00/,'terminator half-width r·|1−2f|');
 assert.equal(moon.moonDiscPath(10,10,5,0.001,true),'','new moon: nothing lit');
 const strip=moon.moonStrip('2026-10-30');
 assert.equal(strip.discs.length,30);assert.equal(strip.discs[0].date,'2026-10-30');assert.equal(strip.discs[29].date,'2026-11-28');
 assert.equal(strip.discs[0].percent,70);
 assert.deepEqual([strip.height,strip.discs[0].cy,strip.discs[15].cy,strip.discs[15].cx],[32,8,24,strip.discs[0].cx],'two rows of fifteen');
 const fullest=strip.discs.reduce((a,b)=>b.fraction>a.fraction?b:a);assert.equal(fullest.date,'2026-11-24','99.47% at 9 PM, against 99.43% the evening before');
});

test('the daylight panel adds the Moon: tonight, the strip of evenings, and the next phases',async()=>{
 const h=await componentHarness('app/category-map-dock.tsx',{});
 const base={look:maps.CATEGORY_MAPS.sky,mode:'globe',depth:1,azimuth:315,sun:null,sunAvailable:false,terrainAvailable:true,onMode(){},onDepth(){},onAzimuth(){},onRealSun(){},onSunTime(){},sunPlaying:false,motionAllowed:true,onSunPlay(){},onReset(){},onLayers(){},onClose(){},onSunYear(){},onSunYearCentre(){}};
 const strip=moon.moonStrip('2026-10-30');
 const tree=h.render(h.exports.CategoryMapDock,{...base,sunYear:{on:true,place:'x',outside:false,reading:null,chart:null,note:null,atCentre:true,
  moon:{reading:moon.moonReading('2026-10-30',CENTRE.lat,CENTRE.lon),phases:moon.phaseList(Date.parse('2026-10-30T12:00:00Z')),strip}}});
 const text=JSON.stringify(tree);assert.match(text,/Moon tonight: waning gibbous, 70% lit/);assert.match(text,/Full moon Nov 24, 8:53 AM CST/);
 const node=findNode(tree,n=>n.type===h.exports.MoonPhaseStrip);const figure=node.type(node.props);
 assert.equal(figure.props['aria-label'],'The Moon over the next 30 evenings, from 70% lit tonight; fullest 2026-11-24, 99% lit');
 assert.equal((JSON.stringify(figure).match(/"data-date"/g)||[]).length,30);
 assert.match(page,/moon: sunYearMoon,/);assert.match(page,/reading: moonReading\(sunToday, sunYearPlace\.lat, sunYearPlace\.lon\)/);
});
