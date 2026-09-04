#!/usr/bin/env python3
"""Copy-preservation check: every sentence of text in the crawled content must appear in the built page."""
import os, re, json, html, sys
from bs4 import BeautifulSoup
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))
from build import out_path
P = json.load(open(os.path.join(ROOT, 'src/content/pages.json')))
def norm(t): return re.sub(r'\s+', ' ', html.unescape(t)).replace('\xa0',' ').strip()
def sentences(txt):
    out = []
    for line in txt.split('\n'):
        for s in re.split(r'(?<=[.!?])\s+| I ', line):
            s = norm(s)
            if len(s) > 25: out.append(s)
    return out
bad = 0; checked = 0
for page in P:
    src = BeautifulSoup(page['content'], 'lxml').get_text('\n')
    dst = norm(BeautifulSoup(open(out_path(page['url']), encoding='utf-8').read(), 'lxml').get_text(' '))
    missing = [s for s in set(sentences(src)) if s not in dst]
    missing += [norm(s) for s in [page.get('h1','')] if s and norm(s) not in dst]
    checked += 1
    if missing:
        bad += 1; print('MISSING in', page['url'], '->', [m[:80] for m in missing[:4]])
print(f'{checked} pages checked, {bad} with missing copy')
