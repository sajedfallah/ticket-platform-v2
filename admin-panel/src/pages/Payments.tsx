export default function Payments() {
  const metrics = [
    { title: "Total Revenue", value: "125,000 EUR" },
    { title: "Successful Payments", value: "2,450" },
    { title: "Pending Payments", value: "32" },
    { title: "Failed Payments", value: "8" },
  ];

  return (
    <main>
      <h1>Payments Analytics</h1>
      <section>
        {metrics.map((metric) => (
          <div key={metric.title}>
            <h3>{metric.title}</h3>
            <p>{metric.value}</p>
          </div>
        ))}
      </section>
    </main>
  );
}
