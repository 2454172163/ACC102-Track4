import React from 'react';
import { motion } from 'framer-motion';
import { TrendingUp, TrendingDown, Minus } from 'lucide-react';

const FinancialMetricCard = ({ title, value, change, unit, trend, icon }) => {
  const getTrendIcon = () => {
    if (trend === 'up') return <TrendingUp className="w-4 h-4 text-emerald-500" />;
    if (trend === 'down') return <TrendingDown className="w-4 h-4 text-red-500" />;
    return <Minus className="w-4 h-4 text-slate-400" />;
  };

  const getTrendColor = () => {
    if (trend === 'up') return 'text-emerald-500';
    if (trend === 'down') return 'text-red-500';
    return 'text-slate-400';
  };

  const formatValue = (val) => {
    if (typeof val === 'string' && val.includes('¥')) {
      return val;
    }
    if (typeof val === 'number' && val >= 10000) {
      return `¥${(val / 10000).toFixed(2)}万`;
    }
    return val;
  };

  return (
    <motion.div
      whileHover={{ scale: 1.02, y: -2 }}
      whileTap={{ scale: 0.98 }}
      className="relative bg-white border border-slate-200 rounded-xl p-6 hover:border-slate-300 transition-all duration-300 group shadow-sm hover:shadow-md overflow-hidden"
    >
      <div className="relative z-10">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center space-x-2">
            <div className="p-2 bg-blue-100 rounded-lg text-blue-600">
              {icon}
            </div>
            <h3 className="text-sm font-semibold text-slate-700 group-hover:text-slate-800 transition-colors duration-300">
              {title}
            </h3>
          </div>
          <div className="flex items-center space-x-1">
            {getTrendIcon()}
          </div>
        </div>
        
        <div className="space-y-2">
          <motion.div 
            className="text-2xl font-bold text-slate-900 group-hover:text-slate-800 transition-colors duration-300"
            whileHover={{ scale: 1.05 }}
          >
            {formatValue(value)}
            {unit && !value.includes(unit) && <span className="text-lg text-slate-500 ml-1">{unit}</span>}
          </motion.div>
          
          {change && (
            <motion.div 
              className={`text-sm font-semibold ${getTrendColor()} flex items-center space-x-1`}
              whileHover={{ scale: 1.05 }}
            >
              <span>{change}</span>
            </motion.div>
          )}
        </div>
      </div>
    </motion.div>
  );
};

export default FinancialMetricCard;
