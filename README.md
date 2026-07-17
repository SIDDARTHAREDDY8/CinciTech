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
### 🆕 12 new roles this update · 1177 tracked total · updated `2026-07-17T14:34:46+00:00`

| Firm | New roles |
| --- | ---: |
| Cynet Systems | 6 |
| Artech | 3 |
| TEKsystems | 1 |
| FirstEnergy | 1 |
| O-I Glass | 1 |

| Role | Firm | Location | Found |
| --- | --- | --- | --- |
| [Audit Technician](https://careers.teksystems.com/us/en/job/JP-006162300/Audit-Technician) | TEKsystems | New Albany, Ohio | 2026-07-17 |
| [Information Technology - Application Development - Software Developer - Java](https://www1.jobdiva.com/portal/?a=kvjdnwtsxgckrpsoozx5qc0oueybw1005779v7x6soig8eyqqmzaubfdl9tcx21s&compid=0&jobid=32715403#/jobs/32715403) | Artech | Remote, NY | 2026-07-17 |
| [Quality Engineer - Automation - Multiple Locations - Long Term](https://www1.jobdiva.com/portal/?a=kvjdnwtsxgckrpsoozx5qc0oueybw1005779v7x6soig8eyqqmzaubfdl9tcx21s&compid=0&jobid=32710469#/jobs/32710469) | Artech | Columbus, OH | 2026-07-17 |
| [Quality Engineer - Automation - Multiple Locations - Long Term](https://www1.jobdiva.com/portal/?a=kvjdnwtsxgckrpsoozx5qc0oueybw1005779v7x6soig8eyqqmzaubfdl9tcx21s&compid=0&jobid=32711052#/jobs/32711052) | Artech | Columbus, OH | 2026-07-17 |
| [DotNet Developer - Remote / Telecommute](https://candidateportal.ceipal.com/job-details/puWmx3R3HbNhZM4VUaOonW52QSL8HEBYXBt57XJpe9Y) | Cynet Systems | Ohio | 2026-07-17 |
| [Manual Tester - Remote / Telecommute](https://candidateportal.ceipal.com/job-details/0AMtB25s6XPbYFTawKA43TW5IU0D3r3a6y_9LKt2qHQ) | Cynet Systems | Ohio | 2026-07-17 |
| [Manual Tester - Remote / Telecommute](https://candidateportal.ceipal.com/job-details/f0Ut7LAujb9VbuvGQx03E_v306ZGsIGAGqduUXZFCyE) | Cynet Systems | Ohio | 2026-07-17 |
| [Manual Tester - Remote / Telecommute](https://candidateportal.ceipal.com/job-details/8Grhaeh4evC07EfpQ8BFlWD-Gmf8v2IsrzJHdq8pRnU) | Cynet Systems | Ohio | 2026-07-17 |
| [Manual Tester - Remote / Telecommute](https://candidateportal.ceipal.com/job-details/6NCOLV5uhA0yZXi756Reiu1furO4Vu36loPR__yE9JM) | Cynet Systems | Ohio | 2026-07-17 |
| [Tableau Developer](https://candidateportal.ceipal.com/job-details/oxC2ZRb2ily8LseTRuvH4xJqu45ElPE_K77zBK4_xKQ) | Cynet Systems | Ohio | 2026-07-17 |
| [Cyber and Information Security Analyst - Cyber Security & TSOC](https://fa-etjd-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/104067) | FirstEnergy | Akron, OH, United States | 2026-07-17 |
| [SAP BASIS Administrator - Advanced](https://jobs.smartrecruiters.com/O-I/744000138332019) | O-I Glass | Perrysburg, OH | 2026-07-17 |
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
