import { useState } from 'react';
import { createPayment } from '../api/payment';

export default function Payment() {
  const [status, setStatus] = useState('READY');

  async function handlePayment() {
    setStatus('PROCESSING');
    // Payment integration will call gateway here
    setStatus('PENDING');
  }

  return (
    <main>
      <h1>Payment</h1>
      <p>Status: {status}</p>
      <button onClick={handlePayment}>Pay Now</button>
    </main>
  );
}
