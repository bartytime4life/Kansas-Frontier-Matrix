export type ViewState = {
  bbox?: [number, number, number, number];
  layers: string[];
  time?: string;
  filters: Record<string, string | number | boolean>;
};
