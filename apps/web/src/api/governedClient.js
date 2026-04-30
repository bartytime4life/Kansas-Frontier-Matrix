const JSON_HEADERS = { "content-type": "application/json" };

export function createGovernedApiClient({ baseUrl = "/api" } = {}) {
  async function request(path, init = {}) {
    const response = await fetch(`${baseUrl}${path}`, {
      ...init,
      headers: { ...JSON_HEADERS, ...(init.headers ?? {}) }
    });

    if (!response.ok) {
      throw new Error(`Governed API request failed: ${response.status} ${response.statusText}`);
    }

    return response.json();
  }

  return {
    getLayerManifest: () => request("/ecology/layer-manifest"),
    getEvidenceDrawerPayload: (claimId) => request(`/ecology/evidence/${encodeURIComponent(claimId)}`),
    getFocusOutcome: (body) =>
      request("/ecology/focus", {
        method: "POST",
        body: JSON.stringify(body)
      })
  };
}
