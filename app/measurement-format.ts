/**
 * A measured polygon's area in words. Fields and parcels are fractions of a
 * square mile, so areas under one square unit read in acres or hectares, and
 * larger ones carry both (a PLSS section is one square mile, 640 acres).
 */
export const formatMeasuredArea = (squareMiles: number, metric: boolean): string => {
  const whole = (value: number) => Math.round(value).toLocaleString("en-US");
  if (metric) {
    const squareKilometres = squareMiles * 2.58999;
    const hectares = squareKilometres * 100;
    return squareKilometres < 1 ? `${hectares < 10 ? hectares.toFixed(1) : whole(hectares)} ha approximate` : `${squareKilometres.toFixed(1)} km² (${whole(hectares)} ha) approximate`;
  }
  const acres = squareMiles * 640;
  return squareMiles < 1 ? `${acres < 10 ? acres.toFixed(1) : whole(acres)} acres approximate` : `${squareMiles.toFixed(1)} sq mi (${whole(acres)} acres) approximate`;
};
