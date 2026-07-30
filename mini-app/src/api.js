const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {}),
    },
    ...options,
  });

  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(data.detail || 'خطا در ارتباط با سرور');
  }
  return data;
}

export const api = {
  listEvents: () => request('/events'),
  createOrder: (payload) => request('/orders', {
    method: 'POST',
    body: JSON.stringify(payload),
  }),
  createPayment: (payload) => request('/payments/create', {
    method: 'POST',
    body: JSON.stringify(payload),
  }),
  verifyPayment: (payload) => request('/payments/verify', {
    method: 'POST',
    body: JSON.stringify(payload),
  }),
};
