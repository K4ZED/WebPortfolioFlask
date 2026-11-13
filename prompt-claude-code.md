# Task

This folder is my existing portfolio website (live at https://portfolio-kazed.my.id/, Flask-based). Replace its homepage with a new design: a personal portfolio one-pager for **Kenza Athallah**.

Follow the **Design & Motion Spec** at the bottom of this file exactly for layout, CSS values, fonts, colors and animation. That spec was written for an invented persona ("Marcus Vane"). **Ignore all of its copy, names, numbers and asset URLs.** Use only the content in the **Content** section below. If the two conflict, Content wins.

Before writing anything:
1. Explore the project and tell me how it's structured (app entry, routes, templates, static folders, deploy config).
2. Back up the current homepage template (e.g. rename to `index_old.html`) instead of deleting it.
3. Propose where the new page goes so the `/` route serves it, and wait for my OK before changing routes or deploy config.

Integration:
- Keep the existing `static/img/` and `static/cv/` files. Reference them with local paths (`url_for('static', ...)` if it's a Jinja template, or `/static/...`) instead of the full https://portfolio-kazed.my.id URLs listed below.
- The page itself stays self-contained: its CSS and JS inline in the one template. If it's a Jinja template, make sure `{{ }}` / `{% %}` in the JS (template literals with `${}` are fine) don't clash with Jinja; wrap scripts in `{% raw %}` where needed.
- Don't touch other routes or pages unless I ask.

Rules:
- Pure HTML + CSS + JS in one page (one template). No framework, no build step, no npm. Lenis via CDN importmap.
- Do not use em dashes (—) anywhere in the visible text. Keep copy short and natural.
- When done, run the app locally, open the homepage in a browser preview and check the hero, the preloader and mobile width (360px). Fix anything that overflows.

---

## Content

**Name:** Kenza Athallah (hero line 1: `Kenza`, line 2: `Athallah`). Monogram: `KA`. Footer copyright: `© 2026 Kenza Athallah. All rights reserved.`
The surname is longer than the spec's, so make sure the hero name fits on mobile (shrink the mobile font-size if needed).

**Nav:** About → #story, Projects → #ventures, Impact → #impact, Clients → #voices, Contact → #contact

**Hero**
- Role lines: `Data Analyst`, `Data Science`, `Backend Dev`, `Designer`
- Description: "Data Science student at Universitas Sebelas Maret, based in Sukoharjo. I turn raw data into models, dashboards and backends people can actually use."
- Portrait: use an `<img>` (no video): `https://portfolio-kazed.my.id/static/img/Ken.png`, bare LiquidImage mode.

**Marquee words:** Data Analysis, Machine Learning, Backend Development, Data Visualization, Graphic Design

**About (spec's Story section)**
- Eyebrow: `About`
- Heading: "Five years of code, data and design."
- Body: "I started in tech in 2020 at SMK Telkom Malang, studying software engineering. Since then I've worked as a data analyst at Telkom and Amigo Group, designed for brands as a freelancer, and now study Data Science at UNS. Right now I'm focused on machine learning, backend development, data visualization and cloud."
- The 4 numbered items are experience:
  - 01 Data Analyst Intern: Amigo Group, MBKM program. 2026 to present.
  - 02 Campus Ambassador: MySkill. Feb 2026 to May 2026.
  - 03 Freelance Graphic Designer: CV. Dharma Syafa Kreasi. Jun 2024 to Jul 2025.
  - 04 Telecom Data Analyst Intern: Telkom Landmark Surabaya. Jul 2022 to Dec 2022.

**Projects (spec's Ventures section)**
- Eyebrow: `Selected Projects`, heading: "Things I've built.", right label: `8+ / Projects`
- Cards (name / category / tech / tag / blurb / link):
  1. Sentiment Analysis / Machine Learning, NLP / Deep Learning / NLP / Classifying sentiment in text with a deep learning model, from preprocessing to evaluation. / none
  2. BTS Performance Monitoring / Data Analytics / Telecom / Analysis / Monitoring and analyzing BTS network performance data to spot issues early. / none
  3. ML with Flask / Machine Learning, Web / Scikit-learn, Jinja2 / Live Demo / A machine learning model served through a Flask web app. / https://waows-6-ken-day2.vercel.app/
  4. P!NGFEST / Web, Event / Laravel, Blade / UNS / Event website for Pekan Teknologi UNS. / none
- No project images yet: the LiquidImage shows the branded radial placeholder with the project name in the display font (large, centered). Leave an easy spot to drop in images later.
- If a link exists, the tag becomes a link with ↗ that opens in a new tab.

**Impact**
- Heading: "Five years, measured."
- Stats: `5+` Years in tech · `2` Data analyst internships · `8+` Projects built · `3` Best Project Awards

**Clients (spec's Voices section, same interaction)**
- Eyebrow: `Clients`, heading: "Who I've designed for."
- Items (text / name / sector / logo):
  1. Visual assets for events, built to look good on a poster and on a phone screen. / Wonderland / Entertainment & Events / https://portfolio-kazed.my.id/static/img/Wonderland.png
  2. Promotional and branding materials for retail and supermarket campaigns. / Luwes Group / Retail & Supermarket / https://portfolio-kazed.my.id/static/img/Luwes%20Group.png
  3. Visual content for apparel branding, keeping the look consistent across every drop. / Cardinal / Fashion & Apparel / https://portfolio-kazed.my.id/static/img/Cardinal.png
- No curly quotes around the text. Footer line: `Name / Sector`. Logos use `object-fit:contain` with some padding.

**Contact**
- Eyebrow: `Let's Talk`, heading: "Got data that needs to make sense?"
- Body: "I'm open to internships, freelance work and collaborations. Send me a message and I'll get back to you."
- Email: kenzaathallah.wijaya@gmail.com
- Signature tagline: `Designed & built by Kazed.`
- Links: GitHub → https://github.com/K4ZED · LinkedIn → https://linkedin.com/in/kenzaathallah · Download CV → https://portfolio-kazed.my.id/static/cv/CV_Kenza_ENG.pdf

---

# Design & Motion Spec (reference only, replace its content with the above)

# Recreate this site as a single HTML file: Marcus Vane

Build a **single, self-contained `index.html`** that reproduces the site described below — the same visual result and the same motion. Pure HTML + CSS + JavaScript only. **No build step, no framework, no bundler, no npm.** Use ES modules with CDN `importmap`s where a library is needed (only Lenis is required; GSAP is optional). Hardcode every value — copy, colors, sizes, timings — directly into the file. Do not add a CMS, a config object, or any "control panel." Faithfulness to the original beats brevity; reproduce the markup, the verbatim copy, the exact CSS values, and the motion feel.

The original is a Next.js 16 / React 19 project using Tailwind v4, `@react-spring/web`, the `spring-text-engine` library, and Lenis smooth scroll. You are translating all of that into one plain HTML file. Drop every piece of framework plumbing (routing, zustand, zod, env, SEO/sitemap/robots, bot detection, cookie banner, dev tooling). Keep everything that defines the look and the motion.

---

## What it is

A cinematic, dark-mode founder / portfolio **one-pager** for an invented persona, **Marcus Vane** (Founder · Investor · Operator). The signature move is the hero: a giant two-line accent-red surname rendered in a tall, heavy condensed display face, with the founder's portrait composited in front of it, bleeding off the bottom of the screen. Type is bold and stacked; everything reveals with spring-based motion — letter-by-letter and line-by-line text reveals, staggered section entrances on scroll, an infinite marquee — over near-black, all riding on Lenis smooth scroll. The layout is rem-based and scales proportionally with the viewport.

---

## Page shell & libraries

**Fonts (load from Google Fonts):**
- **Display face:** the original uses **Anton** (Google Fonts) — a tall, heavy, condensed grotesque used as the free analog of "Right Grotesk Tall Bold." Use it for the hero name, all section headings, the marquee words, the preloader, the stat figures, and footer signature. Weight 400 only (Anton ships a single weight).
- **Body / sans face:** the original uses **Onest** (Google Fonts). Use it for body copy, principle titles, venture/voice names, the email link, and nav labels.
- Load via: `<link href="https://fonts.googleapis.com/css2?family=Anton&family=Onest:wght@400;500;600&display=swap" rel="stylesheet">` (preconnect to `fonts.googleapis.com` and `fonts.gstatic.com`).
- CSS variables: `--font-display: "Anton", sans-serif;` and `--font-sans: "Onest", sans-serif;`.

**CSS reset:** minimal reset — `*{margin:0;padding:0;box-sizing:border-box}`, `img,video{display:block;max-width:100%}`, lists reset, buttons/links inherit font and reset appearance.

**Dark background:** `body { background:#08080a; color:#f3f1ea; font-family:var(--font-sans); -webkit-font-smoothing:antialiased; text-rendering:optimizeLegibility; overflow-x:hidden; }`. Set the same background on `html`.

**`::selection`** → `background:#ff3b1d; color:#08080a;`.

**Rem-based adaptive grid (critical — this is how the whole layout scales).** The design is authored in `rem` against a 1920px base where the root font-size is 16px. The root font-size is driven by viewport width so the rem layout stays proportional. Reproduce exactly with CSS media queries on `html` (largest first), plus a JS scale-up above 1920px:

```css
html { font-size: 16px; background:#08080a; }
@media (max-width:1920px){ html{ font-size:0.833333vw; } }  /* 16*100/1920 */
@media (max-width:1440px){ html{ font-size:1.111111vw; } }  /* 16*100/1440 */
@media (max-width:1024px){ html{ font-size:1.5625vw;   } }  /* 16*100/1024 */
@media (max-width:640px){
  html{ font-size:4.444444vw; }                            /* 16*100/360  */
  :root{ --gutter:16px; }                                  /* fixed px gutter on phones */
}
```

Above 1920px, scale the root font-size up proportionally (damped) with JS, recomputed on resize:

```js
const FONT_BASE = 16, BASE_W = 1920, COEF = 0.6666;
function applyAdaptiveGrid(){
  const w = window.innerWidth;
  const reduction = ((BASE_W - w) / BASE_W) * 100 * COEF;
  const size = FONT_BASE - (FONT_BASE * reduction) / 100;
  if (size > FONT_BASE) document.documentElement.style.fontSize = size + "px";
  else document.documentElement.style.removeProperty("font-size"); // let the vw queries drive
}
applyAdaptiveGrid();
addEventListener("resize", applyAdaptiveGrid);
```

**Lenis smooth scroll (load from CDN).** Use an importmap and run the RAF loop. The preloader stops Lenis while loading, then starts it after the wipe (see Motion):

```html
<script type="importmap">
{ "imports": { "lenis": "https://cdn.jsdelivr.net/npm/lenis@1.3.19/dist/lenis.mjs" } }
</script>
<script type="module">
  import Lenis from "lenis";
  const lenis = new Lenis({ smoothWheel: true });
  window.lenis = lenis;
  function raf(t){ lenis.raf(t); requestAnimationFrame(raf); }
  requestAnimationFrame(raf);
  // expose lenis.stop() / lenis.start() to the preloader
</script>
```
Also pull Lenis's stylesheet behavior in by adding the recommended html/lenis classes, or just leave native scroll and let Lenis drive `transform`. Anchor links (`#story`, etc.) should scroll smoothly — intercept clicks on nav anchors and call `lenis.scrollTo(targetEl)`.

**Springs:** there is no react-spring at runtime. Reproduce the spring *feel* with vanilla JS + CSS. You may optionally load **GSAP from CDN** for the text reveals; otherwise hand-roll with `requestAnimationFrame` and CSS `transition`/`@keyframes`. Concrete equivalents for every spring config are given in **Motion system** below — bake those in.

**Reduced motion:** wrap a `@media (prefers-reduced-motion: reduce)` that disables the preloader (jump straight to the page), the marquee animation, and all entrance transitions (show final state immediately).

---

## Layout & sections (in order)

The page is: **Preloader → SiteNav (fixed) → main { Hero → Marquee → Story → Ventures → Impact → Voices → ContactFooter } **. `main` is `position:relative; width:100%; overflow-x:hidden;`.

Shared tokens (use as CSS variables):
- `--background:#08080a` `--foreground:#f3f1ea` `--surface:#111114` `--surface-2:#17171b`
- `--muted:#807f78` `--line:rgba(243,241,234,0.1)` `--line-strong:rgba(243,241,234,0.22)`
- `--accent:#ff3b1d` `--accent-2:#ff6a3d`
- `--gutter:2.5rem` (page side padding; overridden to `16px` ≤640px) · `--section:9rem` (vertical section padding)

Type scale (all `rem`, with line-heights):
- hero `28rem`/lh `0.78` · mega `13rem`/lh `0.86` · display `7.5rem`/lh `0.9` · h1 `5rem`/lh `0.95` · h2 `3.25rem`/lh `1` · h3 `1.75rem`/lh `1.15` · lead `1.375rem`/lh `1.45` · body `1.0625rem`/lh `1.6` · eyebrow `0.8125rem`/lh `1.2`.

Breakpoints used (min-width unless noted): `sm` 640px, `md` 768px, `lg` 1024px. Original is Tailwind, so `sm:` = `@media (min-width:640px)`, etc.

A reusable **Eyebrow** label appears above most section headings: a flex row, `gap:0.75rem`, `font-size:eyebrow`, `font-weight:500`, `text-transform:uppercase`, `letter-spacing:0.22em`, `color:var(--muted)`, preceded by a `0.5rem` (`size-2`) accent-red filled dot (`border-radius:9999px; background:var(--accent)`).

### 1) Preloader
Full-screen cinematic intro. Fixed, `inset:0`, `z-index:100`. Background `--background` (use an absolute `inset:0; z-index:-10; background:var(--background)` layer behind content, matching original). Layout: a flex container, `padding:var(--gutter)`. On phones it's `flex-direction:column; align-items:flex-start; justify-content:flex-end; gap:0.75rem`; at `sm` it becomes `flex-direction:row; align-items:flex-end; justify-content:space-between; gap:1rem`.

Contents:
- Brand label (bottom-left): text **`Marcus Vane`**, `font-family:display; font-size:h3; text-transform:uppercase; line-height:1; letter-spacing:-0.01em` (tight). `color:--foreground`.
- A big counter (bottom-right): `font-family:display; font-size:display; line-height:1; font-variant-numeric:tabular-nums; color:--foreground`. Shows a number counting **0 → 100** followed by a `%` in **accent red** (`color:var(--accent)`).

Behavior: on load, lock scroll (`lenis.stop()`, `window.scrollTo(0,0)`). Spring the counter 0→100 over **2000ms** (linear-ish), rounding to integer each frame. When it reaches 100, fade out both labels (opacity → 0 over ~300ms), then after a **200ms** delay **wipe the whole preloader upward** (`translateY(0 → -100%)`) with the spring timing in Motion (≈600–700ms, ease-out). When the wipe finishes, `lenis.start()` (re-enable scroll). Set `pointer-events:none` and `aria-hidden` once done.

### 2) SiteNav (fixed top)
`<header>` fixed, `inset-inline:0; top:0; z-index:50; pointer-events:none`. Inner `<nav>`: `pointer-events:auto`, flex, `align-items:center; justify-content:space-between`, `padding:1.5rem var(--gutter)` (`py-6 px-gutter`).

- **Logo (left):** anchor to `#top`, flex row `gap:0.75rem`. A monogram **`MV`** in a circular outlined badge: `display:grid; place-items:center; width/height:2.5rem (size-10); border-radius:9999px; border:1px solid var(--line-strong); font-weight:600; letter-spacing:-0.01em`. Next to it (hidden below `sm`): the name **`Marcus Vane`**, `font-size:eyebrow; font-weight:500; uppercase; letter-spacing:0.22em; color:var(--muted)`.
- **Desktop links (≥md):** a horizontal `<ul>`, `gap:2.5rem`. Each link: `font-size:eyebrow; font-weight:500; uppercase; letter-spacing:0.18em; color:var(--muted)`; on hover → `color:var(--foreground)` and an accent underline grows from width 0 to full (`position:absolute; bottom:-0.25rem; left:0; height:1px; background:var(--accent); width:0 → 100% on hover`).
  Links (label → href): **Story → #story**, **Ventures → #ventures**, **Impact → #impact**, **Voices → #voices**, **Contact → #contact**.
- **Burger (mobile, <md):** a button, `size-10`, three `0.5px`-ish bars (`height:0.125rem; width:1.5rem; background:var(--foreground)`, `gap:0.375rem`). Open state animates to an X (top bar `translateY(0.5rem) rotate(45deg)`, middle `opacity:0`, bottom `translateY(-0.5rem) rotate(-45deg)`).
- **Mobile menu panel (<md):** fixed `inset:0; z-index:50; background:var(--background)`, flex column centered, `padding-inline:var(--gutter)`. Fades in (opacity spring, tension 210 / friction 28 → ~450ms ease-out). Links render as a vertical list; each link is `font-family:display; font-size:h2; uppercase; line-height:1; letter-spacing:-0.01em` and reveals with a **staggered upward slide** (each item `translateY(48px → 0)`, opacity 0→1) — trail delay ~120ms before the first, stagger handled via per-item delays (see Motion: useTrail equivalent). Clicking a link closes the menu.

### 3) Hero
`<section id="top">`, `position:relative; display:flex; flex-direction:column; min-height:100svh; overflow:hidden`.

- **Top row** (`z-index:30`): flex, `padding:7rem var(--gutter) 0` (≈`pt-28`; `pt-32`=8rem at sm). Below `sm`: column, `gap:2rem`. At `sm`: `flex-direction:row; align-items:flex-start; justify-content:space-between`.
  - **Left — role words** as an `<h2>`: `font-family:display; uppercase; line-height:1.05; letter-spacing:-0.01em; color:var(--foreground); font-size:h3` (→ `h2` at sm). Four stacked words, each its own block line, revealed line-by-line with an upward slide (see Motion): **Founder**, **Investor**, **Operator**, **Contrarian**.
  - **Right — description** `<p>`: `max-width:26rem; font-size:body; color:var(--muted)`; at `sm` `text-align:right`. Verbatim:
    > I start companies that shouldn't be possible — then make them inevitable. Four exits, one playbook: conviction before consensus.
    Fades + slides up (opacity 0→1, y 16→0) after the name reveal.
- **Portrait column** (`z-index:20`, `pointer-events:none` on the wrapper): absolutely positioned, `bottom:0; left:50%; transform:translateX(-50%); height:86vh; width:80vw` (→ `48vw` at sm, `36vw` at lg). It holds the founder portrait (a transparent-edged cutout) using the **LiquidImage** treatment (see below), `object-fit:cover; object-position:center bottom`, filling the wrapper. In "bare" mode: no surface/veil/glow/vignette overlays — just the image with the liquid SVG-displacement filter (resting near-zero, ramps on hover). The liquid image element itself is `pointer-events:auto`.
- **Gradient base:** an absolute full-width layer, `inset-inline:0; bottom:0; z-index:20; height:26vh; background:linear-gradient(to bottom, transparent, #08080a)` — melts the portrait base + name into the page.
- **Giant name** `<h1>` (`z-index:10`, behind the portrait): absolute, `inset-inline:0; bottom:0; transform:translateY(6%)`, flex column, `align-items:center`, `font-family:display; uppercase; line-height:0.78; letter-spacing:-0.01em; color:var(--accent); font-size:mega` (→ `hero` = 28rem at sm). Two stacked lines, each `display:block; white-space:nowrap`: **`Marcus`** then **`Vane`**. Each line reveals **letter-by-letter** rising from below (`translateY(100% → 0)`, opacity 0→1) with a per-letter stagger (see Motion).
- **Scroll cue** (`z-index:30`): absolute `bottom:2rem; left:var(--gutter)`, flex row `gap:0.75rem; font-size:eyebrow; uppercase; letter-spacing:0.22em; color:var(--muted)`, preceded by a `1px × 2.5rem` accent-red rule (`width:10`). Text: **`Scroll to enter`**. Fades in last.

### 4) Marquee
`<section aria-label="Operating principles">`, `overflow:hidden; border-top:1px solid var(--line); border-bottom:1px solid var(--line); padding-top:2rem; padding-bottom:2rem` (`py-8`).
An inner track (`display:flex; width:max-content; flex-wrap:nowrap`) that translates `x:0% → -50%` on an **infinite linear loop**. The word list is rendered **twice** so the loop is seamless. Each entry: the word `font-family:display; font-size:h2; uppercase; letter-spacing:-0.01em`, followed by an accent-red dot separator (`margin-inline:2rem; width/height:0.625rem; border-radius:9999px; background:var(--accent)`).
Words (verbatim, in order): **Build Bold**, **Scale Relentlessly**, **Think In Decades**, **Bet On People**, **Ship The Future**.
Duration for one full pass: **22 seconds**, linear, looping forever.

### 5) Story
`<section id="story">`, `padding:var(--section) var(--gutter)`. A grid: 1 col on mobile, `12 cols` at `lg` with `gap:var(--gutter)` (and `gap:3rem` vertical on mobile).
- **Left (`lg:col-span-6`):** Eyebrow **`The Story`**. Then an `<h2>` heading, `margin-top:1.5rem; max-width:16ch; font-family:display; uppercase; line-height:0.95; letter-spacing:-0.01em; font-size:h2` (→ `h1` at sm), revealed **line-by-line** (slide up, line stagger ~90ms). Verbatim:
  > Conviction is a competitive advantage.
  Then a `<p>` `margin-top:2rem; max-width:46ch; font-size:lead; color:var(--muted)` that fades+slides up on scroll. Verbatim:
  > For twenty years I've backed the version of the future most people couldn't see yet. From a dorm-room prototype to companies serving a hundred million people, the through-line never changed: find the hard problem everyone avoids, assemble the team nobody else could, and out-stubborn the doubt.
- **Right (`lg:col-span-6; lg:padding-top:0.5rem`):** a `<ul>` of four principles. Each `<li>` is a grid `[auto_1fr]` with `column-gap:1.5rem`, `border-top:1px solid var(--line); padding:2rem 0` (last item also `border-bottom`). Each fades+slides up on scroll, staggered by `index * 90ms`. Left cell: the index number `font-family:sans; font-size:h3; font-weight:600; tabular-nums; color:var(--accent)`. Right cell: an `<h3>` title `font-family:sans; font-size:h3; font-weight:600; letter-spacing:-0.01em`, then a `<p>` `margin-top:0.75rem; max-width:44ch; font-size:body; color:var(--muted)`. The four (verbatim):
  - **01 — Move before it's obvious** — The best opportunities look like mistakes right up until they look inevitable. I commit while the room is still hesitating.
  - **02 — Hire founders, not employees** — I build teams of people who would start their own thing — then give them a reason not to. Ownership compounds faster than talent alone.
  - **03 — Distribution is the product** — Genius unshipped is a hobby. Every venture is engineered around how it reaches the people it was built for.
  - **04 — Play the long game loudly** — Patience and ambition are not opposites. I think in decades and act with urgency every single day.

### 6) Ventures
`<section id="ventures">`, `padding:var(--section) var(--gutter)`. Header row: flex, column on mobile / `sm:row` with `align-items:flex-end; justify-content:space-between`. Left: Eyebrow **`Selected Ventures`** + an `<h2>` (`margin-top:1.5rem; max-width:14ch; font-family:display; uppercase; line-height:0.95; letter-spacing:-0.01em; font-size:h2 → h1 at sm`), line-by-line reveal. Verbatim heading:
> The work that moved markets.
Right: a small label `font-size:eyebrow; uppercase; letter-spacing:0.22em; color:var(--muted)` reading **`04 / Companies`**.

A `<ul>` `margin-top:4rem`, grid `1 col` (→ `2 cols` at md) with `column-gap:var(--gutter); row-gap:4rem`. Each `<li>` fades+slides up on scroll (`y:60→0`), with the **odd-indexed (2nd, 4th) cards offset down** (`md:margin-top:6rem`, i.e. `md:mt-24`) and delayed by `120ms` (the right column staggers after the left). Each card `<article class="group">`:
- A **LiquidImage** (full treatment, with hover liquid distortion + grayscale→color reveal + accent glow), `aspect-ratio:16/11; width:100%; border-radius:0.125rem`. Uses `placeholderLabel` = the venture name (only shown if the image is missing — with real assets it won't be).
- A row `margin-top:1.5rem; border-top:1px solid var(--line); padding-top:1.25rem; display:flex; align-items:flex-start; justify-content:space-between; gap:1.5rem`. Left: `<h3>` name (`font-family:sans; font-size:h3; font-weight:600; letter-spacing:-0.01em`) that **springs from foreground → accent color on hover**; below it a `<p>` `margin-top:0.5rem; max-width:42ch; font-size:body; color:var(--muted)` blurb. Right (shrink-0, right-aligned): the year (`font-size:eyebrow; uppercase; letter-spacing:0.18em; color:var(--muted)`) and the outcome (`margin-top:0.5rem; font-size:eyebrow; font-weight:500; uppercase; letter-spacing:0.18em; color:var(--accent)`).
- Below the row: the category `margin-top:0.75rem; font-size:eyebrow; uppercase; letter-spacing:0.22em; color:var(--muted)`.

The four ventures (verbatim — name / category / year / outcome / blurb / image):
1. **Helix Robotics** — Industrial Automation — 2019 — **Acquired — $1.1B** — "Reinvented warehouse logistics with autonomous fleets now running in 40 countries." — `venture-01.webp`
2. **Northwind Energy** — Climate Infrastructure — 2015 — **IPO — NYSE: NWND** — "Brought utility-scale storage to the grid years before the market believed it was viable." — `venture-02.webp`
3. **Cadence Health** — Digital Medicine — 2011 — **Acquired — $640M** — "Put a clinician in every pocket and rewired how chronic care gets delivered." — `venture-03.webp`
4. **Vane Capital** — Venture Investing — 2008 — **Active — $900M AUM** — "Backing the next generation of contrarian founders building hard, durable companies." — `venture-04.webp`

### 7) Impact
`<section id="impact">`, `padding:var(--section) var(--gutter)`. Header row like Ventures: Eyebrow **`By The Numbers`** + `<h2>` (`font-family:display; uppercase; line-height:1; letter-spacing:-0.01em; font-size:h2`), line-by-line reveal. Verbatim heading:
> Two decades, measured.

A `<dl>` `margin-top:4rem`, grid `1 col` (→ `2 cols` at sm → `4 cols` at lg), `border-top:1px solid var(--line)`. Each stat cell: a `div`, `display:flex; flex-direction:column; gap:1rem; border-bottom:1px solid var(--line); padding:2.5rem 0` (→ `3rem` vertical at lg). Divider rule: at `sm` every 2nd cell gets `border-left` + `padding-left:2rem`; at `lg` all but the first-in-row get `border-left` + `padding-left:2rem` (i.e. cells 2/3/4 of each 4-up row have a left border; the first of each row has none and no left padding). Inside each cell:
- `<dd>` first: the **figure** `font-family:display; font-size:display; line-height:1; letter-spacing:-0.01em`, which **springs foreground → accent on hover** (snappier than the venture name: tension 220 / friction 22).
- `<dt>` second: the **label** `max-width:20ch; font-size:body; uppercase; letter-spacing:0.14em; color:var(--muted)`.

Each cell fades+slides up on scroll, staggered by `index * 110ms`. The four stats (verbatim — value / label):
- **4** — Companies founded & exited
- **$3.2B** — Enterprise value created
- **120M+** — People served by his products
- **2,400** — Jobs created across ventures

### 8) Voices (interactive testimonials)
`<section id="voices">`, `padding:var(--section) var(--gutter)`. Header row: Eyebrow **`Voices`** + `<h2>` (`font-family:display; uppercase; line-height:1; letter-spacing:-0.01em; font-size:h2`), line-by-line reveal. Verbatim heading:
> What they say.

Body grid `margin-top:4rem`, `1 col` (→ `12 cols` at lg, `gap:var(--gutter)`):
- **Selector list (`lg:col-span-5`):** a `<ul>` of the three voices. Each is a full-width `<button>`: `display:flex; align-items:baseline; gap:1.25rem; border-top:1px solid var(--line); padding:1.75rem 0; text-align:left` (last also `border-bottom`). Hover/focus/click sets it **active** (default active = first). Parts: an index `01`/`02`/`03` (`font-size:eyebrow; tabular-nums; letter-spacing:0.18em`) — `color:var(--accent)` when active, else `var(--muted)`; the name `font-family:sans; font-size:h3; font-weight:600; letter-spacing:-0.01em` — `color:var(--foreground)` active / `var(--muted)` inactive; below it the role `margin-top:0.25rem; font-size:eyebrow; uppercase; letter-spacing:0.18em; color:var(--muted)`; and a trailing `1px` accent rule that grows to `2.5rem (w-10)` when active, `0` otherwise.
- **Featured panel (`lg:col-span-7`):** grid `1 col` (→ `[1fr_auto]` at sm, `align-items:flex-start`). A `<blockquote>` (order 2 on mobile / order 1 at sm) holds the active quote in a `<p>` `max-width:30ch; font-family:sans; font-size:h3; font-weight:500; line-height:snug(~1.3); letter-spacing:-0.01em; color:var(--foreground)`, wrapped in curly quotes `“…”`, and **re-plays a word-by-word reveal every time the active voice changes** (words rise `y:18→0`, opacity 0→1, word stagger ~22ms, ~520ms ease-out-quart — see Motion). A `<footer>` `margin-top:2rem; font-size:eyebrow; uppercase; letter-spacing:0.18em; color:var(--muted)` shows `Name — Role`. The portrait (order 1 mobile / order 2 sm, `sm:width:16rem`) is a **LiquidImage** (full treatment), `aspect-ratio:4/5; width:100%; border-radius:0.125rem`, that fades + scales in on first view (`opacity 0→1, scale 1.06→1`). When the active voice changes, swap the portrait `src`.

The three voices (verbatim — quote / name / role / image):
1. "Marcus saw the market three years before the rest of us. Betting alongside him changed the trajectory of my entire career." — **Elena Cardoso** — Managing Partner, Meridian Ventures — `voice-01.webp`
2. "He doesn't just write checks — he gets in the trenches at 6am and refuses to leave until the impossible part is solved." — **David Okonkwo** — Founder & CEO, Cadence Health — `voice-02.webp`
3. "The most demanding mentor I've ever had, and the only reason our company survived its first winter. Relentless, generous, right." — **Priya Nandakumar** — CEO, Northwind Energy — `voice-03.webp`

### 9) ContactFooter
`<footer id="contact">`, `padding-top:var(--section); padding-inline:var(--gutter)` (no bottom section padding before the footer bar).
- Eyebrow **`Let's Build`**.
- An `<h2>` `margin-top:1.5rem; max-width:18ch; font-family:display; uppercase; line-height:0.95; letter-spacing:-0.01em; font-size:h1 → display at sm`, line-by-line reveal. Verbatim:
  > Have something the world says can't be done?
- A `<p>` `margin-top:2rem; max-width:44ch; font-size:lead; color:var(--muted)` that fades+slides up. Verbatim:
  > That's usually where I start. I read every message I'm sent.
- The **email link** (`margin-top:3rem`): an `<a href="mailto:hello@marcusvane.com">`, `display:inline-flex; align-items:baseline; gap:0.75rem (sm:1rem); font-family:sans; font-size:h3 → h1 at sm; font-weight:600; letter-spacing:-0.01em; word-break:break-all`. On hover it **springs to the right (`translateX(0 → 14px)`) and to accent color** (foreground → accent, tension 220 / friction 22). Text: **`hello@marcusvane.com`** followed by an accent-red **↗** arrow.
- **Footer bar** (`margin-top:var(--section); border-top:1px solid var(--line); padding:3rem 0`): grid `1 col` (→ `12 cols` at lg, `gap:2.5rem`).
  - Left (`lg:col-span-6`): signature `<p>` **`Marcus Vane`** (`font-family:display; font-size:h2; uppercase; line-height:1; letter-spacing:-0.01em`), and below it `margin-top:1rem; font-size:eyebrow; uppercase; letter-spacing:0.22em; color:var(--muted)` reading **`Designed & built with conviction.`**.
  - Middle (`lg:col-span-3`): a `<nav aria-label="Social">` `<ul>` of three external links (`target="_blank" rel="noreferrer noopener"`), each `font-size:body; color:var(--muted)`, hover → `color:var(--foreground)` with a leading accent rule that grows `width 0 → 1.5rem`. Links: **LinkedIn → https://www.linkedin.com**, **X / Twitter → https://x.com**, **Substack → https://substack.com**.
  - Right (`lg:col-span-3; lg:text-align:right`): the copyright `<p>` (`font-size:eyebrow; uppercase; letter-spacing:0.18em; color:var(--muted)`): **`© 2026 Marcus Vane. All rights reserved.`** (the original computes the current year — hardcode 2026, or compute it).

### LiquidImage component (used by hero portrait, ventures, voices)
Reproduce as a small reusable JS/CSS component. A `<figure role="img">` `position:relative; overflow:hidden` (with `background:var(--surface)` unless "bare"). Inside, an inline `<svg>` filter (`width:0;height:0;position:absolute`) defining `feTurbulence type="fractalNoise" baseFrequency=0.009 numOctaves=2 result="noise"` → `feDisplacementMap in="SourceGraphic" in2="noise" scale=1`. The `<img>` (or `<video>` for the hero) sits `position:absolute; inset:0; width/height:100%; object-fit; object-position`, with CSS `filter:url(#thatFilter)` applied.

On hover (desktop only — disable on touch/≤768px), animate the filter attributes **imperatively** via JS (write `scale` on the displacement map and `baseFrequency` on the turbulence directly as attributes — do not animate them through CSS strings) using a spring with **tension 140 / friction 13** (a loose, watery wobble): `scale` ramps `1 → 28` (ventures) / `30` (hero portrait) / `22` (voices), `baseFrequency` ramps `0.009 → 0.022`. In **non-bare** mode also layer, on hover, a grayscale→color reveal (a `mix-blend-mode:color` background-colored veil whose opacity goes `~0.88 → 0`, spring tension 220 / friction 26) and an **accent glow sweep** (`linear-gradient(120deg, transparent 30%, color-mix(in srgb, var(--accent) 35%, transparent) 50%, transparent 70%)`, opacity `0 → 1`), plus a persistent radial vignette (`radial-gradient(120% 120% at 50% 120%, color-mix(in srgb, #08080a 70%, transparent), transparent 60%)`) and a branded radial placeholder (`radial-gradient(130% 130% at 30% 15%, var(--surface-2), var(--background))`) shown when no image. **Bare mode** (hero portrait) strips all overlays — just the filtered image. The hero uses a **looped muted autoplay `<video>`** (`autoplay muted loop playsinline preload=auto`) with the portrait `.webp` as its `poster`; same filter/fit applies.

---

## Motion system

All original motion is `@react-spring/web` springs and `spring-text-engine` (also spring-driven). Convert each spring `{tension, friction, mass?}` to a duration + easing. A spring with tension `T`, friction `F`, mass 1 has settle time ≈ `4 / (F / (2·√T))` ... but you don't need the physics — use these **baked equivalents** (they match the configs in the source):

**Spring → timing cheat-sheet (use these exact mappings):**
- `tension 90 / friction 20` (preloader wipe) → **~650ms, cubic-bezier(0.22,1,0.36,1)** (ease-out, gentle).
- `tension 210 / friction 28` (mobile menu fade) → **~450ms ease-out**.
- `tension 260 / friction 30` (mobile menu link trail) → **~420ms ease-out**, items staggered.
- `tension 180 / friction 26` (hero description, story body) → **~520ms cubic-bezier(0.16,1,0.3,1)**.
- `tension 170 / friction 26` (story principles, impact cells) → **~560ms cubic-bezier(0.16,1,0.3,1)**.
- `tension 150 / friction 26` (venture cards) → **~620ms cubic-bezier(0.16,1,0.3,1)**.
- `tension 140 / friction 24` (voice portrait scale-in) → **~640ms cubic-bezier(0.16,1,0.3,1)**.
- `tension 220 / friction 22` (hover → accent on impact figures, email link, liquid reveal) → **~340ms ease-out**.
- `tension 220 / friction 26` (liquid grayscale reveal) → **~380ms ease-out**.
- `tension 140 / friction 13` (liquid distortion) → **~520ms, springy/overshoot** — if using GSAP, `ease:"elastic.out(1,0.5)"` lightly; otherwise a long ease-out is acceptable.

**Text reveals (spring-text-engine equivalents).** The library splits text into letters / words / lines and animates each slot. Replicate by wrapping each unit in a span with `overflow:hidden` on the parent line and translating the inner span:
- **Hero name — letter-by-letter:** each letter `translateY(100% → 0)`, opacity `0 → 1`; **letterStagger 52ms**; per-letter motion `duration 900ms, easeOutExpo` (`cubic-bezier(0.16,1,0.3,1)`). Line 2 ("Vane") starts **240ms** after line 1 (delayIn `i*240`).
- **Hero roles — line-by-line:** each word-line `translateY(110% → 0)`, opacity `0 → 1`; `duration 760ms, easeOutExpo`; staggered `i*80ms`.
- **Section headings (Story / Ventures / Impact / Voices / Contact) — line-by-line:** each line `translateY(110% → 0)`, opacity `0 → 1`; `duration 800–950ms, easeOutExpo`; **lineStagger 90ms** where the heading wraps to multiple lines.
- **Voices quote — word-by-word (replays on change):** each word `translateY(18px → 0)`, opacity `0 → 1`; **wordStagger 22ms**; `duration 520ms, easeOutQuart` (`cubic-bezier(0.165,0.84,0.44,1)`). Re-trigger the whole animation each time the active voice changes (mode "always").
  - easeOutExpo = `cubic-bezier(0.16, 1, 0.3, 1)`; easeOutQuart = `cubic-bezier(0.165, 0.84, 0.44, 1)`.

**Hero reveal sequencing.** The hero waits for the preloader: there's a **REVEAL_DELAY of 2500ms** baseline (≈2000ms count + ~500ms wipe). Then:
- Name line 1 at `2500ms`, line 2 at `2740ms` (each letter further staggered by 52ms).
- Roles at `2700ms + i*80ms`.
- Description at `2900ms`.
- Scroll cue at `3400ms`.
Drive these as `setTimeout`/animation-delay after page load. (Heading reveals in lower sections are **scroll-triggered**, not delayed — see below.)

**In-view triggers.** Every section reveal (Story/Ventures/Impact/Voices/Contact text + the fade/slide-in blocks) and the section heading text reveals fire when the element first enters the viewport, mode **"once"** (play once, never reverse). Use an `IntersectionObserver` with **threshold 0** (fire as soon as any pixel is visible; the original uses default IO options = threshold 0, rootMargin 0). On enter, add an `.in-view` class (or start the animation) and unobserve. Stagger delays are added on top (`i*90`, `i*110`, `i*120`, etc., per section above).

**Marquee loop.** Translate the doubled track `x: 0% → -50%`, **linear, 22s, infinite**. CSS `@keyframes` is the simplest faithful match: `@keyframes marquee{from{transform:translateX(0)}to{transform:translateX(-50%)}}` with `animation:marquee 22s linear infinite`. (The original uses a looping spring with linear easing — visually identical.) Disable under reduced-motion.

**Preloader timing (exact).** Count 0→100 over **2000ms**; on rest, fade labels out over ~300ms; **200ms** delay; wipe up over **~650ms ease-out (cubic-bezier(0.22,1,0.36,1))**; on wipe rest, `lenis.start()`.

---

## Fixed parameters (bake these in)

**Colors (hex / rgba):**
- background `#08080a` · foreground `#f3f1ea` · surface `#111114` · surface-2 `#17171b`
- muted `#807f78` · line `rgba(243,241,234,0.1)` · line-strong `rgba(243,241,234,0.22)`
- **accent (signature red) `#ff3b1d`** · accent-2 `#ff6a3d`

**Type scale (rem / line-height):** hero `28rem`/`0.78` · mega `13rem`/`0.86` · display `7.5rem`/`0.9` · h1 `5rem`/`0.95` · h2 `3.25rem`/`1` · h3 `1.75rem`/`1.15` · lead `1.375rem`/`1.45` · body `1.0625rem`/`1.6` · eyebrow `0.8125rem`/`1.2`. Common tracking: headings `-0.01em`; eyebrows/labels `0.18em`–`0.22em`; stat labels `0.14em`.

**Fonts:** display = **Anton** (400); sans = **Onest** (400/500/600).

**Spacing:** gutter `2.5rem` (desktop) → `16px` (≤640px); section vertical padding `9rem`.

**Breakpoints:** sm `640px`, md `768px`, lg `1024px`. Adaptive-grid base width `1920px`; vw root-font formula `16*100/baseWidth`; scale-up coef `0.6666`. Mobile-disable hover/liquid effects ≤ `768px`.

**Spring → duration/easing** (full table in Motion system). Key ones: text reveals `easeOutExpo cubic-bezier(0.16,1,0.3,1)`, 760–950ms; hero letterStagger `52ms`, line delay `240ms`; heading lineStagger `90ms`; voices wordStagger `22ms` / `520ms easeOutQuart`; in-view block reveals 520–640ms ease-out with per-index stagger `90/110/120ms`; hover-to-accent ~340ms; liquid distortion springy ~520ms; preloader count `2000ms`, wipe `~650ms`; marquee `22s linear infinite`.

**REVEAL_DELAY:** `2500ms` (hero entrance baseline after preloader).

---

## Assets

Load each asset from its full bucket URL below (do not use relative `/assets/...` paths). Keep each asset in its original role.

Base: `https://api.getlayers.ai/storage/v1/object/public/public/assets/marcus-vane-6799bd1fb6`

- **Hero portrait** (the cutout composited in the hero; also the hero video's `poster`):
  `https://api.getlayers.ai/storage/v1/object/public/public/assets/marcus-vane-6799bd1fb6/hero/portrait.webp`
- **Hero looped video** (muted autoplay, loops, `playsinline`):
  `https://api.getlayers.ai/storage/v1/object/public/public/assets/marcus-vane-6799bd1fb6/hero/hero.mp4`
- **Ventures grid:**
  - `https://api.getlayers.ai/storage/v1/object/public/public/assets/marcus-vane-6799bd1fb6/ventures/venture-01.webp` (Helix Robotics)
  - `https://api.getlayers.ai/storage/v1/object/public/public/assets/marcus-vane-6799bd1fb6/ventures/venture-02.webp` (Northwind Energy)
  - `https://api.getlayers.ai/storage/v1/object/public/public/assets/marcus-vane-6799bd1fb6/ventures/venture-03.webp` (Cadence Health)
  - `https://api.getlayers.ai/storage/v1/object/public/public/assets/marcus-vane-6799bd1fb6/ventures/venture-04.webp` (Vane Capital)
- **Voices / testimonials:**
  - `https://api.getlayers.ai/storage/v1/object/public/public/assets/marcus-vane-6799bd1fb6/voices/voice-01.webp` (Elena Cardoso)
  - `https://api.getlayers.ai/storage/v1/object/public/public/assets/marcus-vane-6799bd1fb6/voices/voice-02.webp` (David Okonkwo)
  - `https://api.getlayers.ai/storage/v1/object/public/public/assets/marcus-vane-6799bd1fb6/voices/voice-03.webp` (Priya Nandakumar)