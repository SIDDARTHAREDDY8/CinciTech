"""Keyword + location filtering for scraped jobs.

Focused scope: core SOFTWARE ENGINEERING + DATA + AI/ML roles (plus a couple of
niche titles like Member of Technical Staff / Forward Deployed Engineer).
NOT broad IT — we drop help desk, network/sysadmin, business analyst, project
manager, QA, functional ERP/CRM consultants, support, etc.
"""
from __future__ import annotations

import re

# Keep a job only if its title matches ANY of these. This is a BROAD tech/IT
# allowlist — software, data, AI/ML, plus all of "IT" (support, infra/network,
# sysadmin, security, QA, DBA, ERP/functional, health-IT/Epic, IT PM/BA). Ambiguous
# titles ("Project Manager", "Business Analyst") are NOT keywords — they only pass
# when paired with an IT signal (" it ", "technical", "data", "software", …), so a
# non-IT PM/BA still drops. We avoid bare "engineer"/"analyst" (match mechanical/
# finance) and use phrases.
KEYWORDS = [
    # software engineer / developer (all flavors)
    "software engineer", "software developer", "software development engineer",
    "sde", " swe", "developer", "programmer", "coder",
    "full stack", "fullstack", "full-stack", "full stack engineer",
    "front end", "frontend", "front-end", "back end", "backend", "back-end",
    "web developer", "web engineer", "mobile engineer", "mobile developer",
    "ios engineer", "ios developer", "android engineer", "android developer",
    "embedded engineer", "embedded software", "firmware engineer", "game developer",
    "application engineer", "applications engineer", "api engineer", "application developer",
    # software-adjacent engineering (write code)
    "platform engineer", "cloud engineer", "devops engineer", "devops", "cloud ",
    "site reliability", "sre", "security engineer", "infrastructure engineer",
    "systems software", "distributed systems",
    # data
    "data engineer", "data scientist", "data science", "data analyst",
    "data analytics", "analytics engineer", "data architect", "database engineer",
    "big data", "etl developer", "etl engineer", "bi developer", "bi analyst",
    "business intelligence", "data warehouse", "data governance", "data management",
    # ai / ml
    "machine learning", " ml ", " mle", "ml engineer", "ai engineer", " ai ",
    "artificial intelligence", "deep learning", "nlp", "natural language",
    "llm", "genai", "generative ai", "computer vision", "applied scientist",
    "research scientist", "research engineer", "mlops", "ai/ml", "ml/ai",
    # architects
    "software architect", "data architect", "cloud architect", "solutions architect",
    "application architect", "technical architect", "enterprise architect",
    "security architect", "integration architect",
    # --- broad IT: support / infra / network / sysadmin ---
    " it ", "information technology", "help desk", "helpdesk", "service desk",
    "desktop support", "desktop technician", "technical support", "support engineer",
    "support analyst", "support specialist", "application support", "production support",
    "it support", "it specialist", "it analyst", "it technician", "it manager",
    "it director", "it lead", "it coordinator", "it administrator", "it operations",
    "system administrator", "systems administrator", "sysadmin", "system admin",
    "network engineer", "network administrator", "network analyst", "network architect",
    "noc ", "telecom", "voip", "infrastructure", "systems engineer", "systems analyst",
    "system analyst", "storage engineer", "virtualization", "vmware", "citrix",
    "site reliability", "automation engineer",
    # --- enterprise / functional / health IT ---
    "business systems analyst", "it business analyst", "systems integration",
    "epic ", "ehr", "emr", "informatics", "health information", "health it",
    "servicenow", "sharepoint", "salesforce", "dynamics", "power bi", "tableau",
    "sap ", "erp", "peoplesoft", "workday", "netsuite", "oracle dba", "oracle developer",
    "oracle apps", "functional analyst", "functional consultant", "crm developer",
    # --- qa / test ---
    "quality assurance", " qa ", "qa engineer", "qa analyst", "test engineer",
    "quality engineer", "sdet", "test automation", "tester", "test analyst",
    # --- database / data admin ---
    "database administrator", "dba", "database developer", "data administrator",
    # --- security ---
    "cybersecurity", "cyber security", "information security", "security analyst",
    "security operations", "soc analyst", "iam ", "identity and access",
    "grc", "it audit", "penetration test", "incident response", "vulnerability",
    # --- agile / IT delivery / IT-qualified PM & BA ---
    "scrum master", "product owner", "agile coach", "release manager",
    "technical writer", "technical project manager", "it project manager",
    "technical program manager", "technical product manager", "it program manager",
    "implementation consultant", "solutions consultant",
    # niche titles
    "member of technical staff", "member of the technical staff", "technical staff",
    "forward deployed",
]

