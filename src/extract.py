#!/usr/bin/env python3
"""Extract verbatim page content from the crawled coachmastersacademy.com HTML.

Usage: python3 src/extract.py <raw_dir>
  raw_dir contains one .html per URL (see README "Re-crawling") and ../sitemap_urls.txt
Output: src/content/pages.json  - one record per page; copy is untouched.
"""
import re, os, sys, json, html
from bs4 import BeautifulSoup, NavigableString, Comment, Tag
def T(name): return Tag(name=name)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'src', 'raw')
URLS = os.path.join(RAW_DIR, '..', 'sitemap_urls.txt')
SITE = 'https://www.coachmastersacademy.com'

KEEP_TAGS = {'h1','h2','h3','h4','h5','h6','p','ul','ol','li','a','img','iframe','strong','em','b','i','u','br',
             'table','thead','tbody','tr','td','th','blockquote','form','label','input','select','option',
             'textarea','video','source','sup','sub','hr','details','summary'}
KEEP_ATTRS = {'href','src','alt','colspan','rowspan','type','name','placeholder','value','required','rows','cols',
              'action','method','selected','target','open'}
DROP_TAGS = {'script','style','noscript','svg','link','meta','head','title','button'}
# exact class tokens whose subtree is site chrome, not copy
DROP_CLASSES = {'sidebar','sidebar-widget','widget','cookie-bar','cookieConsent','cookie-consent','modal','preloader',
                'scroll-to-top','search-popup','recent-searches','mobile-menu','nav-outer','sub-page','page-title',
                'breadcrumb','social-links','social-icon','share-box','back-to-top','subnav'}

def fname(u):
    f = re.sub(r'^/', '', u).rstrip('/')
    f = re.sub(r'[/?=%]', '_', f)
    return (f or 'index') + '.html'

def fix_url(u, asset=False):
    u = (u or '').strip()
    for pre in (SITE, 'https://coachmastersacademy.com', 'http://www.coachmastersacademy.com'):
        if u.startswith(pre): u = u[len(pre):] or '/'
    if asset:
        if u.startswith('/') and not u.startswith('//'): u = SITE + u
        return u
    if re.match(r'/(public|siteimages|upload|ckFiles|lms)/', u): return SITE + u
    if u.startswith('/'): u = re.sub(r'/+$', '', u) or '/'
    return u

def text(x):
    return re.sub(r'\s+', ' ', x if isinstance(x, str) else x.get_text(' ')).strip()

def has_drop_class(tag):
    cls = set(tag.get('class') or [])
    if tag.get('id') in DROP_CLASSES: return True
    if any(c.startswith('sidebar') and 'page' not in c for c in cls): return True
    return bool(cls & DROP_CLASSES)

def convert_widgets(root):
    """Accordions / tab panes -> <details>, so the copy survives without Bootstrap JS."""
    # bootstrap 5 accordion items
    for item in root.select('.accordion-item'):
        btn = item.select_one('button, .accordion-button, .card-header')
        body = item.select_one('.accordion-body, .accordion-collapse, .card-body')
        if not btn: continue
        d = T('details'); s = T('summary'); s.string = text(btn); d.append(s)
        if body:
            for c in list(body.children): d.append(c.extract())
        item.replace_with(d)
    # bootstrap tabs: nav-tabs + tab-content
    for nav in root.select('ul.nav-tabs, .nav-tabs'):
        labels = [text(a) for a in nav.select('a, button')]
        content = nav.find_next_sibling(class_='tab-content') or (nav.parent.select_one('.tab-content') if nav.parent else None)
        if not content: continue
        panes = content.select('.tab-pane')
        if not panes: continue                      # not a Bootstrap tab set; keep the markup as it is
        wrap = T('div')
        for i, pane in enumerate(panes):
            d = T('details'); 
            if i == 0: d['open'] = ''
            s = T('summary'); s.string = labels[i] if i < len(labels) else f'Tab {i+1}'; d.append(s)
            for c in list(pane.children): d.append(c.extract())
            wrap.append(d)
        content.replace_with(wrap); nav.decompose()
    # generic collapse buttons outside .accordion-item (bootstrap 3/4 panels)
    for btn in root.select('[data-bs-toggle="collapse"], [data-toggle="collapse"]'):
        target = btn.get('data-bs-target') or btn.get('data-target') or btn.get('href') or ''
        body = root.select_one(target) if target.startswith('#') else None
        if body is None: continue
        d = T('details'); s = T('summary'); s.string = text(btn); d.append(s)
        for c in list(body.children): d.append(c.extract())
        body.decompose()
        holder = btn
        for anc in btn.parents:
            if anc.name in ('h1','h2','h3','h4','h5','h6','div') and anc.get('class') and any('head' in c for c in anc.get('class')):
                holder = anc; break
        holder.replace_with(d)

