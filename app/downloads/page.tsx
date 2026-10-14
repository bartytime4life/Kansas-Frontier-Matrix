import { redirect } from "next/navigation";

/** Existing bookmarks use hosted sources; no PC download service is contacted. */
export default function DownloadsPage() { redirect("/?layers=sources"); }
