import React, { useState } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [key, setKey] = useState('');
  const [mode, setMode] = useState('1');
  const [encryptedText, setEncryptedText] = useState('');
  const [decryptedText, setDecryptedText] = useState('');

  const handleEncrypt = async () => {
    try {
      const response = await fetch('/encrypt', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text, key, mode }),
      });
      const data = await response.json();
      setEncryptedText(data.encrypted);
    } catch (error) {
      console.error('Encryption failed', error);
    }
  };

  const handleDecrypt = async () => {
    try {
      const response = await fetch('/decrypt', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: encryptedText, key, mode }),
      });
      const data = await response.json();
      setDecryptedText(data.decrypted);
    } catch (error) {
      console.error('Decryption failed', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Text Encryption Tool</h1>
        <div className="form-group">
          <label>Enter Text:</label>
          <input
            type="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Enter text to encrypt"
          />
        </div>
        <div className="form-group">
          <label>Enter Key (Number):</label>
          <input
            type="number"
            value={key}
            onChange={(e) => setKey(e.target.value)}
            placeholder="Enter encryption key"
          />
        </div>
        <div className="form-group">
          <label>Select Mode:</label>
          <select value={mode} onChange={(e) => setMode(e.target.value)}>
            <option value="1">Substitution Cipher</option>
            <option value="2">Transposition Cipher</option>
            <option value="3">Complex Cipher</option>
          </select>
        </div>
        <div className="form-group">
          <button onClick={handleEncrypt}>Encrypt</button>
          <button onClick={handleDecrypt}>Decrypt</button>
        </div>
        {encryptedText && (
          <div className="result">
            <h2>Encrypted Text:</h2>
            <p>{encryptedText}</p>
          </div>
        )}
        {decryptedText && (
          <div className="result">
            <h2>Decrypted Text:</h2>
            <p>{decryptedText}</p>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
