import time
from typing import Dict, Any, Generator, List
from utils.financial_data import get_stock_info, get_stock_financials
from agents.news_agent import NewsAgent
from agents.earnings_agent import EarningsAgent
from agents.sentiment_agent import SentimentAgent
from agents.analysis_agent import AnalysisAgent

class ResearchCoordinator:
    def __init__(self, api_key: str = None, api_provider: str = None):
        self.api_key = api_key
        self.api_provider = api_provider
        
        # Instantiate agents
        self.news_agent = NewsAgent()
        self.earnings_agent = EarningsAgent()
        self.sentiment_agent = SentimentAgent()
        self.analysis_agent = AnalysisAgent()

    def run_research(self, symbol: str) -> Generator[Dict[str, Any], None, None]:
        """
        Coordinates the execution of the four agents.
        Yields structured updates for the UI to display in real-time.
        """
        symbol = symbol.upper().strip()
        
        # Step 1: Data Gathering
        yield {
            "stage": "data_gathering",
            "message": f"Initiating data ingestion pipeline for symbol: {symbol}...",
            "progress": 5
        }
        time.sleep(0.5)
        
        try:
            company_info = get_stock_info(symbol)
            financials = get_stock_financials(symbol)
            yield {
                "stage": "data_gathering",
                "message": f"Successfully loaded financial sheets and market profiles for {company_info.get('longName', symbol)}.",
                "progress": 15,
                "data": {"info": company_info, "financials": financials}
            }
        except Exception as e:
            yield {
                "stage": "error",
                "message": f"Infrastructural data ingestion failed: {str(e)}",
                "progress": 0
            }
            return

        # Initialize collector for agent reports
        reports = {}

        # Helper function to execute an agent (live or simulated)
        def execute_agent(agent, progress_start, progress_end, context=None) -> Generator[Dict[str, Any], None, None]:
            steps_run = []
            
            # Determine execution path based on API config
            if self.api_key and self.api_provider:
                agent_generator = agent.run_live(
                    symbol=symbol,
                    company_info=company_info,
                    financials=financials,
                    api_key=self.api_key,
                    api_provider=self.api_provider,
                    context=context
                )
            else:
                agent_generator = agent.run_simulated(
                    symbol=symbol,
                    company_info=company_info,
                    financials=financials,
                    context=context
                )
                
            for step in agent_generator:
                if step["type"] == "final":
                    # Store report and yield final state for this agent
                    reports[agent.name] = step["message"]
                    yield {
                        "stage": agent.name,
                        "agent_name": agent.name,
                        "avatar": agent.avatar,
                        "type": "final",
                        "content": step["message"],
                        "message": f"Agent {agent.name} has finalized its assessment.",
                        "progress": progress_end
                    }
                else:
                    # Capture intermediate logging steps
                    steps_run.append(step)
                    # Yield incremental progress
                    yield {
                        "stage": agent.name,
                        "agent_name": agent.name,
                        "avatar": agent.avatar,
                        "type": "log",
                        "log": step,
                        "message": step["message"],
                        # Interpolate progress bar values
                        "progress": progress_start + int((progress_end - progress_start) * 0.7)
                    }
                    time.sleep(0.3) # Natural visual pacing for the user

        # Step 2: News Agent execution
        yield {
            "stage": "news_analysis",
            "message": "Analyzing news and SEBI corporate disclosures...",
            "progress": 20
        }
        for update in execute_agent(self.news_agent, progress_start=20, progress_end=40):
            yield update

        # Step 3: Earnings Agent execution
        yield {
            "stage": "earnings_analysis",
            "message": "Parsing quarterly financial statement sheets and transcripts...",
            "progress": 40
        }
        for update in execute_agent(self.earnings_agent, progress_start=40, progress_end=60):
            yield update

        # Step 4: Sentiment Agent execution
        yield {
            "stage": "sentiment_analysis",
            "message": "Computing options flow and institutional equity flow indexes...",
            "progress": 60
        }
        for update in execute_agent(self.sentiment_agent, progress_start=60, progress_end=80):
            yield update

        # Step 5: Portfolio Analysis Agent execution
        yield {
            "stage": "final_synthesis",
            "message": "Compiling unified investment research memorandum...",
            "progress": 80
        }
        
        # Pass reports of other agents as context
        context = {
            "news_report": reports.get(self.news_agent.name, ""),
            "earnings_report": reports.get(self.earnings_agent.name, ""),
            "sentiment_report": reports.get(self.sentiment_agent.name, "")
        }
        
        for update in execute_agent(self.analysis_agent, progress_start=80, progress_end=100, context=context):
            yield update

        # Final complete trigger
        yield {
            "stage": "completed",
            "message": f"Investment research compilation complete for {symbol}.",
            "progress": 100,
            "final_report": reports.get(self.analysis_agent.name, "")
        }
