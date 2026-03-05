import { getData } from "../lib";

export default async function SectorsPage() {
  const sectors = await getData<Array<{ sector: string; sector_strength: number; one_liner: string }>>("/api/sectors");

  return (
    <div>
      <h1>Sector Map</h1>
      <div className="grid">
        {sectors.map((s) => (
          <div className="card" key={s.sector}>
            <h3>{s.sector}</h3>
            <p className="green">Strength: {s.sector_strength}</p>
            <small>{s.one_liner}</small>
          </div>
        ))}
      </div>
    </div>
  );
}
