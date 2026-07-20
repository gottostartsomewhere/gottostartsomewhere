"""Generates every SVG in this folder. Run `python assets/generate.py` from the repo root.

GitHub strips CSS from READMEs, so the whole terminal look is baked into SVG.
Fonts are not fetchable inside GitHub's image sandbox either, which is why the
headline is a hand-drawn 5x7 bitmap font and everything else uses the system
monospace stack.
"""

import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)))
W = 880

BG      = "#04060a"
PANEL   = "#080c12"
INK     = "#060a0e"
BORDER  = "#1c3a2c"
RULE    = "#16212a"
GREEN   = "#34e39b"
CYAN    = "#38d6ff"
RED     = "#e0533d"
AMBER   = "#e5a13a"
TEXT    = "#eef4f0"
BODY    = "#c9d3dd"
MUTED   = "#8b949e"
DIM     = "#5b6570"

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
ADV = 0.6  # monospace advance width as a fraction of font-size


def w(text, size):
    """Approximate rendered width of monospace text."""
    return len(text) * size * ADV


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def txt(x, y, s, size=12, fill=MUTED, weight="400", anchor="start", ls=None):
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    k = f' letter-spacing="{ls}"' if ls else ""
    return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}"{a}{k}>{esc(s)}</text>')


def rect(x, y, ww, h, fill="none", stroke=None, sw=1, extra=""):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{ww}" height="{h}" fill="{fill}"{s}{extra}/>'


def tri(cx, cy, size, fill, up=True):
    d = 1 if up else -1
    return (f'<polygon points="{cx},{cy - d * size} {cx - size},{cy + d * size * 0.8} '
            f'{cx + size},{cy + d * size * 0.8}" fill="{fill}"/>')


def star(cx, cy, r, fill):
    """Five-point star, drawn rather than typed so no font has to supply it."""
    import math
    pts = []
    for i in range(10):
        rad = r if i % 2 == 0 else r * 0.42
        a = math.pi / 2 * 3 + i * math.pi / 5
        pts.append(f"{round(cx + math.cos(a) * rad, 1)},{round(cy + math.sin(a) * rad, 1)}")
    return f'<polygon points="{" ".join(pts)}" fill="{fill}"/>'


def chip(x, y, label, size=11, fg=None, bd=BORDER, bg="#0a1512", pad=11, h=24):
    """Bordered pill. Returns (svg, width)."""
    fg = fg or "#9fdcc0"
    cw = w(label, size) + pad * 2
    s = (rect(x, y, round(cw, 1), h, bg, bd)
         + txt(round(x + cw / 2, 1), y + h / 2 + size * 0.36, label, size, fg, anchor="middle"))
    return s, cw


def svg(width, height, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" role="img" aria-label="{esc(label)}">\n'
            + "\n".join("  " + b for b in body) + "\n</svg>\n")


def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{name}  {len(content)}b")


