import React from 'react';

export default function SupportTips() {
  const tips = [
    { icon: "🧘‍♀️", title: "4-7-8 Breathing Technique", desc: "Inhale 4s, hold 7s, exhale 8s to calm autonomic pre-exam nervous tension." },
    { icon: "⏱️", title: "Pomodoro Focus Sprints", desc: "Work in 25-minute sprints with 5-minute cognitive breaks to avoid mental burnout." },
    { icon: "📊", title: "Eisenhower Matrix", desc: "Sort tasks into Urgent vs. Important to regain control over overlapping deadlines." },
    { icon: "🤝", title: "Campus Mental Health", desc: "24/7 confidential student support helpline: 1-800-273-TALK." }
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
      {tips.map((t, idx) => (
        <div key={idx} className="p-6 rounded-2xl bg-slate-900/70 border border-white/10 backdrop-blur">
          <div className="text-3xl mb-3">{t.icon}</div>
          <h3 className="text-lg font-bold text-slate-100 mb-2">{t.title}</h3>
          <p className="text-sm text-slate-400 leading-relaxed">{t.desc}</p>
        </div>
      ))}
    </div>
  );
}
