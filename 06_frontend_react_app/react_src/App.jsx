import React, { useState } from 'react';
import StressAnalyzer from './components/StressAnalyzer';
import BatchAnalysis from './components/BatchAnalysis';
import SupportTips from './components/SupportTips';

export default function App() {
  const [activeTab, setActiveTab] = useState('single');

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 font-sans">
      {/* Header */}
      <header className="border-b border-white/10 bg-slate-900/60 backdrop-blur sticky top-0 z-50 px-6 py-4">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-indigo-600 flex items-center justify-center font-bold text-xl shadow-lg shadow-indigo-500/30">
              ⚡
            </div>
            <div>
              <h1 className="text-xl font-bold tracking-tight">
                MindTrack<span className="text-indigo-400">.AI</span>
              </h1>
              <p className="text-xs text-slate-400 font-mono">Academic Stress NLP v1.0</p>
            </div>
          </div>

          <div className="flex bg-white/5 p-1 rounded-full border border-white/10">
            <button
              onClick={() => setActiveTab('single')}
              className={`px-5 py-1.5 text-sm font-semibold rounded-full transition-all ${
                activeTab === 'single' ? 'bg-indigo-600 text-white shadow-md' : 'text-slate-400 hover:text-white'
              }`}
            >
              Real-Time Analyzer
            </button>
            <button
              onClick={() => setActiveTab('batch')}
              className={`px-5 py-1.5 text-sm font-semibold rounded-full transition-all ${
                activeTab === 'batch' ? 'bg-indigo-600 text-white shadow-md' : 'text-slate-400 hover:text-white'
              }`}
            >
              Batch Survey
            </button>
            <button
              onClick={() => setActiveTab('wellness')}
              className={`px-5 py-1.5 text-sm font-semibold rounded-full transition-all ${
                activeTab === 'wellness' ? 'bg-indigo-600 text-white shadow-md' : 'text-slate-400 hover:text-white'
              }`}
            >
              Coping Hub
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-6 py-10">
        {activeTab === 'single' && <StressAnalyzer />}
        {activeTab === 'batch' && <BatchAnalysis />}
        {activeTab === 'wellness' && <SupportTips />}
      </main>
    </div>
  );
}
