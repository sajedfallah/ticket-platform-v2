export default function StatsGrid({items=[]}) {
  return (
    <div className="stats-grid">
      {items.map((item) => (
        <div key={item.title} className="stat-card">
          <span>{item.title}</span>
          <strong>{item.value}</strong>
        </div>
      ))}
    </div>
  );
}
