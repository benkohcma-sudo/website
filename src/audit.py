#!/usr/bin/env python3
"""Layout audit over dist/: finds pages where flat CMS markup leaked through as raw lists,
forms, headings or widgets, plus broken local asset references."""
import os, re, sys, json
from collections import Counter, defaultdict
from bs4 import BeautifulSoup
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); DIST = os.path.join(ROOT, 'dist')
issues = defaultdict(list)
def main_of(soup):
    m = soup.find('main'); return m if m else soup
for dp, _, files in os.walk(DIST):
    for fn in files:
        if fn != 'index.html': continue
        path = os.path.join(dp, fn); url = '/' + os.path.relpath(dp, DIST).replace(os.sep, '/').rstrip('.') ; url = '/' if url == '/.' else url
        html = open(path, encoding='utf-8').read(); soup = BeautifulSoup(html, 'lxml'); main = main_of(soup)
        prose = main.select('.prose')
        # 1. raw pagination lists (links to ?page= or /page/N inside a plain <ul>)
        for ul in main.find_all('ul'):
            links = ul.find_all('a', href=True)
            if links and sum(1 for a in links if re.search(r'(\?page=|/page/)\d+', a['href'])) >= 2 and not ul.find_parent(class_='pagination'):
                issues['raw pagination list'].append(url); break
        # 2. raw search widgets / Categories widgets
        if main.find('input', attrs={'type': 'search'}) and not main.select('.blog-search'): issues['raw search form'].append(url)
        if any(h.get_text(strip=True) == 'Categories' for h in main.find_all(['h2', 'h3'])) and not main.select('.blog-cats'): issues['raw Categories widget'].append(url)
        # 3. headings problems
        h1s = soup.find_all('h1')
        if len(h1s) != 1: issues[f'{len(h1s)} h1 tags'].append(url)
        if any(p.find('h1') for p in prose): issues['h1 inside content'].append(url)
        # 4. empty or near-empty content
        text = re.sub(r'\s+', ' ', main.get_text(' ')).strip()
        if len(text.split()) < 40: issues['almost no content'].append(url)
        # 5. stray <select>/<option> or <input> outside forms
        for el in main.find_all(['select', 'input', 'textarea']):
            if not el.find_parent('form'): issues['form field outside a form'].append(url); break
        # 6. local asset references that do not exist
        for tag, attr in (('img', 'src'), ('source', 'src'), ('video', 'poster'), ('script', 'src'), ('link', 'href')):
            for el in soup.find_all(tag):
                v = el.get(attr) or ''
                if v.startswith('/assets/') and not os.path.exists(os.path.join(DIST, v.lstrip('/'))): issues['missing local asset: ' + v].append(url)
        # 7. images with data: URIs (flattened pictures from the old site)
        if main.find('img', src=re.compile(r'^data:')): issues['inline data: image'].append(url)
        # 8. tables not wrapped (horizontal overflow risk)
        for t in main.find_all('table'):
            if not t.find_parent(class_='table-wrap') and not t.find_parent('form'): issues['table without scroll wrapper (JS wraps at runtime)'].append(url); break
        # 9. leftover "Register Now" / date inside a heading (webinar program-title)
        for h in main.find_all('h2'):
            if h.find('a') and 'Register' in h.get_text(): issues['link inside h2 (webinar title)'].append(url); break
        # 10. empty links
        if any(not a.get_text(strip=True) and not a.find('img') and not a.find('svg') for a in main.find_all('a')): issues['empty link'].append(url)
        # 11. consecutive images stacked in prose (3+ in a row outside a grid)
        for p in prose:
            run = 0
            for ch in p.children:
                if getattr(ch, 'name', None) == 'img': run += 1
                elif getattr(ch, 'name', None): run = 0
                if run >= 3: issues['3+ images stacked in prose'].append(url); break
            else: continue
            break
for k, v in sorted(issues.items(), key=lambda kv: -len(kv[1])):
    print(f'{len(v):4}  {k}')
    for u in sorted(set(v))[:4]: print(f'        {u}')
if not issues: print('no issues')
