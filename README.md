# Quantitative Strategy: Nikkei 225 Mean Reversion with Statistical Risk Controls

This repository hosts a robust quantitative trading strategy developed for **Nikkei 225 (NI225) Futures**. The strategy evolved from a naive Z-Score mean reversion model into a sophisticated algorithm incorporating volatility scaling, regime filtering, and statistical emergency exits.

## Strategy Evolution & Performance
The development focus was on **Drawdown Reduction** and **Risk-Adjusted Returns**. Through iterative optimization and failure analysis, the Maximum Drawdown was reduced by over 60%.

| Version | Key Enhancement | Max Drawdown | Profit Factor | Status |
| :--- | :--- | :--- | :--- | :--- |
| **v1.0** | Basic Z-Score Entry | 79.83% | 1.005 | Failed (High Risk) |
| **v4.0** | 200-SMA Trend Filter | 36.72% | 1.200 | Viable |
| **v5.0** | Statistical Z-Stop | 31.16% | 1.181 | Robust |
| **v6.0** | **Session Time Filter** | **29.37%** | **1.235** | **Production Ready** |

## Core Methodology
1. **Trend Regime Detection**: Uses a 200-period SMA to ensure entries are aligned with the long-term market direction, preventing "catching a falling knife."
2. **Volatility Scaling (ATR)**: Position sizing is dynamically adjusted based on Average True Range (ATR) to equalize risk across different market environments.
3. **Statistical Emergency Exit (Z-Stop)**: If the Z-Score hits ±3.0, the model identifies a "regime break" where mean reversion logic is no longer valid, triggering an immediate exit to prevent catastrophic losses.
4. **Market Session Optimization**: Filters out high-noise periods (market open) and low-liquidity night sessions to focus on high-probability windows.

## Risk Validation (Monte Carlo)
To ensure the strategy's edge is not a result of "luck" or specific trade sequencing, I performed a **Monte Carlo Simulation (n=1000)** using Python.

![Monte Carlo Simulation](./assets/monte_carlo_plot.png)

* **Average Max Drawdown**: 5.17M JPY
* **Tail Risk (Worst Case)**: 17.68M JPY
* **Analysis**: The simulation confirms a high probability of positive expectancy regardless of trade order, though it highlights the inherent leverage risks of the Nikkei 225 index.

## Robustness & Limitations
During cross-asset testing (S&P 500, USD/JPY), this specific model showed significant performance decay. This confirms that the strategy is highly specialized to the **Nikkei 225's unique mean-reverting characteristics** and session volatility. It is not intended as a "Holy Grail" but as a specialized tool for the Japanese equity market.

## Tech Stack
- **Pine Script (v5)**: Strategy logic and backtesting.
- **Python (Pandas, NumPy, Matplotlib)**: Statistical analysis and Monte Carlo simulation.
