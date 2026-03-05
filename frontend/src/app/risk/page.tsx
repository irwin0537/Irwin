import { getData } from "../lib";

export default async function RiskPage() {
  const risk = await getData<{
    risk_level: string;
    accountA_exposure: number;
    accountB_exposure: number;
    drawdown_today_pct: number;
    action_suggestion: string;
  }>("/api/risk");

  return (
    <div>
      <h1>Portfolio Risk</h1>
      <div className="grid">
        <div className="card"><p>Risk Level</p><h2>{risk.risk_level}</h2></div>
        <div className="card"><p>Account A Exposure</p><h2>{risk.accountA_exposure}%</h2></div>
        <div className="card"><p>Account B Exposure</p><h2>{risk.accountB_exposure}%</h2></div>
        <div className="card"><p>Today Drawdown</p><h2 className="red">{risk.drawdown_today_pct}%</h2></div>
      </div>
      <div className="card" style={{ marginTop: 16 }}>
        <h3>Action Suggestion</h3>
        <p>{risk.action_suggestion}</p>
      </div>
    </div>
  );
}
