<?php
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
