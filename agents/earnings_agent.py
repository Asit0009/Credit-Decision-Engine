import time
from typing import Dict, Any, Generator
from agents.base_agent import BaseAgent

class EarningsAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Financial & Accounting Analyst",
            role="Extracts performance metrics, guides operating targets, and parses corporate earnings transcripts.",
            avatar="FA"
        )

    def get_system_prompt(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> str:
        return (
            "You are a Chartered Financial Analyst (CFA) specializing in Indian corporate accounting and SEBI filings. "
            "Your task is to analyze the earnings metrics, income statements, and management call transcripts of the target company. "
            "Assess revenue growth, net profit trajectories, gross and operating margins, and balance sheet strength. "
            "Express figures in Indian Rupees (₹) and Crores (Cr) (where 1 Crore = 10 Million). Compare historical numbers "
            "against guidance targets and highlight management commentary concerning risks and capital expenditure (CapEx) trends."
        )

    def get_user_prompt(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> str:
        return (
            f"Analyze the financial statements and earnings reports of {company_info.get('longName', symbol)} ({symbol}).\n"
            f"Key Financial Figures (in ₹ Crores for Indian stocks, else Billions): {financials}\n"
            f"Official Guidance: {financials.get('earnings_guidance', 'No guidance provided.')}\n\n"
            "Format your analysis as a structured Markdown memo with the following headings:\n"
            "1. Financial Performance Analysis (Revenue, Net Income, EPS trends)\n"
            "2. Margin Analysis (Gross, Operating, Net Margin trend)\n"
            "3. Management Guidance Summary & Capital Allocation\n"
            "4. Earnings Call Risks & Opportunities (2 key takeaways from the call transcript)"
        )

    def run_simulated(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> Generator[Dict[str, str], None, None]:
        symbol = symbol.upper().strip()
        
        yield self.log_step("search", f"Querying SEBI filing database (Form 10-K / annual reports) for ticker: {symbol}...")
        time.sleep(1.0)
        
        yield self.log_step("analyze", f"Parsing latest earnings call transcript and quarterly financial statements...")
        time.sleep(1.2)
        
        # Corporate-specific custom simulation logs for Indian stocks (without emojis)
        if "RELIANCE" in symbol:
            yield self.log_step("analyze", "Extracting quarterly numbers: Jio revenue segments (₹25,300 Cr), O2C segment operational margins (13.5%)...")
            time.sleep(1.4)
            yield self.log_step("synthesize", "Modeling historical EBITDA trends and Capex allocations for 5G and new energy projects...")
            time.sleep(1.0)
            
            final_report = (
                "### Reliance Industries Limited (RELIANCE.NS) Earnings & Guidance Analysis\n\n"
                "**1. Financial Performance Analysis**\n"
                "* **Revenue Momentum:** Revenue grew steadily from ₹9,74,864 Cr in FY23 to ₹10,00,122 Cr in FY24, showing strong domestic consumption patterns across retail and digital services.\n"
                "* **EPS Growth:** EPS expanded from ₹96.20 to ₹102.50, supported by solid domestic consumer additions.\n"
                "* **Net Profit:** Maintained leading position in the corporate sector at over ₹79,00,000 Cr, showcasing robust cash flow generation.\n\n"
                "**2. Margin Analysis**\n"
                "* **Retail Operating EBITDA Margin:** Remained strong at **8.4%**, indicating high supply chain efficiency in retail logistics.\n"
                "* **Consolidated Operating Margin:** Held steady at **13.5%**, supported by gas realizations from KG-D6 block offsetting petrochemical margin compressions.\n\n"
                "**3. Management Guidance Summary & Capital Allocation**\n"
                "* **Guidance Target:** Management expects double-digit growth in retail sales and digital platform subscriptions, with consolidated capex scaling down in FY25.\n"
                "* **Capital Allocation:** Reinvestment focused on green energy infrastructure and gradual retail store expansion, while holding dividends steady.\n\n"
                "**4. Transcript Risks & Opportunities**\n"
                "* **Risk (Consumer Spending Slowdown):** CFO Srikanth Venkatachari noted that rural consumption remains sensitive to inflation, requiring promotional support.\n"
                "* **Opportunity (ARPU Expansion):** Management highlighted that 5G service adoption is preparing the telecom segment for substantial average revenue per user (ARPU) expansion."
            )
        elif "TCS" in symbol:
            yield self.log_step("analyze", "Extracting quarterly numbers: IT services segment margins (24.6%), banking domain revenue shares...")
            time.sleep(1.4)
            yield self.log_step("synthesize", "Modeling operating cash flow conversions and calculating employee utilization ratios (85.2%)...")
            time.sleep(1.0)
            
            final_report = (
                "### Tata Consultancy Services Limited (TCS.NS) Earnings & Guidance Analysis\n\n"
                "**1. Financial Performance Analysis**\n"
                "* **Revenue Trends:** Revenue increased from ₹2,25,458 Cr in FY23 to ₹2,40,893 Cr in FY24, reflecting resilient IT services demand despite global macro headwinds.\n"
                "* **EPS Trajectory:** Diluted EPS expanded from ₹115.20 to ₹125.80, driven by operational efficiencies.\n"
                "* **Net Profit:** Expanded to ₹45,910 Cr, displaying strong profit conversion.\n\n"
                "**2. Margin Analysis**\n"
                "* **Operating Margin:** Maintained at **24.6%**, one of the highest in the IT services sector, showcasing excellent control over subcontracting and hiring costs.\n"
                "* **Subcontracting Expense:** Reduced to 6.2% of total revenues, contributing directly to margin defense.\n\n"
                "**3. Management Guidance Summary & Capital Allocation**\n"
                "* **Guidance Target:** Management targets an operating margin band of 25-27% for FY25, supported by the execution of high-margin cloud contracts and optimization of resource pipelines.\n"
                "* **Capital Return:** Consistently high dividend payout ratio, with special dividends declared in Q3.\n\n"
                "**4. Transcript Risks & Opportunities**\n"
                "* **Risk (Discretionary Budget Delays):** CEO K. Krithivasan noted that banking and retail sector clients in North America continue to optimize budgets, delaying large new project starts.\n"
                "* **Opportunity (GenAI Platform Adoption):** Management highlighted a massive pipeline in cloud migration and GenAI services, with over 100 pilots currently underway."
            )
        elif "HDFCBANK" in symbol:
            yield self.log_step("analyze", "Extracting quarterly numbers: Net Interest Income (₹29,000 Cr), non-interest income shares...")
            time.sleep(1.4)
            yield self.log_step("synthesize", "Modeling Net Interest Margins (NIM) contraction and deposit cost adjustments...")
            time.sleep(1.0)
            
            final_report = (
                "### HDFC Bank Limited (HDFCBANK.NS) Earnings & Guidance Analysis\n\n"
                "**1. Financial Performance Analysis**\n"
                "* **Revenue Growth:** Total revenue surged to ₹2,45,000 Cr in FY24 post-merger with HDFC Corp, reflecting the combined balance sheet scale.\n"
                "* **EPS Trajectory:** EPS grew from ₹75.20 to ₹80.10, indicating stable dilution management.\n"
                "* **Net Profit:** Stood at ₹60,800 Cr in FY24, displaying the bank's leading profit engine.\n\n"
                "**2. Margin Analysis**\n"
                "* **Net Interest Margin (NIM):** NIM normalized at **3.4%** in recent quarters, compressed from the pre-merger peak of 4.1% due to HDFC Corp's higher borrowing costs.\n"
                "* **Cost-to-Income Ratio:** Maintained at **39.2%**, showcasing digital operational efficiencies.\n\n"
                "**3. Management Guidance Summary & Capital Allocation**\n"
                "* **Guidance Target:** Management guides for a gradual recovery in NIMs to 3.5-3.7% over the next 4-6 quarters, supported by CASA deposit growth. Loan growth is projected to be slightly below deposit growth to adjust the LDR ratio.\n"
                "* **Capital Adequacy:** Capital Adequacy Ratio remains comfortable at 18.8%, far exceeding regulatory requirements.\n\n"
                "**4. Transcript Risks & Opportunities**\n"
                "* **Risk (Liquidity Pressures):** CEO Sashidhar Jagdishan emphasized that deposit growth is the primary constraint, as systemic liquidity in India remains tight.\n"
                "* **Opportunity (Mortgage Cross-sell):** The merger allows HDFC Bank to cross-sell banking products to HDFC Corp's mortgage clients, representing a large untapped customer base."
            )
        elif "INFY" in symbol:
            yield self.log_step("analyze", "Extracting quarterly numbers: Operating margins (20.8%), retail and energy segment contributions...")
            time.sleep(1.4)
            yield self.log_step("synthesize", "Modeling EBITDA margins and resource utilization optimizations...")
            time.sleep(1.0)
            
            final_report = (
                "### Infosys Limited (INFY.NS) Earnings & Guidance Analysis\n\n"
                "**1. Financial Performance Analysis**\n"
                "* **Revenue Trends:** Revenue grew from ₹1,46,767 Cr in FY23 to ₹1,53,670 Cr in FY24, showing steady execution across core IT segments.\n"
                "* **EPS Trajectory:** EPS rose from ₹57.80 to ₹63.10, aligned with top-line growth.\n"
                "* **Net Profit:** Expanded to ₹26,233 Cr, showing solid profit conversion.\n\n"
                "**2. Margin Analysis**\n"
                "* **Operating Margin:** Stable at **20.8%**, supported by project 'Maximus' cost savings, which offset domestic wage inflation.\n"
                "* **Utilization Rate:** Maintained at **84.8%** (excluding trainees), indicating efficient resource allocation.\n\n"
                "**3. Management Guidance Summary & Capital Allocation**\n"
                "* **Guidance Target:** Management guides for a revenue growth target of 1-3% in CC and operating margins in the 20-22% band for FY25.\n"
                "* **Capital Allocation:** Reinvestment focused on AI cloud platform Topaz and returning cash through dividends and buybacks.\n\n"
                "**4. Transcript Risks & Opportunities**\n"
                "* **Risk (Discretionary Spend Compressions):** CEO Salil Parekh noted that client decision-making on large discretionary programs remains slow, delaying project starts.\n"
                "* **Opportunity (AI Pipeline):** Management highlighted a strong pipeline of AI and cloud migrations, with key wins in telecom and retail segments."
            )
        else:
            # Generic fallback mock financials for Indian stocks
            yield self.log_step("analyze", f"Analyzing financials for {symbol} with historical balances...")
            time.sleep(1.0)
            yield self.log_step("synthesize", "Extracting key financial trends and calculating margin variances...")
            time.sleep(0.8)
            
            final_report = (
                f"### {symbol} Earnings & Guidance Analysis\n\n"
                "**1. Financial Performance Analysis**\n"
                f"* **Revenue Growth:** Steady upward trajectory (annual growth of ~12.2% in ₹ Crores), demonstrating local market validation.\n"
                f"* **EPS Trends:** EPS rose from ₹24.0 to ₹29.0, aligned with domestic growth.\n"
                "* **Net Income:** Solid profit conversion, indicating steady capital discipline.\n\n"
                "**2. Margin Analysis**\n"
                f"* **Operating Margin:** Stable at **20.0%**, indicating disciplined management of domestic sales and overhead.\n"
                "* **Gross Margin:** Maintained at standard historical levels with minimal input-cost fluctuation.\n\n"
                "**3. Management Guidance Summary & Capital Allocation**\n"
                f"* **Guidance:** {financials.get('earnings_guidance')}\n"
                "* **Capital Allocation:** Reinvestment focused on domestic capacity expansion and research, supporting dividend stability.\n\n"
                "**4. Transcript Risks & Opportunities**\n"
                "* **Risk (Logistics Costs):** Management cited rising domestic freight costs and supply chain constraints as margins risks.\n"
                "* **Opportunity (Automation):** Transition to automated distribution networks is projected to lower long-term fulfillment costs."
            )
            
        yield self.log_step("final", final_report)
