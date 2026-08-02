import { useLocation } from "react-router-dom";
import QRCode from "../components/QRCode";


export default function TicketSuccess() {

  const location = useLocation();

  const ticket = location.state?.ticket;


  if (!ticket) {
    return (
      <main className="ticket-page">
        <div className="ticket-card">
          <img
            src="/logo-tikino.png"
            className="brand-logo"
          />

          <h1>
            بلیت پیدا نشد
          </h1>

        </div>
      </main>
    );
  }


  const verifyUrl =
    `http://localhost:8080/verify/${ticket.ticket_code}`;


  return (
    <main className="ticket-page">

      <div className="ticket-card">


        <img
          src="/logo-tikino.png"
          className="brand-logo"
        />


        <div className="brand-name">
          Tikino
        </div>


        <div className="pass-title">
          EVENT PASS
        </div>


        <div className="divider"/>


        <h2>
          بلیت رویداد شما
        </h2>


        <p className="subtitle">
          ورود سریع با QR Code
        </p>


        <QRCode
          value={verifyUrl}
        />



        <div className="ticket-info">


          <div>
            <span>
              کد بلیت
            </span>

            <strong>
              {ticket.ticket_code}
            </strong>
          </div>



          <div>
            <span>
              سفارش
            </span>

            <strong>
              #{ticket.order_id}
            </strong>
          </div>



          <div>
            <span>
              وضعیت
            </span>

            <strong className="active">
              معتبر
            </strong>
          </div>


        </div>



        <div className="tikino-footer">
          Powered by Tikino
        </div>


      </div>

    </main>
  );
}