"use client";
import {useEffect,useRef,useState,type ComponentProps} from 'react';
type WorkspaceModule=typeof import('./workspace');
let loaded:WorkspaceModule|null=null;
let pending:Promise<WorkspaceModule>|null=null;
function loadWorkspace(){
 if(loaded)return Promise.resolve(loaded);
 if(!pending)pending=import('./workspace').then(module=>{loaded=module;return module;}).finally(()=>{pending=null;});
 return pending;
}
// The map imports this small shell only. Once opened, keep the workspace mounted
// so hiding it preserves drafts; its existing active prop stops background work.
export default function AssistantLoader(props:ComponentProps<WorkspaceModule['default']>){
 const [module,setModule]=useState<WorkspaceModule|null>(null);
 const [failed,setFailed]=useState(false),[attempt,setAttempt]=useState(0);
 const ownsLoadingFocus=useRef(false);
 useEffect(()=>{
  if(!props.active||module)return;
  let current=true;
  void loadWorkspace().then(value=>{if(current){setModule(value);setFailed(false);}},()=>{if(current)setFailed(true);});
  return ()=>{current=false;};
 },[props.active,module,attempt]);
 useEffect(()=>{
  if(module&&props.active&&ownsLoadingFocus.current&&document.activeElement===document.body)props.inputRef?.current?.focus({preventScroll:true});
  if(module||!props.active)ownsLoadingFocus.current=false;
 },[module,props.active,props.inputRef]);
 if(module){const Workspace=module.default;return <Workspace {...props}/>;}
 if(!props.active)return null;
 return <div aria-busy={!failed} onFocusCapture={()=>{ownsLoadingFocus.current=true;}}
  onBlurCapture={event=>{if(event.relatedTarget instanceof Node&&!event.currentTarget.contains(event.relatedTarget))ownsLoadingFocus.current=false;}}>
  <p tabIndex={-1} data-assistant-loading role={failed?'alert':'status'}>{failed?'Chat could not load. You can keep exploring the map.':'Opening Chat with KFM…'}</p>
  {failed&&<button type="button" onClick={()=>{setFailed(false);setAttempt(value=>value+1);}}>Retry chat</button>}
 </div>;
}
