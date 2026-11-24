"""Tests of scan_antipatterns.py: the rules for D5, D7, D8, D10, D11, the bundles (Q13) and the `design-ok:` exceptions.

Run: uv run --with pytest pytest skills/arsenal/werkzeuge/test_scan_antipatterns.py
Each new rule has a positive and a negative test; the bundle logic has the steps one feature (P3), two features (P2),
two bundles (P1) and the exception comment.
"""
import importlib.util
import json
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("scan_antipatterns", HERE / "scan_antipatterns.py")
sa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sa)


def run(text: str, name: str = "x.html", abgabe: bool = False):
    """(findings, excused) of one text as if it were a file."""
    sc = sa.Scan(Path(name), text, {})
    sc.run()
    return sa.postprocess([sc], abgabe)


def rules(text: str, name: str = "x.html") -> set[str]:
    found, _ = run(text, name)
    return {x["rule"] for x in found}


def page(css: str = "", body: str = "<h1>Titel</h1>") -> str:
    return (f'<!doctype html><html lang="de"><head><meta name="viewport" content="width=device-width,initial-scale=1">'
            f"<style>{css}</style></head><body>{body}</body></html>")


# ---- D5 linear-easing ------------------------------------------------------------------------------------------
def test_linear_easing_positive():
    assert "linear-easing" in rules(page(".box{transition: transform .3s linear}"))
    assert "linear-easing" in rules(page(".box{animation: slide .4s linear}"))


@pytest.mark.parametrize("css", [
    ".progress{transition: width 1s linear}",
    ".spinner{animation: spin 1s linear infinite}",
    ".menu{transition: visibility 0s linear .2s, opacity .2s cubic-bezier(0,0,0,1)}",
    ".box{transition: transform .3s cubic-bezier(0,0,0,1)}",
    ".bg{background: linear-gradient(red, blue)}",
])
def test_linear_easing_negative(css):
    assert "linear-easing" not in rules(page(css))


# ---- D7 scale-no-origin ----------------------------------------------------------------------------------------
def test_scale_no_origin_positive():
    assert "scale-no-origin" in rules(page(".dropdown{transform: scale(.95); opacity:0}"))
    kf = "@keyframes pop{from{transform:scale(.9)}to{transform:scale(1)}} .modal{animation: pop .2s}"
    assert "scale-no-origin" in rules(page(kf))


@pytest.mark.parametrize("css", [
    ".dropdown{transform: scale(.95); transform-origin: top left}",
    ".dropdown{transform-origin: top right} .dropdown.open{transform: scale(.98)}",
    ".btn:active{transform: scale(.97)}",
    ".dropdown{transform: scale(1)}",
])
def test_scale_no_origin_negative(css):
    assert "scale-no-origin" not in rules(page(css))


# ---- D8 no-tabular-nums ----------------------------------------------------------------------------------------
TABLE = "<table><tr><td>Miete</td><td>1.250,00 €</td></tr><tr><td>Strom</td><td>89,90 €</td></tr></table>"


def test_no_tabular_nums_positive():
    assert "no-tabular-nums" in rules(page("", "<h1>t</h1>" + TABLE))
    assert "no-tabular-nums" in rules(page("", '<h1>t</h1><span class="price">19 €</span><span class="price">29 €</span>'))


def test_no_tabular_nums_negative():
    assert "no-tabular-nums" not in rules(page("td{font-variant-numeric: tabular-nums}", "<h1>t</h1>" + TABLE))
    assert "no-tabular-nums" not in rules(page("", '<h1>t</h1><span class="price">19 €</span>'))  # one number, nothing to compare
    assert "no-tabular-nums" not in rules(page("", "<h1>t</h1><table><tr><td>Name</td><td>Rolle</td></tr></table>"))


# ---- D10 emoji-in-text -----------------------------------------------------------------------------------------
@pytest.mark.parametrize("snippet", [
    "<h1>Los geht's \U0001F680</h1>",
    '<h1>t</h1><button aria-label="Speichern \u2705">S</button>',
    '<h1>t</h1><img src="a.png" alt="\U0001F525 heiß">',
    "<h1>t</h1><p>Achtung \u26a0\ufe0f hier</p>",
    "<h1>t</h1><p>\U0001F1E9\U0001F1EA Deutsch</p>",
    "<h1>t</h1><script>el.textContent = 'fertig \U0001F389';</script>",
])
def test_emoji_positive(snippet):
    assert "emoji-in-text" in rules(page("", snippet))


