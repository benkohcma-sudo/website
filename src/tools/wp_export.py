#!/usr/bin/env python3
"""Turn the Social Foundation pages into WordPress page templates.

    /usr/bin/python3 src/build.py && /usr/bin/python3 src/tools/wp_export.py

Writes wordpress/theme-files/ from the pages in dist/. Run it again after any change to those
pages; the templates are regenerated, never edited by hand.
"""
import os, re, html
import testimonies

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DIST = os.path.join(ROOT, 'dist')
OUT = os.path.join(ROOT, 'wordpress', 'theme-files')

SF = '/pages/our-social-foundation'
WP_SF = '/our-social-foundation'          # WordPress page slugs: the parent page and its two children
PAGES = [   # (built page, template file, template name)
    (SF, 'template-social-foundation.php', 'Our Social Foundation'),
    (SF + '/i-am-not-afraid', 'template-sf-i-am-not-afraid.php', 'Social Foundation - I Am NOT Afraid'),
    (SF + '/dare-to-dream', 'template-sf-dare-to-dream.php', 'Social Foundation - Dare to Dream'),
]


def template(url, fname, tname):
    h = open(os.path.join(DIST, url.lstrip('/'), 'index.html'), encoding='utf-8').read()
    main = re.search(r'<main[^>]*>(.*)</main>', h, re.S).group(1).strip()
    assert '<?' not in main, 'page text contains a PHP opening tag'

    # files shipped with the theme
    main = re.sub(r'\b(src|href|poster)="/assets/([^"]+)"',
                  lambda g: '%s="<?php echo esc_url( get_theme_file_uri( \'assets/%s\' ) ); ?>"' % (g.group(1), g.group(2)), main)
    # the three Social Foundation pages live in WordPress, so their links go through home_url()
    main = re.sub(r'\bhref="' + re.escape(SF) + r'(/[^"]*)?"',
                  lambda g: 'href="<?php echo esc_url( home_url( \'%s/\' ) ); ?>"' % (WP_SF + (g.group(1) or '').rstrip('/')), main)
    # every other link (About Us, Our Story ...) stays as it is: those pages are not part of WordPress

    # testimonies become an editable list at the top of the template and a loop in the page
    head = ''
    rows = testimonies.items(url)
    if rows:
        main, ok = testimonies.swap(main, testimonies.WP_LOOP)
        assert ok, 'testimony cards not found in ' + url
        head = testimonies.wp_list(rows)

    out = ("<?php\n"
           "/**\n"
           " * Template Name: %s\n"
           " *\n"
           " * Generated from dist%s/index.html by src/tools/wp_export.py.\n"
           " * Do not edit by hand (except the TESTIMONIES list, if there is one): ask the designer for a\n"
           " * change and this file is regenerated.\n"
           " */\n"
           "%s"
           "get_header();\n"
           "?>\n"
           "<main class=\"page-enter\">\n%s\n</main>\n"
           "<?php\n"
           "get_footer();\n") % (tname, url, head, main)
    os.makedirs(os.path.join(OUT, 'page-templates'), exist_ok=True)
    path = os.path.join(OUT, 'page-templates', fname)
    open(path, 'w', encoding='utf-8').write(out)
    return path, len(out)


FUNCTIONS = r"""<?php
/**
 * Our Social Foundation: loads the new design's stylesheet and scripts on its three page templates only.
 *
 * In the theme's functions.php add:
 *     require get_theme_file_path( 'functions-social-foundation.php' );
 */
add_action( 'wp_enqueue_scripts', function () {
	$templates = array(
		'page-templates/template-social-foundation.php',
		'page-templates/template-sf-i-am-not-afraid.php',
		'page-templates/template-sf-dare-to-dream.php',
	);
	if ( ! is_page_template( $templates ) ) {
		return;
	}
	wp_enqueue_style( 'cma-fonts', 'https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&family=Inter:wght@400;500;600&display=swap', array(), null );
	wp_enqueue_style( 'cma-main', get_theme_file_uri( 'assets/css/main.css' ), array( 'cma-fonts' ), '2026.11' );
	wp_enqueue_script( 'gsap', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js', array(), '3.12.5', true );
	wp_enqueue_script( 'gsap-st', 'https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js', array( 'gsap' ), '3.12.5', true );
	wp_enqueue_script( 'cma-main', get_theme_file_uri( 'assets/js/main.js' ), array( 'gsap-st' ), '2026.11', true );
}, 20 );
"""


if __name__ == '__main__':
    for url, fname, tname in PAGES:
        path, n = template(url, fname, tname)
        print('%-72s %6d bytes' % (os.path.relpath(path, ROOT), n))
    fpath = os.path.join(OUT, 'functions-social-foundation.php')
    open(fpath, 'w', encoding='utf-8').write(FUNCTIONS)
    print(os.path.relpath(fpath, ROOT))
