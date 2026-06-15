import time
import os
import json
from typing import Generator, Dict, Any, List

class BaseAgent:
    def __init__(self, name: str, role: str, avatar: str):
        self.name = name
        self.role = role
        self.avatar = avatar

    def log_step(self, step_type: str, message: str) -> Dict[str, str]:
        """Format a step update for UI streaming."""
        return {
            "agent": self.name,
            "avatar": self.avatar,
            "type": step_type,  # e.g., 'search', 'analyze', 'synthesize', 'final'
            "message": message,
            "timestamp": time.strftime("%H:%M:%S")
        }

    def run_simulated(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> Generator[Dict[str, str], None, None]:
        """
        Simulate the agent's work step-by-step.
        Must be overridden by child classes to yield sequential log steps, ending with a 'final' report block.
        """
        yield self.log_step("status", f"Initializing {self.name} for {symbol}...")
        time.sleep(1.0)
        yield self.log_step("final", f"Analysis completed by {self.name} base agent.")

    def run_live(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], api_key: str, api_provider: str, context: Dict[str, Any] = None) -> Generator[Dict[str, str], None, None]:
        """
        Execute the agent's reasoning using a live LLM (OpenAI or Gemini).
        Streams intermediate steps and outputs the final structured analysis.
        """
        yield self.log_step("status", f"Connecting {self.name} to {api_provider} API...")
        time.sleep(0.5)
        
        system_prompt = self.get_system_prompt(symbol, company_info, financials, context)
        user_prompt = self.get_user_prompt(symbol, company_info, financials, context)
        
        try:
            if api_provider.lower() == "openai":
                import openai
                client = openai.OpenAI(api_key=api_key)
                
                yield self.log_step("analyze", f"Submitting queries to GPT model as {self.name}...")
                response = client.chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.2
                )
                output_text = response.choices[0].message.content
                yield self.log_step("synthesize", "Formatting structural report sections...")
                time.sleep(0.8)
                yield self.log_step("final", output_text)
                
            elif api_provider.lower() == "gemini":
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=system_prompt)
                
                yield self.log_step("analyze", f"Submitting queries to Gemini model as {self.name}...")
                response = model.generate_content(user_prompt)
                output_text = response.text
                yield self.log_step("synthesize", "Formatting structural report sections...")
                time.sleep(0.8)
                yield self.log_step("final", output_text)
                
            else:
                yield self.log_step("error", f"Unsupported API provider: {api_provider}")
                
        except Exception as e:
            yield self.log_step("error", f"Live execution failed: {str(e)}. Falling back to simulation.")
            # Yield simulation steps if live fails
            for step in self.run_simulated(symbol, company_info, financials, context):
                yield step

    def get_system_prompt(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> str:
        """Construct the system prompt for the live agent. Override in subclass."""
        return f"You are the {self.name}, acting as a financial expert."

    def get_user_prompt(self, symbol: str, company_info: Dict[str, Any], financials: Dict[str, Any], context: Dict[str, Any] = None) -> str:
        """Construct the user prompt for the live agent. Override in subclass."""
        return f"Analyze {symbol} with the provided financials: {json.dumps(financials)}"