# ── 5x7 bitmap font ──────────────────────────────────────────────────────────
FONT = {
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "B": ["11110", "10001", "10001", "11110", "10001", "10001", "11110"],
    "C": ["01111", "10000", "10000", "10000", "10000", "10000", "01111"],
    "D": ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    "E": ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "G": ["01110", "10001", "10000", "10111", "10001", "10001", "01111"],
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "J": ["00111", "00010", "00010", "00010", "00010", "10010", "01100"],
    "K": ["10001", "10010", "10100", "11000", "10100", "10010", "10001"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "N": ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    "O": ["01110", "10001", "10001", "10001", "10001", "10001", "01110"],
    "P": ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "S": ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    "T": ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    "U": ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    "V": ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    "W": ["10001", "10001", "10001", "10101", "10101", "11011", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    " ": ["00000"] * 7,
}


def pixel_text(s, x, y, px, fill):
    """Draw uppercase text as a 5x7 bitmap. px = size of one pixel."""
    out = []
    cx = x
    for ch in s.upper():
        glyph = FONT.get(ch)
        if glyph:
            for row, bits in enumerate(glyph):
                run = 0
                for col in range(6):
                    on = col < 5 and bits[col] == "1"
                    if on:
                        run += 1
                    elif run:
                        out.append(rect(cx + (col - run) * px, y + row * px, run * px, px, fill))
                        run = 0
        cx += 6 * px
    return out, cx - x - px


def pixel_width(s, px):
    return len(s) * 6 * px - px


# ── candlesticks ─────────────────────────────────────────────────────────────
def candles(x0, y0, cw, ch, n=26, seed=11, pitch=None, body_w=None):
    random.seed(seed)
    pitch = pitch or cw / n
    body_w = body_w or max(pitch - 5, 3)
    price, series = 30.0, []
    for _ in range(n):
        o = price
        c = o + random.uniform(-6, 6) + 2.2
        series.append((o, c, max(o, c) + random.uniform(1, 5), min(o, c) - random.uniform(1, 5)))
        price = c
    lo = min(s[3] for s in series)
    hi = max(s[2] for s in series)

    def yy(v):
        return round(y0 + ch - (v - lo) / (hi - lo) * ch, 1)

    out = []
    for i, (o, c, h, l) in enumerate(series):
        x = x0 + i * pitch
        cx = round(x + body_w / 2, 1)
        col = GREEN if c >= o else RED
        top, bot = min(yy(o), yy(c)), max(yy(o), yy(c))
        out.append(rect(round(cx - 0.6, 1), yy(h), 1.2, round(yy(l) - yy(h), 1), col, extra=' opacity=".45"'))
        out.append(rect(round(x, 1), top, round(body_w, 1), max(round(bot - top, 1), 1.5), col))
    return out


# ── banner ───────────────────────────────────────────────────────────────────
def banner():
    H = 268
    b = [rect(0.5, 0.5, W - 1, H - 1, BG, BORDER)]

    # title bar
    b.append(rect(1, 1, W - 2, 33, PANEL))
    b.append(f'<line x1="1" y1="34" x2="{W - 1}" y2="34" stroke="{BORDER}"/>')
    for i, c in enumerate((RED, AMBER, GREEN)):
        b.append(f'<circle cx="{18 + i * 18}" cy="17.5" r="5.5" fill="{c}"/>')
    b.append(txt(78, 22, "github.com/gottostartsomewhere", 12, MUTED))
    b.append(f'<circle cx="792" cy="17.5" r="3.5" fill="{GREEN}"/>')
    b.append(txt(802, 21.5, "LIVE", 10, GREEN, "700", ls=2))

    # ticker tape
    b.append(rect(1, 35, W - 2, 27, INK))
    b.append(f'<line x1="1" y1="62" x2="{W - 1}" y2="62" stroke="{BORDER}"/>')
    tape = [("OPENBB", "OPEN", AMBER, False), ("EDGARTOOLS", "FILLED", GREEN, True),
            ("YFINANCE", "FILLED", GREEN, True), ("SUPABASE-PY", "FILLED", GREEN, True),
            ("LEDGER-API", "BUILD", CYAN, False)]
    x = 22
    for sym, status, col, up in tape:
        b.append(txt(x, 52.5, sym, 11, MUTED, "600"))
        x += w(sym, 11) + 10
        if up:
            b.append(tri(x + 4, 48.5, 4.5, col))
        else:
            b.append(f'<circle cx="{x + 4}" cy="48.5" r="3.5" fill="{col}"/>')
        x += 14
        b.append(txt(x, 52.5, status, 11, col, "600"))
        x += w(status, 11) + 26

    # left: identity
    b.append(rect(28, 92, 3, 34, GREEN))
    px, _ = pixel_text("JOHN KEVIN", 46, 92, 4, TEXT)
    b += px
    b.append(txt(46, 152, "Backend & fintech engineer  ·  Chennai", 13, MUTED))
    b.append(txt(46, 174, "payments  ·  ledgers  ·  market-data tooling", 12, DIM))
    x = 46
    for lab in ("VIT CHENNAI", "WISEFOLIO", "OPEN SOURCE"):
        s, cw = chip(x, 198, lab, 10, DIM, RULE, "#080c12", 9, 22)
        b.append(s)
        x += cw + 8

    # right: chart
    cx0, cy0, cw0, ch0 = 512, 86, 340, 152
    b.append(rect(cx0 + 0.5, cy0 + 0.5, cw0 - 1, ch0 - 1, INK, BORDER))
    for i in range(1, 4):
        y = round(cy0 + ch0 / 4 * i, 1)
        b.append(f'<line x1="{cx0 + 1}" y1="{y}" x2="{cx0 + cw0 - 1}" y2="{y}" stroke="{RULE}"/>')
    b.append(txt(cx0 + 12, cy0 + 20, "CONTRIB · 12M", 10, DIM, ls=1))
    b += candles(cx0 + 14, cy0 + 30, cw0 - 28, ch0 - 46, n=24)
    return svg(W, H, b, "John Kevin, backend and fintech engineer in Chennai")


# ── section header ───────────────────────────────────────────────────────────
def header(label, color, name):
    H = 40
    half = (W - w(label, 11) - len(label) * 3 - 44) / 2
    b = [rect(0, 0, W, H, BG)]
    b.append(f'<defs><linearGradient id="l"><stop offset="0" stop-color="{BORDER}" stop-opacity="0"/>'
             f'<stop offset="1" stop-color="{BORDER}"/></linearGradient>'
             f'<linearGradient id="r"><stop offset="0" stop-color="{BORDER}"/>'
             f'<stop offset="1" stop-color="{BORDER}" stop-opacity="0"/></linearGradient></defs>')
    b.append(rect(0, 19.5, half, 1, "url(#l)"))
    b.append(rect(W - half, 19.5, half, 1, "url(#r)"))
    b.append(rect(half + 14, 16, 7, 7, color))
    b.append(txt(half + 30, 24, label, 11, color, "700", ls=3))
    return svg(W, H, b, label)


# ── fills blotter ────────────────────────────────────────────────────────────
def blotter():
    rows = [
        ("OpenBB", "NSE market-data extension (obb.nse.*)", "70k", "OPEN", AMBER),
        ("edgartools", "S-3 filing section extraction", "", "FILLED", GREEN),
        ("yfinance", "interval handling fixes", "24k", "FILLED", GREEN),
        ("supabase-py", "PostgREST array filter type coercion", "", "FILLED", GREEN),
    ]
    H = 34 + len(rows) * 42 + 10
    b = [rect(0.5, 0.5, W - 1, H - 1, PANEL, BORDER)]
    b.append(rect(1, 1, W - 2, 32, INK))
    b.append(f'<line x1="1" y1="33" x2="{W - 1}" y2="33" stroke="{BORDER}"/>')
    b.append(txt(24, 21, "REPOSITORY", 10, DIM, "700", ls=2))
    b.append(txt(224, 21, "CONTRIBUTION", 10, DIM, "700", ls=2))
    b.append(txt(700, 21, "STARS", 10, DIM, "700", ls=2))
    b.append(txt(856, 21, "STATUS", 10, DIM, "700", ls=2, anchor="end"))

    y = 33
    for i, (repo, what, stars, status, col) in enumerate(rows):
        cy = y + 27
        if i:
            b.append(f'<line x1="24" y1="{y}" x2="{W - 24}" y2="{y}" stroke="{RULE}" '
                     f'stroke-dasharray="3 4"/>')
        b.append(rect(24, y + 14, 2, 16, col))
        b.append(txt(38, cy, repo, 13, TEXT, "600"))
        b.append(txt(224, cy, what, 13, BODY))
        if stars:
            b.append(star(704, cy - 4, 5, AMBER))
            b.append(txt(716, cy, stars, 12, MUTED))
        cw = w(status, 10) + 20
        b.append(rect(856 - cw, y + 12, cw, 20, "none", col))
        b.append(txt(856 - cw / 2, cy - 0.5, status, 10, col, "700", anchor="middle"))
        y += 42
    return svg(W, H, b, "Merged and open pull requests")


# ── project card ─────────────────────────────────────────────────────────────
def card(repo, subtitle, stack, accent, name):
    H = 104
    b = [rect(0.5, 0.5, W - 1, H - 1, PANEL, BORDER)]
    # corner brackets
    b.append(f'<path d="M1 15 L1 1 L15 1" fill="none" stroke="{accent}" stroke-width="2"/>')
    b.append(f'<path d="M{W - 1} {H - 15} L{W - 1} {H - 1} L{W - 15} {H - 1}" fill="none" '
             f'stroke="{accent}" stroke-width="2"/>')
    b.append(txt(26, 40, repo, 16, TEXT, "700"))
    b.append(txt(26 + w(repo, 16) + 14, 40, "· " + subtitle, 13, MUTED))
    x = 26
    for s in stack:
        sv, cw = chip(x, 58, s, 11, "#9fdcc0", BORDER, "#0a1512", 10, 24)
        b.append(sv)
        x += cw + 7
    b.append(txt(852, 40, "OPEN REPO", 10, accent, "700", ls=2, anchor="end"))
    b.append(f'<path d="M842 54 L852 54 M847 49 L852 54 L847 59" fill="none" stroke="{accent}" '
             f'stroke-width="1.5"/>')
    return svg(W, H, b, name)


# ── instruments ──────────────────────────────────────────────────────────────
def stack_grid():
    rows = [
        ["Python", "TypeScript", "C++", "FastAPI", "Node"],
        ["PostgreSQL", "Redis", "MongoDB", "SQLAlchemy"],
        ["Docker", "AWS", "GitHub Actions", "React", "Next.js"],
    ]
    H = len(rows) * 38 + 10
    b = [rect(0, 0, W, H, BG)]
    y = 8
    for row in rows:
        widths = [w(s, 12) + 24 for s in row]
        total = sum(widths) + 8 * (len(row) - 1)
        x = (W - total) / 2
        for s, cw in zip(row, widths):
            sv, _ = chip(round(x, 1), y, s, 12, "#9fdcc0", BORDER, "#0a1512", 12, 28)
            b.append(sv)
            x += cw + 8
        y += 38
    return svg(W, H, b, "Python, TypeScript, C++, FastAPI, Node, PostgreSQL, Redis, "
                        "MongoDB, SQLAlchemy, Docker, AWS, GitHub Actions, React, Next.js")


# ── footer ───────────────────────────────────────────────────────────────────
def footer():
    H = 52
    line = "risk controls: balances reconcile, retries are idempotent, and the webhook always fires."
    b = [rect(0, 0, W, H, BG)]
    b.append(rect(0, 0.5, W, 1, BORDER))
    b.append(txt(W / 2, 32, line, 11, DIM, anchor="middle"))
    return svg(W, H, b, line)


if __name__ == "__main__":
    write("banner.svg", banner())
    write("hdr-filled.svg", header("FILLED", GREEN, "filled"))
    write("hdr-positions.svg", header("OPEN POSITIONS", CYAN, "positions"))
    write("hdr-instruments.svg", header("INSTRUMENTS", GREEN, "instruments"))
    write("hdr-tape.svg", header("THE TAPE", CYAN, "tape"))
    write("blotter.svg", blotter())
    write("card-ledger.svg", card("ledger-api", "double-entry payment ledger",
                                  ["FastAPI", "Postgres", "Redis"], GREEN, "ledger-api"))
    write("card-cvasacs.svg", card("CVA-SACS", "equity stress-testing engine",
                                   ["Python", "XGBoost", "FinBERT"], CYAN, "CVA-SACS"))
    write("stack.svg", stack_grid())
    write("footer.svg", footer())
