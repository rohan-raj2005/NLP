import React, { useState } from 'react';

const SAMPLE_BATCH = [
  "The professor is extremely approachable and responds to student emails within hours.",
  "I haven't slept properly in two weeks and feel like breaking down crying every day.",
  "Four coding milestones due in 72 hours while working part-time is completely unsustainable.",
  "The grading criteria for the term paper were extremely vague and subjective."
];

export default function BatchAnalysis() {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleRunBatch = async () => {
    setLoading(true);
    try {
      const res = await fetch('/api/batch', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ texts: SAMPLE_BATCH })
      });
      const data = await res.json();
      setResults(data.results || []);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 rounded-2xl bg-slate-900/70 border border-white/10 backdrop-blur shadow-xl">
      <div className="flex items-center justify-between mb-6">
        <div>
          <h2 className="text-xl font-bold">Batch Course Survey Analytics</h2>
          <p className="text-sm text-slate-400">Evaluate bulk student reflections simultaneously</p>
        </div>
        <button
          onClick={handleRunBatch}
          disabled={loading}
          className="px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 font-semibold text-white shadow-lg"
        >
          {loading ? "Processing..." : "Load Sample Survey (4 records)"}
        </button>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full text-left text-sm">
          <thead className="border-b border-white/10 text-slate-400">
            <tr>
              <th className="p-3">#</th>
              <th className="p-3">Student Text</th>
              <th className="p-3">Detected Label</th>
              <th className="p-3">Aspect</th>
              <th className="p-3">Stress Score</th>
            </tr>
          </thead>
          <tbody>
            {results.map((r, i) => (
              <tr key={i} className="border-b border-white/5 hover:bg-white/5">
                <td className="p-3">{i + 1}</td>
                <td className="p-3 font-medium text-slate-200">{r.student_text}</td>
                <td className="p-3 font-semibold text-indigo-400">{r.predicted_label}</td>
                <td className="p-3 text-slate-400">{r.aspect}</td>
                <td className="p-3 font-mono font-bold text-rose-400">{r.stress_index}/100</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
