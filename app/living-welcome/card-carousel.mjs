// Geometry shared by touch scrolling, arrow buttons and keyboard focus.
export function centeredCard(cards, viewport) {
  const center = viewport.left + viewport.width / 2;
  return cards.reduce((best, card) => {
    const distance = Math.abs(card.left + card.width / 2 - center);
    return !best || distance < best.distance ? { id: card.id, distance } : best;
  }, null)?.id ?? null;
}
export function centeredScrollLeft(card, viewport, scrollLeft, maxScroll) {
  return Math.max(0, Math.min(maxScroll, scrollLeft + card.left + card.width / 2 - viewport.left - viewport.width / 2));
}
