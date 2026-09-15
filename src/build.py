import re
#!/usr/bin/env python3
"""Static site generator for the Coach Masters Academy redesign.

    python3 src/build.py            -> writes dist/

Every page's copy comes verbatim from src/content/pages.json (crawled from the
live site). Templates only add layout, styling and animation hooks.
"""
import os, re, json, html, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, 'dist')
CONTENT = json.load(open(os.path.join(ROOT, 'src', 'content', 'pages.json')))
PAGES = {p['url']: p for p in CONTENT}

def _share_section_subnavs():
    """A section's sub-navigation belongs to every page it lists (and that page's ?page=N listings),
    even when the live site's template for that page left the bar out (e.g. Gallery)."""
    sets = {}
    for p in CONTENT:
        if p.get('subnav'): sets.setdefault(tuple((x['text'], x['href']) for x in p['subnav']), p['subnav'])
    for nav in sets.values():
        members = {x['href'].rstrip('/') for x in nav if x['href'].startswith('/')}
        for p in CONTENT:
            base = p['url'].split('?')[0].rstrip('/') or '/'
            if base in members and not p.get('subnav'): p['subnav'] = nav
_share_section_subnavs()
SITE = 'https://www.coachmastersacademy.com'

# ---------------------------------------------------------------- site data (verbatim from live header/footer)
NAV = [
    ('About Us', '/about-us', '/about-us'),
    ('Coaching Certification', '/icf-coaching-training-program', '/icf-coaching'),
    ('Coaching Workshop', '/coaching-skill-training-course-and-workshop', '/coaching-skill'),
    ('Coaching Service', '/executive-leadership-coaching-service-for-managers-and-leaders', '/executive'),
    ('Schedule', '/events/calendar', '/events/calendar'),
    ('Resource', '/blog/coaching', '/blog'),
    ('Registration', '/registration', '/registration'),
]
APPS = [
    ('LMS', 'https://coachmastersacademy.thinkific.com/users/sign_in'),
    ('AM', 'https://assignment.management.coachmastersacademy.com'),
    ('Find Your Coach', 'https://findyourcoach.coachmastersacademy.com/login'),
]
PHONE = '+65-6808-6971 I +65-8299-8170'
EMAIL = 'info@coachmastersacademy.com'
ADDRESS = '1 Raffles Place Tower 2, Level 19 and 20 Singapore 048616'
FOOTER_LINKS = [
    ('Home', '/'), ('About Us', '/about-us'), ('Certificate Coaching', '/icf-coaching-training-program'),
    ('Work Shops', '/workshops'), ('Resources', '/webinar'), ('Events', '/events/news'), ('Privacy Policy', '/privacy-policy'),
]
SOCIAL = [
    ('Facebook', 'https://www.facebook.com/CMAGLOBALOFFICE/', 'M14 8h-2.5V6.5c0-.7.2-1.1 1.2-1.1H14V3h-2c-2.5 0-3.5 1.4-3.5 3.5V8H6v2.5h2.5V21h3v-10.5h2.2L14 8z'),
    ('Twitter', 'https://twitter.com/CMAGLOBALOFFICE', 'M22 5.9c-.7.3-1.5.5-2.4.6.9-.5 1.5-1.3 1.8-2.3-.8.5-1.7.8-2.6 1a4.1 4.1 0 0 0-7 3.7C8.4 8.8 5.4 7.1 3.4 4.6a4.1 4.1 0 0 0 1.3 5.5c-.7 0-1.3-.2-1.9-.5 0 2 1.4 3.7 3.3 4.1-.6.2-1.2.2-1.9.1.5 1.6 2.1 2.8 3.9 2.9A8.3 8.3 0 0 1 2 18.4 11.7 11.7 0 0 0 8.3 20c7.5 0 11.7-6.3 11.7-11.7v-.5c.8-.6 1.5-1.3 2-2z'),
    ('LinkedIn', 'https://www.linkedin.com/company/coach-masters-academy/', 'M6.5 8.5h-3V21h3V8.5zM5 3.5a1.8 1.8 0 1 0 0 3.6 1.8 1.8 0 0 0 0-3.6zM21 13.3c0-3.4-1.8-5-4.3-5-2 0-2.9 1.1-3.4 1.9V8.5h-3V21h3v-6.7c0-1.8.3-3.5 2.5-3.5 2.1 0 2.2 2 2.2 3.6V21h3v-7.7z'),
    ('Instagram', 'https://www.instagram.com/cmaglobaloffice/', 'M12 7.3a4.7 4.7 0 1 0 0 9.4 4.7 4.7 0 0 0 0-9.4zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zm6-7.9a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0zM21 8c0-1.6-.4-3-1.5-4.1S17.1 2.5 15.5 2.4C13.9 2.3 10.1 2.3 8.5 2.4 6.9 2.5 5.5 2.8 4.4 3.9S2.5 6.4 2.4 8c-.1 1.6-.1 6.4 0 8 .1 1.6.4 3 1.5 4.1s2.5 1.4 4.1 1.5c1.6.1 6.4.1 8 0 1.6-.1 3-.4 4.1-1.5s1.4-2.5 1.5-4.1c.1-1.6.1-6.4 0-8zm-2.1 9.7c-.3.9-1 1.5-1.9 1.9-1.3.5-4.4.4-5.9.4s-4.6.1-5.9-.4c-.9-.3-1.5-1-1.9-1.9-.5-1.3-.4-4.4-.4-5.9s-.1-4.6.4-5.9c.3-.9 1-1.5 1.9-1.9 1.3-.5 4.4-.4 5.9-.4s4.6-.1 5.9.4c.9.3 1.5 1 1.9 1.9.5 1.3.4 4.4.4 5.9s.1 4.6-.4 5.9z'),
    ('YouTube', 'https://www.youtube.com/c/CoachMastersAcademychannel', 'M22.5 7.2c-.3-1-1-1.7-2-2C18.8 4.8 12 4.8 12 4.8s-6.8 0-8.5.4c-1 .3-1.7 1-2 2C1 8.9 1 12 1 12s0 3.1.5 4.8c.3 1 1 1.7 2 2 1.7.4 8.5.4 8.5.4s6.8 0 8.5-.4c1-.3 1.7-1 2-2 .5-1.7.5-4.8.5-4.8s0-3.1-.5-4.8zM9.8 15.1V8.9l5.7 3.1-5.7 3.1z'),
]
ARROW = '<svg class="arrow" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 13 13 3M5 3h8v8"/></svg>'
PIN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>'

