# Quantitative Finance & Algorithmic Trading Modules

### Overview
This repository contains a collection of Python modules designed for **Quantitative Finance**, **Risk Management**, and **Algorithmic Execution**. 

These tools were built to simulate the workflow of a **Hedge Fund** or **Proprietary Trading Desk**, covering the full lifecycle from Strategy Backtesting to Trade Execution logic.

### 📂 File Descriptions

| File Name | Type | Description | Status |
| :--- | :--- | :--- | :--- |
| `01_trend_following_backtest.py` | **Backtest** | A Long/Short strategy reacting to Moving Average crossovers. Includes **Maximum Drawdown** calculation to measure risk. | ✅ Simulation |
| `02_live_paper_trader.py` | **Paper Trading** | A virtual trading engine that fetches **Live NSE Data** (via `nselib`) and simulates order execution with configurable **Slippage Models**. | 🟢 Real-Time Data / Virtual Trade |
| `03_iceberg_execution_algo.py` | **Execution** | Algorithmic logic to split large "Parent Orders" into hidden "Child Orders" to minimize market impact (Institutional Execution). | ✅ Simulation |
| `04_vwap_analyzer.py` | **Analysis** | Computes **VWAP (Volume Weighted Average Price)** and generates a time-weighted execution schedule for institutional buying. | ✅ Simulation |
| `05_pairs_trading_stat_arb.py` | **Quant Strategy** | A **Statistical Arbitrage** model using the Engle-Granger test to find Cointegration between banking stocks (HDFC & ICICI) for Market Neutral strategies. | ✅ Backtest |

### 📊 Risk, Optimization & Derivatives Modules

| File Name | Type | Description | Status |
| :--- | :--- | :--- | :--- |
| `06_risk_manager_var.py` | **Risk Mgmt** | Calculates **Value at Risk (VaR)** using Historical Simulation. Essential for daily risk reporting and capital adequacy. | ✅ Analytical Tool |
| `07_portfolio_optimizer.py` | **Portfolio Mgmt** | Uses **Monte Carlo Simulation** to generate the Efficient Frontier and identify the portfolio with the Maximum Sharpe Ratio. | ✅ Optimization |
| `08_option_pricer_black_scholes.py` | **Derivatives** | Implements the **Black-Scholes Model** to calculate theoretical Call/Put prices and Greeks (Delta) for hedging logic. | ✅ Calculator |
| `09_sentiment_analysis_nlp.py` | **Alt Data** | A basic **Natural Language Processing (NLP)** script that scores financial news headlines as Bullish or Bearish. | ✅ NLP Demo |

### 🧠 Advanced Quant & AI Modules

| File Name | Type | Description | Status |
| :--- | :--- | :--- | :--- |
| `10_kalman_filter_trend.py` | **Signal Processing** | Implements a **Kalman Filter** to estimate the "true" stock price state from noisy data. Reduces lag compared to standard Moving Averages. | ✅ Math Model |
| `11_ml_xgboost_predictor.py` | **Machine Learning** | Uses **XGBoost (Gradient Boosting)** to predict future price direction (Up/Down) based on volatility and momentum features. | ✅ AI Model |
| `12_volatility_surface_3d.py` | **Derivatives** | Generates a **3D Volatility Surface** to visualize the "Option Smile" and Term Structure, critical for pricing exotic options. | ✅ 3D Visualization |
| `13_hft_orderbook_sim.py` | **Microstructure** | A **Limit Order Book (L2)** matching engine using Heap data structures. Simulates how HFT algos consume liquidity. | ✅ Simulation |

### 🧬 Deep Tech & High-Frequency Modules 

| File Name | Type | Description | Status |
| :--- | :--- | :--- | :--- |
| `14_deep_learning_lstm_forecast.py` | **Deep Learning** | Uses **LSTM (Long Short-Term Memory)** Neural Networks to predict time-series data, capturing non-linear patterns that standard regressions miss. | ✅ AI / Keras |
| `15_rl_trading_agent.py` | **Reinforcement Learning** | A **Q-Learning Agent** that learns to trade by trial-and-error. It optimizes a reward function (P&L) rather than predicting prices. | ✅ RL / AI |
| `16_hierarchical_risk_parity.py` | **Portfolio Optimization** | Uses **Graph Theory & Clustering** to build robust portfolios (HRP) that survive market crashes better than Markowitz models. | ✅ Machine Learning |
| `17_optimal_execution_almgren.py` | **Transaction Cost Analysis** | Implements the **Almgren-Chriss Model** to calculate the optimal trading trajectory, balancing Volatility Risk vs. Market Impact cost. | ✅ Quant Math |

