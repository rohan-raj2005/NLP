/**
 * app.js - Frontend Logic & API Client for MindTrack AI
 */

const API_BASE = window.location.origin.includes('http') ? window.location.origin : 'http://127.0.0.1:8000';

const PRESETS = {
  stress: "I am having severe anxiety and panic attacks because of the upcoming final exam. I haven't slept in three days.",
  overload: "Having three heavy project deadlines and two midterms in the exact same 48 hours is impossible to manage.",
  negation: "I am not stressed at all, the professor explains complex algorithms with great clarity and patience!",
  frustration: "Teaching assistants took over a month to return our graded homework, leaving us totally blind for midterms.",
  positive: "I really enjoyed the hands-on lab sessions this semester; they made theoretical concepts very easy to grasp."
};

const SAMPLE_BATCH = [
  "The professor is extremely approachable and responds to student emails within hours.",
  "I haven't slept properly in two weeks and feel like breaking down crying every day.",
  "The course syllabus was distributed on the first day of class as scheduled.",
  "Four coding milestones due in 72 hours while working part-time is completely unsustainable.",
  "The grading criteria for the term paper were extremely vague and subjective.",
  "I have completely lost motivation and stopped attending lectures because nothing makes sense.",
  "I'm not overwhelmed anymore now that the TA helped clarify the project roadmap."
];

// Switch active navigation tab
function switchTab(tabId) {
  document.querySelectorAll('.tab-view').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach(el => el.classList.remove('active'));

  const viewEl = document.getElementById(`view-${tabId}`);
  const btnEl = document.getElementById(`tab-${tabId}-btn`);

  if (viewEl) viewEl.classList.add('active');
  if (btnEl) btnEl.classList.add('active');
}

// Character counter
const textarea = document.getElementById('student-input');
if (textarea) {
  textarea.addEventListener('input', () => {
    const countEl = document.getElementById('char-count');
    if (countEl) countEl.innerText = textarea.value.length;
  });
}

// Apply preset text
function applyPreset(key) {
  if (textarea && PRESETS[key]) {
    textarea.value = PRESETS[key];
    const countEl = document.getElementById('char-count');
    if (countEl) countEl.innerText = textarea.value.length;
    analyzeSingleText();
  }
}

function clearInput() {
  if (textarea) {
    textarea.value = '';
    const countEl = document.getElementById('char-count');
    if (countEl) countEl.innerText = '0';
  }
}

// Run single text analysis
async function analyzeSingleText() {
  const text = textarea ? textarea.value.trim() : '';
  if (!text) {
    alert('Please enter some student feedback or select a preset pill first.');
    return;
  }

  const spinner = document.getElementById('btn-spinner');
  const analyzeBtn = document.getElementById('analyze-btn');
  if (spinner) spinner.style.display = 'inline-block';
  if (analyzeBtn) analyzeBtn.disabled = true;

  try {
    const response = await fetch(`${API_BASE}/api/analyze`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });

    if (!response.ok) {
      throw new Error(`Server returned status: ${response.status}`);
    }

    const data = await response.json();
    renderAnalysisResult(data);
  } catch (err) {
    console.warn('API error, falling back to local heuristic predictor:', err);
    const fallbackData = generateLocalPrediction(text);
    renderAnalysisResult(fallbackData);
  } finally {
    if (spinner) spinner.style.display = 'none';
    if (analyzeBtn) analyzeBtn.disabled = false;
  }
}

// Render single result
function renderAnalysisResult(data) {
  const placeholder = document.getElementById('output-placeholder');
  const resultBox = document.getElementById('analysis-result');
  
  if (placeholder) placeholder.style.display = 'none';
  if (resultBox) resultBox.style.display = 'block';

  // Badge label
  const badge = document.getElementById('res-badge');
  if (badge) {
    badge.innerText = data.predicted_label;
    badge.className = 'label-badge';
    if (data.predicted_label === 'Positive') badge.classList.add('positive');
    else if (data.predicted_label === 'Neutral') badge.classList.add('neutral');
    else if (data.predicted_label === 'Overload') badge.classList.add('overload');
  }

  // Aspect & Urgency
  const aspectEl = document.getElementById('res-aspect');
  if (aspectEl) aspectEl.innerText = data.aspect || 'Academic Domain';

  const urgencyEl = document.getElementById('res-urgency');
  if (urgencyEl) {
    urgencyEl.innerText = `Urgency: ${data.urgency || 'Normal'}`;
    urgencyEl.style.background = data.urgency === 'High' ? 'rgba(244, 63, 94, 0.2)' : 'rgba(99, 102, 241, 0.2)';
    urgencyEl.style.color = data.urgency === 'High' ? '#f43f5e' : '#818cf8';
  }

  // Stress Index Gauge
  const stressVal = document.getElementById('res-stress-index');
  const progressBar = document.getElementById('res-progress-bar');
  if (stressVal) stressVal.innerText = `${data.stress_index}/100`;
  if (progressBar) progressBar.style.width = `${Math.min(data.stress_index, 100)}%`;

  // Probabilities Bars
  const probContainer = document.getElementById('prob-bars');
  if (probContainer && data.probabilities) {
    probContainer.innerHTML = '';
    for (const [cls, prob] of Object.entries(data.probabilities)) {
      const pct = (prob * 100).toFixed(1);
      const item = document.createElement('div');
      item.className = 'prob-item';
      item.innerHTML = `
        <div class="prob-info">
          <span>${cls}</span>
          <strong>${pct}%</strong>
        </div>
        <div class="prob-bar-track">
          <div class="prob-bar-fill" style="width: ${pct}%"></div>
        </div>
      `;
      probContainer.appendChild(item);
    }
  }

  // Recommendations
  const recList = document.getElementById('res-rec-list');
  if (recList && data.recommendations) {
    recList.innerHTML = '';
    data.recommendations.forEach(rec => {
      const li = document.createElement('li');
      li.innerText = rec;
      recList.appendChild(li);
    });
  }
}

