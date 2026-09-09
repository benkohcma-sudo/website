"""Hand-designed pages. All copy is verbatim from the live site (src/content/pages.json).
Text is written here only for layout; a verification script (src/verify.py) checks
that every sentence from the crawled page still appears in the generated one.
"""
import re, html
from bs4 import BeautifulSoup
from build import (PAGES, layout, page_hero, subnav, crumbs, btn, link, aside, esc, ARROW, PIN, generic_page, SITE, PHONE, EMAIL, page_heading, awards_band)

IMG = SITE + '/public/storage/'

def globe_scripts():
    return '<script src="/assets/js/globe-data.js"></script>'

# ====================================================================== HOME
def home(page):
    body = f'''
<section class="hv" data-home-hero>
  <video class="hv__video" muted playsinline preload="auto" poster="/assets/video/home-stairs-poster.jpg" aria-label="Walking up the staircase into a Coach Masters Academy classroom">
    <source src="/assets/video/home-stairs.mp4" type="video/mp4" media="(min-width: 900px)">
    <source src="/assets/video/home-stairs-720.mp4" type="video/mp4">
  </video>
  <div class="hv__scrim"></div>
  <div class="hv__scrim hv__scrim--end"></div>
  <div class="container hv__inner">
    <div class="hv__copy">
      <h1 class="hv__title">Your next chapter starts here.</h1>
      <p class="hv__sub">Move forward with clarity, confidence and purpose.</p>
      <a class="hv__btn" href="/icf-coaching-training-program">Explore Programmes <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></a>
    </div>
  </div>
  <div class="hv__end" data-hero-end>
    <div class="hv__end-inner">
      <h2>Welcome to Coach Masters Academy.</h2>
      <h3>Prepare our coaches to achieve Sustainable result for their clients</h3>
      <p>Coach Masters Academy develops coaches and leaders who coach with discipline, presence, and measurable impact. Through rigorous coaching education programs and deliberate practice, you build conceptual precision and applied capability to support meaningful, lasting change—across leadership practice, organisational performance, and the underlying patterns that shape professional and personal life.</p>
      <div class="hv__end-actions">
        {btn('Coaching Certification', '/icf-coaching-training-program')}
        {btn('Registration', '/registration', 'btn--ghost')}
      </div>
    </div>
  </div>
</section>

{awards_band()}

<section class="section">
  <div class="container split split--wide">
    <div class="media media--tall" data-reveal="scale"><img src="{IMG}featured_image1/Media.jpeg_1749727763" alt="" data-parallax="30"></div>
    <div>
      <h2 data-reveal>Advancing Human Potential <br>Through Global Coaching Certification</h2>
      <p data-reveal>Coach Masters Academy delivers globally accessible online courses for certification through flexible, interactive programs that support diverse schedules. Participants may join at their convenience across multiple programs designed to strengthen coaching capability and support long-term professional development within the coaching field.</p>
      <ul class="list-check" data-reveal>
        <li>As you pursue coach training, it is imperative to select a program with high standards, a proven methodology, and global recognition.</li>
        <li>Coach Masters Academy stands out as a leader in transformative learning. Our transformative coaching framework has been successfully implemented worldwide, enabling thousands of coaches and leaders to achieve sustainable outcomes.</li>
        <li>We take great pride in being at the forefront of transformative learning and are committed to providing our participants with the highest quality education possible.</li>
        <li>Our programs have supported the development of coaches who advance into reputed industry coaches.</li>
      </ul>
      <p data-reveal style="margin-top:28px">{btn('Read More', '/icf-coaching-training-program')}</p>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow" data-reveal>YOUR PATHWAY TO PROFESSIONAL COACH CREDENTIALING</p>
      <h2 data-reveal>ICF-Accredited Coaching Certification with Industry-leading Standards</h2>
      <p data-reveal>Our programmes are designed in alignment with the International Coaching Federation Core Competencies and ethical expectations, supporting participants to strengthen the capabilities associated with professional coaching: ethical practice, a coaching mindset, clear agreements, trust and safety, coaching presence, active listening, evoking awareness, and facilitating client growth.</p>
      <p data-reveal>Grounded in more than a decade of research and global field practice, our transformational coaching approach integrates disciplined theoretical inquiry with applied coaching skill. Participants learn a consistent, rigorous method for working with real change in real conversations—conversations that influence how people think, choose, lead, and relate.</p>
      <p class="lead" data-reveal><strong>Your journey towards mastering coaching begins with us.</strong></p>
    </div>
    <div class="grid grid-3">
      <a class="service" href="/icf-coaching-training-program" data-reveal>
        <img src="{IMG}image_item/services-1.jpg_1749723834" alt="">
        <div class="service__body"><h3>ICF COACHING CERTIFICATION PROGRAMS FOR ASPIRING COACHES</h3><p>Achieve personal mastery and a globally recognized professional coach certification.</p><span class="link">Read More{ARROW}</span></div>
      </a>
      <a class="service" href="/coaching-skill-training-course-and-workshop" data-reveal>
        <img src="{IMG}image_item/services-2.jpg_1749723874" alt="">
        <div class="service__body"><h3>INTERACTIVE WORKSHOPS AND PRACTICAL LABS FOR COACHES</h3><p>Equip leaders to integrate coaching skills as part of their managerial role to improve work engagement.</p><span class="link">Read More{ARROW}</span></div>
      </a>
      <a class="service" href="/executive-leadership-coaching-service-for-managers-and-leaders" data-reveal>
        <img src="{IMG}image_item/services-3.jpg_1749723934" alt="">
        <div class="service__body"><h3>EXECUTIVE COACHING CERTIFICATION IN LEADERSHIP DEVELOPMENT</h3><p>Accelerate your team and leaders’ effectiveness and efficiency for optimal performance with our leadership development program.</p><span class="link">Read More{ARROW}</span></div>
      </a>
    </div>
  </div>
</section>

<section class="section section--green">
  <div class="container split">
    <h2 data-reveal>Coaching Methodology Grounded in <br>Science for Sustainable Change</h2>
    <p class="lead" data-reveal style="color:#C7D4BF"> Our proprietary transformative coaching framework—the Awareness–Clarity–Choice Conversation—draws on research from positive psychology and transformative learning theory. It is designed to deepen awareness, surface assumptions, and support new meaning-making, enabling clients to clarify what matters most, expand their choices, and commit to actions that are coherent, values-aligned, and sustainable over time. </p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head" style="max-width:900px">
      <h2 data-reveal>Why Choose Coach Masters Academy for Your Life Coach Certification</h2>
      <p data-reveal>We know that developing mastery in coaching and acquiring the skills, attitudes, and competencies necessary to become truly professional requires a demanding curriculum that moves students beyond classroom concepts into participative coach-learning contexts. What makes our program truly transformative is that we go beyond skills and knowledge into the mastery of coaching. It provides a quality layered learning process where our students go through a formative process where the coaching competencies are forged and refined. We also offer flexible enrollment options across live-facilitated and online learning formats, supported by varied pricing structures and payment arrangements designed to make professional certification accessible while preserving academic rigor.</p>
    </div>
    <div class="feature-row">
      <div class="feature-row__media media" data-reveal="scale"><img src="{IMG}image_item/learning-1.jpg_1749727015" alt=""></div>
      <div data-reveal>
        <h3>Flexible Online Learning &amp; Global Coaching Network</h3>
        <ul>
          <li>Connect with coaches and leaders worldwide to <strong>develop your global coaching network</strong> for collaboration.</li>
          <li>Experience rich, diverse, and cross-cultural learning that <strong>prepares and positions you as a global citizen</strong></li>
          <li>An opportunity to <strong>accumulate coaching experience</strong> and pay back through our SAY Foundation, a non-profit charitable organization offering pro-bono coaching</li>
        </ul>
      </div>
    </div>
    <div class="feature-row">
      <div class="feature-row__media media" data-reveal="scale"><img src="{IMG}image_item/learning-2.jpg_1749727051" alt=""></div>
      <div data-reveal>
        <h3>Comprehensive Instructional Design</h3>
        <p><b>Accelerated learning </b>with carefully designed Learning Lab, Practical Lab, Practicum, Peer Peer Support and Coaching Supervision to develop your coaching competency.</p>
      </div>
    </div>
    <div class="feature-row">
      <div class="feature-row__media media" data-reveal="scale"><img src="{IMG}image_item/learning-3.jpg_1749727088" alt=""></div>
      <div data-reveal>
        <h3>Lifelong Support &amp; Continuous Learning For Coaches</h3>
        <p><b>Extensive post-training support</b> through our monthly learning webinars and live coaching demonstrations. Opportunities to serve as Student Mentors contribute to faculty-guided learning environments, while selected programs offer access to Continual Coach Education units through professional partnership frameworks.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container split">
    <div>
      <p class="eyebrow" data-reveal>Explore Our Signature Training Courses</p>
      <h2 data-reveal>Real-World Coaching Skills Developed with Industry Professionals</h2>
      <p data-reveal>Our in-depth, immersive professional coaching training course helps you develop your coaching mastery. Our coaching institute gives you an amazing opportunity to hone your skills under the proper supervision of professional coaches. We understand that there is a need for endless practice to become a great coach. Hence, our coach training program enables you to experience in-depth coaching practice.</p>
      <p data-reveal>With our transformative coach certification program, you will get comprehensive training that can help you become the best coach. Our transformative coaching can enhance your coaching skills and awareness if you already offer professional coaching services.</p>
      <p data-reveal>If you have always wanted to help others genuinely and have dreamt about doing the kind of work that can bring a massive difference in people's lives, join the coaching skill course of this renowned coaching Academy.</p>
    </div>
    <div class="cta-band" data-reveal="scale">
      <p class="eyebrow" style="color:#F3A77F">Live Coaching Discovery Sessions</p>
      <h2>Join a Live Coaching Experience &amp; Gain Practical Insight</h2>
      <p>Explore coaching online through our FREE Live Webinar. Investing in coach training (or any training for that matter) can be a complex decision and that is why we want to help you to make an informed decision.</p>
      <p>You can join us in any of the upcoming webinars to observe a live coaching demonstration and gain first-hand experience of our coaching approach and learning culture. These sessions also provide opportunities to interact with our coaches and facilitators, ask questions, and engage in professional dialogue.</p>
      {btn('Click Here For Register', '/webinar')}
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="chips" data-reveal>
      <span class="chip-tile"><img src="{IMG}image_item/4/expertise-image-1.jpg" alt="">communication coaching</span>
      <span class="chip-tile"><img src="{IMG}image_item/5/expertise-image-2.jpg" alt="">Personal Coaching</span>
      <span class="chip-tile"><img src="{IMG}image_item/6/expertise-image-3.jpg" alt="">Strategy</span>
      <span class="chip-tile"><img src="{IMG}image_item/7/expertise-image-4.jpg" alt="">Productivity &amp; Efficiency Coaching</span>
      <span class="chip-tile"><img src="{IMG}image_item/8/expertise-image-5.jpg" alt="">Education</span>
      <span class="chip-tile"><img src="{IMG}image_item/9/expertise-image-6.jpg" alt="">Leadership</span>
      <span class="chip-tile"><img src="{IMG}image_item/10/expertise-image-7.jpg" alt="">Coaching Certification</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split split--wide">
    <div>
      <h2 data-reveal>Download Full Program Brochure &amp; Curriculum Guide</h2>
      <p class="lead" data-reveal>Receive the brochure, schedule of training by completing the form below</p>
    </div>
    <div class="prose prose--wide" data-reveal>
      <!-- CMS: brochure form posts to backend (download_programpack); country list supplied by backend -->
      <form action="" method="post" name="download_programpack">
        <input name="down_username" placeholder="Name *" type="text">
        <input name="down_email" placeholder="Email *" type="text">
        <input name="down_number" placeholder="Mobile Number *" type="text">
        <select name="down_country"><option value="">Select Country</option></select>
        <select name="down_intrest">
          <option value="">Select Your Interest</option>
          <option value="Curiosity">Curiosity</option>
          <option value="Gathering Information">Gathering Information</option>
          <option value="Personal Development">Personal Development</option>
          <option value="Obtain Coaching Certification">Obtain Coaching Certification</option>
          <option value="Others">Others</option>
        </select>
        <textarea name="down_message" placeholder="Message *" rows="3"></textarea>
        <input name="recaptcha_token" type="hidden">
        <button type="submit">Submit</button>
        <p>By submitting this form, you acknowledge that Coach Masters Academy will use this information to contact you.</p>
      </form>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container center">
    <p class="eyebrow" data-reveal>STRATEGIC ALLIANCES WITH GLOBAL COACHING INSTITUTIONS</p>
    <h2 data-reveal>Trusted Partnerships with Leading Coaching Experts &amp; Organizations</h2>
    <p class="lead" data-reveal>Coach Masters Academy collaborates with ICF-aligned bodies and respected coaching organizations to uphold training quality, support global recognition, and extend professional networks.</p>
  </div>
  <div class="marquee" style="margin-top:40px" data-reveal="none">
    <div class="marquee__track">
      <div class="logo-tile"><img src="{IMG}image_item/partner-1.png_1749732353" alt=""></div>
      <div class="logo-tile"><img src="{IMG}image_item/partner-2.png_1749732381" alt=""></div>
      <div class="logo-tile"><img src="{IMG}image_item/partner-3.png_1749732426" alt=""></div>
      <div class="logo-tile"><img src="{IMG}image_item/partner-4.png_1749732477" alt=""></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow" data-reveal>WHAT OUR CLIENT SAYS</p>
      <h2 data-reveal>Hear what our clients shared about their learning experiences with us. </h2>
    </div>
  </div>
  <div class="marquee" data-reveal="none">
    <div class="marquee__track" style="animation-duration:70s">
      {quote('Coach Masters Academy puts the "Masterful" into Masterful coaching and training. The Faculty Team knows how to bring the best out of people. Training with CMA has allowed me to surpass what I thought was possible and reach a level of understanding and confidence in my coaching skills beyond what I initially aimed for. But it was more than just an education, and it was "Life-Changing”.', 'CHARL SWART', 'MANAGING DIRECTOR I', SITE + '/siteimages/testimonial/testimonial8985751011544702739.jpg')}
      {quote('I have a paradigm shift on what is truly transformative coaching compare with conventional coaching. This training offers me deep insights into the essence of powerful asking and active listening needed for effective coaching. What I really appreciate is the continual professional development and it clearly shows the commitment of the academy. ', 'Swandajani Gunadi', 'Director - Chief of Human Capital and Chief of Marketing for Adira Finance', SITE + '/siteimages/testimonial/1493961869_31_SwandajaniGunadi.jpg')}
      {quote('The Master Trainer is an amazing individual with 100% passion for passing on in an engaging and energetic way the essential skills required to be a successful Professional Coach. His delivery has such outstanding clarity that he makes the content of his training truly practical and memorable.', 'Howard Bryant', 'Managing Director of Retails Asia Limited', SITE + '/siteimages/testimonial/1493961890_32_HowardBryant.jpg')}
      {quote('CMA maintains a high standard in the delivery with useful materials, impactful videos, and lots of opportunities for reflection and practice. The learning through listening to coaching conversation follows by in-depth discussion provides a rich resource that helps us to map theory with application and I find it to be extremely invaluable accelerating our competencies. The academy also provides many good platforms for post-training learning where we can learn from various Supervisors across the globe. It allows me to apply my skills outside the classroom learning context.', 'Elvin Tay', 'Senior Learning Consultant', SITE + '/siteimages/testimonial/1500551171_42_Elvin Tay.jpg')}
      {quote('An amazing program that truly creates space and creativity for people to be empowered with the knowledge they already possess inside. A life-changing experience. I would highly recommend it for anybody influencing leaders or looking to create positive change in people.', 'Amy Styles', 'National Training Manager', SITE + '/siteimages/testimonial/1493961938_36_amy.jpg')}
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="container">
    <div class="section-head section-head--row">
      <div>
        <p class="eyebrow" data-reveal>LATEST INSIGHTS &amp; UPDATES</p>
        <h2 data-reveal>Latest News, Insights &amp; Upcoming Events in Coaching</h2>
      </div>
      <p data-reveal>{link('View all news', '/events/news')}</p>
    </div>
    <div class="grid grid-4">
      {news_card('/events/news/icf-approved-coaching-certificate-training-program-in-australia-melbourne', SITE + '/siteimages/news/206/20216049501581844265_206_An Evidence-Based Coaching Approach.jpg', 'ICF Approved Coaching Certificate Training  Program in Australia - Melbourne')}
      {news_card('/events/news/icf-approved-coaching-certificate-training-program-and-course-in-canada-toronto', SITE + '/siteimages/news/207/4158957841581921546_207_Core Training for Professional Coaching 9.png', 'ICF Approved Coaching Certificate Training  Program and Course in Canada, Toronto')}
      {news_card('/events/news/icf-approved-coaching-certification-training-program-and-course-in-botswana-gaborone', SITE + '/siteimages/news/204/380792511581826526_204_Evocative Inside-out Approach 6.png', 'ICF Approved Coaching Certification Training Program and Course in Botswana, Gaborone')}
      {news_card('/events/news/icf-approved-coaching-certification-training-program-and-course-in-zimbabwe-harare', SITE + '/siteimages/news/205/11598867891581835024_205_Core Training for Professional Coaching 3.jpg', 'ICF Approved Coaching Certification Training Program and Course in Zimbabwe, Harare')}
    </div>
  </div>
</section>'''
    return layout(page, body, body_class='is-home')

