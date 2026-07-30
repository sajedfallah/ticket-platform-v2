export default function Orders() {
  const orders = [
    { id: "ORD-1001", user: "Telegram User", status: "PAID" },
    { id: "ORD-1002", user: "Telegram User", status: "PENDING" },
  ];

  return (
    <main>
      <h1>Orders</h1>
      {orders.map((order) => (
        <div key={order.id}>
          <p>{order.id}</p>
          <p>{order.user}</p>
          <p>{order.status}</p>
        </div>
      ))}
    </main>
  );
}
