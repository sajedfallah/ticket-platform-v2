const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export async function getSalesReport() {
  const response = await fetch(`${API_URL}/reports/sales`);
  return response.json();
}

export async function getEventReport(eventId) {
  const response = await fetch(`${API_URL}/reports/events/${eventId}`);
  return response.json();
}
