import { useEffect, useState } from 'react';
import { getSalesReport } from '../api/reports';

export default function Reports() {
  const [report, setReport] = useState(null);

  useEffect(() => {
    getSalesReport().then(setReport);
  }, []);

  return (
    <section>
      <h1>Sales Reports</h1>
      <pre>{JSON.stringify(report, null, 2)}</pre>
    </section>
  );
}