def quote(text, name, role, img):
    return f'''<div class="quote-card"><span class="q">“</span><p>{text}</p><div class="who"><img src="{esc(img)}" alt=""><div><b>{esc(name)}</b><span>{esc(role)}</span></div></div></div>'''

def news_card(href, img, title, reveal=True):
    return f'''<article class="card card--image"{' data-reveal' if reveal else ''}>
  <a class="card__media" href="{esc(href)}"><img src="{esc(img)}" alt="" loading="lazy"></a>
  <div class="card__body"><h3><a href="{esc(href)}">{title}</a></h3>{link('read more', href)}</div>
</article>'''

# ====================================================================== ABOUT US (globe hero)
def about(page):
    body = subnav(page) + f'''
<section class="globe-hero globe-hero--video">
  <video class="globe-video__el" muted playsinline preload="auto" poster="/assets/video/about-globe-poster.jpg" aria-label="Globe turning from the Americas to Singapore">
    <source src="/assets/video/about-globe.mp4" type="video/mp4">
  </video>
  <div class="container globe-hero__inner">
    <div class="globe-hero__stage">
      <div class="globe-hero__copy">
        <h1 data-split>Inspiring Positive Change Through mastery of coaching.</h1>
        <div class="globe-hero__swap">
          <p class="lead globe-hero__lead">At Coach Masters Academy, we take great pride in our unwavering dedication to enhancing professional coaching standards and empowering coaches and leaders to drive transformative change and deliver impactful results.</p>
          <div class="globe-stats globe-stats--reveal" aria-live="polite">
            <div class="stat"><div class="stat__num" data-count="5">0</div><div class="stat__label">Continents Actively Present</div></div>
            <div class="stat"><div class="stat__num" data-count="10">0</div><div class="stat__label">Regional Offices</div></div>
            <div class="stat"><div class="stat__num" data-count="58">0</div><div class="stat__label">Faculty Members</div></div>
            <div class="stat"><div class="stat__num" data-count="6200">0</div><div class="stat__label">Graduates across the globe</div></div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="globe-hint"><i></i><span>Scroll to spin</span></div>
</section>

<section class="section">
  <div class="container split split--wide">
    <div class="media-stack" data-reveal="scale">
      <div class="media media--tall media--blob"><img src="{IMG}featured_image1/1/about-us-img-1.jpg" alt="" data-parallax="24"></div>
      <div class="media media--square"><img src="{IMG}featured_image2/1/about-us-img-2.jpg" alt=""></div>
      <div class="badge-float"><img src="{SITE}/public/twenty25/images/icon-company-experience.svg" alt="" width="40" height="40"><div><b>30+</b><span>years of experience</span></div></div>
    </div>
    <div>
      <blockquote class="prose" data-reveal style="max-width:none">“ We have always been driven by a mission to create profound shifts in coaching conversations through meaningful dialogue, facilitating more transformational change. ”</blockquote>
      <ul class="list-check" data-reveal style="margin-top:28px">
        <li>goal setting and accountability</li>
        <li>mindset and confidence building</li>
      </ul>
      <div data-reveal style="display:flex;align-items:center;gap:18px;margin-top:34px;flex-wrap:wrap">
        <div style="display:flex">{''.join(f'<img src="{SITE}/public/twenty25/images/satisfy-client-img-{i}.jpg" alt="" style="width:44px;height:44px;border-radius:50%;object-fit:cover;border:3px solid var(--bg);margin-left:{-12 if i>1 else 0}px">' for i in range(1,6))}</div>
        <p style="margin:0;font-family:var(--font-head);color:var(--ink)">Join our 5000+ satisfied client</p>
      </div>
      <div class="card" data-reveal style="margin-top:36px;display:flex;gap:18px;align-items:center;padding:22px 26px">
        <div class="card__icon" style="margin:0;flex:none"><img src="{SITE}/public/twenty25/images/icon-company-result.svg" alt="" width="26" height="26"></div>
        <div><h3 style="margin:0 0 2px">5200+ five star reviews</h3><p style="margin:0">Creative Result · Award wining</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    <div class="section-head center" style="margin-inline:auto">
      <h2 data-reveal>A Vision to Inspire Positive Change through  Mastery of Coaching</h2>
    </div>
    <a class="video-cta" href="https://www.youtube.com/watch?v=NAVllbMOilw" target="_blank" rel="noopener" data-reveal="scale">
      <img src="{IMG}featured_image1/2/our-potential-img.jpg" alt="" data-parallax="40">
      <div style="position:relative;z-index:1;display:grid;justify-items:center"><div class="play"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></div><span>watch video</span></div>
    </a>
  </div>
</section>

<section class="section section--green">
  <div class="container split">
    <div>
      <p class="eyebrow" data-reveal style="color:#F3A77F">Mission</p>
      <h2 data-reveal>Our  Mission</h2>
      <p class="lead" data-reveal style="color:#C7D4BF">Empower You To Be an Effective Change Agent By delivering high-quality coaching education and coaching service</p>
    </div>
    <ul class="list-check" data-reveal style="color:#DDE7D6">
      <li>Our coaching program empowers you with the skills and knowledge to drive impactful change.</li>
      <li>Grounded in scientific research and best practices, our approach facilitates profound learning.</li>
      <li>It enables significant transformations that resonate well beyond individual sessions, ensuring lasting results in your personal and professional life.</li>
    </ul>
  </div>
</section>

{faculty_section(PAGES['/our-faculty'], compact=True)}
'''
    return layout(page, body, extra_js=globe_scripts())

