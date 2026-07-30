const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export async function getEvents() {
  const response = await fetch(`${API_URL}/api/events`);
  return response.json();
}
