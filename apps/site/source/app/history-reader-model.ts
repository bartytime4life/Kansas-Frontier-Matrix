export const OCR_BYTES = 757514;
export const OCR_SHA256 = "68e6c1c76bbd982c395f724318b9beca0894f7c9cd5b543a6c6cd296d0b8ed15";
export const OCR_PAGE_SIZE = 16;
export function historyParagraphs(text: string) { return text.split(/\n\s*\n/).map(text => text.trim()).filter(Boolean).map((text, index) => ({ text, number: index + 1 })); }
export function searchHistory(rows: ReturnType<typeof historyParagraphs>, query: string) {
  const words = query.trim().toLowerCase().split(/\s+/).filter(Boolean);
  return rows.filter(row => words.every(word => row.text.toLowerCase().includes(word)));
}
export async function readHistoryText(response: Response) {
  if (!response.ok || !response.body) throw new Error("The text could not be loaded.");
  const reader = response.body.getReader(), chunks: Uint8Array[] = []; let size = 0;
  try { while (true) { const { done, value } = await reader.read(); if (done) break; size += value.byteLength; if (size > OCR_BYTES) throw new Error("The text exceeded its verified size."); chunks.push(value); } }
  finally { await reader.cancel(); }
  if (size !== OCR_BYTES) throw new Error("The text is incomplete.");
  const bytes = new Uint8Array(size); let offset = 0; for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
  const digest = [...new Uint8Array(await crypto.subtle.digest("SHA-256", bytes))].map(value => value.toString(16).padStart(2, "0")).join("");
  if (digest !== OCR_SHA256) throw new Error("The text did not match its source checksum.");
  return new TextDecoder("utf-8", { fatal: true }).decode(bytes);
}
