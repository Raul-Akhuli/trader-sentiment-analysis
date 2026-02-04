# Trader Performance vs Market Sentiment

## Objective
Analyze how Bitcoin market sentiment (Fear vs Greed) impacts trader behavior and performance on Hyperliquid.

---

## Datasets
1. **Bitcoin Fear & Greed Index**
   - Daily market sentiment classification

2. **Hyperliquid Trader Data**
   - Trade-level data including account, side, size, timestamp, and PnL

---

## Methodology
1. Cleaned and standardized column names
2. Converted timestamps to daily level (IST, day-first format)
3. Aggregated trade-level data to daily trader metrics:
   - Daily PnL
   - Trade frequency
   - Win rate
   - Average trade size
   - Long/Short ratio
4. Merged trader metrics with daily sentiment
5. Compared trader behavior and performance across Fear vs Greed days
6. Performed trader segmentation:
   - Frequent vs Infrequent traders
   - Consistent vs Inconsistent traders

---

## Key Insights
- Trader PnL volatility is higher during Fear periods
- Frequent traders perform relatively better during Greed days
- Long bias increases during Greed, indicating higher risk appetite

---

## Strategy Recommendations
- Reduce trade frequency and risk exposure during Fear days
- Allow higher activity during Greed days only for consistent traders

---

## How to Run
```bash
pip install -r requirements.txt
### Conclusion
Market sentiment strongly impacts both trader behavior and performance. Incorporating sentiment-aware rules can help reduce drawdowns and improve overall trading outcomes.

