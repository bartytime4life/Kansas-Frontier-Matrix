export type AvailabilityBin = Readonly<{ start: number; end: number; peak: number; total: number }>;

/** Ordinal bins summarize recorded counts; they never fill missing years. */
export const buildAvailabilityBins = (
  steps: readonly number[], counts: Readonly<Record<number, number>>, maxBins = 24,
): AvailabilityBin[] => {
  if (steps.length === 0 || maxBins < 1) return [];
  const size = Math.ceil(steps.length / maxBins);
  const bins: AvailabilityBin[] = [];
  for (let index = 0; index < steps.length; index += size) {
    const group = steps.slice(index, index + size);
    const values = group.map((step) => Math.max(0, counts[step] ?? 0));
    bins.push({ start: group[0], end: group[group.length - 1], peak: Math.max(...values), total: values.reduce((sum, value) => sum + value, 0) });
  }
  return bins;
};
