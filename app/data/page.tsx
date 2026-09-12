import { requireChatGPTUser } from "../chatgpt-auth";
import { intakeUser } from "../data-intake-server";
import DataWorkspace from "./workspace";
export const dynamic = "force-dynamic";
export default async function DataPage({ searchParams }: { searchParams: Promise<{ source?: string }> }) {
  const params = await searchParams;
  const source = typeof params.source === "string" ? params.source : "";
  return <SignedInData returnTo={source ? `/data?source=${encodeURIComponent(source)}` : "/data"} />;
}
async function SignedInData({ returnTo }: { returnTo: string }) {
  await requireChatGPTUser(returnTo);
  const user = await intakeUser();
  return <DataWorkspace mode="submit" name={user.name} steward={user.steward} />;
}
