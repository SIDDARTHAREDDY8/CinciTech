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
### 🆕 13 new roles this update · 1574 tracked total · updated `2026-10-29T18:49:29+00:00`

| Firm | New roles |
| --- | ---: |
| 84.51° | 2 |
| Great American Insurance | 2 |
| Vertiv | 2 |
| Robert Half | 1 |
| Stanton House | 1 |
| Agility Connect | 1 |
| CareSource | 1 |
| Abbott (Columbus) | 1 |
| GE Aerospace | 1 |
| STERIS | 1 |

| Role | Firm | Location | Found |
| --- | --- | --- | --- |
| [Sr Network Engineer](https://www.roberthalf.com/us/en/job/cincinnati-oh/sr-network-engineer/04130-0013493473-usen) | Robert Half | Cincinnati, 04130 | 2026-10-29 |
| [Solutions Engineer, Enterprise](https://www.stantonhouse.com/us/jobs/33044-Solutions-Engineer-Enterprise) | Stanton House | San Francisco, CA (hybrid) | 2026-10-29 |
| [QA Automation Engineer](https://agilityconnect.io/jobs/8582) | Agility Connect | Cincinnati, OH | 2026-10-29 |
| [Lead Data Engineer](https://job-boards.greenhouse.io/8451/jobs/8773368002) | 84.51° | Cincinnati, OH; Chicago, IL | 2026-10-29 |
| [Senior Data Engineer (P1754) (P1752)](https://job-boards.greenhouse.io/8451/jobs/8923332002) | 84.51° | Cincinnati, OH; Chicago, IL | 2026-10-29 |
| [2027 Summer Internship Program - Full Stack AI Development Intern-1](https://caresource.wd1.myworkdayjobs.com/CareSource/job/Remote/XMLNAME-2027-Summer-Internship-Program---Full-Stack-AI-Development-Intern-1_R14181) | CareSource | Remote | 2026-10-29 |
| [Content Publishing Developer Intern - Summer 2027](https://gaig.wd1.myworkdayjobs.com/GAIG_External/job/Cincinnati-OH-USA/Content-Publishing-Developer-Intern---Summer-2027_R9813) | Great American Insurance | Cincinnati, OH (USA) | 2026-10-29 |
| [IT Data Intern - Summer 2027](https://gaig.wd1.myworkdayjobs.com/GAIG_External/job/Cincinnati-OH-USA/IT-Data-Intern---Summer-2027_R9820) | Great American Insurance | Cincinnati, OH (USA) | 2026-10-29 |
| [Product Manager- Epic](https://abbott.wd5.myworkdayjobs.com/abbottcareers2/job/United-States-of-America--Remote/Product-Manager--Epic_31165840) | Abbott (Columbus) | United States of America : Remote | 2026-10-29 |
| [Test Engineer](https://geaerospace.wd5.myworkdayjobs.com/GE_ExternalSite/job/Evendale/Test-Engineer_R5042435-1) | GE Aerospace | Evendale | 2026-10-29 |
| [Test Engineer (Thermal Lab) - 2nd Shift](https://egup.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/20261158) | Vertiv | Columbus, OH, United States | 2026-10-29 |
| [Internal Audit Operations Specialist](https://egup.fa.us2.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX/job/20271079) | Vertiv | Westerville, OH, United States | 2026-10-29 |
| [Technical Support Specialist - Software](https://career4.successfactors.com/careers?company=steriscorpP&lang=en_US&career_ns=job_application&career_job_req_id=55386&jobPipeline=PhenomCareerSite) | STERIS | Mentor, Ohio | 2026-10-29 |
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
