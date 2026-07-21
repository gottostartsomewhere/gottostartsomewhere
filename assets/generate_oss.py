"""Renders the open-source section as a git-graph SVG, in light and dark variants.

GitHub strips CSS from READMEs, so this is drawn rather than styled. The README
picks a variant with <picture media="(prefers-color-scheme: dark)">.

Run: python assets/generate_oss.py
"""

import os

OUT = os.path.dirname(os.path.abspath(__file__))

W = 880
PAD_T = 14
ROW_H = 82
PAD_B = 10
LANE = 34          # x of the graph lane
TEXT_X = 66        # x where repo/desc text starts
RIGHT = W - 28     # right edge for status pills

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace"

THEMES = {
    "dark": dict(
        bg="none", line="#30363d", text="#e6edf3", muted="#8b949e", dim="#6e7681",
        accent="#00BFFF", merged="#a371f7", review="#d29922", node_fill="#0d1117",
        code_bg="#161b22", code_fg="#c9d1d9",
    ),
    "light": dict(
        bg="none", line="#d1d9e0", text="#1f2328", muted="#59636e", dim="#818b98",
        accent="#0969da", merged="#8250df", review="#9a6700", node_fill="#ffffff",
        code_bg="#f6f8fa", code_fg="#1f2328",
    ),
}

# repo, contribution, detail, status, merged?
ROWS = [
    ("OpenBB-finance/OpenBB", "NSE market-data extension",
     "A provider layer for Indian equities, built with the core maintainers",
     "in review", False),
    ("ranaroussi/yfinance", "Interval handling fixes",
     "Corrected resampling behaviour across intraday and daily intervals",
     "merged", True),
    ("dgunning/edgartools", "S-3 filing section extraction",
     "Parses shelf registrations out of raw SEC EDGAR submissions",
     "merged", True),
    ("supabase/supabase-py", "PostgREST array filter coercion",
     "Fixed silently wrong results when filtering on typed array columns",
     "merged", True),
]

MONO_ADV = 0.6  # monospace advance width as a fraction of font-size


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size, fill, weight="400", family=SANS, anchor="start", ls=None):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    k = f' letter-spacing="{ls}"' if ls else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}"{a}{k}>{esc(s)}</text>')


def build(theme_name):
    t = THEMES[theme_name]
    height = PAD_T + len(ROWS) * ROW_H + PAD_B
    o = []

    first_cy = PAD_T + 26
    last_cy = PAD_T + (len(ROWS) - 1) * ROW_H + 26

    # the lane: solid through merged history, dashed up to the open one
    o.append(f'<line x1="{LANE}" y1="{first_cy}" x2="{LANE}" y2="{first_cy + 30}" '
             f'stroke="{t["line"]}" stroke-width="2" stroke-dasharray="4 4"/>')
    o.append(f'<line x1="{LANE}" y1="{first_cy + 30}" x2="{LANE}" y2="{last_cy}" '
             f'stroke="{t["line"]}" stroke-width="2"/>')

    for i, (repo, title, detail, status, merged) in enumerate(ROWS):
        top = PAD_T + i * ROW_H
        cy = top + 26
        col = t["merged"] if merged else t["review"]

        # node: filled for merged, hollow for the one still open
        if merged:
            o.append(f'<circle cx="{LANE}" cy="{cy}" r="6.5" fill="{col}"/>')
            o.append(f'<circle cx="{LANE}" cy="{cy}" r="6.5" fill="none" '
                     f'stroke="{t["node_fill"]}" stroke-width="1.5"/>')
        else:
            o.append(f'<circle cx="{LANE}" cy="{cy}" r="6.5" fill="{t["node_fill"]}" '
                     f'stroke="{col}" stroke-width="2.5"/>')

        # owner dimmed, repo name emphasised, in one flow so proportional
        # font metrics never have to be guessed at
        owner, _, name = repo.partition("/")
        o.append(f'<text x="{TEXT_X}" y="{cy + 5}" font-family="{SANS}" font-size="13.5" '
                 f'fill="{t["dim"]}">{esc(owner)}/<tspan fill="{t["text"]}" '
                 f'font-weight="600">{esc(name)}</tspan></text>')

        o.append(txt(TEXT_X, cy + 26, title, 13.5, t["text"], "500"))
        o.append(txt(TEXT_X, cy + 46, detail, 12.5, t["muted"], "400"))

        # status pill, monospace so the box maths is exact
        fs = 10.5
        pw = len(status) * fs * MONO_ADV + 22
        px = RIGHT - pw
        o.append(f'<rect x="{round(px, 1)}" y="{cy - 9}" width="{round(pw, 1)}" height="19" '
                 f'rx="9.5" fill="none" stroke="{col}" stroke-width="1"/>')
        o.append(txt(round(px + pw / 2, 1), cy + 4.5, status, fs, col, "600",
                     family=MONO, anchor="middle"))

    label = "; ".join(f"{r[0]}, {r[1]}, {r[3]}" for r in ROWS)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {height}" '
            f'width="{W}" height="{height}" role="img" aria-label="{esc(label)}">\n'
            + "\n".join("  " + x for x in o) + "\n</svg>\n")


if __name__ == "__main__":
    for name in THEMES:
        path = os.path.join(OUT, f"oss-{name}.svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(name))
        print(f"oss-{name}.svg")
