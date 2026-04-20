import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# ===================== GLOBAL PAGE CONFIG (1:1 UI BASE SETUP) =====================
st.set_page_config(
    page_title="Financial Analytics Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global Color Palette (EXACT copy from your NoCode interface)
PRIMARY_BLUE = "#165DFF"
POSITIVE_GREEN = "#10b981"
NEGATIVE_RED = "#ef4444"
CARD_LIGHT_BG = "#f8fafc"
PAGE_LIGHT_BG = "#ffffff"
SIDEBAR_UNACTIVE = "#64748b"

# ===================== SESSION STATE INIT (TAB SWITCH INTERACTION LOGIC) =====================
# Persistent tab switching, exactly same as NoCode sidebar click logic
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Financial Metrics"

# Sidebar tab list (100% same as your interface)
TAB_LIST = [
    "Financial Metrics",
    "Stock Trends",
    "Portfolio Analysis",
    "Risk Assessment"
]

# ===================== FULL COMPANY DATABASE (5 listed home appliance enterprises) =====================
# Complete metric & trend data for EVERY company, fully matched with your NoCode data system
COMPANY_DATABASE = {
    "Gree Electric": {
        "stock_code": "000651",
        "industry": "Home Appliances",
        "market_cap": "200B",
        # Core Financial Metrics
        "revenue_growth": 12.8,
        "revenue_growth_change": 1.5,
        "net_profit_margin": 8.5,
        "net_profit_margin_change": 0.8,
        "gross_margin": 28.3,
        "gross_margin_change": -0.5,
        "roe": 15.2,
        "roe_change": 1.2,
        # Risk Metrics
        "var_95": 45000,
        "var_change": -5000,
        "volatility": 18.5,
        "volatility_change": 2.1,
        "beta_coeff": 1.12,
        "beta_change": 0.05,
        "downside_risk": 12.3,
        "downside_risk_change": -1.2,
        # Portfolio Metrics
        "portfolio_value": 1250000,
        "portfolio_value_change": 5.2,
        "annualized_return": 12.8,
        "annualized_return_change": 1.5,
        "max_drawdown": -8.3,
        "max_drawdown_change": -2.1,
        "sharpe_ratio": 1.45,
        "sharpe_ratio_change": 0.2,
        # Time-series trend data
        "month_labels": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        "revenue_trend": [10.2, 11.5, 13.8, 11.9, 14.7, 12.3, 13.1, 12.7, 13.5, 14.2, 12.9, 13.4],
        "profit_trend": [7.2, 7.8, 9.1, 8.3, 9.5, 8.7, 9.9, 8.5, 9.2, 10.1, 8.8, 9.4],
        "var_year_trend": [38000, 40000, 42000, 44000, 51000, 41000, 45000],
        "portfolio_trend_base": 1050000
    },
    "Midea Group": {
        "stock_code": "000333",
        "industry": "Home Appliances",
        "market_cap": "400B",
        "revenue_growth": 15.6,
        "revenue_growth_change": 2.3,
        "net_profit_margin": 10.2,
        "net_profit_margin_change": 1.1,
        "gross_margin": 32.5,
        "gross_margin_change": 0.7,
        "roe": 18.9,
        "roe_change": 1.8,
        "var_95": 62000,
        "var_change": -3200,
        "volatility": 15.2,
        "volatility_change": 1.4,
        "beta_coeff": 0.98,
        "beta_change": -0.03,
        "downside_risk": 9.7,
        "downside_risk_change": -0.9,
        "portfolio_value": 1890000,
        "portfolio_value_change": 7.4,
        "annualized_return": 15.9,
        "annualized_return_change": 2.2,
        "max_drawdown": -6.5,
        "max_drawdown_change": -1.3,
        "sharpe_ratio": 1.72,
        "sharpe_ratio_change": 0.28,
        "month_labels": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        "revenue_trend": [12.4, 13.9, 15.8, 14.2, 16.5, 15.1, 14.8, 15.5, 16.2, 17.1, 15.7, 16.4],
        "profit_trend": [8.5, 9.2, 10.7, 9.8, 11.2, 10.5, 9.9, 10.8, 11.5, 12.1, 10.3, 11.0],
        "var_year_trend": [51000, 54000, 57000, 59000, 64000, 55000, 60000],
        "portfolio_trend_base": 1580000
    },
    "Haier Smart Home": {
        "stock_code": "600690",
        "industry": "Home Appliances",
        "market_cap": "250B",
        "revenue_growth": 9.7,
        "revenue_growth_change": 0.9,
        "net_profit_margin": 7.4,
        "net_profit_margin_change": 0.5,
        "gross_margin": 26.8,
        "gross_margin_change": -0.3,
        "roe": 13.1,
        "roe_change": 0.8,
        "var_95": 38500,
        "var_change": -4100,
        "volatility": 16.9,
        "volatility_change": 1.7,
        "beta_coeff": 1.05,
        "beta_change": 0.02,
        "downside_risk": 10.8,
        "downside_risk_change": -0.7,
        "portfolio_value": 1420000,
        "portfolio_value_change": 4.1,
        "annualized_return": 10.6,
        "annualized_return_change": 0.9,
        "max_drawdown": -7.4,
        "max_drawdown_change": -1.6,
        "sharpe_ratio": 1.29,
        "sharpe_ratio_change": 0.15,
        "month_labels": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        "revenue_trend": [8.1, 9.0, 10.5, 9.4, 11.2, 10.1, 9.8, 10.3, 10.9, 11.7, 9.9, 10.6],
        "profit_trend": [6.3, 6.9, 7.8, 7.1, 8.2, 7.5, 7.2, 7.9, 8.4, 9.0, 7.6, 8.1],
        "var_year_trend": [32000, 34000, 36000, 39000, 43000, 35000, 39000],
        "portfolio_trend_base": 1190000
    },
    "Supor": {
        "stock_code": "002032",
        "industry": "Home Appliances",
        "market_cap": "180B",
        "revenue_growth": 7.3,
        "revenue_growth_change": 0.6,
        "net_profit_margin": 9.1,
        "net_profit_margin_change": 0.4,
        "gross_margin": 34.2,
        "gross_margin_change": 1.1,
        "roe": 12.4,
        "roe_change": 0.7,
        "var_95": 29800,
        "var_change": -2700,
        "volatility": 17.8,
        "volatility_change": 1.9,
        "beta_coeff": 1.09,
        "beta_change": 0.04,
        "downside_risk": 11.5,
        "downside_risk_change": -0.5,
        "portfolio_value": 980000,
        "portfolio_value_change": 3.5,
        "annualized_return": 9.4,
        "annualized_return_change": 0.7,
        "max_drawdown": -7.9,
        "max_drawdown_change": -1.8,
        "sharpe_ratio": 1.18,
        "sharpe_ratio_change": 0.11,
        "month_labels": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        "revenue_trend": [6.1, 6.8, 7.9, 7.0, 8.3, 7.5, 7.2, 7.7, 8.1, 8.8, 7.4, 7.9],
        "profit_trend": [7.8, 8.3, 9.4, 8.6, 9.9, 9.2, 8.8, 9.3, 9.8, 10.5, 8.9, 9.5],
        "var_year_trend": [25000, 27000, 28500, 30500, 33000, 26500, 29800],
        "portfolio_trend_base": 820000
    },
    "Joyoung": {
        "stock_code": "002242",
        "industry": "Home Appliances",
        "market_cap": "120B",
        "revenue_growth": 5.8,
        "revenue_growth_change": 0.4,
        "net_profit_margin": 8.7,
        "net_profit_margin_change": 0.3,
        "gross_margin": 31.6,
        "gross_margin_change": 0.5,
        "roe": 10.9,
        "roe_change": 0.6,
        "var_95": 21500,
        "var_change": -1900,
        "volatility": 19.1,
        "volatility_change": 2.4,
        "beta_coeff": 1.15,
        "beta_change": 0.06,
        "downside_risk": 13.2,
        "downside_risk_change": -0.4,
        "portfolio_value": 740000,
        "portfolio_value_change": 2.9,
        "annualized_return": 8.2,
        "annualized_return_change": 0.5,
        "max_drawdown": -8.7,
        "max_drawdown_change": -2.3,
        "sharpe_ratio": 1.05,
        "sharpe_ratio_change": 0.09,
        "month_labels": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        "revenue_trend": [4.9, 5.5, 6.3, 5.7, 6.8, 6.1, 5.9, 6.4, 6.7, 7.3, 6.0, 6.5],
        "profit_trend": [7.4, 7.9, 8.9, 8.2, 9.3, 8.6, 8.3, 8.8, 9.2, 9.8, 8.5, 9.0],
        "var_year_trend": [18000, 19500, 20500, 22000, 24000, 19000, 21500],
        "portfolio_trend_base": 610000
    }
}

# Correlation Matrix base data (exact NoCode matrix layout)
CORRELATION_BASE = np.array([
    [1.00, 0.75, 0.68, 0.45, 0.32],
    [0.75, 1.00, 0.82, 0.51, 0.38],
    [0.68, 0.82, 1.00, 0.47, 0.41],
    [0.45, 0.51, 0.47, 1.00, 0.65],
    [0.32, 0.38, 0.41, 0.65, 1.00]
])
CORR_COMPANY_LIST = list(COMPANY_DATABASE.keys())

# ===================== SIDEBAR CONTROL PANEL (1: FULL PERFECT REPLICA) =====================
with st.sidebar:
    # Sidebar Header
    st.markdown("""
    <div style="display:flex;align-items:center;gap:8px;margin-bottom:24px;">
        <div style="width:28px;height:28px;border-radius:6px;background:#165DFF;display:flex;align-items:center;justify-content:center;color:white;font-weight:bold;">
            ⚙
        </div>
        <span style="font-size:20px;font-weight:700;color:#0f172a;">Control Panel</span>
    </div>
    """, unsafe_allow_html=True)

    # 1. Company Selection Dropdown (full info label as original NoCode)
    st.subheader("Select Companies")
    company_options = list(COMPANY_DATABASE.keys())
    selected_company = st.selectbox(
        label="1 Company Selected",
        options=company_options,
        index=0
    )
    # Load full data of chosen company
    data = COMPANY_DATABASE[selected_company]

    # Show company basic info (stock code / industry / market cap)
    st.caption(f"{data['stock_code']} · {data['industry']} · {data['market_cap']}")
    st.divider()

    # 2. Date Range Picker (exact original date range UI)
    st.subheader("Date Range")
    from datetime import datetime
    start_default = datetime(2025, 4, 20)
    end_default = datetime(2026, 4, 20)
    date_start, date_end = st.date_input(
        label="Date Range",
        value=[start_default, end_default]
    )
    st.divider()

    # 3. Analysis Dimension Tab Buttons (click to switch, persistent highlight)
    st.subheader("Analysis Dimension")
    for tab in TAB_LIST:
        if tab == st.session_state.active_tab:
            # Active tab: primary blue highlight exactly as NoCode
            st.button(
                label=tab,
                type="primary",
                use_container_width=True,
                on_click=lambda t=tab: setattr(st.session_state, "active_tab", t)
            )
        else:
            # Unactive tab: grey default style
            st.button(
                label=tab,
                use_container_width=True,
                on_click=lambda t=tab: setattr(st.session_state, "active_tab", t)
            )

# ===================== MAIN PAGE GLOBAL HEADER (TOP PAGE TITLE) =====================
st.markdown("""
<div style="margin-bottom:32px;">
    <h1 style="font-size:32px;font-weight:700;margin:0;color:#0f172a;">Financial Analytics Platform</h1>
    <p style="font-size:16px;color:#64748b;margin:4px 0 0 0;">AI-Powered Investment Decision System</p>
</div>
""", unsafe_allow_html=True)

# Dynamic page subtitle (updates with selected company)
st.subheader(f"Analyzing {selected_company}")
col_top_right, _ = st.columns([1, 5])
with col_top_right:
    # Global Export CSV Button on every page, same position as original interface
    st.download_button(
        label="📥 Export CSV",
        data=pd.DataFrame({
            "Company": [selected_company],
            "Stock_Code": [data["stock_code"]],
            "Start_Date": [str(date_start)],
            "End_Date": [str(date_end)]
        }).to_csv(index=False).encode("utf-8"),
        file_name=f"{selected_company}_full_financial_data.csv",
        mime="text/csv"
    )

# ===================== TAB 1: FINANCIAL METRICS (FULL 1:1 REPLICA) =====================
if st.session_state.active_tab == "Financial Metrics":
    st.markdown("## Core Financial Metrics")
    # 4 Metric Cards Grid (exact layout, value, change number, green/red color rule)
    c1, c2, c3, c4 = st.columns(4)

    # Card 1: Revenue Growth
    with c1:
        change_color = POSITIVE_GREEN if data["revenue_growth_change"] >= 0 else NEGATIVE_RED
        st.metric(
            label="Revenue Growth",
            value=f"{data['revenue_growth']} %",
            delta=f"{data['revenue_growth_change']:+.1f}%"
        )
        st.markdown(f"<style>[data-testid='stMetricDelta']{{color:{change_color};}}</style>", unsafe_allow_html=True)

    # Card 2: Net Profit Margin
    with c2:
        change_color = POSITIVE_GREEN if data["net_profit_margin_change"] >= 0 else NEGATIVE_RED
        st.metric(
            label="Net Profit Margin",
            value=f"{data['net_profit_margin']} %",
            delta=f"{data['net_profit_margin_change']:+.1f}%"
        )
        st.markdown(f"<style>[data-testid='stMetricDelta']{{color:{change_color};}}</style>", unsafe_allow_html=True)

    # Card 3: Gross Margin
    with c3:
        change_color = POSITIVE_GREEN if data["gross_margin_change"] >= 0 else NEGATIVE_RED
        st.metric(
            label="Gross Margin",
            value=f"{data['gross_margin']} %",
            delta=f"{data['gross_margin_change']:+.1f}%"
        )
        st.markdown(f"<style>[data-testid='stMetricDelta']{{color:{change_color};}}</style>", unsafe_allow_html=True)

    # Card 4: ROE
    with c4:
        change_color = POSITIVE_GREEN if data["roe_change"] >= 0 else NEGATIVE_RED
        st.metric(
            label="ROE",
            value=f"{data['roe']} %",
            delta=f"{data['roe_change']:+.1f}%"
        )
        st.markdown(f"<style>[data-testid='stMetricDelta']{{color:{change_color};}}</style>", unsafe_allow_html=True)

    st.divider()

    # Bottom Dual Bar Charts (exact original NoCode chart style)
    chart_col1, chart_col2 = st.columns(2)
    x = np.arange(len(data["month_labels"]))

    # Chart 1: Revenue Growth Trend Bar Chart
    with chart_col1:
        st.markdown("### Revenue Growth Trend")
        fig1, ax1 = plt.subplots(figsize=(10, 4.5))
        ax1.bar(x, data["revenue_trend"], color=PRIMARY_BLUE, alpha=0.85)
        ax1.set_ylabel("Percentage (%)")
        ax1.set_xticks(x)
        ax1.set_xticklabels(data["month_labels"])
        ax1.grid(alpha=0.2, linestyle="--")
        ax1.set_ylim(4, 17)
        plt.tight_layout()
        st.pyplot(fig1)

    # Chart 2: Net Profit Margin Trend Bar Chart
    with chart_col2:
        st.markdown("### Net Profit Margin Trend")
        fig2, ax2 = plt.subplots(figsize=(10, 4.5))
        ax2.bar(x, data["profit_trend"], color=PRIMARY_BLUE, alpha=0.85)
        ax2.set_ylabel("Percentage (%)")
        ax2.set_xticks(x)
        ax2.set_xticklabels(data["month_labels"])
        ax2.grid(alpha=0.2, linestyle="--")
        ax2.set_ylim(3, 13)
        plt.tight_layout()
        st.pyplot(fig2)

# ===================== TAB 2: STOCK TRENDS (COMPLETED FULL TREND MODULE) =====================
elif st.session_state.active_tab == "Stock Trends":
    st.markdown("## Stock Price Trend Analysis")
    # Simulate stock price time series data with date linkage
    trend_month = pd.date_range(start=date_start, end=date_end, freq="M")
    base_price_dict = {
        "Gree Electric": 30, "Midea Group": 60, "Haier Smart Home": 22,
        "Supor": 26, "Joyoung": 18
    }
    base = base_price_dict[selected_company]
    price_series = base + np.linspace(0, 16, len(trend_month)) + np.random.randn(len(trend_month))*1.8

    # Stock price filled line chart (1:1 original portfolio chart style)
    fig_stock, ax_stock = plt.subplots(figsize=(12, 5))
    ax_stock.plot(trend_month, price_series, color=PRIMARY_BLUE, linewidth=2.2)
    ax_stock.fill_between(trend_month, price_series, alpha=0.12, color=PRIMARY_BLUE)
    ax_stock.set_title(f"{selected_company} Monthly Stock Price Trend (CNY)")
    ax_stock.grid(alpha=0.2, linestyle="--")
    plt.tight_layout()
    st.pyplot(fig_stock)

# ===================== TAB 3: PORTFOLIO ANALYSIS (FULL PERFECT REPLICA) =====================
elif st.session_state.active_tab == "Portfolio Analysis":
    st.markdown("## Portfolio Analysis")
    # 4 Portfolio Metric Cards
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        change_color = POSITIVE_GREEN if data["portfolio_value_change"] >= 0 else NEGATIVE_RED
        st.metric(
            label="Portfolio Value",
            value=f"¥{data['portfolio_value']:,}",
            delta=f"{data['portfolio_value_change']:+.1f}%"
        )
        st.markdown(f"<style>[data-testid='stMetricDelta']{{color:{change_color};}}</style>", unsafe_allow_html=True)

    with c2:
        change_color = POSITIVE_GREEN if data["annualized_return_change"] >= 0 else NEGATIVE_RED
        st.metric(
            label="Annualized Return",
            value=f"{data['annualized_return']} %",
            delta=f"{data['annualized_return_change']:+.1f}%"
        )
        st.markdown(f"<style>[data-testid='stMetricDelta']{{color:{change_color};}}</style>", unsafe_allow_html=True)

    with c3:
        change_color = POSITIVE_GREEN if data["max_drawdown_change"] >= 0 else NEGATIVE_RED
        st.metric(
            label="Max Drawdown",
            value=f"{data['max_drawdown']} %",
            delta=f"{data['max_drawdown_change']:+.1f}%"
        )
        st.markdown(f"<style>[data-testid='stMetricDelta']{{color:{change_color};}}</style>", unsafe_allow_html=True)

    with c4:
        change_color = POSITIVE_GREEN if data["sharpe_ratio_change"] >= 0 else NEGATIVE_RED
        st.metric(
            label="Sharpe Ratio",
            value=f"{data['sharpe_ratio']}",
            delta=f"{data['sharpe_ratio_change']:+.2f}"
        )
        st.markdown(f"<style>[data-testid='stMetricDelta']{{color:{change_color};}}</style>", unsafe_allow_html=True)

    st.divider()
    chart_col1, chart_col2 = st.columns(2)

    # Chart 1: Portfolio Value Filled Line Trend
    with chart_col1:
        st.markdown("### Portfolio Value Trend")
        port_x = pd.date_range(start=date_start, end=date_end, freq="M")
        port_base = data["portfolio_trend_base"]
        port_value = port_base + np.linspace(0, 200000, len(port_x)) + np.random.randn(len(port_x))*8000
        fig_port, ax_port = plt.subplots(figsize=(10, 4.5))
        ax_port.plot(port_x, port_value, color=PRIMARY_BLUE, linewidth=2)
        ax_port.fill_between(port_x, port_value, alpha=0.12, color=PRIMARY_BLUE)
        ax_port.grid(alpha=0.2, linestyle="--")
        plt.tight_layout()
        st.pyplot(fig_port)

    # Chart 2: Stock Correlation Matrix Heatmap (exact original matrix)
    with chart_col2:
        st.markdown("### Stock Correlation Matrix")
        fig_corr, ax_corr = plt.subplots(figsize=(9, 4.5))
        im = ax_corr.imshow(CORRELATION_BASE, cmap=mcolors.LinearSegmentedColormap.from_list("blue", ["#e6f0ff", PRIMARY_BLUE]))
        ax_corr.set_xticks(np.arange(len(CORR_COMPANY_LIST)))
        ax_corr.set_yticks(np.arange(len(CORR_COMPANY_LIST)))
        ax_corr.set_xticklabels(CORR_COMPANY_LIST, rotation=45, ha="right")
        ax_corr.set_yticklabels(CORR_COMPANY_LIST)

        # Print number value on heatmap cells
        for i in range(len(CORR_COMPANY_LIST)):
            for j in range(len(CORR_COMPANY_LIST)):
                text = ax_corr.text(j, i, CORRELATION_BASE[i, j], ha="center", va="center", color="white", fontweight="bold")
        plt.tight_layout()
        st.pyplot(fig_corr)

# ===================== TAB 4: RISK ASSESSMENT (FULL PERFECT REPLICA) =====================
elif st.session_state.active_tab == "Risk Assessment":
    st.markdown("## Risk Assessment")
    # 4 Risk Metric Cards
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        change_color = POSITIVE_GREEN if data["var_change"] >= 0 else NEGATIVE_RED
        st.metric(
            label="VaR (95%)",
            value=f"¥{data['var_95']:,}",
            delta=f"¥{data['var_change']:+.0f}"
        )
        st.markdown(f"<style>[data-testid='stMetricDelta']{{color:{change_color};}}</style>", unsafe_allow_html=True)

    with c2:
        change_color = POSITIVE_GREEN if data["volatility_change"] >= 0 else NEGATIVE_RED
        st.metric(
            label="Volatility",
            value=f"{data['volatility']} %",
            delta=f"{data['volatility_change']:+.1f}%"
        )
        st.markdown(f"<style>[data-testid='stMetricDelta']{{color:{change_color};}}</style>", unsafe_allow_html=True)

    with c3:
        change_color = POSITIVE_GREEN if data["beta_change"] >= 0 else NEGATIVE_RED
        st.metric(
            label="Beta Coefficient",
            value=f"{data['beta_coeff']}",
            delta=f"{data['beta_change']:+.2f}"
        )
        st.markdown(f"<style>[data-testid='stMetricDelta']{{color:{change_color};}}</style>", unsafe_allow_html=True)

    with c4:
        change_color = POSITIVE_GREEN if data["downside_risk_change"] >= 0 else NEGATIVE_RED
        st.metric(
            label="Downside Risk",
            value=f"{data['downside_risk']} %",
            delta=f"{data['downside_risk_change']:+.1f}%"
        )
        st.markdown(f"<style>[data-testid='stMetricDelta']{{color:{change_color};}}</style>", unsafe_allow_html=True)

    st.divider()
    chart_col1, chart_col2 = st.columns(2)

    # Chart 1: Risk-Return Scatter Plot
    with chart_col1:
        st.markdown("### Risk-Return Matrix")
        risk_x = [9.7, 12.3, 15.2, 18.5, 21.4]
        return_y = [18.2, 15.2, 22.6, 19.4, 25.8]
        fig_risk, ax_risk = plt.subplots(figsize=(10, 4.5))
        ax_risk.scatter(risk_x, return_y, color=PRIMARY_BLUE, s=120)
        ax_risk.set_xlabel("Risk (%)")
        ax_risk.set_ylabel("Expected Return (%)")
        ax_risk.set_ylim(0, 30)
        ax_risk.set_xlim(0, 25)
        ax_risk.grid(alpha=0.2, linestyle="--")
        plt.tight_layout()
        st.pyplot(fig_risk)

    # Chart 2: VaR Value Trend Bar Chart
    with chart_col2:
        st.markdown("### VaR Risk Value Trend")
        year_label = ["2021", "2022", "2023", "2024", "2025", "2026"]
        var_data = data["var_year_trend"]
        fig_var, ax_var = plt.subplots(figsize=(10, 4.5))
        ax_var.bar(year_label, var_data, color=PRIMARY_BLUE, alpha=0.85)
        ax_var.set_ylabel("Value (¥)")
        ax_var.grid(alpha=0.2, linestyle="--")
        plt.tight_layout()
        st.pyplot(fig_var)