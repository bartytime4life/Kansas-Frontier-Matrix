"use strict";
(() => {
  const $ = (id) => document.getElementById(id);
  let token = "", cursor = null, request = 0, detailRequest = 0, currentRecords = [];
  async function api(path) {
    const response = await fetch(path, { headers: { Authorization: "Bearer " + token }, cache: "no-store" });
    const data = await response.json();
    if (!response.ok) throw new Error(data.reason_code === "OWNER_REVIEW_AUTH_REQUIRED" ? "The private review key was not accepted." : "The request could not be verified. Check the store or filters and retry.");
    return data;
  }
  function node(tag, text) { const e = document.createElement(tag); e.textContent = text; return e; }
  function message(text) { $("status").textContent = text; }
  async function load(after = null) {
    const serial = ++request;
    $("next").disabled = true;
    const params = new URLSearchParams();
    for (const key of ["source", "county", "kind", "start", "end"]) if ($(key).value.trim()) params.set(key, $(key).value.trim());
    if (after) params.set("after", after);
    try {
      const data = await api("/review/v1/records?" + params);
      if (serial !== request) return;
      currentRecords = data.records;
      $("rows").replaceChildren();
      data.records.forEach((record, index) => {
        const tr = node("tr", "");
        tr.append(node("td", record.event_date));
        const where = node("td", record.county ? record.county + " County" : "County unavailable");
        where.append(node("small", record.source_id)); tr.append(where);
        const kind = node("td", record.instrument_type.replaceAll("_", " ")); kind.append(node("small", "Unreleased · " + record.transaction_status)); tr.append(kind);
        const amount = node("td", record.amount ? record.amount.currency + " " + record.amount.value : "Not reported");
        if (record.amount) amount.append(node("small", record.amount.kind.replaceAll("_", " ")));
        tr.append(amount);
        const cell = node("td", ""); const button = node("button", "Inspect record"); button.type = "button"; button.setAttribute("aria-label", "Inspect " + record.instrument_type.replaceAll("_", " ") + " from " + record.event_date); button.addEventListener("click", () => detail(index)); cell.append(button); tr.append(cell); $("rows").append(tr);
      });
      cursor = data.next_cursor; $("next").hidden = !cursor; $("empty").hidden = data.records.length !== 0;
      $("detail").hidden = true; message(data.records.length + " record versions shown. Coverage is incomplete; release review is pending.");
    } catch (error) { if (serial === request) { $("rows").replaceChildren(); currentRecords = []; cursor = null; $("next").hidden = true; $("detail").hidden = true; message(error.message); } }
    finally { if (serial === request) $("next").disabled = false; }
  }
  async function detail(index) {
    const record = currentRecords[index], serial = request, detailSerial = ++detailRequest;
    try {
      const data = await api("/review/v1/evidence?digest=" + encodeURIComponent(record.record_digest));
      if (serial !== request || detailSerial !== detailRequest || !token) return;
      $("record-json").textContent = JSON.stringify(record, null, 2); $("bundles").replaceChildren();
      for (const bundle of data.bundles) {
        const link = node("a", "Open official source"); link.href = bundle.source_url; link.target = "_blank"; link.rel = "noreferrer";
        $("bundles").append(link, node("pre", JSON.stringify(bundle, null, 2)));
      }
      $("detail").hidden = false; $("detail").scrollIntoView({ behavior: "auto", block: "start" });
    } catch (error) { message(error.message); }
  }
  $("login").addEventListener("submit", async (event) => {
    event.preventDefault(); token = $("key").value.trim(); $("key").value = "";
    try { const data = await api("/review/v1/status"); $("count").textContent = data.counts.versions; $("captures").textContent = data.counts.captures - data.counts.withdrawn_captures; $("login").hidden = true; $("workspace").hidden = false; await load(); }
    catch (error) { token = ""; message(error.message); }
  });
  $("filters").addEventListener("submit", (event) => { event.preventDefault(); load(); });
  $("next").addEventListener("click", () => { if (cursor) load(cursor); });
  $("close").addEventListener("click", () => { ++detailRequest; $("detail").hidden = true; });
  $("signout").addEventListener("click", () => { token = ""; ++request; currentRecords = []; cursor = null; $("rows").replaceChildren(); $("record-json").textContent = ""; $("bundles").replaceChildren(); $("workspace").hidden = true; $("login").hidden = false; message("Signed out. Record data has been cleared from the workspace."); });
})();
