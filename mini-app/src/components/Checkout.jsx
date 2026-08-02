export default function Checkout({
  event,
  quantity,
  setQuantity,
  total,
  onPurchase,
  loading
}) {


  return (

    <section className="checkout">



      <div>

        <span>
          نوع بلیت
        </span>


        <strong>

          {event.ticket_name}

        </strong>


      </div>





      <label>


        تعداد



        <select


          value={quantity}


          onChange={
            e =>
            setQuantity(
              Number(e.target.value)
            )
          }


        >


          {[1,2,3,4].map(v=>(


            <option

              key={v}

              value={v}

            >

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

          {total}

        </strong>



      </div>








      <button


        className="primary"


        disabled={loading}


        onClick={onPurchase}


      >


        {

          loading

          ?

          "در حال صدور بلیت..."

          :

          "خرید بلیت"

        }



      </button>




    </section>


  );

}