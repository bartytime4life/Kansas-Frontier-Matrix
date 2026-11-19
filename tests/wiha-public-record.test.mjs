import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

// Execute the actual projection; all personal values below are invented.
const js = ts.transpileModule(await readFile(new URL("../app/wiha-public-record.ts", import.meta.url), "utf8"), {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
const { wihaPublicRecord: project } = await import(`data:text/javascript;base64,${Buffer.from(js).toString("base64")}`);

test("public administration, geography, wildlife and historical text survive without an identity target", () => {
  for (const note of ["Program payment to landowner $12 per acre", "Owner payment $1,250; contract expires 2030",
    "Bill paid $1,250; contract expires 2030", "Mark public access boundaries with signs", "$-to owner",
    "mark signs at the public access gate", "bill for this contract paid $12 per acre",
    "Landowners receive $12 per acre for this contract", "Clark county; payment $12 per acre", "Access from Dale road",
    "Pheasants last seen at the north gate", "Contract TEST-42; paid $1,250; expires 2030. Pheasants last seen at the north gate",
    "No home address: only public tract information", "Do not publish a home address",
    "John Brown historic interpretation; public program payment $12", "Contract reference 1234567890; payment $1234567890"]) {
    assert.equal(project({ NOTES: note }).notes, note, note);
  }
});

test("personal contact, residence and movement variants are held before presentation", () => {
  for (const note of ["Personal phone 2025550199", "Call owner on (202)5550199", "Call owner on 202‑555‑0199",
    "Personal phone ２０２５５５０１９９", "Owner email example [at] example [dot] com", "Contact exam\u200bple@example.com",
    "2025550199 (owner phone)", "Owner email example at example dot com", "The family lives by the north gate",
    "The owner's home is the blue house by the gate", "The tenant residence is beside north gate", "Alice Park owns N/2 Sec 24",
    "Home address is 123 Fictional Lane", "Avery Example, 123 Fictional Lane, Demo KS", "Owner mailing address: 123 Fictional Lane",
    "Avery Example resides at 123 Fictional Lane", "Avery Example is currently at 38.0000, -98.0000",
    "Avery Example leaves home at 06:15 every weekday; follow to the gate", "Track Avery Example from home to work each morning",
    "Avery Example last known location: north gate", "Real-time location of Avery Example is north gate",
    "alice example at the north gate at 07:00 daily", "Avery Example at the north gate at 07:00 daily", "Example family home is the blue house by the gate",
    "Public note. " + "A".repeat(227) + " a@example.com", "A".repeat(240) + " Personal phone 2025550199"]) {
    const result = project({ NOTES: note, CONTRACTID: "TEST-42" });
    assert.equal(result.notes, null, note);
    assert.match(result.notesStatus, /review required/);
    assert.equal(result.contractReference, "TEST-42");
  }
  // A public/historical prefix is not authority to bypass a personal detail.
  for (const note of ["Public historical reference. Home address is 123 Fictional Lane", "Pheasants last seen at the gate. Avery Example last seen at home",
    "Historic public tract. Alice Example T1S R1W", "John Brown historic interpretation; Alice Example N/2 Sec 24"]) {
    assert.equal(project({ NOTES: note }).notes, null, note);
  }
});

test("county output is canonical and every species slot is screened in full independently", async () => {
  const manifest = JSON.parse(await readFile(new URL("../public/data/subsurface/manifest.json", import.meta.url), "utf8"));
  assert.equal(manifest.counties.length, 105);
  for (const { name } of manifest.counties) assert.equal(project({ COUNTY: ` ${name.toUpperCase()} County ` }).county, name);
  for (const slot of [1, 2, 3, 4, 5]) for (const value of ["example@example.com", "Pheasant " + " ".repeat(80) + "Personal phone 2025550199", "Pheasant "+"A".repeat(45)+" example@example.com", "X".repeat(4097), "123 Fictional Lane", "2025550199",
    "2025550199 (owner phone)", "The family lives by the north gate", "Alice Park owns N/2 Sec 24", "Owner email example at example dot com"]) {
    const result = project({ COUNTY: "example@example.com", SPECIES1: "Sandhill crane", [`SPECIES${slot}`]: value, NOTES: "Contact example@example.com" });
    assert.equal(result.county, null);
    assert.ok(!JSON.stringify(result).includes("example@example.com"));
    assert.ok(!JSON.stringify(result).includes("2025550199"));
    assert.match(result.fieldsStatus, /review required/);
    assert.equal(result.species, slot === 1 ? null : "Sandhill crane");
  }
  assert.equal(project({ COUNTY: "Dickinson", SPECIES1: "Sandhill crane", NOTES: "Payment $12 per acre" }).notes, "Payment $12 per acre");
  for (const label of ["Ross's goose", "Virginia rail", "Richard's pipit", "American wigeon", "Sandhill crane"]) assert.equal(project({ SPECIES1: label }).species, label);
  for (const field of ["NOTES", "COUNTY", "SPECIES1", "SPECIES2", "SPECIES3", "SPECIES4", "SPECIES5"]) {
    const result = project({ CONTRACTID: 2025550199, [field]: "2025550199 (owner phone)" });
    assert.equal(result.contractReference, null, `${field} must not reintroduce its held phone through a reference`);
    assert.ok(!JSON.stringify(result).includes("2025550199"));
  }
});

test("original bounds and opaque administrative references remain independent of phone guesses", () => {
  for (const length of [240, 241, 4096]) {
    const result = project({ NOTES: "A".repeat(length) });
    assert.equal(result.notes.length, Math.min(length, 240));
  }
  for (const note of ["A".repeat(4097), " ".repeat(4097) + "Payment $12", "A".repeat(65536)]) assert.equal(project({ NOTES: note }).notes, null);
  for (const reference of [42, "TEST-42", "ABC/12.3", 2025550199]) assert.equal(project({ CONTRACTID: reference }).contractReference, String(reference));
  for (const reference of ["example@example.com", "202-555-0199", "000-00-0000", "SSN000000000"]) assert.equal(project({ CONTRACTID: reference }).contractReference, null);
  assert.equal(project({ CONTRACTID: 2025550199, NOTES: "Contract 2025550199; payment $12" }).contractReference, "2025550199");
  assert.equal(project({ CONTRACTID: 2025550199, NOTES: "Personal phone 202-555-0199" }).contractReference, null, "a reference duplicating a detected held phone needs review");
});
