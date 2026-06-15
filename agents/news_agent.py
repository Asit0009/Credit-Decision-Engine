import time
from typing import Dict, Any, Generator
from agents.base_agent import BaseAgent

class NewsAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="News & Events Analyst",
            role="Gathers recent news, corporate disclosures, and press releases to evaluate business events.",
            avatar="NE"
        )

    def get_system_prompt(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> str:
        return (
            "You are a Senior News & Event Analyst at an institutional investment fund in India. Your task is to scan recent news, "
            "press releases, and major event announcements for the given stock. Evaluate the significance, credibility, "
            "and potential financial impact of these developments. Categorize each event (e.g., regulatory approval, tariff hike, "
            "deal win, management changes) and assign an Impact Score from -10 (critical headwind) to +10 (critical tailwind). "
            "Outline your logic and provide a summarized memo for the Investment Committee."
        )

    def get_user_prompt(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> str:
        return (
            f"Analyze the recent news developments for {company_info.get('longName', symbol)} ({symbol}).\n"
            f"Company Sector: {company_info.get('sector')}\n"
            f"Business Summary: {company_info.get('longBusinessSummary')}\n\n"
            "Format your analysis as a structured Markdown memo with the following headings:\n"
            "1. Executive News Summary\n"
            "2. Top News Catalysts (listed in a table with Event, Category, Impact Score (-10 to +10), and Description)\n"
            "3. Operational Risks & Headwinds\n"
            "4. Immediate Catalyst Assessment (next 3-6 months)"
        )

    def run_simulated(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> Generator[Dict[str, str], None, None]:
        symbol = symbol.upper().strip()
        
        yield self.log_step("search", f"Querying SEBI disclosures and corporate press filings for ticker: {symbol}...")
        time.sleep(1.2)
        
        yield self.log_step("search", f"Scanning domestic financial media (Moneycontrol, ET, Livemint) for news matching {symbol}...")
        time.sleep(1.0)
        
        # Corporate-specific custom simulation logs for Indian Stocks (without emojis)
        if "RELIANCE" in symbol:
            yield self.log_step("analyze", "Filtering articles on Jio tariff hikes, retail store counts expansion, and refining margins (GRM) at Jamnagar...")
            time.sleep(1.5)
            yield self.log_step("synthesize", "Assessing news impact of green energy giga-factory commissions in Gujarat and retail IPO spin-off timelines...")
            time.sleep(1.2)
            
            final_report = (
                "### Reliance Industries Limited (RELIANCE.NS) News Analysis\n\n"
                "**1. Executive News Summary**\n"
                "Reliance is witnessing supportive operational news flow across its primary segments. Telecom (Jio) is expected to execute a 15-20% tariff hike, which will expand ARPUs and margins. Retail expansion continues at a rapid pace with over 18,000 active stores, while the traditional Oil-to-Chemicals (O2C) business is stabilizing despite global refining margin volatility. The long-term green energy project commissions in Gujarat are emerging as a major strategic catalyst.\n\n"
                "**2. Top News Catalysts**\n\n"
                "| Event | Category | Impact Score (-10 to +10) | Description |\n"
                "| :--- | :--- | :---: | :--- |\n"
                "| Telecom Tariff Hike | Strategic Pricing | **+8.5** | Projected 15-20% tariff increase in Jio to boost telecommunication margins and ARPU levels. |\n"
                "| New Energy Giga-Factories | Capacity Expansion | **+6.5** | Gradual rollout of solar and hydrogen cell manufacturing plants in Gujarat starting mid-2024. |\n"
                "| Refining Margin Volatility | Commodities | **-3.5** | Temporary compression in global gross refining margins (GRM) impacts chemical segments. |\n\n"
                "**3. Operational Risks & Headwinds**\n"
                "* **High Leverage:** Continuous capital expenditures across telecom and retail businesses keep net debt levels elevated.\n"
                "* **O2C Fluctuations:** Susceptibility to global crude pricing and Russian oil import discount fluctuations.\n\n"
                "**4. Immediate Catalyst Assessment**\n"
                "The core catalyst for the next 3-6 months is the official implementation date and consumer response to the telecom tariff hike, which will directly flow into high-margin service earnings."
            )
        elif "TCS" in symbol:
            yield self.log_step("analyze", "Filtering articles on deal wins (Aviva, BSNL contract ramp), global IT budgets, and return-to-office directives...")
            time.sleep(1.5)
            yield self.log_step("synthesize", "Assessing impact of BFSI spending delays in North America and attrition rates stabilization (down to 12.5%)...")
            time.sleep(1.2)
            
            final_report = (
                "### Tata Consultancy Services Limited (TCS.NS) News Analysis\n\n"
                "**1. Executive News Summary**\n"
                "TCS continues to demonstrate operational resilience in a challenging global IT expenditure environment. The company secured several multi-billion dollar deals, including a major cloud migration contract with Aviva and the roll-out of the nationwide BSNL 4G/5G contract. Attrition has successfully normalized down to 12.5%, reducing recruitment costs. However, soft discretionary IT spend in the BFSI sector in North America remains a short-term drag.\n\n"
                "**2. Top News Catalysts**\n\n"
                "| Event | Category | Impact Score (-10 to +10) | Description |\n"
                "| :--- | :--- | :---: | :--- |\n"
                "| BSNL 4G/5G Equipment Deal | Order Win | **+7.5** | Commencing billings for the mega BSNL consortium contract, securing domestic revenue streams. |\n"
                "| Attrition Normalization | Human Resources | **+4.0** | Attrition falling back to historical averages lowers onboarding costs and stabilizes projects. |\n"
                "| BFSI Discretionary Spending Cuts | Macro | **-4.5** | Delayed decision-making by North American banking clients limits short-term contract expansions. |\n\n"
                "**3. Operational Risks & Headwinds**\n"
                "* **Subdued US Demand:** High-interest rates in western markets compression IT discretionary budgets.\n"
                "* **Wage Inflation:** Annual salary cycles compress IT margins slightly unless offset by pricing power.\n\n"
                "**4. Immediate Catalyst Assessment**\n"
                "Management commentary on pipeline conversions for GenAI deals and billing commencements of the UK deals represent the key triggers over the next 2 quarters."
            )
        elif "HDFCBANK" in symbol:
            yield self.log_step("analyze", "Filtering articles on HDFC Corp merger consolidation, retail deposit mobilization, and regulatory compliance on LDR limits...")
            time.sleep(1.5)
            yield self.log_step("synthesize", "Evaluating net interest margin compressions and liquidity buffer allocations in response to RBI rules...")
            time.sleep(1.2)
            
            final_report = (
                "### HDFC Bank Limited (HDFCBANK.NS) News Analysis\n\n"
                "**1. Executive News Summary**\n"
                "Post-merger with HDFC Corp, HDFC Bank's news cycle is focused on deposit growth. To align its Loan-to-Deposit Ratio (LDR) with historical averages, the bank is running aggressive retail deposit mobilization campaigns. While loan growth remains robust, net interest margins (NIM) are temporarily compressed due to higher deposit costs. The bank's credit profile remains immaculate, with negligible Gross NPA levels.\n\n"
                "**2. Top News Catalysts**\n\n"
                "| Event | Category | Impact Score (-10 to +10) | Description |\n"
                "| :--- | :--- | :---: | :--- |\n"
                "| Branch Expansion Program | Strategic Growth | **+6.0** | Adding 1,000+ branches annually to capture low-cost CASA deposits in semi-urban areas. |\n"
                "| LDR Compression Concerns | Asset-Liability | **-5.0** | RBI scrutiny on elevated loan-to-deposit ratio forces a slower loan growth profile. |\n"
                "| Stable Credit Asset Quality | Risk Management | **+5.5** | Net NPA ratios remain under 0.35%, indicating excellent underwritings. |\n\n"
                "**3. Operational Risks & Headwinds**\n"
                "* **Margin Compressions:** Elevated cost of funds due to intense competition for retail bank deposits.\n"
                "* **Merger Integration Drag:** Legal and compliance adjustments post-merger require administrative overhead.\n\n"
                "**4. Immediate Catalyst Assessment**\n"
                "Deposit growth rates relative to loan growth over the next two quarters will determine whether the market re-rates the bank back to its historical premium multiples."
            )
        elif "INFY" in symbol:
            yield self.log_step("analyze", "Filtering articles on large deal signings, AI cloud platform Topaz adoption, and executive exits...")
            time.sleep(1.5)
            yield self.log_step("synthesize", "Assessing implications of downward guidance revisions and margin pressure from sub-contracting costs...")
            time.sleep(1.2)
            
            final_report = (
                "### Infosys Limited (INFY.NS) News Analysis\n\n"
                "**1. Executive News Summary**\n"
                "Infosys is focusing on generative AI through its newly launched 'Topaz' platform, securing several high-profile enterprise deals. However, guidance adjustments from management have created short-term stock volatility. While contract pipelines are large, client decision-making remains slow, resulting in delayed revenue conversion. Talent attrition has normalized, helping manage labor costs.\n\n"
                "**2. Top News Catalysts**\n\n"
                "| Event | Category | Impact Score (-10 to +10) | Description |\n"
                "| :--- | :--- | :---: | :--- |\n"
                "| Infosys Topaz Platform Ramp | Product Release | **+7.0** | Rapid expansion of AI-driven cloud automation services with key fortune-500 enterprise clients. |\n"
                "| Guidance Adjustments | Earnings Guide | **-6.0** | Lowering conservative revenue growth guidance due to delayed project ramp-ups. |\n"
                "| Margin Optimization Plans | Efficiency | **+4.5** | Structural cost savings under project 'Maximus' driving margin recoveries. |\n\n"
                "**3. Operational Risks & Headwinds**\n"
                "* **Client Decision Delays:** Slow conversion of Total Contract Value (TCV) into actual billed revenue.\n"
                "* **Competition:** Price wars in commoditized legacy maintenance contracts compression margins.\n\n"
                "**4. Immediate Catalyst Assessment**\n"
                "The primary driver is the stabilization of discretionary spend by European and US clients, expected to show signs of recovery by Q3."
            )
        else:
            # Generic fallback mock news for Indian stocks
            yield self.log_step("analyze", f"Filtering recent publications and analyst notes for {symbol}...")
            time.sleep(1.2)
            yield self.log_step("synthesize", "Identifying core operational events, SEBI disclosures, and domestic market risks...")
            time.sleep(1.0)
            
            final_report = (
                f"### {symbol} News Analysis\n\n"
                "**1. Executive News Summary**\n"
                f"Operational trends for {symbol} indicate steady placement in the Indian corporate sector, balanced by macro headwinds (inflation, interest rates). News flows show solid domestic demand and capacity expansion, offset slightly by high input costs.\n\n"
                "**2. Top News Catalysts**\n\n"
                f"| Event | Category | Impact Score (-10 to +10) | Description |\n"
                "| :--- | :--- | :---: | :--- |\n"
                f"| Capital Expansion Project | Strategic | **+5.5** | New manufacturing facility approvals signed, increasing production capacity. |\n"
                "| Commodity Input Pressures | Macroeconomics | **-3.0** | Raw material pricing tracking higher, potentially compressing margins in near-term. |\n\n"
                "**3. Operational Risks & Headwinds**\n"
                "* **Competition:** Domestic and global imports pricing pressures forcing minor price concessions.\n\n"
                "**4. Immediate Catalyst Assessment**\n"
                "The upcoming quarterly earnings release serves as the primary check on revenue momentum and operating leverage."
            )
            
        yield self.log_step("final", final_report)
