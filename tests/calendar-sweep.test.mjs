import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
const source = await readFile(new URL("../app/calendar-sweep.ts", import.meta.url), "utf8");
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const c = await import("data:text/javascript;base64," + Buffer.from(js).toString("base64"));
const today = "2026-10-20";
test("calendar validation refuses future dates, invalid leap days, and non-calendar input", () => {
  for (const day of ["2026-10-21", "1900-02-29", "2026-04-31", "1799-12-31", "2026-1-1", "", null, 2026]) assert.equal(c.validCalendarDay(day, today), false);
  for (const day of ["1800-01-01", "2000-02-29", today]) assert.equal(c.validCalendarDay(day, today), true);
});
test("changing year or month clamps month ends and leap dates without timezone drift", () => {
  assert.equal(c.replaceCalendarPart("2024-02-29", "year", 2023, today), "2023-02-28");
  assert.equal(c.replaceCalendarPart("2026-01-31", "month", 2, today), "2026-02-28");
  assert.equal(c.replaceCalendarPart("2026-09-30", "month", 12, today), today);
  assert.equal(c.replaceCalendarPart("2026-01-01", "month", 13, today), "2026-01-01");
});
test("UTC daily frames cross daylight-saving boundaries without duplicated or missing dates", () => {
  assert.deepEqual(c.calendarFrames("2026-03-07", "2026-03-10", "days"), ["2026-03-07", "2026-03-08", "2026-03-09", "2026-03-10"]);
  assert.deepEqual(c.calendarFrames("2024-02-28", "2024-03-01", "days"), ["2024-02-28", "2024-02-29", "2024-03-01"]);
});
test("monthly and yearly frames preserve their anchor and explicit end; they do not invent averages", () => {
  assert.deepEqual(c.calendarFrames("2026-01-31", "2026-04-15", "months"), ["2026-01-31", "2026-02-28", "2026-03-31", "2026-04-15"]);
  assert.deepEqual(c.calendarFrames("2024-02-29", "2026-03-01", "years"), ["2024-02-29", "2025-02-28", "2026-02-28", "2026-03-01"]);
  assert.deepEqual(c.calendarFrames("2026-03-02", "2026-03-01", "days"), []);
});
test("frame lookup gives the preceding frame and handles dates between month anchors", () => {
  const frames = ["2026-01-01", "2026-02-01", "2026-03-01"];
  assert.equal(c.calendarFrameIndex(frames, "2026-02-15"), 1);
  assert.equal(c.calendarFrameIndex(frames, "2026-01-01"), 0);
  assert.equal(c.calendarFrameIndex(frames, "2026-03-01"), 2);
});
test("URL restore preserves comparison sides and rejects malformed, reversed, oversized, or future state", () => {
  const good = { day: "2026-10-12", start: "2026-10-01", end: today, step: "days", before: "2026-10-01", showing: "B" };
  assert.deepEqual(c.readCalendarSweep(JSON.stringify(good), today), good);
  assert.equal(c.calendarFrameDay({ ...good, showing: "A" }), good.before);
  for (const patch of [{day:"2026-10-21"},{start:"2026-10-13"},{end:"2026-10-11"},{step:"seconds"},{showing:"A",before:null},{before:"1900-02-29"}]) assert.equal(c.readCalendarSweep(JSON.stringify({...good,...patch}),today),null);
  for (const raw of ["{", "null", "[]", "x".repeat(513)]) assert.equal(c.readCalendarSweep(raw,today),null);
});
test("date seeking preserves the A pin, expands explicit bounds, and returns to side B", () => {
  const old = {day:"2026-10-12",start:"2026-10-01",end:today,step:"days",before:"2026-10-01",showing:"A"};
  assert.deepEqual(c.calendarDayInRange(old,"2026-09-10"),{...old,day:"2026-09-10",start:"2026-09-10",showing:"B"});
});
test("calendar source selection honors query floors and never silently activates a source", () => {
  const visible = {"usgs-earthquakes":true,"noaa-hms-smoke":true,"nasa-gibs-fire-points":true,"raspberry-shake-stations":false};
  assert.deepEqual(c.calendarArchiveFeeds(visible,"2000-01-01"),["usgs-earthquakes"]);
  assert.deepEqual(c.calendarArchiveFeeds(visible,"2026-10-01"),["usgs-earthquakes","noaa-hms-smoke","nasa-gibs-fire-points"]);
});
test("historical visibility requires an exact checked day, matching year, selected source, and current build", () => {
  const base={"usgs-earthquakes":false,"noaa-hms-smoke":false,"nws-alerts":false,"static":true};
  const selected={...base,"usgs-earthquakes":true,"noaa-hms-smoke":true,"nws-alerts":true};
  const currentOnly=["usgs-earthquakes","noaa-hms-smoke","nws-alerts"];
  const apply=(checked={},year=2024,ready=true)=>c.calendarVisibility(base,selected,"2024-02-29",year,today,checked,currentOnly,ready);
  assert.equal(apply()["usgs-earthquakes"],false);
  assert.equal(apply({"usgs-earthquakes":"2024-02-28"})["usgs-earthquakes"],false);
  assert.equal(apply({"usgs-earthquakes":"2024-02-29"})["usgs-earthquakes"],true);
  assert.equal(apply({"usgs-earthquakes":"2024-02-29"},2023)["usgs-earthquakes"],false);
  assert.equal(apply({"usgs-earthquakes":"2024-02-29"},2024,false)["usgs-earthquakes"],false);
  assert.equal(apply({"nws-alerts":"2024-02-29"})["nws-alerts"],false);
  assert.equal(apply().static,true);
});
test("calendar visibility retains ordinary atlas behavior when no calendar is active", () => {
  const base={"nws-alerts":true};
  assert.equal(c.calendarVisibility(base,base,null,2026,today,{},["nws-alerts"],true),base);
});
