const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

async function request(path: string, options?: RequestInit) {
  const response = await fetch(`${API_URL}${path}`, {
    headers: {
      'Content-Type': 'application/json',
    },
    ...options,
  });

  return response.json();
}

export async function getEvents() {
  return request('/api/events');
}

export async function createOrder(payload: {
  event_id: number;
  ticket_type_id: number;
  quantity: number;
}) {
  return request('/api/orders/create', {
    method: 'POST',
    body: JSON.stringify(payload),
  });
}

export async function getTickets(userId: number) {
  return request(`/api/tickets/user/${userId}`);
}
