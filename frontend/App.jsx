import React, { useState } from 'react';
import './App.css';

function App() {
  const [inputText, setInputText] = useState('');
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          input_text: inputText,
          model_name: 'default'
        })
      });
      const data = await response.json();
      setPrediction(data);
    } catch (error) {
      console.error('Error:', error);
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>🚀 AI Platform</h1>
        <p>Advanced AI Model Serving Platform</p>
      </header>
      
      <main className="container">
        <div className="input-section">
          <textarea
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Enter your text here..."
            rows="4"
          />
          <button onClick={handlePredict} disabled={loading}>
            {loading ? 'Processing...' : 'Get Prediction'}
          </button>
        </div>

        {prediction && (
          <div className="result-section">
            <h2>Prediction Result</h2>
            <p><strong>Prediction:</strong> {prediction.prediction}</p>
            <p><strong>Confidence:</strong> {(prediction.confidence * 100).toFixed(2)}%</p>
            <p><strong>Model Used:</strong> {prediction.model_used}</p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
