<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta http-equiv="Content-Style-Type" content="text/css">
  <title></title>
  <meta name="Generator" content="Cocoa HTML Writer">
  <meta name="CocoaVersion" content="2575.7">
  <style type="text/css">
    p.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 16.0px 'Helvetica Neue'; -webkit-text-stroke: #000000}
    p.p2 {margin: 0.0px 0.0px 0.0px 0.0px; font: 16.0px 'Helvetica Neue'; -webkit-text-stroke: #000000; min-height: 18.0px}
    span.s1 {font-kerning: none}
  </style>
</head>
<body>
<p class="p1"><span class="s1">import streamlit as st</span></p>
<p class="p1"><span class="s1">import yfinance as yf</span></p>
<p class="p1"><span class="s1">import pandas as pd</span></p>
<p class="p1"><span class="s1">import matplotlib.pyplot as plt</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">st.set_page_config(page_title="家电三巨头分析工具", layout="wide")</span></p>
<p class="p1"><span class="s1">st.title("家电三巨头 股价与财务指标交互式分析工具")</span></p>
<p class="p1"><span class="s1">st.subheader("美的集团(000333.SZ) | 格力电器(000651.SZ) | 海尔智家(600690.SH)")</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">st.sidebar.header("参数设置")</span></p>
<p class="p1"><span class="s1">company = st.sidebar.selectbox("选择公司", ["美的集团", "格力电器", "海尔智家"])</span></p>
<p class="p1"><span class="s1">start_date = st.sidebar.date_input("开始日期", pd.to_datetime("2020-01-01"))</span></p>
<p class="p1"><span class="s1">end_date = st.sidebar.date_input("结束日期", pd.to_datetime("2025-01-01"))</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">code_dict = {</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>"美的集团": "000333.SZ",</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>"格力电器": "000651.SZ",</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>"海尔智家": "600690.SH"</span></p>
<p class="p1"><span class="s1">}</span></p>
<p class="p1"><span class="s1">ticker = code_dict[company]</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">st.subheader("1. 股价走势分析")</span></p>
<p class="p1"><span class="s1">data = yf.download(ticker, start=start_date, end=end_date)</span></p>
<p class="p1"><span class="s1">if not data.empty:</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>data = data[["Close"]]</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>data.columns = ["收盘价"]</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>st.dataframe(data.head(10))</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>fig, ax = plt.subplots(figsize=(10, 4))</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>ax.plot(data.index, data["收盘价"], label=f"{company}收盘价")</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>ax.set_title(f"{company}收盘价走势")</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>ax.set_xlabel("日期")</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>ax.set_ylabel("收盘价(元)")</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>ax.legend()</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>st.pyplot(fig)</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>csv = data.to_csv().encode("utf-8")</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>st.download_button("下载股价数据", csv, f"{company}_股价数据.csv", "text/csv")</span></p>
<p class="p1"><span class="s1">else:</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>st.warning("暂无数据，请调整日期")</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">st.subheader("2. 核心财务指标（年度）")</span></p>
<p class="p1"><span class="s1">finance_data = {</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>"美的": {"ROE": "23.5%", "毛利率": "22.8%", "营收增速": "5.6%"},</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>"格力": {"ROE": "18.2%", "毛利率": "24.5%", "营收增速": "1.2%"},</span></p>
<p class="p1"><span class="s1"><span class="Apple-converted-space">    </span>"海尔": {"ROE": "21.7%", "毛利率": "23.1%", "营收增速": "6.3%"}</span></p>
<p class="p1"><span class="s1">}</span></p>
<p class="p1"><span class="s1">finance_df = pd.DataFrame(finance_data[company])</span></p>
<p class="p1"><span class="s1">st.dataframe(finance_df)</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">st.success("工具运行完成！可切换公司、调整日期查看不同数据")</span></p>
</body>
</html>
