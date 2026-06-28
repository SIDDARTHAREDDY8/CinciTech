#!/usr/bin/env python3
"""Render data/jobs.json into docs/index.html — a real-looking, static job board.

Output lives in docs/ so GitHub Pages can serve it directly
(Settings → Pages → Deploy from branch → main → /docs). No backend, no build step:
the jobs are embedded as JSON and filtered/rendered client-side.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "jobs.json"
CONFIG = ROOT / "config" / "firms.yaml"
OUT = ROOT / "docs" / "index.html"

TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ohio Tech Jobs — Cincinnati &amp; statewide software, data &amp; ML roles</title>
<meta name="description" content="A free, auto-updating board of software, data, ML and cloud jobs across Ohio and Cincinnati — from local employers and staffing firms, refreshed every 3 hours.">
<style>
  :root{
    --bg:#f5f6f8; --card:#fff; --ink:#0f172a; --muted:#64748b; --line:#e6e8ec;
    --brand:#0a7d3f; --brand-2:#0d9b57; --accent:#1d4ed8; --new:#0a7d3f; --chip:#eef2f7;
  }
  *{box-sizing:border-box}
  html,body{margin:0}
  body{font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       background:var(--bg); color:var(--ink); -webkit-font-smoothing:antialiased}
  a{color:inherit}

  /* ---------- hero ---------- */
  .hero{background:linear-gradient(135deg,#08331c 0%,#0a7d3f 55%,#0d9b57 100%); color:#fff; padding:34px 20px 30px}
  .hero-in{max-width:1000px; margin:0 auto}
  .badge{display:inline-block; background:rgba(255,255,255,.16); border:1px solid rgba(255,255,255,.25);
         font-size:12px; font-weight:600; letter-spacing:.3px; padding:4px 11px; border-radius:999px; margin-bottom:14px}
  h1{margin:0 0 8px; font-size:30px; line-height:1.15; letter-spacing:-.6px; font-weight:800}
  h1 .accent{color:#d7ffe9}
  .tag{margin:0; max-width:640px; font-size:15.5px; color:#e7fff1; opacity:.95}
  .stats{display:flex; gap:26px; flex-wrap:wrap; margin-top:20px}
  .stat .n{font-size:24px; font-weight:800; line-height:1}
  .stat .l{font-size:12px; text-transform:uppercase; letter-spacing:.6px; opacity:.85; margin-top:4px}

  /* ---------- controls ---------- */
  .bar{position:sticky; top:0; z-index:20; background:rgba(255,255,255,.92); backdrop-filter:blur(8px);
       border-bottom:1px solid var(--line); padding:12px 20px}
  .bar-in{max-width:1000px; margin:0 auto; display:flex; gap:10px; flex-wrap:wrap; align-items:center}
  .search{position:relative; flex:1; min-width:220px}
  .search svg{position:absolute; left:12px; top:50%; transform:translateY(-50%); opacity:.5}
  input[type=search]{width:100%; padding:11px 12px 11px 38px; font-size:14px; border:1px solid var(--line);
       border-radius:10px; background:#fff; color:var(--ink)}
  select{padding:11px 12px; font-size:14px; border:1px solid var(--line); border-radius:10px; background:#fff; color:var(--ink); cursor:pointer}
  input:focus,select:focus{outline:2px solid var(--brand); outline-offset:0; border-color:var(--brand)}
  .toggle{display:inline-flex; align-items:center; gap:7px; font-size:13.5px; color:var(--muted);
          border:1px solid var(--line); border-radius:10px; padding:10px 12px; cursor:pointer; user-select:none; white-space:nowrap; background:#fff}
  .toggle input{accent-color:var(--brand)}

  /* ---------- list ---------- */
  .wrap{max-width:1000px; margin:0 auto; padding:18px 20px 80px}
  .count{font-size:13px; color:var(--muted); margin:4px 2px 14px}
  .count b{color:var(--ink)}
  .card{display:flex; gap:14px; align-items:flex-start; background:var(--card); border:1px solid var(--line);
        border-radius:14px; padding:16px 16px; margin-bottom:10px; transition:box-shadow .15s, transform .15s, border-color .15s}
  .card:hover{box-shadow:0 8px 26px rgba(15,23,42,.08); transform:translateY(-1px); border-color:#d4d8df}
  .logo{flex:none; width:46px; height:46px; border-radius:11px; display:grid; place-items:center;
        font-weight:800; font-size:17px; color:#fff; letter-spacing:-.5px}
  .body{flex:1; min-width:0}
  .ttl{font-size:16px; font-weight:700; letter-spacing:-.2px; margin:0 0 3px}
  .co{font-size:13.5px; color:var(--muted); font-weight:600}
  .metarow{display:flex; gap:8px; flex-wrap:wrap; margin-top:9px}
  .chip{display:inline-flex; align-items:center; gap:5px; font-size:12px; color:#334155; background:var(--chip);
        border-radius:999px; padding:4px 10px; white-space:nowrap}
  .chip.kind-emp{background:#e7f0ff; color:#1e40af}
  .chip.kind-staff{background:#f1f0fb; color:#6d28d9}
  .new{background:var(--new); color:#fff; font-weight:700; letter-spacing:.4px}
  .right{flex:none; display:flex; flex-direction:column; align-items:flex-end; gap:10px}
  .posted{font-size:12px; color:var(--muted); white-space:nowrap; font-variant-numeric:tabular-nums}
  .apply{display:inline-block; background:var(--brand); color:#fff; text-decoration:none; font-weight:700;
         font-size:13px; padding:9px 16px; border-radius:9px; white-space:nowrap; transition:background .15s}
  .apply:hover{background:#08612f}
  .empty{text-align:center; color:var(--muted); padding:60px 20px}
  .empty .big{font-size:17px; color:var(--ink); font-weight:600; margin-bottom:6px}

  footer{border-top:1px solid var(--line); background:#fff}
  .foot{max-width:1000px; margin:0 auto; padding:26px 20px 40px; color:var(--muted); font-size:13.5px}
  .foot b{color:var(--ink)}
  .foot a{color:var(--brand); text-decoration:none; font-weight:600}

  @media (max-width:600px){
    h1{font-size:24px}
    .card{padding:14px 13px; gap:11px}
    .logo{width:40px; height:40px; font-size:15px}
    .right{flex-direction:row; align-items:center; gap:12px}
    .posted{display:none}
  }
</style>
</head>
<body>
<header class="hero">
  <div class="hero-in">
    <span class="badge">⟳ Auto-updated every 3 hours</span>
    <h1>Ohio &amp; Cincinnati <span class="accent">Tech Jobs</span></h1>
    <p class="tag">Software, data, ML &amp; cloud roles across Ohio — from local employers (startups → Fortune 500) and staffing firms, gathered into one place so you never tab through 100 career pages again.</p>
    <div class="stats">
      <div class="stat"><div class="n">__COUNT__</div><div class="l">Open roles</div></div>
      <div class="stat"><div class="n">__COMPANIES__</div><div class="l">Companies</div></div>
      <div class="stat"><div class="n" id="newcount">·</div><div class="l">New today</div></div>
      <div class="stat"><div class="n" id="updated" style="font-size:14px;font-weight:600">__UPDATED__</div><div class="l">Last refresh (ET)</div></div>
    </div>
  </div>
</header>

<div class="bar">
  <div class="bar-in">
    <div class="search">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
      <input type="search" id="q" placeholder="Search title, company, skill…">
    </div>
    <select id="loc">
      <option value="">All Ohio + remote</option>
      <option value="cincinnati">Cincinnati + N. Kentucky</option>
      <option value="columbus">Columbus</option>
      <option value="cleveland">Cleveland</option>
      <option value="dayton">Dayton</option>
      <option value="akron">Akron / NE Ohio</option>
      <option value="toledo">Toledo</option>
      <option value="remote">Remote</option>
    </select>
    <select id="kind">
      <option value="">All employers</option>
      <option value="emp">Direct employers</option>
      <option value="staff">Staffing &amp; vendors</option>
    </select>
    <select id="firm"><option value="">All companies</option>__FIRM_OPTS__</select>
    <label class="toggle"><input type="checkbox" id="fresh"> Last 7 days</label>
  </div>
</div>

<div class="wrap">
  <div class="count" id="count"></div>
  <div id="list"></div>
  <div class="empty" id="empty" style="display:none">
    <div class="big">No roles match your filters</div>
    <div>Try clearing the search or widening the location.</div>
  </div>
</div>

<footer>
  <div class="foot">
    <b>Why this exists.</b> Job-hunting in Ohio means checking dozens of staffing firms and company career pages one at a time. This board watches them for you and surfaces only Ohio-located or remote software / data / ML roles — so you can spend your energy applying, not searching.
    <br><br>
    Built for new grads, career switchers, international students on OPT/CPT, and contractors targeting the Cincinnati &amp; Ohio tech market. Every role links straight to the company's own application page. New postings are flagged each run.
    <br><br>
    Open-source &amp; free · <a href="https://github.com/SIDDARTHAREDDY8/CinciTech">github.com/SIDDARTHAREDDY8/CinciTech</a> · You've got this. 🍀
  </div>
</footer>

<script>
const JOBS = __JOBS_JSON__;
const KIND = __FIRMKIND_JSON__;   // firm name -> "emp" | "staff"
const UPDATED = "__UPDATED_ISO__";   // scrape time (UTC ISO)
const $ = id => document.getElementById(id);
// Ohio is Eastern Time — show the last-refresh stamp in ET (auto EST/EDT).
(function(){
  const t = Date.parse(UPDATED);
  if(!isNaN(t)) $('updated').textContent =
    new Date(t).toLocaleString('en-US',{timeZone:'America/New_York',month:'short',day:'numeric',hour:'numeric',minute:'2-digit'}) + ' ET';
})();
const listEl=$('list'), emptyEl=$('empty'), countEl=$('count');
const q=$('q'), locSel=$('loc'), kindSel=$('kind'), firmSel=$('firm'), fresh=$('fresh');

function esc(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
// Some ATSs (Taleo) hand us the location as a JSON-array string like ["OH-Fairfield"];
// strip brackets/quotes and tidy separators so chips read cleanly.
function cleanLoc(l){return (l||'').replace(/[\[\]"']/g,'').replace(/\s*[;|]\s*/g,'; ').replace(/\s+/g,' ').trim();}

// Freshness: prefer the real posted date when it parses & is recent (<=200d, to
// ignore evergreen/bogus dates), else fall back to first_seen.
function ageDays(j){
  const p=Date.parse(j.posted||'');
  if(!isNaN(p)){const d=(Date.now()-p)/864e5; if(d>=-3&&d<=200) return d;}
  const f=Date.parse(j.first_seen||''); return isNaN(f)?9999:(Date.now()-f)/864e5;
}
function ageLabel(d){
  if(d>=9999) return '';
  if(d<1) return 'Today'; if(d<2) return 'Yesterday';
  if(d<7) return Math.floor(d)+'d ago'; if(d<14) return '1w ago';
  if(d<31) return Math.floor(d/7)+'w ago'; return Math.floor(d/30)+'mo ago';
}
function metro(loc){
  const l=(loc||'').toLowerCase();
  if(/remote|hybrid|virtual|anywhere|telework/.test(l)) return 'remote';
  // Greater Cincinnati = city + OH exurbs (West Chester/Mason/Milford…) + Northern KY
  if(l.includes('cincinnati')||l.includes('blue ash')||l.includes('mason')||l.includes('evendale')||l.includes('fairfield')||l.includes('west chester')||l.includes('norwood')||l.includes('sharonville')||l.includes('milford')||l.includes('loveland')||l.includes('montgomery')||l.includes('springdale')||l.includes('liberty township')||l.includes('hamilton')||l.includes('middletown')||l.includes('lebanon')||l.includes('springboro')||l.includes('batavia')||((/\bky\b|kentucky/.test(l))&&(l.includes('newport')||l.includes('covington')||l.includes('florence')||l.includes('erlanger')||l.includes('hebron')||l.includes('edgewood')||l.includes('fort mitchell')||l.includes('crestview')||l.includes('fort thomas')||l.includes('wilder')||l.includes('bellevue')||l.includes('boone')||l.includes('kenton')||l.includes('campbell')))) return 'cincinnati';
  if(l.includes('columbus')||l.includes('dublin')||l.includes('westerville')||l.includes('new albany')||l.includes('hilliard')||l.includes('marysville')||l.includes('grove city')||l.includes('gahanna')||l.includes('powell')||l.includes('worthington')||l.includes('reynoldsburg')) return 'columbus';
  if(l.includes('cleveland')||l.includes('westlake')||l.includes('solon')||l.includes('mentor')||l.includes('beachwood')||l.includes('independence')||l.includes('brooklyn')||l.includes('avon')||l.includes('elyria')||l.includes('wickliffe')) return 'cleveland';
  if(l.includes('dayton')||l.includes('kettering')||l.includes('beavercreek')||l.includes('miamisburg')||l.includes('springfield')) return 'dayton';
  if(l.includes('akron')||l.includes('canton')||l.includes('youngstown')||l.includes('hudson')||l.includes('twinsburg')||l.includes('medina')||l.includes('stow')) return 'akron';
  if(l.includes('toledo')||l.includes('maumee')||l.includes('perrysburg')||l.includes('findlay')||l.includes('bowling green')) return 'toledo';
  return 'other';
}
const PALETTE=['#0a7d3f','#1e40af','#b45309','#7c3aed','#be123c','#0e7490','#9333ea','#15803d','#c2410c','#4338ca','#0f766e','#a21caf'];
function color(name){let h=0; for(let i=0;i<name.length;i++) h=(h*31+name.charCodeAt(i))>>>0; return PALETTE[h%PALETTE.length];}
function monogram(name){return (name||'?').replace(/[^A-Za-z0-9]/g,'').slice(0,2).toUpperCase()||'?';}

function render(){
  const term=q.value.toLowerCase().trim();
  const loc=locSel.value, kind=kindSel.value, firm=firmSel.value, fo=fresh.checked;
  const rows=JOBS.filter(j=>
    (!firm || j.firm===firm) &&
    (!kind || (KIND[j.firm]||'staff')===kind) &&
    (!loc || metro(j.location)===loc) &&
    (!term || (j.title+' '+j.firm+' '+(j.location||'')).toLowerCase().includes(term)) &&
    (!fo || ageDays(j)<=7)
  ).sort((a,b)=>ageDays(a)-ageDays(b));

  countEl.innerHTML = `Showing <b>${rows.length.toLocaleString()}</b> role${rows.length===1?'':'s'}` +
                      (rows.length!==JOBS.length?` of ${JOBS.length.toLocaleString()}`:'');
  emptyEl.style.display = rows.length?'none':'block';
  listEl.innerHTML = rows.map(j=>{
    const d=ageDays(j), isNew=d<1;
    const k=(KIND[j.firm]||'staff');
    const kindChip = k==='emp'
      ? '<span class="chip kind-emp">🏢 Direct employer</span>'
      : '<span class="chip kind-staff">🤝 Staffing / vendor</span>';
    const lc = cleanLoc(j.location);
    const locChip = lc ? `<span class="chip">📍 ${esc(lc)}</span>` : '';
    const newChip = isNew ? '<span class="chip new">● NEW</span>' : '';
    const al=ageLabel(d);
    return `<div class="card">
      <div class="logo" style="background:${color(j.firm)}">${esc(monogram(j.firm))}</div>
      <div class="body">
        <h3 class="ttl">${esc(j.title)}</h3>
        <div class="co">${esc(j.firm)}</div>
        <div class="metarow">${newChip}${locChip}${kindChip}</div>
      </div>
      <div class="right">
        ${al?`<span class="posted">${al}</span>`:''}
        <a class="apply" href="${esc(j.url)}" target="_blank" rel="noopener">Apply →</a>
      </div>
    </div>`;
  }).join('');
}
// "new today" headline number
$('newcount').textContent = JOBS.filter(j=>ageDays(j)<1).length;
[q,locSel,kindSel,firmSel,fresh].forEach(el=>el.addEventListener('input',render));
render();
</script>
</body>
</html>
"""