### 🏛️ Infrastructure & Deep Tech

| File Name | Type | Description | Status |
| :--- | :--- | :--- | :--- |
| `18_event_driven_backtester.py` | **Architecture** | A robust **Event-Driven Engine** handling Market, Signal, and Order events in a FIFO queue. Prevents look-ahead bias and simulates real exchange latency. | ✅ Infrastructure |
| `19_triangular_arbitrage_graph.py` | **Graph Theory** | Uses **NetworkX** and the Bellman-Ford algorithm to detect negative cycles in Forex graphs, identifying risk-free **Triangular Arbitrage** opportunities. | ✅ Math / Algo |
| `20_signal_processing_emd.py` | **Physics** | Demonstrates **Signal Decomposition** (similar to HHT/EMD) to separate high-frequency market noise from underlying structural trends using physics-based transforms. | ✅ Signal Processing |
| `21_alternative_data_bert.py` | **NLP / LLM** | Utilizes **FinBERT (Transformers)** to analyze complex financial sentences, detecting nuanced sentiment that simple keyword algorithms miss. | ✅ AI / Deep Learning |

### 🛡️ Fortress Modules 

| File Name | Type | Description | Status |
| :--- | :--- | :--- | :--- |
| `22_high_performance_numba.py` | **Latency Eng** | Uses **JIT Compilation (Numba)** to accelerate Python loops by 100x, achieving C++ speeds for High-Frequency Trading. | ✅ Optimization |
| `23_market_making_avellaneda.py` | **HFT Strategy** | Implements the **Avellaneda-Stoikov Model** to dynamically adjust Bid-Ask spreads based on inventory risk. | ✅ Market Making |
| `24_tail_risk_evt.py` | **Risk Mgmt** | Uses **Extreme Value Theory (EVT)** and Generalized Pareto Distributions to model "Black Swan" events beyond standard VaR. | ✅ Fat-Tail Math |
| `25_covariance_shrinkage.py` | **Quant Math** | Applies **Ledoit-Wolf Shrinkage** to denoise Correlation Matrices, ensuring robust portfolio optimization even with limited data. | ✅ Linear Algebra |

### 🕵️‍♂️ Hidden Layer & Deep Research 

| File Name | Type | Description | Status |
| :--- | :--- | :--- | :--- |
| `26_synthetic_data_gan.py` | **Generative AI** | Uses a **GAN (Generative Adversarial Network)** to generate "Deep Fake" market data. Solves the problem of limited historical data for training AI models. | ✅ Research Grade |
| `27_copula_dependence.py` | **Adv. Risk** | Implements **Copulas** to model Tail Dependence. Captures "Crash Correlations" where assets move together only during extreme panic events. | ✅ PhD Mathematics |
| `28_order_flow_imbalance.py` | **Microstructure** | Calculates **Order Flow Imbalance (OFI)** from Level 2 data. This is a primary predictive signal used by HFT firms to forecast the next tick. | ✅ HFT Signal |
| `29_dynamic_hedge_kalman.py` | **Adaptive Quant** | Uses **Kalman Filters** to dynamically estimate the hedge ratio between two assets, allowing the strategy to adapt to changing market regimes instantly. | ✅ Adaptive Algo |

### 📐 Math & Probability 

| File Name | Type | Description | Status |
| :--- | :--- | :--- | :--- |
| `30_stochastic_volatility_heston.py` | **Stochastic Calc** | Simulates the **Heston Model** using Euler-Maruyama method. Models volatility as a dynamic process, capturing the "Leverage Effect" seen in real crashes. | ✅ Grad-Level Math |
| `31_regime_detection_hmm.py` | **Probabilistic** | Uses **Hidden Markov Models (HMM)** to unsupervisedly classify market data into "Regimes" (Bull, Bear, Sideways) for regime-switching strategies. | ✅ Machine Learning |
| `32_black_litterman_allocation.py` | **Bayesian** | Implements the **Black-Litterman Model** to blend "Market Equilibrium" with "Investor Views," solving the instability problems of standard Mean-Variance optimization. | ✅ Asset Mgmt Standard |
| `33_kelly_criterion_sizing.py` | **Risk Mgmt** | Demonstrates the **Kelly Criterion** for optimal position sizing. Proves mathematically why over-leveraging a winning strategy leads to long-term ruin. | ✅ Money Mgmt |

