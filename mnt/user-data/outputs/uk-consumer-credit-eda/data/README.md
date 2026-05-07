# Data Sources & Download Guide

The `raw/` folder is gitignored to keep the repo lightweight.
Follow the steps below to download each dataset before running the notebooks.

---

## 1. Bank of England — Consumer Credit Statistics

**Notebook:** `01_macro_lending_trends.ipynb`

1. Go to: https://www.bankofengland.co.uk/statistics/tables
2. Under *Monetary & Financial Statistics*, download **Table A5.2** — Consumer credit
3. Save as: `data/raw/boe_consumer_credit.xlsx`

---

## 2. FCA Financial Lives Survey

**Notebook:** `02_borrower_profile_eda.ipynb`

1. Go to: https://www.fca.org.uk/financial-lives/financial-lives-data
2. Download the latest **Technical Annex & Data Tables** (Excel format)
3. Save as: `data/raw/fca_financial_lives.xlsx`

---

## 3. Kaggle — Give Me Some Credit

**Notebook:** `02_borrower_profile_eda.ipynb`, `03_default_risk_analysis.ipynb`

1. Go to: https://www.kaggle.com/c/GiveMeSomeCredit/data
2. Download `cs-training.csv`
3. Save as: `data/raw/cs_training.csv`

> **Note:** Requires a free Kaggle account.
> Alternatively, install the Kaggle CLI and run:
> ```bash
> kaggle competitions download -c GiveMeSomeCredit
> ```

---

## 4. ONS — Household Debt Statistics

**Notebook:** `02_borrower_profile_eda.ipynb`

1. Go to: https://www.ons.gov.uk/economy/investmentsourcesandfinancingofbusinesses/bulletins/wealthingreatbritainwave
2. Download the household debt table
3. Save as: `data/raw/ons_household_debt.xlsx`

---

## 5. UK Finance — Lending Trends

**Notebook:** `01_macro_lending_trends.ipynb`

1. Go to: https://www.ukfinance.org.uk/data-and-research/data
2. Download *Household Finance Review* (latest quarter)
3. Save as: `data/raw/ukfinance_lending_trends.xlsx`

---

## Folder Structure (after downloading)

```
data/
├── raw/
│   ├── boe_consumer_credit.xlsx
│   ├── fca_financial_lives.xlsx
│   ├── cs_training.csv
│   ├── ons_household_debt.xlsx
│   └── ukfinance_lending_trends.xlsx
└── processed/            ← generated automatically by notebooks
```
