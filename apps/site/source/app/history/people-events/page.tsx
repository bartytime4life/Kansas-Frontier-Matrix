import s from "../../downloads/workspace.module.css";
import h from "../../history-research.module.css";

export default function PeopleEventsResearch() {
  return <main className={s.page}><div className={`${s.wrap} ${h.wrap}`}>
    <nav className={h.navigation} aria-label="History navigation"><a href="/downloads#history">← History &amp; archives</a><a href="/knowledge">Reviewed KFM knowledge</a></nav>
    <header className={h.intro}><p className={s.eyebrow}>KANSAS HISTORY</p><h1>People, events &amp; historical context</h1></header>
    <p className={s.alert} role="status">This catalogue is unavailable pending review and approval for public release.</p>
    <p>Research entries and downloads will remain unavailable until rights, sensitivity, evidence and release reviews are complete.</p>
    <p>You can explore the history source directory, read the 1909 Kansas history book, or search reviewed KFM knowledge.</p>
    <p><a href="/history/prentis-1909">Read &amp; search the book →</a></p>
  </div></main>;
}
