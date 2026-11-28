// Admin-requested local review; model text is displayed as text, never HTML.
(() => {
  "use strict";
  if (WORKSPACE !== "working") return;
  let current = null, configured = false, maintenance = false, timer = null, previousState = null, previousDone = 0, refreshedAt = 0, serial = 0;
  const messages = {
    ADMIN_PAUSED:"Paused by the admin. Resume when ready; the schedule will respect this pause.",
    ADMIN_CANCELLED:"Stopped by the admin. Start a new batch when ready.",
    AI_DATA_MAINTENANCE:"Drive maintenance is running. Acceptance will resume when it finishes.",
    AI_BACKUP_RUNNING:"A backup is running. Qwen progress is saved; resume after the backup finishes.",
    AI_BACKUP_STATE_UNAVAILABLE:"Backup status is unavailable. Review is paused until the service status can be checked.",
    AI_NO_NEW_PENDING_FILES_MATCH_FILTERS:"No new pending files match. Change the filters or enable re-review of previous AI holds.",
    AI_RESUME_OR_CANCEL_CURRENT_BATCH:"Resume or stop the existing batch before starting another.",
    LOCAL_QWEN_UNAVAILABLE_OR_INVALID:"Local Qwen is unavailable. Check Ollama, then resume the batch.",
    LOCAL_QWEN_MODEL_PIN_CHANGED:"The installed Qwen model changed. The operator must verify its model pin before review can continue.",
    AI_WORKING_DATA_BUSY_RETRY:"Working Data is busy. Try again shortly.",
    AI_WORKING_DATA_BUSY_RESUME:"Working Data is busy. The AI draft is saved; resume when analysis finishes.",
    AI_DATA_VOLUME_UNAVAILABLE:"The data volume is unavailable. Reconnect it, then resume.",
    AI_PROMPT_CHANGED_START_NEW_BATCH:"The review rules changed. Stop this saved batch and start a new one.",
    AI_SOURCE_BATCH_FILE_CHANGED_OR_REVIEWED:"An original file changed or has already been reviewed. Use the filters to start a new pending-file selection.",
    INTERRUPTED_RESTART:"Progress was saved after an interruption. Resume to continue."
  };
  const explain = code => messages[code] || String(code || "").replaceAll("_"," ");
  const active = () => current && ["running","pausing","cancelling"].includes(current.state);
  function scope() {
    const disallowed = ($("f-status").value && $("f-status").value !== "review") || $("f-lane").value === "inbox";
    $("ai-start").disabled = !configured || maintenance || active() || current?.state === "paused" || !!disallowed;
    $("ai-scope").textContent = disallowed ? "Choose Any status or Needs review, and captured files, to run smart acceptance."
      : "Only pending files matching the current filters are queued. Qwen reviews metadata, bounded plain or gzip text and available Studio OCR; it does not validate every record.";
  }
  function render(data) {
    configured = data.enabled === true; maintenance = !!data.maintenance; current = data.job || null;
    $("smart-acceptance").hidden = false;
    $("ai-model").textContent = data.model ? `${data.model} · on this PC` : "Not connected";
    if (!configured) { $("ai-state").textContent = data.reason || "Local Qwen is not configured."; scope(); return; }
    const job = current, counts = job?.counts || {};
    const live = job?.currentStatuses || {}, resolvedLater=(live.reviewed||0)>(counts.accepted||0)||(live.ready||0)>0;
    const done = ["accepted","held","failed","stale"].reduce((n,k)=>n+(counts[k]||0),0);
    $("ai-progress").hidden = !job;
    $("ai-progress").max = job?.total || 1; $("ai-progress").value = done;
    $("ai-pause").hidden = !active(); $("ai-pause").disabled = job?.state !== "running";
    $("ai-resume").hidden = job?.state !== "paused";
    $("ai-resume").disabled = !!data.maintenance;
    $("ai-cancel").hidden = !job || !["running","paused","pausing"].includes(job.state);
    $("ai-rerun").hidden = !job || !["completed","cancelled"].includes(job.state) || (!!counts.accepted && !counts.held) || resolvedLater;
    $("ai-rerun").disabled = maintenance;
    $("ai-rerun").textContent = counts.held ? `Re-review ${counts.held} held files` : "Re-review same pending files";
    $("ai-state").textContent = !job ? "Ready. Enter your name, choose a batch size, and start a local review."
      : `${job.state.replaceAll("_"," ")} · ${done} / ${job.total} processed · ${counts.accepted||0} accepted locally · ${counts.held||0} held · ${counts.failed||0} failed · ${counts.stale||0} changed/skipped · requested by ${job.admin}${job.cached ? ` · ${job.cached} unchanged AI reviews skipped` : ""}${job.error ? `. ${explain(job.error)}` : ""}${["pausing","cancelling"].includes(job.state) ? ". Finishing the current file first." : ""}`;
    if (job && resolvedLater) $("ai-state").textContent += ` Qwen run outcomes above are historical. Current files: ${live.reviewed||0} reviewed locally · ${live.review||0} need review · ${live.blocked||0} blocked.`;
    if (data.maintenance) $("ai-state").textContent += data.maintenanceReason === "backup"
      ? " A backup is running; review progress is saved."
      : " Drive maintenance is running; acceptance will resume afterward.";
    if (data.resolution) $("ai-state").textContent += ` Local reference review: ${data.resolution.accepted} of ${data.resolution.selection} accepted; ${data.resolution.remaining} remaining.`;
    else if (data.preparation) $("ai-state").textContent += ` Prepared metadata: ${(data.preparation.prepared||0)+(data.preparation.cached||0)} packets saved locally. Preparation does not release files.`;
    const results = $("ai-results"); results.replaceChildren();
    if (job?.recent.length) {
      const list = el("ul",{class:"ai-results"});
      for (const item of job.recent) {
        const review = item.review;
        list.append(el("li",{},el("button",{type:"button",class:"link",text:review?.title || "File review",onclick:()=>openItem(item.id)}),
          el("span",{class:`chip ${item.state==='accepted'?'reviewed':'review'}`,text:item.state==='accepted'?'Accepted locally':item.state}),
          el("p",{text:review?.description ? review.description.slice(0,350)+(review.description.length>350?"…":"") : explain(item.error || review?.reason)}),
          review?.ai_reviewed ? el("small",{text:`AI reviewer: ${review.attribution.model} · requested by ${review.attribution.requested_by}`}) : null));
      }
      results.append(list);
    }
    scope();
  }
  async function poll() {
    clearTimeout(timer);
    const request = ++serial;
    try {
      const data = await api("/api/ai-review/status");
      if (request !== serial) return;
      const next = data.job?.state; render(data);
      const done = ["accepted","held","failed","stale"].reduce((n,k)=>n+(data.job?.counts?.[k]||0),0);
      if ((previousState && previousState !== next && ["completed","paused","cancelled"].includes(next)) || (done!==previousDone && Date.now()-refreshedAt>10000)) { await refresh(); refreshedAt=Date.now(); }
      previousState = next; previousDone=done;
    } catch(error) { $("ai-state").textContent = explain(error.message); }
    timer = setTimeout(poll,active()?2500:15000);
  }
  try { $("ai-admin").value = localStorage.getItem("kfm-ai-admin") || ""; } catch { /* Optional convenience. */ }
  $("filters").addEventListener("input",scope);
  $("ai-form").addEventListener("submit",async event=>{
    event.preventDefault(); ++serial; $("ai-start").disabled = true;
    const filters = {};
    for (const [key,value] of new URLSearchParams(query())) if (["domain","family","lane","text","bbox"].includes(key)) filters[key] = key === "bbox" ? value.split(",").map(Number) : value;
    const admin = $("ai-admin").value.trim();
    try {
      try { localStorage.setItem("kfm-ai-admin",admin); } catch { /* Optional. */ }
      render(await api("/api/ai-review/start",{admin,filters,limit:Number($("ai-limit").value),retryHeld:$("ai-retry").checked}));
      poll();
    } catch(error) { $("ai-state").textContent = explain(error.message); scope(); }
  });
  for (const action of ["pause","resume","cancel"]) $("ai-"+action).addEventListener("click",async()=>{
    try { ++serial; render(await api("/api/ai-review/"+action,{})); poll(); }
    catch(error) { $("ai-state").textContent = explain(error.message); }
  });
  $("ai-rerun").addEventListener("click",async()=>{
    if (!$("ai-admin").reportValidity() || !current) return;
    const sourceBatch=current.id, admin=$("ai-admin").value.trim();
    const held=current.counts.held||0;
    try {
      ++serial; $("ai-rerun").disabled=true;
      render(await api("/api/ai-review/start",{admin,filters:{},limit:held||current.total,retryHeld:true,sourceBatch,...(held?{sourceState:"held"}:{})}));
      poll();
    } catch(error) { $("ai-state").textContent=explain(error.message); }
    finally { $("ai-rerun").disabled=false; }
  });
  poll();
})();
