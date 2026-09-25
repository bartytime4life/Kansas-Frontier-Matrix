import Link from "next/link";
import { requireChatGPTUser } from "../chatgpt-auth";
import { intakeUser } from "../data-intake-server";
import DataWorkspace from "../data/workspace";
export const dynamic = "force-dynamic";
export default async function StewardsPage() {
  await requireChatGPTUser("/stewards"); const user = await intakeUser();
  if (!user.steward) return <main style={{ maxWidth: 640, margin: "10vh auto", padding: 24 }}><h1>Steward desk</h1><p>This queue is available to assigned KFM stewards. You can track your own proposals in Data commons.</p><Link href="/data">Your submissions</Link> · <Link href="/">Back to map</Link></main>;
  return <DataWorkspace mode="review" name={user.name} steward />;
}
