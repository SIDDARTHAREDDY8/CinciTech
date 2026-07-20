# Cincinnati & Ohio Tech Jobs 🟢

**A free, auto-updating job board for software, data, ML & cloud roles across Ohio — pulled
from 130+ company career pages and staffing firms every 3 hours, filtered to Ohio + remote.**

### 👉 [Browse the live board »](https://siddarthareddy8.github.io/CinciTech/)

---

## Why I built this

Job-hunting in Ohio is a grind of open tabs. The roles are out there — at Cincinnati and
Columbus startups, at Fortune 500s like P&G, Kroger and Sherwin-Williams, at hospitals and
manufacturers that quietly hire software and data people, and across dozens of staffing
firms — but they're scattered across a hundred different career portals, each with its own
search box and its own login. There's no single place to see "what tech jobs are open in
Ohio right now."

I got tired of checking the same 100 sites by hand, so I built one that checks them for me.
Every few hours it scrapes all of those sources, keeps only the Ohio-located and remote
software / data / ML / cloud roles, drops the noise, and drops each job straight onto one
searchable board with a direct apply link. No account, no paywall, no recruiter spam.

## Who it helps

- **New grads & students** starting their careers in Ohio
- **International students** on OPT/CPT who need to see the whole local market fast
- **Career switchers** breaking into tech without a network to lean on
- **Contractors & C2C folks** tracking staffing-firm reqs across the state
- **Anyone in or moving to Cincinnati, Columbus, Cleveland or Dayton** who just wants the
  jobs in one place

If that's you, this is yours to use freely.

## A note 🍀

Job searching is hard, and it can make you feel small — especially when you're doing it from
a new country, a new field, or after a setback. Please remember: a rejection is one company on
one day, not a verdict on you. The right role often comes after the one that felt like "the
one." Keep applying, keep building, keep going. You only need it to work **once**.

This board exists to take one annoying part off your plate so you have more energy for the
parts that matter. Rooting for you. 💚

---

