export function nextFocusableIndex(current, count) {
  if (count <= 0) return -1;
  return (current + 1) % count;
}
