type PriceCardProps = {
  title: string;
  price: number;
  onSelect?: () => void;
};

export default function PriceCard({ title, price, onSelect }: PriceCardProps) {
  return (
    <button className="price-card" onClick={onSelect}>
      <span>{title}</span>
      <strong>{price.toLocaleString()} تومان</strong>
    </button>
  );
}
