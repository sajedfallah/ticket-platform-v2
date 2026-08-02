import { useEffect, useMemo, useState } from "react";

import { api } from "./api";

import Header from "./components/Header";
import EventCard from "./components/EventCard";
import Checkout from "./components/Checkout";
import TicketCard from "./components/TicketCard";

import "./styles.css";



function formatAmount(amount, currency = "EUR") {

  return new Intl.NumberFormat("fa-IR", {

    style: "currency",

    currency,

    maximumFractionDigits: 0,

  }).format(amount / 100);

}





export default function App({ telegram }) {


  const telegramUser =
    telegram?.initDataUnsafe?.user;


  const userId =
    Number(telegramUser?.id || 1001);



  const [events,setEvents] = useState([]);

  const [selectedEvent,setSelectedEvent] = useState(null);

  const [quantity,setQuantity] = useState(1);

  const [ticket,setTicket] = useState(null);

  const [status,setStatus] = useState("loading");

  const [error,setError] = useState("");





  useEffect(()=>{


    api.listEvents()

    .then(result=>{


      const items =
        result.items || [];


      setEvents(items);


      setSelectedEvent(
        items[0] || null
      );


      setStatus("ready");


    })


    .catch(err=>{


      setError(err.message);

      setStatus("error");


    });


  },[]);








  const total = useMemo(()=>{


    return (

      (selectedEvent?.ticket_price || 0)

      *

      quantity

    );


  },[selectedEvent,quantity]);









  async function purchaseTicket(){


    if(!selectedEvent)
      return;



    setStatus("purchasing");



    try {



      const order = await api.createOrder({

        user_id:userId,

        event_id:selectedEvent.id,

        ticket_type_id:selectedEvent.ticket_type_id,

        quantity

      });







      const payment =
        await api.createPayment({


          order_id:order.id,


          callback_url:
            window.location.href


        });







      const verification =
        await api.verifyPayment({


          payment_id:
            payment.payment_id,


          success:true


        });








      setTicket({


        ...verification.ticket,


        event_title:
          selectedEvent.title,


        ticket_name:
          selectedEvent.ticket_name,


        order_number:
          order.order_number



      });





      setStatus("success");



    }


    catch(err){


      setError(err.message);

      setStatus("error");


    }


  }









  if(ticket){


    return (

      <TicketCard


        ticket={ticket}


        onBack={()=>setTicket(null)}


      />

    );


  }









  if(status==="loading"){


    return (

      <main className="shell">

        <p>

          در حال بارگذاری...

        </p>


      </main>

    );


  }









  return (

    <main className="shell">



      <Header />





      {
        error &&

        <div className="error">

          {error}

        </div>

      }








      <section className="event-list">


        {
          events.map(event=>(


            <EventCard


              key={event.id}


              event={event}


              selected={
                selectedEvent?.id === event.id
              }


              onSelect={()=>{

                setSelectedEvent(event);

              }}


            />


          ))

        }


      </section>









      {

        selectedEvent &&


        <Checkout



          event={selectedEvent}



          quantity={quantity}



          setQuantity={setQuantity}



          total={

            formatAmount(

              total,

              selectedEvent.currency

            )

          }



          onPurchase={purchaseTicket}



          loading={
            status==="purchasing"
          }



        />

      }



    </main>

  );

}