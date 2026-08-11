import invalidFixture from "../../../../fixtures/ui/promotion_gate_status_board_projection/invalid/extra-field.json";
import holdFixture from "../../../../fixtures/ui/promotion_gate_status_board_projection/valid/hold.json";
import { mountPromotionGateStatusBoard } from "../../src/features/promotion_gate_status_board";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Promotion gate status board fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
mountPromotionGateStatusBoard(root, requested === "invalid" ? invalidFixture : holdFixture);
