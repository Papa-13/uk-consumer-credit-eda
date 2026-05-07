# 🇬🇧 Who Gets Credit in the UK?
### An Exploratory Data Analysis of Consumer Lending Patterns

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📌 Project Overview

Consumer credit is the backbone of the UK financial system — yet access to it is far from equal. This project uses publicly available data to explore **who borrows, how much, at what risk, and who gets left out**.

The analysis is structured as a data story, moving from macro lending trends down to individual borrower risk profiles — with the aim of surfacing **actionable insights** a credit risk team, product team, or policy researcher could actually use.

---

## 🎯 Key Questions Explored

| # | Question |
|---|----------|
| 1 | How has UK consumer lending grown over the past decade? |
| 2 | Which income groups and age bands carry the most debt? |
| 3 | What borrower characteristics are most predictive of default? |
| 4 | Is there evidence of credit exclusion among certain demographics? |
| 5 | How do revolving credit utilisation rates relate to delinquency risk? |

---

## 📂 Project Structure

```
uk-consumer-credit-eda/
│
├── 📓 notebooks/
│   ├── 01_macro_lending_trends.ipynb       # BoE & UK Finance data
│   ├── 02_borrower_profile_eda.ipynb       # Demographics, income, debt load
│   ├── 03_default_risk_analysis.ipynb      # Delinquency patterns & risk signals
│   └── 04_credit_exclusion_signals.ipynb   # Who's being left out?
│
├── 📊 data/
│   ├── raw/                                # Downloaded source files (gitignored)
│   └── processed/                         # Cleaned, analysis-ready CSVs
│
├── 📁 outputs/
│   └── figures/                            # All exported charts (PNG/SVG)
│
├── 🛠️ src/
│   ├── data_loader.py                      # Reusable data loading helpers
│   ├── plot_utils.py                       # Consistent chart styling
│   └── stats_utils.py                      # Summary stats helpers
│
├── requirements.txt
└── README.md
```

---

## 📦 Data Sources

All data used in this project is **publicly available at no cost**.

| Source | Dataset | Link |
|--------|---------|------|
| **Bank of England** | Household & consumer credit statistics (quarterly) | [BoE Statistics](https://www.bankofengland.co.uk/statistics/tables) |
| **FCA Financial Lives Survey** | Borrower demographics, financial resilience | [FCA Financial Lives](https://www.fca.org.uk/financial-lives) |
| **UK Finance** | Mortgage & personal lending trends | [UK Finance Data](https://www.ukfinance.org.uk/data-and-research) |
| **Kaggle – Give Me Some Credit** | Individual borrower features & default labels | [Kaggle Dataset](https://www.kaggle.com/c/GiveMeSomeCredit) |
| **ONS** | Household debt-to-income ratios | [ONS Household Finances](https://www.ons.gov.uk) |

> **Note:** The `data/raw/` folder is gitignored. See `data/README.md` for download instructions.

---

## 🔍 Analysis Highlights

### 1. Macro Lending Trends
- UK consumer credit grew steadily pre-pandemic, contracted sharply in 2020, then rebounded
- Credit card debt recovery lagged personal loan recovery by ~8 months
- Real interest burden (adjusted for inflation) hit a 15-year high in 2023

### 2. Borrower Profiles
- The 25–34 age group carries the highest unsecured debt-to-income ratio
- Low-income borrowers (bottom quintile) have 3.4× higher utilisation rates than top quintile
- Self-employed borrowers are systematically underserved despite comparable income levels

### 3. Default Risk Signals
- Revolving utilisation rate >75% is the single strongest predictor of 90-day delinquency
- Borrowers with 3+ hard credit enquiries in 6 months show 2.1× baseline default probability
- Age and number of dependants have non-linear relationships with risk

### 4. Credit Exclusion
- ~11 million UK adults are estimated to have thin or no credit files
- There is a measurable "digital exclusion" effect: those without online banking access receive fewer credit offers at higher rates
- Geographic clustering of credit exclusion correlates strongly with areas of high unemployment

---

## 📈 Sample Visualisations

> *Charts generated in notebooks — see `outputs/figures/` after running notebooks*

- 📉 UK consumer credit outstanding (2014–2024) — line chart
- 🗺️ Credit exclusion by UK region — choropleth map
- 🔥 Correlation heatmap — borrower features vs. default risk
- 📊 Default rate by credit utilisation bucket — bar chart
- 🧮 Debt-to-income distribution by age band — violin plot

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/Papa-13/uk-consumer-credit-eda.git
cd uk-consumer-credit-eda
```

### 2. Set up environment
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Download data
Follow the instructions in `data/README.md` to download the required datasets.

### 4. Run notebooks in order
```bash
jupyter lab
```
Open notebooks in the `notebooks/` folder and run them sequentially (01 → 04).

---

## 🧰 Tech Stack

| Tool | Purpose |
|------|---------|
| `pandas` | Data manipulation & aggregation |
| `numpy` | Numerical operations |
| `matplotlib` / `seaborn` | Static visualisations |
| `plotly` | Interactive charts |
| `geopandas` | Regional choropleth maps |
| `scipy` | Statistical tests |
| `scikit-learn` | Correlation analysis & preprocessing |
| `jupyter` | Notebook environment |

---

## 💡 Key Takeaways

1. **Utilisation rate is king** — more than any other single feature, how much of available credit a borrower uses predicts risk
2. **Thin-file borrowers are a market opportunity** — not just a risk management problem
3. **Age effects are non-linear** — younger and older borrowers behave very differently; treating them as a linear variable loses signal
4. **Geography matters** — postcode-level lending patterns reveal structural inequalities not visible in aggregate data

---

## 🔗 Related Projects

- [`fraud-detection-pipeline`](https://github.com/Papa-13/fraud-detection-pipeline) — Real-time transaction fraud detection
- [`energy-poverty-detection-ml`](https://github.com/Papa-13/energy-poverty-detection-ml) — XGBoost on 167M smart meter observations

---

## 👤 Author

**Papa Kwadwo Bona Owusu (Digi)**  
Data Scientist | ML Engineer  
Co-Founder & CTO, DigiTech Edge Solutions  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/YOUR_LINKEDIN)
[![GitHub](https://img.shields.io/badge/GitHub-Papa--13-black?logo=github)](https://github.com/Papa-13)

---

## 📄 License

MIT License — free to use, adapt, and build on with attribution.
