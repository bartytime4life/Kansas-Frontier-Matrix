import type { Metadata } from 'next';
import AssistantWorkspace from './workspace';
export const metadata:Metadata={title:'Ask KFM · PC research assistant',description:'Invited-user research with released KFM evidence and a private PC inference worker.'};
export default function AssistantPage(){return <AssistantWorkspace/>;}