def test_emoji_in_css_content_and_svg():
    assert "emoji-in-text" in rules(page('.a::before{content:"\U0001F525"}'))
    assert "emoji-in-text" in rules('<svg viewBox="0 0 10 10"><text x="1" y="5">\U0001F600</text></svg>', "icon.svg")
    assert "emoji-in-text" in rules('.a::after{content:"\u2728"}', "a.css")


@pytest.mark.parametrize("snippet", [
    "<h1>Preis 20 € – © 2026 ™</h1>",
    "<h1>t</h1><p>✓ erledigt ✗ offen ★ ➜</p>",   # typographic symbols are not emoji
    "<h1>t</h1><script>console.log('\U0001F680 debug');</script>",
    "<h1>t</h1><p>Käse, Straße, 12:30</p>",
])
def test_emoji_negative(snippet):
    assert "emoji-in-text" not in rules(page("", snippet))


# ---- D11 simple-gradient ---------------------------------------------------------------------------------------
@pytest.mark.parametrize("css", [
    ".hero{background: linear-gradient(135deg, #667eea, #f5576c)}",
    ".btn{background-image: linear-gradient(90deg, #ff7e5f 0%, #feb47b 50%, #3b82f6 100%)}",
    ".card{background: radial-gradient(circle, #0ea5e9, #f43f5e)}",
    ".k{background: linear-gradient(#3b82f6, #ffffff)}",
])
def test_simple_gradient_positive(css):
    assert "simple-gradient" in rules(page(css))


@pytest.mark.parametrize("css", [
    ".bg{background: linear-gradient(#0a0a0f, #12121a)}",                                  # depth: one hue
    ".fade{background: linear-gradient(transparent, #000000)}",                              # fade to transparent
    ".scale{background: linear-gradient(90deg, #e11d48, #f59e0b, #22c55e, #3b82f6)}",       # four stops: a data scale
    ".photo{background: linear-gradient(#000, #fff), url(a.jpg)}",                           # over a photo
    ".m{mask-image: linear-gradient(#000, #fff)}",                                           # mask
    ".stripe{background: repeating-linear-gradient(45deg, #3b82f6, #f43f5e 10px)}",          # stripes: own rule
    ".legend{background: linear-gradient(90deg, #22c55e, #ef4444)}",                         # data legend
])
def test_simple_gradient_negative(css):
    assert "simple-gradient" not in rules(page(css))


def test_simple_gradient_tailwind_and_svg():
    assert "simple-gradient" in rules(page("", '<h1 class="bg-gradient-to-r from-blue-500 to-pink-500">t</h1>'))
    assert "simple-gradient" not in rules(page("", '<h1 class="bg-gradient-to-r from-blue-500 to-blue-700">t</h1>'))
    two = '<svg><defs><linearGradient id="g"><stop offset="0" stop-color="#667eea"/><stop offset="1" stop-color="#f5576c"/></linearGradient></defs></svg>'
    assert "simple-gradient" in rules(two, "g.svg")
    fade = two.replace('stop-color="#f5576c"', 'stop-color="#f5576c" stop-opacity="0"')
    assert "simple-gradient" not in rules(fade, "g.svg")


# ---- cramped-padding, radial-spotlight-glow ----------------------------------------------------------------------
def test_cramped_padding():
    assert "cramped-padding" in rules(page(".card{padding: 6px}"))
    assert "cramped-padding" in rules(page(".panel{padding: 4px 8px}"))
    for css in (".card{padding: 16px}", ".card .row{padding: 7px 0}", ".btn{padding: 4px 8px}", ".card{padding: 0}", ".card{padding: var(--s)}"):
        assert "cramped-padding" not in rules(page(css))


