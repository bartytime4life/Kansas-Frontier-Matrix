import { requireChatGPTUser } from "../../chatgpt-auth";
import { intakeUser } from "../../data-intake-server";
import { localSignInNotice } from "../../local-signin-notice";
import LandWorkspace from "./workspace";
export const dynamic="force-dynamic";
export default async function LandPage({searchParams}:{searchParams:Promise<{submission?:string}>}){
  const notice=await localSignInNotice("/data/land-records");if(notice)return notice;
  await requireChatGPTUser("/data/land-records");const user=await intakeUser(),p=await searchParams;
  const initialId=typeof p.submission==="string"&&/^[0-9a-f-]{36}$/.test(p.submission)?p.submission:"";
  return <LandWorkspace name={user.name} steward={user.steward} initialId={initialId}/>;
}
