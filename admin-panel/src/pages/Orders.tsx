export default function Orders() {
  const orders = [
    {
      id: "ORD-1001",
      user: "Telegram User",
      event: "Nexus Music Night",
      ticket: "VIP",
      amount: "100 EUR",
      payment: "PAID",
      status: "COMPLETED",
    },
    {
      id: "ORD-1002",
      user: "Telegram User",
      event: "Summer Festival",
      ticket: "Gold",
      amount: "50 EUR",
      payment: "PENDING",
      status: "WAITING",
    },
  ];

  return (
    <main>
      <h1>Orders Management</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>User</th>
            <th>Event</th>
            <th>Ticket</th>
            <th>Amount</th>
            <th>Payment</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order) => (
            <tr key={order.id}>
              <td>{order.id}</td>
              <td>{order.user}</td>
              <td>{order.event}</td>
              <td>{order.ticket}</td>
              <td>{order.amount}</td>
              <td>{order.payment}</td>
              <td>{order.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}