# Drop these even if a keyword matched — clearly NON-IT roles/disciplines.
# NOTE: broad-IT roles (help desk, network, sysadmin, QA, DBA, ERP, support, PM/BA)
# are NO LONGER excluded — this is now an all-IT board. We keep out non-IT engineering,
# clinical CARE (but allow health-IT/informatics), and other non-tech roles.
EXCLUDE = [
    # sales / staffing / clearance
    "sales", "account manager", "account executive", "recruiter",
    "business development", "talent acquisition", "staffing consultant",
    "clearance", "secret", "ts/sci", "polygraph", "technical recruiter",
    # field/hardware technician (not IT)
    "field service", "field technician", "datacenter technician", "data center technician",
    "cable installer", "line technician", "maintenance technician",
    # non-IT engineering disciplines
    "mechanical engineer", "civil engineer", "chemical engineer", "aerospace",
    "structural engineer", "process engineer", "manufacturing engineer",
    "sales engineer", "electrical engineer", "industrial engineer", "controls engineer",
    "environmental engineer", "petroleum", "geotechnical", "design engineer",
    "project engineer", "machining", " cnc", "tool engineer", "validation engineer",
    "facilities", "hvac",
    # clinical CARE (health-IT / informatics stay IN via KEYWORDS)
    "clinical nurse", "clinical pharmacist", "clinical research", "clinical coordinator",
    "clinical specialist", "clinical educator", "clinical trial", "clinical therapist",
    "registered nurse", "nurse", " rn ", " lpn", "physician", "therapist",
    "pharmacy", "pharmacist", "caregiver", "phlebot", "respiratory", "radiolog",
    "sonograph", "surgical", "dental", "dietitian", "patient",
    # other clearly non-IT roles
    "warehouse", "forklift", "driver", " cdl", "welder", "machinist", "assembler",
    "custodian", "janitor", "cashier", "bartender", "chef", "cook", "barista",
    "plumber", "electrician", "mechanic", "laborer", "receptionist", "machine operator",
    "production operator", "packer", "sanitation", "picker", "stocker",
    "accountant", "bookkeeper", "attorney", "paralegal", "teacher", "instructor",
    "financial analyst", "tax analyst", "accounting analyst", "procurement",
    "buyer", "merchandis", "payroll", "marketing", "graphic designer", "social media",
]


def matches_keywords(title: str) -> bool:
    t = f" {title.lower()} "
    if any(x in t for x in EXCLUDE):
        return False
    return any(k in t for k in KEYWORDS)


# Drop clearly non-US locations (these staffing firms post global/offshore roles).
# Deny-list known foreign countries / Canadian provinces / offshore cities; keep US
# and ambiguous/empty locations. Add to this if a foreign city slips through.
NON_US = [
    # countries
    "canada", "india", "united kingdom", " uk", "england", "scotland", "wales",
    "ireland", "poland", "belgium", "netherlands", "germany", "france",
    "switzerland", "portugal", "spain", "italy", "mexico", "brazil", "colombia",
    "argentina", "philippines", "singapore", "australia", "china", "japan",
    "romania", "ukraine", "czech", "hungary", "austria", "sweden", "denmark",
    # canadian provinces (names + ", XX" codes — none overlap US state codes)
    "ontario", "quebec", "québec", "alberta", "british columbia", "manitoba",
    "saskatchewan", "nova scotia", "new brunswick", "newfoundland",
    ", on", ", qc", ", ab", ", bc", ", mb", ", sk", ", ns", ", nb", ", nl", ", pe",
    # canadian cities
    "toronto", "montreal", "montréal", "vancouver", "calgary", "ottawa", "halifax",
    "sherbrooke", "moncton", "winnipeg", "edmonton", "mississauga", "waterloo",
    # india cities
    "hyderabad", "chennai", "bangalore", "bengaluru", "mumbai", "pune", "delhi",
    "noida", "gurgaon", "gurugram", "kolkata", "ahmedabad", "coimbatore",
    "chandigarh", "trivandrum", "kochi", "indore", "jaipur",
    # europe / other offshore cities
    "london", "leeds", "manchester", "dublin", "lisbon", "porto", "wrocław",
    "wroclaw", "kraków", "krakow", "warsaw", "mechelen", "brussels", "geneva",
    "zurich", "amsterdam", "paris", "berlin", "munich", "madrid", "barcelona",
    "milan", "rome", "bucharest", "prague", "manila", "sydney", "melbourne",
    "flanders", "voivod",
]


def is_non_us(location: str) -> bool:
    if not location:
        return False  # unknown -> keep (firms here are US-focused)
    l = f" {location.lower()} "
    return any(tok in l for tok in NON_US)


# Remote/hybrid roles have no city to match — always keep them (an Ohio-HQ employer's
# remote role is fair game for an Ohio job-seeker).
REMOTE_TOKENS = ("remote", "hybrid", "virtual", "anywhere", "work from home", "wfh",
                 "telework", "work-from-home")

