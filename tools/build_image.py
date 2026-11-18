#!/usr/bin/env python3
"""Composite the 17 November 2026 world-news cover.

Reads assets/base-art.png (AI-generated editorial artwork, no text) and
draws the masthead, the date line and the caption chips with PIL.
Deterministic: identical inputs always produce identical output bytes.

Output: entry.png at the repository root. The file holds PNG bytes when
they fit the 1 MiB cap, otherwise JPEG bytes (the competition tells the
formats apart by their first bytes; the name stays entry.png).

Stage configuration lives in CONFIG below; each submission stage adjusts
it (V1 base composition, V2 storytelling, V3 readability, V4 accuracy,
V5 final polish).
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(ROOT, "assets", "base-art.png")
OUT = os.path.join(ROOT, "entry.png")
W = H = 1024
CAP = 1048576

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

WHITE = (255, 255, 255)
AMBER = (255, 198, 74)
CHIP_FILL = (7, 13, 23, 218)
CHIP_LINE = (255, 255, 255, 72)

CONFIG = dict(
    masthead1="THE WORLD AT A",
    masthead2="TURNING POINT",
    masthead1_size=57,
    masthead2_size=112,
    date_text="TUESDAY, NOVEMBER 17, 2026",
    date_size=45,
    hero_line="HORMUZ: CREW FLEES HIT TANKER, TRAFFIC NEARLY HALTED",
    hero_size=38,
    chips=[
        "HORMUZ STRAIT TRAFFIC AT 8% OF NORMAL",
        "UKRAINE STRIKES CRIMEAN BRIDGE AGAIN",
        "TRUMP MEETS QUAD LEADERS IN MANILA",
        "NVIDIA BEATS AS AI TRADE UNWINDS",
        "CONGO EBOLA PASSES 11,000 CASES",
        "UN: DRONES DRIVE SUDAN CIVILIAN TOLL",
    ],
    chip_size=21,
    band_top=852,
    top_scrim_h=415,
)


def font(path, size):
    return ImageFont.truetype(path, size)


def fit(draw, text, path, size, max_w):
    """Shrink the font until the text fits max_w; return (font, size)."""
    while size > 10:
        f = font(path, size)
        if draw.textlength(text, font=f) <= max_w:
            return f, size
        size -= 2
    return font(path, size), size


def vgrad(base, top, height, max_alpha, dark=(0, 0, 0), upward=False):
    """Paint a vertical black gradient scrim onto an RGBA overlay."""
    ov = Image.new("RGBA", base.size, (0, 0, 0, 0))
    px = ov.load()
    for y in range(top, min(top + height, base.size[1])):
        t = (y - top) / max(1, height - 1)
        a = int(max_alpha * (t if upward else 1 - t))
        for x in range(base.size[0]):
            px[x, y] = dark + (a,)
    return ov


def centered(draw, cx, y, text, f, fill, shadow=True):
    w = draw.textlength(text, font=f)
    x = cx - w / 2
    if shadow:
        draw.text((x, y + 3), text, font=f, fill=(0, 0, 0, 190))
    draw.text((x, y), text, font=f, fill=fill)
    return w


def build(cfg=CONFIG):
    img = Image.open(ART).convert("RGB").resize((W, H), Image.LANCZOS)
    img = img.convert("RGBA")

    # Scrims: top for the masthead, bottom band for the chips.
    img.alpha_composite(vgrad(img, 0, cfg["top_scrim_h"], 205))
    band = Image.new("RGBA", (W, H - cfg["band_top"]), (4, 8, 15, 232))
    img.alpha_composite(band, (0, cfg["band_top"]))

    d = ImageDraw.Draw(img, "RGBA")
    cx = W // 2

    f1, _ = fit(d, cfg["masthead1"], SERIF_B, cfg["masthead1_size"], 900)
    centered(d, cx, 26, cfg["masthead1"], f1, WHITE)
    f2, _ = fit(d, cfg["masthead2"], SERIF_B, cfg["masthead2_size"], 980)
    y2 = 26 + cfg["masthead1_size"] + 16
    centered(d, cx, y2, cfg["masthead2"], f2, WHITE)
    rule_y = y2 + cfg["masthead2_size"] + 22
    d.line([(92, rule_y), (W - 92, rule_y)], fill=AMBER + (255,), width=3)

    fd, _ = fit(d, cfg["date_text"], SANS_B, cfg["date_size"], 940)
    date_y = rule_y + 16
    centered(d, cx, date_y, cfg["date_text"], fd, AMBER + (255,))

    y = date_y + cfg["date_size"] + 14
    if cfg.get("hero_line"):
        d.line([(cx - 62, y + 2), (cx + 62, y + 2)],
               fill=(226, 54, 54, 255), width=4)
        fh, _ = fit(d, cfg["hero_line"], SANS_B, cfg["hero_size"], 960)
        centered(d, cx, y + 12, cfg["hero_line"], fh, WHITE)
        y += cfg["hero_size"] + 22

    # Caption chips: 2 columns x 3 rows inside the bottom band.
    chips = cfg["chips"]
    margin, gap_x, gap_y, chip_h = 24, 16, 9, 46
    chip_w = (W - 2 * margin - gap_x) // 2
    top = cfg["band_top"] + 12
    for i, text in enumerate(chips):
        r, c = divmod(i, 2)
        x0 = margin + c * (chip_w + gap_x)
        y0 = top + r * (chip_h + gap_y)
        d.rounded_rectangle([x0, y0, x0 + chip_w, y0 + chip_h],
                            radius=10, fill=CHIP_FILL, outline=CHIP_LINE,
                            width=1)
        fc, _ = fit(d, text, SANS_B, cfg["chip_size"], chip_w - 22)
        tw = d.textlength(text, font=fc)
        th = fc.size
        d.text((x0 + (chip_w - tw) / 2, y0 + (chip_h - th) / 2 - 1),
               text, font=fc, fill=WHITE + (255,))

    rgb = img.convert("RGB")
    rgb.save(OUT, format="PNG", optimize=True)
    size = os.path.getsize(OUT)
    fmt = "PNG"
    if size > CAP:
        rgb.save(OUT, format="JPEG", quality=88, optimize=True,
                 progressive=False, subsampling=1)
        size = os.path.getsize(OUT)
        fmt = "JPEG"
    print(f"entry.png: {fmt} {size} bytes ({size / CAP:.1%} of cap), "
          f"{rgb.size[0]}x{rgb.size[1]}")
    return OUT


if __name__ == "__main__":
    build()