def esc(s): return html.escape(s or '', quote=True)

def btn(text, href, cls='', arrow=True):
    ext = ' target="_blank" rel="noopener"' if href.startswith('http') else ''
    return f'<a class="btn {cls}" href="{esc(href)}"{ext}>{esc(text)}{ARROW if arrow else ""}</a>'

def link(text, href, cls=''):
    return f'<a class="link {cls}" href="{esc(href)}">{esc(text)}{ARROW}</a>'

# ---------------------------------------------------------------- chrome
def header():
    nav = ''.join(f'<a href="{h}" data-section="{sec}">{esc(t)}</a>' for t, h, sec in NAV if t != 'Registration')
    apps = ''.join(f'<a href="{h}" target="_blank" rel="noopener">{esc(t)}</a>' for t, h in APPS)
    return f'''
<div class="topbar">
  <div class="container">
    <div class="topbar__contact"><a href="tel:+6568086971">{esc(PHONE)}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    <div class="topbar__apps">{apps}</div>
  </div>
</div>
<header class="site-header">
  <div class="container">
    <a class="logo" href="/" aria-label="Coach Masters Academy home"><img src="/assets/img/logo.png" alt="Coach Masters Academy" width="250" height="70"></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
    <div class="header__cta">
      {btn('Registration', '/registration', 'btn--sm')}
      <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<nav class="mobile-nav" aria-label="Mobile">{nav}<div class="mobile-nav__apps">{apps}</div></nav>'''

