import { serveAirflowTile } from "../../airflow-tiles";

export const dynamic = "force-dynamic";
export const GET = (request: Request) => serveAirflowTile(request);
