"use client";
import { useSyncExternalStore } from "react";
import type { ComponentProps } from "react";
import HostedDownloads from "./earth-engine-downloads-hosted";
import LocalDownloads from "./earth-engine-downloads-local";
export { EarthEngineDownloadForm, parseDownloadStatus } from "./earth-engine-downloads-local";
const subscribe = () => () => {};
export default function EarthEngineDownloads(props: ComponentProps<typeof LocalDownloads>) {
 const local = useSyncExternalStore(subscribe, () => window.location.origin === "http://127.0.0.1:4173", () => false);
 return local ? <LocalDownloads {...props} /> : <HostedDownloads {...props} />;
}
