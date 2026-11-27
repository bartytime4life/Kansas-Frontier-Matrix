"use client";

import { useEffect, useMemo, useRef, useState, useSyncExternalStore } from "react";
import Link from "next/link";
import { INQUIRY_CONTACT, INQUIRY_LIMITS, SERVICE_OPTIONS, inquiryDraft, readInquirySelection, serviceInquiryPath } from "../science-handoff.mjs";
import styles from "./services.module.css";

const LOCATION_EVENT = "kfm-science-inquiry-selection";
function subscribeLocation(callback) {
  window.addEventListener("popstate", callback);
  window.addEventListener(LOCATION_EVENT, callback);
  return () => { window.removeEventListener("popstate", callback); window.removeEventListener(LOCATION_EVENT, callback); };
}
const clientSearch = () => window.location.search;
const serverSearch = () => "";

export function ServiceScopeLink({ service, children }) {
  const search = useSyncExternalStore(subscribeLocation, clientSearch, serverSearch);
  const { context } = readInquirySelection(search);
  const href = `${serviceInquiryPath(context || "", service)}#project-brief`;
  function chooseScope(event) {
    if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.currentTarget?.target === "_blank") return;
    event.preventDefault();
    if (`${window.location.pathname}${window.location.search}${window.location.hash}` !== href) window.history.pushState(null, "", href);
    window.dispatchEvent(new Event(LOCATION_EVENT));
    const builder = document.getElementById("project-brief");
    builder?.scrollIntoView({ block: "start", behavior: "auto" });
    builder?.focus({ preventScroll: true });
  }
  return <Link href={href} onClick={chooseScope}>{children}</Link>;
}

function downloadBrief(draft) {
  const url = URL.createObjectURL(new Blob([`${draft.text}\n`], { type: "text/plain;charset=utf-8" }));
  const link = document.createElement("a");
  link.href = url;
  link.download = draft.filename;
  try { document.body.appendChild(link); link.click(); }
  finally { link.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000); }
}

export default function InquiryBuilder() {
  const search = useSyncExternalStore(subscribeLocation, clientSearch, serverSearch);
  const { service, context } = readInquirySelection(search);
  const [question, setQuestion] = useState("");
  const [area, setArea] = useState("");
  const [timing, setTiming] = useState("");
  const [feedback, setFeedback] = useState(null);
  const actionId = useRef(0);
  const key = JSON.stringify([service, context, question, area, timing]);
  useEffect(() => subscribeLocation(() => { actionId.current += 1; setFeedback(null); }), []);
  const result = useMemo(() => {
    try { return { draft: inquiryDraft({ service, question, area, timing, context: context || "" }), error: "" }; }
    catch (error) { return { draft: null, error: error instanceof Error ? error.message : "Check the project fields before preparing a brief." }; }
  }, [service, question, area, timing, context]);
  const { draft, error } = result;
  const selectedService = SERVICE_OPTIONS.find(option => option.id === service);
  const message = feedback?.key === key ? feedback.message : "";

  function editField(setter, value) {
    actionId.current += 1;
    setFeedback(null);
    setter(value);
  }
  function selectService(value) {
    actionId.current += 1;
    setFeedback(null);
    window.history.pushState(null, "", `${serviceInquiryPath(context || "", value)}#project-brief`);
    window.dispatchEvent(new Event(LOCATION_EVENT));
  }
  async function copyBrief() {
    if (!draft) return;
    const id = ++actionId.current;
    try {
      await navigator.clipboard.writeText(draft.text);
      if (id === actionId.current) setFeedback({ key, message: "Project brief copied. Nothing has been submitted." });
    } catch {
      if (id === actionId.current) setFeedback({ key, message: "Copy is unavailable. Select the read-only project brief below and copy it, or download the text file. Nothing has been submitted." });
    }
  }
  function saveBrief() {
    if (!draft) return;
    actionId.current += 1;
    try { downloadBrief(draft); setFeedback({ key, message: "Text download prepared. Nothing has been submitted." }); }
    catch { setFeedback({ key, message: "This browser could not prepare the download. Select and copy the project brief below." }); }
  }
  function openEmailDraft() {
    actionId.current += 1;
    setFeedback({ key, message: "Review the draft in your email app and send it there. Nothing has been submitted by this page." });
  }

  return <div className={styles.inquiry}>
    <fieldset className={styles.fields}><legend>Project brief details</legend>
      <label className={styles.field}>What would help?<select name="service" value={service} onChange={event => selectService(event.target.value)}>{SERVICE_OPTIONS.map(option => <option key={option.id} value={option.id}>{option.label}</option>)}</select><small>{selectedService.deliverable}</small></label>
      <label className={styles.field}>Your question or intended use<textarea name="question" value={question} maxLength={INQUIRY_LIMITS.question} rows={5} placeholder="For example: help our team explain how two Topeka years differed, with source-linked figures." onChange={event => editField(setQuestion, event.target.value)} /><small>{question.length}/{INQUIRY_LIMITS.question} characters · A question enables the email draft.</small></label>
      <label className={styles.field}>General area<input name="area" value={area} maxLength={INQUIRY_LIMITS.area} placeholder="For example: Shawnee County, Kansas" onChange={event => editField(setArea, event.target.value)} /><small>A town, county or broad area is enough. Omit private addresses and precise sensitive locations.</small></label>
      <label className={styles.field}>Desired timing<input name="timing" value={timing} maxLength={INQUIRY_LIMITS.timing} placeholder="For example: discuss this month" onChange={event => editField(setTiming, event.target.value)} /><small>Timing is a request; availability is discussed before work starts.</small></label>
      {context && <aside className={styles.context}><strong>Your starting analysis is attached</strong><code>{context}</code><Link href={context}>Open the analysis ↗</Link><p>Only this public tool selection is included. It does not establish matching geographic coverage or reviewed conclusions.</p></aside>}
      <p className={styles.privacy}>Your draft stays on this page until you choose to copy, save or email it. Nothing is submitted here. Keep private or sensitive records out of the brief. Opening an email draft includes the text in your own email app.</p>
    </fieldset>
    <section className={styles.preview} aria-labelledby="project-preview-heading"><span className={styles.eyebrow}>Your take-away / prepared on this device</span><h3 id="project-preview-heading">A clear starting point.</h3><p>Review, save or email this project brief. Scope, pricing and availability are agreed by email before any work begins.</p>
      {error && <p className={styles.status} role="alert">{error}</p>}
      <label className={styles.field}><span className={styles.eyebrow}>Read-only project brief</span><textarea className={styles.draft} aria-label="Read-only project brief" readOnly value={draft?.text || ""} onFocus={event => event.currentTarget.select()} /></label>
      <div className={styles.actions}><button type="button" disabled={!draft} onClick={copyBrief}>Copy brief <span aria-hidden="true">↗</span></button><button type="button" disabled={!draft} onClick={saveBrief}>Download .txt <span aria-hidden="true">↓</span></button>{draft?.canEmail ? <a href={draft.mailto} onClick={openEmailDraft}>Open email draft <span aria-hidden="true">↗</span></a> : <button type="button" disabled>Open email draft ↗</button>}</div>
      {message && <p className={styles.status} role="status">{message}</p>}
      <p className={styles.delivery}>Nothing is sent by this form. Sending is your action in your email app. If it does not open, copy the brief and email <a href={`mailto:${INQUIRY_CONTACT}`}>{INQUIRY_CONTACT}</a>.</p>
    </section>
  </div>;
}