# ====================================================================== OUR STORY (curved journey)
def story(page):
    soup = BeautifulSoup(page['content'], 'lxml')
    items = []
    for li in soup.select('ul li'):
        h2 = li.find('h2'); p = li.find('p'); h3 = li.find('h3')
        if h2 and h3: items.append((h3.get_text(strip=True), h2.decode_contents().strip(), p.decode_contents().strip() if p else ''))
    milestones = ''.join(f'''
      <li class="milestone">
        <div class="milestone__card">
          <div class="milestone__year">{esc(y)}</div>
          <h3>{t}</h3>
          <p>{d}</p>
        </div>
      </li>''' for y, t, d in items)
    body = subnav(page) + f'''
<section class="page-hero">
  <div class="container">
    {crumbs(page)}
    <h1 data-split>Our Story</h1>
  </div>
</section>
<section class="section section--tight">
  <div class="container split split--wide">
    <div class="media media--tall media--blob" data-reveal="scale"><img src="{IMG}featured_image1/3/team-member.jpg" alt="image" data-parallax="24"></div>
    <div>
      <p class="eyebrow" data-reveal>Dr. Ben Koh's - Founder</p>
      <h2 data-reveal>Unassuming Beginning with a Noble Mission</h2>
      <p class="lead" data-reveal>Dr. Ben Koh's pioneering spirit and strong belief in transformational coaching established our foundation in 2010 within the education sector of Kazakhstan. Today, we are a leading global coaching academy. We take pride in our rich legacy, which spans a decade of milestones, including our notable rebranding to align with our international goals. We want our story to inform and inspire you to embark on this coaching educational journey with us.</p>
      <p data-reveal style="display:flex;gap:14px;align-items:center;flex-wrap:wrap">
        <span class="pill pill--green">co founder</span>
        <a class="link" href="https://www.linkedin.com/in/benkohkt/" target="_blank" rel="noopener">LinkedIn{ARROW}</a>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="journey">
      <svg class="journey__svg" aria-hidden="true">
        <path class="track" d=""/>
        <path class="draw" d=""/>
        <circle class="halo" r="14"/>
        <circle class="dot" r="6"/>
      </svg>
      <ol class="journey__list">{milestones}</ol>
    </div>
  </div>
</section>
{cta_band()}'''
    return layout(page, body)

