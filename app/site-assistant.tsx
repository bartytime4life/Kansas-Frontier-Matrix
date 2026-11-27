'use client';
import {Suspense,useState} from 'react';
import {createPortal} from 'react-dom';
import {usePathname,useSearchParams} from 'next/navigation';
import {assistantSurfaceForPath} from './assistant-surfaces.mjs';
import AssistantPanel from './assistant-panel';
import {BUILD_UTC_YEAR} from './build-clock';
import type {AssistantFocus} from './assistant-context';
import styles from './assistant-panel.module.css';
export function PageAssistant({inlineQuestion}:{inlineQuestion?:string}={}){
 const pathname=usePathname(),params=useSearchParams(),[dialog,setDialog]=useState<{draftQuestion?:string}|null>(null);
 const surface=assistantSurfaceForPath(pathname??'');
 const inline=inlineQuestion!==undefined;
 if(!surface||(surface.id==='archive-search')!==inline)return null;
 const recordId=surface.id==='knowledge-record'?params.get('id'):null;
 const focus:AssistantFocus={title:surface.title,detail:inline?'Review and edit the question before sending. Archive results and OCR snippets stay on the search page.':'Public page context only. Private form values, uploads and account information are not sent.',context:{version:1,frame:BUILD_UTC_YEAR,view:'Page',layers:[],surface:surface.id,selection:recordId&&/^[a-zA-Z0-9][a-zA-Z0-9._:-]{0,127}$/.test(recordId)?{kind:'knowledge',recordId}:null}};
 const panel=dialog&&<AssistantPanel focus={focus} {...dialog} onClose={()=>setDialog(null)}/>;
 return <><button type='button' className={inline?undefined:styles.trigger} aria-haspopup='dialog' aria-expanded={dialog!==null} onClick={()=>setDialog({draftQuestion:inlineQuestion})}>{inline?'Ask KFM for search terms':<>Ask KFM<small>About {surface.title.toLowerCase()}</small></>}</button>{inline&&panel?createPortal(panel,document.body):panel}</>;
}
export default function SiteAssistant(){return <Suspense fallback={null}><PageAssistant/></Suspense>;}