# THIS IS AN OHIO + CINCINNATI BOARD. Every source — including the national staffing
# firms — is filtered to Ohio-located OR remote. OHIO_DEFAULT is the fallback for
# firms with no per-firm location_filter (the staffing firms): it uses STATE-anchored
# tokens (", oh", " oh ", "ohio") rather than bare city names, so other-state cities
# like "Columbus, GA" or "Dayton, TN" don't sneak in. Per-firm location_filter lists
# (the Ohio employers) already carry their specific Ohio cities and take precedence.
OHIO_DEFAULT = ["ohio", "cincinnati", ", oh", " oh ", "oh-", "(oh)", "oh,"]

# Greater Cincinnati spills across the river into NORTHERN KENTUCKY (Newport,
# Covington, Florence, Erlanger, Hebron, the CVG-airport corridor) — that's the same
# metro / commute, so those jobs are in scope. We only accept these specific NKY
# cities AND require a KY signal, so "Newport, RI" / "Florence, SC" / "Covington, GA"
# don't sneak in. (All of Kentucky is NOT in scope — Louisville/Lexington are far.)
NKY_CITIES = (
    "newport", "covington", "florence", "erlanger", "hebron", "edgewood",
    "fort mitchell", "ft mitchell", "crestview hills", "fort wright", "ft wright",
    "wilder", "bellevue", "fort thomas", "ft thomas", "highland heights",
    "cold spring", "alexandria", "villa hills", "taylor mill", "elsmere",
    "park hills", "southgate", "ludlow", "boone county", "kenton county",
    "campbell county", "northern kentucky", "n. kentucky",
)


def _is_nky(loc: str) -> bool:
    """True only for Northern Kentucky (Greater Cincinnati) — a known NKY city AND a
    Kentucky signal, so far-away same-named cities in other states are excluded."""
    l = loc.lower()
    if not re.search(r"\bky\b|kentucky", l):
        return False
    return any(c in l for c in NKY_CITIES)

# Several firms were configured for a US-wide board, so their location_filter lists
# contain broad tokens ("United States", "USA", "US", "") that match any US job (and
# "" matches everything). On an OHIO board those must be ignored, or every national
# role leaks through. We strip them and fall back to OHIO_DEFAULT.
_BROAD_TOKENS = {"united states", "usa", "us", "u.s.", "u.s", "north america",
                 "noam", "anywhere in the us", "nationwide", ""}


def matches_location(location: str, allowed: list[str]) -> bool:
    if not allowed:
        return True
    if not location:
        return True  # keep unknowns rather than silently dropping
    loc = location.lower()
    if any(w in loc for w in REMOTE_TOKENS):
        return True
    return any(a.lower() in loc for a in allowed)


def keep_location(location: str, firm: dict) -> bool:
    """Ohio-board location gate: keep a job only if it's US AND (in Ohio OR remote).

    - firm['ohio_only']: employer that operates only in Ohio but labels jobs by
      facility name ("GRANT MEDICAL CENTER") → keep any US role.
    - empty location: DROPPED. This is the FINAL gate — the board shows no
      unknown-location jobs. (detail_date firms keep blanks transiently in
      apply_filters so they survive to the detail-page enrichment that fills the
      real location; this re-check then drops any that are still blank.)
    - otherwise: must hit a remote token or an Ohio token (per-firm list or OHIO_DEFAULT).
    """
    if is_non_us(location):
        return False
    if not (location or "").strip():
        return False                      # no unknown-location jobs on the board
    if firm.get("ohio_only"):
        return True                       # OH-only employer, facility-named location
    loc = location.lower()
    if any(w in loc for w in REMOTE_TOKENS):
        return True
    if _is_nky(loc):                      # Greater Cincinnati = Ohio + Northern KY
        return True
    allowed = [a for a in (firm.get("location_filter") or []) if a.strip().lower() not in _BROAD_TOKENS]
    if not allowed:
        allowed = OHIO_DEFAULT
    return any(_loc_token_match(loc, a) for a in allowed)


def _loc_token_match(loc: str, token: str) -> bool:
    """Substring match, EXCEPT the bare 2-letter state code 'OH' must be word-bounded
    so 'Johnston, IA' / 'Cohoes, NY' don't match on the 'oh' inside another word."""
    t = token.strip().lower()
    if t == "oh":
        return re.search(r"\boh\b", loc) is not None
    return t in loc


def apply_filters(jobs: list[dict], firm: dict) -> list[dict]:
    """Keep tech roles that are US + (Ohio OR remote) — see keep_location.

    detail_date firms (iCIMS etc.) have BLANK locations on the listing page and only
    get the real location from a per-job detail fetch later, so we let their blank
    jobs through here; run.py re-applies keep_location after that enrichment, which
    drops any still-blank — so the final board never shows an unknown location.
    """
    out = []
    keep_blank = bool(firm.get("detail_date"))
    for j in jobs:
        if not matches_keywords(j["title"]):
            continue
        loc = (j.get("location") or "").strip()
        if not loc and keep_blank:
            out.append(j)
            continue
        if keep_location(j.get("location", ""), firm):
            out.append(j)
    return out