def footer():
    links = ''.join(f'<li><a href="{h}">{esc(t)}</a></li>' for t, h in FOOTER_LINKS)
    social = ''.join(f'<a href="{h}" target="_blank" rel="noopener" aria-label="{n}"><svg viewBox="0 0 24 24"><path d="{d}"/></svg></a>' for n, h, d in SOCIAL)
    return f'''
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="logo logo--light" href="/"><img src="/assets/img/logo.png" alt="Coach Masters Academy" width="250" height="70"></a>
        <h4>Contact US</h4>
        <ul>
          <li>{esc(ADDRESS)}</li>
          <li><a href="tel:+6568086971">{esc(PHONE)}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
      <div>
        <h4>INFORMATION LINKS</h4>
        <ul>{links}</ul>
      </div>
      <div>
        <h4>Programs</h4>
        <ul>
          <li><a href="/icf-coaching-training-program">Coaching Certification</a></li>
          <li><a href="/coaching-skill-training-course-and-workshop">Coaching Workshop</a></li>
          <li><a href="/executive-leadership-coaching-service-for-managers-and-leaders">Coaching Service</a></li>
          <li><a href="/events/calendar">Schedule</a></li>
          <li><a href="/our-faculty">Our Faculty</a></li>
        </ul>
      </div>
      <div>
        <h4>SUBSCRIBE OUR NEWSLETTER</h4>
        <p>Sign up to be the first to get information on coaching events to your inbox.</p>
        <!-- CMS: newsletter form posts to backend; country select supplied by backend -->
        <form class="footer-form" method="post" action="#"><input type="email" name="email" placeholder="Your email address" required><button type="submit">Subscribe</button></form>
        <div class="social" style="margin-top:22px">{social}</div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; Coach Masters Academy. All rights reserved.</span>
      <span><a href="/privacy-policy">Privacy Policy</a></span>
    </div>
  </div>
</footer>'''

# key phrases that turn orange in section headings (copy unchanged, only colour)
HEADING_HL = {
    'Advancing Human Potential Through Global Coaching Certification': 'Global Coaching Certification',
    'ICF-Accredited Coaching Certification with Industry-leading Standards': 'Industry-leading Standards',
    'Coaching Methodology Grounded in Science for Sustainable Change': 'Sustainable Change',
    'Why Choose Coach Masters Academy for Your Life Coach Certification': 'Life Coach Certification',
    'Real-World Coaching Skills Developed with Industry Professionals': 'Industry Professionals',
    'Join a Live Coaching Experience & Gain Practical Insight': 'Practical Insight',
    'Download Full Program Brochure & Curriculum Guide': 'Curriculum Guide',
    'Trusted Partnerships with Leading Coaching Experts & Organizations': 'Leading Coaching Experts',
    'Hear what our clients shared about their learning experiences with us.': 'learning experiences',
    'Latest News, Insights & Upcoming Events in Coaching': 'Upcoming Events',
    'Inspiring Positive Change Through mastery of coaching.': 'mastery of coaching.',
    'A Vision to Inspire Positive Change through Mastery of Coaching': 'Mastery of Coaching',
    'Our Mission': 'Mission',
    'Meet the minds behind meaningful change.': 'meaningful change.',
    'Unassuming Beginning with a Noble Mission': 'Noble Mission',
    'ICF Coaching Education that Starts Where Real Change Begins': 'Real Change Begins',
    'Proven Success: Coaching Cohorts, Graduates, and More': 'Coaching Cohorts, Graduates, and More',
    'ICF Credential Paths: From ACC to MCC': 'From ACC to MCC',
    'Explore Your Coaching Pathway: Foundational to Mastery': 'Foundational to Mastery',
    'Comprehensive Suite of ICF Accredited Coaching Education': 'ICF Accredited Coaching Education',
    'Our Premium Services': 'Premium',
    'Certified and experienced coaching professionals': 'coaching professionals',
    'Shaping Tomorrow with Our Clients.': 'Our Clients.',
    'Not All Coaching Programs are Created the Same': 'Created the Same',
    'Get Real Results, Real Change with our Transformational Approach': 'Transformational Approach',
    'Learn from Anywhere. Grow Beyond Boundaries.': 'Grow Beyond Boundaries.',
    'Explore Our Monthly Training Calendar': 'Training Calendar',
    'Your Success Matters to Us.': 'Matters to Us.',
    'Welcome to Coach Masters Academy.': 'Coach Masters Academy.',
    'Your journey towards mastering coaching begins with us.': 'mastering coaching',
    'Unique Contribution:Making Good Leaders Great': 'Good Leaders Great',
    'Thought-Leader in the field of transforming coaching': 'transforming coaching',
    'Become an ICF-Certified Coach with Coach Masters Academy': 'Coach Masters Academy',
    'Coaching Workshop for Leaders and Managers': 'Leaders and Managers',
    'Executive Leadership Coaching Services for High‑Impact Leaders': 'High‑Impact Leaders',
    'Coaching Education': 'Education',
    'Mentor Coaching': 'Coaching',
    'Schedule': 'Schedule',
    'Registration': 'Registration',
}
STOP = {'us', 'more', 'you', 'the', 'and', 'of', 'to', 'in', 'for', 'a', 'with', 'our', 'your', 'is', 'it'}

