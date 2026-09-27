import type { StreamflowFrame } from "./streamflow";
import type { NoaaGaugeFeatureProperties } from "./noaa-hydrology";

export type MapSignal = Readonly<{ kind: "observed" | "forecast" | "catalog"; title: string; detail: string }>;

export const deriveMapSignals = ({ streamflow, gauges, entered, exited }: {
  streamflow?: StreamflowFrame | null;
  gauges?: readonly NoaaGaugeFeatureProperties[];
  entered?: number;
  exited?: number;
}): MapSignal[] => {
  const signals: MapSignal[] = [];
  if (streamflow) {
    const comparable = streamflow.features.filter(({ properties }) => !properties.missing && ["rising", "falling", "steady"].includes(properties.trend));
    if (comparable.length >= 3) {
      const rising = comparable.filter(({ properties }) => properties.trend === "rising").length;
      const falling = comparable.filter(({ properties }) => properties.trend === "falling").length;
      if (rising > comparable.length / 2 || falling > comparable.length / 2) {
        signals.push({ kind: "observed", title: `${Math.max(rising, falling)} of ${comparable.length} sampled gauges ${rising > falling ? "rising" : "falling"}`,
          detail: `USGS observations at the selected River Pulse cursor. Sampled gauges only; this is not a statewide trend or flood prediction.` });
      }
    }
  }
  const comparableForecasts = (gauges ?? []).filter((gauge) => gauge.hasForecast
    && gauge.observedValue !== null && gauge.forecastValue !== null
    && Boolean(gauge.observedUnit && gauge.observedUnit === gauge.forecastUnit)
    && Boolean(gauge.observedAt && gauge.forecastAt && Date.parse(gauge.forecastAt) > Date.parse(gauge.observedAt)));
  if (comparableForecasts.length >= 2) {
    const higher = comparableForecasts.filter((gauge) => gauge.forecastValue! > gauge.observedValue!).length;
    const lower = comparableForecasts.filter((gauge) => gauge.forecastValue! < gauge.observedValue!).length;
    if (higher > comparableForecasts.length / 2 || lower > comparableForecasts.length / 2) {
      signals.push({ kind: "forecast", title: `${Math.max(higher, lower)} of ${comparableForecasts.length} NOAA gauge forecasts ${higher > lower ? "above" : "below"} latest observation`,
        detail: "Provider forecast values at their stated future times, compared only within each gauge and matching unit. This does not predict a flood or conditions between gauges." });
    }
  }
  if ((entered ?? 0) > 0 || (exited ?? 0) > 0) {
    signals.push({ kind: "catalog", title: `${entered ?? 0} records entered · ${exited ?? 0} exited`,
      detail: "Change in visible time-aware catalog records between declared frames. It is not measured environmental change." });
  }
  return signals;
};
