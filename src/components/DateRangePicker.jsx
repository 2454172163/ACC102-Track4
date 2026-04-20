import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Calendar, Clock, ChevronDown } from 'lucide-react';
import { format, subDays, subMonths, subYears } from 'date-fns';

const DateRangePicker = ({ dateRange, onDateRangeChange }) => {
  const [isOpen, setIsOpen] = useState(false);

  const presets = [
    { label: 'Last 7 Days', value: { start: subDays(new Date(), 7), end: new Date() } },
    { label: 'Last 30 Days', value: { start: subDays(new Date(), 30), end: new Date() } },
    { label: 'Last 3 Months', value: { start: subMonths(new Date(), 3), end: new Date() } },
    { label: 'Last 6 Months', value: { start: subMonths(new Date(), 6), end: new Date() } },
    { label: 'Last 1 Year', value: { start: subYears(new Date(), 1), end: new Date() } },
    { label: 'Last 2 Years', value: { start: subYears(new Date(), 2), end: new Date() } },
    { label: 'Last 5 Years', value: { start: subYears(new Date(), 5), end: new Date() } },
  ];

  const handlePresetClick = (preset) => {
    onDateRangeChange(preset.value);
    setIsOpen(false);
  };

  const formatDateRange = (range) => {
    if (!range.start || !range.end) return 'Select Date Range';
    return `${format(range.start, 'yyyy-MM-dd')} to ${format(range.end, 'yyyy-MM-dd')}`;
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
          <Calendar className="w-5 h-5 text-slate-500 group-hover:text-slate-600" />
          <span className="text-slate-700">{formatDateRange(dateRange)}</span>
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
            className="absolute top-full left-0 right-0 mt-2 bg-white border border-slate-300 rounded-lg shadow-lg z-50"
          >
            <div className="p-4">
              <div className="flex items-center space-x-2 mb-4">
                <Clock className="w-4 h-4 text-slate-500" />
                <span className="text-sm font-semibold text-slate-700">Quick Select</span>
              </div>
              
              <div className="space-y-1">
                {presets.map((preset, index) => (
                  <motion.button
                    key={index}
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: index * 0.05 }}
                    onClick={() => handlePresetClick(preset)}
                    whileHover={{ x: 5 }}
                    className="w-full px-3 py-2 text-left text-sm text-slate-600 hover:bg-slate-50 rounded-lg transition-all duration-200"
                  >
                    {preset.label}
                  </motion.button>
                ))}
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

export default DateRangePicker;
