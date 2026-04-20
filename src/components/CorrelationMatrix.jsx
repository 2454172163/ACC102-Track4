import React from 'react';

const CorrelationMatrix = ({ companies, data }) => {
  const getColor = (value) => {
    // Map correlation values to blue color scale
    const intensity = Math.abs(value);
    if (value > 0) {
      // Positive correlation - blue scale
      return `rgba(59, 130, 246, ${intensity})`;
    } else {
      // Negative correlation - red scale
      return `rgba(239, 68, 68, ${intensity})`;
    }
  };

  const formatValue = (value) => {
    return value.toFixed(2);
  };

  return (
    <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm">
      <h3 className="text-lg font-bold text-slate-800 mb-6">Stock Correlation Matrix</h3>
      
      <div className="overflow-x-auto">
        <table className="w-full">
          <thead>
            <tr>
              <th className="text-left p-2 text-sm font-semibold text-slate-700"></th>
              {companies.map((company, index) => (
                <th key={index} className="text-center p-2 text-sm font-semibold text-slate-700 min-w-[80px]">
                  {company.name}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((row, rowIndex) => (
              <tr key={rowIndex}>
                <td className="p-2 text-sm font-semibold text-slate-800">
                  {companies[rowIndex]?.name || `Stock${rowIndex + 1}`}
                </td>
                {row.map((value, colIndex) => (
                  <td 
                    key={colIndex}
                    className="p-2 text-center text-sm font-semibold"
                    style={{ 
                      backgroundColor: getColor(value),
                      color: Math.abs(value) > 0.5 ? 'white' : '#1e293b'
                    }}
                  >
                    {formatValue(value)}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      
      <div className="mt-4 flex items-center justify-between text-sm text-slate-600">
        <div className="flex items-center space-x-2">
          <div className="w-4 h-4 bg-red-500 rounded"></div>
          <span className="font-medium">Negative Correlation</span>
        </div>
        <div className="flex items-center space-x-2">
          <div className="w-4 h-4 bg-blue-500 rounded"></div>
          <span className="font-medium">Positive Correlation</span>
        </div>
      </div>
    </div>
  );
};

export default CorrelationMatrix;
