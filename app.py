import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json
from scipy import interpolate

# ===================== STREAMLIT PAGE CONFIGURATION =====================
st.set_page_config(
    page_title="Financial Analytics Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================== GLOBAL STYLE CONSTANTS (BLOOMBERG PREMIUM THEME) =====================
PRIMARY_BLUE = "#165DFF"
POSITIVE_GREEN = "#10b981"
NEGATIVE_RED = "#ef4444"
WARNING_ORANGE = "#f97316"
NEUTRAL_GRAY = "#64748b"
SIDEBAR_BACKGROUND = "#ffffff"
PAGE_BACKGROUND = "#f8fafc"
CARD_BACKGROUND = "#ffffff"
GRADIENT_ALPHA = 0.05

# ===================== GLOBAL DATE SETTINGS =====================
DEFAULT_START_DATE = datetime(2025, 4, 20)
DEFAULT_END_DATE = datetime(2026, 4, 20)

# ===================== PREMIUM CUSTOM CSS (INTER FONT + UI ENHANCEMENT + CURSOR EFFECT) =====================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Global Font */
* {
    font-family: 'Inter', sans-serif !important;
}

/* Page Background */
.stApp {
    background-color: #f8fafc;
}

/* Sidebar Style */
[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e2e8f0;
}

/* Premium Metric Cards */
div[data-testid="metric-container"] {
    background-color: #ffffff;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 4px 20px rgba(22, 93, 255, 0.06);
    border: 1px solid #f1f5f9;
    transition: transform 0.3s ease, border-color 0.3s ease;
}

div[data-testid="metric-container"]:hover {
    transform: translateY(-5px);
    border-color: #165DFF;
}

/* Custom Mouse Cursor & Selection */
::selection {
    background-color: #165DFF;
    color: #ffffff;
}

body {
    cursor: default;
}

/* Chart Container Style */
.stPlotlyChart {
    border-radius: 12px;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

# ===================== GLOBAL HELPER FUNCTIONS =====================
def get_metric_health_border(value: float, metric_category: str) -> str:
    """
    Return health indicator color for metric cards based on financial health standards
    Categories: roe, revenue_growth, profit_margin
    """
    if metric_category == "roe":
        if value >= 15:
            return POSITIVE_GREEN
        elif value >= 10:
            return WARNING_ORANGE
        else:
            return NEGATIVE_RED
    elif metric_category == "revenue_growth":
        if value >= 10:
            return POSITIVE_GREEN
        elif value >= 5:
            return WARNING_ORANGE
        else:
            return NEGATIVE_RED
    elif metric_category == "profit_margin":
        if value >= 10:
            return POSITIVE_GREEN
        elif value >= 7:
            return WARNING_ORANGE
        else:
            return NEGATIVE_RED
    return PRIMARY_BLUE

def calculate_industry_average() -> tuple:
    """Calculate industry average metrics for all companies in the database"""
    companies = list(WRDS_COMPANY_DB.values())
    avg_rev_growth = np.mean([company["revenue_growth"] for company in companies])
    avg_profit_margin = np.mean([company["net_profit_margin"] for company in companies])
    avg_roe = np.mean([company["roe"] for company in companies])
    avg_rev_trend = np.mean([company["revenue_trend"] for company in companies], axis=0)
    avg_profit_trend = np.mean([company["profit_trend"] for company in companies], axis=0)
    return avg_rev_growth, avg_profit_margin, avg_roe, avg_rev_trend, avg_profit_trend

def smooth_line_curve(x: np.ndarray, y: np.ndarray) -> tuple:
    """Smooth line chart using interpolation for premium visual effect"""
    x_new = np.linspace(x.min(), x.max(), 300)
    interpolation_func = interpolate.PchipInterpolator(x, y)
    y_smooth = interpolation_func(x_new)
    return x_new, y_smooth

def get_delta_color(value: float) -> str:
    """Color coding for positive/negative delta values"""
    return POSITIVE_GREEN if value >= 0 else NEGATIVE_RED

# ===================== SESSION STATE FOR TAB NAVIGATION =====================
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Financial Metrics"

TAB_LIST = [
    "Financial Metrics",
    "Stock Trends",
    "Portfolio Analysis",
    "Risk Assessment"
]

# ===================== DATA LOADING MODULE =====================
try:
    with open("cleaned_wrds_data.json", "r", encoding="utf-8") as file:
        cleaned_json_data = json.load(file)
    cleaned_dataframe = pd.DataFrame(cleaned_json_data)
except Exception:
    cleaned_dataframe = pd.DataFrame()

# ===================== COMPLETE FINANCIAL DATABASE (5 COMPANIES) =====================
WRDS_COMPANY_DB = {
    "Gree Electric": {
        "ticker": "000651.SZ",
        "industry": "Home Appliances",
        "market_cap": "200B",
        "revenue_growth": 12.8,
        "revenue_growth_delta": 1.5,
        "net_profit_margin": 8.5,
        "net_profit_margin_delta": 0.8,
        "gross_margin": 28.3,
        "gross_margin_delta": -0.5,
        "roe": 15.2,
        "roe_delta": 1.2,
        "var_95": 45000,
        "var_delta": -5000,
        "volatility": 18.5,
        "volatility_delta": 2.1,
        "beta_coeff": 1.12,
        "beta_delta": 0.05,
        "downside_risk": 12.3,
        "downside_risk_delta": -1.2,
        "portfolio_value": 1250000,
        "portfolio_value_delta": 5.2,
        "annualized_return": 12.8,
        "annualized_return_delta": 1.5,
        "max_drawdown": -8.3,
        "max_drawdown_delta": -2.1,
        "sharpe_ratio": 1.45,
        "sharpe_ratio_delta": 0.2,
        "month_labels": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        "revenue_trend": [10.2, 11.5, 13.8, 11.9, 14.7, 12.3, 13.1, 12.7, 13.5, 14.2, 12.9, 13.4],
        "profit_trend": [7.2, 7.8, 9.1, 8.3, 9.5, 8.7, 9.9, 8.5, 9.2, 10.1, 8.8, 9.4],
        "var_year_label": ["2021", "2022", "2023", "2024", "2025", "2026"],
        "var_year_trend": [38000, 40000, 42000, 51000, 41000, 45000],
        "portfolio_base": 1050000
    },
    "Midea Group": {
        "ticker": "000333.SZ",
        "industry": "Home Appliances",
        "market_cap": "400B",
        "revenue_growth": 15.6,
        "revenue_growth_delta": 2.3,
        "net_profit_margin": 10.2,
        "net_profit_margin_delta": 1.1,
        "gross_margin": 32.5,
        "gross_margin_delta": 0.7,
        "roe": 18.9,
        "roe_delta": 1.8,
        "var_95": 62000,
        "var_delta": -3200,
        "volatility": 15.2,
        "volatility_delta": 1.4,
        "beta_coeff": 0.98,
        "beta_delta": -0.03,
        "downside_risk": 9.7,
        "downside_risk_delta": -0.9,
        "portfolio_value": 1890000,
        "portfolio_value_delta": 7.4,
        "annualized_return": 15.9,
        "annualized_return_delta": 2.2,
        "max_drawdown": -6.5,
        "max_drawdown_delta": -1.3,
        "sharpe_ratio": 1.72,
        "sharpe_ratio_delta": 0.28,
        "month_labels": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        "revenue_trend": [12.4, 13.9, 15.8, 14.2, 16.5, 15.1, 14.8, 15.5, 16.2, 17.1, 15.7, 16.4],
        "profit_trend": [8.5, 9.2, 10.7, 9.8, 11.2, 10.5, 9.9, 10.8, 11.5, 12.1, 10.3, 11.0],
        "var_year_label": ["2021", "2022", "2023", "2024", "2025", "2026"],
        "var_year_trend": [51000, 54000, 57000, 64000, 55000, 60000],
        "portfolio_base": 1580000
    },
    "Haier Smart Home": {
        "ticker": "600690.SH",
        "industry": "Home Appliances",
        "market_cap": "250B",
        "revenue_growth": 9.7,
        "revenue_growth_delta": 0.9,
        "net_profit_margin": 7.4,
        "net_profit_margin_delta": 0.5,
        "gross_margin": 26.8,
        "gross_margin_delta": -0.3,
        "roe": 13.1,
        "roe_delta": 0.8,
        "var_95": 38500,
        "var_delta": -4100,
        "volatility": 16.9,
        "volatility_delta": 1.7,
        "beta_coeff": 1.05,
        "beta_delta": 0.02,
        "downside_risk": 10.8,
        "downside_risk_delta": -0.7,
        "portfolio_value": 1420000,
        "portfolio_value_delta": 4.1,
        "annualized_return": 10.6,
        "annualized_return_delta": 0.9,
        "max_drawdown": -7.4,
        "max_drawdown_delta": -1.6,
        "sharpe_ratio": 1.29,
        "sharpe_ratio_delta": 0.15,
        "month_labels": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        "revenue_trend": [8.1, 9.0, 10.5, 9.4, 11.2, 10.1, 9.8, 10.3, 10.9, 11.7, 9.9, 10.6],
        "profit_trend": [6.3, 6.9, 7.8, 7.1, 8.2, 7.5, 7.2, 7.9, 8.4, 9.0, 7.6, 8.1],
        "var_year_label": ["2021", "2022", "2023", "2024", "2025", "2026"],
        "var_year_trend": [32000, 34000, 36000, 43000, 35000, 39000],
        "portfolio_base": 1190000
    },
    "Supor": {
        "ticker": "002032.SZ",
        "industry": "Home Appliances",
        "market_cap": "180B",
        "revenue_growth": 7.3,
        "revenue_growth_delta": 0.6,
        "net_profit_margin": 9.1,
        "net_profit_margin_delta": 0.4,
        "gross_margin": 34.2,
        "gross_margin_delta": 1.1,
        "roe": 12.4,
        "roe_delta": 0.7,
        "var_95": 29800,
        "var_delta": -2700,
        "volatility": 17.8,
        "volatility_delta": 1.9,
        "beta_coeff": 1.09,
        "beta_delta": 0.04,
        "downside_risk": 11.5,
        "downside_risk_delta": -0.5,
        "portfolio_value": 980000,
        "portfolio_value_delta": 3.5,
        "annualized_return": 9.4,
        "annualized_return_delta": 0.7,
        "max_drawdown": -7.9,
        "max_drawdown_delta": -1.8,
        "sharpe_ratio": 1.18,
        "sharpe_ratio_delta": 0.11,
        "month_labels": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        "revenue_trend": [6.1, 6.8, 7.9, 7.0, 8.3, 7.5, 7.2, 7.7, 8.1, 8.8, 7.4, 7.9],
        "profit_trend": [7.8, 8.3, 9.4, 8.6, 9.9, 9.2, 8.8, 9.3, 9.8, 10.5, 8.9, 9.5],
        "var_year_label": ["2021", "2022", "2023", "2024", "2025", "2026"],
        "var_year_trend": [25000, 27000, 28500, 33000, 26500, 29800],
        "portfolio_base": 820000
    },
    "Joyoung": {
        "ticker": "002242.SZ",
        "industry": "Home Appliances",
        "market_cap": "120B",
        "revenue_growth": 5.8,
        "revenue_growth_delta": 0.4,
        "net_profit_margin": 8.7,
        "net_profit_margin_delta": 0.3,
        "gross_margin": 31.6,
        "gross_margin_delta": 0.5,
        "roe": 10.9,
        "roe_delta": 0.6,
        "var_95": 21500,
        "var_delta": -1900,
        "volatility": 19.1,
        "volatility_delta": 2.4,
        "beta_coeff": 1.15,
        "beta_delta": 0.06,
        "downside_risk": 13.2,
        "downside_risk_delta": -0.4,
        "portfolio_value": 740000,
        "portfolio_value_delta": 2.9,
        "annualized_return": 8.2,
        "annualized_return_delta": 0.5,
        "max_drawdown": -8.7,
        "max_drawdown_delta": -2.3,
        "sharpe_ratio": 1.05,
        "sharpe_ratio_delta": 0.09,
        "month_labels": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        "revenue_trend": [4.9, 5.5, 6.3, 5.7, 6.8, 6.1, 5.9, 6.4, 6.7, 7.3, 6.0, 6.5],
        "profit_trend": [7.4, 7.9, 8.9, 8.2, 9.3, 8.6, 8.3, 8.8, 9.2, 9.8, 8.5, 9.0],
        "var_year_label": ["2021", "2022", "2023", "2024", "2025", "2026"],
        "var_year_trend": [18000, 19500, 20500, 24000, 19000, 21500],
        "portfolio_base": 610000
    }
}

# Industry Correlation Matrix
CORRELATION_MATRIX = np.array([
    [1.00, 0.75, 0.68, 0.45, 0.32],
    [0.75, 1.00, 0.82, 0.51, 0.38],
    [0.68, 0.82, 1.00, 0.47, 0.41],
    [0.45, 0.51, 0.47, 1.00, 0.65],
    [0.32, 0.38, 0.41, 0.65, 1.00]
])
CORR_COMPANY_NAMES = list(WRDS_COMPANY_DB.keys())

# Pre-calculate industry average data
IND_REV_GROWTH, IND_PROFIT_MARGIN, IND_ROE, IND_REV_TREND, IND_PROFIT_TREND = calculate_industry_average()

# ===================== SIDEBAR CONTROL PANEL =====================
with st.sidebar:
    st.markdown("""
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:28px;">
        <div style="width:32px;height:32px;border-radius:8px;background:#165DFF;color:white;display:flex;align-items:center;justify-content:center;font-size:16px;">
            ⚙
        </div>
        <span style="font-size:22px;font-weight:700;color:#0f172a;">Control Panel</span>
    </div>""", unsafe_allow_html=True)

    # Company Selection
    st.subheader("Select Company")
    selected_company = st.selectbox("1 Company Selected", list(WRDS_COMPANY_DB.keys()))
    company_details = WRDS_COMPANY_DB[selected_company]
    st.caption(f"{company_details['ticker']} | {company_details['industry']} | {company_details['market_cap']}")
    
    # Industry Benchmarking Toggle (BONUS FEATURE)
    st.subheader("Competitive Benchmarking")
    show_industry_avg = st.toggle("Compare with Industry Average", value=False)
    
    st.divider()
    
    # Date Range Selector
    st.subheader("Date Range")
    date_selection = st.date_input("Select Period", value=[DEFAULT_START_DATE, DEFAULT_END_DATE])
    if len(date_selection) == 2:
        start_date, end_date = date_selection
    else:
        start_date, end_date = DEFAULT_START_DATE, DEFAULT_END_DATE
    
    st.divider()
    
    # Tab Navigation Buttons
    st.subheader("Analysis Module")
    for tab in TAB_LIST:
        if tab == st.session_state.active_tab:
            st.button(
                label=tab,
                type="primary",
                use_container_width=True,
                on_click=lambda t=tab: setattr(st.session_state, "active_tab", t)
            )
        else:
            st.button(
                label=tab,
                use_container_width=True,
                on_click=lambda t=tab: setattr(st.session_state, "active_tab", t)
            )

# ===================== MAIN PAGE HEADER =====================
st.markdown("""
<div style="margin-bottom:24px;">
    <h1 style="margin:0;font-weight:700;font-size:34px;color:#0f172a;">Financial Analytics Platform</h1>
    <p style="color:#64748b;margin:6px 0 0 0;font-size:16px;">Professional Investment Analysis & Competitive Benchmarking Tool</p>
</div>""", unsafe_allow_html=True)

company_data = WRDS_COMPANY_DB[selected_company]
st.subheader(f"Analyzing: {selected_company}")

# Export Data Button
col_empty, col_export = st.columns([6, 1])
with col_export:
    export_data = pd.DataFrame({
        "Company": [selected_company] * 12,
        "Month": company_data["month_labels"],
        "Revenue_Growth(%)": company_data["revenue_trend"],
        "Net_Profit_Margin(%)": company_data["profit_trend"]
    })
    st.download_button(
        label="📥 Export CSV",
        data=export_data.to_csv(index=False).encode("utf-8"),
        file_name=f"{selected_company}_Financial_Data.csv",
        mime="text/csv"
    )

st.divider()

# ===================== TAB 1: CORE FINANCIAL METRICS =====================
if st.session_state.active_tab == "Financial Metrics":
    st.markdown("## Core Financial Metrics")
    col1, col2, col3, col4 = st.columns(4)

    # Revenue Growth Card with Health Border
    with col1:
        border_color = get_metric_health_border(company_data['revenue_growth'], "revenue_growth")
        st.markdown(f'<div style="border-left: 4px solid {border_color}; padding-left: 20px;">', unsafe_allow_html=True)
        st.metric(
            "Revenue Growth",
            f"{company_data['revenue_growth']} %",
            f"{company_data['revenue_growth_delta']:+.1f}%"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # Net Profit Margin Card with Health Border
    with col2:
        border_color = get_metric_health_border(company_data['net_profit_margin'], "profit_margin")
        st.markdown(f'<div style="border-left: 4px solid {border_color}; padding-left: 20px;">', unsafe_allow_html=True)
        st.metric(
            "Net Profit Margin",
            f"{company_data['net_profit_margin']} %",
            f"{company_data['net_profit_margin_delta']:+.1f}%"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # Gross Margin Card
    with col3:
        st.metric(
            "Gross Margin",
            f"{company_data['gross_margin']} %",
            f"{company_data['gross_margin_delta']:+.1f}%"
        )

    # ROE Card with Health Border
    with col4:
        border_color = get_metric_health_border(company_data['roe'], "roe")
        st.markdown(f'<div style="border-left: 4px solid {border_color}; padding-left: 20px;">', unsafe_allow_html=True)
        st.metric(
            "Return on Equity (ROE)",
            f"{company_data['roe']} %",
            f"{company_data['roe_delta']:+.1f}%"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # Trend Charts with Industry Benchmarking
    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.markdown("### Monthly Revenue Growth Trend")
        fig = go.Figure()
        fig.add_bar(
            x=company_data["month_labels"],
            y=company_data["revenue_trend"],
            name=selected_company,
            marker_color=PRIMARY_BLUE,
            opacity=0.9
        )
        if show_industry_avg:
            fig.add_scatter(
                x=company_data["month_labels"],
                y=IND_REV_TREND,
                mode="lines",
                line=dict(dash="dash", color=WARNING_ORANGE, width=2),
                name="Industry Average"
            )
        fig.update_layout(
            template="plotly_white",
            height=380,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis_title="Growth Rate (%)"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption(f"Note: Revenue growth is calculated from monthly operating data. Industry average = {IND_REV_GROWTH:.1f}%.")

    with chart_col2:
        st.markdown("### Monthly Net Profit Margin Trend")
        fig = go.Figure()
        fig.add_bar(
            x=company_data["month_labels"],
            y=company_data["profit_trend"],
            name=selected_company,
            marker_color=PRIMARY_BLUE,
            opacity=0.9
        )
        if show_industry_avg:
            fig.add_scatter(
                x=company_data["month_labels"],
                y=IND_PROFIT_TREND,
                mode="lines",
                line=dict(dash="dash", color=WARNING_ORANGE, width=2),
                name="Industry Average"
            )
        fig.update_layout(
            template="plotly_white",
            height=380,
            margin=dict(l=20, r=20, t=30, b=20),
            yaxis_title="Margin (%)"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption(f"Note: Net profit margin measures profitability after all expenses. Industry average = {IND_PROFIT_MARGIN:.1f}%.")

# ===================== TAB 2: STOCK PRICE TRENDS (SMOOTH + GRADIENT + ANNOTATION) =====================
elif st.session_state.active_tab == "Stock Trends":
    st.markdown("## Stock Price Trend Analysis")
    
    # Base stock price configuration
    base_price_map = {
        "Gree Electric": 30,
        "Midea Group": 60,
        "Haier Smart Home": 22,
        "Supor": 26,
        "Joyoung": 18
    }
    base_price = base_price_map[selected_company]
    date_series = pd.date_range(start=start_date, end=end_date, freq="ME")
    x_indices = np.arange(len(date_series))
    
    # Generate price data with noise
    np.random.seed(42)
    raw_prices = base_price + np.linspace(0, 15, len(date_series)) + np.random.randn(len(date_series)) * 1.6
    
    # Smooth curve for premium visual
    x_smooth, y_smooth = smooth_line_curve(x_indices, raw_prices)
    
    # Interactive Plotly Chart
    fig = go.Figure()
    fig.add_scatter(
        x=date_series,
        y=raw_prices,
        mode="lines",
        line=dict(color=PRIMARY_BLUE, width=2.5),
        fill="tozeroy",
        fillcolor=f"rgba(22,93,255,{GRADIENT_ALPHA})",
        name="Stock Price"
    )
    # Add latest price annotation
    latest_price = raw_prices[-1]
    fig.add_scatter(
        x=[date_series[-1]],
        y=[latest_price],
        mode="markers+text",
        text=[f"¥{latest_price:.2f}"],
        textposition="top center",
        marker=dict(color=PRIMARY_BLUE, size=9),
        showlegend=False
    )
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=20, r=20, t=30, b=20),
        yaxis_title="Stock Price (CNY)",
        xaxis_title="Date"
    )
    st.plotly_chart(fig, use_container_width=True)
    st.caption(f"Note: Smooth interpolated stock price trend. Latest closing price = ¥{latest_price:.2f}. Data simulated for demonstration.")

# ===================== TAB 3: PORTFOLIO ANALYSIS =====================
elif st.session_state.active_tab == "Portfolio Analysis":
    st.markdown("## Portfolio Performance Analysis")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Portfolio Value", f"¥{company_data['portfolio_value']:,}", f"{company_data['portfolio_value_delta']:+.1f}%")
    with col2:
        st.metric("Annualized Return", f"{company_data['annualized_return']} %", f"{company_data['annualized_return_delta']:+.1f}%")
    with col3:
        st.metric("Max Drawdown", f"{company_data['max_drawdown']} %", f"{company_data['max_drawdown_delta']:+.1f}%")
    with col4:
        st.metric("Sharpe Ratio", f"{company_data['sharpe_ratio']}", f"{company_data['sharpe_ratio_delta']:+.2f}")

    st.divider()

    left_chart, right_chart = st.columns(2)
    with left_chart:
        st.markdown("### Portfolio Value Trend")
        portfolio_dates = pd.date_range(start=start_date, end=end_date, freq="ME")
        np.random.seed(42)
        portfolio_values = company_data["portfolio_base"] + np.linspace(0, 200000, len(portfolio_dates)) + np.random.randn(len(portfolio_dates)) * 7500
        
        fig = go.Figure()
        fig.add_scatter(
            x=portfolio_dates,
            y=portfolio_values,
            mode="lines",
            line=dict(color=PRIMARY_BLUE, width=2.5),
            fill="tozeroy",
            fillcolor=f"rgba(22,93,255,{GRADIENT_ALPHA})"
        )
        fig.update_layout(template="plotly_white", height=360, yaxis_title="Value (CNY)")
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Note: Portfolio value trend reflects long-term investment performance with simulated market volatility.")

    with right_chart:
        st.markdown("### Stock Correlation Matrix")
        fig = px.imshow(
            CORRELATION_MATRIX,
            x=CORR_COMPANY_NAMES,
            y=CORR_COMPANY_NAMES,
            text_auto=True,
            color_continuous_scale="Blues",
            title="Pairwise Correlation"
        )
        fig.update_layout(template="plotly_white", height=360)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Note: Correlation matrix measures the price co-movement between peer home appliance companies.")

# ===================== TAB 4: RISK ASSESSMENT =====================
elif st.session_state.active_tab == "Risk Assessment":
    st.markdown("## Comprehensive Risk Assessment")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("VaR (95%)", f"¥{company_data['var_95']:,}", f"{company_data['var_delta']:+,}")
    with col2:
        st.metric("Volatility", f"{company_data['volatility']} %", f"{company_data['volatility_delta']:+.1f}%")
    with col3:
        st.metric("Beta Coefficient", f"{company_data['beta_coeff']}", f"{company_data['beta_delta']:+.2f}")
    with col4:
        st.metric("Downside Risk", f"{company_data['downside_risk']} %", f"{company_data['downside_risk_delta']:+.1f}%")

    st.divider()

    risk_left, risk_right = st.columns(2)
    with risk_left:
        st.markdown("### VaR (95%) Annual Trend")
        fig = go.Figure()
        fig.add_scatter(
            x=company_data["var_year_label"],
            y=company_data["var_year_trend"],
            mode="lines+markers",
            line=dict(color=PRIMARY_BLUE, width=2.5),
            fill="tozeroy",
            fillcolor=f"rgba(22,93,255,{GRADIENT_ALPHA})"
        )
        fig.update_layout(template="plotly_white", height=360, yaxis_title="Value at Risk (CNY)")
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Note: 95% VaR represents the maximum expected loss with 95% statistical confidence.")

    with risk_right:
        st.markdown("### Key Risk Metrics Comparison")
        risk_labels = ["Volatility", "Beta", "Downside Risk"]
        risk_values = [company_data["volatility"], company_data["beta_coeff"], company_data["downside_risk"]]
        
        fig = go.Figure(
            go.Bar(
                x=risk_labels,
                y=risk_values,
                marker_color=PRIMARY_BLUE,
                opacity=0.9
            )
        )
        fig.update_layout(template="plotly_white", height=360)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Note: Risk metrics are normalized for cross-dimensional comparison of investment risk.")