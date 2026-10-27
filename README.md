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
### 🆕 13 new roles this update · 1575 tracked total · updated `2026-10-27T15:42:52+00:00`

| Firm | New roles |
| --- | ---: |
| Great American Insurance | 2 |
| Robert Half | 1 |
| CareSource | 1 |
| Fifth Third Bank | 1 |
| Sherwin-Williams | 1 |
| FirstEnergy | 1 |
| Huntington Bank | 1 |
| Materion | 1 |
| Nationwide Children's Hospital | 1 |
| Vertiv | 1 |
| Honda | 1 |
| Fidelity Investments | 1 |

| Role | Firm | Location | Found |
| --- | --- | --- | --- |
| [Security Forward Deployed Engineer](https://www.roberthalf.com/us/en/job/cincinnati-oh/security-forward-deployed-engineer/02940-0013512369-usen) | Robert Half | Cincinnati, 02940 | 2026-10-27 |
| [Information Security GRC Analyst IV - ESH](https://caresource.wd1.myworkdayjobs.com/CareSource/job/Remote/Information-Security-GRC-Analyst-IV---ESH_R14143) | CareSource | Remote | 2026-10-27 |
| [AI Risk Management Senior Associate](https://fifththird.wd5.myworkdayjobs.com/53careers/job/Cincinnati-OH/AI-Risk-Management-Senior-Associate_R73467) | Fifth Third Bank | Cincinnati, OH | 2026-10-27 |
| [Senior Technical Product Manager](https://gaig.wd1.myworkdayjobs.com/GAIG_External/job/Cincinnati-OH-USA/Senior-Technical-Product-Manager_R9789) | Great American Insurance | Cincinnati, OH (USA) | 2026-10-27 |
| [Senior Data Scientist](https://gaig.wd1.myworkdayjobs.com/GAIG_External/job/Cincinnati-OH-USA/Senior-Data-Scientist_R9787) | Great American Insurance | Cincinnati, OH (USA) | 2026-10-27 |
| [R&D IT Summer Internship- Brecksville, OH](https://ejhp.fa.us6.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_2/job/2627637) | Sherwin-Williams | Brecksville, OH, United States | 2026-10-27 |
| [Systems Administrator - IT Infrastructure & Operations](https://fa-etjd-saasfaprod1.fa.ocs.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1/job/105640) | FirstEnergy | Akron, OH, United States | 2026-10-27 |
| [Programmer/Analyst Senior](https://huntington.wd12.myworkdayjobs.com/HNBcareers/job/Columbus-OH/Programmer-Analyst-Senior_R0076898) | Huntington Bank | Columbus, OH | 2026-10-27 |
| [Customer Support Specialist - Manufacturing](https://materion.wd5.myworkdayjobs.com/Materion/job/Cleveland-OH/Customer-Support-Specialist---Manufacturing_2026-R8834) | Materion | Cleveland, OH | 2026-10-27 |
| [IT Project Scientist I - Research Data Navigation](https://nationwidechildrens.wd5.myworkdayjobs.com/NCHCareers/job/431-S-18th-St-Columbus-OH/IT-Project-Scientist-I---Research-Data-Navigation_R-28600-1) | Nationwide Children's Hospital | 431 S 18th St, Columbus, OH | 2026-10-27 |
| [IT Project Manager](https://egup.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/20271302) | Vertiv | Westerville, OH, United States | 2026-10-27 |
| [Supplier Quality Engineer](https://careers.honda.com/us/en/job/12274) | Honda | Raymond, Ohio, United States | 2026-10-27 |
| [Audit Manager](https://wd1.myworkdaysite.com/recruiting/fmr/FidelityCareers/job/Covington-KY/Audit-Manager_2137323) | Fidelity Investments | Covington, KY | 2026-10-27 |
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
