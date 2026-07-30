export default function TicketInventory() {
  const tickets = [
    { type: "VIP", capacity: 100, sold: 45 },
    { type: "Gold", capacity: 300, sold: 210 },
    { type: "Normal", capacity: 500, sold: 320 },
  ];

  return (
    <main>
      <h1>Ticket Inventory</h1>
      {tickets.map((ticket) => (
        <div key={ticket.type}>
          <h3>{ticket.type}</h3>
          <p>Capacity: {ticket.capacity}</p>
          <p>Sold: {ticket.sold}</p>
          <p>Available: {ticket.capacity - ticket.sold}</p>
        </div>
      ))}
    </main>
  );
}
