'use client';
import {Suspense,useState} from 'react';
import {usePathname,useSearchParams} from 'next/navigation';
import {assistantSurfaceForPath} from './assistant-surfaces.mjs';
import AssistantPanel from './assistant-panel';
import {BUILD_UTC_YEAR} from './build-clock';
import type {AssistantFocus} from './assistant-context';
import styles from './assistant-panel.module.css';
export function PageAssistant(){
 const pathname=usePathname(),params=useSearchParams(),[open,setOpen]=useState(false);
 const surface=assistantSurfaceForPath(pathname??'');
 if(!surface)return null;
 const recordId=surface.id==='knowledge-record'?params.get('id'):null;
 const focus:AssistantFocus={title:surface.title,detail:'Public page context only. Private form values, uploads and account information are not sent.',context:{version:1,frame:BUILD_UTC_YEAR,view:'Page',layers:[],surface:surface.id,selection:recordId&&/^[a-zA-Z0-9][a-zA-Z0-9._:-]{0,127}$/.test(recordId)?{kind:'knowledge',recordId}:null}};
 return <><button type='button' className={styles.trigger} aria-haspopup='dialog' aria-expanded={open} onClick={()=>setOpen(true)}>Ask KFM<small>About {surface.title.toLowerCase()}</small></button>{open&&<AssistantPanel focus={focus} onClose={()=>setOpen(false)}/>}</>;
}
export default function SiteAssistant(){return <Suspense fallback={null}><PageAssistant/></Suspense>;}
