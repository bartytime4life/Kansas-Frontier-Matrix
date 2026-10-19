'use client';
import {useEffect,useRef} from 'react';
import AssistantWorkspace from './assistant/workspace';
import type {AssistantFocus} from './assistant-context';
import styles from './assistant-panel.module.css';
export default function AssistantPanel({focus,onClose}:{focus:AssistantFocus;onClose:()=>void}){
 const dialog=useRef<HTMLDialogElement>(null);
 useEffect(()=>{
  const prior=document.activeElement instanceof HTMLElement?document.activeElement:null;
  if(!dialog.current?.open)dialog.current?.showModal();
  return()=>{if(prior?.isConnected)prior.focus({preventScroll:true});};
 },[]);
 return <dialog ref={dialog} className={styles.panel} aria-label='KFM page assistant' onCancel={event=>{event.preventDefault();onClose();}}>
  <header><h2>Ask KFM</h2><button type='button' autoFocus onClick={onClose} aria-label='Close page assistant'>Close</button></header>
  <AssistantWorkspace focus={focus}/>
 </dialog>;
}
