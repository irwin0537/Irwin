import { getData } from "../lib";

export default async function ScannerPage() {
  const rows = await getData<
    Array<{ name: string; sector: string; trend_score: number; rs_score: number; flow_score: number; total_score: number }>
  >("/api/scanner");

  return (
    <div>
      <h1>Stock Scanner</h1>
      <table className="table card">
        <thead>
          <tr>
            <th>Stock</th><th>Sector</th><th>Trend</th><th>RS</th><th>Flow</th><th>Total</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((r, i) => (
            <tr key={`${r.name}-${i}`}>
              <td>{r.name}</td><td>{r.sector}</td><td>{r.trend_score}</td><td>{r.rs_score}</td><td>{r.flow_score}</td><td className="green">{r.total_score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