def _hl_phrase(text):
    t = re.sub(r'\s+', ' ', text).strip()
    if t in HEADING_HL: return HEADING_HL[t]
    for key, v in HEADING_HL.items():
        if re.sub(r'\s+', ' ', key) == t: return v
    if ':' in t and len(t.split(':', 1)[1].split()) >= 2: return t.split(':', 1)[1].strip()
    words = t.split()
    if len(words) >= 5 and words[-1].strip('.,!?').lower() not in STOP and words[-2].strip('.,!?').lower() not in STOP:
        return ' '.join(words[-2:])
    return ''

def emphasize(main_html):
    """Section headings: heavier, with the key phrase in orange. Quoted sentences: pull-quote cards."""
    def heading(m):
        open_tag, inner, close = m.group(1), m.group(2), m.group(3)
        if '<' in re.sub(r'<br\s*/?>', ' ', inner) or 'class="hv__' in open_tag or 'awards__' in inner: return m.group(0)
        plain = html.unescape(re.sub(r'<br\s*/?>', ' ', inner))
        phrase = _hl_phrase(plain)
        if not phrase: return m.group(0)
        esc_phrase = html.escape(phrase, quote=False)
        idx = inner.rfind(esc_phrase)
        if idx < 0: idx = inner.rfind(phrase); esc_phrase = phrase if idx >= 0 else esc_phrase
        if idx < 0: return m.group(0)
        before, after = inner[:idx], inner[idx + len(esc_phrase):]
        # only wrap on word boundaries, so the text still reads identically when tags are stripped
        if (before and not before[-1].isspace() and not before.endswith('>')) or (after and not after[0].isspace() and not after.startswith('<')): return m.group(0)
        inner = before + '<em class="hl">' + esc_phrase + '</em>' + after
        return open_tag + inner + close
    main_html = re.sub(r'(<h2(?:\s[^>]*)?>)(.*?)(</h2>)', heading, main_html, flags=re.S)
    def quote(m):
        tag, inner, cite = m.group(1), m.group(2), (m.group(3) or '')
        if cite and not cite[0].isspace(): inner, cite = inner + cite, ''   # ", according to X" belongs to the sentence
        cite = cite.strip()
        plain = re.sub(r'\s+', ' ', inner).strip()
        if len(plain) < 50 or '<' in plain.replace('<br>', '').replace('<br/>', ''): return m.group(0)
        cite_html = f'<span class="pull__cite">{cite}</span>' if cite else ''
        parts = re.split(r'(?<=[.!?])\s+', plain, maxsplit=1)
        if len(parts) == 2:
            lead, rest = parts
            w = rest.split(' ', 3)
            head = ' '.join(w[:3]); tail = (' ' + w[3]) if len(w) > 3 else ''
            body = f'<span class="pull__lead">{lead}</span><strong class="pull__stmt"><em class="hl">{head}</em>{tail}</strong>'
        else:
            w = plain.split(' ', 3)
            body = f'<strong class="pull__stmt"><em class="hl">{" ".join(w[:3])}</em>{(" " + w[3]) if len(w) > 3 else ""}</strong>'
        long_cls = ' pull--long' if len(plain) > 220 else ''
        return f'<div class="pull{long_cls}" data-reveal><i class="pull__rule"></i><{tag} class="pull__text">{body}{cite_html}</{tag}>'
    # a quoted sentence (optionally followed by a short attribution) standing as its own paragraph
    main_html = re.sub(r'<(p|h5)(?:\s[^>]*)?>\s*((?:“|&ldquo;|"|&quot;)[^<]{40,}?(?:”|&rdquo;|"|&quot;))([^<]{0,90})</\1>', lambda m: quote(m) + '</div>', main_html)
    return main_html

# links that are dead on the live site itself (WordPress tag pages returning 404): shown as plain text
DEAD_LINKS = {'/blog/blog/coaching-articles/' + t for t in (
    'agency', 'choice', 'coaching-approach', 'coaching-education', 'coaching-mindset', 'coaching-training',
    'leadership-development', 'personal-agency', 'professional-coaching', 'self-help', 'transformational-approach', 'transformative-coaching',
    'self-coaching', 'transformative-edge')}

def fix_links(body_html):
    # uploaded files (audio, PDFs) live on the client's server, not in this build
    body_html = re.sub(r'href="(/blog/wp-content/[^"]+)"', lambda m: f'href="{SITE}{m.group(1)}" target="_blank" rel="noopener"', body_html)
    def unwrap(m):
        href = m.group(1).split('#')[0].rstrip('/')
        return m.group(2) if href in DEAD_LINKS else m.group(0)
    return re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>', unwrap, body_html, flags=re.S)

