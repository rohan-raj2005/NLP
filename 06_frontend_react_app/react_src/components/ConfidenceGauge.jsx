import React from 'react';

export default function ConfidenceGauge({ stressIndex, confidence }) {
  return (
    <div className="space-y-4">
      <div>
        <div className="flex justify-between text-sm font-semibold mb-1">
          <span className="text-slate-300">Academic Stress Index</span>
          <span className="font-mono text-rose-400 font-bold">{stressIndex}/100</span>
        </div>
        <div className="h-3 w-full bg-slate-800 rounded-full overflow-hidden">
          <div
            className="h-full bg-gradient-to-r from-emerald-500 via-amber-500 to-rose-500 rounded-full transition-all duration-700"
            style={{ width: `${stressIndex}%` }}
          />
        </div>
      </div>

      <div className="flex justify-between text-xs text-slate-400">
        <span>Model Confidence: <strong>{(confidence * 100).toFixed(1)}%</strong></span>
        <span>Status: {stressIndex > 70 ? 'High Distress Alert' : 'Normal'}</span>
      </div>
    </div>
  );
}
