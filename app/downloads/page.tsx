import { redirect } from "next/navigation";
import DownloadsWorkspace from "./workspace";
export const dynamic = "force-dynamic";
export default function DownloadsPage() { if(process.env.KFM_LOCAL_COMPOSED === "1") return <DownloadsWorkspace />; redirect("/?layers=sources"); }
