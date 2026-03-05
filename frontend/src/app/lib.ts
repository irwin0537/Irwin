const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function getData<T>(path: string): Promise<T> {
  const res = await fetch(`${API_URL}${path}`, { cache: "no-store" });
  if (!res.ok) {
    throw new Error(`Request failed: ${path}`);
  }
  return res.json();
}
