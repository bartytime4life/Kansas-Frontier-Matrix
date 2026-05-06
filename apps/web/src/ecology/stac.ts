export type StacCatalog = {
  stac_version: string;
  type: "Catalog";
  id: string;
  title: string;
  description: string;
  links: Array<{
    rel: string;
    href: string;
    type?: string;
    title?: string;
  }>;
  "kfm:domain"?: string;
  "kfm:collection_count"?: number;
};

export async function fetchEcologyStacCatalog(
  apiBase = "/api"
): Promise<StacCatalog> {
  const response = await fetch(`${apiBase}/ecology/catalog/stac`);

  if (!response.ok) {
    throw new Error(`Failed to load ecology STAC catalog: ${response.status}`);
  }

  return response.json();
}