// Batch Analysis Runner
async function loadSampleBatch() {
  const tableBody = document.getElementById('batch-table-body');
  if (tableBody) {
    tableBody.innerHTML = `<tr><td colspan="6" class="text-center py-4 text-muted">Running NLP batch inference on ${SAMPLE_BATCH.length} student records...</td></tr>`;
  }

  try {
    const response = await fetch(`${API_BASE}/api/batch`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ texts: SAMPLE_BATCH })
    });

    let data;
    if (response.ok) {
      data = await response.json();
    } else {
      throw new Error('Server returned non-200');
    }

    renderBatchResults(data);
  } catch (err) {
    console.warn('Batch API unavailable, rendering client-side predictions:', err);
    const mockResults = SAMPLE_BATCH.map(t => generateLocalPrediction(t));
    const stressIdxs = mockResults.map(r => r.stress_index);
    renderBatchResults({
      batch_size: mockResults.length,
      average_stress_index: Math.round(stressIdxs.reduce((a, b) => a + b, 0) / stressIdxs.length),
      results: mockResults
    });
  }
}

function renderBatchResults(data) {
  const tableBody = document.getElementById('batch-table-body');
  if (!tableBody) return;

  tableBody.innerHTML = '';
  let highStressCount = 0;
  let positiveCount = 0;

  data.results.forEach((res, idx) => {
    if (res.stress_index >= 70) highStressCount++;
    if (res.predicted_label === 'Positive') positiveCount++;

    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td>${idx + 1}</td>
      <td><strong>${escapeHtml(res.student_text)}</strong></td>
      <td><span class="label-badge ${res.predicted_label.toLowerCase()}">${res.predicted_label}</span></td>
      <td>${res.aspect || 'Academic'}</td>
      <td><strong style="color: ${res.stress_index > 65 ? '#f43f5e' : '#34d399'}">${res.stress_index}/100</strong></td>
      <td>${res.confidence_pct || '90%'}</td>
    `;
    tableBody.appendChild(tr);
  });

  // Update Stats Cards
  document.getElementById('stat-total').innerText = data.results.length;
  document.getElementById('stat-stress-pct').innerText = `${Math.round((highStressCount / data.results.length) * 100)}%`;
  document.getElementById('stat-avg-stress').innerText = data.average_stress_index || '45';
  document.getElementById('stat-pos-rate').innerText = `${Math.round((positiveCount / data.results.length) * 100)}%`;
}

// Client-side fallback predictor
function generateLocalPrediction(text) {
  const lower = text.toLowerCase();
  let label = "Neutral";
  let stress = 25;
  let aspect = "General";
  let urgency = "Low";

  if (lower.includes("not stressed") || lower.includes("not overwhelmed")) {
    label = "Positive";
    stress = 12;
    aspect = "Teaching";
  } else if (lower.includes("anxiety") || lower.includes("panic") || lower.includes("crying") || lower.includes("insomnia")) {
    label = "High Stress";
    stress = 94;
    aspect = "Mental Well-being";
    urgency = "High";
  } else if (lower.includes("deadline") || lower.includes("hours") || lower.includes("impossible") || lower.includes("unsustainable")) {
    label = "Overload";
    stress = 78;
    aspect = "Workload";
    urgency = "Medium";
  } else if (lower.includes("vague") || lower.includes("rubric") || lower.includes("ignored") || lower.includes("month")) {
    label = "Frustration";
    stress = 62;
    aspect = "Examination";
    urgency = "Medium";
  } else if (lower.includes("lost motivation") || lower.includes("stopped attending") || lower.includes("nothing makes sense")) {
    label = "Disengagement";
    stress = 50;
    aspect = "Engagement";
  } else if (lower.includes("approachable") || lower.includes("clarity") || lower.includes("enjoyed") || lower.includes("helpful")) {
    label = "Positive";
    stress = 8;
    aspect = "Teaching";
  }

  return {
    student_text: text,
    predicted_label: label,
    confidence: 0.92,
    confidence_pct: "92.0%",
    stress_index: stress,
    urgency: urgency,
    aspect: aspect,
    probabilities: {
      "High Stress": label === "High Stress" ? 0.92 : 0.02,
      "Overload": label === "Overload" ? 0.90 : 0.03,
      "Frustration": label === "Frustration" ? 0.88 : 0.03,
      "Positive": label === "Positive" ? 0.91 : 0.02,
      "Neutral": label === "Neutral" ? 0.85 : 0.05,
      "Disengagement": label === "Disengagement" ? 0.89 : 0.02
    },
    recommendations: [
      "Consult course office hours for tailored pacing advice.",
      "Utilize university wellness resources and academic coaching."
    ],
    is_alert_required: stress >= 75
  };
}

function escapeHtml(str) {
  return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

// Attach event handlers to window for inline HTML onclick compatibility
if (typeof window !== 'undefined') {
  window.switchTab = switchTab;
  window.applyPreset = applyPreset;
  window.clearInput = clearInput;
  window.analyzeSingleText = analyzeSingleText;
  window.loadSampleBatch = loadSampleBatch;
}
