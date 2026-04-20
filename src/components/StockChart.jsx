import React from 'react';
import { motion } from 'framer-motion';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Area, AreaChart } from 'recharts';
import { TrendingUp } from 'lucide-react';

const StockChart = ({ data, selectedCompanies }) => {
  const colors = ['#3b82f6', '#60a5fa', '#2563eb', '#1d4ed8', '#1e40af'];

  const formatTooltip = (value, name) => {
    if (name === 'date') return [value, 'Date'];
    return [`¥${value}`, 'Stock Price'];
  };

  return (
    <motion.div 
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
      className="relative bg-white border border-slate-200 rounded-xl p-6 hover:border-slate-300 transition-all duration-300 shadow-sm hover:shadow-md overflow-hidden"
    >
      <div className="relative z-10">
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center space-x-3">
            <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center shadow-sm">
              <TrendingUp className="w-4 h-4 text-white" />
            </div>
            <h3 className="text-lg font-bold text-slate-800">Stock Price Trends</h3>
          </div>
          <div className="flex items-center space-x-4">
            {selectedCompanies.map((company, index) => (
              <motion.div 
                key={company.id} 
                className="flex items-center space-x-2"
                whileHover={{ scale: 1.05 }}
              >
                <div 
                  className="w-3 h-3 rounded-full"
                  style={{ backgroundColor: colors[index % colors.length] }}
                ></div>
                <span className="text-sm font-medium text-slate-600">{company.id}</span>
              </motion.div>
            ))}
          </div>
        </div>
        
        <div className="h-80">
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={data}>
              <defs>
                <linearGradient id="colorGradient" x1="0" y1="0" x2="0" y2="1">
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
                label={{ value: 'Month', position: 'insideBottomRight', offset: -5 }}
              />
              <YAxis 
                stroke="#64748b"
                fontSize={12}
                fontWeight={500}
                tickFormatter={(value) => `¥${value}`}
                label={{ value: 'Stock Price (CNY)', angle: -90, position: 'insideLeft' }}
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
                dataKey="price"
                stroke="#3b82f6"
                strokeWidth={2}
                fill="url(#colorGradient)"
              />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>
    </motion.div>
  );
};

export default StockChart;
