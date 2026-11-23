// The Kansas records page: the largest and smallest values in four datasets the labs already ship.
// app/kansas-records.generated.json is written by scripts/prepare-kansas-records.mjs.
import records from "./kansas-records.generated.json";

export const RECORD_EXPLORERS = {
  people: { href: "/labs?story=census-mosaic", label: "Explore county population" },
  survey: { href: "/labs/observatory", label: "Compare county estimates" },
  bridges: { href: "/labs?story=built-kansas", label: "Explore the bridge inventory" },
  tornadoes: { href: "/labs?story=tornado-tracks", label: "Explore historical tornado tracks" },
} as const;

export type RecordItem = { label: string; value: string; where: string; href?: string; note?: string };
export type RecordSection = {
  id: keyof typeof RECORD_EXPLORERS;
  title: string;
  source: string;
  caution: string;
  snapshot: { path: string; bytes: number; sha256: string };
  items: RecordItem[];
};
export const KANSAS_RECORDS = records.sections as unknown as readonly RecordSection[];