def cta_band():
    return f'''
<section class="section section--tight">
  <div class="container">
    <div class="cta-band" data-reveal="scale">
      <p class="eyebrow" style="color:#F3A77F">Registration</p>
      <h2>Your journey towards mastering coaching begins with us.</h2>
      <p>You can call our Global Office at +65-8299-8170 to explore which entry point and advanced structure best fit your experience, goals, and context.</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap">{btn('Registration', '/registration')}{btn('Schedule a Call', 'https://calendly.com/coachmastersacademyglobaloffice/30min-phone-call-appointment', 'btn--white')}</div>
    </div>
  </div>
</section>'''

# ====================================================================== OUR FACULTY (carousel like the reference)
def parse_faculty(page):
    soup = BeautifulSoup(page['content'], 'lxml')
    groups = []; cur = None; pending_img = None
    for el in soup.body.children if soup.body else soup.children:
        name = getattr(el, 'name', None)
        if name == 'h2':
            cur = {'title': el.get_text(strip=True), 'people': []}; groups.append(cur)
        elif name == 'img': pending_img = el.get('src')
        elif name == 'h3' and cur is not None:
            cur['people'].append({'name': el.get_text(' ', strip=True), 'img': pending_img, 'role': ''}); pending_img = None
        elif name == 'p' and cur is not None and cur['people'] and not cur['people'][-1]['role']:
            cur['people'][-1]['role'] = el.get_text(' ', strip=True)
    return [g for g in groups if g['people']]

def split_person(p):
    """Name / credential / role / location, all taken from the two verbatim CMS lines.
    Only whitespace is normalised; no wording is changed."""
    full = re.sub(r'\s+', ' ', p['name']).strip()
    role = re.sub(r'\s+', ' ', p['role']).strip()
    name = full; cred = ''
    if ' I ' in full: name, cred = [x.strip() for x in full.split(' I ', 1)]
    parts = [x.strip() for x in role.split(' I ') if x.strip()]
    loc = parts[-1] if len(parts) > 1 else ''
    return {'name': name, 'cred': cred, 'role': role, 'loc': loc, 'img': p['img'] or ''}

def feature_card(d):
    """The large card. Its content is swapped by JS when another person is selected."""
    return f'''<article class="person person--feature" data-feature>
  <div class="person__photo"><img src="{esc(d['img'])}" alt="{esc(d['name'])}" data-f-img></div>
  <div class="person__body">
    <h3 data-f-name>{esc(d['name'])}</h3>
    <p class="role role--cred" data-f-cred>{esc(d['cred'])}</p>
    <p class="role" data-f-role>{esc(d['role'])}</p>
    <div class="loc" data-f-locwrap>{PIN}<span data-f-loc>{esc(d['loc'])}</span></div>
    {link('View profile', '/our-faculty')}
  </div>
</article>'''

def person_card(p):
    d = split_person(p)
    return f'''<button class="person person--sm" type="button"
  data-name="{esc(d['name'])}" data-cred="{esc(d['cred'])}" data-role="{esc(d['role'])}" data-loc="{esc(d['loc'])}" data-img="{esc(d['img'])}"
  aria-label="Show {esc(d['name'])}">
  <span class="person__photo"><img src="{esc(d['img'])}" alt="{esc(d['name'])}" loading="lazy"></span>
  <span class="person__body">
    <span class="person__name">{esc(d['name'])}</span>
    {f'<span class="role">{esc(d["cred"])}</span>' if d['cred'] else ''}
    <span class="role">{esc(d['role'])}</span>
    {f'<span class="loc">{PIN}<span>{esc(d["loc"])}</span></span>' if d['loc'] else ''}
  </span>
</button>'''

