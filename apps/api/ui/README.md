# apps/api/ui

Map Explorer + Timeline + Stories + Focus Mode UI scaffold (policy-aware).

## Layout

```text
apps/api/ui/
├─ README.md
├─ src/
│  ├─ components/
│  │  ├─ MapCanvas/
│  │  ├─ LayerPanel/
│  │  ├─ TimeControl/
│  │  ├─ EvidenceDrawer/
│  │  ├─ ReceiptViewer/
│  │  └─ TrustBadges/
│  ├─ pages/
│  │  ├─ Explorer.tsx
│  │  ├─ Story.tsx
│  │  └─ Focus.tsx
│  ├─ state/
│  │  ├─ view_state.ts
│  │  └─ query_params.ts
│  ├─ api/
│  │  ├─ client.ts
│  │  └─ contracts.ts
│  └─ styles/
└─ tests/
   └─ e2e/
```
