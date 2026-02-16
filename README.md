# Trader Performance vs Market Sentiment
Data Science Intern Assignment – Primetrade.ai

## Objective
Analyze how Bitcoin market sentiment (Fear vs Greed) impacts trader behavior and daily performance on Hyperliquid, and extract actionable trading insights.


---

## 📊 Datasets

1. **Bitcoin Fear & Greed Index**
   - Daily market sentiment classification (Fear / Greed)

2. **Hyperliquid Trader Data**
   - Trade-level data including account, side, size (USD), timestamp, leverage, closed PnL

---

## 🔎 Methodology

### 1️⃣ Data Preparation
- Cleaned and standardized column names
- Converted timestamps to daily level
- Aggregated trade-level data into daily trader metrics:
  - Daily PnL
  - Trade frequency
  - Win rate
  - Average trade size
  - Long/Short ratio
- Merged trader metrics with daily market sentiment

---

### 2️⃣ Sentiment-Based Analysis
- Compared PnL, win rate, and trading behavior across:
  - Fear days
  - Greed days
- Evaluated behavioral shifts in:
  - Trade frequency
  - Leverage usage
  - Position bias

---

### 3️⃣ Trader Segmentation (Bonus – Clustering)

Created trader-level aggregated metrics:

- Average PnL
- PnL volatility
- Average leverage
- Total trades
- Average position size
- Long exposure ratio

Applied:
- StandardScaler
- KMeans clustering (k=3)

Identified trader archetypes:
- Aggressive high-leverage traders
- Conservative low-volatility traders
- High-frequency moderate-risk traders

---

## 🤖 Bonus: Streamlit Dashboard

Interactive dashboard includes:
- Daily PnL visualization
- Sentiment-based filtering
- Cluster-based analysis

---

## 💡 Key Insights

1. PnL volatility is significantly higher during Fear periods.
2. Traders increase long bias and frequency during Greed regimes.
3. High-leverage traders experience extreme volatility during Fear days.
4. Conservative traders show better risk-adjusted performance.

---

## 🎯 Strategy Recommendations

1. During Fear:
   - Reduce leverage
   - Trade selectively
   - Avoid overexposure

2. During Greed:
   - Increase participation for consistent traders
   - Monitor directional bias

---

## ⚙️ How to Run


## How to Run
Install dependencies, which are in the txt file
And after downloading the dataset, you can add it as a link
Then run the ipynb file
to visualize run streamlit run app.py


