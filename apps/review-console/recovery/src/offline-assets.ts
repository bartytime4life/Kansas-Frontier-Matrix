/** Build a finite cache list; performance entries alone can omit module assets. */
export function offlineAssetUrls(pageUrl: string, resources: string[], documentAssets: string[]): string[] {
  const page = new URL(pageUrl);
  const candidates = [page.href, ...documentAssets, new URL('/baseline-evidence.json', page).href, ...resources];
  const urls = new Set<string>();
  for (const candidate of candidates) {
    if (!candidate) continue;
    try {
      const url = new URL(candidate, page);
      if (!['http:', 'https:'].includes(url.protocol) || url.origin !== page.origin ||
          url.pathname.startsWith('/api/') || url.pathname.includes('/@vite') ||
          url.pathname.includes('__vite') || url.pathname.includes('hot-update')) continue;
      url.hash = '';
      urls.add(url.href);
    } catch { /* An unusable reference is not a cache request. */ }
  }
  return [...urls].slice(0, 180);
}
