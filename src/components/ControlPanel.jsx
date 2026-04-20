import React from 'react';
import { motion } from 'framer-motion';
import CompanySelector from './CompanySelector.jsx';
import DateRangePicker from './DateRangePicker.jsx';
import AnalysisTabs from './AnalysisTabs.jsx';
import { Sliders } from 'lucide-react';

const ControlPanel = ({ 
  selectedCompanies, 
  onCompanyChange,
  dateRange,
  onDateRangeChange,
  activeTab,
  onTabChange
}) => {
  return (
    <motion.div 
      initial={{ x: -300, opacity: 0 }}
      animate={{ x: 0, opacity: 1 }}
      transition={{ duration: 0.6, delay: 0.2 }}
      className="w-80 bg-white border-r border-slate-200 p-6 space-y-6 shadow-sm"
    >
      <div className="relative z-10">
        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.4 }}
          className="flex items-center space-x-3 mb-6"
        >
          <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center shadow-sm">
            <Sliders className="w-4 h-4 text-white" />
          </div>
          <h2 className="text-xl font-bold text-slate-800">Control Panel</h2>
        </motion.div>
        
        <div className="space-y-6">
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.5 }}
          >
            <label className="block text-sm font-semibold text-slate-700 mb-3">
              Select Companies
            </label>
            <CompanySelector 
              selectedCompanies={selectedCompanies}
              onCompanyChange={onCompanyChange}
            />
          </motion.div>
          
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.6 }}
          >
            <label className="block text-sm font-semibold text-slate-700 mb-3">
              Date Range
            </label>
            <DateRangePicker 
              dateRange={dateRange}
              onDateRangeChange={onDateRangeChange}
            />
          </motion.div>
          
          <motion.div
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.7 }}
          >
            <label className="block text-sm font-semibold text-slate-700 mb-3">
              Analysis Dimension
            </label>
            <AnalysisTabs 
              activeTab={activeTab}
              onTabChange={onTabChange}
            />
          </motion.div>
        </div>
      </div>
    </motion.div>
  );
};

export default ControlPanel;
