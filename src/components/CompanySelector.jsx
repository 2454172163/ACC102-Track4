import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, ChevronDown, Building2 } from 'lucide-react';

const CompanySelector = ({ selectedCompanies, onCompanyChange }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');

  const companies = [
    { id: '000651', name: 'Gree Electric', sector: 'Home Appliances', marketCap: '200B' },
    { id: '000333', name: 'Midea Group', sector: 'Home Appliances', marketCap: '400B' },
    { id: '600690', name: 'Haier Smart Home', sector: 'Home Appliances', marketCap: '250B' },
    { id: '002032', name: 'Supor', sector: 'Kitchen Appliances', marketCap: '30B' },
    { id: '002508', name: 'Robam Appliance', sector: 'Kitchen Appliances', marketCap: '25B' },
    { id: '002465', name: 'Hytera Communications', sector: 'Telecom Equipment', marketCap: '15B' },
    { id: '603868', name: 'Flyco Appliance', sector: 'Personal Care', marketCap: '18B' },
    { id: '002705', name: 'Xinbao Appliance', sector: 'Small Appliances', marketCap: '12B' },
  ];

  const filteredCompanies = companies.filter(company =>
    company.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    company.id.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const toggleCompany = (company) => {
    const isSelected = selectedCompanies.some(c => c.id === company.id);
    if (isSelected) {
      onCompanyChange(selectedCompanies.filter(c => c.id !== company.id));
    } else {
      onCompanyChange([...selectedCompanies, company]);
    }
  };

  return (
    <div className="relative">
      <motion.button
        onClick={() => setIsOpen(!isOpen)}
        whileHover={{ scale: 1.02 }}
        whileTap={{ scale: 0.98 }}
        className="w-full bg-white border border-slate-300 rounded-lg px-4 py-3 flex items-center justify-between hover:border-slate-400 transition-all duration-300 group shadow-sm"
      >
        <div className="flex items-center space-x-3">
          <Building2 className="w-5 h-5 text-slate-500 group-hover:text-slate-600" />
          <span className="text-slate-700">
            {selectedCompanies.length > 0 
              ? `${selectedCompanies.length} Company${selectedCompanies.length > 1 ? 'ies' : ''} Selected`
              : 'Select Companies'
            }
          </span>
        </div>
        <ChevronDown className={`w-5 h-5 text-slate-500 transition-transform duration-300 ${isOpen ? 'rotate-180' : ''}`} />
      </motion.button>

      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ opacity: 0, y: -10, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -10, scale: 0.95 }}
            transition={{ duration: 0.2 }}
            className="absolute top-full left-0 right-0 mt-2 bg-white border border-slate-300 rounded-lg shadow-lg z-50 overflow-hidden"
          >
            <div className="p-4 border-b border-slate-200">
              <div className="relative">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-slate-400" />
                <input
                  type="text"
                  placeholder="Search companies..."
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                  className="w-full pl-10 pr-4 py-2 bg-slate-50 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-slate-700 placeholder-slate-400"
                />
              </div>
            </div>
            
            <div className="max-h-64 overflow-y-auto">
              {filteredCompanies.map((company, index) => {
                const isSelected = selectedCompanies.some(c => c.id === company.id);
                return (
                  <motion.button
                    key={company.id}
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: index * 0.05 }}
                    onClick={() => toggleCompany(company)}
                    whileHover={{ x: 5 }}
                    className={`w-full px-4 py-3 text-left hover:bg-slate-50 transition-all duration-200 flex items-center justify-between ${
                      isSelected ? 'bg-blue-50 text-blue-800' : 'text-slate-600'
                    }`}
                  >
                    <div>
                      <div className="font-medium">{company.name}</div>
                      <div className="text-sm text-slate-500">{company.id} • {company.sector} • {company.marketCap}</div>
                    </div>
                    {isSelected && (
                      <div className="w-2 h-2 bg-blue-600 rounded-full"></div>
                    )}
                  </motion.button>
                );
              })}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default CompanySelector;
