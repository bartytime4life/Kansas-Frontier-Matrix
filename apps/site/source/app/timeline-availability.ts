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

/** Major ticks whose labels fit. Ticks are equal-width columns, so deep-time
 * steps sit a few columns apart; an interior label closer than minGap (a share
 * of the axis) to the previous shown label or to the last tick keeps its mark
 * but drops its text. The first and last major ticks are always labelled. */
export const timelineLabelSteps = (
  steps: readonly number[], majors: ReadonlySet<number>, minGap = 0.06,
): Set<number> => {
  const indexes = steps.flatMap((step, index) => majors.has(step) ? [index] : []);
  const shown = new Set<number>();
  if (indexes.length === 0) return shown;
  const span = Math.max(1, steps.length - 1);
  const lastIndex = indexes[indexes.length - 1];
  let previous = indexes[0];
  shown.add(steps[previous]);
  for (const index of indexes.slice(1, -1)) {
    if ((index - previous) / span < minGap || (lastIndex - index) / span < minGap) continue;
    shown.add(steps[index]);
    previous = index;
  }
  shown.add(steps[lastIndex]);
  return shown;
};
