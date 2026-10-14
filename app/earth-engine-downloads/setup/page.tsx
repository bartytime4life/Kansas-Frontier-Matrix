import { redirect } from "next/navigation";
import LocalSetup from "./local-setup";
export const dynamic = "force-dynamic";
export default function Page() { if(process.env.KFM_LOCAL_COMPOSED === "1") return <LocalSetup />; redirect("/?layers=sources"); }