| | |
| --- | --- |
| 🔄 **Refresh** | every 3 hours via GitHub Actions |
| 🎯 **Scope** | software / data / ML / cloud roles in **Ohio + remote** (Cincinnati, Columbus, Cleveland, Dayton, …) |
| 🏢 **Sources** | 130+ — local employers (startups → Fortune 500), health systems & manufacturers that hire tech, plus staffing/IT-vendor firms |
| 🧹 **Filtered** | Ohio-located or remote only; keeps SWE/data/ML; drops sales, nursing, warehouse, clearance, non-IT analyst/engineer roles |
| 📦 **Archive** | full searchable board at [`docs/index.html`](docs/index.html) · raw data in [`data/jobs.json`](data/jobs.json) |
| 🧭 **Sibling** | [JobsBuddy](https://github.com/SIDDARTHAREDDY8/JobsBuddy) does the same for full-time, H1B-sponsor roles |

## 🆕 Live Jobs

<!-- JOBS:START -->
### 🆕 10 new roles this update · 1292 tracked total · updated `2026-07-20T22:38:56+00:00`

| Firm | New roles |
| --- | ---: |
| Russell Tobin | 2 |
| Cynet Systems | 2 |
| Insight Global | 1 |
| Artech | 1 |
| Fifth Third Bank | 1 |
| American Electric Power | 1 |
| KeyBank | 1 |
| Honda | 1 |

| Role | Firm | Location | Found |
| --- | --- | --- | --- |
| [Data and AI Platform Manager](https://jobs.insightglobal.com/jobs/find_a_job/ohio/columbus/data-and-ai-platform-manager/job-554234/) | Insight Global | Columbus, OH | 2026-07-20 |
| [Solutions Architect](https://www2.jobdiva.com/portal/?a=nyjdnw8rs3eurnjvdink7d2fl4mnyy0b22tjlzi328snknlo1pzpk0ue533mvm7r&compid=2&jobid=28913756#/jobs/28913756) | Russell Tobin | REMOTE | 2026-07-20 |
| [ERP Consultant - Oracle](https://www2.jobdiva.com/portal/?a=nyjdnw8rs3eurnjvdink7d2fl4mnyy0b22tjlzi328snknlo1pzpk0ue533mvm7r&compid=2&jobid=28885292#/jobs/28885292) | Russell Tobin | REMOTE | 2026-07-20 |
| [Information Technology - Operations - IT Project Manager (SAP)](https://www1.jobdiva.com/portal/?a=kvjdnwtsxgckrpsoozx5qc0oueybw1005779v7x6soig8eyqqmzaubfdl9tcx21s&compid=0&jobid=32723668#/jobs/32723668) | Artech | Remote, NC | 2026-07-20 |
| [SAP BTP Lead - Remote / Telecommute](https://candidateportal.ceipal.com/job-details/a1iC9U0v-B9ZWTev7OxknJ6SLSCl4Tj7I0NZ1lxRhMQ) | Cynet Systems | Ohio | 2026-07-20 |
| [DotNet Developer - Remote / Telecommute](https://candidateportal.ceipal.com/job-details/QmLJ1uTueg4m3p6Vu0Vmt6DSfFeQN2oHJcfRsZL2sfU) | Cynet Systems | Ohio | 2026-07-20 |
| [Depositor Services Processing & Support Specialist I](https://fifththird.wd5.myworkdayjobs.com/53careers/job/Cincinnati-OH/Depositor-Services-Processing---Support-Specialist-I_R70596) | Fifth Third Bank | Cincinnati, OH | 2026-07-20 |
| [Davis-Bacon Act (DBA) Federal Labor Compliance Lead](https://aep.wd1.myworkdayjobs.com/AEPCareerSite/job/Columbus-OH/Davis-Bacon-Act--DBA--Federal-Labor-Compliance-Lead_R17484) | American Electric Power | Columbus, OH | 2026-07-20 |
| [Software Engineer - Azure GenAI](https://keybank.wd5.myworkdayjobs.com/External_Career_Site/job/Brooklyn-OH/Software-Engineer---Azure-GenAI_R-39676) | KeyBank | Brooklyn, OH | 2026-07-20 |
| [Senior ADAS Hardware Test Engineer I](https://careers.honda.com/us/en/job/11896) | Honda | Raymond, Ohio, United States | 2026-07-20 |
<!-- JOBS:END -->

## How it works

```
config/firms.yaml   →  one entry per firm (URL + how to read its job cards)
scraper/engine.py   →  fetch each firm (api / api_html / dom / apify_search)
scraper/filters.py  →  keep IT roles, drop non-IT; US/Cincinnati/remote locations
scraper/store.py    →  dedupe + first-seen tracking into data/jobs.json
build_site.py       →  render data/jobs.json into docs/index.html (GitHub Pages)
build_readme.py     →  inject newly-found roles into this README (JOBS markers)
.github/workflows   →  run every 3 hours, commit fresh jobs + site + README
```

Each firm can run in one of two modes:

- **`dom`** — Playwright renders the page and reads job cards via CSS selectors.
  Works on any site. Breaks if the firm redesigns (just re-fix the selectors).
- **`api`** — call the JSON endpoint the page itself calls (DevTools → Network → XHR).
  Faster and more stable. Use it when you can find the endpoint.

## Setup

```bash
cd ohio-tech-jobs
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
```

## Run

```bash
python run.py                      # all firms
python run.py --only "TEKsystems"  # one firm
python run.py --headful            # watch the browser (debug selectors)
python build_site.py               # rebuild the HTML board
open docs/index.html
```

## Calibrating a firm  (the one manual step)

Career pages differ, so each firm needs its selectors confirmed once:

1. Open the firm's job-search URL in Chrome.
2. Right-click a job listing → **Inspect**.
3. Find the repeating container element → that's your `card` selector.
4. Inside it, find the title / location / link elements → fill those selectors.
5. Run `python run.py --only "<Firm>" --headful` and watch it pull jobs.

**Tip:** before writing selectors, check the **Network → XHR** tab. If you see a
clean JSON request returning the jobs, switch that firm to `mode: api` instead —
it's far more reliable than scraping rendered HTML.

## Adding more firms

Append to `config/firms.yaml`. Your Desktop already has
`Comprehensive_List_of_US_Tech_Staffing_&_Vendor_Companies.pdf` — pull names from there.

## Notes / honesty

- These firms **want** their jobs found (that's how they fill reqs), so listings are
  public — no login wall.
- Be polite: the 3-hour cron is plenty. Don't hammer.
- Some firms use anti-bot (Cloudflare). If a firm returns nothing in `dom` mode,
  it may need `mode: api` or an Apify Actor.
- Selectors in `firms.yaml` are **starting points** and must be confirmed live.
