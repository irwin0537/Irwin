import { getData } from "../lib";

export default async function TradePlannerPage() {
  const plans = await getData<
    Array<{ name: string; action: string; planned_position_pct: number; entry_condition: string; stop_loss: string }>
  >("/api/trade-plan");

  return (
    <div>
      <h1>Trade Planner</h1>
      <div className="grid">
        {plans.map((p, i) => (
          <div className="card" key={`${p.name}-${i}`}>
            <h3>{p.name}</h3>
            <p>Action: {p.action}</p>
            <p>Position: {p.planned_position_pct}%</p>
            <p>Entry: {p.entry_condition}</p>
            <p className="red">Stop Loss: {p.stop_loss}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
