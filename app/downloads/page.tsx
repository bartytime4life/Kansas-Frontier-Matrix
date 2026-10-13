import type { Metadata } from "next";
import DownloadsWorkspace from "./workspace";
export const metadata: Metadata = { title: "Local library & downloads | Kansas Frontier Matrix", description: "Inspect locally stored KFM collections, background downloads and approved map periods." };
export default function DownloadsPage() { return <DownloadsWorkspace />; }
