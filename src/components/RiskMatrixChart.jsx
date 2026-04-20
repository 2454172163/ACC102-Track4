import React from 'react';
import { ScatterChart, Scatter, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts';

const RiskMatrixChart = ({ data }) => {
  const colors = ['#3b82f6', '#60a5fa', '#2563eb', '#1d4ed8', '#1e40af'];

  const formatTooltip = (value, name, props) => {
    if (name === 'risk') return [`${value}%`, 'Risk'];
    if (name === 'return') return [`${value}%`, 'Expected Return'];
    return [props.payload.company, 'Company'];
  };

  return (
    <div className="bg-white border border-slate-200 rounded-xl p-6 shadow-sm">
      <h3 className="text-lg font-bold text-slate-800 mb-6">Risk-Return Matrix</h3>
      
      <div className="h-80">
        <ResponsiveContainer width="100%" height="100%">
          <ScatterChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#e2e8f0" />
            <XAxis 
              type="number"
              dataKey="risk"
              name="Risk"
              unit="%"
              stroke="#64748b"
              fontSize={12}
              fontWeight={500}
              domain={[0, 35]}
              label={{ value: 'Risk (%)', position: 'insideBottomRight', offset: -5 }}
            />
            <YAxis 
              type="number"
              dataKey="return"
              name="Expected Return"
              unit="%"
              stroke="#64748b"
              fontSize={12}
              fontWeight={500}
              domain={[0, 30]}
              label={{ value: 'Expected Return (%)', angle: -90, position: 'insideLeft' }}
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
            <Scatter dataKey="return" fill="#3b82f6">
              {data.map((entry, index) => (
                <Cell 
                  key={`cell-${index}`} 
                  fill={colors[index % colors.length]}
                  r={Math.sqrt(entry.size) / 2}
                />
              ))}
            </Scatter>
          </ScatterChart>
        </ResponsiveContainer>
      </div>
      
      <div className="mt-4 flex flex-wrap gap-4">
        {data.map((item, index) => (
          <div key={index} className="flex items-center space-x-2">
            <div 
              className="w-3 h-3 rounded-full"
              style={{ backgroundColor: colors[index % colors.length] }}
            ></div>
            <span className="text-sm font-medium text-slate-600">{item.company}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RiskMatrixChart;
