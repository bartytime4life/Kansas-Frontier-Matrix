import { createShellFrame } from "./shell/shell-frame.js";

const appRoot = document.getElementById("app");

if (!appRoot) {
  throw new Error("Expected #app root to exist.");
}

appRoot.appendChild(createShellFrame());
