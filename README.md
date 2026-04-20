# ACC102 Track4: Financial Analytics Platform for Chinese Home Appliance Listed Companies
## Individual Mini Assignment

**Student Name**: Xinyao.Zhang
**Student ID**: 2472353
**WRDS Username**: Xinyao24

---

## Project Overview
This project is an interactive financial analytics dashboard built with Streamlit. It focuses on financial performance, stock trends, portfolio management, and risk assessment for 5 major Chinese home appliance companies. The project fully complies with ACC102 Track4 requirements, including raw data processing, data cleaning, quantitative analysis, financial visualization, and a local interactive user interface.

## Data Source
- Primary Database: WRDS Compustat Global (Fundamental Financial Metrics) + WRDS CRSP (Market Risk Metrics)
- Data Cleaning & Processing Workflow: Fully completed in analysis.ipynb
- Analyzed Listed Companies: Gree Electric, Midea Group, Haier Smart Home, Supor, Joyoung

## Core Functions
1. Core Financial Metrics Analysis (Revenue Growth, Profit Margin, ROE, Gross Margin)
2. Historical Stock Trend Visualization
3. Investment Portfolio Performance Evaluation
4. Multi-dimensional Risk Assessment (VaR, Volatility, Beta, Downside Risk)
5. Inter-company Stock Correlation Matrix Analysis
6. Export of Cleaned Structured Dataset

## File Structure
├── app.py                  # Main Streamlit interactive dashboard program
├── analysis.ipynb          # Data collection, cleaning, statistical analysis & processing
├── requirements.txt        # All project dependency installation packages
├── README.md               # Complete project operation documentation
├── cleaned_wrds_data.json  # Auto-generated exported cleaned WRDS dataset
└── reflection_report.pdf   # Personal learning reflection report

## Installation & Execution Steps (Mac OS)
1. Open Terminal and navigate to the project folder:
cd /Users/cynthia/Desktop/ACC102-Track4

2. Install all required dependency packages:
pip install -r requirements.txt

3. Complete data cleaning and quantitative analysis:
Open and run all code cells inside analysis.ipynb to generate cleaned dataset.

4. Launch the local interactive dashboard:
streamlit run app.py

## Mandatory Assignment Compliance Statement
1. Local Runtime Only: This tool is designed for local execution on personal devices. Streamlit Cloud remote deployment is strictly prohibited.
2. All documentation, code comments, and analytical content are fully written in English.
3. Complete end-to-end workflow: Data Acquisition → Data Cleaning → Quantitative Analysis → Visualization → Interactive Dashboard.
4. WRDS academic database compliance with registered user account.

## AI Disclosure
Generative AI is used for auxiliary code structure optimization, document formatting, and logical framework sorting. All financial analysis logic, project framework design, and final verification are completed independently.