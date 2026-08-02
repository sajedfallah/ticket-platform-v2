const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export async function createPayment(orderId: number) {
  const response = await fetch(`${API_URL}/api/payments/create`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      order_id: orderId,
      callback_url: 'http://localhost:8080/payment/callback'
    }),
  });

  return response.json();
}


export async function verifyPayment(
  paymentId: string
) {
  const response = await fetch(`${API_URL}/api/payments/verify`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      payment_id: paymentId,
      success: true
    }),
  });

  return response.json();
}