def test_radial_spotlight_glow():
    assert "radial-spotlight-glow" in rules(page("body{background: radial-gradient(circle at 50% 0%, rgba(255,255,255,.15), transparent 60%)}"))
    for css in ("body{background: radial-gradient(circle, #ffffff, #cccccc)}", "body{background: linear-gradient(#fff, transparent)}"):
        assert "radial-spotlight-glow" not in rules(page(css))


# ---- changed severities (Q2, Q3, D4) ---------------------------------------------------------------------------
def sev(text: str, rule: str, name: str = "x.html"):
    return {x["severity"] for x in run(text, name)[0] if x["rule"] == rule}


def test_changed_severities():
    # side-tab was P1 on main: D4 allows it with a named function, so P2 (remove or justify, design-ok: D4), not P3.
    assert sev(page(".c{border-left: 4px solid #3b82f6; padding: 16px}"), "side-tab") == {"P2"}
    assert sev(page(".c{border-left: 4px solid #3b82f6; border-radius: 12px}"), "border-accent-on-rounded") == {"P2"}
    assert sev(page(".g{backdrop-filter: blur(12px)}"), "glassmorphism") == {"P3"}
    assert sev(page(".eyebrow{font-size:12px}"), "kicker-above-heading") == {"P3"}
    assert sev(page("", '<p class="eyebrow">Neu</p><h1>Titel</h1>'), "kicker-above-heading") == {"P3"}


def test_emoji_and_simple_gradient_are_p2():
    # The owner's decision after the P13 check: D10 and D11 must be removed or justified (D2), so they are P2, exit 3.
    assert sev(page("", "<h1>Los \U0001F680</h1>"), "emoji-in-text") == {"P2"}
    assert sev(page(".hero{background: linear-gradient(135deg, #667eea, #f5576c)}"), "simple-gradient") == {"P2"}
    assert sa.RULES["emoji-in-text"][0] == sa.RULES["simple-gradient"][0] == "P2"
    assert sa.RULES["linear-easing"][0] == sa.RULES["no-tabular-nums"][0] == "P3"


def test_svg_is_scanned():
    assert ".svg" in sa.EXTS


def test_collect_takes_svg(tmp_path):
    (tmp_path / "a.svg").write_text("<svg/>")
    (tmp_path / "b.txt").write_text("x")
    assert [p.name for p in sa.collect([str(tmp_path)])] == ["a.svg"]


# ---- bundles (Q13) ---------------------------------------------------------------------------------------------
CREAM = "body{background:#f5f0e8;color:#222}"
SERIF = "h1{font-family:'Fraunces',Georgia,serif}"
TERRA = ":root{--accent:#c8553d}"
NEONCSS = "body{background:#050505} .a{color:#00ff9d;border:1px solid #00ff9d}"
GLOW = ".a{box-shadow:0 0 24px #00ff9d}"


def test_one_feature_is_no_bundle():
    found, _ = run(page(CREAM))
    assert {x["rule"] for x in found} >= {"cream-palette"}
    assert not {"bundle", "bundle-multi"} & {x["rule"] for x in found}
    found, _ = run(page(SERIF))   # one feature without an own rule: only the hint
    assert [x["severity"] for x in found if x["rule"] == "bundle-feature"] == ["P3"]
    assert "bundle" not in {x["rule"] for x in found}


def test_two_features_make_a_p2_bundle():
    found, _ = run(page(CREAM + SERIF))
    b = [x for x in found if x["rule"] == "bundle"]
    assert len(b) == 1 and b[0]["severity"] == "P2" and "Creme-Look" in b[0]["hint"]
    assert "bundle-multi" not in {x["rule"] for x in found}


def test_two_bundles_make_p1():
    found, _ = run(page(CREAM + SERIF + NEONCSS + GLOW))
    r = {x["rule"]: x for x in found}
    assert r["bundle-multi"]["severity"] == "P1"
    assert "Creme-Look" in r["bundle-multi"]["hint"] and "Neon-Dunkel" in r["bundle-multi"]["hint"]
    assert sum(1 for x in found if x["rule"] == "bundle") == 2


