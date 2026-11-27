'use client';
import {useEffect,useRef} from 'react';
import {createPortal} from 'react-dom';
import AssistantWorkspace from './assistant/loader';
import type {AssistantFocus} from './assistant-context';
import styles from './assistant-panel.module.css';
export default function AssistantPanel({focus,onClose,draftQuestion,portal=false}:{focus:AssistantFocus;onClose:()=>void;draftQuestion?:string;portal?:boolean}){
 const dialog=useRef<HTMLDialogElement>(null);
 useEffect(()=>{
  const prior=document.activeElement instanceof HTMLElement?document.activeElement:null;
  if(!dialog.current?.open)dialog.current?.showModal();
  return()=>{if(prior?.isConnected)prior.focus({preventScroll:true});};
 },[]);
 const panel=<dialog ref={dialog} className={styles.panel} aria-label='KFM page assistant' onCancel={event=>{event.preventDefault();onClose();}}>
  <header><h2>Ask KFM</h2><button type='button' autoFocus onClick={onClose} aria-label='Close page assistant'>Close</button></header>
  <AssistantWorkspace active focus={focus} draftRequest={draftQuestion?{id:1,value:draftQuestion,intent:'explore'}:undefined}/>
 </dialog>;
 return portal?createPortal(panel,document.body):panel;
}
