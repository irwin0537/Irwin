import { getData } from "../lib";

export default async function DashboardPage() {
  const market = await getData<{
    market_regime: string;
    risk_level: string;
    recommended_exposure: number;
    summary: string;
  }>("/api/market");

  return (
    <div>
      <h1>Market Dashboard</h1>
      <div className="grid">
        <div className="card">
          <p>Market Regime</p>
          <h2 className="green">{market.market_regime}</h2>
        </div>
        <div className="card">
          <p>Risk Level</p>
          <h2>{market.risk_level}</h2>
        </div>
        <div className="card">
          <p>Recommended Exposure</p>
          <h2>{market.recommended_exposure}%</h2>
        </div>
      </div>
      <div className="card" style={{ marginTop: 16 }}>
        <h3>AI Summary</h3>
        <p>{market.summary}</p>
      </div>
    </div>
  );
}
