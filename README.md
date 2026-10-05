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
### 🆕 11 new roles this update · 1742 tracked total · updated `2026-10-05T22:27:48+00:00`

| Firm | New roles |
| --- | ---: |
| Medical Mutual of Ohio | 2 |
| Vernovis | 1 |
| First Solar | 1 |
| Path Robotics | 1 |
| Root Insurance | 1 |
| Fifth Third Bank | 1 |
| Sherwin-Williams | 1 |
| Huntington Bank | 1 |
| Battelle | 1 |
| L3Harris | 1 |

| Role | Firm | Location | Found |
| --- | --- | --- | --- |
| [Data Analytics Engineer](https://vernovis.com/blog/jobs/12222/) | Vernovis | Cincinnati, | 2026-10-05 |
| [Data Science Intern – Device Characterization (Spring 2027)](https://fa-esbv-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/1026161) | First Solar | Perrysburg, OH, United States | 2026-10-05 |
| [Data Engineer, ML Ops](https://boards.greenhouse.io/pathrobotics/jobs/8868497002?gh_jid=8868497002) | Path Robotics | Columbus, Ohio | 2026-10-05 |
| [Software Engineer Intern: Agent Commerce](https://ats.rippling.com/joinroot/jobs/845e02f9-86ee-41f9-a9ad-730ed08fca3b) | Root Insurance | Remote (United States) | 2026-10-05 |
| [Enterprise Domains IT Product Owner](https://fifththird.wd5.myworkdayjobs.com/53careers/job/Cincinnati-OH/Enterprise-Domains-IT-Product-Owner_R73244-1) | Fifth Third Bank | Cincinnati, OH | 2026-10-05 |
| [SCADA Lead Full Stack Application Developer - Industrial Automation](https://ejhp.fa.us6.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_2/job/2625640) | Sherwin-Williams | Cleveland, OH, United States | 2026-10-05 |
| [IS Technical Specialist (Full-Stack SDE)](https://huntington.wd12.myworkdayjobs.com/HNBcareers/job/Columbus-OH/IS-Technical-Specialist--Full-Stack-SDE-_R0076340) | Huntington Bank | Columbus, OH | 2026-10-05 |
| [HR AI Automation Internship (Summer 2027)](https://jobs.battelle.org/us/en/job/76591) | Battelle | Columbus, OH | 2026-10-05 |
| [MS Dynamics 365 Technical Architect](https://medmutual.rec.pro.ukg.net/MED1500MMOO/JobBoard/ef821115-21e9-4a27-9b98-50f8e2f05f30/OpportunityDetail?opportunityId=cfbeef41-5ccc-4e22-8ddf-b290e03225e2) | Medical Mutual of Ohio | Brooklyn OH | 2026-10-05 |
| [Manager, Data Engineering](https://medmutual.rec.pro.ukg.net/MED1500MMOO/JobBoard/ef821115-21e9-4a27-9b98-50f8e2f05f30/OpportunityDetail?opportunityId=26142d75-4bb9-400e-9fb5-b606c030df4c) | Medical Mutual of Ohio | Brooklyn OH | 2026-10-05 |
| [Associate, Systems Engineer](https://careers.l3harris.com/en/job/mason/associate-systems-engineer/4832/101569326352) | L3Harris | Mason, OH | 2026-10-05 |
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
