export default function Events() {
  const events = [
    { id: 1, title: 'Nexus Music Night', status: 'Published' },
    { id: 2, title: 'Summer Festival', status: 'Draft' },
  ];

  return (
    <main>
      <h1>Events Management</h1>
      {events.map((event) => (
        <div key={event.id}>
          <strong>{event.title}</strong>
          <span>{event.status}</span>
        </div>
      ))}
    </main>
  );
}
