/**
 * Static decoding of common ICAO aircraft type designators (ICAO Doc 8643)
 * into manufacturer, model, engine class and wake turbulence category. The
 * feed's `t` field is the designator; this table only expands it. Unknown or
 * rare designators stay raw: nothing is guessed from a registration or
 * callsign. Wake categories follow ICAO (L under 7,000 kg MTOW, M to
 * 136,000 kg, H above, J for the A380). Checked against Doc 8643 on
 * 2026-11-06; no runtime imports, so tests load this file on its own.
 */
export type EngineClass = "piston" | "turboprop" | "jet" | "piston helicopter" | "turbine helicopter" | "tiltrotor" | "unpowered";
export type WakeCategory = "L" | "M" | "H" | "J";
export type AircraftTypeInfo = Readonly<{ code: string; manufacturer: string; model: string; engine: EngineClass; wake: WakeCategory }>;

export const AIRCRAFT_TYPE_SOURCE = "Static table of ICAO Doc 8643 designators (checked 2026-11-06); the feed supplies only the code.";
export const WAKE_TITLES: Readonly<Record<WakeCategory, string>> = Object.freeze({ L: "light", M: "medium", H: "heavy", J: "super" });

type Row = readonly [string, string, string, EngineClass, WakeCategory];
const ROWS: readonly Row[] = [
  // Airbus and Boeing airliners
  ["A19N", "Airbus", "A319neo", "jet", "M"], ["A20N", "Airbus", "A320neo", "jet", "M"], ["A21N", "Airbus", "A321neo", "jet", "M"],
  ["A318", "Airbus", "A318", "jet", "M"], ["A319", "Airbus", "A319", "jet", "M"], ["A320", "Airbus", "A320", "jet", "M"], ["A321", "Airbus", "A321", "jet", "M"],
  ["A306", "Airbus", "A300-600", "jet", "H"], ["A332", "Airbus", "A330-200", "jet", "H"], ["A333", "Airbus", "A330-300", "jet", "H"], ["A339", "Airbus", "A330-900neo", "jet", "H"],
  ["A343", "Airbus", "A340-300", "jet", "H"], ["A359", "Airbus", "A350-900", "jet", "H"], ["A35K", "Airbus", "A350-1000", "jet", "H"], ["A388", "Airbus", "A380-800", "jet", "J"],
  ["B712", "Boeing", "717-200", "jet", "M"], ["B733", "Boeing", "737-300", "jet", "M"], ["B734", "Boeing", "737-400", "jet", "M"], ["B735", "Boeing", "737-500", "jet", "M"],
  ["B736", "Boeing", "737-600", "jet", "M"], ["B737", "Boeing", "737-700", "jet", "M"], ["B738", "Boeing", "737-800", "jet", "M"], ["B739", "Boeing", "737-900", "jet", "M"],
  ["B37M", "Boeing", "737 MAX 7", "jet", "M"], ["B38M", "Boeing", "737 MAX 8", "jet", "M"], ["B39M", "Boeing", "737 MAX 9", "jet", "M"], ["B3XM", "Boeing", "737 MAX 10", "jet", "M"],
  ["B744", "Boeing", "747-400", "jet", "H"], ["B748", "Boeing", "747-8", "jet", "H"], ["B752", "Boeing", "757-200", "jet", "M"], ["B753", "Boeing", "757-300", "jet", "M"],
  ["B762", "Boeing", "767-200", "jet", "H"], ["B763", "Boeing", "767-300", "jet", "H"], ["B764", "Boeing", "767-400", "jet", "H"],
  ["B772", "Boeing", "777-200", "jet", "H"], ["B773", "Boeing", "777-300", "jet", "H"], ["B77L", "Boeing", "777-200LR / 777F", "jet", "H"], ["B77W", "Boeing", "777-300ER", "jet", "H"],
  ["B788", "Boeing", "787-8", "jet", "H"], ["B789", "Boeing", "787-9", "jet", "H"], ["B78X", "Boeing", "787-10", "jet", "H"],
  ["MD11", "McDonnell Douglas", "MD-11", "jet", "H"], ["MD82", "McDonnell Douglas", "MD-82", "jet", "M"], ["MD83", "McDonnell Douglas", "MD-83", "jet", "M"], ["MD88", "McDonnell Douglas", "MD-88", "jet", "M"],
  // Regional airliners
  ["CRJ2", "Bombardier", "CRJ-200", "jet", "M"], ["CRJ7", "Bombardier", "CRJ-700", "jet", "M"], ["CRJ9", "Bombardier", "CRJ-900", "jet", "M"], ["CRJX", "Bombardier", "CRJ-1000", "jet", "M"],
  ["E135", "Embraer", "ERJ-135", "jet", "M"], ["E145", "Embraer", "ERJ-145", "jet", "M"], ["E170", "Embraer", "E170", "jet", "M"], ["E175", "Embraer", "E175", "jet", "M"],
  ["E190", "Embraer", "E190", "jet", "M"], ["E195", "Embraer", "E195", "jet", "M"], ["E290", "Embraer", "E190-E2", "jet", "M"], ["E295", "Embraer", "E195-E2", "jet", "M"],
  ["BCS1", "Airbus", "A220-100", "jet", "M"], ["BCS3", "Airbus", "A220-300", "jet", "M"],
  ["DH8A", "De Havilland Canada", "Dash 8-100", "turboprop", "M"], ["DH8B", "De Havilland Canada", "Dash 8-200", "turboprop", "M"], ["DH8C", "De Havilland Canada", "Dash 8-300", "turboprop", "M"], ["DH8D", "De Havilland Canada", "Dash 8-400", "turboprop", "M"],
  ["AT43", "ATR", "ATR 42-300", "turboprop", "M"], ["AT45", "ATR", "ATR 42-500", "turboprop", "M"], ["AT72", "ATR", "ATR 72-200", "turboprop", "M"], ["AT75", "ATR", "ATR 72-500", "turboprop", "M"], ["AT76", "ATR", "ATR 72-600", "turboprop", "M"],
  ["SF34", "Saab", "340", "turboprop", "M"], ["B190", "Beechcraft", "1900", "turboprop", "M"], ["SW4", "Fairchild", "Metro / Merlin IV", "turboprop", "M"],
  // Business jets (Wichita builds many of these)
  ["C510", "Cessna", "Citation Mustang", "jet", "L"], ["C525", "Cessna", "CitationJet / CJ1", "jet", "L"], ["C25A", "Cessna", "Citation CJ2", "jet", "L"], ["C25B", "Cessna", "Citation CJ3", "jet", "L"], ["C25C", "Cessna", "Citation CJ4", "jet", "M"],
  ["C550", "Cessna", "Citation II / Bravo", "jet", "L"], ["C560", "Cessna", "Citation V / Ultra / Encore", "jet", "M"], ["C56X", "Cessna", "Citation Excel / XLS", "jet", "M"],
  ["C650", "Cessna", "Citation III / VI / VII", "jet", "M"], ["C680", "Cessna", "Citation Sovereign", "jet", "M"], ["C68A", "Cessna", "Citation Latitude", "jet", "M"],
  ["C700", "Cessna", "Citation Longitude", "jet", "M"], ["C750", "Cessna", "Citation X", "jet", "M"],
  ["BE40", "Beechcraft", "Beechjet 400 / Hawker 400", "jet", "M"], ["PRM1", "Beechcraft", "Premier I", "jet", "L"], ["H25B", "Hawker", "800 / 850 / 900", "jet", "M"], ["HA4T", "Hawker", "4000", "jet", "M"],
  ["LJ31", "Learjet", "31", "jet", "M"], ["LJ35", "Learjet", "35 / 36", "jet", "M"], ["LJ45", "Learjet", "45", "jet", "M"], ["LJ60", "Learjet", "60", "jet", "M"], ["LJ75", "Learjet", "70 / 75", "jet", "M"],
  ["CL30", "Bombardier", "Challenger 300", "jet", "M"], ["CL35", "Bombardier", "Challenger 350", "jet", "M"], ["CL60", "Bombardier", "Challenger 600 series", "jet", "M"],
  ["GL5T", "Bombardier", "Global 5000", "jet", "M"], ["GLEX", "Bombardier", "Global Express / 6000", "jet", "M"], ["GL7T", "Bombardier", "Global 7500", "jet", "M"],
  ["GLF4", "Gulfstream", "G-IV / G400 / G450", "jet", "M"], ["GLF5", "Gulfstream", "G-V / G550", "jet", "M"], ["GLF6", "Gulfstream", "G650", "jet", "M"],
  ["E50P", "Embraer", "Phenom 100", "jet", "L"], ["E55P", "Embraer", "Phenom 300", "jet", "M"], ["E545", "Embraer", "Legacy 450 / Praetor 500", "jet", "M"], ["E550", "Embraer", "Legacy 500 / Praetor 600", "jet", "M"],
  ["FA50", "Dassault", "Falcon 50", "jet", "M"], ["F2TH", "Dassault", "Falcon 2000", "jet", "M"], ["F900", "Dassault", "Falcon 900", "jet", "M"], ["FA7X", "Dassault", "Falcon 7X", "jet", "M"], ["FA8X", "Dassault", "Falcon 8X", "jet", "M"],
  ["PC24", "Pilatus", "PC-24", "jet", "M"],
  // Turboprops
  ["PC12", "Pilatus", "PC-12", "turboprop", "L"], ["TBM7", "Daher (Socata)", "TBM 700", "turboprop", "L"], ["TBM8", "Daher (Socata)", "TBM 850", "turboprop", "L"], ["TBM9", "Daher", "TBM 900 series", "turboprop", "L"],
  ["BE9L", "Beechcraft", "King Air 90", "turboprop", "L"], ["BE20", "Beechcraft", "King Air 200", "turboprop", "L"], ["BE30", "Beechcraft", "King Air 300", "turboprop", "L"], ["B350", "Beechcraft", "King Air 350", "turboprop", "L"],
  ["C208", "Cessna", "208 Caravan", "turboprop", "L"], ["C441", "Cessna", "441 Conquest II", "turboprop", "L"], ["DHC6", "De Havilland Canada", "DHC-6 Twin Otter", "turboprop", "L"],
  ["MU2", "Mitsubishi", "MU-2", "turboprop", "L"], ["P46T", "Piper", "Meridian / M500 / M600", "turboprop", "L"], ["PAY2", "Piper", "Cheyenne II", "turboprop", "L"],
  // Piston singles and twins
  ["C150", "Cessna", "150", "piston", "L"], ["C152", "Cessna", "152", "piston", "L"], ["C172", "Cessna", "172 Skyhawk", "piston", "L"], ["C177", "Cessna", "177 Cardinal", "piston", "L"],
  ["C180", "Cessna", "180 Skywagon", "piston", "L"], ["C182", "Cessna", "182 Skylane", "piston", "L"], ["C185", "Cessna", "185 Skywagon", "piston", "L"], ["C206", "Cessna", "206 Stationair", "piston", "L"],
  ["C210", "Cessna", "210 Centurion", "piston", "L"], ["C310", "Cessna", "310", "piston", "L"], ["C340", "Cessna", "340", "piston", "L"], ["C402", "Cessna", "402", "piston", "L"],
  ["C414", "Cessna", "414 Chancellor", "piston", "L"], ["C421", "Cessna", "421 Golden Eagle", "piston", "L"],
  ["P28A", "Piper", "PA-28 Cherokee / Warrior / Archer", "piston", "L"], ["P28B", "Piper", "PA-28-235 / Dakota", "piston", "L"], ["P28R", "Piper", "PA-28R Arrow", "piston", "L"], ["P28T", "Piper", "PA-28RT Turbo Arrow", "piston", "L"],
  ["PA18", "Piper", "PA-18 Super Cub", "piston", "L"], ["PA24", "Piper", "PA-24 Comanche", "piston", "L"], ["PA30", "Piper", "PA-30 Twin Comanche", "piston", "L"], ["PA31", "Piper", "PA-31 Navajo", "piston", "L"],
  ["PA32", "Piper", "PA-32 Cherokee Six / Saratoga", "piston", "L"], ["PA34", "Piper", "PA-34 Seneca", "piston", "L"], ["PA38", "Piper", "PA-38 Tomahawk", "piston", "L"], ["PA44", "Piper", "PA-44 Seminole", "piston", "L"], ["PA46", "Piper", "PA-46 Malibu / Mirage", "piston", "L"],
  ["BE23", "Beechcraft", "Musketeer / Sundowner", "piston", "L"], ["BE33", "Beechcraft", "Bonanza 33 / Debonair", "piston", "L"], ["BE35", "Beechcraft", "Bonanza 35 (V-tail)", "piston", "L"], ["BE36", "Beechcraft", "Bonanza 36", "piston", "L"],
  ["BE55", "Beechcraft", "Baron 55", "piston", "L"], ["BE58", "Beechcraft", "Baron 58", "piston", "L"], ["BE76", "Beechcraft", "Duchess", "piston", "L"],
  ["M20P", "Mooney", "M20 (piston)", "piston", "L"], ["M20T", "Mooney", "M20 (turbocharged)", "piston", "L"],
  ["DA20", "Diamond", "DA20 Katana / Eclipse", "piston", "L"], ["DA40", "Diamond", "DA40 Star", "piston", "L"], ["DA42", "Diamond", "DA42 Twin Star", "piston", "L"], ["DA62", "Diamond", "DA62", "piston", "L"],
  ["SR20", "Cirrus", "SR20", "piston", "L"], ["SR22", "Cirrus", "SR22", "piston", "L"], ["S22T", "Cirrus", "SR22T", "piston", "L"],
  ["RV6", "Van's", "RV-6", "piston", "L"], ["RV7", "Van's", "RV-7", "piston", "L"], ["RV8", "Van's", "RV-8", "piston", "L"], ["RV10", "Van's", "RV-10", "piston", "L"], ["RV12", "Van's", "RV-12", "piston", "L"],
  ["AA5", "Grumman American", "AA-5 Traveler / Cheetah / Tiger", "piston", "L"],
  // Helicopters
  ["R22", "Robinson", "R22", "piston helicopter", "L"], ["R44", "Robinson", "R44", "piston helicopter", "L"], ["R66", "Robinson", "R66", "turbine helicopter", "L"],
  ["B06", "Bell", "206 JetRanger / LongRanger", "turbine helicopter", "L"], ["B407", "Bell", "407", "turbine helicopter", "L"], ["B412", "Bell", "412", "turbine helicopter", "L"], ["B429", "Bell", "429", "turbine helicopter", "L"], ["B505", "Bell", "505", "turbine helicopter", "L"],
  ["EC20", "Airbus Helicopters", "EC120 / H120", "turbine helicopter", "L"], ["EC30", "Airbus Helicopters", "EC130 / H130", "turbine helicopter", "L"], ["EC35", "Airbus Helicopters", "EC135 / H135", "turbine helicopter", "L"], ["EC45", "Airbus Helicopters", "EC145 / H145", "turbine helicopter", "L"],
  ["AS50", "Airbus Helicopters", "AS350 / H125", "turbine helicopter", "L"], ["AS55", "Airbus Helicopters", "AS355", "turbine helicopter", "L"],
  ["A109", "Leonardo (Agusta)", "A109", "turbine helicopter", "L"], ["A139", "Leonardo (AgustaWestland)", "AW139", "turbine helicopter", "L"], ["A169", "Leonardo", "AW169", "turbine helicopter", "L"],
  ["S76", "Sikorsky", "S-76", "turbine helicopter", "L"], ["S92", "Sikorsky", "S-92", "turbine helicopter", "M"],
  // Military (the feed's military flag is separate; this only names the type)
  ["C130", "Lockheed", "C-130 Hercules", "turboprop", "M"], ["C30J", "Lockheed Martin", "C-130J Super Hercules", "turboprop", "M"], ["C17", "Boeing", "C-17 Globemaster III", "jet", "H"], ["C5M", "Lockheed", "C-5M Super Galaxy", "jet", "H"],
  ["K35R", "Boeing", "KC-135R Stratotanker", "jet", "H"], ["B52", "Boeing", "B-52 Stratofortress", "jet", "H"], ["P8", "Boeing", "P-8 Poseidon", "jet", "M"],
  ["F16", "General Dynamics / Lockheed Martin", "F-16 Fighting Falcon", "jet", "M"], ["F15", "McDonnell Douglas / Boeing", "F-15 Eagle", "jet", "M"], ["F18H", "McDonnell Douglas / Boeing", "F/A-18 Hornet", "jet", "M"], ["F35", "Lockheed Martin", "F-35 Lightning II", "jet", "M"],
  ["T38", "Northrop", "T-38 Talon", "jet", "L"], ["TEX2", "Beechcraft", "T-6 Texan II", "turboprop", "L"],
  ["H60", "Sikorsky", "UH-60 Black Hawk", "turbine helicopter", "M"], ["H64", "Boeing", "AH-64 Apache", "turbine helicopter", "M"], ["H47", "Boeing", "CH-47 Chinook", "turbine helicopter", "M"], ["UH1", "Bell", "UH-1 Iroquois", "turbine helicopter", "L"],
  ["V22", "Bell Boeing", "V-22 Osprey", "tiltrotor", "M"],
  // Generic ICAO designators the feed uses when the exact model is not known
  ["GLID", "(generic)", "glider or sailplane", "unpowered", "L"], ["BALL", "(generic)", "balloon", "unpowered", "L"], ["ULAC", "(generic)", "ultralight", "piston", "L"], ["GYRO", "(generic)", "autogyro", "piston", "L"],
];

export const AIRCRAFT_TYPES: ReadonlyMap<string, AircraftTypeInfo> = new Map(ROWS.map(([code, manufacturer, model, engine, wake]) =>
  [code, Object.freeze({ code, manufacturer, model, engine, wake })]));

/** Decoded information for an ICAO designator, or null when the table has no entry (the raw code is then the whole truth). */
export function decodeAircraftType(code: string | null | undefined): AircraftTypeInfo | null {
  if (typeof code !== "string") return null;
  return AIRCRAFT_TYPES.get(code.trim().toUpperCase()) ?? null;
}

/** One line beside the raw code: "B738 · Boeing 737-800 · jet · medium wake (static table)"; an unknown code stays raw. */
export function aircraftTypeLine(code: string | null | undefined): string {
  if (!code) return "Aircraft type not reported";
  const info = decodeAircraftType(code);
  return info ? `${code} · ${info.manufacturer} ${info.model} · ${info.engine} · ${WAKE_TITLES[info.wake]} wake (static table)` : `${code} · designator not in the static table`;
}
