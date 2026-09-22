// 03-design 6번 - 모듈 변수 + DOM 직접 갱신. 상태관리 라이브러리를 쓰지 않는다.
const API = '/api/tasks';
const POLL_MS = 3000; // 03-design 5번 - MVP 는 폴링 3초

let tasks = [];
let editingId = null;

const el = (id) => document.getElementById(id);
const listBox = el('list');
const emptyBox = el('empty');

const BADGE = {
  todo: 'bg-slate-200 text-slate-700 dark:bg-slate-700 dark:text-slate-200',
  in_progress: 'bg-amber-200 text-amber-900 dark:bg-amber-500/30 dark:text-amber-200',
  done: 'bg-emerald-200 text-emerald-900 dark:bg-emerald-500/30 dark:text-emerald-200',
};

// --- 테마 토글 (3.2) -------------------------------------------------------
function syncThemeLabel() {
  const dark = document.documentElement.classList.contains('dark');
  el('theme-label').textContent = dark ? '라이트' : '다크';
}

el('theme-toggle').onclick = () => {
  const root = document.documentElement;
  root.classList.toggle('dark');
  localStorage.setItem('theme', root.classList.contains('dark') ? 'dark' : 'light');
  syncThemeLabel();
};

// --- 시각 변환 -------------------------------------------------------------
// 02-specs - due_at 은 UTC 로 오고 화면에서 로컬로 바꾼다.
function toLocalInput(iso) {
  if (!iso) return '';
  const d = new Date(iso);
  const pad = (n) => String(n).padStart(2, '0');
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}` +
         `T${pad(d.getHours())}:${pad(d.getMinutes())}`;
}

function toUtcIso(local) {
  return local ? new Date(local).toISOString() : null;
}

function remaining(iso) {
  if (!iso) return '';
  const diff = new Date(iso) - new Date();
  const over = diff < 0;
  const mins = Math.floor(Math.abs(diff) / 60000);
  const days = Math.floor(mins / 1440);
  const hh = String(Math.floor((mins % 1440) / 60)).padStart(2, '0');
  const mm = String(mins % 60).padStart(2, '0');
  const body = days > 0 ? `D-${days} ${hh}:${mm}` : `${hh}:${mm}`;
  return over ? `지남 ${body}` : body;
}

// --- 목록 렌더 (3.3) -------------------------------------------------------
function render() {
  listBox.innerHTML = '';
  emptyBox.classList.toggle('hidden', tasks.length > 0);

  for (const t of tasks) {
    const card = document.createElement('article');
    card.className =
      'cursor-pointer rounded-2xl border border-slate-200 bg-white/70 p-4 shadow-lg ' +
      'backdrop-blur transition hover:shadow-xl dark:border-slate-700 ' +
      'dark:bg-slate-800/70';
    card.onclick = (e) => {
      if (e.target.dataset.role !== 'delete') openEdit(t.id);
    };

    const top = document.createElement('div');
    top.className = 'flex items-start justify-between gap-3';

    const title = document.createElement('h3');
    title.className = 'min-w-0 flex-1 break-words text-sm font-medium sm:text-base';
    title.textContent = t.title;
    if (t.status === 'done') title.classList.add('line-through', 'opacity-60');

    const del = document.createElement('button');
    del.type = 'button';
    del.dataset.role = 'delete';
    del.textContent = '휴지통';
    del.className =
      'shrink-0 rounded-lg border border-slate-300 px-2 py-1 text-xs ' +
      'text-slate-500 hover:text-red-600 dark:border-slate-600';
    del.onclick = () => removeTask(t.id, t.title);

    top.append(title, del);

    const meta = document.createElement('div');
    meta.className = 'mt-3 flex flex-wrap items-center gap-2 text-xs';

    const badge = document.createElement('span');
    badge.className = `rounded-full px-2 py-1 font-medium ${BADGE[t.status]}`;
    badge.textContent = t.status;
    meta.appendChild(badge);

    if (t.due_at) {
      const due = document.createElement('span');
      due.className = 'text-slate-500 dark:text-slate-400';
      due.textContent = `마감까지 ${remaining(t.due_at)}`;
      meta.appendChild(due);
    }

    card.append(top, meta);
    listBox.appendChild(card);
  }
}

// --- API ------------------------------------------------------------------
async function load() {
  const res = await fetch(API);
  if (!res.ok) return;
  tasks = await res.json();
  render();
}

el('add-form').onsubmit = async (e) => {
  e.preventDefault();
  const title = el('f-title').value.trim();
  if (!title) return;
  const res = await fetch(API, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      title,
      status: el('f-status').value,
      due_at: toUtcIso(el('f-due').value),
    }),
  });
  if (res.ok) {
    el('add-form').reset();
    load();
  }
};

async function removeTask(id, title) {
  if (!confirm(`"${title}" 을 지운다.`)) return;
  const res = await fetch(`${API}/${id}`, { method: 'DELETE' });
  if (res.ok) load();
}

// --- 수정 모달 (3.5) -------------------------------------------------------
async function openEdit(id) {
  const res = await fetch(`${API}/${id}`);
  if (!res.ok) return;
  const t = await res.json();
  editingId = id;
  el('e-title').value = t.title;
  el('e-desc').value = t.description || '';
  el('e-due').value = toLocalInput(t.due_at);
  el('e-status').value = t.status;
  el('edit-backdrop').classList.replace('hidden', 'flex');
}

function closeEdit() {
  editingId = null;
  el('edit-backdrop').classList.replace('flex', 'hidden');
}

el('e-cancel').onclick = closeEdit;

el('edit-form').onsubmit = async (e) => {
  e.preventDefault();
  const res = await fetch(`${API}/${editingId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      title: el('e-title').value.trim(),
      description: el('e-desc').value.trim() || null,
      status: el('e-status').value,
      due_at: toUtcIso(el('e-due').value),
    }),
  });
  if (res.ok) {
    closeEdit();
    load();
  }
};

// --- 시작 ------------------------------------------------------------------
syncThemeLabel();
load();
setInterval(load, POLL_MS);
