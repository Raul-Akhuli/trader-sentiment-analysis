# Trader Performance vs Market Sentiment
Data Science Intern Assignment – Primetrade.ai

## Objective
Analyze how Bitcoin market sentiment (Fear vs Greed) impacts trader behavior and daily performance on Hyperliquid, and extract actionable trading insights.

## Datasets
1. Bitcoin Fear & Greed Index  
   - Daily market sentiment classification (Fear / Greed)

2. Hyperliquid Trader Data  
   - Trade-level data including account, side, size (USD), timestamp (IST), and closed PnL

## Methodology
- Cleaned and standardized column names
- Converted timestamps to daily level using IST (day-first format)
- Aggregated trade-level data into daily trader metrics:
  - Daily PnL
  - Trade frequency
  - Win rate
  - Average trade size
  - Long/Short ratio
- Merged trader metrics with daily market sentiment
- Compared trader behavior and performance across Fear vs Greed regimes
- Segmented traders based on:
  - Trading frequency (Frequent vs Infrequent)
  - Performance consistency (Consistent vs Inconsistent)

## Key Insights
1. Performance Volatility  
   - Daily PnL volatility is significantly higher during Fear periods, reflecting unstable market conditions.

2. Behavioral Shift  
   - Traders place fewer but larger trades during Fear days.  
   - Trade frequency and long bias increase during Greed periods, indicating higher risk appetite.

3. Trader Segments  
   - Frequent traders outperform infrequent traders during Greed days.  
   - Consistent traders experience smaller drawdowns during Fear periods.

## Actionable Strategy Recommendations
1. During Fear days  
   - Reduce trade frequency  
   - Focus only on high-confidence setups to control downside risk

2. During Greed days  
   - Increase trading activity selectively for consistent traders  
   - Monitor long exposure to avoid excessive directional risk

## How to Run
Install dependencies, which are in the txt file
And after downloading the dataset, you can add it as a link
Then run the ipynb file


