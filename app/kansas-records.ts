// The Kansas records page: the largest and smallest values in four datasets the labs already ship.
// app/kansas-records.generated.json is written by scripts/prepare-kansas-records.mjs.
import records from "./kansas-records.generated.json";

export type RecordItem = { label: string; value: string; where: string; href?: string; note?: string };
export type RecordSection = { id: string; title: string; source: string; caution: string; items: RecordItem[] };
export const KANSAS_RECORDS = records.sections as unknown as readonly RecordSection[];
