'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const page = document.body.dataset.page;
  let user = null, token = '', recovery = null, setup = false, busy = false;
  const requestIds = new WeakMap();
  const messages = {
    SIGN_IN_REQUIRED: 'Please sign in to this private Studio.',
    INVALID_USERNAME_OR_PASSWORD: 'The username or password is incorrect.',
    SIGN_IN_TEMPORARILY_LIMITED: 'Sign-in is temporarily limited after repeated failures. Try again later.',
    SETUP_CODE_INVALID_OR_EXPIRED: 'The setup code is invalid or expired. Generate a new code on this PC.',
    LAST_ACTIVE_ADMIN_MUST_REMAIN: 'Keep at least one enabled administrator with a permanent password. Use My account to change your own password.',
    CURRENT_PASSWORD_INCORRECT: 'Your current password did not match.',
    STORAGE_CHANGED_RELOAD_AND_RETEST: 'The drive identity record changed. Reload it and record a new check.',
    CURRENT_PASS_EVIDENCE_REQUIRED: 'Review requires a passing observation for the current drive identities.',
    READ_ONLY_ACCOUNT: 'This account has read-only access.',
    ADMIN_REQUIRED: 'An administrator account is required for this action.',
    POSITIVE_DEVICE_IDENTITY_REQUIRED: 'Record both drives’ serials, UUIDs, filesystems and mountpoints before a passing check.',
    CAPACITY_FLOOR_NOT_ESTABLISHED: 'Record capacity, available bytes and reserve floors for both drives; available space must meet the floor.'
  };
  function say(text) { (page === 'sign-in' ? $('sign-message') : $('notice')).textContent = text; }
  function element(tag, text, parent) { const e = document.createElement(tag); if (text !== undefined) e.textContent = String(text); if (parent) parent.append(e); return e; }
  function value(form, key) { return form.elements.namedItem(key).value; }
  function setBusy(flag) { busy = flag; document.querySelectorAll('form button').forEach(b => { b.disabled = flag; }); }
  async function api(path, body) {
    const response = await fetch(path, {method: body === undefined ? 'GET' : 'POST', credentials:'same-origin', cache:'no-store', redirect:'error',
      headers: {...(body === undefined ? {} : {'Content-Type':'application/json'}), ...(token ? {'X-KFM-CSRF':token} : {})},
      ...(body === undefined ? {} : {body:JSON.stringify(body)})});
    if (!response.ok) {
      const problem = await response.json().catch(() => ({}));
      if (problem.error === 'PASSWORD_CHANGE_REQUIRED') location.assign('/account/password');
      if (response.status === 401 && page !== 'sign-in') location.assign('/sign-in');
      throw new Error(messages[problem.error] || problem.error || `Request failed (${response.status}).`);
    }
    return response;
  }
  async function perform(fn) { if (busy) return; setBusy(true); try { await fn(); } catch(error) { say(error.message); } finally { setBusy(false); } }
  function fields(form) { return Object.fromEntries(new FormData(form)); }
  function requestId(form) { if (!requestIds.has(form)) requestIds.set(form, crypto.randomUUID()); return requestIds.get(form); }
  function completed(form) { requestIds.delete(form); }
  function wireForm(id, action) { $(id).addEventListener('submit', event => {event.preventDefault(); perform(() => action(event.currentTarget));}); }
  async function download(path, name) {
    const response = await api(path), blob = await response.blob(), url = URL.createObjectURL(blob);
    const link = element('a'); link.href = url; link.download = name; document.body.append(link); link.click(); link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  function renderTable(id, headers, rows) {
    const box=$(id);box.replaceChildren();const table=element('table',undefined,box);
    const head=element('tr',undefined,element('thead',undefined,table));headers.forEach(h => {element('th',h,head).scope='col';});
    const body=element('tbody',undefined,table); rows.forEach(row => {const tr=element('tr',undefined,body);row.forEach(cell=>element('td',cell,tr));});
  }
  function deviceFields() {
    const host=$('device-fields'); host.replaceChildren();
    for (const role of ['source','backup']) {
      const fs=element('fieldset',undefined,host); element('legend',role==='source'?'Main source drive':'Backup destination',fs);
      for (const [key,label] of [['label','Label'],['serial','Serial'],['uuid','Filesystem UUID'],['filesystem','Filesystem'],['mountpoint','Verified mount path'],['device','Observed device path'],['lvmMembers','LVM / physical-member evidence'],['totalBytes','Total bytes'],['freeBytes','Free bytes'],['floorBytes','Minimum reserve bytes']]) {
        const l=element('label',label,fs),input=element('input',undefined,l);input.name=role+'.'+key;
        input.maxLength=key.endsWith('Bytes')?19:2000;
        if (key.endsWith('Bytes')) {input.inputMode='numeric';input.pattern='[0-9]*';}
      }
    }
  }
  function renderRecovery() {
    const summary=$('drive-summary');summary.replaceChildren();
    for (const role of ['source','backup']) {
      const d=recovery.storage?.[role] || {},card=element('article',undefined,summary);card.className='drive';
      element('h2',role==='source'?'Main source':'Backup destination',card);
      element('p',d.label || recovery.intendedRoles[role],card);
      const dl=element('dl',undefined,card);
      for (const [label,key] of [['Serial','serial'],['UUID','uuid'],['Mount','mountpoint'],['Filesystem','filesystem'],['Free bytes','freeBytes'],['Reserve','floorBytes']]) {element('dt',label,dl);element('dd',d[key]??'Not recorded',dl);}
      element('small','Storage record '+recovery.storageRevision+' · operator-recorded, not live inspection',card);
    }
    const gates=$('gates');gates.replaceChildren();const select=$('gate-select');select.replaceChildren();
    recovery.gates.forEach((g,index) => {
      const row=element('article',undefined,gates);row.className='checkpoint';element('span',String(index+1).padStart(2,'0'),row).className='checkpoint-number';
      const content=element('div',undefined,row);element('strong',g.title,content);element('p',g.expected,content);element('span',g.status.replaceAll('_',' '),content).className='badge';
      if(g.observation)element('small',' · observation #'+g.observation,content);
      const button=element('button','Record check',row);button.type='button';button.disabled=user.role==='viewer';
      button.addEventListener('click',()=> {select.value=g.id;$('recovery-form').elements.namedItem('expected').value=g.expected;$('recovery-check').scrollIntoView({behavior:'auto',block:'start'});});
      const option=element('option',g.title,select);option.value=g.id;
    });
    const plans=$('plans');plans.replaceChildren();for(const plan of recovery.plans) {
      const details=element('details',undefined,plans);element('summary',plan.title,details);element('pre',plan.command,details);element('p',plan.scope,details);
      const copy=element('button','Copy plan—not execute',details);copy.type='button';copy.addEventListener('click',()=>perform(async()=>{await navigator.clipboard.writeText(plan.command);say('Command plan copied. Nothing was executed.');}));
    }
    const history=$('recovery-history');history.replaceChildren();
    for(const item of recovery.events.slice(-100).reverse()) {
      const entry=element('article',undefined,history);entry.className='history-entry';const e=item.event;
      element('strong',`#${item.sequence} · ${e.kind} · ${e.actor}`,entry);element('p',`Observed ${e.observedAt} · recorded ${e.recordedAt}`,entry);
      element('p',e.observed || e.reason || e.notes || 'Drive identities recorded',entry);
      if(e.risk)element('p','Risk: '+e.risk,entry);
      const detail=element('details',undefined,entry);element('summary','Full evidence record',detail);element('pre',JSON.stringify(item,null,2),detail);
    }
    if(!recovery.events.length)element('p','No recovery records yet. Nothing has been verified or restored.',history);
    $('storage-details').hidden=user.role!=='admin';$('recovery-review').hidden=user.role!=='admin';
    if(user.role==='viewer')$('recovery-form').hidden=true;
  }
  async function loadRecovery() { recovery=await(await api('/api/recovery/state')).json();renderRecovery(); }
  async function loadUsers() {
    const data=await(await api('/auth/users')).json();renderTable('user-table',['Username','Role','Enabled','Password'],data.users.map(u=>[u.username,u.role,u.enabled?'Yes':'No',u.must_change?'Must change':'Set—not readable']));
    const data2=await(await api('/auth/audit')).json();const audit=$('audit');audit.replaceChildren();
    for(const e of data2.events)element('p',`${new Date(e.at*1000).toISOString()} · ${e.actor} · ${e.action} · ${e.target}`,audit);
  }
  wireForm('login-form',async form=> {
    const data={username:value(form,'username'),password:value(form,'password')};
    if(setup)data.setupCode=value(form,'setupCode');
    const result=await(await api(setup?'/auth/bootstrap':'/auth/login',data)).json();
    form.reset();
    if(setup){setup=false;$('setup-label').hidden=true;$('setup-help').hidden=true;$('login-button').textContent='Sign in';$('sign-title').textContent='Owner account created.';say('Sign in with your new local account.');}
    else location.assign(result.next);
  });
  wireForm('password-form',async form=> {
    if(value(form,'newPassword')!==value(form,'repeat'))throw new Error('The new passphrases do not match.');
    await api('/auth/password',{currentPassword:value(form,'currentPassword'),newPassword:value(form,'newPassword')});form.reset();location.assign('/sign-in');
  });
  wireForm('user-form',async form=> {
    const data=fields(form);
    if(data.action==='update'){delete data.password;data.enabled=data.enabled==='true';}
    else {delete data.enabled;if(data.action==='reset')delete data.role;}
    await api('/auth/users',data);form.reset();$('user-action').dispatchEvent(new Event('change'));await loadUsers();say('Account change saved. Existing sessions were revoked where applicable.');
  });
  $('user-action').addEventListener('change',()=>{
    const action=$('user-action').value; $('temporary-label').hidden=action==='update';$('enabled-label').hidden=action!=='update';
    $('user-form').elements.namedItem('password').required=action!=='update';
  });
  wireForm('storage-form',async form=> {
    const data=fields(form),devices={source:{},backup:{}};
    for(const role of ['source','backup'])for(const key of ['label','serial','uuid','filesystem','mountpoint','device','lvmMembers','totalBytes','freeBytes','floorBytes']){
      const raw=data[role+'.'+key];devices[role][key]=key.endsWith('Bytes')?(raw===''?null:Number(raw)):raw;
      if(key.endsWith('Bytes')&&raw!==''&&!Number.isSafeInteger(devices[role][key]))throw new Error('Capacity must be an exact whole-byte integer within JavaScript safe integer range.');
    }
    await api('/api/recovery/events',{kind:'storage',requestId:requestId(form),observedAt:data.observedAt,devices,notes:data.notes});completed(form);await loadRecovery();say('Drive-identity record saved. Earlier checks remain historical; current checks require this revision.');
  });
  wireForm('recovery-form',async form=> {
    const data=fields(form);data.storageRevision=recovery.storageRevision;data.retestOf=data.retestOf?Number(data.retestOf):null;
    await api('/api/recovery/events',{...data,kind:'observation',requestId:requestId(form)});completed(form);await loadRecovery();say('Observation saved under your signed-in identity. It does not authorize recovery.');
  });
  wireForm('recovery-review',async form=> {
    const data=fields(form);data.observation=Number(data.observation);
    await api('/api/recovery/events',{...data,kind:'review',requestId:requestId(form)});completed(form);await loadRecovery();say('Scoped evidence review saved. Disk commands and restores remain disabled.');
  });
  // Edits after an attempted save create a new idempotency identity, never silently reuse a conflicting one.
  for(const id of ['storage-form','recovery-form','recovery-review'])$(id).addEventListener('input',()=>requestIds.delete($(id)));
  $('logout').addEventListener('click',()=>perform(async()=>{await api('/auth/logout',{});token='';location.assign('/sign-in');}));
  $('recovery-export').addEventListener('click',()=>perform(()=>download('/api/recovery/export','kfm-recovery-evidence.json')));
  (async()=>{
    if(page==='sign-in') {
      $('signin').hidden=false;
      try {setup=(await(await api('/auth/status')).json()).setupRequired;if(setup){$('sign-title').textContent='Create your owner account.';$('sign-description').textContent='First-time setup requires the one-time code generated on this PC.';$('setup-label').hidden=false;$('setup-help').hidden=false;$('login-button').textContent='Create owner account';$('login-form').elements.namedItem('password').minLength=15;$('login-form').elements.namedItem('password').autocomplete='new-password';}}
      catch(e){say(e.message);}
      return;
    }
    try {
      const session=await(await api('/auth/session')).json();user=session.user;token=session.csrf;
      $('workspace').hidden=false;$('current-user').textContent=user.username+' · '+user.role;$('users-nav').hidden=user.role!=='admin';
      for(const n of document.querySelectorAll('[data-nav]'))if(n.dataset.nav===page)n.setAttribute('aria-current','page');
      const titles={studio:'Overview',recovery:'Backup & recovery',users:'Users & access','account/password':'My account'};$('breadcrumb').textContent='STUDIO / '+(titles[page]||'Overview').toUpperCase();
      if(page==='recovery'){ $('recovery-view').hidden=false;deviceFields();await loadRecovery();
        if(recovery.storage)for(const role of ['source','backup'])for(const [key,val] of Object.entries(recovery.storage[role])){const field=$('storage-form').elements.namedItem(role+'.'+key);if(field)field.value=val??'';}
      }else if(page==='users'){ $('users-view').hidden=false;await loadUsers(); }
      else if(page==='account/password'){ $('account-view').hidden=false;if(user.mustChangePassword)$('password-guidance').textContent='Change your temporary password before opening private records. Your current session cannot access them yet.'; }
      else { $('overview-view').hidden=false;const data=await(await api('/api/recovery/state')).json();$('recovery-count').textContent=data.gates.filter(g=>g.status==='REVIEWED_EVIDENCE').length+' / 7';$('role-summary').textContent='Signed in as '+user.role+'. Access is enforced by the server.';const ws=session.workspace||{};$('workspace-state').textContent=ws.workingData?'Connected':'Not connected';$('workspace-summary').textContent=ws.workingData?('Held reviews can be sent to Working Data.'+(ws.library?' Library mounted.':'')):'Send to KFM is off. On this PC run studio-admin.sh workspace setup, then restart Studio.'; }
    } catch(error){say(error.message);}
  })();
})();
