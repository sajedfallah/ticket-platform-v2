const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export async function createPayment(orderId: number) {
  const response = await fetch(`${API_URL}/api/payments/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ order_id: orderId })
  });

  return response.json();
}

export async function getPaymentStatus(paymentId: number) {
  const response = await fetch(`${API_URL}/api/payments/${paymentId}`);
  return response.json();
}
