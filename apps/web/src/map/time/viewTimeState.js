export function buildViewTimeState({ eventTime, observedTime, releaseTime, selectedTime }) {
  return {
    eventTime: eventTime ?? null,
    observedTime: observedTime ?? null,
    releaseTime: releaseTime ?? null,
    selectedTime: selectedTime ?? releaseTime ?? observedTime ?? eventTime ?? null
  };
}