def faculty_section(page, compact=False):
    groups = parse_faculty(page)
    first = split_person(groups[0]['people'][0]) if groups and groups[0]['people'] else {'name': '', 'cred': '', 'role': '', 'loc': '', 'img': ''}
    tabs = ''.join(f'<button type="button"{" class=is-active" if i == 0 else ""}>{esc(g["title"])}</button>' for i, g in enumerate(groups))
    tracks = ''.join('<div class="faculty__track"' + (' hidden' if i else '') + '>' + ''.join(person_card(p) for p in g['people']) + '</div>' for i, g in enumerate(groups))
    n0 = len(groups[0]['people']) if groups else 0
    return f'''
<section class="section faculty">
  <div class="container">
    <div class="faculty__head">
      <div>
        <p class="eyebrow" data-reveal>Our Global Faculty</p>
        <h2 data-reveal>Meet the minds behind meaningful change.</h2>
        <p class="lead" data-reveal>World-class coaches, trainers and thought leaders united by a shared purpose: to elevate coaching, empower people and shape a better future together.</p>
      </div>
      <div class="faculty__controls" data-reveal>
        <button class="arrow-btn" type="button" data-prev aria-label="Previous"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5m7-7-7 7 7 7"/></svg></button>
        <div><div class="counter">01 <span>/ {n0:02d}</span></div><div class="bar" style="margin-top:8px"><i></i></div></div>
        <button class="arrow-btn arrow-btn--accent" type="button" data-next aria-label="Next"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14m-7-7 7 7-7 7"/></svg></button>
      </div>
    </div>
    <div class="tabs" role="tablist" data-reveal="none">{tabs}</div>
    <div class="faculty__stage">
      <canvas class="faculty__map" aria-hidden="true"></canvas>
      <svg class="faculty__line" viewBox="0 0 1200 40" preserveAspectRatio="none" aria-hidden="true"><path d="M0 20 C 200 -10, 400 50, 600 20 S 1000 -10, 1200 20" fill="none" stroke="#eb6422" stroke-width="1.5" stroke-dasharray="4 6" opacity=".6"/></svg>
      {feature_card(first)}
      {tracks}
    </div>
  </div>
</section>'''

def faculty(page):
    body = subnav(page) + f'''
<section class="page-hero" style="padding-bottom:0">
  <div class="container">{crumbs(page)}<h1 data-split>Our Faculty</h1></div>
</section>
{faculty_section(page)}
{cta_band()}'''
    return layout(page, body, extra_js=globe_scripts())

# ====================================================================== registry
RENDERERS = {
    '/': home,
    '/about-us': about,
    '/pages/our-story': story,
    '/our-faculty': faculty,
}
PREFIX_RENDERERS = []


# ====================================================================== shared parsers for listings
def top_nodes(content):
    soup = BeautifulSoup(content, 'lxml')
    root = soup.body or soup
    return [n for n in root.children if getattr(n, 'name', None) or (str(n).strip())]

def card_groups(content):
    """Split flat listing markup into cards. A new card starts at each image (or link wrapping an image)."""
    groups = []; cur = None
    for n in top_nodes(content):
        name = getattr(n, 'name', None)
        img = n if name == 'img' else (n.find('img') if name == 'a' else None)
        if img is not None:
            cur = {'img': img.get('src'), 'alt': img.get('alt', ''), 'href': n.get('href') if name == 'a' else '', 'title': '', 'date': '', 'excerpt': '', 'links': []}
            groups.append(cur); continue
        if cur is None: continue
        if name in ('h2', 'h3', 'h4', 'h5', 'h6'):
            t = n.get_text(' ', strip=True)
            if not t: continue
            if name == 'h5' and re.match(r'^\d{1,2}\s+\w{3}', t) and not cur['date']: cur['date'] = t
            elif not cur['title']: cur['title'] = t; a = n.find('a'); cur['href'] = cur['href'] or (a.get('href') if a else '')
        elif name == 'p':
            t = n.get_text(' ', strip=True)
            if t and not cur['excerpt']: cur['excerpt'] = t
        elif name == 'a':
            t = n.get_text(' ', strip=True)
            if n.get('href'): cur['links'].append((t, n['href'])); cur['href'] = cur['href'] or n['href']
        elif isinstance(n, str) and not cur['title']:
            cur['title'] = n.strip()
    return groups

def pagination_html(content):
    """Keep the site's pagination links (Next », page numbers, 'Showing x to y of z results')."""
    soup = BeautifulSoup(content, 'lxml')
    links = [a for a in soup.find_all('a', href=True) if 'page=' in a['href'] or a.get_text(strip=True) in ('Next »', '« Previous')]
    showing = next((p.get_text(' ', strip=True) for p in soup.find_all('p') if 'Showing' in p.get_text()), '')
    if not links and not showing: return ''
    seen = set(); out = []
    for a in links:
        key = (a['href'], a.get_text(strip=True))
        if key in seen: continue
        seen.add(key); out.append(f'<a href="{esc(a["href"])}">{esc(a.get_text(strip=True))}</a>')
    return f'<div class="pagination" data-reveal>{"".join(out)}</div>' + (f'<p class="muted" style="margin-top:14px;font-size:14px">{esc(showing)}</p>' if showing else '')

def intro_html(content, stop_at_first_card=True):
    """Everything before the first card (headline copy, filters) rendered as prose."""
    out = []
    for n in top_nodes(content):
        name = getattr(n, 'name', None)
        if name == 'img' or (name == 'a' and n.find('img')): break
        out.append(str(n))
    return ''.join(out)

def outro_html(content):
    """Markup after the last card's Read-more link (pagination, category lists) kept verbatim."""
    nodes = top_nodes(content); last = -1
    for i, n in enumerate(nodes):
        if getattr(n, 'name', None) == 'img' or (getattr(n, 'name', None) == 'a' and n.find('img')): last = i
    if last < 0: return ''
    # skip the card's own title/excerpt/link, then keep the rest
    j = last + 1; seen_link = False
    while j < len(nodes):
        n = nodes[j]; name = getattr(n, 'name', None)
        if name == 'a' and seen_link is False and n.get_text(strip=True): seen_link = True; j += 1; break
        if name in ('h2','h3','h4','h5','h6','p') or isinstance(n, str) or name == 'a': j += 1; continue
        break
    return ''.join(str(n) for n in nodes[j:])

def listing_page(page, heading=None, kind='cards'):
    groups = card_groups(page['content'])
    outro = outro_html(page['content'])
    intro = intro_html(page['content'])
    intro = re.sub(r'<ul>\s*(<li>\s*<a href="[^"]*calendar[^"]*">.*?</a>\s*</li>\s*)+</ul>', '', intro, flags=re.S)  # calendar type tabs handled by table
    if kind == 'gallery':
        cards = ''.join(f'<figure data-reveal><img src="{esc(g["img"])}" alt="{esc(g["alt"] or g["title"])}" loading="lazy"><figcaption>{esc(g["title"])}</figcaption></figure>' for g in groups if g['img'] and 'banner' not in g['img'])
        grid = f'<div class="gallery-grid">{cards}</div>'
    else:
        cards = ''
        for g in groups:
            if not g['title'] or 'banner' in (g['img'] or ''): continue
            href = g['href'] or '#'
            more = next((t for t, h in g['links'] if t), 'Read More')
            cards += f'''<article class="card card--image" data-reveal>
  <a class="card__media" href="{esc(href)}"><img src="{esc(g['img'])}" alt="{esc(g['alt'])}" loading="lazy"></a>
  <div class="card__body">{f'<span class="pill" style="margin-bottom:12px">{esc(g["date"])}</span>' if g['date'] else ''}<h3><a href="{esc(href)}">{esc(g['title'])}</a></h3>{f'<p>{esc(g["excerpt"])}</p>' if g['excerpt'] else ''}{link(more, href)}</div>
</article>'''
        grid = f'<div class="grid grid-3">{cards}</div>'
    body = subnav(page) + page_hero(page, heading) + f'''
<section class="section section--tight">
  <div class="container">
    {f'<div class="prose prose--wide" data-auto-reveal style="margin-bottom:48px">{intro}</div>' if intro.strip() else ''}
    {grid}
    {f'<div class="prose prose--wide listing-outro" data-auto-reveal>{outro}</div>' if outro.strip() else ''}
  </div>
</section>'''
    return layout(page, body)

