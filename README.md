<p align="center">
  <img src="./assets/roulette.svg" width="190" alt="Spinning roulette wheel">
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

`Python` `TypeScript` `FastAPI` `Node` `PostgreSQL` `Redis` `SQLAlchemy` `Docker` `AWS` `React` `Next.js`

---

<p align="center"><sub>house rules: balances reconcile, retries are idempotent, and the webhook always fires.</sub></p>
