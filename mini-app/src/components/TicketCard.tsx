export default function TicketCard({ ticket }: { ticket: any }) {
  return (
    <div className="ticket-card">
      <h3>{ticket?.event || 'Event Ticket'}</h3>
      <p>Code: {ticket?.code || 'TKT-0000'}</p>
      <span>{ticket?.status || 'ACTIVE'}</span>
    </div>
  );
}
