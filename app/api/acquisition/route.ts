import { parseAcquisitionInventory } from "../../acquisition-inventory";
import { acquisitionReceiptRoutes } from "../../acquisition-receipt-server";

export const { GET, POST } = acquisitionReceiptRoutes("inventory", parseAcquisitionInventory);
