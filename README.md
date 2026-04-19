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
<p class="p1"><span class="s1"># 家电三巨头交互式财务分析工具</span></p>
<p class="p1"><span class="s1">## 1. 问题与目标用户</span></p>
<p class="p1"><span class="s1">帮助会计/金融专业学生、投资者快速查看家电行业头部企业的股价走势与核心财务指标，提供可视化、可交互、可下载的数据分析工具。</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">## 2. 数据</span></p>
<p class="p1"><span class="s1">数据来源：雅虎财经(yfinance)</span></p>
<p class="p1"><span class="s1">获取日期：2026年4月19日</span></p>
<p class="p1"><span class="s1">核心字段：股票收盘价、ROE、毛利率、营收增速</span></p>
<p class="p1"><span class="s1">涉及公司：美的集团、格力电器、海尔智家</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">## 3. 分析方法</span></p>
<p class="p1"><span class="s1">使用Python进行数据获取、清洗、可视化</span></p>
<p class="p1"><span class="s1">使用Streamlit搭建交互式界面</span></p>
<p class="p1"><span class="s1">实现功能：公司切换、日期筛选、股价绘图、数据下载、财务指标展示</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">## 4. 核心结论</span></p>
<p class="p1"><span class="s1">1. 三家企业股价走势受行业周期与市场环境影响明显</span></p>
<p class="p1"><span class="s1">2. 海尔智家营收增速领先，格力电器毛利率最高，美的集团ROE表现最优</span></p>
<p class="p1"><span class="s1">3. 工具可快速对比企业经营与股价表现，辅助基础投资与财务分析</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">## 5. 运行方法</span></p>
<p class="p1"><span class="s1">1. 安装依赖：pip install -r requirements.txt</span></p>
<p class="p1"><span class="s1">2. 运行工具：streamlit run app.py</span></p>
<p class="p1"><span class="s1">3. 在侧边栏选择公司与日期，查看结果</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">## 6. 产品链接与演示</span></p>
<p class="p1"><span class="s1">本地运行即可使用，无需云端部署</span></p>
<p class="p2"><span class="s1"></span><br></p>
<p class="p1"><span class="s1">## 7. 局限性与优化方向</span></p>
<p class="p1"><span class="s1">1. 财务数据为手动整理，可后续对接API自动获取</span></p>
<p class="p1"><span class="s1">2. 可增加更多财务指标与行业对比功能</span></p>
<p class="p1"><span class="s1">3. 可扩展季度数据、分红数据等分析维度</span></p>
</body>
</html>
