import time
from typing import Dict, Any, Generator
from agents.base_agent import BaseAgent

class SentimentAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Quantitative Sentiment Analyst",
            role="Calculates quantitative market sentiment, retail interest, options pricing flow, and analyst ratings.",
            avatar="QS"
        )

    def get_system_prompt(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> str:
        return (
            "You are a Quantitative Sentiment Analyst specializing in the Indian stock market (NSE/BSE). "
            "Your role is to determine the prevailing market sentiment for the target ticker symbol. "
            "Synthesize qualitative data (financial media headlines, corporate filings) and quantitative metrics "
            "(sell-side broker ratings, option put/call open interest ratios on NSE, Foreign Institutional Investor (FII) "
            "and Domestic Institutional Investor (DII) flow trends, short interest, and retail volume momentum). "
            "Compute an overall Quantitative Sentiment Score from -100 (extreme fear) to +100 (extreme greed). "
            "Explain the weights of each component."
        )

    def get_user_prompt(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> str:
        return (
            f"Analyze the market sentiment signals for {company_info.get('longName', symbol)} ({symbol}).\n"
            f"Company Metadata: {company_info}\n\n"
            "Format your analysis as a structured Markdown memo with the following headings:\n"
            "1. Quantitative Sentiment Score (Explicitly define a score between -100 and +100)\n"
            "2. Analyst Consensus & Recommendations (Buy/Hold/Sell breakdowns, target price ranges in INR)\n"
            "3. Options Flow & Market Internals (Put/Call open interest ratios, FII/DII equity flow trends)\n"
            "4. Retail & Social Sentiment Indicators (Relative search volumes, retail discussion volumes)"
        )

    def run_simulated(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> Generator[Dict[str, str], None, None]:
        symbol = symbol.upper().strip()
        
        yield self.log_step("search", f"Querying NSE option chain open interest data for ticker: {symbol}...")
        time.sleep(1.0)
        
        yield self.log_step("analyze", f"Tracking FII and DII buying activity and institutional block trade disclosures on BSE/NSE...")
        time.sleep(1.2)
        
        yield self.log_step("synthesize", "Aggregating domestic brokerage research notes and average price targets...")
        time.sleep(1.0)

        # Corporate-specific custom simulation reports for Indian stocks (without emojis)
        if "RELIANCE" in symbol:
            final_report = (
                "### Reliance Industries Limited (RELIANCE.NS) Market Sentiment Analysis\n\n"
                "**1. Quantitative Sentiment Score**\n"
                "* **Score:** **+60 / 100** (Bullish)\n"
                "* **Sentiment Tone:** Positive. Large mutual funds (DIIs) are actively accumulating shares, and retail interest remains highly supportive of retail/telecom segment valuations.\n\n"
                "**2. Analyst Consensus & Recommendations**\n"
                "* **Consensus Rating:** **Buy**\n"
                "* **Recommendation Breakdown:** Buy: 32 | Hold: 5 | Sell: 2\n"
                "* **Price Target Spread:** Average target of **₹3,250.00** (implying a 10% upside from current levels). High target at ₹3,560.00, low target at ₹2,800.00.\n\n"
                "**3. Options Flow & Market Internals**\n"
                "* **Put/Call Ratio (PCR):** **0.88** (reflects structural bullish bias, call writing observed around the ₹3,100 strike).\n"
                "* **Institutional Flow:** Foreign Institutional Investors (FIIs) turned net buyers in recent weeks, while domestic mutual funds hold overweight positions.\n"
                "* **Short Interest:** Negligible, as short sellers avoid large index weight shares due to dividend distributions and hedging.\n\n"
                "**4. Retail & Social Sentiment Indicators**\n"
                "* **Search Trends:** Increased searches on Jio tariff announcements and green energy gigafactories.\n"
                "* **Social Media Sentiment:** 75% positive sentiment score on local investor message boards, reflecting high retail optimism."
            )
        elif "TCS" in symbol:
            final_report = (
                "### Tata Consultancy Services Limited (TCS.NS) Market Sentiment Analysis\n\n"
                "**1. Quantitative Sentiment Score**\n"
                "* **Score:** **+35 / 100** (Resilient)\n"
                "* **Sentiment Tone:** Neutral-to-Bullish. Institutional flows are steady, but macro IT spending concerns keep absolute sentiment score moderate.\n\n"
                "**2. Analyst Consensus & Recommendations**\n"
                "* **Consensus Rating:** **Moderate Buy**\n"
                "* **Recommendation Breakdown:** Buy: 24 | Hold: 12 | Sell: 4\n"
                "* **Price Target Spread:** Average target of **₹4,120.00** (implying a 7% upside). High target at ₹4,450.00, low target at ₹3,700.00.\n\n"
                "**3. Options Flow & Market Internals**\n"
                "* **Put/Call Ratio (PCR):** **0.76** (indicates healthy options volume distribution, call open interest peaks around ₹4,000).\n"
                "* **FII/DII Positioning:** DIIs continue to accumulate on price dips, while FIIs hold neutral-to-underweight weights on Indian IT sector shares.\n\n"
                "**4. Retail & Social Sentiment Indicators**\n"
                "* **Search Trends:** Stable search volume, peaking during salary hikes and dividend announcements.\n"
                "* **Social Media Sentiment:** 68% positive tone on retail boards, focusing primarily on high dividend yields and buybacks."
            )
        elif "HDFCBANK" in symbol:
            final_report = (
                "### HDFC Bank Limited (HDFCBANK.NS) Market Sentiment Analysis\n\n"
                "**1. Quantitative Sentiment Score**\n"
                "* **Score:** **+20 / 100** (Neutral / Consolidation)\n"
                "* **Sentiment Tone:** Neutral. While long-term value is recognized, short-term options flow reflects hedging as the market monitors post-merger integration.\n\n"
                "**2. Analyst Consensus & Recommendations**\n"
                "* **Consensus Rating:** **Moderate Buy**\n"
                "* **Recommendation Breakdown:** Buy: 38 | Hold: 8 | Sell: 2\n"
                "* **Price Target Spread:** Average target of **₹1,750.00** (implying a 12.8% upside). High target at ₹1,950.00, low target at ₹1,500.00.\n\n"
                "**3. Options Flow & Market Internals**\n"
                "* **Put/Call Ratio (PCR):** **1.05** (reflects defensive hedging bias, heavy put writing near the ₹1,500 support level).\n"
                "* **FII/DII Positioning:** FIIs adjusted allocations post-merger, creating selling pressure, while DIIs absorbed shares aggressively to support valuations.\n\n"
                "**4. Retail & Social Sentiment Indicators**\n"
                "* **Search Trends:** High search volumes concerning HDFC mortgage accounts migration and CASA deposit campaigns.\n"
                "* **Social Media Sentiment:** 58% positive sentiment, with retail forums expressing impatience regarding the bank's sideways stock price consolidation."
            )
        elif "INFY" in symbol:
            final_report = (
                "### Infosys Limited (INFY.NS) Market Sentiment Analysis\n\n"
                "**1. Quantitative Sentiment Score**\n"
                "* **Score:** **+30 / 100** (Moderately Bullish)\n"
                "* **Sentiment Tone:** Neutral-to-positive. Guidance adjustments kept absolute sentiment moderate, offset by solid enterprise contract pipelines.\n\n"
                "**2. Analyst Consensus & Recommendations**\n"
                "* **Consensus Rating:** **Moderate Buy**\n"
                "* **Price Target Spread:** Average target of **₹1,620.00** (implying a 9.4% upside). High target at ₹1,780.00, low target at ₹1,400.00.\n\n"
                "**3. Options Flow & Market Internals**\n"
                "* **Put/Call Ratio (PCR):** **0.80** (standard options distribution, call open interest peaks around ₹1,550).\n"
                "* **FII/DII Positioning:** DII mutual funds maintain steady holdings, while FIIs show neutral-to-underweight positioning on IT sector shares.\n\n"
                "**4. Retail & Social Sentiment Indicators**\n"
                "* **Retail Tone:** Moderate engagement on public forums, focusing on AI platform Topaz wins and dividend yields."
            )
        else:
            # Generic fallback mock sentiment for Indian stocks
            final_report = (
                f"### {symbol} Market Sentiment Analysis\n\n"
                "**1. Quantitative Sentiment Score**\n"
                "* **Score:** **+25 / 100** (Mildly Bullish)\n"
                "* **Sentiment Tone:** Moderately positive. Stable trading volumes and standard macro expectations in the Indian market.\n\n"
                "**2. Analyst Consensus & Recommendations**\n"
                "* **Consensus Rating:** **Moderate Buy**\n"
                f"* **Price Target Spread:** Average price target points to ~10% upside from current trading ranges.\n\n"
                "**3. Options Flow & Market Internals**\n"
                "* **Put/Call Ratio (PCR):** **0.85** (standard option distribution, representing typical equity hedging on NSE).\n"
                "* **Institutional Flow:** DII mutual funds net buyers on dips, providing valuation support.\n\n"
                "**4. Retail & Social Sentiment Indicators**\n"
                f"* **Retail Tone:** Moderate engagement on public forums, mirroring broader Nifty sector trends."
            )
            
        yield self.log_step("final", final_report)
