{{-- Dare to Dream | Our Social Foundation | Coach Masters Academy
     Generated from dist/pages/our-social-foundation/dare-to-dream/index.html by src/tools/blade_export.py. Do not edit by hand (except
     the TESTIMONIES list, if there is one):
     ask the designer for a change and this file is regenerated.
     Change 'layouts.app' and the section names below to match the site's own layout. --}}
@extends('layouts.app')

@section('title', 'Dare to Dream | Our Social Foundation | Coach Masters Academy')
@section('meta_description', 'In February 2026, Dare to Dream brought graduating university students together with coaches from the CMA community for a three-day personal development camp in Colombo, Sri Lanka..')

@section('content')
{{-- TESTIMONIES (What our participants say)
     Add, edit or remove entries in this list. Each one is a card: name, the line under the
     name, and the words without quotation marks (they are added for you).
     To manage them in the admin instead, pass $testimonies from the controller in the same
     shape and this list is skipped. --}}
@php
    $testimonies = $testimonies ?? [
        ['name' => 'Sharu Vijayan', 'role' => 'Youth Camp 2026 participant', 'text' => 'The camp was well organized and engaging, and it created a safe space for learning, teamwork, and personal growth. The activities were meaningful, and the facilitators were very supportive. Overall, it was a memorable and enriching experience.'],
        ['name' => 'Priya Saththivel', 'role' => 'Youth Camp 2026 participant', 'text' => 'This workshop helped me to understand many aspects of achieving goal, self confidence, leadership skills, communication strategies, team work and how to handle a hard situation. Shared many things in night session that I have never shared with anyone and the coaches helped me to solve my problems.'],
        ['name' => 'Srinika Weerasundara', 'role' => 'Youth Camp 2026 participant', 'text' => 'Thank you for the guidance, support, and honesty that brought clarity to my thoughts and purpose to my life. You helped me see myself better and move forward with confidence. This experience and the people behind it will always be remembered'],
        ['name' => 'Hudha Haleem Ishak', 'role' => 'Youth Camp 2026 participant', 'text' => 'Being as a participant in multicultural and multinational program helped me a lot to build up my self in many ways. Learnt a lot through experience and practical. Thank you each and every individual who made this very special and unique!'],
        ['name' => 'Keshan Malinga', 'role' => 'Youth Camp 2026 participant', 'text' => 'The camp was very well organized and informative. The sessions were inspiring and helped improve leadership skills, teamwork, and confidence. Thank you to the organizers and trainers for a great experience.'],
        ['name' => 'Christina Jenifer', 'role' => 'Youth Camp 2026 participant', 'text' => 'This camp has given a moment to look at the star we always had in the heart, the courage to pursue it with a strong mentally. And I am really thankful for the every coaches that shared their valuable knowledge with us.'],
    ];
@endphp
{{-- If the layout already opens <main>, delete this wrapper and keep what is inside it. --}}
<main class="page-enter">
<nav class="subnav" aria-label="Section"><div class="container"><a href="{{ url('/about-us') }}">Who We Are</a><a href="{{ url('/pages/our-services') }}">Our Service</a><a href="{{ url('/pages/our-story') }}">Our Story</a><a href="{{ url('/icf-master-certified-coach-mcc') }}">Our Founder</a><a href="{{ url('/our-faculty') }}">Our Faculty</a><a href="{{ url('/pages/our-social-foundation') }}">Our Social Foundation</a><a href="{{ url('/events/gallery') }}">Gallery</a></div></nav>
<section class="page-hero page-hero--image">
  <img class="page-hero__photo" src="{{ asset('assets/img/hero/sf-dare-to-dream.jpg') }}" alt="" data-parallax="26">
  <div class="page-hero__scrim"></div>
  <div class="container"><div class="page-hero__narrow">
    
    <h1 data-split>Dare to Dream</h1>
    <p class="lead" data-reveal style="margin-top:22px"><span class="ev-meta"><span>Colombo, Sri Lanka</span> <span class="ev-meta__sep">|</span> <span>February 2026</span></span></p>
  </div></div>
</section><section class="section section--white ev-facts"><div class="container"><dl class="ev-facts__list" data-seq><div class="ev-fact" data-reveal><dt>Where</dt><dd>Colombo, Sri Lanka</dd></div><div class="ev-fact" data-reveal><dt>When</dt><dd>February 2026</dd></div><div class="ev-fact" data-reveal><dt>Format</dt><dd>Three-day camp</dd></div><div class="ev-fact" data-reveal><dt>For</dt><dd>Graduating university students</dd></div></dl></div></section><section class="section ev-story"><div class="container"><div class="ev-story__col"><h2 data-reveal>A Future Beyond the Expected</h2><p class="sf-lead" data-reveal>Big Heart. Big Smile. Leaving Our Footprints Behind.</p><p data-reveal>Graduation often makes the future feel unusually urgent. A first job, new responsibilities, a sensible plan. There is much to decide and no shortage of advice about what success should look like.</p><p data-reveal>Yet amid the pressure to decide what comes next, a more personal question can easily be overlooked: What kind of life do I truly want to create?</p><p data-reveal>In February 2026, <strong>Dare to Dream</strong> brought graduating university students together with coaches from the CMA community for a three-day personal development camp in Colombo, Sri Lanka.</p><p data-reveal>Through creative workshops, inspirational talks, experiential activities and coaching conversations, participants were encouraged to look beyond familiar possibilities, explore their deepest values and aspirations, and imagine futures they might not previously have considered.</p><p data-reveal>The invitation to dream bigger carried a deeper intention.</p><p class="sf-statement" data-reveal>Dreaming bigger is not necessarily about achieving more. It is about discovering what might become possible when we begin questioning the limits of what we have come to expect for ourselves.</p><p data-reveal>For young people entering a new stage of life, this exploration can be especially meaningful. It encourages them to consider the kind of success they wish to pursue, what they want their lives to stand for, and whether the direction they are contemplating genuinely reflects who they are.</p><p data-reveal>This speaks to an important dimension of CMA's transformational coaching approach: helping people broaden their perspectives and discover possibilities that may remain outside their present understanding.</p><p data-reveal>Beyond the learning activities, the three days were filled with warmth, laughter and the generosity of people sharing their experiences and aspirations. Coaches and young graduates connected through conversations that were as enriching as they were inspiring.</p><p data-reveal>There was a genuine sense of giving and receiving, with each person contributing something of themselves to the experience.</p><p class="ev-refrain" data-reveal>Big Heart. Big Smile. Leaving Our Footprints Behind.</p><p data-reveal>These words captured the spirit of the gathering. We came together for three days, but the kindness shared, the relationships formed and the conversations that touched us may continue to influence the lives of those who participated.</p><p data-reveal>We cannot know where these young graduates' dreams will eventually lead. Their futures remain theirs to discover and shape.</p></div></div></section><section class="section section--surface ev-reviews"><div class="container ev-reviews__layout"><div class="ev-reviews__head"><h2 data-reveal>What our participants say</h2></div><div class="ev-marquee" aria-label="Participant testimonies">
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
</div></div></section><section class="section section--green sf-band sf-band--closing"><div class="container"><p class="ev-closing" data-reveal>Our hope is that they leave with a wider sense of what is possible, a deeper appreciation of what matters to them, and the confidence to pursue dreams they may not previously have dared to imagine.</p></div></section><section class="section section--white sf-events"><div class="container"><div class="sf-events__grid sf-events__grid--one"><a class="card sf-event" href="{{ url('/pages/our-social-foundation/i-am-not-afraid') }}" data-reveal><p class="sf-event__meta"><span>Cambodia</span> <span class="ev-meta__sep">|</span> <span>February 2025</span></p><h3>I Am NOT Afraid</h3><p class="sf-event__sub">Putting Our Belief in People into Action</p><span class="link">Read the story<svg class="arrow" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 13 13 3M5 3h8v8"/></svg></span></a><a class="card sf-event sf-event--back" href="{{ url('/pages/our-social-foundation') }}" data-reveal><p class="sf-event__meta"><span>About Us</span></p><h3>Our Social Foundation</h3><span class="link">Back to the page<svg class="arrow" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 13 13 3M5 3h8v8"/></svg></span></a></div></div></section>
</main>
@endsection
