import React, { useState } from 'react';
import ConfidenceGauge from './ConfidenceGauge';

const PRESETS = [
  { label: "🔥 Severe Exam Panic", text: "I am having severe anxiety and panic attacks because of the upcoming final exam. I haven't slept in three days." },
  { label: "⏳ 3 Deadlines in 48h", text: "Having three heavy project deadlines and two midterms in the exact same 48 hours is impossible to manage." },
  { label: "✨ Not Stressed (Negation)", text: "I am not stressed at all, the professor explains complex algorithms with great clarity and patience!" },
  { label: "🌱 Clear & Supportive", text: "I really enjoyed the hands-on lab sessions this semester; they made theoretical concepts very easy to grasp." }
];

export default function StressAnalyzer() {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleAnalyze = async () => {
    if (!text.trim()) return;
    setLoading(true);
    try {
      const res = await fetch('http://127.0.0.1:8000/api/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
      });
      const data = await res.json();
      setResult(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
      {/* Input */}
      <div className="p-6 rounded-2xl bg-slate-900/70 border border-white/10 backdrop-blur shadow-xl">
        <h2 className="text-xl font-bold mb-2">Student Voice Input</h2>
        <div className="flex flex-wrap gap-2 mb-4">
          {PRESETS.map((p, idx) => (
            <button
              key={idx}
              onClick={() => setText(p.text)}
              className="text-xs px-3 py-1.5 rounded-full bg-white/5 border border-white/10 hover:bg-indigo-600/30 transition-all text-slate-300"
            >
              {p.label}
            </button>
          ))}
        </div>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          rows={6}
          className="w-full p-4 rounded-xl bg-slate-950/80 border border-white/10 focus:border-indigo-500 focus:outline-none text-slate-100"
          placeholder="Type or paste student feedback..."
        />
        <div className="mt-4 flex justify-end">
          <button
            onClick={handleAnalyze}
            disabled={loading}
            className="px-6 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 font-semibold text-white transition-all shadow-lg shadow-indigo-600/30"
          >
            {loading ? "Analyzing..." : "Run NLP Analysis"}
          </button>
        </div>
      </div>

      {/* Result */}
      <div className="p-6 rounded-2xl bg-slate-900/70 border border-white/10 backdrop-blur shadow-xl">
        {result ? (
          <div>
            <div className="flex items-center justify-between mb-4">
              <span className="text-lg font-bold px-4 py-1.5 rounded-full bg-rose-500/20 text-rose-300 border border-rose-500/30">
                {result.predicted_label}
              </span>
              <span className="text-sm font-semibold text-slate-400">
                {result.aspect} | Urgency: {result.urgency}
              </span>
            </div>

            <ConfidenceGauge stressIndex={result.stress_index} confidence={result.confidence} />

            <div className="mt-6 p-4 rounded-xl bg-indigo-950/40 border border-indigo-500/20">
              <h4 className="text-sm font-bold text-indigo-300 mb-2">Supportive Recommendations:</h4>
              <ul className="list-disc list-inside text-sm text-slate-300 space-y-1">
                {result.recommendations?.map((rec, i) => (
                  <li key={i}>{rec}</li>
                ))}
              </ul>
            </div>
          </div>
        ) : (
          <div className="h-full flex items-center justify-center text-slate-500">
            Awaiting input for analysis...
          </div>
        )}
      </div>
    </div>
  );
}
