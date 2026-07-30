export default function Sidebar() {
  const items = [
    'Dashboard',
    'Events',
    'Tickets',
    'Orders',
    'Payments',
    'Reports',
    'Check-in',
    'Users',
    'Settings'
  ];

  return (
    <aside>
      <h2>Ticket Platform</h2>
      {items.map((item) => (
        <div key={item}>{item}</div>
      ))}
    </aside>
  );
}
