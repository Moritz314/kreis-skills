#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright"]
# ///
"""Aufruf: attrappe.py shot <url> <out.png> [--quer] [--nur-display]
Rendert die Seite in der iPhone-17-Pro-Max-Attrappe (Rahmen + Island) oder nur das Display (440x956, quer 956x440, Faktor 3 -> 1320x2868).
Die Seite läuft direkt im Display-Viewport (nicht im iframe), damit env(safe-area-inset-*) per CSS-Variablen simuliert werden kann
und Scroll/Touch echt sind; der Rahmen wird danach darübergelegt."""
import sys, pathlib, base64
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
def main():
    a = sys.argv[1:]
    if len(a) < 3 or a[0] != "shot": sys.exit(__doc__)
    url, out = a[1], a[2]; quer = "--quer" in a; nur = "--nur-display" in a
    vw, vh = (956, 440) if quer else (440, 956)
    sa = (20, 62, 20, 62) if quer else (62, 0, 34, 0)      # oben, rechts, unten, links
    css = f":root{{--sat:{sa[0]}px;--sar:{sa[1]}px;--sab:{sa[2]}px;--sal:{sa[3]}px}}"
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": vw, "height": vh}, device_scale_factor=3, is_mobile=True, has_touch=True,
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 26_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Mobile/15E148 Safari/604.1")
        ctx.add_init_script("document.addEventListener('DOMContentLoaded',()=>{const s=document.createElement('style');s.textContent=%r;document.head.appendChild(s)})" % css)
        pg = ctx.new_page(); pg.goto(url, wait_until="networkidle", timeout=60000); pg.wait_for_timeout(800)
        if nur: pg.screenshot(path=out); b.close(); return
        shot = base64.b64encode(pg.screenshot()).decode()
        # Rahmen darüberlegen: Seite als Bild im Display, Rahmen (SVG) darüber
        hull = HERE / ("frame-quer.svg" if quer else "frame-hoch.svg")
        s = 6.0362; W, H = (163.4, 78) if quer else (78, 163.4)
        dp = b.new_context(viewport={"width": round(W * s), "height": round(H * s)}, device_scale_factor=3).new_page()
        svg64 = base64.b64encode(hull.read_bytes()).decode()
        dp.set_content(f'<body style="margin:0;background:#e9e9ec"><div style="position:relative;width:{W*s}px;height:{H*s}px">'
            f'<img src="data:image/png;base64,{shot}" style="position:absolute;left:{(W-(158.36 if quer else 72.891))/2*s}px;top:{(H-(72.891 if quer else 158.36))/2*s}px;width:{vw}px;height:{vh}px;border-radius:62px">'
            f'<img src="data:image/svg+xml;base64,{svg64}" style="position:absolute;inset:0;width:100%;height:100%"></div>')
        dp.wait_for_timeout(300); dp.screenshot(path=out); b.close()
main()
