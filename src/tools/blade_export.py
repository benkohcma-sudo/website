#!/usr/bin/env python3
"""Turn built pages into Laravel Blade views, so the back-end developer can drop them in.

    /usr/bin/python3 src/build.py && /usr/bin/python3 src/tools/blade_export.py

Writes laravel/resources/views/social-foundation/*.blade.php from the pages in dist/.
Run it again after any change to those pages; the views are regenerated, never edited by hand.
"""
import os, re, html
import testimonies

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIST = os.path.join(ROOT, 'dist')
OUT = os.path.join(ROOT, 'laravel', 'resources', 'views', 'social-foundation')

PAGES = [   # (url, view file)
    ('/pages/our-social-foundation', 'index'),
    ('/pages/our-social-foundation/i-am-not-afraid', 'i-am-not-afraid'),
    ('/pages/our-social-foundation/dare-to-dream', 'dare-to-dream'),
]


def blade(url, name):
    src = os.path.join(DIST, url.lstrip('/'), 'index.html')
    h = open(src, encoding='utf-8').read()
    title = html.unescape(re.search(r'<title>(.*?)</title>', h, re.S).group(1).strip())
    m = re.search(r'<meta name="description" content="([^"]*)"', h)
    desc = html.unescape(m.group(1)) if m else ''
    main = re.search(r'<main[^>]*>(.*)</main>', h, re.S).group(1).strip()

    # Blade reads @word and {{ }} as its own syntax; nothing in the page text may be taken for it
    main = re.sub(r'@(?=[A-Za-z])', '@@', main).replace('{{', '@{{')
    # files in public/assets go through asset(), links to other pages through url()
    main = re.sub(r'\b(src|href|poster)="/assets/([^"]+)"', lambda g: '%s="{{ asset(\'assets/%s\') }}"' % (g.group(1), g.group(2)), main)
    main = re.sub(r'\bhref="(/[^"/][^"]*|/)"', lambda g: 'href="{{ url(\'%s\') }}"' % g.group(1), main)

    # testimonies become an editable list at the top of the view and a loop in the page
    head = ''
    rows = testimonies.items(url)
    if rows:
        main, ok = testimonies.swap(main, testimonies.BLADE_LOOP)
        assert ok, 'testimony cards not found in ' + url
        head = testimonies.blade_list(rows)

    q = lambda s: s.replace('\\', '\\\\').replace("'", "\\'")
    out = ("{{-- %s\n"
           "     Generated from dist%s/index.html by src/tools/blade_export.py. Do not edit by hand (except\n"
           "     the TESTIMONIES list, if there is one):\n"
           "     ask the designer for a change and this file is regenerated.\n"
           "     Change 'layouts.app' and the section names below to match the site's own layout. --}}\n"
           "@extends('layouts.app')\n\n"
           "@section('title', '%s')\n"
           "@section('meta_description', '%s')\n\n"
           "@section('content')\n%s"
           "{{-- If the layout already opens <main>, delete this wrapper and keep what is inside it. --}}\n"
           "<main class=\"page-enter\">\n%s\n</main>\n"
           "@endsection\n") % (title, url, q(title), q(desc), head, main)
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, name + '.blade.php')
    open(path, 'w', encoding='utf-8').write(out)
    return path, len(out)


if __name__ == '__main__':
    for url, name in PAGES:
        path, n = blade(url, name)
        print('%-70s %6d bytes' % (os.path.relpath(path, ROOT), n))