# Green screen, white CMA logo, then orange steps climb in and lift away to open the page.
# Shown on the first page of a visit (sessionStorage), skipped for ?nomotion and reduced motion.
PRELOADER = (
    '<script>(function(){var d=document.documentElement,s=0;try{s=sessionStorage.getItem("cmaPre")}catch(e){}'
    'if(s||/nomotion/.test(location.search)||matchMedia("(prefers-reduced-motion: reduce)").matches)d.classList.add("pre-skip");'
    'else d.classList.add("is-preloading")})()</script>'
    '<div class="preloader" aria-hidden="true"><div class="preloader__bg"></div>'
    '<div class="preloader__logo"><img src="/assets/img/logo.png" alt=""><i class="preloader__line"></i></div>'
    '<div class="preloader__steps">' + '<i class="preloader__step"></i>' * 8 + '</div></div>'
)

def group_form_fields(body):
    """Forms that arrive as a flat run of <label> + field siblings get each label wrapped with its
    field (.field), and radio/checkbox option labels gathered under their question (.field--choices).
    Nothing is renamed, reworded or removed; stepper forms and table forms are left alone."""
    from bs4 import BeautifulSoup, Comment
    def one(m):
        html_ = m.group(0)
        if 'js-steps' in html_[:300] or '<table' in html_ or '<label' not in html_:
            return html_
        soup = BeautifulSoup(html_, 'html.parser'); form = soup.find('form')
        kids = [c for c in form.contents if getattr(c, 'name', None) or isinstance(c, Comment)]
        if not any(getattr(k, 'name', None) == 'label' and not k.find('input') for k in kids):
            return html_
        is_choice = lambda t: getattr(t, 'name', None) == 'label' and t.find('input', attrs={'type': re.compile('^(radio|checkbox)$')}) is not None
        is_field = lambda t: getattr(t, 'name', None) in ('input', 'select', 'textarea') and t.get('type') != 'hidden'
        new = []; i = 0
        while i < len(kids):
            k = kids[i]; nxt = kids[i + 1] if i + 1 < len(kids) else None
            if getattr(k, 'name', None) == 'label' and not k.find('input') and nxt is not None:
                if is_choice(nxt):
                    j = i + 1; opts = []
                    while j < len(kids) and is_choice(kids[j]): opts.append(kids[j]); j += 1
                    wrap = soup.new_tag('div', attrs={'class': 'field field--full field--choices'}); wrap.append(k.extract())
                    box = soup.new_tag('div', attrs={'class': 'choices'})
                    for o in opts: box.append(o.extract())
                    wrap.append(box); new.append(wrap); i = j; continue
                if is_field(nxt):
                    cls = 'field field--full' if nxt.name == 'textarea' else 'field'
                    wrap = soup.new_tag('div', attrs={'class': cls}); wrap.append(k.extract()); wrap.append(nxt.extract())
                    new.append(wrap); i += 2; continue
            new.append(k.extract()); i += 1
        form.clear()
        for n in new: form.append(n)
        return str(form)
    if '<form' not in body: return body
    body = re.sub(r'<form\b[^>]*>.*?</form>', one, body, flags=re.S)
    def frame(m):
        # long interest forms: the heading and note just above move into the form, and the form sits in an orange frame
        intro, form = m.group(1) or '', m.group(3)
        if form.count('class="field') < 5: return m.group(0)
        if intro:
            k = form.index('>') + 1
            form = form[:k] + '<div class="form-intro">' + intro + '</div>' + form[k:]
        return '<div class="form-frame">' + form + '</div>'
    return re.sub(r'((<h[2-4]>(?:(?!</h[2-4]>).)*</h[2-4]>)\s*(?:<p>(?:(?!</p>|<form).)*</p>\s*)?)?(<form\b[^>]*>(?:(?!</form>).)*</form>)', frame, body, flags=re.S)

def layout(page, body, extra_head='', extra_js='', body_class=''):
    body = fix_links(group_form_fields(emphasize(body)))
    title = page.get('title') or 'Coach Masters Academy'
    desc = page.get('description', '')
    return f'''<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}{page['url']}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/main.css">
{extra_head}
</head>
<body class="{body_class}">
{PRELOADER}
{header()}
<main class="page-enter">
{body}
</main>
{footer()}
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
{extra_js}
<script src="/assets/js/main.js"></script>
</body>
</html>'''

