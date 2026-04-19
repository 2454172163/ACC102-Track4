import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Home Appliance Giants Analysis Tool",
    layout="wide"
)

st.title("Home Appliance Giants Stock & Financial Analysis Tool")
st.subheader("Midea Group | Gree Electric | Haier Smart Home")

# Sidebar
with st.sidebar:
    st.header("Analysis Settings")
    selected_company = st.selectbox(
        "Select a Company",
        ["Midea Group", "Gree Electric", "Haier Smart Home"]
    )
    start_date = st.date_input("Start Date", pd.to_datetime("2023-01-01"))
    end_date = st.date_input("End Date", pd.to_datetime("2025-01-01"))

# Financial Indicators
st.markdown("---")
st.subheader("Core Financial Indicators (2024)")
financial_data = {
    "Midea Group": {"ROE (%)": 23.5, "Gross Margin (%)": 22.8, "Revenue Growth (%)": 5.6},
    "Gree Electric": {"ROE (%)": 18.2, "Gross Margin (%)": 24.5, "Revenue Growth (%)": 1.2},
    "Haier Smart Home": {"ROE (%)": 21.7, "Gross Margin (%)": 23.1, "Revenue Growth (%)": 6.3}
}
st.dataframe(pd.DataFrame(financial_data).T, use_container_width=True)

# Simulated Stock Price
st.markdown("---")
st.subheader("Simulated Stock Price Trend")
dates = pd.date_range(start=start_date, end=end_date, freq='M')
base_price = {"Midea Group": 60, "Gree Electric": 30, "Haier Smart Home": 20}
prices = [base_price[selected_company] + i*0.2 + np.random.randn()*2 for i in range(len(dates))]
df = pd.DataFrame({"Date": dates, "Closing Price (CNY)": prices})

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df["Date"], df["Closing Price (CNY)"], linewidth=2)
ax.set_title(f"{selected_company} Simulated Price")
st.pyplot(fig, use_container_width=True)

# Download
st.download_button("Download CSV", df.to_csv(index=False).encode("utf-8"), "stock_data.csv")
st.success("Tool loaded successfully.")