import { useQuery } from '@tanstack/react-query';

// 模拟家电行业财务数据
const generateFinancialData = (companies, dateRange) => {
  const metrics = [
    { key: 'revenue', label: 'Revenue Growth', unit: '%' },
    { key: 'profit', label: 'Net Profit Margin', unit: '%' },
    { key: 'roe', label: 'ROE', unit: '%' },
    { key: 'debt', label: 'Debt Ratio', unit: '%' },
    { key: 'cashflow', label: 'Free Cash Flow', unit: 'B' },
  ];

  const years = [];
  const currentYear = new Date().getFullYear();
  for (let i = currentYear - 5; i <= currentYear; i++) {
    years.push(i.toString());
  }

  return companies.map(company => ({
    company: company.id,
    data: metrics.map(metric => ({
      ...metric,
      values: years.map(year => ({
        year,
        value: (Math.random() * 20 + 5).toFixed(2),
        change: (Math.random() * 10 - 5).toFixed(2)
      }))
    }))
  }));
};

// 模拟家电行业股价数据
const generateStockData = (companies, dateRange) => {
  const days = 30;
  const data = [];
  
  for (let i = 0; i < days; i++) {
    const date = new Date();
    date.setDate(date.getDate() - (days - i));
    
    const basePrice = 30 + Math.random() * 20; // 家电股价格区间
    data.push({
      date: date.toISOString().split('T')[0],
      price: basePrice.toFixed(2)
    });
  }
  
  return data;
};

// 模拟投资组合数据
const generatePortfolioData = (companies, dateRange) => {
  const months = 12;
  const data = [];
  let baseValue = 1000000; // 初始投资100万
  
  for (let i = 0; i < months; i++) {
    const date = new Date();
    date.setMonth(date.getMonth() - (months - i));
    
    // 模拟投资组合价值增长
    const growth = (Math.random() * 0.05 + 0.01); // 1%-6%的月增长
    baseValue = baseValue * (1 + growth);
    
    data.push({
      date: date.toISOString().slice(0, 7),
      value: Math.round(baseValue)
    });
  }
  
  return data;
};

// 模拟风险数据
const generateRiskData = (companies, dateRange) => {
  const years = [];
  const currentYear = new Date().getFullYear();
  for (let i = currentYear - 5; i <= currentYear; i++) {
    years.push(i.toString());
  }

  return {
    var: years.map(year => ({
      year,
      var: Math.round(Math.random() * 15000 + 35000) // VaR值在3.5万-5万之间
    })),
    riskMatrix: companies.map(company => ({
      company: company.name,
      risk: Math.round(Math.random() * 15 + 15), // 风险15-30%
      return: Math.round(Math.random() * 15 + 10), // 预期收益10-25%
      size: Math.round(Math.random() * 300 + 100) // 气泡大小
    }))
  };
};

export const useFinancialData = (companies, dateRange) => {
  return useQuery({
    queryKey: ['financial-data', companies.map(c => c.id).join(','), dateRange.start.getTime(), dateRange.end.getTime()],
    queryFn: () => generateFinancialData(companies, dateRange),
    enabled: companies.length > 0,
    staleTime: 5 * 60 * 1000,
  });
};

export const useStockData = (companies, dateRange) => {
  return useQuery({
    queryKey: ['stock-data', companies.map(c => c.id).join(','), dateRange.start.getTime(), dateRange.end.getTime()],
    queryFn: () => generateStockData(companies, dateRange),
    enabled: companies.length > 0,
    staleTime: 5 * 60 * 1000,
  });
};

export const usePortfolioData = (companies, dateRange) => {
  return useQuery({
    queryKey: ['portfolio-data', companies.map(c => c.id).join(','), dateRange.start.getTime(), dateRange.end.getTime()],
    queryFn: () => generatePortfolioData(companies, dateRange),
    enabled: companies.length > 0,
    staleTime: 5 * 60 * 1000,
  });
};

export const useRiskData = (companies, dateRange) => {
  return useQuery({
    queryKey: ['risk-data', companies.map(c => c.id).join(','), dateRange.start.getTime(), dateRange.end.getTime()],
    queryFn: () => generateRiskData(companies, dateRange),
    enabled: companies.length > 0,
    staleTime: 5 * 60 * 1000,
  });
};
