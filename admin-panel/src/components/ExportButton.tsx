export default function ExportButton(){
  function exportReport(){
    window.print();
  }

  return <button onClick={exportReport}>Export Report</button>;
}