def laurel(flip=False):
    """Orange laurel branch (SVG): quadratic stem with leaf pairs along it, tapering to the tip."""
    import math
    P0, P1, P2 = (64, 116), (4, 86), (34, 6)
    def pt(t):
        x = (1-t)**2*P0[0] + 2*(1-t)*t*P1[0] + t*t*P2[0]; y = (1-t)**2*P0[1] + 2*(1-t)*t*P1[1] + t*t*P2[1]; return x, y
    def tan(t):
        dx = 2*(1-t)*(P1[0]-P0[0]) + 2*t*(P2[0]-P1[0]); dy = 2*(1-t)*(P1[1]-P0[1]) + 2*t*(P2[1]-P1[1]); return math.degrees(math.atan2(dy, dx))
    leaves = ''
    for i in range(7):
        t = 0.06 + 0.86 * i / 6
        x, y = pt(t); a = tan(t); size = 1.05 - 0.5 * t
        for side in (-1, 1):
            rot = a + 90 + side * 42                    # leaf points forward along the stem, splayed to each side
            L = 24 * size; W = 6.5 * size
            leaves += f'<path d="M0 0 C {W} -{L*0.35:.1f}, {W} -{L*0.75:.1f}, 0 -{L:.1f} C -{W} -{L*0.75:.1f}, -{W} -{L*0.35:.1f}, 0 0 Z" transform="translate({x:.1f} {y:.1f}) rotate({rot:.1f})"/>'
    stem = f'M{P0[0]} {P0[1]} Q{P1[0]} {P1[1]} {P2[0]} {P2[1]}'
    return f'<svg class="laurel{" laurel--flip" if flip else ""}" viewBox="0 0 100 120" aria-hidden="true"><path d="{stem}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><g fill="currentColor">{leaves}</g></svg>'

def awards_band():
    """Transformative Edge (TM) Foundational Advantage banner (from the client graphic), rebuilt in HTML."""
    def award(title, line, accent):
        return f'<div class="award" data-reveal>{laurel()}<div class="award__text"><b>{title}</b><span>{line}</span><em>{accent}</em></div>{laurel(True)}</div>'
    return f'''
<section class="section section--tight awards">
  <div class="container">
    <div class="awards__head">
      <h2 data-reveal><span class="awards__l1">Transformative Edge</span><span class="awards__l2">Foundational Advantage</span></h2>
      <p class="awards__sub" data-reveal>ICF-Accredited Professional Coaching Certification Program</p>
    </div>
    <div class="awards__row">
      {award('Coaching Impact Award', 'Distinguished Coaching Education', 'International Coaching Federation')}
      {award('Best Education Award', 'Grade “A” Status', '')}
      {award('Best Coaching Skill Training', '', 'in Asia Pacific 2021')}
    </div>
  </div>
</section>'''

# ---------------------------------------------------------------- generic building blocks
def subnav(page):
    if not page.get('subnav'): return ''
    # an item with no destination on the live site (href "#") is shown muted, not as a dead link
    RENAME = {'Our Vision': 'Who We Are'}     # sub-navigation labels the client asked to change
    return '<nav class="subnav" aria-label="Section"><div class="container">' + ''.join(
        (f'<span class="subnav__soon" title="Coming soon">{esc(s["text"])}</span>' if s['href'] in ('#', '') else f'<a href="{esc(s["href"])}">{esc(RENAME.get(s["text"], s["text"]))}</a>')
        for s in page['subnav']) + '</div></nav>'

def crumbs(page, label=None):
    return ''   # breadcrumb trails removed from every hero (design decision; section sub-navigation remains)

def _crumbs_unused(page, label=None):
    parts = ['<a href="/">Home</a>']
    u = page['url']
    if u.startswith('/events/news/') or u.startswith('/events/news?'): parts.append('<span><a href="/events/news">News</a></span>')
    elif u.startswith('/events/gallery'): parts.append('<span><a href="/events/gallery">Gallery</a></span>')
    elif u.startswith('/events/calendar/') or u.startswith('/event/'): parts.append('<span><a href="/events/calendar">Schedule</a></span>')
    elif u.startswith('/webinar/'): parts.append('<span><a href="/webinar">Webinar</a></span>')
    elif u.startswith('/blog/'): parts.append('<span><a href="/blog/coaching">Blog</a></span>')
    elif page.get('subnav') and page['subnav'][0]['href'] != u:
        parts.append(f'<span><a href="{esc(page["subnav"][0]["href"])}">{esc(page["subnav"][0]["text"])}</a></span>')
    parts.append(f'<span>{esc(label or page_heading(page))}</span>')
    return '<div class="crumbs">' + ''.join(parts) + '</div>'

