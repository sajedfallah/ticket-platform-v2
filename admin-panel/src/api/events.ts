import { apiRequest } from './client';

export function getEvents() {
  return apiRequest('/api/events');
}

export function createEvent(data: unknown) {
  return apiRequest('/api/events', {
    method: 'POST',
    body: JSON.stringify(data),
  });
}
