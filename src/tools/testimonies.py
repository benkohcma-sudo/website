"""Dare to Dream testimonies as an editable list for the WordPress and Laravel exports.

The static page prints the six cards as plain HTML. In the hand-over files the cards are
swapped for a list at the top of the template and a loop that prints the same markup, so
the developer (or the admin, through ACF in WordPress) can add, edit or remove a testimony
without touching the layout. Used by wp_export.py and blade_export.py.
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MARQUEE = re.compile(r'<div class="ev-marquee".*?</article></div></div></div>', re.S)
ROLE = 'Youth Camp 2026 participant'


def items(url):
    from pages_custom import SF_EVENTS
    ev = next((e for e in SF_EVENTS if e['url'] == url), None)
    if not ev or ev['media'].get('kind') != 'reviews':
        return None
    return ev['media']['items']


def _q(s):
    return "'" + s.replace('\\', '\\\\').replace("'", "\\'") + "'"


# ---------------------------------------------------------------- WordPress
def wp_list(rows):
    lines = ''.join("\tarray( 'name' => %s, 'role' => %s, 'text' => %s ),\n" % (_q(n), _q(ROLE), _q(t)) for n, t in rows)
    return ("/*\n"
            " * TESTIMONIES (What our participants say)\n"
            " * Add, edit or remove entries in this list. Each one is a card: name, the line under the\n"
            " * name, and the words without quotation marks (they are added for you).\n"
            " * With Advanced Custom Fields, a repeater field named 'testimonies' on this page (sub fields\n"
            " * 'name', 'role', 'text') replaces this list, so the admin can edit them in the page editor.\n"
            " */\n"
            "$cma_testimonies = array(\n" + lines + ");\n"
            "if ( function_exists( 'get_field' ) && ( $cma_rows = get_field( 'testimonies' ) ) ) {\n"
            "\t$cma_testimonies = array_values( $cma_rows );\n"
            "}\n")


WP_LOOP = """<div class="ev-marquee" aria-label="Participant testimonies">
<?php foreach ( array( 0, 1 ) as $cma_col ) :
	$cma_mine = array();
	foreach ( $cma_testimonies as $cma_i => $cma_t ) {
		if ( $cma_i % 2 === $cma_col ) { $cma_mine[ $cma_i ] = $cma_t; }
	} ?>
<div class="ev-marquee__col<?php echo $cma_col ? ' is-down' : ''; ?>" style="--dur:<?php echo count( $cma_mine ) * 11 + $cma_col * 6; ?>s"><div class="ev-marquee__inner">
<?php foreach ( array( false, true ) as $cma_dup ) : foreach ( $cma_mine as $cma_i => $cma_t ) : ?>
<article class="ev-rv"<?php echo $cma_dup ? ' aria-hidden="true"' : ''; ?>><div class="ev-rv__top"><span class="ev-rv__av ev-rv__av--<?php echo $cma_i % 3; ?>"><?php echo esc_html( mb_substr( $cma_t['name'], 0, 1 ) ); ?></span><div><p class="ev-rv__name"><?php echo esc_html( $cma_t['name'] ); ?></p><p class="ev-rv__meta"><?php echo esc_html( $cma_t['role'] ); ?></p></div></div><blockquote class="ev-rv__text">&ldquo;<?php echo esc_html( $cma_t['text'] ); ?>&rdquo;</blockquote><p class="ev-rv__foot">Shared on LinkedIn</p></article>
<?php endforeach; endforeach; ?>
</div></div>
<?php endforeach; ?>
</div>"""


# ---------------------------------------------------------------- Laravel Blade
def blade_list(rows):
    lines = ''.join("        ['name' => %s, 'role' => %s, 'text' => %s],\n" % (_q(n), _q(ROLE), _q(t)) for n, t in rows)
    return ("{{-- TESTIMONIES (What our participants say)\n"
            "     Add, edit or remove entries in this list. Each one is a card: name, the line under the\n"
            "     name, and the words without quotation marks (they are added for you).\n"
            "     To manage them in the admin instead, pass $testimonies from the controller in the same\n"
            "     shape and this list is skipped. --}}\n"
            "@php\n"
            "    $testimonies = $testimonies ?? [\n" + lines + "    ];\n"
            "@endphp\n")


BLADE_LOOP = """<div class="ev-marquee" aria-label="Participant testimonies">
@foreach ([0, 1] as $col)
@php $mine = collect($testimonies)->values()->filter(fn ($t, $i) => $i % 2 === $col); @endphp
<div class="ev-marquee__col{{ $col ? ' is-down' : '' }}" style="--dur:{{ $mine->count() * 11 + $col * 6 }}s"><div class="ev-marquee__inner">
@foreach ([false, true] as $dup)
@foreach ($mine as $i => $t)
<article class="ev-rv"{!! $dup ? ' aria-hidden="true"' : '' !!}><div class="ev-rv__top"><span class="ev-rv__av ev-rv__av--{{ $i % 3 }}">{{ mb_substr($t['name'], 0, 1) }}</span><div><p class="ev-rv__name">{{ $t['name'] }}</p><p class="ev-rv__meta">{{ $t['role'] }}</p></div></div><blockquote class="ev-rv__text">&ldquo;{{ $t['text'] }}&rdquo;</blockquote><p class="ev-rv__foot">Shared on LinkedIn</p></article>
@endforeach
@endforeach
</div></div>
@endforeach
</div>"""


def swap(main, loop):
    """Replace the printed cards with the loop; returns (main, replaced?)."""
    new, n = MARQUEE.subn(lambda _: loop, main, count=1)
    return new, bool(n)