def test_p1_changes_exit_code(tmp_path):
    f = tmp_path / "a.html"
    f.write_text(page(CREAM + SERIF + NEONCSS + GLOW))
    assert sa.main([str(f), "--min", "P1"]) == 1
    g = tmp_path / "b.html"
    g.write_text(page(CREAM + SERIF))
    assert sa.main([str(g), "--min", "P1"]) == 0
    assert sa.main([str(g)]) == 3


@pytest.mark.parametrize("css, body, name", [
    (CREAM + TERRA, "<h1>t</h1>", "Creme-Look"),
    ("body{background:#050505} .a{color:#00ff9d;border-color:#00e5ff}", "<h1>t</h1>", "Neon-Dunkel"),
    (".r{border-top:1px solid #000}.s{border-bottom:1px solid #000}.t{border-top:1px solid #000}.u{border-bottom:1px solid #000}"
     ".l{text-transform:uppercase;letter-spacing:.12em;font-size:11px}.m{text-transform:uppercase;letter-spacing:.1em;font-size:12px}",
     "<h1>t</h1>", "Zeitungs-Look"),
    (".a{box-shadow:6px 6px 0 #000} h1{font-weight:900} h2{font-weight:800}", "<h1>t</h1>", "Kasten-Look"),
    ("", '<div><h1>Titel</h1><div class="actions"><a class="btn primary">A</a><a class="btn">B</a></div></div>'
         '<p class="eyebrow">Neu</p><h1>x</h1>', "SaaS-Hero"),
    (".a{border:1px solid #ddd;box-shadow:0 10px 40px rgba(0,0,0,.1)} "
     + "".join(f".c{i}{{border-radius:16px}}" for i in range(5)), "<h1>t</h1>", "Kartenvorlage"),
    ("", "<h1>Wir sind nahtlos und ganzheitlich</h1><p>Nicht Software, sondern Wirkung. Nicht Lärm, sondern Ruhe.</p>", "Textmuster"),
])
def test_each_bundle_is_found(css, body, name):
    found, _ = run(page(css, body))
    hits = [x for x in found if x["rule"] == "bundle"]
    assert any(name in x["hint"] for x in hits), [x["hint"] for x in found]


def test_bundle_over_css_and_html_file_only_with_abgabe(tmp_path):
    css = sa.Scan(Path("style.css"), CREAM, {})
    css.run()
    html = sa.Scan(Path("index.html"), page("", "<h1>t</h1>") .replace("<style></style>", "<style>" + SERIF + "</style>"), {})
    html.run()
    per_file, _ = sa.postprocess([css, html], False)
    together, _ = sa.postprocess([css, html], True)
    assert "bundle" not in {x["rule"] for x in per_file}
    assert "bundle" in {x["rule"] for x in together}


# ---- design-ok -------------------------------------------------------------------------------------------------
def test_design_ok_excuses_bundle():
    css = "/* design-ok: Q13 Creme und Serif kommen aus der Marke des Kunden */" + CREAM + SERIF
    found, excused = run(page(css))
    assert not {"bundle", "cream-palette"} & {x["rule"] for x in found}
    assert {"bundle", "cream-palette"} <= {x["rule"] for x in excused}
    assert all(x["excuse"] == "Q13" and "Marke" in x["reason"] for x in excused)


def test_design_ok_excuses_question_rules_only():
    html = page(".g{backdrop-filter: blur(8px)}", '<p class="eyebrow">Kapitel 3</p><h1>t</h1>') \
        .replace("<body>", "<body><!-- design-ok: Q3 Zeile trägt die Kapitelnummer -->")
    found, excused = run(html)
    assert "kicker-above-heading" not in {x["rule"] for x in found}
    assert "kicker-above-heading" in {x["rule"] for x in excused}
    assert "glassmorphism" in {x["rule"] for x in found}          # Q2 is not excused by Q3


def test_design_ok_does_not_excuse_hard_rules():
    html = page("", "<h1>Hallo \U0001F680</h1>").replace("<body>", "<body><!-- design-ok: Q10 Marke will es so, sagt der Kunde -->")
    found, excused = run(html)
    assert "emoji-in-text" in {x["rule"] for x in found} and not excused
    css = "/* design-ok: Q13 bewusst gewählt vom Auftrag */ .h{background: linear-gradient(135deg,#667eea,#f5576c)}"
    assert "simple-gradient" in {x["rule"] for x in run(page(css))[0]}


