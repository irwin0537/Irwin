import { getData } from "../lib";

export default async function ReviewPage() {
  const review = await getData<{
    plan_adherence: string;
    good: string;
    bad: string;
    fixes: string;
    tomorrow_focus: string;
  }>("/api/review");

  return (
    <div>
      <h1>Review System</h1>
      <div className="card">
        <p>Plan Adherence: <strong>{review.plan_adherence}</strong></p>
        <p>✅ Good: {review.good}</p>
        <p>❌ Bad: {review.bad}</p>
        <p>🔧 Fixes: {review.fixes}</p>
        <p>🎯 Tomorrow Focus: {review.tomorrow_focus}</p>
      </div>
    </div>
  );
}
