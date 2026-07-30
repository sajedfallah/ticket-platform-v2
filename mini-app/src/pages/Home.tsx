import EventCard from '../components/EventCard';

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 p-4">
      <h1 className="mb-6 text-3xl font-bold text-white">Ticket Platform</h1>
      <EventCard
        title="Nexus Music Night"
        category="Music"
        date="20 August"
        location="Amsterdam"
      />
    </main>
  );
}
