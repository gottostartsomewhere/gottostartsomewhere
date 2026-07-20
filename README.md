<p align="center">
  <img src="./assets/ticker.svg" width="392" alt="Candlestick chart trending up">
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

---

Final-year CS at VIT Chennai and on the founding team at **WiseFolio**, an early-stage fintech, building the data and payment layers behind an equities investing platform. Most of what is left of my week goes to open source in the Python finance ecosystem.

### Filled

Merged into the finance and data libraries I actually use.

- **[OpenBB](https://github.com/OpenBB-finance/OpenBB/pull/7591)** &nbsp;`70k ★`&nbsp; building an NSE market-data extension (`obb.nse.*`), alongside the core maintainers
- **[edgartools](https://github.com/dgunning/edgartools/pull/899)** &nbsp; S-3 filing section extraction for the SEC EDGAR library
- **[yfinance](https://github.com/ranaroussi/yfinance/pull/2780)** &nbsp;`24k ★`&nbsp; fixes to interval handling
- **[supabase-py](https://github.com/supabase/supabase-py/pull/1530)** &nbsp; a type-coercion fix in the PostgREST array filters

### Open positions

**[ledger-api](https://github.com/gottostartsomewhere/ledger-api)** &nbsp;·&nbsp; double-entry payment ledger &nbsp;·&nbsp; `FastAPI` `Postgres` `Redis`

Balanced debit/credit rows inside one row-locked transaction so balances can't drift. Idempotent writes (Redis plus a Postgres fingerprint) keep retries safe from double-charges, and settlement events ship through an HMAC-signed transactional outbox that survives a DB rollback.

**[CVA-SACS](https://github.com/gottostartsomewhere/Cva_Sacs)** &nbsp;·&nbsp; equity stress-testing engine &nbsp;·&nbsp; [live demo](https://cvasacs.streamlit.app) &nbsp;·&nbsp; `Python` `XGBoost` `FinBERT`

Stacks gradient-boosted models with CVaR, Monte Carlo, and conformal intervals over ~130 features plus a FinBERT sentiment index into a single 0 to 100 risk score. Walk-forward backtested, with SHAP for explainability. Built to be honest about uncertainty, not just print a number.

### Instruments

`Python` `TypeScript` `C++` `FastAPI` `Node` `PostgreSQL` `Redis` `MongoDB` `SQLAlchemy` `Docker` `AWS` `React` `Next.js`

### Tape

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=gottostartsomewhere&show_icons=true&include_all_commits=true&count_private=true&bg_color=04060a&title_color=34e39b&icon_color=38d6ff&text_color=c9d3dd&border_color=1c3a2c" alt="GitHub stats">
  &nbsp;
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=gottostartsomewhere&layout=compact&langs_count=8&bg_color=04060a&title_color=34e39b&text_color=c9d3dd&border_color=1c3a2c" alt="Top languages">
</p>

<p align="center">
  <img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=gottostartsomewhere&bg_color=04060a&color=c9d3dd&line=34e39b&point=38d6ff&area=true&area_color=34e39b&hide_border=true" alt="Contribution activity graph">
</p>

---

<p align="center"><sub>risk controls: balances reconcile, retries are idempotent, and the webhook always fires.</sub></p>
