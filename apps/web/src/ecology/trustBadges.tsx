import type { CSSProperties } from "react";

export type TrustBadge =
  | "DERIVED_SUPPORTED"
  | "PUBLIC_GENERALIZED"
  | "EVIDENCE_RESOLVED"
  | "LIMITATIONS_PRESENT"
  | "REDACTION_APPLIED";

const badgeLabel: Record<TrustBadge, string> = {
  DERIVED_SUPPORTED: "Derived-supported",
  PUBLIC_GENERALIZED: "Public generalized",
  EVIDENCE_RESOLVED: "Evidence resolved",
  LIMITATIONS_PRESENT: "Limitations noted",
  REDACTION_APPLIED: "Redaction applied"
};

const badgeStyle: Record<TrustBadge, CSSProperties> = {
  DERIVED_SUPPORTED: { background: "#e6f4ea", color: "#1e6b38" },
  PUBLIC_GENERALIZED: { background: "#e8f0fe", color: "#1947a6" },
  EVIDENCE_RESOLVED: { background: "#f3e8fd", color: "#6c2eb9" },
  LIMITATIONS_PRESENT: { background: "#fff4e5", color: "#8b5d00" },
  REDACTION_APPLIED: { background: "#fde8e8", color: "#9f1c1c" }
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
