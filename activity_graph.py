#!/usr/bin/env python3
"""Render a themed contribution-activity SVG for the profile README.

Runs inside GitHub Actions with the workflow's GITHUB_TOKEN, so it has no
dependency on third-party hosted services. Standard library only.

Usage:
  python scripts/activity_graph.py --user NAME --out profile/activity.svg
  python scripts/activity_graph.py --demo --out preview.svg   # fake data
"""
import argparse, datetime as dt, json, os, random, urllib.request

DAYS = 182  # about six months
C = dict(bg="#0A0F1F", grid="#15203A", cyan="#22D3EE", violet="#A78BFA",
         green="#34D399", text="#E2E8F0", muted="#7C8BA5", edge="#1F2B48")
MONO = "'JetBrains Mono','SF Mono',Consolas,'Liberation Mono',monospace"
SANS = "'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"

QUERY = """query($login:String!){ user(login:$login){ contributionsCollection{
  contributionCalendar{ weeks{ contributionDays{ date contributionCount }}}}}}"""


def fetch(user, token):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": user}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json",
                 "User-Agent": "profile-activity-graph"})
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.load(r)
    if "errors" in payload:
        raise SystemExit(f"GraphQL error: {payload['errors']}")
    weeks = payload["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    days = [(d["date"], d["contributionCount"]) for w in weeks for d in w["contributionDays"]]
    return days[-DAYS:]


def demo():
    today = dt.date.today()
    rnd = random.Random(7)
    out = []
    for i in range(DAYS):
        d = today - dt.timedelta(days=DAYS - 1 - i)
        base = 2 + 6 * (i / DAYS)
        out.append((d.isoformat(), 0 if rnd.random() < 0.12 else int(rnd.expovariate(1 / base))))
    return out


def rolling(vals, n=7):
    return [sum(vals[max(0, i - n + 1):i + 1]) / len(vals[max(0, i - n + 1):i + 1]) for i in range(len(vals))]


def render(days):
    W, H = 1000, 330
    L, R, T, B = 60, 30, 110, 50
    pw, ph = W - L - R, H - T - B
    dates = [dt.date.fromisoformat(d) for d, _ in days]
    vals = [v for _, v in days]
    avg = rolling(vals)
    top = max(max(vals), 4)
    step = pw / (len(vals) - 1)
    x = lambda i: L + i * step
    y = lambda v: T + ph - (v / top) * ph

    total = sum(vals)
    active = sum(1 for v in vals if v)
    best_i = max(range(len(vals)), key=lambda i: vals[i])
    best = f"{vals[best_i]} on {dates[best_i]:%d %b}"

    bars = "".join(
        f'<rect x="{x(i) - step * 0.35:.1f}" y="{y(v):.1f}" width="{max(step * 0.7, 1):.1f}" '
        f'height="{T + ph - y(v):.1f}" rx="1" fill="{C["violet"]}" opacity=".28"/>'
        for i, v in enumerate(vals) if v)
    pts = " ".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(avg))
    area = f"M{L},{T + ph} L" + " L".join(pts.split()) + f" L{x(len(avg) - 1):.1f},{T + ph} Z"

    grid = ""
    for k in range(5):
        gy = T + ph * k / 4
        label = round(top * (1 - k / 4))
        grid += (f'<line x1="{L}" x2="{W - R}" y1="{gy:.1f}" y2="{gy:.1f}" stroke="{C["grid"]}"/>'
                 f'<text x="{L - 12}" y="{gy + 4:.1f}" text-anchor="end" class="ax">{label}</text>')
    months = ""
    for i, d in enumerate(dates):
        if d.day == 1 and x(i) < W - R - 20:
            months += f'<text x="{x(i):.1f}" y="{T + ph + 26}" class="ax">{d:%b}</text>'

    chips = [("contributions", f"{total:,}"), ("active days", f"{active}/{len(vals)}"), ("busiest day", best)]
    chip_svg, cx = "", W - R
    for label, value in reversed(chips):
        w = 34 + 9.2 * max(len(value), len(label))
        cx -= w
        chip_svg += (f'<g transform="translate({cx:.0f} 26)">'
                     f'<rect width="{w - 12:.0f}" height="52" rx="10" fill="#0E1629" stroke="{C["edge"]}"/>'
                     f'<text x="14" y="24" class="val">{value}</text>'
                     f'<text x="14" y="42" class="ax">{label}</text></g>')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Contribution activity for the last six months: {total} contributions">
<defs>
  <linearGradient id="a" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{C["cyan"]}" stop-opacity=".35"/><stop offset="1" stop-color="{C["cyan"]}" stop-opacity="0"/>
  </linearGradient>
</defs>
<style>
  .ax{{font:12px {MONO};fill:{C["muted"]}}}
  .val{{font:600 15px {MONO};fill:{C["text"]}}}
  .ttl{{font:600 20px {SANS};fill:{C["text"]}}}
  .sub{{font:13px {SANS};fill:{C["muted"]}}}
  .line{{stroke-dasharray:4000;stroke-dashoffset:4000;animation:draw 2.4s ease-out forwards}}
  .fill{{opacity:0;animation:show .8s 1.6s ease-out forwards}}
  @keyframes draw{{to{{stroke-dashoffset:0}}}}
  @keyframes show{{to{{opacity:1}}}}
  @media (prefers-reduced-motion: reduce){{.line{{animation:none;stroke-dashoffset:0}}.fill{{animation:none;opacity:1}}}}
</style>
<rect width="{W}" height="{H}" rx="16" fill="{C["bg"]}" stroke="{C["edge"]}"/>
<text x="{L - 20}" y="52" class="ttl">Contribution signal</text>
<text x="{L - 20}" y="74" class="sub">Last six months, line shows the 7-day average</text>
{chip_svg}
{grid}{months}
{bars}
<path class="fill" d="{area}" fill="url(#a)"/>
<polyline class="line" points="{pts}" fill="none" stroke="{C["cyan"]}" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="{x(len(avg) - 1):.1f}" cy="{y(avg[-1]):.1f}" r="4.5" fill="{C["violet"]}" class="fill"/>
</svg>'''


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--user", default=os.environ.get("GITHUB_REPOSITORY_OWNER", ""))
    ap.add_argument("--out", default="profile/activity.svg")
    ap.add_argument("--demo", action="store_true")
    a = ap.parse_args()
    data = demo() if a.demo else fetch(a.user, os.environ["GITHUB_TOKEN"])
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    open(a.out, "w", encoding="utf-8").write(render(data))
    print(f"wrote {a.out}")
