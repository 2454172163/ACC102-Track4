import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Settings, Bell, User, X, LogOut, UserCircle, Settings2 } from 'lucide-react';

const Header = () => {
  const [showNotifications, setShowNotifications] = useState(false);
  const [showUserMenu, setShowUserMenu] = useState(false);
  const [showSettingsMenu, setShowSettingsMenu] = useState(false);

  const toggleNotifications = () => {
    setShowNotifications(!showNotifications);
    // 关闭其他菜单
    setShowUserMenu(false);
    setShowSettingsMenu(false);
  };

  const toggleUserMenu = () => {
    setShowUserMenu(!showUserMenu);
    // 关闭其他菜单
    setShowNotifications(false);
    setShowSettingsMenu(false);
  };

  const toggleSettingsMenu = () => {
    setShowSettingsMenu(!showSettingsMenu);
    // 关闭其他菜单
    setShowNotifications(false);
    setShowUserMenu(false);
  };

  const closeAllMenus = () => {
    setShowNotifications(false);
    setShowUserMenu(false);
    setShowSettingsMenu(false);
  };

  return (
    <motion.header 
      initial={{ y: -100, opacity: 0 }}
      animate={{ y: 0, opacity: 1 }}
      transition={{ duration: 0.6, ease: "easeOut" }}
      className="relative bg-white border-b border-slate-200 sticky top-0 z-50 shadow-sm"
    >
      <div className="max-w-7xl mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          <motion.div 
            className="flex items-center space-x-3"
            whileHover={{ scale: 1.02 }}
            transition={{ type: "spring", stiffness: 400, damping: 10 }}
          >
            <div className="relative">
              <div className="w-10 h-10 bg-blue-600 rounded-lg flex items-center justify-center shadow-md">
                <div className="w-6 h-6 bg-white rounded-md flex items-center justify-center">
                  <div className="w-3 h-3 bg-blue-600 rounded-sm"></div>
                </div>
              </div>
            </div>
            <div>
              <h1 className="text-2xl font-bold text-slate-800">Financial Analytics Platform</h1>
              <p className="text-sm text-slate-500">AI-Powered Investment Decision System</p>
            </div>
          </motion.div>
          
          <div className="flex items-center space-x-4">
            <div className="relative">
              <motion.button
                onClick={toggleNotifications}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="relative p-3 rounded-lg hover:bg-slate-100 transition-all duration-300 group"
                title="Notifications"
              >
                <Bell className="w-5 h-5 text-slate-500 group-hover:text-slate-700" />
                {showNotifications && (
                  <span className="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full"></span>
                )}
              </motion.button>

              <AnimatePresence>
                {showNotifications && (
                  <motion.div
                    initial={{ opacity: 0, y: -10, scale: 0.95 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    exit={{ opacity: 0, y: -10, scale: 0.95 }}
                    transition={{ duration: 0.2 }}
                    className="absolute right-0 top-full mt-2 w-80 bg-white border border-slate-200 rounded-lg shadow-lg z-50 overflow-hidden"
                  >
                    <div className="p-4 border-b border-slate-200 flex justify-between items-center">
                      <h3 className="font-semibold text-slate-800">Notifications</h3>
                      <button 
                        onClick={closeAllMenus}
                        className="text-slate-400 hover:text-slate-600"
                      >
                        <X className="w-4 h-4" />
                      </button>
                    </div>
                    <div className="p-4">
                      <div className="space-y-3">
                        <div className="p-3 bg-blue-50 rounded-lg">
                          <p className="text-sm font-medium text-slate-800">Market Alert</p>
                          <p className="text-xs text-slate-600 mt-1">Gree Electric stock price increased by 5%</p>
                          <p className="text-xs text-slate-500 mt-2">2 hours ago</p>
                        </div>
                        <div className="p-3 bg-amber-50 rounded-lg">
                          <p className="text-sm font-medium text-slate-800">Risk Warning</p>
                          <p className="text-xs text-slate-600 mt-1">Portfolio volatility exceeds threshold</p>
                          <p className="text-xs text-slate-500 mt-2">5 hours ago</p>
                        </div>
                        <div className="p-3 bg-emerald-50 rounded-lg">
                          <p className="text-sm font-medium text-slate-800">Analysis Complete</p>
                          <p className="text-xs text-slate-600 mt-1">Quarterly financial report analysis finished</p>
                          <p className="text-xs text-slate-500 mt-2">1 day ago</p>
                        </div>
                      </div>
                      <button className="w-full mt-4 text-sm text-blue-600 hover:text-blue-800 font-medium">
                        View All Notifications
                      </button>
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
            
            <div className="relative">
              <motion.button
                onClick={toggleSettingsMenu}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="relative p-3 rounded-lg hover:bg-slate-100 transition-all duration-300 group"
                title="Settings"
              >
                <Settings className="w-5 h-5 text-slate-500 group-hover:text-slate-700" />
              </motion.button>

              <AnimatePresence>
                {showSettingsMenu && (
                  <motion.div
                    initial={{ opacity: 0, y: -10, scale: 0.95 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    exit={{ opacity: 0, y: -10, scale: 0.95 }}
                    transition={{ duration: 0.2 }}
                    className="absolute right-0 top-full mt-2 w-48 bg-white border border-slate-200 rounded-lg shadow-lg z-50 overflow-hidden"
                  >
                    <div className="p-2">
                      <button className="w-full flex items-center space-x-2 px-3 py-2 text-sm text-slate-700 hover:bg-slate-100 rounded-md transition-colors">
                        <Settings2 className="w-4 h-4" />
                        <span>Preferences</span>
                      </button>
                      <button className="w-full flex items-center space-x-2 px-3 py-2 text-sm text-slate-700 hover:bg-slate-100 rounded-md transition-colors">
                        <Settings2 className="w-4 h-4" />
                        <span>Account Settings</span>
                      </button>
                      <hr className="my-1 border-slate-200" />
                      <button className="w-full flex items-center space-x-2 px-3 py-2 text-sm text-slate-700 hover:bg-slate-100 rounded-md transition-colors">
                        <Settings2 className="w-4 h-4" />
                        <span>Help & Support</span>
                      </button>
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
            
            <div className="relative">
              <motion.button
                onClick={toggleUserMenu}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="relative p-3 rounded-lg hover:bg-slate-100 transition-all duration-300 group"
                title="User Profile"
              >
                <User className="w-5 h-5 text-slate-500 group-hover:text-slate-700" />
              </motion.button>

              <AnimatePresence>
                {showUserMenu && (
                  <motion.div
                    initial={{ opacity: 0, y: -10, scale: 0.95 }}
                    animate={{ opacity: 1, y: 0, scale: 1 }}
                    exit={{ opacity: 0, y: -10, scale: 0.95 }}
                    transition={{ duration: 0.2 }}
                    className="absolute right-0 top-full mt-2 w-48 bg-white border border-slate-200 rounded-lg shadow-lg z-50 overflow-hidden"
                  >
                    <div className="p-2">
                      <div className="px-3 py-2 text-sm font-medium text-slate-800 border-b border-slate-200 mb-1">
                        User Account
                      </div>
                      <button className="w-full flex items-center space-x-2 px-3 py-2 text-sm text-slate-700 hover:bg-slate-100 rounded-md transition-colors">
                        <UserCircle className="w-4 h-4" />
                        <span>Profile</span>
                      </button>
                      <button className="w-full flex items-center space-x-2 px-3 py-2 text-sm text-slate-700 hover:bg-slate-100 rounded-md transition-colors">
                        <Settings2 className="w-4 h-4" />
                        <span>Settings</span>
                      </button>
                      <hr className="my-1 border-slate-200" />
                      <button className="w-full flex items-center space-x-2 px-3 py-2 text-sm text-red-600 hover:bg-red-50 rounded-md transition-colors">
                        <LogOut className="w-4 h-4" />
                        <span>Sign Out</span>
                      </button>
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          </div>
        </div>
      </div>
    </motion.header>
  );
};

export default Header;
