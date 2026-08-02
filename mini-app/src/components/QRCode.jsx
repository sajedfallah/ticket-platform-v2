import { QRCodeCanvas } from "qrcode.react";


export default function QRCode({ value }) {

  return (

    <div className="qr-wrapper">

      <QRCodeCanvas

        value={value}

        size={220}

        level="H"

        includeMargin={true}

      />

    </div>

  );

}