import { parseAcquisitionTerrain } from "../../../acquisition-terrain";
import { acquisitionReceiptRoutes } from "../../../acquisition-receipt-server";

export const { GET, POST } = acquisitionReceiptRoutes("terrain", parseAcquisitionTerrain);
