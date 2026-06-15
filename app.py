import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
import os

from utils.financial_data import get_stock_info, get_stock_history, get_stock_financials, is_indian_stock
from utils.report_generator import ResearchCoordinator

# Page Configuration
st.set_page_config(
    page_title="Apex Institutional Equities Platform",
    page_icon="https://cdn-icons-png.flaticon.com/512/3135/3135706.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Premium CSS Injector
def inject_custom_styles():
    st.markdown("""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
        
        <style>
        /* Global CSS Overrides */
        html, body, [class*="css"] {
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Dark Theme Accent Adjustments */
        .stApp {
            background-color: #0c0f16;
            color: #e2e8f0;
        }
        
        /* Glassmorphic Cards */
        .premium-card {
            background: rgba(21, 25, 35, 0.75);
            border: 1px solid rgba(45, 55, 72, 0.6);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 18px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
        }
        
        .metric-title {
            color: #94a3b8;
            font-size: 0.85rem;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.075em;
        }
        
        .metric-value {
            color: #f8fafc;
            font-size: 1.8rem;
            font-weight: 700;
            margin-top: 4px;
        }
        
        /* Glowing Badges for Ratings */
        .rating-badge {
            display: inline-block;
            padding: 8px 16px;
            border-radius: 8px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-size: 1.1rem;
            text-align: center;
            box-shadow: 0 0 15px rgba(0,0,0,0.2);
        }
        
        .rating-buy {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(5, 150, 105, 0.2) 100%);
            border: 1px solid #10b981;
            color: #34d399;
            box-shadow: 0 0 12px rgba(16, 185, 129, 0.1);
        }
        
        .rating-hold {
            background: linear-gradient(135deg, rgba(245, 158, 11, 0.15) 0%, rgba(217, 119, 6, 0.2) 100%);
            border: 1px solid #f59e0b;
            color: #fbbf24;
            box-shadow: 0 0 12px rgba(245, 158, 11, 0.1);
        }
        
        .rating-sell {
            background: linear-gradient(135deg, rgba(239, 68, 68, 0.15) 0%, rgba(220, 38, 38, 0.2) 100%);
            border: 1px solid #ef4444;
            color: #f87171;
            box-shadow: 0 0 12px rgba(239, 68, 68, 0.1);
        }
        
        /* Terminal Log styling */
        .agent-terminal {
            background: #06090e;
            border: 1px solid #1f2937;
            border-radius: 8px;
            padding: 16px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            max-height: 450px;
            overflow-y: auto;
            color: #38bdf8;
            box-shadow: inset 0 2px 8px rgba(0,0,0,0.8);
        }
        
        .terminal-line {
            margin-bottom: 6px;
            line-height: 1.4;
        }
        
        .terminal-time {
            color: #4b5563;
            margin-right: 8px;
        }
        
        .terminal-tag {
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 700;
            margin-right: 8px;
            text-transform: uppercase;
        }
        
        .tag-search { background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.4); }
        .tag-analyze { background: rgba(139, 92, 246, 0.15); color: #a78bfa; border: 1px solid rgba(139, 92, 246, 0.4); }
        .tag-synthesize { background: rgba(236, 72, 153, 0.15); color: #f472b6; border: 1px solid rgba(236, 72, 153, 0.4); }
        .tag-status { background: rgba(156, 163, 175, 0.15); color: #cbd5e1; border: 1px solid rgba(156, 163, 175, 0.4); }
        .tag-error { background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4); }
        
        /* Custom Header Styling */
        .gradient-text {
            background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #94a3b8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 800;
            font-size: 2.4rem;
            letter-spacing: -0.01em;
            margin-bottom: 0.2rem;
        }
        
        /* Agent Info Card */
        .agent-info-card {
            background: rgba(31, 41, 55, 0.25);
            border: 1px solid rgba(75, 85, 99, 0.25);
            border-radius: 8px;
            padding: 14px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
        }
        
        .analyst-badge {
            display: inline-block;
            background: rgba(30, 41, 59, 0.8);
            border: 1px solid #334155;
            color: #94a3b8;
            padding: 4px 8px;
            border-radius: 4px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            font-weight: 700;
            margin-right: 12px;
            min-width: 28px;
            text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

inject_custom_styles()

# Header Section
col_header, col_status = st.columns([5, 2])
with col_header:
    st.markdown('<div class="gradient-text">APEX PORTFOLIO RESEARCH</div>', unsafe_allow_html=True)
    st.markdown('<div style="color: #64748b; font-size: 0.95rem; font-weight: 500; margin-bottom: 2rem; letter-spacing: 0.05em; text-transform: uppercase;">Institutional Equity Intelligence Platform</div>', unsafe_allow_html=True)
with col_status:
    st.markdown("""
        <div style="text-align: right; margin-top: 14px;">
            <span style="background: rgba(14, 165, 233, 0.1); border: 1px solid rgba(14, 165, 233, 0.4); color: #38bdf8; padding: 4px 10px; border-radius: 6px; font-size: 0.72rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase;">SECURE LINK</span>
        </div>
    """, unsafe_allow_html=True)

# Session State Initializations
if "logs" not in st.session_state:
    st.session_state.logs = []
if "agent_reports" not in st.session_state:
    st.session_state.agent_reports = {}
if "final_report" not in st.session_state:
    st.session_state.final_report = None
if "company_info" not in st.session_state:
    st.session_state.company_info = None
if "financials" not in st.session_state:
    st.session_state.financials = None
if "research_active" not in st.session_state:
    st.session_state.research_active = False
if "current_ticker" not in st.session_state:
    st.session_state.current_ticker = ""

# Sidebar Control Room
with st.sidebar:
    st.markdown("### Analysis Parameters")
    
    # Preset Indian Tickers and Custom Input
    ticker_presets = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS"]
    selected_preset = st.selectbox("Select Target Enterprise", ticker_presets + ["Custom Ticker (NSE/BSE)"])
    
    if selected_preset == "Custom Ticker (NSE/BSE)":
        ticker_input = st.text_input("Enter NSE/BSE Symbol (e.g., SBIN.NS)", value="SBIN.NS").upper().strip()
    else:
        ticker_input = selected_preset
        
    st.markdown("---")
    st.markdown("### Execution Environment")
    api_provider = st.selectbox("Model Engine", ["Simulation Mode (Offline-Safe)", "OpenAI (GPT-4)", "Google (Gemini)"])
    
    api_key = ""
    if api_provider != "Simulation Mode (Offline-Safe)":
        provider_name = "OpenAI API Key" if "OpenAI" in api_provider else "Gemini API Key"
        api_key = st.text_input(f"Enter {provider_name}", type="password")
        
    st.markdown("---")
    
    # Run Research Button
    trigger_research = st.button("Execute Stock Analysis", use_container_width=True, type="primary", disabled=st.session_state.research_active)
    
    st.markdown("---")
    # Agent Team Summary
    st.markdown("### Equity Research Desk")
    st.markdown("""
        <div class="agent-info-card">
            <span class="analyst-badge">NE</span>
            <div>
                <strong style="font-size: 0.85rem; color: #f1f5f9;">News & Events Analyst</strong>
                <p style="font-size: 0.75rem; margin: 2px 0 0 0; color: #64748b; line-height: 1.3;">Scans corporate filings and event disclosures.</p>
            </div>
        </div>
        <div class="agent-info-card">
            <span class="analyst-badge">FA</span>
            <div>
                <strong style="font-size: 0.85rem; color: #f1f5f9;">Financial & Accounting Analyst</strong>
                <p style="font-size: 0.75rem; margin: 2px 0 0 0; color: #64748b; line-height: 1.3;">Models quarterly metrics and operating guidance.</p>
            </div>
        </div>
        <div class="agent-info-card">
            <span class="analyst-badge">QS</span>
            <div>
                <strong style="font-size: 0.85rem; color: #f1f5f9;">Quantitative Sentiment Analyst</strong>
                <p style="font-size: 0.75rem; margin: 2px 0 0 0; color: #64748b; line-height: 1.3;">Measures options flow and broker price targets.</p>
            </div>
        </div>
        <div class="agent-info-card">
            <span class="analyst-badge">LS</span>
            <div>
                <strong style="font-size: 0.85rem; color: #f1f5f9;">Lead Equity Strategist</strong>
                <p style="font-size: 0.75rem; margin: 2px 0 0 0; color: #64748b; line-height: 1.3;">Compiles valuation thresholds and portfolio targets.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ----------------- Currency Format Helpers -----------------
def format_currency_value(val: float, is_indian: bool) -> str:
    """Format large numbers beautifully in INR (Crores / Lakh Crores) or USD."""
    if is_indian:
        if val >= 1e12:
            return f"₹{val / 1e12:.2f} Lakh Cr"
        elif val >= 1e7:
            return f"₹{val / 1e7:,.1f} Cr"
        else:
            return f"₹{val:,.2f}"
    else:
        if val >= 1e12:
            return f"${val / 1e12:.2f}T"
        elif val >= 1e9:
            return f"${val / 1e9:,.1f}B"
        else:
            return f"${val:,.2f}"

# ----------------- Execution Engine -----------------
if trigger_research and ticker_input:
    # Clear previous run data
    st.session_state.logs = []
    st.session_state.agent_reports = {}
    st.session_state.final_report = None
    st.session_state.company_info = None
    st.session_state.financials = None
    st.session_state.research_active = True
    st.session_state.current_ticker = ticker_input
    
    # Setup coordinator
    prov_key = api_key if api_provider != "Simulation Mode (Offline-Safe)" else None
    prov_type = "openai" if "OpenAI" in api_provider else ("gemini" if "Google" in api_provider else None)
    
    coordinator = ResearchCoordinator(api_key=prov_key, api_provider=prov_type)
    
    # UI Elements for live progress
    st.markdown("### Execution Pipeline Status")
    progress_bar = st.progress(0)
    status_msg = st.empty()
    
    # Columns: live status and terminal
    status_col, terminal_col = st.columns([1, 2])
    
    with status_col:
        st.write("**Active Process Queue:**")
        news_status = st.empty()
        earnings_status = st.empty()
        sentiment_status = st.empty()
        analysis_status = st.empty()
        
        news_status.markdown("`[Pending]` News & Events Analyst: `Idle`")
        earnings_status.markdown("`[Pending]` Financial & Accounting Analyst: `Idle`")
        sentiment_status.markdown("`[Pending]` Quantitative Sentiment Analyst: `Idle`")
        analysis_status.markdown("`[Pending]` Lead Equity Strategist: `Idle`")
        
    with terminal_col:
        st.write("**Internal Processing Log:**")
        terminal_container = st.empty()
        
    # Streaming iteration
    for update in coordinator.run_research(ticker_input):
        progress_bar.progress(update["progress"])
        status_msg.markdown(f"**Process:** {update['message']}")
        
        # Capture raw metadata
        if "data" in update:
            st.session_state.company_info = update["data"]["info"]
            st.session_state.financials = update["data"]["financials"]
            
        # Handle intermediate log items
        if update.get("type") == "log":
            st.session_state.logs.append(update["log"])
            
            # Highlight current active agent in status indicators
            active_agent = update["agent_name"]
            if active_agent == "News & Events Analyst":
                news_status.markdown("`[Running]` News & Events Analyst: `Analysing...`")
            elif active_agent == "Financial & Accounting Analyst":
                news_status.markdown("`[Complete]` News & Events Analyst: `Complete`")
                earnings_status.markdown("`[Running]` Financial & Accounting Analyst: `Analysing...`")
            elif active_agent == "Quantitative Sentiment Analyst":
                earnings_status.markdown("`[Complete]` Financial & Accounting Analyst: `Complete`")
                sentiment_status.markdown("`[Running]` Quantitative Sentiment Analyst: `Analysing...`")
            elif active_agent == "Lead Equity Strategist":
                sentiment_status.markdown("`[Complete]` Quantitative Sentiment Analyst: `Complete`")
                analysis_status.markdown("`[Running]` Lead Equity Strategist: `Synthesising...`")
                
            # Render terminal content
            terminal_html = '<div class="agent-terminal">'
            for log in st.session_state.logs:
                tag_cls = f"tag-{log['type']}"
                terminal_html += (
                    f'<div class="terminal-line">'
                    f'<span class="terminal-time">[{log["timestamp"]}]</span>'
                    f'<span class="terminal-tag {tag_cls}">{log["type"]}</span>'
                    f'<strong style="color:#e2e8f0;">{log["agent"]}</strong>: {log["message"]}'
                    f'</div>'
                )
            terminal_html += '</div>'
            terminal_container.markdown(terminal_html, unsafe_allow_html=True)
            
        elif update.get("type") == "final":
            # Save completed agent document
            st.session_state.agent_reports[update["agent_name"]] = update["content"]
            
            agent_name = update["agent_name"]
            if agent_name == "News & Events Analyst":
                news_status.markdown("`[Complete]` News & Events Analyst: `Finished`")
            elif agent_name == "Financial & Accounting Analyst":
                earnings_status.markdown("`[Complete]` Financial & Accounting Analyst: `Finished`")
            elif agent_name == "Quantitative Sentiment Analyst":
                sentiment_status.markdown("`[Complete]` Quantitative Sentiment Analyst: `Finished`")
            elif agent_name == "Lead Equity Strategist":
                analysis_status.markdown("`[Complete]` Lead Equity Strategist: `Finished`")
                
        # Finalization
        if update["stage"] == "completed":
            st.session_state.final_report = update["final_report"]
            st.session_state.research_active = False
            st.toast("Pipeline compilation completed successfully.", icon=None)
            time.sleep(1.0)
            st.rerun()

# ----------------- Dashboard Layout -----------------
# Ensure we have data loaded (using fallback data initially if no research has run)
if not st.session_state.company_info and ticker_input:
    # Warm up base data silently to populate the UI on load
    st.session_state.current_ticker = ticker_input
    st.session_state.company_info = get_stock_info(ticker_input)
    st.session_state.financials = get_stock_financials(ticker_input)

# Display Dashboard tabs if data exists
if st.session_state.company_info:
    info = st.session_state.company_info
    financials = st.session_state.financials
    ticker_sym = st.session_state.current_ticker
    is_ind = is_indian_stock(ticker_sym)
    curr_sym = "₹" if is_ind else "$"
    
    # 1. Company Profiler Banner
    st.markdown(f"""
        <div class="premium-card">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <h1 style="margin: 0; font-size: 2rem; color: #f8fafc;">{info.get('longName')} ({ticker_sym})</h1>
                    <span style="color: #94a3b8; font-size: 0.95rem;">{info.get('sector')} • {info.get('industry')} • <a href="{info.get('website')}" target="_blank" style="color: #60a5fa; text-decoration: none;">{info.get('website')}</a></span>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 2.2rem; font-weight: 800; color: #3b82f6;">{curr_sym}{info.get('currentPrice'):,.2f}</div>
                    <span style="color: #94a3b8; font-size: 0.85rem;">Market Price ({'INR' if is_ind else 'USD'})</span>
                </div>
            </div>
            <p style="margin: 16px 0 0 0; font-size: 0.92rem; line-height: 1.6; color: #cbd5e1;">{info.get('longBusinessSummary')}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Main Tabs
    tab_dashboard, tab_workspace, tab_report = st.tabs([
        "Market Performance Monitor", 
        "Analyst Working Papers", 
        "Investment Recommendation Memo"
    ])
    
    # ---- TAB 1: Market Dashboard ----
    with tab_dashboard:
        # Mini Metrics Row
        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        
        pe_val = f"{info.get('trailingPE'):.1f}x" if info.get('trailingPE') else "N/A"
        div_val = f"{info.get('dividendYield') * 100:.2f}%" if info.get('dividendYield') else "0.00%"
        mcap_formatted = format_currency_value(info.get('marketCap', 0), is_ind)
        
        render_metric_card = lambda col, title, value: col.markdown(f"""
            <div class="premium-card" style="padding: 16px 20px; text-align: center; margin-bottom: 0;">
                <div class="metric-title">{title}</div>
                <div class="metric-value">{value}</div>
            </div>
        """, unsafe_allow_html=True)
        
        render_metric_card(m_col1, "Market Capitalization", mcap_formatted)
        render_metric_card(m_col2, "Trailing P/E Ratio", pe_val)
        render_metric_card(m_col3, "Dividend Yield", div_val)
        render_metric_card(m_col4, f"52-Week Spread ({curr_sym})", f"{curr_sym}{info.get('fiftyTwoWeekLow'):,.2f} - {curr_sym}{info.get('fiftyTwoWeekHigh'):,.2f}")
        
        st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
        
        # Chart and Balance Sheet Columns
        chart_col, fin_col = st.columns([2, 1])
        
        with chart_col:
            st.markdown("### Stock Price History")
            history = get_stock_history(ticker_sym)
            if not history.empty:
                # Plotly Stock Line Chart
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=history.index, 
                    y=history['Close'],
                    mode='lines',
                    name='Price',
                    line=dict(width=2.5, color='#3b82f6'),
                    fill='tozeroy',
                    fillcolor='rgba(59, 130, 246, 0.05)'
                ))
                
                fig.update_layout(
                    template="plotly_dark",
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    margin=dict(l=20, r=20, t=10, b=20),
                    height=380,
                    xaxis=dict(showgrid=False, color='#64748b'),
                    yaxis=dict(showgrid=True, gridcolor='rgba(148, 163, 184, 0.1)', color='#64748b', side='right'),
                    hovermode="x unified"
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Price history not currently available for this symbol.")
                
        with fin_col:
            unit_label = "₹ Crores" if is_ind else "$ Billions"
            st.markdown(f"### Key Financial Trends ({unit_label})")
            
            # Render financials table
            fin_df = pd.DataFrame({
                "Year": financials["years"],
                f"Revenue ({unit_label})": financials["revenue"],
                f"Net Profit ({unit_label})": financials["net_income"],
                "Op Margin (%)": financials["operating_margin"]
            }).set_index("Year")
            
            st.table(fin_df)
            
            # Simple Chart of revenue & net income
            fig_fin = go.Figure()
            fig_fin.add_trace(go.Bar(
                x=financials["years"],
                y=financials["revenue"],
                name=f"Revenue ({unit_label.split()[-1]})",
                marker_color='#3b82f6'
            ))
            fig_fin.add_trace(go.Bar(
                x=financials["years"],
                y=financials["net_income"],
                name=f"Net Profit ({unit_label.split()[-1]})",
                marker_color='#10b981'
            ))
            fig_fin.update_layout(
                template="plotly_dark",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                margin=dict(l=20, r=20, t=10, b=10),
                height=180,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False)
            )
            st.plotly_chart(fig_fin, use_container_width=True)
            
    # ---- TAB 2: Analyst Working Papers (Logs & Collaboration) ----
    with tab_workspace:
        st.markdown("### Analyst Working Papers & Memos")
        st.markdown("Review the independent findings and process logs compiled by each research analyst.")
        
        # Display Agent Reports Side-by-Side if available
        if st.session_state.agent_reports:
            agent_tabs = st.tabs(list(st.session_state.agent_reports.keys()))
            for a_tab, a_name in zip(agent_tabs, st.session_state.agent_reports.keys()):
                with a_tab:
                    st.markdown(st.session_state.agent_reports[a_name])
        else:
            st.info("No research has been executed yet. Click 'Analyze Stock' in the sidebar to run the agent pipeline.")
            
        # Display full running log terminal if it exists
        if st.session_state.logs:
            st.markdown("#### Real-time System Trace Console")
            terminal_html = '<div class="agent-terminal" style="max-height: 300px;">'
            for log in st.session_state.logs:
                tag_cls = f"tag-{log['type']}"
                terminal_html += (
                    f'<div class="terminal-line">'
                    f'<span class="terminal-time">[{log["timestamp"]}]</span>'
                    f'<span class="terminal-tag {tag_cls}">{log["type"]}</span>'
                    f'<strong style="color:#e2e8f0;">{log["agent"]}</strong>: {log["message"]}'
                    f'</div>'
                )
            terminal_html += '</div>'
            st.markdown(terminal_html, unsafe_allow_html=True)

    # ---- TAB 3: Investment Memo Report ----
    with tab_report:
        if st.session_state.final_report:
            # Parse recommendation and targets for nice cards
            report_txt = st.session_state.final_report
            
            # Safe parsing values
            rec_rating = "HOLD"
            tgt_val = "N/A"
            stop_val = "N/A"
            
            if "BUY" in report_txt[:500].upper():
                rec_rating = "BUY"
            elif "SELL" in report_txt[:500].upper():
                rec_rating = "SELL"
                
            try:
                import re
                def extract_numeric(text_segment):
                    cleaned = text_segment.replace(",", "")
                    match = re.search(r'[-+]?\d*\.\d+|\d+', cleaned)
                    return match.group() if match else "N/A"

                if "TARGET PRICE:" in report_txt.upper():
                    tgt_segment = report_txt.upper().split("TARGET PRICE:")[1].split("|")[0].strip()
                    tgt_val = extract_numeric(tgt_segment)
                if "STOP-LOSS:" in report_txt.upper():
                    stop_segment = report_txt.upper().split("STOP-LOSS:")[1].split("\n")[0].strip()
                    stop_val = extract_numeric(stop_segment)
            except:
                pass
                
            # Nice Executive Badges Row
            rep_col1, rep_col2, rep_col3, rep_col4 = st.columns([1.5, 1, 1, 2])
            
            with rep_col1:
                rating_cls = "rating-buy" if rec_rating == "BUY" else ("rating-hold" if rec_rating == "HOLD" else "rating-sell")
                st.markdown("<div style='color:#94a3b8; font-size:0.85rem; font-weight:500; margin-bottom:6px;'>INVESTMENT RATING</div>", unsafe_allow_html=True)
                st.markdown(f'<div class="rating-badge {rating_cls}">{rec_rating}</div>', unsafe_allow_html=True)
                
            with rep_col2:
                st.markdown("<div style='color:#94a3b8; font-size:0.85rem; font-weight:500; margin-bottom:6px;'>TARGET PRICE</div>", unsafe_allow_html=True)
                st.markdown(f'<div style="font-size: 1.8rem; font-weight: 700; color:#3b82f6;">{f"{curr_sym}{float(tgt_val):,.2f}" if tgt_val != "N/A" else "N/A"}</div>', unsafe_allow_html=True)
                
            with rep_col3:
                st.markdown("<div style='color:#94a3b8; font-size:0.85rem; font-weight:500; margin-bottom:6px;'>STOP-LOSS</div>", unsafe_allow_html=True)
                st.markdown(f'<div style="font-size: 1.8rem; font-weight: 700; color:#ef4444;">{f"{curr_sym}{float(stop_val):,.2f}" if stop_val != "N/A" else "N/A"}</div>', unsafe_allow_html=True)
                
            with rep_col4:
                # Extract Sentiment Score for Gauge (typically from Sentiment Agent output)
                sent_score = 0
                sent_report = st.session_state.agent_reports.get("Market Sentiment Agent", "")
                if sent_report:
                    try:
                        import re
                        raw_matches = re.findall(r'(-?\+?\d+)\s*/\s*100', sent_report)
                        if raw_matches:
                            sent_score = int(raw_matches[0])
                    except:
                        sent_score = 30 # default
                
                # Sentiment Gauge Chart
                fig_gauge = go.Figure(go.Indicator(
                    mode = "gauge+number",
                    value = sent_score,
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    title = {'text': "Quantitative Sentiment Index", 'font': {'size': 13, 'color': '#94a3b8'}},
                    number = {'font': {'color': '#f8fafc', 'size': 20}, 'suffix': '/100'},
                    gauge = {
                        'axis': {'range': [-100, 100], 'tickwidth': 1, 'tickcolor': "#64748b"},
                        'bar': {'color': "#60a5fa"},
                        'bgcolor': "rgba(31, 41, 55, 0.4)",
                        'borderwidth': 1,
                        'bordercolor': "rgba(75, 85, 99, 0.4)",
                        'steps': [
                            {'range': [-100, -30], 'color': 'rgba(239, 68, 68, 0.15)'},
                            {'range': [-30, 30], 'color': 'rgba(245, 158, 11, 0.1)'},
                            {'range': 30, 'color': 'rgba(16, 185, 129, 0.15)'}
                        ],
                    }
                ))
                fig_gauge.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    margin=dict(l=10, r=10, t=10, b=10),
                    height=100
                )
                st.plotly_chart(fig_gauge, use_container_width=True)
                
            st.markdown("<hr style='border-color: rgba(75, 85, 99, 0.3); margin-top:20px; margin-bottom:20px;'/>", unsafe_allow_html=True)
            
            # Print Final Report
            st.markdown(report_txt)
            
            st.markdown("---")
            # Copy/Download Section
            st.download_button(
                label="Download Research Memorandum (Markdown)",
                data=report_txt,
                file_name=f"{ticker_sym}_equity_research_report.md",
                mime="text/markdown",
                use_container_width=True
            )
        else:
            st.info("No recommendation memorandum has been compiled for this asset. Execute analysis to generate research.")
else:
    st.info("Ingesting database profiles. Trigger equity analysis to generate memorandum.")
