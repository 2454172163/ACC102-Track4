import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, LineChart, Line } from 'recharts';

const FinancialChart = ({ data, metric, title }) => {
  const formatTooltip = (value, name) => {
    if (name === 'year') return [value, 'Year'];
    
    // Format values based on metric type
    if (metric === 'var') {
      return [`¥${(value / 10000).toFixed(2)}万`, title];
    }
    return [`${value}%`, title];
  };

  const getBarColor = () => {
    if (metric === 'var') return '#3b82f6'; // VaR uses blue
    return '#60a5fa'; // Default blue
  };

  return (
    <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm">
      <h3 className="text-lg font-bold text-slate-800 mb-6">{title}</h3>
      
      <div className="h-64">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
            <XAxis 
              dataKey="year" 
              stroke="#64748b"
              fontSize={12}
              fontWeight={500}
              label={{ value: 'Year', position: 'insideBottomRight', offset: -5 }}
            />
            <YAxis 
              stroke="#64748b"
              fontSize={12}
              fontWeight={500}
              tickFormatter={(value) => {
                if (metric === 'var') {
                  return `¥${(value / 10000).toFixed(0)}万`;
                }
                return `${value}%`;
              }}
              label={{ value: metric === 'var' ? 'Value (¥万)' : 'Percentage (%)', angle: -90, position: 'insideLeft' }}
            />
            <Tooltip 
              formatter={formatTooltip}
              labelStyle={{ color: '#1e293b', fontWeight: 600 }}
              contentStyle={{ 
                background: 'white',
                border: '1px solid #e2e8f0',
                borderRadius: '8px',
                boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)'
              }}
            />
            <Bar 
              dataKey={metric} 
              fill={getBarColor()}
              radius={[4, 4, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default FinancialChart;