def test_design_ok_needs_reason_and_number():
    for c in ("/* design-ok: Q3 */", "/* design-ok: Q3 kurz */", "/* design-ok: weil ich es will */", "/* design-ok: Q16 zu hohe Nummer, wirklich */"):
        found, excused = run(page(c + ".eyebrow{font-size:12px}"))
        assert "design-ok-no-reason" in {x["rule"] for x in found}, c
        assert "kicker-above-heading" in {x["rule"] for x in found}
        assert not excused


def test_design_ok_d4_for_side_tab():
    css = ".c{border-left: 4px solid #3b82f6; padding:16px} /* design-ok: D4 Randstreifen zeigt den Status der Zeile */"
    found, excused = run(page(css))
    assert "side-tab" not in {x["rule"] for x in found}
    assert "side-tab" in {x["rule"] for x in excused}


def test_json_output_has_excused(tmp_path, capsys):
    f = tmp_path / "a.html"
    f.write_text(page("/* design-ok: Q13 Marke des Kunden schreibt beides vor */" + CREAM + SERIF))
    sa.main([str(f), "--json"])
    data = json.loads(capsys.readouterr().out)
    assert data["excused_count"] >= 2 and data["counts"]["P2"] == 0
    assert {x["excuse"] for x in data["excused"]} == {"Q13"}


# ---- list and header --------------------------------------------------------------------------------------------
def test_list_and_docstring_know_every_rule():
    doc = sa.__doc__
    for rid in sa.RULES:
        assert f"  {rid} " in doc, rid
    assert sa.RULES["glassmorphism"][0] == sa.RULES["kicker-above-heading"][0] == "P3"
    assert sa.RULES["side-tab"][0] == sa.RULES["border-accent-on-rounded"][0] == "P2"
    assert sa.RULES["bundle"][0] == "P2" and sa.RULES["bundle-multi"][0] == "P1"


def test_new_rules_are_marked_with_their_number():
    for rid, nr in (("linear-easing", "D5"), ("scale-no-origin", "D7"), ("no-tabular-nums", "D8"),
                    ("emoji-in-text", "D10"), ("simple-gradient", "D11"), ("bundle", "Q13")):
        assert nr in sa.RULES[rid][2], rid


# ---- Regeln der Durchsicht vom 2026-11-20 (Vercel-Leitfaden, 4.6.0-Skill): one hit and one non-hit each -----------------------
def head(extra: str = "", css: str = "", fit: bool = False) -> str:
    vp = "width=device-width,initial-scale=1" + (",viewport-fit=cover" if fit else "")
    return (f'<!doctype html><html lang="de"><head><meta name="viewport" content="{vp}">'
            f'<meta name="theme-color" content="#fff"><style>:root{{color-scheme:light dark}}{css}</style>'
            f"</head><body><h1>Titel</h1>{extra}</body></html>")


NEW_RULES = [
    ("paste-blocked", '<input name="a" onpaste="event.preventDefault()">', '<input name="a" onpaste="log()">'),
    ("field-attrs-missing", '<input type="text" aria-label="Betreff">', '<input type="text" name="betreff" aria-label="Betreff">'),
    ("autofocus", '<input name="a" aria-label="A" autofocus>', '<input name="a" aria-label="A">'),
    ("no-intl-format", "<script>const m = d.getMonth() + 1;</script>", "<script>new Intl.DateTimeFormat('de').format(d)</script>"),
    ("img-no-lazy", "".join(f'<img src="{i}.webp" alt="a" width="9" height="9">' for i in range(5)),
     "".join(f'<img src="{i}.webp" alt="a" width="9" height="9"{"" if i < 3 else " loading=lazy"}>' for i in range(5))),
    ("hero-img-lazy", '<section class="hero"><img src="h.webp" alt="h" loading="lazy"></section>',
     '<section class="hero"><img src="h.webp" alt="h" fetchpriority="high"></section>'),
    ("video-autoplay-attrs", '<video autoplay muted loop src="v.mp4"></video>', '<video autoplay muted loop playsinline src="v.mp4"></video>'),
    ("gif-image", '<img src="a.gif" alt="a" width="9" height="9">', '<img src="a.webp" alt="a" width="9" height="9">'),
    ("will-change-static", None, None),
    ("viewport-fit-missing", None, None),
    ("anchor-under-fixed-bar", None, None),
    ("icon-no-aria-hidden", '<button aria-label="x"><svg viewBox="0 0 24 24"><path d="M0 0"/></svg></button>',
     '<button aria-label="x"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M0 0"/></svg></button>'),
    ("onclick-navigation", '<button onclick="location.href=\'/x\'">Weiter</button>', '<button onclick="open()">Weiter</button>'),
]