def load_firm_kind() -> dict:
    """Map firm name -> 'emp' (direct employer) | 'staff' (staffing/vendor) from config."""
    kind = {}
    try:
        import yaml
        for f in yaml.safe_load(CONFIG.read_text())["firms"]:
            kind[f["name"]] = "emp" if f.get("employer") else "staff"
    except Exception:
        pass
    return kind


def main():
    data = json.loads(DATA.read_text()) if DATA.exists() else {"jobs": [], "count": 0, "updated": "never"}
    jobs = data.get("jobs", [])
    kind = load_firm_kind()
    firms = sorted({j["firm"] for j in jobs}, key=str.lower)
    firm_opts = "".join(f'<option value="{f}">{f}</option>' for f in firms)
    updated = (data.get("updated", "never") or "never")[:16].replace("T", " ")

    html = (TEMPLATE
            .replace("__COUNT__", f"{data.get('count', len(jobs)):,}")
            .replace("__COMPANIES__", str(len(firms)))
            .replace("__UPDATED__", updated)
            .replace("__FIRM_OPTS__", firm_opts)
            .replace("__JOBS_JSON__", json.dumps(jobs))
            .replace("__FIRMKIND_JSON__", json.dumps(kind))
            .replace("__UPDATED_ISO__", data.get("updated", "")))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html)
    (OUT.parent / ".nojekyll").write_text("")  # serve raw HTML, skip Jekyll
    print(f"built {OUT} with {len(jobs)} jobs from {len(firms)} companies")


if __name__ == "__main__":
    main()
