"use client";

import { Component, useEffect, useRef, type ReactNode } from "react";

export const UI_ERROR_CODE = "KFM-UI-UNEXPECTED-ERROR";
const SAFE_CORRELATION_ID = /^[A-Za-z0-9_-]{1,128}$/;

export const correlationIdForError = (error: unknown): string => {
  // JavaScript can throw any value. Never invoke a digest getter during recovery.
  try {
    if (typeof error !== "object" || error === null) return "unavailable";
    const value: unknown = Object.getOwnPropertyDescriptor(error, "digest")?.value;
    const digest = typeof value === "string" ? value.trim() : "";
    return SAFE_CORRELATION_ID.test(digest) ? digest : "unavailable";
  } catch {
    return "unavailable";
  }
};

export const reportUiError = (error: unknown): void => {
  // Root callbacks replace React's default raw exception/component-stack logging.
  console.error("[KFM UI error boundary]", {
    code: UI_ERROR_CODE,
    correlationId: correlationIdForError(error),
  });
};

type RecoveryState = { failure: { digest: string } | null };

export class ExplorerErrorBoundary extends Component<{ children: ReactNode }, RecoveryState> {
  state: RecoveryState = { failure: null };

  static getDerivedStateFromError(error: unknown): RecoveryState {
    return { failure: { digest: correlationIdForError(error) } };
  }

  private reset = () => this.setState({ failure: null });

  render() {
    return this.state.failure
      ? <ErrorFallback error={this.state.failure} reset={this.reset} />
      : this.props.children;
  }
}

export default function ErrorFallback({
  error,
  reset,
}: {
  error: unknown;
  reset: () => void;
}) {
  const correlationId = correlationIdForError(error);
  const titleRef = useRef<HTMLHeadingElement>(null);

  useEffect(() => {
    titleRef.current?.focus();
  }, []);

  return (
    <main className="kfm-error-boundary" aria-labelledby="kfm-error-title">
      <section className="kfm-error-boundary__card" role="alert">
        <p className="kfm-error-boundary__eyebrow">Explorer safeguard</p>
        <h1 id="kfm-error-title" ref={titleRef} tabIndex={-1}>This workspace could not be loaded.</h1>
        <p>
          An unexpected error interrupted this view. Try again to reopen it.
          Saved browser-local workspaces remain available; unsaved changes may
          be lost. If the error continues, return to Explorer.
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
