import Link from "next/link";

const items = [
  ["/dashboard", "Dashboard"],
  ["/sectors", "Sector Map"],
  ["/scanner", "Stock Scanner"],
  ["/trade-planner", "Trade Planner"],
  ["/risk", "Portfolio Risk"],
  ["/review", "Review"],
] as const;

export function Sidebar() {
  return (
    <aside className="sidebar">
      <h2>AI Trading OS</h2>
      {items.map(([href, label]) => (
        <Link className="nav-item" href={href} key={href}>
          {label}
        </Link>
      ))}
    </aside>
  );
}
