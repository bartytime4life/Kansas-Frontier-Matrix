// Private WORK-package browser. Store text is always rendered as text, never HTML.
(() => {
  "use strict";
  const KEY = "kfm-review-selection";
  let packages = [], selected = null, request = 0, imageUrl = null, controller = null;
  const current = () => packages.find((p) => p.id === $("review-package").value);

  function persist() {
    try { sessionStorage.setItem(KEY, JSON.stringify({ package: current()?.id, member: selected?.id,
      files: $("review-file-search").value, text: $("review-content-search").value })); } catch { /* Optional. */ }
  }
  function clearPreview() {
    request += 1;
    controller?.abort();
    if (imageUrl) URL.revokeObjectURL(imageUrl);
    imageUrl = null;
    $("review-preview").replaceChildren();
    $("review-state").textContent = "";
  }
  function renderMembers() {
    const collection = current();
    const search = $("review-file-search").value.toLocaleLowerCase();
    const members = (collection?.members || []).filter((m) => `${m.label} ${m.name}`.toLocaleLowerCase().includes(search));
    $("review-members").replaceChildren(...members.map((member) => el("li", {}, el("button", {
      type: "button", "aria-pressed": String(selected?.id === member.id),
      text: `${member.label} · ${bytes(member.bytes)}`, onclick: () => openMember(member),
    }))));
    $("review-count").textContent = `${members.length} of ${collection?.members.length || 0} files`;
    $("review-role").textContent = collection ? `${collection.sourceRole} Rights: ${collection.rights}.` : "";
  }
  async function openMember(member) {
    clearPreview();
    selected = member;
    const sequence = request;
    const collection = current();
    $("review-title").textContent = member.label;
    $("review-content-search").disabled = member.kind === "image";
    $("review-search-form").querySelector("button").disabled = member.kind === "image";
    $("review-state").textContent = "Checking file integrity…";
    renderMembers(); persist();
    try {
      const base = `/api/reviews/${collection.id}/${member.id}`;
      if (member.kind === "image") {
        controller = new AbortController();
        const response = await fetch(base, { cache: "no-store", credentials: "omit", redirect: "error",
          headers: { "X-KFM-Session": TOKEN }, signal: controller.signal });
        if (!response.ok || response.headers.get("Content-Type") !== "image/png") throw new Error("Image could not be verified.");
        const blob = await response.blob();
        if (sequence !== request) return;
        imageUrl = URL.createObjectURL(blob);
        $("review-preview").append(el("img", { src: imageUrl, alt: `${member.label}. Document pixels only; historical position is not verified.` }));
        $("review-state").textContent = "File digest verified. Document image only; no historical geometry or release is inferred.";
      } else {
        const text = $("review-content-search").value;
        const value = await api(base + (text ? `?text=${encodeURIComponent(text)}` : ""));
        if (sequence !== request) return;
        $("review-preview").append(el("pre", { text: value.text || "No matches." }));
        const count = value.matchedRows == null ? "" : ` ${value.matchedRows} matching rows; ${value.shownRows} selected for this preview.`;
        $("review-state").textContent = `File digest verified. Pending review.${count}${value.truncated ? " Preview limited; the complete file remains in the private store." : ""}`;
      }
    } catch (error) {
      if (sequence === request) $("review-state").textContent = `File held: ${error.message}`;
    }
  }
  $("review-package").addEventListener("change", () => {
    selected = null; clearPreview(); $("review-title").textContent = "Select a file";
    $("review-content-search").value = ""; renderMembers(); persist();
  });
  $("review-file-search").addEventListener("input", () => { renderMembers(); persist(); });
  $("review-search-form").addEventListener("submit", (event) => { event.preventDefault(); if (selected) openMember(selected); });
  async function load() {
    try {
      packages = (await api("/api/reviews")).packages;
      if (!packages.length) return;
      $("reviews").hidden = false;
      $("review-package").replaceChildren(...packages.map((p) => el("option", { value: p.id, text: p.title })));
      let saved;
      try { saved = JSON.parse(sessionStorage.getItem(KEY) || "null"); } catch { /* Invalid optional state. */ }
      if (saved && packages.some((p) => p.id === saved.package)) {
        $("review-package").value = saved.package;
        $("review-file-search").value = typeof saved.files === "string" ? saved.files.slice(0, 100) : "";
        $("review-content-search").value = typeof saved.text === "string" ? saved.text.slice(0, 100) : "";
        selected = current().members.find((m) => m.id === saved.member) || null;
      }
      renderMembers();
      if (selected) await openMember(selected);
    } catch (error) {
      if (TOKEN) { $("reviews").hidden = false; $("review-state").textContent = `Collection review held: ${error.message}`; }
    }
  }
  load();
})();
