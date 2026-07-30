import { useState } from 'react';
import { createOrder } from '../api/client';
import Button from '../components/Button';
import StatusBadge from '../components/StatusBadge';

export default function Checkout() {
  const [status, setStatus] = useState('READY');
  const [orderId, setOrderId] = useState<number | null>(null);

  async function handleCreateOrder() {
    setStatus('CREATING');
    try {
      const order = await createOrder({
        event_id: 1,
        ticket_type_id: 1,
        quantity: 1,
      });
      setOrderId(order.id);
      setStatus('PENDING_PAYMENT');
    } catch {
      setStatus('FAILED');
    }
  }

  return (
    <main>
      <h1>Checkout</h1>
      <p>Review ticket information and continue payment.</p>

      <StatusBadge status={status} />

      {orderId && <p>Order #{orderId}</p>}

      <Button onClick={handleCreateOrder}>
        Create Order
      </Button>
    </main>
  );
}
