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
### 🆕 11 new roles this update · 1023 tracked total · updated `2026-07-14T20:11:45+00:00`

| Firm | New roles |
| --- | ---: |
| Robert Half | 2 |
| Cynet Systems | 2 |
| Vertiv | 2 |
| Apex Systems | 1 |
| First Solar | 1 |
| Path Robotics | 1 |
| Kroger | 1 |
| Dana Incorporated | 1 |

| Role | Firm | Location | Found |
| --- | --- | --- | --- |
| [Intelligent Automation Engineer - RPA Automation](https://www.apexsystems.com/job/3042267_usa/intelligent-automation-engineer---rpa-automation) | Apex Systems | Brooklyn, OH | 2026-07-14 |
| [Sr Solutions Architect](https://www.roberthalf.com/us/en/job/cincinnati-oh/sr-solutions-architect/04130-0013455969-usen) | Robert Half | Cincinnati, 04130 | 2026-07-14 |
| [Ms Dynamics Crm Ce Technofunctional Sr Consultant](https://www.roberthalf.com/us/en/job/new-york-ny/ms-dynamics-crm-ce-technofunctional-sr-consultant/02940-0013463294-usen) | Robert Half | Cincinnati, 02940 | 2026-07-14 |
| [Tableau Developer](https://candidateportal.ceipal.com/job-details/KwExrgO9Hswy5Fluq4QLRfcuglD41oa2tvOA_aNRvuY) | Cynet Systems | Ohio | 2026-07-14 |
| [Desktop Support Technician](https://candidateportal.ceipal.com/job-details/ShAUveqyf3MwM68qeq0zLoiKPhiZ3pfIlGtqA-7Q9bc) | Cynet Systems | Ohio | 2026-07-14 |
| [Software Engineer Intern (1st Shift)](https://fa-esbv-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/1025137) | First Solar | Perrysburg, OH, United States | 2026-07-14 |
| [Software Engineer, C++/Robotics](https://boards.greenhouse.io/pathrobotics/jobs/8633387002?gh_jid=8633387002) | Path Robotics | Columbus, Ohio | 2026-07-14 |
| [Senior Advanced Solutions Architect - Data Platforms](https://eluq.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_2001/job/208119) | Kroger | Blue Ash, OH, United States | 2026-07-14 |
| [AI Insights & Governance Analyst](https://egup.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/20275898) | Vertiv | Westerville, OH, United States | 2026-07-14 |
| [Monitoring Technical Support Engineer](https://egup.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/20276722) | Vertiv | Westerville, OH, United States | 2026-07-14 |
| [NVH Test Engineer](https://jobs.dana.com/job/Maumee-NVH-Test-Engineer-OH-43537/1408762400/) | Dana Incorporated | OH | 2026-07-14 |
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