def blog_listing(page): return listing_page(page, page.get('h1') or 'Resource')
def news_listing(page): return listing_page(page, 'News')
def gallery_listing(page): return listing_page(page, 'Gallery', kind='gallery')
def workshops_listing(page): return listing_page(page, 'Workshops')

def wide_page(page, heading=None):
    """Long-form pages that need the full width (tables, calendars, forms)."""
    content = re.sub(r'^\s*<h1>.*?</h1>', '', page['content'], count=1, flags=re.S)
    body = subnav(page) + page_hero(page, heading) + f'''
<section class="section section--tight">
  <div class="container"><div class="prose prose--wide" data-auto-reveal>{content}</div></div>
</section>'''
    return layout(page, body)

def calendar_page(page): return wide_page(page, 'Schedule')
def webinar_page(page): return wide_page(page, 'Webinar')
def registration_page(page): return wide_page(page, 'Registration')

def blog_post(page):
    content = re.sub(r'^\s*<h1>.*?</h1>', '', page['content'], count=1, flags=re.S)
    # first image becomes the hero media; the h5 date becomes a pill; drop the repeated h3 title
    m = re.search(r'^\s*<img[^>]*src="([^"]+)"[^>]*>', content)
    hero_img = ''
    if m: hero_img = m.group(1); content = content[m.end():]
    d = re.search(r'^\s*<h5>(.*?)</h5>', content, re.S); date = ''
    if d: date = d.group(1).strip(); content = content[d.end():]
    content = re.sub(r'^\s*<h3>\s*' + re.escape(html.escape(page['h1'], quote=False)) + r'\s*</h3>', '', content, count=1)
    body = f'''
<section class="page-hero">
  <div class="container">
    {crumbs(page)}
    {f'<span class="pill" style="margin-bottom:18px">{esc(date)}</span>' if date else ''}
    <h1 data-split>{esc(page['h1'])}</h1>
    {f'<div class="page-hero__banner" data-reveal="scale"><img src="{esc(hero_img)}" alt="" data-parallax="30"></div>' if hero_img else ''}
  </div>
</section>
<section class="section section--tight landing">
  <div class="container"><div class="prose prose--wide" data-auto-reveal>{content}</div></div>
</section>'''
    return layout(page, body)

# ====================================================================== COACHING CERTIFICATION (pathway journey)
def certification(page):
    c = page['content']
    # 1. stats block
    m = re.search(r'<h2>(Proven Success[^<]*)</h2>\s*<p>(\d+)</p>\s*<p>([^<]+)</p>\s*<p>(\d+)</p>\s*<p>([^<]+)</p>', c)
    stats = ''
    if m:
        stats = f'''
<section class="section section--green section--tight">
  <div class="container">
    <h2 data-reveal style="max-width:20ch">{m.group(1)}</h2>
    <div class="stats" style="grid-template-columns:repeat(2,1fr);max-width:720px">
      <div class="stat" data-reveal><div class="stat__num" data-count="{m.group(2)}">0</div><div class="stat__label">{m.group(3)}</div></div>
      <div class="stat" data-reveal><div class="stat__num" data-count="{m.group(4)}">0</div><div class="stat__label">{m.group(5)}</div></div>
    </div>
  </div>
</section>'''
        c = c.replace(m.group(0), '')
    # 2. the four Advantages (accordion) -> curved journey
    details = re.findall(r'<details>\s*<summary>(.*?)</summary>(.*?)</details>', c, re.S)
    journey = ''
    if details:
        items = ''.join(f'<li class="milestone"><div class="milestone__card"><div class="milestone__year">Advantage {i+1:02d}</div><h3>{t.strip()}</h3><p>{re.sub(r"</?p>", "", b).strip()}</p></div></li>' for i, (t, b) in enumerate(details))
        journey = f'''
<div class="journey" style="margin-top:56px">
  <svg class="journey__svg" aria-hidden="true"><path class="track" d=""/><path class="draw" d=""/><circle class="halo" r="14"/><circle class="dot" r="6"/></svg>
  <ol class="journey__list">{items}</ol>
</div>'''
        c = re.sub(r'(<details>.*?</details>\s*)+', '@@JOURNEY@@', c, count=1, flags=re.S)
    # 2b. the accreditation strip (a flattened jpeg on the live site) -> the transparent badges
    BADGES = [('icf-level-1', 'ICF Level 1 accredited coaching education'), ('icf-level-2', 'ICF Level 2 accredited coaching education'),
              ('icf-level-3', 'ICF Level 3 accredited coaching education'), ('icf-aatc', 'ICF Advanced Accreditation in Team Coaching'),
              ('icf-cce', 'ICF Continuing Coach Education'), ('coaching-impact-award', 'ICF Coaching Impact Award')]
    grid = '<div class="badge-strip" data-strip>' + ''.join(f'<img src="/assets/img/badges/{f}.png" alt="{a}" loading="lazy">' for f, a in BADGES) + '</div>'
    c = re.sub(r'<img[^>]*src="data:image/jpeg[^"]*"[^>]*>', grid, c, count=1)
    # 3. track cards (icon, h3, p, p, picture) -> feature rows
    tracks = re.findall(r'<img[^>]*entry-level-icon1\.png"[^>]*>\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>\s*(<p>.*?</p>)\s*(?:<img[^>]*src="([^"]+)"[^>]*>)?', c, re.S)
    rows = ''
    if tracks:
        PAIRS = [('icf-acc', 'ICF Associate Certified Coach', 'cma-certified-professional-coach', 'Certified Professional Coach'),
                 ('icf-pcc', 'ICF Professional Certified Coach', 'cma-advanced-practitioner-cpc', 'Advanced Practitioner Certified Professional Coach'),
                 ('icf-mcc', 'ICF Master Certified Coach', 'cma-advanced-practitioner-cpc', 'Advanced Practitioner Certified Professional Coach'),
                 ('icf-team-coaching', 'ICF Team Coaching Advanced Certification', 'cma-certified-team-coach', 'Certified Team Coach')]
        for i, (t, sub, desc, pic) in enumerate(tracks):
            a, aa, b, ba = PAIRS[i % len(PAIRS)]
            rows += f'''
<div class="feature-row">
  <figure class="feature-row__media badge-pair" data-reveal="scale"><img src="/assets/img/badges/{a}.png" alt="{aa}" loading="lazy"><img src="/assets/img/badges/{b}.png" alt="{ba}" loading="lazy"></figure>
  <div data-reveal><span class="pill" style="margin-bottom:14px">{re.sub(r"<[^>]+>", "", sub).strip()}</span><h3>{re.sub(r"</?strong>", "", t)}</h3><div class="prose">{desc}</div></div>
</div>'''
        c = re.sub(r'(<img[^>]*entry-level-icon1\.png"[^>]*>\s*<h3>.*?</h3>\s*<p>.*?</p>\s*<p>.*?</p>\s*(?:<img[^>]*>)?\s*)+', '@@TRACKS@@', c, count=1, flags=re.S)
    # 4. split remaining prose around the placeholders
    parts = re.split(r'(@@JOURNEY@@|@@TRACKS@@)', c)
    out = ''
    for part in parts:
        if part == '@@JOURNEY@@': out += f'</div></div></section><section class="section section--surface"><div class="container">{journey}</div></section><section class="section"><div class="container"><div class="prose prose--wide" data-auto-reveal>'
        elif part == '@@TRACKS@@': out += f'</div>{rows}<div class="prose prose--wide" data-auto-reveal>'
        else: out += part
    # the interest form at the end becomes a step-by-step form (same fields, same wording)
    k = out.rfind('<form')
    if k >= 0:
        end_tag = out.index('>', k)
        attrs = out[k+5:end_tag]
        out = out[:k] + '<form' + attrs + ' class="js-steps" data-steps="2,2,5,3">' + out[end_tag+1:]
    body = subnav(page) + page_hero(page) + awards_band() + f'''
<section class="section section--tight">
  <div class="container"><div class="prose prose--wide" data-auto-reveal style="max-width:820px">{out}</div></div>
</section>
{stats}
{cta_band()}'''
    # stats belong right after the intro: move them before the first split section
    body = body.replace(stats, '', 1)
    body = body.replace('</div></div></section><section class="section section--surface">', f'</div></div></section>{stats}<section class="section section--surface">', 1)
    return layout(page, body)

