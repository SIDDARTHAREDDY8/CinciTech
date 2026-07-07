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
### 🆕 12 new roles this update · 768 tracked total · updated `2026-07-07T20:36:27+00:00`

| Firm | New roles |
| --- | ---: |
| Next Step Systems | 3 |
| Russell Tobin | 1 |
| Artech | 1 |
| Vernovis | 1 |
| CareSource | 1 |
| Root Insurance | 1 |
| Great American Insurance | 1 |
| Worldpay | 1 |
| STERIS | 1 |
| Lubrizol | 1 |

| Role | Firm | Location | Found |
| --- | --- | --- | --- |
| [Staff Software Engineer, Configuration & Experimentation Infrastructure](https://www2.jobdiva.com/portal/?a=nyjdnw8rs3eurnjvdink7d2fl4mnyy0b22tjlzi328snknlo1pzpk0ue533mvm7r&compid=2&jobid=28818842#/jobs/28818842) | Russell Tobin | Remote, CA | 2026-07-07 |
| [Devops (OSI/AspenTech/Emerson Monarch products (ADMS) - Remote - 6+ Months](https://www1.jobdiva.com/portal/?a=kvjdnwtsxgckrpsoozx5qc0oueybw1005779v7x6soig8eyqqmzaubfdl9tcx21s&compid=0&jobid=32553778#/jobs/32553778) | Artech | Remote, NY | 2026-07-07 |
| [Staff Machine Learning Engineer, Work From Home](https://www.nextstepsystems.com/job/staff-machine-learning-engineer-work-from-home/) | Next Step Systems | San Francisco, CA, USA (Remote) | 2026-07-07 |
| [Senior Machine Learning Engineer, Work From Home](https://www.nextstepsystems.com/job/senior-machine-learning-engineer-work-from-home/) | Next Step Systems | San Francisco, CA, USA (Remote) | 2026-07-07 |
| [Machine Learning Technical Lead, Work From Home](https://www.nextstepsystems.com/job/machine-learning-technical-lead-work-from-home/) | Next Step Systems | San Francisco, CA, USA (Remote) | 2026-07-07 |
| [ERP Applications Manager](https://vernovis.com/blog/jobs/12005/) | Vernovis | Cincinnati, | 2026-07-07 |
| [Senior Director, Clinical Data Governance and Integration](https://caresource.wd1.myworkdayjobs.com/CareSource/job/Remote/Senior-Director--Clinical-Data-Governance-and-Integration_R12620) | CareSource | Remote | 2026-07-07 |
| [Staff Data Engineer, Financial Data Operations](https://ats.rippling.com/joinroot/jobs/1c80913f-cca4-479e-99b5-15e5f6312e1b) | Root Insurance | Remote (United States) | 2026-07-07 |
| [Workday Financial Systems Analyst](https://gaig.wd1.myworkdayjobs.com/GAIG_External/job/Cincinnati-OH-USA/Workday-Financial-Systems-Analyst_R9195-1) | Great American Insurance | Cincinnati, OH (USA) | 2026-07-07 |
| [Senior DevOps Cloud Engineer](https://worldpay.wd5.myworkdayjobs.com/Worldpay_External_Careers_Site/job/CINCINNATI-OHIO/Senior-DevOps-Cloud-Engineer_JR0609751) | Worldpay | CINCINNATI, OHIO | 2026-07-07 |
| [Senior IT Internal Auditor](https://career4.successfactors.com/careers?company=steriscorpP&lang=en_US&career_ns=job_application&career_job_req_id=55093&jobPipeline=PhenomCareerSite) | STERIS | Mentor, Ohio | 2026-07-07 |
| [IT Category Manager - Software & SaaS](https://jobs.lubrizol.com/job/Wickliffe-IT-Category-Manager-Software-&-SaaS-OH-44092-2298/1384114200/) | Lubrizol | OH | 2026-07-07 |
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
