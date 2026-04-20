import React, { useState } from 'react';
import { motion } from 'framer-motion';
import Header from '../components/Header.jsx';
import ControlPanel from '../components/ControlPanel.jsx';
import AnalysisArea from '../components/AnalysisArea.jsx';

const Index = () => {
  const [selectedCompanies, setSelectedCompanies] = useState([]);
  const [dateRange, setDateRange] = useState({
    start: new Date(new Date().setFullYear(new Date().getFullYear() - 1)),
    end: new Date()
  });
  const [activeTab, setActiveTab] = useState('financial');

  return (
    <div className="min-h-screen bg-slate-50 relative overflow-hidden">
      <div className="relative z-10">
        <Header />
        
        <motion.div 
          className="flex"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.6 }}
        >
          <ControlPanel 
            selectedCompanies={selectedCompanies}
            onCompanyChange={setSelectedCompanies}
            dateRange={dateRange}
            onDateRangeChange={setDateRange}
            activeTab={activeTab}
            onTabChange={setActiveTab}
          />
          
          <AnalysisArea 
            selectedCompanies={selectedCompanies}
            dateRange={dateRange}
            activeTab={activeTab}
          />
        </motion.div>
      </div>
    </div>
  );
};

export default Index;