def clean(node):
    """Return sanitized HTML of node: unwrap layout tags, drop chrome, keep text + semantic tags."""
    for c in node.find_all(string=lambda t: isinstance(t, Comment)): c.extract()
    for t in list(node.find_all(True)):
        if t.parent is None: continue
        if has_drop_class(t): t.decompose()
    convert_widgets(node)
    for t in list(node.find_all(True)):
        if t.parent is None: continue
        if t.name in DROP_TAGS: t.decompose()
    for t in list(node.find_all(True)):
        if t.parent is None: continue
        if t.name == 'i' and not t.get_text(strip=True): t.decompose(); continue
        if t.name == 'select':
            opts = t.find_all('option')
            if len(opts) > 12:
                for o in opts[1:]: o.decompose()
                t.append(Comment(' CMS: full option list supplied by backend '))
        if t.name not in KEEP_TAGS:
            t.unwrap(); continue
        attrs = {k: v for k, v in t.attrs.items() if k in KEEP_ATTRS}
        if t.name == 'a' and 'href' in attrs: attrs['href'] = fix_url(attrs['href'])
        if t.name in ('img','iframe','source','video') and 'src' in attrs: attrs['src'] = fix_url(attrs['src'], asset=True)
        if t.name == 'form' and 'action' in attrs: attrs['action'] = fix_url(attrs['action'])
        if t.name == 'img': attrs.setdefault('alt', '')
        t.attrs = attrs
    s = str(node)
    s = re.sub(r'^<(div|body|section)[^>]*>|</(div|body|section)>$', '', s.strip())
    s = re.sub(r'<(p|li|h[1-6]|strong|em|b|i|u|label)>\s*(?:&nbsp;|\xa0|\s)*</\1>', '', s)
    s = re.sub(r'<p>\s*(<br\s*/?>\s*)+</p>', '', s)
    s = re.sub(r'\s*\n\s*', '\n', s)
    s = re.sub(r'\n{2,}', '\n', s)
    s = re.sub(r'(<br/?>\s*){3,}', '<br><br>', s)
    s = re.sub(r'<a href="#">\s*Accept\s*</a>', '', s)                 # cookie bar
    s = re.sub(r'<a href="javascript:[^"]*">\s*(<img[^>]*>)\s*</a>', r'\1', s)
    s = re.sub(r'<(h[1-6])>\s*<\1>(.*?)</\1>\s*</\1>', r'<\1>\2</\1>', s, flags=re.S)  # nested same heading
    return s.strip()

def extract(path, url):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    soup = BeautifulSoup(raw, 'lxml')
    rec = {'url': url}
    rec['title'] = text(soup.title.get_text()) if soup.title else ''
    m = soup.find('meta', attrs={'name': 'description'})
    rec['description'] = text(m.get('content', '')) if m else ''
    header = soup.find('header'); footer = soup.find_all('footer')
    if not header or not footer: return None
    footer = footer[-1]
    # collect everything between </header> and <footer>
    mid = soup.new_tag('div')
    for sib in list(header.next_siblings):
        if sib is footer: break
        if footer in getattr(sib, 'descendants', []): 
            # footer nested deeper: take children before it
            for c in list(sib.children):
                if c is footer or (hasattr(c,'descendants') and footer in c.descendants): break
                mid.append(c.extract())
            break
        mid.append(sib.extract())
    # sub navigation
    rec['subnav'] = []
    sn = mid.select_one('#subnav')
    if sn:
        for a in sn.select('a[href]'):
            t = text(a)
            if t and t != 'View more Pages': rec['subnav'].append({'text': t, 'href': fix_url(a['href'])})
        sn.decompose()
    # page title block
    rec['h1'] = ''; rec['breadcrumb'] = []
    h1 = mid.find('h1')
    if h1: rec['h1'] = text(h1)
    pt = mid.select_one('.page-title, .page-title-section, .breadcrumb-area')
    if pt:
        rec['breadcrumb'] = [text(li) for li in pt.select('li')]
        pt.decompose()
    elif h1: h1.decompose()
    # standalone banner image straight after header
    rec['banner'] = ''
    first = next((c for c in mid.children if not isinstance(c, NavigableString) or (not isinstance(c, Comment) and c.strip())), None)
    if first is not None and getattr(first, 'name', None) == 'img':
        rec['banner'] = fix_url(first.get('src',''), asset=True); first.decompose()
    rec['content'] = clean(mid)
    rec['text_len'] = len(text(BeautifulSoup(rec['content'], 'lxml').get_text(' ')))
    return rec

def main():
    urls = [l.strip() for l in open(URLS) if l.strip()]
    pages = []
    for u in urls:
        p = os.path.join(RAW_DIR, fname(u))
        if not os.path.exists(p): print('missing', u); continue
        r = extract(p, u)
        if r: pages.append(r)
    out = os.path.join(ROOT, 'src', 'content', 'pages.json')
    json.dump(pages, open(out, 'w'), ensure_ascii=False, indent=1)
    print(len(pages), 'pages ->', out)

if __name__ == '__main__':
    main()