RENDERERS.update({
    '/icf-coaching-training-program': certification,
    '/events/calendar': calendar_page,
    '/webinar': webinar_page,
    '/registration': registration_page,
    '/events/news': news_listing,
    '/events/gallery': gallery_listing,
    '/workshops': workshops_listing,
    '/blog/': blog_listing,
    '/blog/coaching': blog_listing,
    '/coaching-articles': blog_listing,
})
PREFIX_RENDERERS.extend([
    ('/events/news?', news_listing),
    ('/events/gallery?', gallery_listing),
    ('/blog/category/', blog_listing),
    ('/blog/20', blog_listing),
    ('/blog/', blog_post),
    ('/events/calendar/', lambda p: wide_page(p)),
    ('/event/', lambda p: wide_page(p)),
])


# ====================================================================== smart layout for flat CMS pages
"""The CMS hands us a flat list: headings, paragraphs, runs of images, numbers with
labels. These helpers read that list back into sections (logo rows, stat cards,
icon cards, chips) and only fall back to plain prose for ordinary text."""

def _txt(n): return re.sub(r'\s+', ' ', n.get_text(' ', strip=True)) if hasattr(n, 'get_text') else str(n).strip()
def _is_num(n): return getattr(n, 'name', None) == 'h2' and re.fullmatch(r'[\d,.+]+', _txt(n) or 'x') is not None
def _short(n, words=7): return len(_txt(n).split()) <= words
def _img(n): return getattr(n, 'name', None) == 'img'
def _imgsrc(n): return (n.get('src') or '') if _img(n) else ''

def parse_blocks(content):
    nodes = [n for n in top_nodes(content) if getattr(n, 'name', None) or str(n).strip()]
    blocks = []; i = 0; N = len(nodes)
    name = lambda k: getattr(nodes[k], 'name', None) if k < N else None
    while i < N:
        n = nodes[i]
        # --- stats: optional h3 title + (numeric h2, h3 label)+
        j = i
        title = None
        if name(j) == 'h3' and j + 1 < N and _is_num(nodes[j + 1]): title = nodes[j]; j += 1
        stats = []
        while j + 1 < N and _is_num(nodes[j]) and name(j + 1) == 'h3': stats.append((_txt(nodes[j]), _txt(nodes[j + 1]))); j += 2
        if stats:
            blocks.append({'t': 'stats', 'title': _txt(title) if title is not None else '', 'items': stats}); i = j; continue
        # --- logo / badge run: 3+ images in a row
        j = i
        while j < N and _img(nodes[j]): j += 1
        if j - i >= 3:
            blocks.append({'t': 'logos', 'items': [(_imgsrc(x), x.get('alt', '')) for x in nodes[i:j]]}); i = j; continue
        # --- icon cards: (img, h2|h3, p)+  or feature cards: (h2|h3, p, img)+
        def triplet(k, order):
            if k + 2 >= N: return None
            a, b, c = nodes[k], nodes[k + 1], nodes[k + 2]
            if order == 'ihp' and _img(a) and name(k + 1) in ('h2', 'h3') and name(k + 2) == 'p': return {'img': _imgsrc(a), 'title': _txt(b), 'body': b.decode_contents() if False else c.decode_contents()}
            if order == 'hpi' and name(k) in ('h2', 'h3') and name(k + 1) == 'p' and _img(c): return {'img': _imgsrc(c), 'title': _txt(a), 'body': b.decode_contents()}
            return None
        for order in ('ihp', 'hpi'):
            j = i; items = []
            while True:
                t = triplet(j, order)
                if not t: break
                items.append(t); j += 3
            if len(items) >= 2:
                if order == 'hpi' and j + 1 < N and name(j) in ('h2', 'h3') and name(j + 1) == 'p':
                    items.append({'img': '', 'title': _txt(nodes[j]), 'body': nodes[j + 1].decode_contents()}); j += 2
                blocks.append({'t': 'cards', 'items': items}); i = j; break
        else:
            # --- chips: (img, short p)+ x3
            j = i; items = []
            while j + 1 < N and _img(nodes[j]) and name(j + 1) == 'p' and _short(nodes[j + 1], 5): items.append((_imgsrc(nodes[j]), _txt(nodes[j + 1]))); j += 2
            if len(items) >= 3:
                blocks.append({'t': 'chips', 'items': items}); i = j; continue
            # --- section head: short h3 then h2
            if name(i) == 'h3' and _short(n, 6) and name(i + 1) == 'h2':
                blocks.append({'t': 'head', 'eyebrow': _txt(n), 'h2': nodes[i + 1].decode_contents()}); i += 2; continue
            # --- a lone image between text: media
            if _img(n):
                blocks.append({'t': 'media', 'src': _imgsrc(n), 'alt': n.get('alt', '')}); i += 1; continue
            # --- prose: everything else, merged
            if blocks and blocks[-1]['t'] == 'prose': blocks[-1]['html'] += '\n' + str(n)
            else: blocks.append({'t': 'prose', 'html': str(n)})
            i += 1
            continue
        continue
    return blocks

def merge_stat_rows(blocks):
    out = []
    for b in blocks:
        if b['t'] == 'stats' and out and out[-1]['t'] == 'statrow': out[-1]['groups'].append(b)
        elif b['t'] == 'stats': out.append({'t': 'statrow', 'groups': [b]})
        else: out.append(b)
    return out

