import { useEffect, useState } from "react";
import { Html5QrcodeScanner } from "html5-qrcode";


export default function Verify(){

const [code,setCode]=useState("");



useEffect(()=>{


const scanner =
new Html5QrcodeScanner(
"reader",
{
fps:10,
qrbox:250
}
);


scanner.render(

(decoded)=>{

setCode(decoded);

scanner.clear();

},

(error)=>{}

);



return ()=>{

scanner.clear();

};


},[]);



return (

<main className="shell">


<section className="ticket-card">


<img
src="/logo-tikino.png"
className="brand-logo"
/>


<h1>
Tikino Gate
</h1>


<p>
اسکن بلیت ورودی
</p>


<div id="reader"></div>


{
code &&

<div>

<hr/>

<h2>
QR دریافت شد
</h2>

<p>
{code}
</p>


</div>

}


</section>


</main>

);

}