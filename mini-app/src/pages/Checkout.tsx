import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

import { createOrder } from '../api/client';
import { createPayment, verifyPayment } from '../api/payment';

import Button from '../components/Button';
import StatusBadge from '../components/StatusBadge';


export default function Checkout() {
  const navigate = useNavigate();

  const [status, setStatus] = useState('READY');
  const [orderId, setOrderId] = useState<number | null>(null);


  async function handleCreateOrder() {
    setStatus('CREATING');

    try {
      // 1 - Create Order
      const order = await createOrder({
        event_id: 1,
        ticket_type_id: 1,
        quantity: 1,
      });

      setOrderId(order.id);
      setStatus('CREATING_PAYMENT');


      // 2 - Create Payment
      const payment = await createPayment(order.id);


      setStatus('VERIFYING_PAYMENT');


      // 3 - Verify Payment (Demo Mode)
      const result = await verifyPayment(payment.payment_id);


      if (result.ticket) {
        setStatus('SUCCESS');


        // 4 - Send real ticket to success page
        navigate('/ticket-success', {
          state: {
            ticket: result.ticket,
          },
        });

      } else {
        setStatus('FAILED');
      }


    } catch (error) {
      console.error(error);
      setStatus('FAILED');
    }
  }


  return (
    <main>
      <h1>Checkout</h1>

      <p>
        Review ticket information and continue payment.
      </p>


      <StatusBadge status={status} />


      {orderId && (
        <p>
          Order #{orderId}
        </p>
      )}


      <Button onClick={handleCreateOrder}>
        Buy Ticket
      </Button>

    </main>
  );
}