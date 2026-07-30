export default function DataTable({ columns = [], rows = [] }) {
  return (
    <table className="data-table">
      <thead>
        <tr>
          {columns.map((column) => <th key={column}>{column}</th>)}
        </tr>
      </thead>
      <tbody>
        {rows.map((row, index) => (
          <tr key={index}>
            {columns.map((column) => <td key={column}>{row[column]}</td>)}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
