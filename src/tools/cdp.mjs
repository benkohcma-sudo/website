// Headless-Chrome driver for checking the built site.
//   node src/tools/cdp.mjs <url> <scriptFile> [screenshot.png] [w] [h]
// The script file runs as an async function body in the page; its return value is printed as JSON.
// Set CDP_RELOAD_SCRIPT=<file> to reload the page afterwards and run a second script.
import { spawn } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
const [url, scriptFile, shot, W = '1440', H = '900'] = process.argv.slice(2);
const CH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const port = 9300 + Math.floor(Math.random() * 500);
const chrome = spawn(CH, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--autoplay-policy=no-user-gesture-required',
  `--remote-debugging-port=${port}`, `--window-size=${W},${H}`, '--user-data-dir=/tmp/cdp-profile-' + port, 'about:blank'], { stdio: 'ignore' });
const sleep = ms => new Promise(r => setTimeout(r, ms));
let ws;
try {
  let targets;
  for (let i = 0; i < 50; i++) { try { targets = await (await fetch(`http://127.0.0.1:${port}/json`)).json(); if (targets.length) break; } catch {} await sleep(200); }
  const page = targets.find(t => t.type === 'page');
  ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise((res, rej) => { ws.onopen = res; ws.onerror = rej; });
  let id = 0; const pending = new Map();
  ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pending.has(m.id)) { pending.get(m.id)(m); pending.delete(m.id); }
    if (m.method === 'Runtime.exceptionThrown') console.error('PAGE ERROR:', m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text);
    if (m.method === 'Runtime.consoleAPICalled' && /error|warn/.test(m.params.type)) console.error('PAGE ' + m.params.type + ':', m.params.args.map(a => a.value ?? a.description).join(' ')); };
  const send = (method, params = {}) => new Promise(res => { const i = ++id; pending.set(i, res); ws.send(JSON.stringify({ id: i, method, params })); });
  await send('Page.enable'); await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride', { width: +W, height: +H, deviceScaleFactor: 1, mobile: false });
  await send('Page.navigate', { url });
  await sleep(2500);
  const run = async (file) => {
    const body = readFileSync(file, 'utf8');
    const r = await send('Runtime.evaluate', { expression: `(async () => { ${body} })()`, awaitPromise: true, returnByValue: true });
    console.log(JSON.stringify(r.result?.result?.value ?? r.result, null, 2));
  };
  await run(scriptFile);
  if (process.env.CDP_FRAMES) {                                    // CDP_FRAMES=<n>:<ms>:<dir> grabs a burst of frames after the script
    const [n, ms, dir] = process.env.CDP_FRAMES.split(':');
    for (let i = 0; i < +n; i++) { const t = Date.now(); const s = await send('Page.captureScreenshot', { format: 'jpeg', quality: 80 }); writeFileSync(`${dir}/f-${String(i).padStart(3, '0')}.jpg`, Buffer.from(s.result.data, 'base64')); await sleep(Math.max(0, +ms - (Date.now() - t))); }
    console.error('frames ->', dir);
  }
  if (shot) { const s = await send('Page.captureScreenshot', { format: 'png' }); writeFileSync(shot, Buffer.from(s.result.data, 'base64')); console.error('screenshot ->', shot); }
  if (process.env.CDP_RELOAD_SCRIPT) { await send('Page.reload', {}); await sleep(3000); console.log('--- after reload ---'); await run(process.env.CDP_RELOAD_SCRIPT); }
} finally { try { ws?.close(); } catch {} chrome.kill(); }
