<?php
/*
| Our Social Foundation — three pages.
|
| Paste these three lines into routes/web.php.
| They must sit ABOVE any catch-all page route such as
|     Route::get('/pages/{slug}', ...)
| otherwise that route answers first and these never run.
*/

use Illuminate\Support\Facades\Route;

Route::view('/pages/our-social-foundation', 'social-foundation.index')->name('social-foundation');
Route::view('/pages/our-social-foundation/i-am-not-afraid', 'social-foundation.i-am-not-afraid')->name('social-foundation.i-am-not-afraid');
Route::view('/pages/our-social-foundation/dare-to-dream', 'social-foundation.dare-to-dream')->name('social-foundation.dare-to-dream');
