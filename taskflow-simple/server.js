// 업무 관리 앱 - 의존성 없이 Node 기본 모듈만 쓴다.
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 8000;
const DATA = path.join(__dirname, 'data', 'tasks.json');

function load() {
  try {
    return JSON.parse(fs.readFileSync(DATA, 'utf8'));
  } catch (e) {
    return [];
  }
}

function save(tasks) {
  fs.writeFileSync(DATA, JSON.stringify(tasks, null, 2), 'utf8');
}

function json(res, code, body) {
  res.writeHead(code, { 'Content-Type': 'application/json; charset=utf-8' });
  res.end(JSON.stringify(body));
}

function body(req) {
  return new Promise((resolve) => {
    let raw = '';
    req.on('data', (c) => (raw += c));
    req.on('end', () => {
      try {
        resolve(JSON.parse(raw || '{}'));
      } catch (e) {
        resolve({});
      }
    });
  });
}

const TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
};

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, `http://localhost:${PORT}`);
  const parts = url.pathname.split('/').filter(Boolean);

  // /api/tasks
  if (parts[0] === 'api' && parts[1] === 'tasks') {
    const tasks = load();
    const id = parts[2];

    if (req.method === 'GET' && !id) return json(res, 200, tasks);

    if (req.method === 'POST' && !id) {
      const b = await body(req);
      if (!b.title) return json(res, 400, { error: 'title 이 필요하다' });
      const task = {
        id: Date.now(),
        title: b.title,
        status: 'todo',
        createdAt: new Date().toISOString(),
      };
      tasks.push(task);
      save(tasks);
      return json(res, 201, task);
    }

    if (req.method === 'PUT' && id) {
      const b = await body(req);
      const t = tasks.find((x) => String(x.id) === id);
      if (!t) return json(res, 404, { error: '없는 업무다' });
      if (b.title) t.title = b.title;
      if (b.status) t.status = b.status;
      save(tasks);
      return json(res, 200, t);
    }

    if (req.method === 'DELETE' && id) {
      const i = tasks.findIndex((x) => String(x.id) === id);
      if (i === -1) return json(res, 404, { error: '없는 업무다' });
      tasks.splice(i, 1);
      save(tasks);
      res.writeHead(204);
      return res.end();
    }

    return json(res, 405, { error: '지원하지 않는 방식이다' });
  }

  // 정적 파일
  const file = url.pathname === '/' ? 'index.html' : url.pathname.slice(1);
  const full = path.join(__dirname, 'public', file);
  if (!full.startsWith(path.join(__dirname, 'public'))) {
    res.writeHead(403);
    return res.end();
  }
  fs.readFile(full, (err, data) => {
    if (err) {
      res.writeHead(404);
      return res.end('not found');
    }
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(full)] || 'text/plain' });
    res.end(data);
  });
});

server.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