def render_blocks(blocks):
    blocks = merge_stat_rows(blocks)
    out = []
    for b in blocks:
        t = b['t']
        if t == 'prose':
            out.append(f'<div class="prose prose--wide" data-auto-reveal>{b["html"]}</div>')
        elif t == 'head':
            out.append(f'<div class="section-head" style="margin-top:24px"><p class="eyebrow" data-reveal>{esc(b["eyebrow"])}</p><h2 data-reveal>{b["h2"]}</h2></div>')
        elif t == 'statrow':
            groups = ''
            for g in b['groups']:
                cards = ''.join(f'<div class="stat" data-reveal><div class="stat__num" data-count="{re.sub(r"[^0-9.]", "", v) or 0}">0</div><div class="stat__label">{esc(l)}</div></div>' for v, l in g['items'])
                title = f'<h3 data-reveal>{esc(g["title"])}</h3>' if g['title'] else ''
                groups += f'<div class="stats-group">{title}<div class="stats" style="grid-template-columns:repeat({min(4, len(g["items"]))},1fr)">{cards}</div></div>'
            out.append(f'<div class="stats-row" style="grid-template-columns:repeat({min(3, len(b["groups"]))},1fr)">{groups}</div>')
        elif t == 'stats':
            cards = ''.join(f'<div class="stat" data-reveal><div class="stat__num" data-count="{re.sub(r"[^0-9.]", "", v) or 0}">0</div><div class="stat__label">{esc(l)}</div></div>' for v, l in b['items'])
            title = f'<h3 data-reveal>{esc(b["title"])}</h3>' if b['title'] else ''
            out.append(f'<div class="stats-group">{title}<div class="stats" style="grid-template-columns:repeat({min(4, len(b["items"]))},1fr)">{cards}</div></div>')
        elif t == 'logos':
            SWAP = {'level-1.png': 'icf-level-1', 'level-2.png': 'icf-level-2', 'level-3.png': 'icf-level-3', 'cce.png': 'icf-cce'}
            def swap(src):
                name = src.rsplit('/', 1)[-1]
                return f'/assets/img/badges/{SWAP[name]}.png' if name in SWAP else src
            items = [(swap(src), alt) for src, alt in b['items']]
            if len(items) >= 8:
                # two endless lanes drifting opposite ways; the JS doubles each track for a seamless loop
                half = (len(items) + 1) // 2
                lane = lambda its: ''.join(f'<div class="logo-tile logo-tile--client"><img src="{esc(s)}" alt="{esc(a)}" loading="lazy"></div>' for s, a in its)
                out.append(f'<div class="logo-lanes" data-reveal="none">'
                           f'<div class="marquee"><div class="marquee__track" style="animation-duration:48s">{lane(items[:half])}</div></div>'
                           f'<div class="marquee marquee--reverse"><div class="marquee__track" style="animation-duration:56s">{lane(items[half:])}</div></div>'
                           f'</div>')
            else:
                tiles = ''.join(f'<div class="logo-cell"><img src="{esc(s)}" alt="{esc(a)}" loading="lazy"></div>' for s, a in items)
                out.append(f'<div class="logo-row" data-strip>{tiles}</div>')
        elif t == 'cards':
            cards = ''
            for c in b['items']:
                icon = f'<div class="icon-card__img"><img src="{esc(c["img"])}" alt="" loading="lazy"></div>' if c['img'] else ''
                cards += f'<article class="card icon-card" data-reveal>{icon}<h3>{esc(c["title"])}</h3><p>{c["body"]}</p></article>'
            out.append(f'<div class="grid grid-3">{cards}</div>')
        elif t == 'chips':
            chips = ''.join(f'<span class="chip-tile"><img src="{esc(s)}" alt="">{esc(l)}</span>' for s, l in b['items'])
            out.append(f'<div class="chips" data-reveal>{chips}</div>')
        elif t == 'media':
            out.append(f'<div class="media media--wide" data-reveal="scale" style="max-width:820px"><img src="{esc(b["src"])}" alt="{esc(b["alt"])}" loading="lazy" data-parallax="24"></div>')
    return '\n'.join(f'<div class="lp-block lp-block--{b["t"]}">{h}</div>' for b, h in zip(blocks, out))

def smart_page(page):
    """Generic pages: plain text keeps the article + aside; anything with image
    runs, stat numbers or card patterns gets the landing layout."""
    from build import strip_duplicate_heading
    content = strip_duplicate_heading(page['content'], page.get('h1'))
    content = re.sub(r'^\s*<h1>.*?</h1>', '', content, count=1, flags=re.S)
    blocks = parse_blocks(content)
    if all(b['t'] in ('prose', 'media', 'head') for b in blocks) and sum(1 for b in blocks if b['t'] == 'media') <= 1:
        return generic_page(page)
    body = subnav(page) + page_hero(page) + f'''
<section class="section section--tight landing">
  <div class="container">{render_blocks(blocks)}</div>
</section>
{cta_band()}'''
    return layout(page, body)


# ====================================================================== OUR FOUNDER
def parse_testimonials(nodes):
    """(photo img, quote-icon img, p quote, h3 name, p role) groups -> list of dicts."""
    out = []; i = 0
    while i < len(nodes):
        n = nodes[i]
        if _img(n) and i + 4 < len(nodes) and _img(nodes[i + 1]) and getattr(nodes[i + 2], 'name', None) == 'p' \
           and getattr(nodes[i + 3], 'name', None) == 'h3' and getattr(nodes[i + 4], 'name', None) == 'p':
            out.append({'img': _imgsrc(n), 'text': nodes[i + 2].decode_contents().strip(), 'name': _txt(nodes[i + 3]), 'role': _txt(nodes[i + 4])}); i += 5
        else: i += 1
    return out

def founder(page):
    nodes = [n for n in top_nodes(page['content']) if getattr(n, 'name', None) or str(n).strip()]
    # split at the testimonials heading
    cut = next((k for k, n in enumerate(nodes) if getattr(n, 'name', None) == 'h3' and 'client says' in _txt(n).lower()), len(nodes))
    body_nodes = [n for n in nodes[:cut] if not _img(n)]                       # drop the 2016 banner graphic
    quotes = parse_testimonials(nodes[cut:])
    t_eyebrow = _txt(nodes[cut]) if cut < len(nodes) else ''
    t_h2 = next((n.decode_contents() for n in nodes[cut:cut + 3] if getattr(n, 'name', None) == 'h2'), '')
    # first eyebrow + h2 + two paragraphs sit beside the portrait; the rest flows as prose
    eyebrow = ''; h2 = ''; intro = []; rest = []
    for n in body_nodes:
        nm = getattr(n, 'name', None)
        if nm == 'h3' and not eyebrow and not h2: eyebrow = _txt(n)
        elif nm == 'h2' and not h2: h2 = n.decode_contents()
        elif nm == 'p' and h2 and not rest and len(intro) < 2: intro.append(str(n))
        else: rest.append(str(n))
    PORTRAIT = SITE + '/siteimages/ourfaculty/1/19660094231651223065_1_Ben Professional 2.png'
    body = subnav(page) + f'''
<section class="page-hero" style="padding-bottom:0">
  <div class="container">{crumbs(page)}<h1 data-split>{esc(page['h1'])}</h1></div>
</section>
<section class="section section--tight">
  <div class="container split split--wide">
    <div class="media-stack" data-reveal="scale">
      <div class="media media--tall media--blob"><img src="{esc(PORTRAIT)}" alt="Ben Koh, Master Certified Coach" data-parallax="24"></div>
      <div class="badge-float" style="left:auto;right:-6%;top:auto;bottom:10%"><img src="/assets/img/badges/icf-mcc.png" alt="" width="54" height="54"><div><b>MCC</b><span>Master Certified Coach</span></div></div>
    </div>
    <div>
      {f'<p class="eyebrow" data-reveal>{esc(eyebrow)}</p>' if eyebrow else ''}
      <h2 data-reveal>{h2}</h2>
      <div class="prose" data-auto-reveal>{''.join(intro)}</div>
    </div>
  </div>
</section>
<section class="section section--tight">
  <div class="container"><div class="prose prose--wide" data-auto-reveal style="max-width:860px">{''.join(rest)}</div></div>
</section>
<section class="section section--surface">
  <div class="container">
    <div class="section-head">
      {f'<p class="eyebrow" data-reveal>{esc(t_eyebrow)}</p>' if t_eyebrow else ''}
      {f'<h2 data-reveal>{t_h2}</h2>' if t_h2 else ''}
    </div>
  </div>
  <div class="marquee" data-reveal="none">
    <div class="marquee__track" style="animation-duration:70s">{''.join(quote(q['text'], q['name'], q['role'], q['img']) for q in quotes)}</div>
  </div>
</section>
{cta_band()}'''
    return layout(page, body)

RENDERERS['/icf-master-certified-coach-mcc'] = founder
