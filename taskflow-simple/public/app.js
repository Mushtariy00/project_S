const list = document.getElementById('list');
const empty = document.getElementById('empty');
const form = document.getElementById('add-form');
const title = document.getElementById('title');

const STATUS = ['todo', 'in_progress', 'done'];

async function load() {
  const res = await fetch('/api/tasks');
  const tasks = await res.json();
  render(tasks);
}

function render(tasks) {
  list.innerHTML = '';
  empty.style.display = tasks.length ? 'none' : 'block';
  for (const t of tasks) {
    const li = document.createElement('li');
    if (t.status === 'done') li.className = 'done';

    const span = document.createElement('span');
    span.className = 'title';
    span.textContent = t.title;

    const sel = document.createElement('select');
    for (const s of STATUS) {
      const opt = document.createElement('option');
      opt.value = s;
      opt.textContent = s;
      if (s === t.status) opt.selected = true;
      sel.appendChild(opt);
    }
    sel.onchange = () => update(t.id, { status: sel.value });

    const del = document.createElement('button');
    del.textContent = '삭제';
    del.onclick = () => remove(t.id);

    li.append(span, sel, del);
    list.appendChild(li);
  }
}

async function update(id, patch) {
  await fetch('/api/tasks/' + id, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(patch),
  });
  load();
}

async function remove(id) {
  await fetch('/api/tasks/' + id, { method: 'DELETE' });
  load();
}

form.onsubmit = async (e) => {
  e.preventDefault();
  if (!title.value.trim()) return;
  await fetch('/api/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title: title.value.trim() }),
  });
  title.value = '';
  load();
};

load();
