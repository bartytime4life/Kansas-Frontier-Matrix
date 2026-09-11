"use client";

import { useEffect } from "react";

type BoundaryError = globalThis.Error & { digest?: string };

export const UI_ERROR_CODE = "KFM-UI-UNEXPECTED-ERROR";
const SAFE_CORRELATION_ID = /^[A-Za-z0-9_-]{1,128}$/;

export const correlationIdForError = (error: BoundaryError): string => {
  const digest = typeof error?.digest === "string" ? error.digest.trim() : "";
  return SAFE_CORRELATION_ID.test(digest) ? digest : "unavailable";
};

export default function ErrorBoundary({
  error,
  reset,
}: {
  error: BoundaryError;
  reset: () => void;
}) {
  const correlationId = correlationIdForError(error);

  useEffect(() => {
    // Keep diagnostics useful without exposing the exception, stack, or request data.
    console.error("[KFM UI error boundary]", {
      code: UI_ERROR_CODE,
      correlationId,
    });
  }, [correlationId]);

  return (
    <main className="kfm-error-boundary" aria-labelledby="kfm-error-title">
      <section className="kfm-error-boundary__card" role="alert">
        <p className="kfm-error-boundary__eyebrow">Explorer safeguard</p>
        <h1 id="kfm-error-title">This workspace could not be loaded.</h1>
        <p>
          The Explorer stopped this view before it could show an unsupported
          result. Try again, or return to the map and continue with any saved
          browser-local workspace.
        </p>
        <div className="kfm-error-boundary__actions">
          <button type="button" onClick={reset}>
            Try again
          </button>
          <a href="/">Return to Explorer</a>
        </div>
        <p className="kfm-error-boundary__support">
          Support code: <code>{UI_ERROR_CODE}</code>
          {correlationId !== "unavailable" ? (
            <>
              {" · correlation "}
              <code>{correlationId}</code>
            </>
          ) : null}
        </p>
      </section>
    </main>
  );
}
