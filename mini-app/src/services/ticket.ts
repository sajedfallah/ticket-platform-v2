export async function issueTicket(orderId: string) {
  const response = await fetch('/api/tickets/issue', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ order_id: orderId }),
  });

  return response.json();
}