def page_heading(page):
    """H1 from the page; fall back to the <title> minus site suffix; last resort slug."""
    if page.get('h1'): return page['h1']
    t = re.split(r'\s*[|\-–]\s*Coach Masters Academy.*$', page.get('title', ''), flags=re.I)[0].strip()
    if t and t.lower() not in ('coach masters academy',): return t
    slug = page['url'].rstrip('/').split('/')[-1].split('?')[0]
    return html.unescape(slug).replace('%20', ' ').replace('-', ' ').strip().title() or 'Coach Masters Academy'

# full-width photo heroes for the main section pages (photo on the right, title on the left)
HERO_IMAGES = {
    '/events/calendar': 'schedule',
    '/executive-leadership-coaching-service-for-managers-and-leaders': 'coaching-service',
    '/mentor-coaching': 'mentoring', '/pages/mentor-coaching': 'mentoring',
    '/icf-coaching-training-program': 'certification',
    '/coaching-skill-training-course-and-workshop': 'workshop',
    '/pages/coaching-education': 'coaching-education',
    '/registration': 'registration',
    '/icf-coaching-certification-training-level-1-foundational-advantage': 'core-training',
    '/pages/why-cma': 'why-cma',
    '/pages/our-unique-approach': 'unique-approach',
    '/faq': 'faq',
}

def take_lead(page, content):
    """For pages with a photo hero, the opening paragraph (if it comes before any heading)
    becomes the hero's subheading. Returns (lead_html, remaining_content)."""
    if page['url'] not in HERO_IMAGES: return '', content
    paras, pos = [], 0
    while len(paras) < 3:                                   # every paragraph before the first heading
        m = re.match(r'\s*<p>(.*?)</p>', content[pos:], re.S)
        if not m or '<img' in m.group(1): break
        paras.append(m.group(1).strip()); pos += m.end()
    if not paras or sum(len(re.sub(r'<[^>]+>', ' ', x).split()) for x in paras) > 140: return '', content
    return '</p><p class="lead lead--more" data-reveal>'.join(paras), content[pos:]

def page_hero(page, label=None, lead=''):
    h = label or page_heading(page)
    img = HERO_IMAGES.get(page['url'])
    if img:
        phrase = _hl_phrase(h)
        h_html = esc(h)
        if phrase and len(phrase) < len(h) and h.endswith(phrase) and h[-len(phrase) - 1].isspace():   # a one-word title stays white
            h_html = esc(h[:-len(phrase)]) + '<em class="hl">' + esc(phrase) + '</em>'
        return f'''
<section class="page-hero page-hero--image">
  <img class="page-hero__photo" src="/assets/img/hero/{img}.jpg" alt="" data-parallax="26">
  <div class="page-hero__scrim"></div>
  <div class="container"><div class="page-hero__narrow">
    {crumbs(page, h)}
    <h1 data-split>{h_html}</h1>
    {f'<p class="lead" data-reveal style="margin-top:22px">{lead}</p>' if lead else ''}
  </div></div>
</section>'''
    return _page_hero_plain(page, h, lead)

def _page_hero_plain(page, h, lead=''):
    banner = f'<div class="page-hero__banner" data-reveal="scale"><img src="{esc(page["banner"])}" alt="" data-parallax="30"></div>' if page.get('banner') else ''
    return f'''
<section class="page-hero{' page-hero--banner' if banner else ''}">
  <div class="container"><div class="page-hero__narrow">
    {crumbs(page, h)}
    <h1 data-split>{esc(h)}</h1>
    {f'<p class="lead" data-reveal style="margin-top:22px">{lead}</p>' if lead else ''}
    {banner}
  </div></div>
</section>'''

def aside(page):
    """Sticky side card used on long-form pages: contact + section links (verbatim contact details)."""
    links = ''
    if page.get('subnav'):
        links = '<div class="aside-links">' + ''.join(f'<a href="{esc(s["href"])}">{esc(s["text"])}</a>' for s in page['subnav']) + '</div>'
    return f'''
<aside class="article__aside" data-reveal="right">
  <div class="aside-card">
    <h4>how can we help</h4>
    <p>If you need any helps, please feel free to contact us.</p>
    <a class="tel" href="tel:+6568086971">{esc(PHONE)}</a>
    <a href="mailto:{EMAIL}" style="display:block;margin-top:6px">{EMAIL}</a>
    {btn('Registration', '/registration', 'btn--white btn--sm')}
  </div>
  {links}
</aside>'''

