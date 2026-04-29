import { useState } from "react";

type FocusResponse = {
  outcome: "ANSWER" | "ABSTAIN" | "DENY";
  answer?: string;
  evidence_refs?: string[];
  decision_refs?: string[];
  reasons?: string[];
  trust?: {
    derivation?: "derived" | "observed";
    precision?: "generalized" | "exact";
  };
};

export default function FocusPanel() {
  const [response, setResponse] = useState<FocusResponse | null>(null);
  const [loading, setLoading] = useState(false);

  async function runQuery() {
    setLoading(true);
    try {
      const res = await fetch("/ecology/focus", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          payload: {
            schema_version: "v1",
            object_type: "FocusModeRequest",
            request_id: "kfm://request/ecology/ui-demo",
            query: "What ecology claim can be answered here?",
            surface: "public"
          }
        })
      });

      setResponse(await res.json());
    } finally {
      setLoading(false);
    }
  }

  const derivation = response?.trust?.derivation ?? "derived";
  const precision = response?.trust?.precision === "exact" ? "generalized" : "generalized";

  return (
    <div style={{ padding: 12, width: 320, borderLeft: "1px solid #ddd" }}>
      <h2>Focus Panel</h2>
      <button onClick={runQuery} disabled={loading}>{loading ? "Running..." : "Run Focus Mode"}</button>

      {response && (
        <div>
          <h3>{response.outcome}</h3>
          {response.answer && <p>{response.answer}</p>}

          <p><strong>Derivation:</strong> {derivation === "observed" ? "Observed" : "Derived"}</p>
          <p><strong>Precision:</strong> {precision === "generalized" ? "Generalized" : "Generalized"} (Exact never shown)</p>

          <h4>Evidence refs</h4>
          <ul>{(response.evidence_refs ?? []).map((ref) => <li key={ref}>{ref}</li>)}</ul>

          <h4>Decision refs</h4>
          <ul>{(response.decision_refs ?? []).map((ref) => <li key={ref}>{ref}</li>)}</ul>

          <h4>Policy reasons</h4>
          <ul>{(response.reasons ?? []).map((reason) => <li key={reason}>{reason}</li>)}</ul>
        </div>
      )}
    </div>
  );
}
