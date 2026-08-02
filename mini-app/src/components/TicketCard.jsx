import QRCode from "./QRCode";

export default function TicketCard({ ticket, onBack }) {
  return (
    <main className="shell ticket-page">
      <section className="ticket-card">
        <img
          src="/logo-tikino.png"
          className="ticket-logo"
          alt="لوگوی تیکینو"
        />

        <div className="event-pass">
          EVENT PASS
        </div>

        <h1 className="ticket-title">
          {ticket.event_title}
        </h1>

        <p className="ticket-type">
          {ticket.ticket_name}
        </p>

        <div className="ticket-divider" />

        <div className="qr-wrap">
          <QRCode value={ticket.ticket_code} />
        </div>

        <div className="ticket-code-label">
          کد بلیت
        </div>

        <div className="ticket-code">
          {ticket.ticket_code}
        </div>

        <div className="ticket-divider" />

        <dl className="ticket-details">
          <div>
            <dt>شماره سفارش</dt>
            <dd>{ticket.order_number}</dd>
          </div>

          <div>
            <dt>وضعیت</dt>
            <dd>{ticket.status}</dd>
          </div>
        </dl>

        <button
          type="button"
          className="secondary"
          onClick={onBack}
        >
          بازگشت به رویدادها
        </button>
      </section>
    </main>
  );
}