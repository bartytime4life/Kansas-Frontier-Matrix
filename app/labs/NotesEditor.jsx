'use client';

import { MAX_NOTE_CHARACTERS } from './notebook.mjs';
import styles from './NotesEditor.module.css';

const PROMPTS = 'Question:\n\nObservations:\n\nLimits and uncertainty:\n\nNext check:\n';

export default function NotesEditor({ id, value, onChange, autoFocus = false }) {
  return <div className={styles.editor}>
    <div className={styles.heading}><label htmlFor={id}>Research notes <span>optional · plain text</span></label><span aria-live="polite">{value.length.toLocaleString('en-US')} / {MAX_NOTE_CHARACTERS.toLocaleString('en-US')}</span></div>
    <p id={`${id}-prompts`} className={styles.prompts}>Keep the question, what you observed, the limits or uncertainty, and what you would check next.</p>
    <textarea id={id} value={value} maxLength={MAX_NOTE_CHARACTERS} rows={6} onChange={event => onChange(event.target.value)} autoFocus={autoFocus} aria-describedby={`${id}-prompts ${id}-privacy`} placeholder={'Question:\nObservations:\nLimits and uncertainty:\nNext check:'}/>
    <div className={styles.foot}><p id={`${id}-privacy`}>Browser-local notes travel in notebook JSON exports and imports. They are excluded from public view links.</p>{!value.trim() && <button type="button" onClick={() => onChange(PROMPTS)}>Use research prompts +</button>}</div>
  </div>;
}
