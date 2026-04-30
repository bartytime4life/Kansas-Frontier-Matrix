import { createShellFrame } from "../shell/shell-frame.js";

export function mountApp(root = document.getElementById("app")) {
  if (!root) {
    throw new Error("Expected #app root to exist.");
  }

  root.replaceChildren(createShellFrame());
  return root;
}