### 🔭 Research Frontiers 

| File Name | Type | Description | Status |
| :--- | :--- | :--- | :--- |
| `34_fractional_diff_stationarity.py` | **Financial ML** | Implements **Fractional Differentiation** (Lopez de Prado). Transforms non-stationary price data into stationary features without erasing trend memory, enabling better AI training. | ✅ ML Standard |
| `35_hawkes_process_arrival.py` | **Microstructure** | Simulates a **Hawkes Process** (Self-Exciting Point Process) to model trade arrival times. Captures the "viral" nature of liquidity and flash crashes. | ✅ HFT Math |
| `36_defi_amm_simulation.py` | **Crypto Quant** | Simulates a **Uniswap v2 AMM** ($x*y=k$) and an Arbitrage Bot. Demonstrates understanding of Decentralized Finance (DeFi) mechanics and on-chain pricing. | ✅ Web3 |
| `37_satellite_vision_signal.py` | **Alt Data** | Demonstrates a **Convolutional Neural Network (CNN)** logic to extract "Car Counts" from satellite imagery, generating trading signals from alternative data sources. | ✅ Computer Vision |

### 🌐 Multi-Asset & Factor Models 

| File Name | Type | Description | Status |
| :--- | :--- | :--- | :--- |
| `38_yield_curve_nelson_siegel.py` | **Fixed Income** | Calibrates the **Nelson-Siegel Model** to government bond data to build the Yield Curve. Essential for pricing bonds and detecting interest rate opportunities. | ✅ Rates Quant |
| `39_pca_risk_factors.py` | **Risk Mgmt** | Uses **PCA (Principal Component Analysis)** to decompose a portfolio into hidden Risk Factors (e.g., Market, Rates), revealing true diversification levels. | ✅ Factor Model |
| `40_exotic_barrier_option.py` | **Exotics** | Prices a **Knock-Out Barrier Option** using Monte Carlo simulations. Demonstrates handling of "Path Dependent" derivatives where history matters. | ✅ Structured Product |
| `41_pin_informed_trading.py` | **Microstructure** | Estimates the **PIN (Probability of Informed Trading)** metric. Detects toxic order flow by separating "Noise" volume from "Informed" volume. | ✅ Market Micro |

### ⚛️ Bleeding Edge 

| File Name | Type | Description | Status |
| :--- | :--- | :--- | :--- |
| `42_smart_order_router.py` | **Execution Algo** | A **Smart Order Router (SOR)** that splits orders across Fragmented Liquidity (NSE/BSE/Dark Pools) to minimize impact and fees. | ✅ Institutional Algo |
| `43_market_data_parser_binary.py` | **Low Level Eng** | Demonstrates **Binary Struct Parsing**. Reads raw byte-streams (simulating ITCH/TBT protocols) directly, avoiding slow string parsing. | ✅ HFT Engineering |
| `44_granger_causality_network.py` | **Econometrics** | Uses **Granger Causality** tests to determine "Lead-Lag" relationships between assets (e.g., Does Banking Sector lead IT Sector?). | ✅ Macro Research |
| `45_quantum_annealing_opt.py` | **Quantum Finance** | Implements **Simulated Annealing**, a physics-based heuristic used in Quantum Computing (D-Wave) to solve NP-Hard portfolio optimization problems. | ✅ Quantum Proxy |

### 🏭 Industrial Dominance 

| File Name | Type | Description | Status |
| :--- | :--- | :--- | :--- |
| `46_cuda_gpu_monte_carlo.py` | **Supercomputing** | Uses **NVIDIA CUDA Kernels** (via Numba) to run 10 million Monte Carlo simulations in parallel on the GPU. Reduces calculation time from minutes to milliseconds. | ✅ Hardware Accel |
| `47_supply_chain_propagation.py` | **Knowledge Graph** | Models the global supply chain as a **Directed Graph**. Mathematically propagates shocks (e.g., Earthquake at TSMC) downstream to predict stock drops before news hits. | ✅ Fundamental Quant |
| `48_clock_sync_ptp_sim.py` | **HFT Infra** | Simulates **Precision Time Protocol (PTP)**. Synchronizes internal server clocks with exchange timestamps to the microsecond to prevent latency arbitrage. | ✅ Low Latency |
| `49_limit_order_queue_estimator.py` | **Microstructure** | Tracks **FIFO Queue Position**. estimates exactly how many shares are ahead of your limit order and calculates "Time to Fill" based on trade velocity. | ✅ Execution Edge |

