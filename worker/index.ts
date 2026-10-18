/** Cloudflare Worker entry point for the vinext-starter template. */
import { handleImageOptimization, DEFAULT_DEVICE_SIZES, DEFAULT_IMAGE_SIZES } from "vinext/server/image-optimization";
import handler from "vinext/server/app-router-entry";
import { IS_PUBLIC_COPY } from "../app/public-profile";
import { publicApplicationOriginAllowed, publicRouteDecision, publicUnavailable } from "../app/public-route-policy";

import { SITE_IDENTITY } from "../app/site-identity";

interface Env {
  ASSETS: { fetch(request: Request): Promise<Response> };
  DB: unknown;
  IMAGES: {
    input(stream: ReadableStream): {
      transform(options: Record<string, unknown>): {
        output(options: { format: string; quality: number }): Promise<{ response(): Response }>;
      };
    };
  };
}

interface ExecutionContext {
  waitUntil(promise: Promise<unknown>): void;
  passThroughOnException(): void;
}

// Image security config. SVG sources with .svg extension auto-skip the
// optimization endpoint on the client side (served directly, no proxy).
// To route SVGs through the optimizer (with security headers), set
// dangerouslyAllowSVG: true in next.config.js and uncomment below:
// const imageConfig: ImageConfig = { dangerouslyAllowSVG: true };

const worker = {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);
    if (IS_PUBLIC_COPY) {
      const managedPreview = import.meta.env.DEV && url.origin === "http://terminal.local:4173";
      if (!managedPreview && !publicApplicationOriginAllowed(request.url, SITE_IDENTITY.hostedUrl, SITE_IDENTITY.canonicalUrl)) return publicUnavailable("PUBLIC_APPLICATION_ORIGIN_UNAVAILABLE", 403);
      const route = publicRouteDecision(request.url, request.method);
      if (!route.allowed) return publicUnavailable(route.reason);
      if (url.hostname === "www.kansasfrontiermatrix.com") {
        url.hostname = "kansasfrontiermatrix.com"; url.protocol = "https:";
        return Response.redirect(url.toString(), 308);
      }
    }

    if (url.pathname === "/_vinext/image") {
      const allowedWidths = [...DEFAULT_DEVICE_SIZES, ...DEFAULT_IMAGE_SIZES];
      return handleImageOptimization(request, {
        fetchAsset: (path) => env.ASSETS.fetch(new Request(new URL(path, request.url))),
        transformImage: async (body, { width, format, quality }) => {
          const result = await env.IMAGES.input(body).transform(width > 0 ? { width } : {}).output({ format, quality });
          return result.response();
        },
      }, allowedWidths);
    }

    return handler.fetch(request, env, ctx);
  },
};

export default worker;
