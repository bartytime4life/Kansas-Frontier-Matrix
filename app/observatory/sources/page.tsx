import Link from "next/link";
export const metadata = { title: "Released archive availability" };
export default function Page() {
 return <main style={{ maxWidth: 780, margin: "40px auto", padding: 24, lineHeight: 1.65 }}>
  <Link href="/">← Explorer</Link><h1>Released archive availability</h1>
  <p role="status">Historical archive delivery is held pending an approved public projection and integration of its date-selected views.</p>
  <p>The public preview will not query private archives or substitute current provider responses for missing historical dates. Reviewed water and weather packages retain their own observation dates in the Explorer.</p>
 </main>;
}