@pytest.mark.parametrize("rule,pos,neg", [r for r in NEW_RULES if r[1] is not None], ids=lambda v: v if isinstance(v, str) and v.islower() else "")
def test_new_rule_positive_and_negative(rule, pos, neg):
    assert rule in rules(head(pos)), rule
    assert rule not in rules(head(neg)), rule


def test_will_change_static():
    assert "will-change-static" in rules(head(css="*{will-change:transform}"))
    assert "will-change-static" not in rules(head(css=".card:hover{will-change:transform}.hero{will-change:opacity}"))


def test_viewport_fit_missing():
    css = ".bar{padding-bottom:env(safe-area-inset-bottom)}"
    assert "viewport-fit-missing" in rules(head(css=css))
    assert "viewport-fit-missing" not in rules(head(css=css, fit=True))


def test_anchor_under_fixed_bar():
    body = '<a href="#kontakt">K</a><section id="kontakt">x</section>'
    css = "header{position:fixed;top:0}"
    assert "anchor-under-fixed-bar" in rules(head(body, css))
    assert "anchor-under-fixed-bar" not in rules(head(body, css + "section{scroll-margin-top:80px}"))


def test_theme_color_and_color_scheme():
    bare = '<!doctype html><html lang="de"><head><meta name="viewport" content="width=device-width,initial-scale=1"></head><body><h1>T</h1></body></html>'
    r = rules(bare)
    assert "theme-color-missing" in r and "color-scheme-missing" in r
    assert not ({"theme-color-missing", "color-scheme-missing"} & rules(head()))


def test_font_display_missing():
    assert "font-display-missing" in rules("@font-face{font-family:A;src:url(a.woff2)}", "x.css")
    assert "font-display-missing" not in rules("@font-face{font-family:A;src:url(a.woff2);font-display:swap}", "x.css")


def test_no_intl_format_in_js_file():
    assert "no-intl-format" in rules("const t = price.toFixed(2) + ' €';", "x.js")
    assert "no-intl-format" not in rules("const t = new Intl.NumberFormat('de-DE').format(price);", "x.js")


def test_paste_and_field_in_jsx():
    assert "paste-blocked" in rules('<input name="p" onPaste={(e) => e.preventDefault()} />', "x.jsx")
    assert "field-attrs-missing" not in rules('<input type="email" name="m" autoComplete="email" {...rest} />', "x.jsx")


def test_new_rules_registered_in_list():
    for r in ("paste-blocked", "field-attrs-missing", "autofocus", "no-intl-format", "img-no-lazy", "hero-img-lazy",
              "video-autoplay-attrs", "gif-image", "will-change-static", "color-scheme-missing", "theme-color-missing",
              "viewport-fit-missing", "anchor-under-fixed-bar", "font-display-missing", "icon-no-aria-hidden",
              "onclick-navigation"):
        assert r in sa.RULES and sa.RULES[r][0] in ("P1", "P2", "P3")


def test_onclick_navigation_in_jsx():
    assert "onclick-navigation" in rules("<button onClick={() => router.push('/x')}>Weiter</button>", "x.jsx")
    assert "onclick-navigation" not in rules("<a href=\"/x\" onClick={() => router.push('/x')}>Weiter</a>", "x.jsx")
    assert "onclick-navigation" not in rules("<button onClick={() => setOpen(true)}>Weiter</button>", "x.jsx")
