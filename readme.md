# Apex Portfolio Research

Apex is an institutional equity intelligence platform that automates the generation of stock research reports. Designed specifically for the Indian market, it uses a modular analytical pipeline to retrieve market data, evaluate corporate news and disclosures, analyze financial statement metrics in Indian Rupees and Crores, and synthesize broker sentiment before producing a unified investment memorandum.

The application is written in Python, using Streamlit for the user interface and Plotly for stock charts and sentiment visualization.

---

## Features

* **INR Financial Ingestion**: Reads real-time stock profiles via Yahoo Finance, converting financials to Rupees and Crores (Cr) / Lakh Crores (Lakh Cr) when NSE/BSE tickers are provided.
* **Modular Code Structure**: Splits tasks among four independent analysis modules, coordinating data flows in a clean pipeline.
* **Dynamic Pipeline Trace**: Displays active pipeline steps and internal logs chronologically in a terminal log viewer.
* **Offline Fallbacks**: Includes static profiles and financial statements for major Indian market enterprises (Reliance, TCS, HDFC Bank, Infosys, ICICI Bank) to allow local testing and evaluation without API keys.
* **LLM Engine Integration**: Supports optional connection to OpenAI and Gemini API endpoints via the sidebar parameters to run live broker reports.

---

## System Components

The research coordinator coordinates four independent analysis files:

1. **News and Events Analyst (`agents/news_agent.py`)**  
   Evaluates recent corporate filings, regulatory news, and press announcements to index major business catalysts and assign impact ratings.

2. **Financial and Accounting Analyst (`agents/earnings_agent.py`)**  
   Examines quarterly results, margins (including NIM for banking assets), cash flows, and management transcripts to extract operational guidance.

3. **Quantitative Sentiment Analyst (`agents/sentiment_agent.py`)**  
   Tracks options flow, NSE put-to-call open interest ratios (PCR), analyst target distributions, and domestic institutional investor (DII) and foreign institutional investor (FII) buy/sell trends.

4. **Lead Equity Strategist (`agents/analysis_agent.py`)**  
   Synthesizes the findings of the three analysts, sets valuation targets (stop-losses and target prices), and drafts the final investment memorandum.

---

## Project Structure

```text
project_4/
├── app.py                      # Main Streamlit dashboard application
├── requirements.txt            # Package dependencies
├── readme.md                   # Project documentation
├── agents/                     # Code modules for independent analyses
│   ├── __init__.py             # Class exports
│   ├── base_agent.py           # Core analyst interface and API configuration
│   ├── news_agent.py           # News and events disclosures parser
│   ├── earnings_agent.py       # Financial sheet and guidance parser
│   ├── sentiment_agent.py      # Wall Street ratings and options flow analyzer
│   └── analysis_agent.py       # Report synthesizer and strategist
└── utils/                      # Internal data utilities
    ├── __init__.py
    ├── financial_data.py       # Yahoo Finance APIs and offline fallback data
    └── report_generator.py     # Data pipeline and execution coordinator
```

---

## Setup and Installation

### Prerequisites
Make sure Python 3.9 or higher is installed on your system.

### Step 1: Install Dependencies
Open your command terminal in the project directory and run:
```bash
pip install -r requirements.txt
```

### Step 2: Launch the App
Start the Streamlit dashboard by running:
```bash
streamlit run app.py
```
By default, the platform will be hosted at `http://localhost:8501`. If another Streamlit process is active, it will automatically select the next available port.

---

## Usage Guide

1. **Select Enterprise**: Pick a stock from the dropdown in the sidebar (such as `RELIANCE.NS` or `TCS.NS`) or input a custom NSE/BSE symbol.
2. **Execute Analysis**: Click the **Execute Stock Analysis** button. The progress bar and status console will display active processing logs.
3. **View Performance**: The **Market Performance Monitor** tab displays key financial metrics and a daily line chart.
4. **Inspect Working Papers**: The **Analyst Working Papers** tab shows the intermediate findings and drafts produced by each module.
5. **Review Memorandum**: The **Investment Recommendation Memo** tab contains the finalized strategical report, price ranges, and options sentiment gauge. You can download the complete report as a Markdown document.
