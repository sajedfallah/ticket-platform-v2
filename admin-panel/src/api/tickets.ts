import { apiRequest } from './client';

export function validateTicket(code: string) {
  return apiRequest('/api/tickets/validate', {
    method: 'POST',
    body: JSON.stringify({ code }),
  });
}
