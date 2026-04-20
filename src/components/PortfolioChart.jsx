import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Area, AreaChart } from 'recharts';

const PortfolioChart = ({ data, title }) => {
  const formatTooltip = (value, name) => {
    if (name === 'date') return [value, 'Date'];
    return [`¥${(value / 10000).toFixed(2)}万`, 'Portfolio Value'];
  };

  const formatYAxis = (value) => {
    return `¥${(value / 10000).toFixed(0)}万`;
  };

  return (
    <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm">
      <h3 className="text-lg font-bold text-slate-800 mb-6">{title}</h3>
      
      <div className="h-80">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={data}>
            <defs>
              <linearGradient id="portfolioGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3}/>
                <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
            <XAxis 
              dataKey="date" 
              stroke="#64748b"
              fontSize={12}
              fontWeight={500}
              tickFormatter={(value) => value.slice(5)}
              label={{ value: 'Month', position: 'insideBottomRight', offset: -5 }}
            />
            <YAxis 
              stroke="#64748b"
              fontSize={12}
              fontWeight={500}
              tickFormatter={formatYAxis}
              label={{ value: 'Portfolio Value (¥万)', angle: -90, position: 'insideLeft' }}
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
            <Area
              type="monotone"
              dataKey="value"
              stroke="#3b82f6"
              strokeWidth={2}
              fill="url(#portfolioGradient)"
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default PortfolioChart;
