type EventCardProps = {
  title: string;
  category: string;
  date: string;
  location: string;
};

export default function EventCard({ title, category, date, location }: EventCardProps) {
  return (
    <div className="rounded-2xl border border-white/10 bg-black/30 p-4 text-white">
      <div className="text-sm text-yellow-400">{category}</div>
      <h3 className="mt-2 text-xl font-bold">{title}</h3>
      <p className="mt-2 text-sm opacity-80">{date}</p>
      <p className="text-sm opacity-80">{location}</p>
      <button className="mt-4 rounded-xl bg-yellow-500 px-4 py-2 text-black">Buy Ticket</button>
    </div>
  );
}
