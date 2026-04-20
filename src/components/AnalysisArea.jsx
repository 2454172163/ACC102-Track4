import React from 'react';
import { motion } from 'framer-motion';
import FinancialMetricCard from './FinancialMetricCard.jsx';
import FinancialChart from './FinancialChart.jsx';
import StockChart from './StockChart.jsx';
import PortfolioChart from './PortfolioChart.jsx';
import RiskMatrixChart from './RiskMatrixChart.jsx';
import CorrelationMatrix from './CorrelationMatrix.jsx';
import { useFinancialData, useStockData, usePortfolioData, useRiskData } from '../hooks/useFinancialData.js';
import { Loader2, TrendingUp, Download } from 'lucide-react';

const AnalysisArea = ({ selectedCompanies, dateRange, activeTab }) => {
  const { data: financialData, isLoading: financialLoading } = useFinancialData(selectedCompanies, dateRange);
  const { data: stockData, isLoading: stockLoading } = useStockData(selectedCompanies, dateRange);
  const { data: portfolioData, isLoading: portfolioLoading } = usePortfolioData(selectedCompanies, dateRange);
  const { data: riskData, isLoading: riskLoading } = useRiskData(selectedCompanies, dateRange);

  const handleExportCSV = () => {
    // Create CSV content based on active tab
    let csvContent = "";
    let filename = "";
    
    switch (activeTab) {
      case 'financial':
        // Financial metrics CSV
        csvContent = "Metric,Value,Change,Unit,Trend\n";
        csvContent += "Revenue Growth,12.8,+1.5,%,up\n";
        csvContent += "Net Profit Margin,8.5,+0.8,%,up\n";
        csvContent += "Gross Margin,28.3,-0.5,%,down\n";
        csvContent += "ROE,15.2,+1.2,%,up\n";
        filename = "financial_metrics.csv";
        break;
        
      case 'stock':
        // Stock data CSV
        if (stockData && stockData.length > 0) {
          csvContent = "Date,Price\n";
          stockData.forEach(item => {
            csvContent += `${item.date},${item.price}\n`;
          });
        } else {
          csvContent = "Date,Price\n2023-01-01,35.2\n2023-01-02,36.1\n2023-01-03,34.8\n";
        }
        filename = "stock_data.csv";
        break;
        
      case 'portfolio':
        // Portfolio data CSV
        csvContent = "Date,Value\n";
        csvContent += "2023-01,1000000\n2023-02,1020000\n2023-03,1050000\n2023-04,1030000\n2023-05,1080000\n";
        filename = "portfolio_data.csv";
        break;
        
      case 'risk':
        // Risk data CSV
        csvContent = "Metric,Value,Change,Trend\n";
        csvContent += "VaR (95%),45000,-5000,down\n";
        csvContent += "Volatility,18.5,+2.1,up\n";
        csvContent += "Beta Coefficient,1.12,+0.05,up\n";
        csvContent += "Downside Risk,12.3,-1.2,down\n";
        filename = "risk_metrics.csv";
        break;
        
      default:
        csvContent = "No data available for export";
        filename = "export.csv";
    }
    
    // Create and download the CSV file
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    
    if (link.download !== undefined) {
      link.setAttribute('href', url);
      link.setAttribute('download', filename);
      link.style.visibility = 'hidden';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
    
    URL.revokeObjectURL(url);
  };

  if (selectedCompanies.length === 0) {
    return (
      <motion.div 
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.6 }}
        className="flex-1 flex items-center justify-center relative"
      >
        <div className="text-center bg-white border border-slate-200 rounded-2xl p-12 shadow-sm">
          <motion.div 
            className="w-20 h-20 bg-blue-600 rounded-full flex items-center justify-center mx-auto mb-6 shadow-md"
            animate={{ rotate: 360 }}
            transition={{ duration: 20, repeat: Infinity, ease: "linear" }}
          >
            <TrendingUp className="w-10 h-10 text-white" />
          </motion.div>
          <h3 className="text-2xl font-bold text-slate-800 mb-4">Start Financial Analysis</h3>
          <p className="text-slate-600 text-lg">Please select companies from the control panel to begin analysis</p>
          <motion.div 
            className="mt-6 flex justify-center"
            animate={{ y: [0, -10, 0] }}
            transition={{ duration: 2, repeat: Infinity }}
          >
            <div className="w-2 h-2 bg-blue-600 rounded-full"></div>
          </motion.div>
        </div>
      </motion.div>
    );
  }

  const renderContent = () => {
    switch (activeTab) {
      case 'financial':
        return (
          <div className="space-y-8">
            {financialLoading ? (
              <div className="flex items-center justify-center py-12">
                <Loader2 className="w-8 h-8 animate-spin text-blue-600" />
              </div>
            ) : (
              <>
                <motion.div 
                  className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, staggerChildren: 0.1 }}
                >
                  <FinancialMetricCard 
                    title="Revenue Growth" 
                    value="12.8" 
                    change="+1.5%" 
                    unit="%" 
                    trend="up"
                    icon={<TrendingUp className="w-5 h-5" />}
                  />
                  <FinancialMetricCard 
                    title="Net Profit Margin" 
                    value="8.5" 
                    change="+0.8%" 
                    unit="%" 
                    trend="up"
                    icon={<TrendingUp className="w-5 h-5" />}
                  />
                  <FinancialMetricCard 
                    title="Gross Margin" 
                    value="28.3" 
                    change="-0.5%" 
                    unit="%" 
                    trend="down"
                    icon={<TrendingUp className="w-5 h-5" />}
                  />
                  <FinancialMetricCard 
                    title="ROE" 
                    value="15.2" 
                    change="+1.2%" 
                    unit="%" 
                    trend="up"
                    icon={<TrendingUp className="w-5 h-5" />}
                  />
                </motion.div>
                
                <motion.div 
                  className="grid grid-cols-1 lg:grid-cols-2 gap-8"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, delay: 0.2 }}
                >
                  <FinancialChart 
                    data={[
                      { year: '2019', revenue: 10.2 },
                      { year: '2020', revenue: 11.5 },
                      { year: '2021', revenue: 13.8 },
                      { year: '2022', revenue: 12.1 },
                      { year: '2023', revenue: 14.5 },
                      { year: '2024', revenue: 12.8 },
                    ]}
                    metric="revenue"
                    title="Revenue Growth Trend"
                  />
                  <FinancialChart 
                    data={[
                      { year: '2019', profit: 7.2 },
                      { year: '2020', profit: 7.8 },
                      { year: '2021', profit: 9.1 },
                      { year: '2022', profit: 8.3 },
                      { year: '2023', profit: 9.7 },
                      { year: '2024', profit: 8.5 },
                    ]}
                    metric="profit"
                    title="Net Profit Margin Trend"
                  />
                </motion.div>
              </>
            )}
          </div>
        );
      
      case 'stock':
        return (
          <div className="space-y-8">
            {stockLoading ? (
              <div className="flex items-center justify-center py-12">
                <Loader2 className="w-8 h-8 animate-spin text-blue-600" />
              </div>
            ) : (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6 }}
              >
                <StockChart 
                  data={stockData || []}
                  selectedCompanies={selectedCompanies}
                />
              </motion.div>
            )}
          </div>
        );
      
      case 'portfolio':
        return (
          <div className="space-y-8">
            {portfolioLoading ? (
              <div className="flex items-center justify-center py-12">
                <Loader2 className="w-8 h-8 animate-spin text-blue-600" />
              </div>
            ) : (
              <>
                <motion.div 
                  className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, staggerChildren: 0.1 }}
                >
                  <FinancialMetricCard 
                    title="Portfolio Value" 
                    value="¥1,250,000" 
                    change="+5.2%" 
                    trend="up"
                    icon={<TrendingUp className="w-5 h-5" />}
                  />
                  <FinancialMetricCard 
                    title="Annualized Return" 
                    value="12.8%" 
                    change="+1.5%" 
                    trend="up"
                    icon={<TrendingUp className="w-5 h-5" />}
                  />
                  <FinancialMetricCard 
                    title="Max Drawdown" 
                    value="-8.3%" 
                    change="-2.1%" 
                    trend="down"
                    icon={<TrendingUp className="w-5 h-5" />}
                  />
                  <FinancialMetricCard 
                    title="Sharpe Ratio" 
                    value="1.45" 
                    change="+0.2" 
                    trend="up"
                    icon={<TrendingUp className="w-5 h-5" />}
                  />
                </motion.div>
                
                <motion.div 
                  className="grid grid-cols-1 lg:grid-cols-2 gap-8"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, delay: 0.2 }}
                >
                  <PortfolioChart 
                    data={portfolioData || [
                      { date: '2023-01', value: 1000000 },
                      { date: '2023-02', value: 1020000 },
                      { date: '2023-03', value: 1050000 },
                      { date: '2023-04', value: 1030000 },
                      { date: '2023-05', value: 1080000 },
                      { date: '2023-06', value: 1120000 },
                      { date: '2023-07', value: 1150000 },
                      { date: '2023-08', value: 1180000 },
                      { date: '2023-09', value: 1200000 },
                      { date: '2023-10', value: 1220000 },
                      { date: '2023-11', value: 1240000 },
                      { date: '2023-12', value: 1250000 },
                    ]}
                    title="Portfolio Value Trend"
                  />
                  
                  <CorrelationMatrix 
                    companies={selectedCompanies}
                    data={[
                      [1.0, 0.75, 0.68, 0.45, 0.32],
                      [0.75, 1.0, 0.82, 0.51, 0.38],
                      [0.68, 0.82, 1.0, 0.47, 0.41],
                      [0.45, 0.51, 0.47, 1.0, 0.65],
                      [0.32, 0.38, 0.41, 0.65, 1.0],
                    ]}
                  />
                </motion.div>
              </>
            )}
          </div>
        );
      
      case 'risk':
        return (
          <div className="space-y-8">
            {riskLoading ? (
              <div className="flex items-center justify-center py-12">
                <Loader2 className="w-8 h-8 animate-spin text-blue-600" />
              </div>
            ) : (
              <>
                <motion.div 
                  className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, staggerChildren: 0.1 }}
                >
                  <FinancialMetricCard 
                    title="VaR (95%)" 
                    value="¥45,000" 
                    change="-¥5,000" 
                    trend="down"
                    icon={<TrendingUp className="w-5 h-5" />}
                  />
                  <FinancialMetricCard 
                    title="Volatility" 
                    value="18.5%" 
                    change="+2.1%" 
                    trend="up"
                    icon={<TrendingUp className="w-5 h-5" />}
                  />
                  <FinancialMetricCard 
                    title="Beta Coefficient" 
                    value="1.12" 
                    change="+0.05" 
                    trend="up"
                    icon={<TrendingUp className="w-5 h-5" />}
                  />
                  <FinancialMetricCard 
                    title="Downside Risk" 
                    value="12.3%" 
                    change="-1.2%" 
                    trend="down"
                    icon={<TrendingUp className="w-5 h-5" />}
                  />
                </motion.div>
                
                <motion.div 
                  className="grid grid-cols-1 lg:grid-cols-2 gap-8"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, delay: 0.2 }}
                >
                  <RiskMatrixChart 
                    data={riskData?.riskMatrix || [
                      { company: 'Gree Electric', risk: 15, return: 12, size: 200 },
                      { company: 'Midea Group', risk: 18, return: 15, size: 400 },
                      { company: 'Haier Smart Home', risk: 20, return: 18, size: 250 },
                      { company: 'Supor', risk: 25, return: 22, size: 150 },
                      { company: 'Robam Appliance', risk: 28, return: 25, size: 120 },
                    ]}
                  />
                  
                  <FinancialChart 
                    data={riskData?.var || [
                      { year: '2019', var: 35000 },
                      { year: '2020', var: 42000 },
                      { year: '2021', var: 38000 },
                      { year: '2022', var: 48000 },
                      { year: '2023', var: 45000 },
                      { year: '2024', var: 45000 },
                    ]}
                    metric="var"
                    title="VaR Risk Value Trend"
                  />
                </motion.div>
              </>
            )}
          </div>
        );
      
      default:
        return null;
    }
  };

  return (
    <motion.div 
      className="flex-1 p-6 relative"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.6, delay: 0.3 }}
    >
      <div className="max-w-7xl mx-auto">
        <motion.div 
          className="mb-8 flex justify-between items-center"
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, delay: 0.4 }}
        >
          <div>
            <h2 className="text-3xl font-bold text-slate-800 mb-2">
              {activeTab === 'financial' && 'Core Financial Metrics'}
              {activeTab === 'stock' && 'Stock Price Trends'}
              {activeTab === 'portfolio' && 'Portfolio Analysis'}
              {activeTab === 'risk' && 'Risk Assessment'}
            </h2>
            <p className="text-slate-600 text-lg">
              Analyzing {selectedCompanies.map(c => c.name).join(', ')}
            </p>
          </div>
          
          <motion.button
            onClick={handleExportCSV}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="flex items-center space-x-2 bg-blue-600 text-white px-4 py-2 rounded-lg shadow-md hover:bg-blue-700 transition-colors"
          >
            <Download className="w-4 h-4" />
            <span>Export CSV</span>
          </motion.button>
        </motion.div>
        
        {renderContent()}
      </div>
    </motion.div>
  );
};

export default AnalysisArea;
