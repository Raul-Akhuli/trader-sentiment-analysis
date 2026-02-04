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


### 📄 summary.md (COPY–PASTE)
```md
## Trader Behavior Insights – Summary

### Objective
The goal of this analysis was to understand how Bitcoin market sentiment (Fear vs Greed) influences trader behavior and daily performance on Hyperliquid.

---

### Methodology
- Trade-level data was aggregated to daily metrics per trader
- Market sentiment was aligned at a daily level
- Performance (PnL, win rate) and behavior (frequency, long bias) were compared across sentiment regimes
- Traders were segmented based on frequency and consistency

---

### Key Findings
1. **Performance Volatility**
   - Daily PnL volatility is significantly higher during Fear periods, indicating unstable market conditions.

2. **Behavioral Shift**
   - Traders place fewer but larger trades during Fear days.
   - Trade frequency and long bias increase during Greed periods.

3. **Trader Segments**
   - Frequent traders outperform infrequent traders during Greed days.
   - Consistent traders show smaller drawdowns during Fear periods.

---

### Actionable Strategies
1. During **Fear** days:
   - Reduce trade frequency
   - Focus on high-confidence setups only

2. During **Greed** days:
   - Increase activity selectively for consistent traders
   - Monitor long exposure to control downside risk

---

### Conclusion
Market sentiment strongly impacts both trader behavior and performance. Incorporating sentiment-aware rules can help reduce drawdowns and improve overall trading outcomes.

