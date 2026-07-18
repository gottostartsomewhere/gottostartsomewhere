<p align="center">
  <img src="./assets/roulette.svg" width="180" alt="Spinning roulette wheel">
</p>

<h1 align="center">John Kevin</h1>

<p align="center">
  Backend &amp; fintech engineer · Chennai<br/>
  <sub>Payments, ledgers, and market-data tooling. Currently all in on open source.</sub>
</p>

<p align="center">
  <a href="https://linkedin.com/in/johnkevindev">LinkedIn</a> ·
  <a href="mailto:johnkevin0742@gmail.com">Email</a> ·
  <a href="https://github.com/gottostartsomewhere?tab=repositories">Repositories</a>
</p>

<p align="center">
  <img src="./assets/chips.svg" width="230" alt="Poker chips">
</p>

Final-year CS at VIT Chennai and on the founding team at **WiseFolio**, an early-stage fintech, building the data and payment layers behind an equities investing platform. Lately I spend my free chips on open source in the Python finance ecosystem.

### ♦&nbsp; Bets that paid off

Contributions to the finance and data libraries I actually use.

- **[OpenBB](https://github.com/OpenBB-finance/OpenBB/pull/7591)** &nbsp;`70k ★`&nbsp; building an NSE market-data extension (`obb.nse.*`), alongside the core maintainers
- **[edgartools](https://github.com/dgunning/edgartools/pull/899)** &nbsp; merged S-3 filing section extraction into the SEC EDGAR library
- **[yfinance](https://github.com/ranaroussi/yfinance/pull/2780)** &nbsp;`24k ★`&nbsp; merged fixes to interval handling
- **[supabase-py](https://github.com/supabase/supabase-py/pull/1530)** &nbsp; merged a type-coercion fix in the PostgREST array filters

### ♠&nbsp; On the table

**[ledger-api](https://github.com/gottostartsomewhere/ledger-api)** &nbsp;·&nbsp; double-entry payment ledger &nbsp;·&nbsp; `FastAPI` `Postgres` `Redis`

Balanced debit/credit rows inside one row-locked transaction so balances can't drift. Idempotent writes (Redis plus a Postgres fingerprint) keep retries safe from double-charges, and settlement events ship through an HMAC-signed transactional outbox that survives a DB rollback.

**[CVA-SACS](https://github.com/gottostartsomewhere/Cva_Sacs)** &nbsp;·&nbsp; equity stress-testing engine &nbsp;·&nbsp; [live demo](https://cvasacs.streamlit.app) &nbsp;·&nbsp; `Python` `XGBoost` `FinBERT`

Stacks gradient-boosted models with CVaR, Monte Carlo, and conformal intervals over ~130 features plus a FinBERT sentiment index into a single 0 to 100 risk score. Walk-forward backtested, with SHAP for explainability. Built to be honest about uncertainty, not just print a number.

### ♣&nbsp; Chips on hand

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,ts,js,cpp,fastapi,nodejs,postgres,redis,mongodb,docker,aws,githubactions,react,nextjs,tailwind&perline=8" alt="Python, TypeScript, JavaScript, C++, FastAPI, Node, PostgreSQL, Redis, MongoDB, Docker, AWS, GitHub Actions, React, Next.js, Tailwind">
</p>

### ♥&nbsp; Table stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=gottostartsomewhere&show_icons=true&hide_border=true&include_all_commits=true&count_private=true&bg_color=0d1117&title_color=c8a24a&icon_color=c8a24a&text_color=c9d1d9&ring_color=c8a24a" alt="GitHub stats">
  &nbsp;
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=gottostartsomewhere&layout=compact&hide_border=true&langs_count=8&bg_color=0d1117&title_color=c8a24a&text_color=c9d1d9" alt="Top languages">
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=gottostartsomewhere&hide_border=true&background=0d1117&stroke=21262d&ring=c8a24a&fire=a80c17&currStreakLabel=c8a24a&sideLabels=c9d1d9&currStreakNum=c9d1d9&sideNums=c9d1d9&dates=8b949e" alt="Contribution streak">
</p>

<p align="center">
  <img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=gottostartsomewhere&bg_color=0d1117&color=c8a24a&line=c8a24a&point=f2efe6&area=true&area_color=c8a24a&hide_border=true" alt="Contribution activity graph">
</p>

---

<p align="center"><sub>house rules: balances reconcile, retries are idempotent, and the webhook always fires.</sub></p>
