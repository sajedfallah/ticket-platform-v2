import { useEffect, useMemo, useState } from "react";
import { QRCodeSVG } from "qrcode.react";
import { api } from "./api";
import "./styles.css";


function formatAmount(amount, currency="EUR") {
  return new Intl.NumberFormat("fa-IR", {
    style:"currency",
    currency,
    maximumFractionDigits:0
  }).format(amount / 100);
}



export default function App({telegram}) {


const telegramUser = telegram?.initDataUnsafe?.user;
const userId = Number(telegramUser?.id || 1001);


const [events,setEvents] = useState([]);
const [selectedEvent,setSelectedEvent] = useState(null);
const [quantity,setQuantity] = useState(1);
const [ticket,setTicket] = useState(null);
const [status,setStatus] = useState("loading");
const [error,setError] = useState("");



useEffect(()=>{

api.listEvents()
.then(res=>{

const items=res.items || [];

setEvents(items);
setSelectedEvent(items[0] || null);
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


if(!selectedEvent)return;


setStatus("purchasing");


try{


const order = await api.createOrder({

user_id:userId,

event_id:selectedEvent.id,

ticket_type_id:selectedEvent.ticket_type_id,

quantity

});



const payment = await api.createPayment({

order_id:order.id,

callback_url:window.location.href

});



const verification = await api.verifyPayment({

payment_id:payment.payment_id,

success:true

});




setTicket({

...verification.ticket,

event_title:selectedEvent.title,

ticket_name:selectedEvent.ticket_name,

order_number:order.order_number

});


setStatus("success");


}catch(err){

setError(err.message);
setStatus("error");

}


}






if(ticket){


return (

<main className="shell">


<section className="ticket-card">


<img
src="/logo-tikino.png"
className="ticket-logo"
/>



<div className="event-pass">

EVENT PASS

</div>



<h1>

{ticket.event_title}

</h1>



<p>

{ticket.ticket_name}

</p>





<div className="qr-wrap">

<QRCodeSVG

value={ticket.ticket_code}

size={220}

level="H"

/>

</div>





<div className="ticket-code">

{ticket.ticket_code}

</div>






<dl>


<div>

<dt>
شماره سفارش
</dt>


<dd>
{ticket.order_number}
</dd>

</div>




<div>

<dt>
وضعیت
</dt>


<dd>
{ticket.status}
</dd>

</div>



</dl>






<button

className="secondary"

onClick={()=>setTicket(null)}

>

بازگشت به رویدادها

</button>




</section>


</main>


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



<header className="hero">


<img

src="/logo-tikino.png"

className="main-logo"

/>



<h1>

خرید بلیت رویدادها

</h1>



</header>







{error &&

<div className="error">

{error}

</div>

}







<section className="event-list">


{events.map(event=>(


<button

key={event.id}

className={
`event-card ${
selectedEvent?.id===event.id
?"selected":""
}`
}


onClick={()=>setSelectedEvent(event)}

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

{formatAmount(
event.ticket_price,
event.currency
)}

</strong>





</button>


))}


</section>









{selectedEvent &&


<section className="checkout">



<div>

<span>
نوع بلیت
</span>


<strong>

{selectedEvent.ticket_name}

</strong>


</div>







<label>


تعداد



<select

value={quantity}

onChange={
e=>setQuantity(Number(e.target.value))
}

>


{[1,2,3,4].map(v=>(

<option key={v}>

{v}

</option>

))}



</select>



</label>








<div className="total">


<span>

مبلغ نهایی

</span>



<strong>

{
formatAmount(
total,
selectedEvent.currency
)
}


</strong>


</div>








<button


className="primary"


disabled={status==="purchasing"}


onClick={purchaseTicket}


>


{
status==="purchasing"
?
"در حال صدور بلیت..."
:
"خرید بلیت"
}


</button>




</section>


}



</main>


);


}