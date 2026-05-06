import type { CSSProperties } from "react";

export type TrustBadge =
  | "DERIVED_SUPPORTED"
  | "OBSERVED_SUPPORTED"
  | "EVIDENCE_RESOLVED"
  | "PUBLIC_GENERALIZED"
  | "PUBLIC_SAFE"
  | "RESTRICTED_SOURCE"
  | "REDACTION_RECEIPT_PRESENT"
  | "CATALOG_CLOSED"
  | "RELEASED";

const badgeLabel: Record<TrustBadge, string> = {
  DERIVED_SUPPORTED: "Derived-supported",
  OBSERVED_SUPPORTED: "Observed-supported",
  EVIDENCE_RESOLVED: "Evidence resolved",
  PUBLIC_GENERALIZED: "Public generalized",
  PUBLIC_SAFE: "Public safe",
  RESTRICTED_SOURCE: "Restricted source",
  REDACTION_RECEIPT_PRESENT: "Redaction receipt",
  CATALOG_CLOSED: "Catalog closed",
  RELEASED: "Released"
};

const badgeStyle: Record<TrustBadge, CSSProperties> = {
  DERIVED_SUPPORTED: { background: "#e6f4ea", color: "#1e6b38" },
  OBSERVED_SUPPORTED: { background: "#e7f3ff", color: "#0f4c81" },
  EVIDENCE_RESOLVED: { background: "#f3e8fd", color: "#6c2eb9" },
  PUBLIC_GENERALIZED: { background: "#e8f0fe", color: "#1947a6" },
  PUBLIC_SAFE: { background: "#edf7ed", color: "#256029" },
  RESTRICTED_SOURCE: { background: "#fff4e5", color: "#8b5d00" },
  REDACTION_RECEIPT_PRESENT: { background: "#fde8e8", color: "#9f1c1c" },
  CATALOG_CLOSED: { background: "#f5f5f5", color: "#4a4a4a" },
  RELEASED: { background: "#e6fffa", color: "#00695c" }
};

export function TrustBadges({ badges }: { badges: TrustBadge[] }) {
  return (
    <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
      {badges.map((badge) => (
        <span
          key={badge}
          style={{
            ...badgeStyle[badge],
            borderRadius: 999,
            fontSize: 12,
            fontWeight: 600,
            padding: "4px 10px"
          }}
        >
          {badgeLabel[badge]}
        </span>
      ))}
    </div>
  );
}