def strip_duplicate_heading(content, h1):
    """If the body starts by repeating the H1 as an h2/h3, drop that one heading."""
    if not h1: return content
    return re.sub(r'^\s*<(h[2-4])>\s*' + re.escape(html.escape(h1, quote=False)) + r'\s*</\1>', '', content, count=1, flags=re.I)

def generic_page(page):
    content = strip_duplicate_heading(page['content'], page.get('h1'))
    content = re.sub(r'<details>', '<details open>', content, count=1)
    lead, content = take_lead(page, content)
    body = subnav(page) + page_hero(page, lead=lead) + f'''
<section class="section section--tight landing">
  <div class="container"><div class="prose prose--wide" data-auto-reveal>{content}</div></div>
</section>'''
    return layout(page, body)

# ---------------------------------------------------------------- output helpers
def out_path(url):
    u = url.split('?')[0]
    q = url.split('?')[1] if '?' in url else ''
    u = u.rstrip('/') or '/'
    u = html.unescape(u).replace('%20', ' ')
    if q: u += '/' + q.replace('=', '-')            # /events/news?page=2 -> /events/news/page-2/
    d = os.path.join(DIST, u.lstrip('/'))
    return os.path.join(d, 'index.html')

def write(url, html_text):
    p = out_path(url)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(html_text)

def rewrite_pagination(html_text):
    """?page=N links -> /page-N/ folders so the static preview works; Laravel keeps ?page=N."""
    return re.sub(r'href="(/[^"?]*)\?page=(\d+)"', r'href="\1/page-\2/"', html_text)

# The live certification pages show a poster with a play button after this paragraph; the extractor dropped it
# because the link held only an icon. Re-inserted after rendering, outside the hero.
VIDEO_CARD = ('<div class="video-card" data-reveal="scale">'
              '<img src="https://www.coachmastersacademy.com/public/twenty25/images/cma-3.png" alt="" loading="lazy">'
              '<a class="video-card__play" href="https://www.coachmastersacademy.com/public/storage/CoachMastersAcademyVideo.mp4" data-video aria-label="Play video">'
              '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></a></div>')
VIDEO_AFTER = {'/icf-coaching-training-program': 'shape lives and systems.</p>', '/pages/coaching-certification': 'shape lives and systems.</p>'}

CALL_BLOCK_RE = re.compile(r'<p>\s*You can call our Global Office.*?</p>\s*<a [^>]*>\s*Schedule a Call\s*</a>', re.S)

def strip_call_block(page):
    """The 'call our Global Office / Schedule a Call' block was removed at the client's request (Sep 2026)."""
    if 'You can call our Global Office' in page.get('content', ''):
        page = dict(page); page['content'] = CALL_BLOCK_RE.sub('', page['content'])
    return page

def insert_videos(url, html_text):
    anchor = VIDEO_AFTER.get(url)
    if not anchor: return html_text
    pos = 0
    while True:
        i = html_text.find(anchor, pos)
        if i < 0:
            print('!! video anchor not found outside the hero:', url); return html_text
        sec = html_text.rfind('<section class="', 0, i)
        if sec >= 0 and 'page-hero' in html_text[sec:sec + 60]:
            pos = i + len(anchor); continue
        j = i + len(anchor)
        return html_text[:j] + VIDEO_CARD + html_text[j:]

def build():
    if os.path.exists(DIST): shutil.rmtree(DIST)
    os.makedirs(DIST)
    shutil.copytree(os.path.join(ROOT, 'assets'), os.path.join(DIST, 'assets'))
    shutil.copy(os.path.join(ROOT, 'src', 'HANDOFF.md'), os.path.join(DIST, 'HANDOFF.md'))
    import pages_custom
    custom = pages_custom.RENDERERS
    n = 0
    for page in CONTENT:
        url = page['url']
        fn = custom.get(url) or next((f for k, f in pages_custom.PREFIX_RENDERERS if url.startswith(k)), None) or pages_custom.smart_page
        try:
            html_text = fn(strip_call_block(page))
        except Exception as e:
            print('!! failed', url, e); html_text = generic_page(page)
        write(url, rewrite_pagination(insert_videos(url, html_text))); n += 1
    print(n, 'pages ->', DIST)

if __name__ == '__main__':
    build()
