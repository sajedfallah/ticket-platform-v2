import React, { useState } from 'react';

export default function CheckInScanner() {
  const [code, setCode] = useState('');
  const [status, setStatus] = useState('READY');

  const validateTicket = () => {
    if (!code) return;
    setStatus('VALIDATING');
    setTimeout(() => setStatus('ACTIVE - ENTRY ALLOWED'), 500);
  };

  return (
    <div>
      <h1>Check-in Scanner</h1>
      <input
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Scan ticket QR code"
      />
      <button onClick={validateTicket}>Validate</button>
      <p>Status: {status}</p>
    </div>
  );
}
