/**
 * express_server.js - Node.js Express REST API Bridge
 * Connects frontend requests to the Python NLP Inference engine via Child Process or HTTP.
 */

const express = require('express');
const cors = require('cors');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 8000;

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '../06_frontend_react_app')));

// Python predictor execution helper
function runPythonPrediction(text) {
  return new Promise((resolve, reject) => {
    const pythonScript = path.join(__dirname, 'predict.py');
    const pythonProcess = spawn('python', ['-c', `
import sys, json
sys.path.insert(0, r'${__dirname}')
from predict import AcademicStressPredictor
p = AcademicStressPredictor()
res = p.predict("""${text.replace(/"/g, '\\"')}""")
print(json.dumps(res))
    `]);

    let dataOut = '';
    let errorOut = '';

    pythonProcess.stdout.on('data', (data) => {
      dataOut += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
      errorOut += data.toString();
    });

    pythonProcess.on('close', (code) => {
      if (code !== 0) {
        return reject(new Error(`Python process exited with code ${code}: ${errorOut}`));
      }
      try {
        const jsonRes = JSON.parse(dataOut.trim());
        resolve(jsonRes);
      } catch (err) {
        reject(new Error(`Failed to parse Python JSON output: ${dataOut}`));
      }
    });
  });
}

// Routes
app.get('/api/health', (req, res) => {
  res.json({
    status: 'online',
    runtime: 'Node.js Express + Python NLP Engine',
    port: PORT,
    timestamp: new Date().toISOString()
  });
});

app.post('/api/analyze', async (req, res) => {
  const { text } = req.body;
  if (!text) {
    return res.status(400).json({ error: "Missing 'text' in request body." });
  }

  try {
    const result = await runPythonPrediction(text);
    res.json(result);
  } catch (err) {
    console.error('Inference error:', err);
    res.status(500).json({ error: 'Internal NLP Inference Failure', details: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`[+] Express Server running on http://localhost:${PORT}`);
  console.log(`[+] Serving UI from ../06_frontend_react_app`);
});
