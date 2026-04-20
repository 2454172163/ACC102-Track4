import React from 'react';
import { motion } from 'framer-motion';
import { TrendingUp, BarChart3, PieChart, Activity } from 'lucide-react';

const AnalysisTabs = ({ activeTab, onTabChange }) => {
  const tabs = [
    { id: 'financial', label: 'Financial Metrics', icon: BarChart3, color: 'bg-blue-600' },
    { id: 'stock', label: 'Stock Trends', icon: TrendingUp, color: 'bg-blue-600' },
    { id: 'portfolio', label: 'Portfolio Analysis', icon: PieChart, color: 'bg-blue-600' },
    { id: 'risk', label: 'Risk Assessment', icon: Activity, color: 'bg-blue-600' },
  ];

  return (
    <div className="bg-white border border-slate-200 rounded-lg p-2 shadow-sm">
      <div className="flex flex-col space-y-2">
        {tabs.map((tab) => {
          const Icon = tab.icon;
          const isActive = activeTab === tab.id;
          
          return (
            <motion.button
              key={tab.id}
              onClick={() => onTabChange(tab.id)}
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              className={`relative flex items-center space-x-3 px-4 py-3 rounded-lg transition-all duration-300 overflow-hidden ${
                isActive
                  ? `${tab.color} text-white shadow-md`
                  : 'text-slate-600 hover:text-slate-800 hover:bg-slate-100'
              }`}
            >
              {isActive && (
                <motion.div
                  layoutId="activeTab"
                  className={`absolute inset-0 ${tab.color} opacity-20`}
                  initial={false}
                  transition={{ type: "spring", stiffness: 500, damping: 30 }}
                />
              )}
              
              <div className="relative z-10 flex items-center space-x-3">
                <Icon className="w-4 h-4" />
                <span className="text-sm font-medium">{tab.label}</span>
              </div>
            </motion.button>
          );
        })}
      </div>
    </div>
  );
};

export default AnalysisTabs;
