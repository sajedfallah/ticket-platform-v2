type Props = {
  value: string;
};

export default function QRCode({ value }: Props) {
  return (
    <div className="qr-card">
      <div>QR CODE</div>
      <small>{value}</small>
    </div>
  );
}
