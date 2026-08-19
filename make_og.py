# -*- coding: utf-8 -*-
"""Generates public/og.png — the 1200x630 card shown when the link is shared.

Run:  python make_og.py
Only needs rerunning if the name, role or credential row changes.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "public", "og.png")

W, H = 1200, 630
BG = (13, 18, 22)          # ink, the site's darkest surface
ACCENT = (110, 155, 255)   # the dark-theme accent, legible on this ground
INK = (233, 238, 243)
MUTED = (123, 136, 150)
LINE = (36, 46, 57)

FONTS = "C:/Windows/Fonts/"


def font(name, size):
    for candidate in (name, "segoeui.ttf", "arial.ttf"):
        try:
            return ImageFont.truetype(FONTS + candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

f_name = font("segoeuib.ttf", 82)
f_role = font("segoeuib.ttf", 44)
f_body = font("segoeui.ttf", 27)
f_mono = font("consolab.ttf", 20)

PAD = 84

# accent rule, echoing the site's section dividers
d.rectangle([PAD, 96, PAD + 64, 102], fill=ACCENT)

d.text((PAD, 140), "Paulo Carvalho", font=f_name, fill=INK)
d.text((PAD, 246), "Java backend engineer", font=f_role, fill=ACCENT)

d.text((PAD, 330),
       "Eighteen years on backends that cannot afford to fail.",
       font=f_body, fill=MUTED)
d.text((PAD, 368),
       "Integrations, legacy Java upgrades, and the bug nobody can find.",
       font=f_body, fill=MUTED)

d.line([PAD, 452, W - PAD, 452], fill=LINE, width=2)

creds = ["ERICSSON", "ITAÚ", "POLICYMEDICAL", "18 YEARS"]
x = PAD
for i, c in enumerate(creds):
    d.text((x, 486), c, font=f_mono, fill=MUTED if i else INK)
    x += int(d.textlength(c, font=f_mono)) + 26
    if i < len(creds) - 1:
        d.text((x - 17, 486), "·", font=f_mono, fill=LINE)

d.text((PAD, 546), "paulosergiocarvalho.com.br", font=f_mono, fill=ACCENT)

img.save(OUT, "PNG", optimize=True)
print("wrote %s (%d bytes)" % (OUT, os.path.getsize(OUT)))
