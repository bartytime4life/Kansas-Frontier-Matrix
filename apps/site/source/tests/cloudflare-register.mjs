import { register } from "node:module";
// Public-route Node tests don't use persistence. Resolve Workers-only imports;
// the intake integration suite separately runs with real D1/R2 emulation.
register(new URL("./cloudflare-loader.mjs", import.meta.url));
