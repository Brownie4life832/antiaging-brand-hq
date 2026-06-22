/* Research Explorer — vanilla JS, no external deps. Consumes window.DATA from data.js. */
(function () {
  const D = window.DATA || {};
  const $ = (id) => document.getElementById(id);
  const GRADE_ORDER = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"];
  const esc = (s) => (s == null ? "" : String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])));

  /* ---------- header meta ---------- */
  const c = D.counts || {};
  $("meta-counts").textContent = [
    `${c.ingredients || 0} ingredients`,
    c.devices ? `${c.devices} devices/procedures` : null,
    c.competitors ? `${c.competitors} competitors` : null,
    c.market ? `${c.market} market/trend reports` : null
  ].filter(Boolean).join(" · ");
  $("meta-date").textContent = D.generatedAt || "—";

  /* ---------- dashboard ---------- */
  function buildDashboard() {
    const dist = D.gradeDist || {};
    const max = Math.max(1, ...GRADE_ORDER.map(g => dist[g] || 0));
    const bucketClass = (g) => (g[0] === "A" || g[0] === "B") ? "s" : g[0] === "C" ? "m" : "w";
    const bars = GRADE_ORDER.filter(g => dist[g]).map(g =>
      `<div class="bar ${bucketClass(g)}" style="height:${Math.round((dist[g] / max) * 100)}%" title="${g}: ${dist[g]}"><span>${g}</span></div>`
    ).join("");
    $("dashboard").innerHTML = `
      <div class="stat"><div class="n">${c.ingredients || 0}</div><div class="l">ingredient dossiers</div></div>
      <div class="stat"><div class="n" style="color:var(--strong)">${c.viableStrong || 0}</div><div class="l">cosmetic-viable, A/B evidence</div></div>
      <div class="stat"><div class="n" style="color:var(--weak)">${c.weak || 0}</div><div class="l">D/F — hype watch</div></div>
      <div class="stat span2 bars-wrap"><div class="l">evidence-grade distribution (topical anti-aging)</div><div class="bars">${bars}</div></div>
      <div class="stat"><div class="n">${(c.strong || 0)}/${(c.moderate || 0)}/${(c.weak || 0)}</div><div class="l">strong / weak / hype</div></div>`;
  }

  /* ---------- ingredients explorer ---------- */
  const state = { q: "", bucket: "all", cls: "", verdict: "", sort: "grade" };
  const ings = D.ingredients || [];

  function classOptions() {
    const set = [...new Set(ings.map(i => i.cls).filter(x => x && x !== "—"))].sort();
    $("ing-class").insertAdjacentHTML("beforeend", set.map(x => `<option value="${esc(x)}">${esc(x)}</option>`).join(""));
  }

  function gradeBadge(i) { return `<span class="badge ${i.gradeBucket}">${esc(i.grade)}</span>`; }
  function verdictBadge(i) {
    const e = i.verdict && i.verdict !== "—" ? i.verdict : "";
    return `<span class="vbadge" title="${esc(i.verdictLabel)}">${e || "—"} ${i.verdictLabel && i.verdictLabel !== "—" ? esc(i.verdictLabel) : ""}</span>`;
  }

  function renderIngredients() {
    let rows = ings.filter(i => {
      if (state.bucket !== "all" && i.gradeBucket !== state.bucket) return false;
      if (state.cls && i.cls !== state.cls) return false;
      if (state.verdict && i.verdictLabel !== state.verdict) return false;
      if (state.q) {
        const q = state.q.toLowerCase();
        if (!(i.name.toLowerCase().includes(q) || (i.cls || "").toLowerCase().includes(q))) return false;
      }
      return true;
    });
    if (state.sort === "name") rows.sort((a, b) => a.name.localeCompare(b.name));
    else if (state.sort === "class") rows.sort((a, b) => (a.cls || "").localeCompare(b.cls || "") || a.gradeRank - b.gradeRank);
    else rows.sort((a, b) => a.gradeRank - b.gradeRank || a.name.localeCompare(b.name));

    $("ing-body").innerHTML = rows.map(i => `
      <tr data-doc="${esc(i.slug)}">
        <td><span class="iname">${esc(i.name)}</span></td>
        <td class="cell-sm">${esc(i.cls)}</td>
        <td class="cell-sm">${esc(i.relevance)}</td>
        <td class="cell-sm">${esc(i.tier)}</td>
        <td class="cell-sm">${esc(i.viabilityShort)}</td>
        <td>${gradeBadge(i)}</td>
        <td>${verdictBadge(i)}</td>
      </tr>`).join("");
    $("ing-count").textContent = `${rows.length} of ${ings.length}`;
  }

  /* ---------- devices & procedures explorer ---------- */
  const devs = D.devices || [];
  const dstate = { q: "", call: "all", sort: "grade" };

  function renderDevices() {
    // Brand-call is genuinely multi-valued (a row can be "🤝 aftercare … ❌ build"),
    // so filter by presence of each recommendation rather than one exclusive bucket.
    let rows = devs.filter(d => {
      const call = d.call || "";
      if (dstate.call === "adjacency" && !(call.includes("✅") || call.includes("🤝"))) return false;
      if (dstate.call === "educate" && !call.includes("📚")) return false;
      if (dstate.call === "avoid" && !call.includes("❌")) return false;
      if (dstate.q) {
        const q = dstate.q.toLowerCase();
        if (!(d.name.toLowerCase().includes(q) || (d.category || "").toLowerCase().includes(q) || (d.note || "").toLowerCase().includes(q))) return false;
      }
      return true;
    });
    if (dstate.sort === "name") rows.sort((a, b) => a.name.localeCompare(b.name));
    else rows.sort((a, b) => a.gradeRank - b.gradeRank || a.name.localeCompare(b.name));

    $("dev-body").innerHTML = rows.map(d => `
      <tr data-doc="${esc(d.slug)}">
        <td><span class="iname">${esc(d.name)}</span>${d.note ? `<div class="cell-note">${esc(d.note)}</div>` : ""}</td>
        <td class="cell-sm">${esc(d.category)}</td>
        <td><span class="badge ${d.gradeBucket}">${esc(d.clinicGrade)}</span></td>
        <td class="cell-sm">${esc(d.homeGrade)}</td>
        <td class="cell-sm">${esc(d.reg)}</td>
        <td class="cell-sm">${esc(d.call)}</td>
      </tr>`).join("");
    $("dev-count").textContent = `${rows.length} of ${devs.length}`;
  }

  /* ---------- generic card lists ---------- */
  function renderList(items, listId, countId, searchId) {
    const box = $(listId), cnt = $(countId);
    function draw(q) {
      const f = !q ? items : items.filter(d => d.name.toLowerCase().includes(q.toLowerCase()));
      box.innerHTML = f.map(d => `<div class="card" data-doc="${esc(d.slug)}"><h3>${esc(d.name)}</h3><p>${esc(d.slug)}.md</p></div>`).join("") || `<p class="muted">No matches.</p>`;
      cnt.textContent = `${f.length} of ${items.length}`;
    }
    if (searchId) $(searchId).addEventListener("input", e => draw(e.target.value));
    draw("");
  }

  /* ---------- reader (lazy-loaded fragments) ---------- */
  const DOCS = D.docsIndex || {};
  const cache = {};
  async function openDoc(slug) {
    const meta = DOCS[slug];
    if (!meta) return;
    $("reader-title").textContent = meta.name;
    $("reader-body").innerHTML = '<p class="muted">Loading…</p>';
    $("reader").classList.remove("hidden");
    document.body.style.overflow = "hidden";
    $("reader").scrollTop = 0;
    try {
      if (!cache[slug]) {
        const r = await fetch(meta.file);
        if (!r.ok) throw new Error(r.status);
        cache[slug] = await r.text();
      }
      $("reader-body").innerHTML = cache[slug];
      $("reader-body").scrollTop = 0;
    } catch (e) {
      $("reader-body").innerHTML = '<h1>' + esc(meta.name) + '</h1><p class="muted">Couldn\'t load this dossier. If you opened the page by double-clicking the file, the browser blocks loading local files — serve the folder instead: run <code>python -m http.server</code> inside <code>site/</code> and open the printed URL, or host it (e.g. GitHub Pages).</p>';
    }
  }
  function closeReader() { $("reader").classList.add("hidden"); document.body.style.overflow = ""; }

  /* delegated clicks: open docs from rows, cards, and intra-doc links */
  document.addEventListener("click", (e) => {
    const host = e.target.closest("[data-doc]");
    if (host) { const s = host.getAttribute("data-doc"); if (DOCS[s]) { e.preventDefault(); openDoc(s); } return; }
  });
  $("reader-close").addEventListener("click", closeReader);
  $("reader").addEventListener("click", (e) => { if (e.target.id === "reader") closeReader(); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeReader(); });

  /* ---------- tabs ---------- */
  $("tabs").addEventListener("click", (e) => {
    const b = e.target.closest("button[data-tab]"); if (!b) return;
    [...$("tabs").children].forEach(x => x.classList.toggle("active", x === b));
    ["ingredients", "devices", "competitors", "market", "strategy", "about"].forEach(t =>
      $("panel-" + t).classList.toggle("hidden", t !== b.dataset.tab));
    window.scrollTo(0, 0);
  });

  /* ---------- wire ingredient controls ---------- */
  $("ing-search").addEventListener("input", e => { state.q = e.target.value; renderIngredients(); });
  $("ing-class").addEventListener("change", e => { state.cls = e.target.value; renderIngredients(); });
  $("ing-verdict").addEventListener("change", e => { state.verdict = e.target.value; renderIngredients(); });
  $("ing-sort").addEventListener("change", e => { state.sort = e.target.value; renderIngredients(); });
  $("bucket-chips").addEventListener("click", e => {
    const b = e.target.closest("button[data-bucket]"); if (!b) return;
    state.bucket = b.dataset.bucket;
    [...$("bucket-chips").children].forEach(x => x.classList.toggle("active", x === b));
    renderIngredients();
  });

  /* ---------- wire device controls ---------- */
  if ($("dev-search")) {
    $("dev-search").addEventListener("input", e => { dstate.q = e.target.value; renderDevices(); });
    $("dev-sort").addEventListener("change", e => { dstate.sort = e.target.value; renderDevices(); });
    $("dev-call-chips").addEventListener("click", e => {
      const b = e.target.closest("button[data-call]"); if (!b) return;
      dstate.call = b.dataset.call;
      [...$("dev-call-chips").children].forEach(x => x.classList.toggle("active", x === b));
      renderDevices();
    });
  }

  /* ---------- about ---------- */
  $("about-body").innerHTML = `
    <h1>About this explorer</h1>
    <p>An offline, interactive view of the brand's research base. Everything is generated from the Markdown in <code>research/</code> by <code>site/build.py</code> — re-run it to refresh after the research changes.</p>
    <h2>What's inside</h2>
    <ul>
      <li><strong>Ingredients</strong> — ${c.ingredients || 0} exhaustive, cited dossiers, each graded by an adversarial pass.</li>
      <li><strong>Devices &amp; Procedures</strong> — ${c.devices || 0} dossiers on energy devices, microneedling, lasers, peels, injectables, exosomes/stem cells &amp; IV — graded clinic vs at-home, with a brand product-adjacency call.</li>
      <li><strong>Competitors</strong> — ${c.competitors || 0} brand teardowns.</li>
      <li><strong>Market &amp; Trends</strong> — ${c.market || 0} reports.</li>
      <li><strong>Strategy</strong> — the competitive landscape, white-space map, evidence matrix, landmark papers, and the product recommendation.</li>
    </ul>
    <h2>How to read the grades</h2>
    <p>Grades reflect the <strong>topical, leave-on, anti-aging</strong> claim specifically (not off-target uses like acne). <strong>A/B</strong> = solid human-topical evidence · <strong>C</strong> = weak/indirect/mechanism-only · <strong>D/F</strong> = unproven topically (the hype zone). Verdicts: ✅ shortlist · ⚠️ conditional · ❌ skip.</p>
    <h2>Caveats</h2>
    <p>The brand's <strong>name, story, positioning, and visual identity are all still open</strong> — this tool's neutral styling is deliberate, not a brand look. Citations are best-effort from the research run; verify any specific figure before public use. Generated ${D.generatedAt || "—"}.</p>`;

  /* ---------- init ---------- */
  // hide tabs whose section is empty (e.g. the public research-only build)
  ["devices", "competitors", "market", "strategy"].forEach(t => {
    if (!((D[t] || []).length)) { const b = document.querySelector('#tabs button[data-tab="' + t + '"]'); if (b) b.remove(); }
  });
  buildDashboard();
  classOptions();
  renderIngredients();
  renderDevices();
  renderList(D.competitors || [], "competitors-list", "competitors-count", "competitors-search");
  renderList(D.market || [], "market-list", "market-count", "market-search");
  renderList(D.strategy || [], "strategy-list", "strategy-count", "strategy-search");
})();
