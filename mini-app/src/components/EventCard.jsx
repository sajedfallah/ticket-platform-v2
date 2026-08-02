function formatAmount(amount, currency) {

  return new Intl.NumberFormat("fa-IR", {

    style: "currency",

    currency,

    maximumFractionDigits: 0,

  }).format(amount / 100);

}



export default function EventCard({
  event,
  selected,
  onSelect
}) {


  return (

    <button

      className={
        `event-card ${
          selected ? "selected" : ""
        }`
      }


      onClick={onSelect}


    >


      <span className="badge">

        {event.category}

      </span>




      <h2>

        {event.title}

      </h2>




      <p>

        {event.description}

      </p>





      <strong>

        {
          formatAmount(
            event.ticket_price,
            event.currency
          )
        }

      </strong>




    </button>


  );

}