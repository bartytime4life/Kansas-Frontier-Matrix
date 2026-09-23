import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import ExplorerPage from "./app/page";
import AboutPage from "./app/about/page";
import OperationalSpine from "./app/operational-spine";
import SiteRuntimeRepair from "./app/site-runtime-repair-client";
import FeedStartupPanel from "./app/feed-startup-panel";
import "./app/globals.css";
import "./app/transformation.css";
import "../../packages/ui/src/layer-library.css";
import "./app/site-layer-library.css";

const isAbout = window.location.pathname === "/about" || window.location.pathname === "/about/";
document.title = isAbout ? "About · Kansas Frontier Matrix Explorer" : "Kansas Frontier Matrix Explorer";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    {!isAbout && <OperationalSpine />}
    <SiteRuntimeRepair />
    {isAbout ? <AboutPage /> : <ExplorerPage />}
    {!isAbout && <FeedStartupPanel />}
  </StrictMode>,
);
