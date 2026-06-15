import time
from typing import Dict, Any, Generator
from agents.base_agent import BaseAgent

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Lead Equity Strategist",
            role="Synthesizes multi-agent research inputs to compile institutional-grade equity research and investment ratings.",
            avatar="LS"
        )

    def get_system_prompt(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> str:
        return (
            "You are the Lead Equity Strategist and Head of Equity Research at a premier institutional investment fund in India (Mumbai). "
            "Your job is to read the findings from your sub-analysts: the News & Events Analyst, the Financial & Accounting Analyst, "
            "and the Quantitative Sentiment Analyst. Synthesize their analyses, combine it with the company profile and financials, "
            "and produce a final, definitive Investment Research Report. You must issue a formal investment rating "
            "(BUY, HOLD, or SELL), define an explicit Target Price and Stop-Loss Level in Indian Rupees (₹), outline a detailed "
            "Investment Thesis, and list key risks and near-term price catalysts."
        )

    def get_user_prompt(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> str:
        news_report = context.get("news_report", "No report available.") if context else "No report available."
        earnings_report = context.get("earnings_report", "No report available.") if context else "No report available."
        sentiment_report = context.get("sentiment_report", "No report available.") if context else "No report available."
        
        return (
            f"Review the primary data for {company_info.get('longName', symbol)} ({symbol}):\n"
            f"Company Metadata: {company_info}\n"
            f"Key Financials (₹ Crores for Indian stock, else Billions): {financials}\n\n"
            f"--- News Analyst Findings ---\n{news_report}\n\n"
            f"--- Earnings Analyst Findings ---\n{earnings_report}\n\n"
            f"--- Sentiment Analyst Findings ---\n{sentiment_report}\n\n"
            "Generate a highly professional, comprehensive, and cohesive Investment Research Report.\n"
            "Format the output strictly using Markdown, structured with the following headings:\n"
            "# EQUITY RESEARCH MEMORANDUM: [Company Name] ([Ticker])\n"
            "**Recommendation:** [BUY/HOLD/SELL] | **Target Price:** ₹[Value] | **Stop-Loss:** ₹[Value]\n\n"
            "## 1. Executive Summary & Investment Thesis\n"
            "## 2. Multi-Agent Analysis Synthesis\n"
            "* **News & Events Catalyst Assessment:** [Synthesis]\n"
            "* **Financial Performance & Guidance Strength:** [Synthesis]\n"
            "* **Market Sentiment Consensus:** [Synthesis]\n"
            "## 3. Financial Summary Table (clearly label units in ₹ Crores)\n"
            "## 4. Key Upside Catalysts\n"
            "## 5. Primary Downside Risks\n"
            "## 6. Portfolio Construction Recommendation"
        )

    def run_simulated(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> Generator[Dict[str, str], None, None]:
        symbol = symbol.upper().strip()
        
        yield self.log_step("analyze", "Reviewing findings from News & Events Analyst, Financial Analyst, and Sentiment Analyst...")
        time.sleep(1.2)
        
        yield self.log_step("synthesize", "Reconciling valuations, target price spreads, and stop-loss support lines in INR (₹)...")
        time.sleep(1.4)
        
        yield self.log_step("synthesize", "Drafting formal investment thesis and risk management parameters...")
        time.sleep(1.0)
        
        # Corporate-specific custom simulation reports for Indian stocks (without emojis)
        if "RELIANCE" in symbol:
            final_report = (
                "# EQUITY RESEARCH MEMORANDUM: Reliance Industries Limited (RELIANCE.NS)\n"
                "**Recommendation:** **BUY** | **Current Price:** ₹2,950.45 | **Target Price:** ₹3,250.00 | **Stop-Loss:** ₹2,750.00\n\n"
                "---\n\n"
                "## 1. Executive Summary & Investment Thesis\n"
                "Reliance Industries Limited (RIL) represents a high-conviction conglomerate play on India's consumption and digital story. The core investment thesis is anchored in two structural growth engines: retail scale and telecom (Jio) consolidation. With telecom tariff hikes on the horizon, Jio is poised for substantial ARPU expansion and high EBITDA conversions. Simultaneously, the retail segment leverages its massive brick-and-mortar footprint to capture urban and rural retail markets. The traditional Oil-to-Chemicals (O2C) segment acts as a stable cash generator, funding RIL's massive capital expenditure pivot into green energy giga-factories in Gujarat.\n\n"
                "## 2. Multi-Agent Analysis Synthesis\n"
                "* **News & Events Catalyst Assessment:** Highly positive. Expected telecom tariff increases represent a major near-term catalyst. Progress on green energy facility commissions adds to strategic long-term value.\n"
                "* **Financial Performance & Guidance Strength:** Strong. Revenue grew to ₹10,00,122 Cr in FY24, supported by margins of 13.5% and stabilizing capital expenditures as telecom rollout concludes.\n"
                "* **Market Sentiment Consensus:** Bullish. Broad institutional backing (DII overweight positions) and option put/call ratio of 0.88 indicate active accumulation on dips.\n\n"
                "## 3. Financial Summary Table (₹ Crores)\n\n"
                "| Financial Metric | FY 2023 | FY 2024 | FY 2025 (Est) |\n"
                "| :--- | :---: | :---: | :---: |\n"
                "| **Revenue (₹ Crores)** | ₹9,74,864 | ₹10,00,122 | ₹10,85,000 |\n"
                "| **Net Income (₹ Crores)** | ₹73,670 | ₹79,020 | ₹85,400 |\n"
                "| **Operating Margin** | 13.2% | 13.5% | 14.1% |\n"
                "| **EPS (Diluted in ₹)** | ₹96.20 | ₹102.50 | ₹112.00 |\n\n"
                "## 4. Key Upside Catalysts\n"
                "1. **Telecom Tariff Hike Execution:** Direct expansion in margins and ARPU due to consolidated market structure.\n"
                "2. **Retail/Jio IPO Spin-offs:** Potential value unlocking through independent listings of Jio and Reliance Retail.\n\n"
                "## 5. Primary Downside Risks\n"
                "1. **Commodity Downcycles:** Volatility in oil refining margins impacting cash flow generation.\n"
                "2. **Capital Over-allocation:** Delayed earnings conversion from massive green energy capex pipelines.\n\n"
                "## 6. Portfolio Construction Recommendation\n"
                "Recommend maintaining RIL as a **Core Overweight** holding in domestic Indian portfolios (5% to 6% target allocation). Accumulate shares on market corrections with a stop-loss support set at ₹2,750.00."
            )
        elif "TCS" in symbol:
            final_report = (
                "# EQUITY RESEARCH MEMORANDUM: Tata Consultancy Services Limited (TCS.NS)\n"
                "**Recommendation:** **BUY** | **Current Price:** ₹3,850.20 | **Target Price:** ₹4,200.00 | **Stop-Loss:** ₹3,600.00\n\n"
                "---\n\n"
                "## 1. Executive Summary & Investment Thesis\n"
                "TCS remains the premier IT services exporter in India, representing a cash-generative compounding asset. The company's core investment thesis is built on its market-leading operating margin defense (24.6% in FY24) and high customer retention. Despite macroeconomic delays in client decision-making in North America, TCS has captured large deal pipelines (BSNL equipment rollout, UK public sector deals). High cash conversion rates support continuous shareholder returns through dividends and buybacks, providing a strong floor to valuations.\n\n"
                "## 2. Multi-Agent Analysis Synthesis\n"
                "* **News & Events Catalyst Assessment:** Positive. Significant domestic and international order wins protect revenue pipelines. Attrition normalization down to 12.5% lowers HR overhead.\n"
                "* **Financial Performance & Guidance Strength:** Resilient. Operating margins of 24.6% demonstrate cost control, with management guiding for a return to the 25-27% band as large deals ramp up.\n"
                "* **Market Sentiment Consensus:** Moderately Bullish. Stable retail interest and consistent DII accumulation offset FII IT underweight positions.\n\n"
                "## 3. Financial Summary Table (₹ Crores)\n\n"
                "| Financial Metric | FY 2023 | FY 2024 | FY 2025 (Est) |\n"
                "| :--- | :---: | :---: | :---: |\n"
                "| **Revenue (₹ Crores)** | ₹2,25,458 | ₹2,40,893 | ₹2,62,000 |\n"
                "| **Net Income (₹ Crores)** | ₹42,147 | ₹45,910 | ₹50,200 |\n"
                "| **Operating Margin** | 24.1% | 24.6% | 25.2% |\n"
                "| **EPS (Diluted in ₹)** | ₹115.20 | ₹125.80 | ₹137.50 |\n\n"
                "## 4. Key Upside Catalysts\n"
                "1. **Discretionary BFSI Recovery:** Earlier-than-expected recovery of North American IT budgets.\n"
                "2. **BSNL Billing Ramp:** Faster execution of domestic networking projects, driving billing recognitions.\n\n"
                "## 5. Primary Downside Risks\n"
                "1. **Sustained Western Slowdown:** Continued high-interest rates in US/EU restricting enterprise capex budgets.\n"
                "2. **Wage Inflation:** Increased employee retention costs if industry hiring rates surge.\n\n"
                "## 6. Portfolio Construction Recommendation\n"
                "Recommend maintaining TCS as an **Overweight Defensive** holding (3.5% to 4.5% allocation). The stock is an excellent defensive anchor during periods of market volatility, with a stop-loss at ₹3,600.00."
            )
        elif "HDFCBANK" in symbol:
            final_report = (
                "# EQUITY RESEARCH MEMORANDUM: HDFC Bank Limited (HDFCBANK.NS)\n"
                "**Recommendation:** **HOLD** | **Current Price:** ₹1,550.80 | **Target Price:** ₹1,700.00 | **Stop-Loss:** ₹1,430.00\n\n"
                "---\n\n"
                "## 1. Executive Summary & Investment Thesis\n"
                "HDFC Bank is in a transitional consolidation phase following its merger with mortgage lender HDFC Corp. The long-term synergy potential is immense, but near-term pressure centers on deposit growth. The bank must mobilize retail deposits aggressively to normalize its Loan-to-Deposit Ratio (LDR), resulting in higher cost of funds and compressed NIMs (3.4% in FY24). While the credit profile remains pristine (Gross NPAs under 1.3%), loan growth is projected to be moderate to manage liquidity buffers. Accumulation should be done gradually as margins establish a bottom.\n\n"
                "## 2. Multi-Agent Analysis Synthesis\n"
                "* **News & Events Catalyst Assessment:** Neutral. Rapid branch expansion is positive for deposit gathering, but offset by regulatory scrutiny on bank LDRs.\n"
                "* **Financial Performance & Guidance Strength:** Stable. Post-merger revenue grew to ₹2,45,000 Cr, but NIM compression requires close observation.\n"
                "* **Market Sentiment Consensus:** Neutral. Option chain put/call ratio of 1.05 and FII reallocations reflect near-term caution, offset by DII buying support.\n\n"
                "## 3. Financial Summary Table (₹ Crores)\n\n"
                "| Financial Metric | FY 2023 | FY 2024 | FY 2025 (Est) |\n"
                "| :--- | :---: | :---: | :---: |\n"
                "| **Revenue (₹ Crores)** | ₹2,05,000 | ₹2,45,000 | ₹2,90,000 |\n"
                "| **Net Income (₹ Crores)** | ₹46,000 | ₹60,800 | ₹71,200 |\n"
                "| **Operating Margin** | 38.5% | 39.2% | 39.8% |\n"
                "| **EPS (Diluted in ₹)** | ₹75.20 | ₹80.10 | ₹93.50 |\n\n"
                "## 4. Key Upside Catalysts\n"
                "1. **Rapid Deposit Inflows:** Successful CASA mobilization easing LDR and cost of funds pressures.\n"
                "2. **Cross-Selling Synergies:** Rapid cross-selling of insurance and deposits to mortgage clients.\n\n"
                "## 5. Primary Downside Risks\n"
                "1. **Systemic Liquidity Deficit:** Sustained tight liquidity in India driving up deposit interest rates.\n"
                "2. **Regulatory Interventions:** RBI directives concerning loan-deposit metrics or credit card charges.\n\n"
                "## 6. Portfolio Construction Recommendation\n"
                "Recommend a **Neutral / Equal Weight** stance (2.0% to 2.5% portfolio allocation). Maintain core positions but pause aggressive additions until NIMs bottom out. Technical support is strong at ₹1,430.00."
            )
        elif "INFY" in symbol:
            final_report = (
                "# EQUITY RESEARCH MEMORANDUM: Infosys Limited (INFY.NS)\n"
                "**Recommendation:** **HOLD** | **Current Price:** ₹1,480.15 | **Target Price:** ₹1,580.00 | **Stop-Loss:** ₹1,360.00\n\n"
                "---\n\n"
                "## 1. Executive Summary & Investment Thesis\n"
                "Infosys is navigating structural demand transitions as legacy maintenance deals face price-based competition. Growth is centered on generative AI through its 'Topaz' cloud automation platform, showing healthy order pipelines. However, conservative revenue guidance from management reflects slow contract conversions and cautious discretionary spend. With margins stable at 20.8% and dividend yields attractive, the stock is a solid hold during IT sector consolidations.\n\n"
                "## 2. Multi-Agent Analysis Synthesis\n"
                "* **News & Events Catalyst Assessment:** Neutral. Solid Topaz wins are offset by conservative management guidance revisions.\n"
                "* **Financial Performance & Guidance Strength:** Moderate. Operating margins of 20.8% reflect cost controls, supporting profit conversion to ₹26,233 Cr in FY24.\n"
                "* **Market Sentiment Consensus:** Neutral-to-positive. Options flow and consensus broker ratings indicate stable market expectations.\n\n"
                "## 3. Financial Summary Table (₹ Crores)\n\n"
                "| Financial Metric | FY 2023 | FY 2024 | FY 2025 (Est) |\n"
                "| :--- | :---: | :---: | :---: |\n"
                "| **Revenue (₹ Crores)** | ₹1,46,767 | ₹1,53,670 | ₹1,68,200 |\n"
                "| **Net Income (₹ Crores)** | ₹24,095 | ₹26,233 | ₹29,100 |\n"
                "| **Operating Margin** | 21.0% | 20.8% | 21.5% |\n"
                "| **EPS (Diluted in ₹)** | ₹57.80 | ₹63.10 | ₹70.20 |\n\n"
                "## 4. Key Upside Catalysts\n"
                "1. **Discretionary Spends Acceleration:** Earlier-than-expected recovery of enterprise client budgets.\n"
                "2. **Generative AI Monitisation:** Margin-accretive platform deals expanding revenue growth.\n\n"
                "## 5. Primary Downside Risks\n"
                "1. **Price Erosion:** Competitive pricing pressure in legacy maintenance contracts.\n"
                "2. **Talent Attrition Volatility:** Rising employee sub-contracting costs if project ramp-ups pick up speed.\n\n"
                "## 6. Portfolio Construction Recommendation\n"
                "Recommend an **Equal Weight** position (1.5% to 2.0% allocation). Accumulate on dips to support ranges with a stop-loss at ₹1,360.00."
            )
        else:
            # Generic fallback mock analysis for Indian stocks
            final_report = (
                f"# EQUITY RESEARCH MEMORANDUM: {company_info.get('longName', symbol)} ({symbol})\n"
                f"**Recommendation:** **HOLD** | **Current Price:** ₹500.00 | **Target Price:** ₹550.00 | **Stop-Loss:** ₹460.00\n\n"
                "---\n\n"
                "## 1. Executive Summary & Investment Thesis\n"
                f"{symbol} displays stable fundamentals in the Indian market with localized macro challenges. Core products continue to perform in line with expectation, but margin compression from inflation requires careful monitoring.\n\n"
                "## 2. Multi-Agent Analysis Synthesis\n"
                "* **News & Events Catalyst Assessment:** Neutral. Core expansion projects are scaling, but balanced by commodity costs.\n"
                f"* **Financial Performance & Guidance Strength:** Stable. Operating margins of {financials.get('operating_margin')[1]}% demonstrate stable execution in ₹ Crores.\n"
                "* **Market Sentiment Consensus:** Moderate Buy. Public and analyst targets reflect reasonable expectations on NSE.\n\n"
                "## 3. Financial Summary Table (₹ Crores)\n\n"
                "| Financial Metric | FY 2023 | FY 2024 | FY 2025 (Est) |\n"
                "| :--- | :---: | :---: | :---: |\n"
                f"| **Revenue (₹ Crores)** | ₹{financials.get('revenue')[0]:,.1f} | ₹{financials.get('revenue')[1]:,.1f} | ₹{financials.get('revenue')[2]:,.1f} |\n"
                f"| **Net Income (₹ Crores)** | ₹{financials.get('net_income')[0]:,.1f} | ₹{financials.get('net_income')[1]:,.1f} | ₹{financials.get('net_income')[2]:,.1f} |\n"
                f"| **Operating Margin** | {financials.get('operating_margin')[0]}% | {financials.get('operating_margin')[1]}% | {financials.get('operating_margin')[2]}% |\n"
                f"| **EPS (Diluted in ₹)** | ₹{financials.get('eps')[0]:,.2f} | ₹{financials.get('eps')[1]:,.2f} | ₹{financials.get('eps')[2]:,.2f} |\n\n"
                "## 4. Key Upside Catalysts\n"
                "1. **Strategic Market Penetration:** Rapid expansion of domestic distribution channels.\n"
                "## 5. Primary Downside Risks\n"
                "1. **Margin Volatility:** Sustained energy and logistics cost increases compressing margins.\n"
                "## 6. Portfolio Construction Recommendation\n"
                "Hold rating reflecting balanced risks. Maintain minor allocations within target sector portfolios."
            )
            
        yield self.log_step("final", final_report)
