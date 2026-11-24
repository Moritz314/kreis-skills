#!/usr/bin/env python3
"""Erzeugt frame-hoch.svg und frame-quer.svg aus den Maßen und prüft die Proportionen.
Aufruf: python3 bauen.py   (Einheit im SVG: 0,01 mm; 1 pt = 25,4/460*3 /... siehe unten)"""
import re, sys

# --- Maße (Quelle siehe README.md) ---
W_MM, H_MM, D_MM = 78.0, 163.4, 8.75            # Apple Support 125091
PX_W, PX_H, PPI = 1320, 2868, 460                # Apple / useyourloaf
PT_W, PT_H = 440, 956                            # Scale 3x
DISP_R_PT = 62.0                                 # Display-Eckenradius (ScreenCorners, Apple-intern)
ISL_W_PT, ISL_H_PT, ISL_TOP_PT = 125.0, 37.0, 11.0   # Dynamic Island (Gemeinschaftswerte, abgeleitet)

MM_PER_PT = 25.4 / PPI * 3                       # 3 px je pt
DISP_W_MM = PX_W / PPI * 25.4                    # abgeleitet: 72,89 mm
DISP_H_MM = PX_H / PPI * 25.4                    # abgeleitet: 158,37 mm
BEZEL_MM = (W_MM - DISP_W_MM) / 2                # abgeleitet: ~2,55 mm
HOUSE_R_MM = DISP_R_PT * MM_PER_PT + BEZEL_MM    # abgeleitet: ~12,8 mm (Apple veröffentlicht den Wert nicht)
U = 100                                          # SVG-Einheiten je mm

def rrect(x, y, w, h, r):
    return (f"M{x+r:.1f} {y:.1f}H{x+w-r:.1f}A{r:.1f} {r:.1f} 0 0 1 {x+w:.1f} {y+r:.1f}V{y+h-r:.1f}"
            f"A{r:.1f} {r:.1f} 0 0 1 {x+w-r:.1f} {y+h:.1f}H{x+r:.1f}A{r:.1f} {r:.1f} 0 0 1 {x:.1f} {y+h-r:.1f}"
            f"V{y+r:.1f}A{r:.1f} {r:.1f} 0 0 1 {x+r:.1f} {y:.1f}Z")

def svg(quer):
    w, h = (H_MM, W_MM) if quer else (W_MM, H_MM)
    sw, sh = (DISP_H_MM, DISP_W_MM) if quer else (DISP_W_MM, DISP_H_MM)
    sx, sy = (w - sw) / 2, (h - sh) / 2
    iw, ih, it = (x * MM_PER_PT for x in (ISL_W_PT, ISL_H_PT, ISL_TOP_PT))
    if quer:   # Island links, mittig
        ix, iy, irw, irh = sx + it, sy + (sh - iw) / 2, ih, iw
    else:
        ix, iy, irw, irh = sx + (sw - iw) / 2, sy + it, iw, ih
    body = rrect(0, 0, w * U, h * U, HOUSE_R_MM * U)
    hole = rrect(sx * U, sy * U, sw * U, sh * U, DISP_R_PT * MM_PER_PT * U)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w*U:.0f} {h*U:.0f}" width="{w:.1f}mm" height="{h:.1f}mm">\n'
            f'<title>iPhone 17 Pro Max {"quer" if quer else "hoch"}, 1 Einheit = 0,01 mm</title>\n'
            f'<path id="gehaeuse" fill="#2b2b2e" fill-rule="evenodd" d="{body}{hole}"/>\n'
            f'<path id="rand" fill="none" stroke="#6b6b70" stroke-width="30" d="{body}"/>\n'
            f'<rect id="island" x="{ix*U:.1f}" y="{iy*U:.1f}" width="{irw*U:.1f}" height="{irh*U:.1f}" rx="{min(irw,irh)*U/2:.1f}" fill="#000"/>\n</svg>\n')

def pruefe(name, quer):
    """Liest die Maße aus dem fertigen SVG zurück und vergleicht mit den Sollwerten."""
    s = open(name).read()
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', s).group(1).split()]
    isl = re.search(r'id="island" x="[\d.]+" y="[\d.]+" width="([\d.]+)" height="([\d.]+)"', s)
    iw, ih = float(isl.group(1)), float(isl.group(2))
    d = re.search(r'id="gehaeuse"[^>]* d="([^"]+)"', s).group(1)
    hole = d.split("Z")[1]
    m = re.match(r"M([\d.]+) ([\d.]+)H([\d.]+)", hole)
    a, b, c = (float(v) for v in m.groups())
    v = float(re.search(r"V([\d.]+)", hole).group(1))
    r = DISP_R_PT * MM_PER_PT * U
    sw, sh = (c - a) + 2 * r, (v + r) - b
    out = [("Display lang/kurz", max(sw, sh) / min(sw, sh), PX_H / PX_W),
           ("Display Breite in pt", sw / U / MM_PER_PT, PT_H if quer else PT_W),
           ("Gehäuse lang/kurz", max(vb[2], vb[3]) / min(vb[2], vb[3]), H_MM / W_MM),
           ("Island lang/kurz", max(iw, ih) / min(iw, ih), ISL_W_PT / ISL_H_PT)]
    ok = True
    for n, i, so in out:
        dev = abs(i - so) / so * 100
        ok &= dev < 0.5
        print(f"{name}: {n}: ist {i:.4f} soll {so:.4f} Abw {dev:.3f} %")
    return ok

if __name__ == "__main__":
    for q, n in ((False, "frame-hoch.svg"), (True, "frame-quer.svg")):
        open(n, "w").write(svg(q))
    print(f"Display {DISP_W_MM:.2f} x {DISP_H_MM:.2f} mm, Rand {BEZEL_MM:.2f} mm, 1 pt = {MM_PER_PT:.4f} mm, Gehäuse-R {HOUSE_R_MM:.2f} mm")
    ok = pruefe("frame-hoch.svg", False) & pruefe("frame-quer.svg", True)
    print("PROPORTIONEN OK" if ok else "PROPORTIONEN ABWEICHUNG"); sys.exit(0 if ok else 1)
