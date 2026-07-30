import EventCard from '../components/EventCard';

const demoEvents = [
  { id: 1, title: 'Nexus Music Night', category: 'Music', date: '20 Aug', location: 'Amsterdam' },
  { id: 2, title: 'Summer Festival', category: 'Festival', date: '05 Sep', location: 'Rotterdam' }
];

export default function Events() {
  return (
    <div>
      <h1>Upcoming Events</h1>
      {demoEvents.map((event) => (
        <EventCard key={event.id} event={event} />
      ))}
    </div>
  );
}