### 🏢 Institutional Scale 

| File Name | Type | Description | Status |
| :--- | :--- | :--- | :--- |
| `50_trade_surveillance_wash_graph.py` | **RegTech** | Uses **Graph Cycle Detection** to identify circular "Wash Trading" rings, a critical compliance requirement for all major exchanges. | ✅ Compliance |
| `51_weather_derivative_pricing.py` | **Exotic Asset** | Prices **HDD/CDD Weather Options** using temperature simulation. Used by energy desks to hedge against "Warm Winters." | ✅ Commodities |
| `52_tax_loss_harvesting_algo.py` | **Tax Alpha** | Automates **Tax Loss Harvesting**: realizing losses to offset gains while maintaining market exposure via correlated substitutes (Spider Strategy). | ✅ WealthTech |
| `53_distributed_grid_ray.py` | **Cloud Infra** | Implements **Distributed Computing** using `Ray`. Demonstrates how to scale analytics from a single laptop to a massive server cluster. | ✅ Scalability |


### 🛠️ Prerequisites
To run these scripts, you need Python installed along with the following financial libraries:

```bash
pip install numpy pandas matplotlib scipy yfinance statsmodels scikit-learn network textblob nselib tensorflow torch transformers xgboost lightgbm hmmlearn numba ray simpy

### ⚠️ Legal Disclaimer & Risk Disclosure

**IMPORTANT: PLEASE READ BEFORE USING THIS REPOSITORY.**

This repository contains advanced financial algorithms, including High-Frequency Trading (HFT) logic, Derivatives pricing models, and Tax optimization strategies. By accessing or using this code, you agree to the following terms:

### 1. No Financial Advice (SEBI/SEC Disclaimer)
* **Educational Use Only:** The code provided here is strictly for **Research and Educational purposes**. It demonstrates the *mathematics* and *engineering* behind Quantitative Finance.
* **Not a Recommendation:** Nothing in this repository constitutes investment advice, financial promotion, or a recommendation to buy/sell any security.
* **No Fiduciary Duty:** The author is not a SEBI Registered Investment Advisor (RIA), Portfolio Manager, or Broker-Dealer. Consult a certified financial professional before making investment decisions.

### 2. Algorithmic Trading Risks
* **Real Money Warning:** Using Python scripts to trade real money carries significant risk. A software bug, API failure, or internet outage can result in **100% loss of capital** in seconds.
* **No Warranty:** This software is provided "AS IS", without warranty of any kind. The author is not liable for any financial losses incurred from running these scripts in a live environment (Paper Trading or Real Trading).
* **Past Performance:** Backtesting results (e.g., File 01, 05) are simulated on historical data. **Past performance is not indicative of future results.** Real-world execution involves slippage, liquidity constraints, and transaction costs that may not be fully modeled here.

### 3. Compliance & Market Manipulation
* **Market Integrity:** Modules like `50_trade_surveillance_wash_graph.py` demonstrate how to **detect** illegal activity (Wash Trading). Using code to **execute** Wash Trades, Spoofing, or Layering is a criminal offense under SEBI (India) and SEC (USA) regulations.
* **HFT Regulations:** High-Frequency Trading (File 46, 48) is highly regulated. Deploying HFT strategies often requires specific exchange approvals, co-location agreements, and stress-testing certifications.

### 4. Technical & Data Risks
* **Data Accuracy:** Data fetched via open-source libraries (`yfinance`, `nselib`) is not real-time tick data and may contain errors or delays. Do not rely on it for precision pricing.
* **Hardware Usage:** Scripts involving GPU acceleration (`46_cuda_gpu_monte_carlo.py`) or Distributed Computing (`53_distributed_grid_ray.py`) can cause high hardware load. The author is not responsible for hardware damage or cloud computing costs.

### 5. Tax & Legal
* **Not Tax Advice:** The Tax Loss Harvesting algorithm (`52_tax_loss_harvesting_algo.py`) is a simulation of logic. Tax laws (Income Tax Act, 1961) change frequently. Do not use this code for tax filing without verifying with a Chartered Accountant.

---

### 📄 License
This project is licensed under the **MIT License** - you are free to use, modify, and distribute this software, but you hold the author harmless from any liability.