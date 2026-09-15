"""Hand-designed pages. All copy is verbatim from the live site (src/content/pages.json).
Text is written here only for layout; a verification script (src/verify.py) checks
that every sentence from the crawled page still appears in the generated one.
"""
import re, html
from bs4 import BeautifulSoup
from build import (PAGES, layout, page_hero, subnav, crumbs, btn, link, aside, esc, ARROW, PIN, generic_page, SITE, PHONE, EMAIL, page_heading, awards_band, take_lead)

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
        <img src="/assets/img/pathway-1.jpg" alt="" loading="lazy">
        <div class="service__body"><h3>ICF COACHING CERTIFICATION PROGRAMS FOR ASPIRING COACHES</h3><p>Achieve personal mastery and a globally recognized professional coach certification.</p><span class="link">Read More{ARROW}</span></div>
      </a>
      <a class="service" href="/coaching-skill-training-course-and-workshop" data-reveal>
        <img src="/assets/img/pathway-2.jpg" alt="" loading="lazy">
        <div class="service__body"><h3>INTERACTIVE WORKSHOPS AND PRACTICAL LABS FOR COACHES</h3><p>Equip leaders to integrate coaching skills as part of their managerial role to improve work engagement.</p><span class="link">Read More{ARROW}</span></div>
      </a>
      <a class="service" href="/executive-leadership-coaching-service-for-managers-and-leaders" data-reveal>
        <img src="/assets/img/pathway-3.jpg" alt="" loading="lazy">
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
    <div class="elastic" data-elastic data-reveal="none">
      <div class="elastic__panel is-active">
        <img src="{IMG}image_item/learning-1.jpg_1749727015" alt="" loading="lazy">
        <div class="elastic__num">01</div>
        <div class="elastic__meta">
          <h3>Flexible Online Learning &amp; Global Coaching Network</h3>
          <ul>
            <li>Connect with coaches and leaders worldwide to <strong>develop your global coaching network</strong> for collaboration.</li>
            <li>Experience rich, diverse, and cross-cultural learning that <strong>prepares and positions you as a global citizen</strong></li>
            <li>An opportunity to <strong>accumulate coaching experience</strong> and pay back through our SAY Foundation, a non-profit charitable organization offering pro-bono coaching</li>
          </ul>
        </div>
      </div>
      <div class="elastic__panel">
        <img src="{IMG}image_item/learning-2.jpg_1749727051" alt="" loading="lazy">
        <div class="elastic__num">02</div>
        <div class="elastic__meta">
          <h3>Comprehensive Instructional Design</h3>
          <p><b>Accelerated learning </b>with carefully designed Learning Lab, Practical Lab, Practicum, Peer Peer Support and Coaching Supervision to develop your coaching competency.</p>
        </div>
      </div>
      <div class="elastic__panel">
        <img src="{IMG}image_item/learning-3.jpg_1749727088" alt="" loading="lazy">
        <div class="elastic__num">03</div>
        <div class="elastic__meta">
          <h3>Lifelong Support &amp; Continuous Learning For Coaches</h3>
          <p><b>Extensive post-training support</b> through our monthly learning webinars and live coaching demonstrations. Opportunities to serve as Student Mentors contribute to faculty-guided learning environments, while selected programs offer access to Continual Coach Education units through professional partnership frameworks.</p>
        </div>
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



<section class="section">
  <div class="container split split--wide">
    <div>
      <h2 data-reveal>Download Full Program Brochure &amp; Curriculum Guide</h2>
      <p class="lead" data-reveal>Receive the brochure, schedule of training by completing the form below</p>
    </div>
    <div class="prose prose--wide form-stage" data-reveal>
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

<section class="section section--tight section--white">
  <div class="container center">
    <p class="eyebrow" data-reveal>STRATEGIC ALLIANCES WITH GLOBAL COACHING INSTITUTIONS</p>
    <h2 data-reveal>Trusted Partnerships with Leading Coaching Experts &amp; Organizations</h2>
    <p class="lead" data-reveal>Coach Masters Academy collaborates with ICF-aligned bodies and respected coaching organizations to uphold training quality, support global recognition, and extend professional networks.</p>
  </div>
  <div class="logo-section logo-section--flush" data-reveal="none">
    <div class="marquee"><div class="marquee__track" style="animation-duration:36s">
      <div class="logo-tile logo-tile--client"><img src="{IMG}image_item/partner-1.png_1749732353" alt=""></div>
      <div class="logo-tile logo-tile--client"><img src="{IMG}image_item/partner-2.png_1749732381" alt=""></div>
      <div class="logo-tile logo-tile--client"><img src="{IMG}image_item/partner-3.png_1749732426" alt=""></div>
      <div class="logo-tile logo-tile--client"><img src="{IMG}image_item/partner-4.png_1749732477" alt=""></div>
    </div></div>
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
        <h1 data-split>Inspiring Positive Change <em class="hl">Through mastery of coaching.</em></h1>
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

<section class="section section--surface">
  <div class="container">
    <div class="tabs tabs--center" role="tablist" data-tabs data-reveal="none">
      <button type="button" class="is-active" role="tab" aria-selected="true">Our Vision</button>
      <button type="button" role="tab" aria-selected="false">Our Mission</button>
      <button type="button" role="tab" aria-selected="false">Our Approach</button>
    </div>
    <div class="tab-panels">
      <div class="tab-panel is-active" role="tabpanel">
        <div class="tab-panel__grid">
          <div><p class="eyebrow">Our Vision</p><h2>We see every conversation holds the power to make a real difference.</h2></div>
          <div class="prose">
            <p>Some conversations change what we know. Others change how we see ourselves, our circumstances and what may be possible.</p>
            <p>We believe those moments matter, because they can influence the choices we make and the way we move forward.</p>
          </div>
        </div>
      </div>
      <div class="tab-panel" role="tabpanel" hidden>
        <div class="tab-panel__grid">
          <div><p class="eyebrow">Mission</p><h2>Our  Mission</h2><p class="lead">Empower You To Be an Effective Change Agent By delivering high-quality coaching education and coaching service</p></div>
          <ul class="list-check">
            <li>Our coaching program empowers you with the skills and knowledge to drive impactful change.</li>
            <li>Grounded in scientific research and best practices, our approach facilitates profound learning.</li>
            <li>It enables significant transformations that resonate well beyond individual sessions, ensuring lasting results in your personal and professional life.</li>
          </ul>
        </div>
      </div>
      <div class="tab-panel" role="tabpanel" hidden>
        <div class="tab-panel__grid">
          <div><p class="eyebrow">Our Approach</p><h2>Changing how change happens.</h2></div>
          <div class="prose">
            <p>For more than a decade, our founder, Dr Ben Koh, has pursued research and fieldwork into how people think, learn and change. That body of work led to CMA’s proprietary transformational approach to coaching — grounded in science, refined through practice, and now taught and applied across the globe.</p>
            <p>It goes beyond solving the immediate problem by working with how people make sense of what they are facing — helping them think differently, choose with greater ownership and strengthen their capacity to adapt as circumstances change.</p>
            <p>This is the foundation of our Transformative Edge™ — shaping how we educate coach practitioners, build coaching capability in organisations and work directly with people through coaching.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cma-photo">
  <img class="cma-photo__img" src="/assets/img/about-conversation.jpg" alt="" data-parallax="30">
  <div class="container cma-photo__grid">
    <div class="cma-photo__intro">
      <p class="eyebrow" data-reveal>CMA</p>
      <h2 class="cma-words" data-reveal><span class="cma-words__w">Conversation.</span> <span class="cma-words__w cma-words__w--alt">Meaning.</span> <span class="cma-words__w">Agency.</span></h2>
      <p class="cma-photo__lead" data-reveal>We are a global coaching organisation with more than a decade of work across professional coaching certification, organisational coaching capability and coaching services.</p>
      <p data-reveal>At the heart of our work, one question has continued to guide us:</p>
    </div>
    <p class="cma-photo__question" data-reveal><em class="hl">How can coaching</em> help people create change they can truly own?</p>
    <div class="cma-photo__note" data-reveal><p>That question has shaped how we educate, how we work with organisations and how we coach.</p>
        <p>It has also kept us looking beyond technique and immediate solutions towards a deeper understanding of how change happens.</p></div>
  </div>
</section>

<section class="section section--green stand">
  <div class="container">
    <div class="section-head center" style="margin-inline:auto">
      <h2 data-reveal>What We <em class="hl">Stand For</em></h2>
    </div>
    <div class="grid grid-4 stand__grid" data-seq>
      <div class="stand__card" data-reveal><span class="stand__num">01</span><h3>Conversation</h3><p>Conversation opens the possibility of seeing differently.</p></div>
      <div class="stand__card" data-reveal><span class="stand__num">02</span><h3>Meaning</h3><p>Meaning shapes how we make sense of what is happening.</p></div>
      <div class="stand__card" data-reveal><span class="stand__num">03</span><h3>Agency</h3><p>Agency is the capacity to respond with choice and ownership.</p></div>
      <div class="stand__card" data-reveal><span class="stand__num">04</span><h3>Change</h3><p>Change may be inevitable. How we meet it is ours to shape.</p></div>
    </div>
    <p class="stand__line" data-reveal>CMA. <em class="hl">Inspiring Positive Change.</em></p>
  </div>
</section>

<section class="section section--white">
  <div class="container">
    <div class="section-head center" style="margin-inline:auto">
      <h2 data-reveal>What <em class="hl">We Do</em></h2>
    </div>
    <div class="grid grid-3">
      <a class="do-card" href="/icf-coaching-training-program" data-reveal>
        <div class="do-card__media"><img src="/assets/img/pathway-1.jpg" alt="" loading="lazy"></div>
        <div class="do-card__body">
          <h3>Professional Coaching Certification</h3>
          <p>We train people to become skilful practitioner through a complete ICF-accredited education pathway, from foundational certification through advanced mastery and team coaching.</p>
          <p>Our coaching education combines internationally recognised professional standards with CMA’s proprietary methodology, and has earned industry recognition and university endorsement.</p>
          <span class="link">Explore Coaching Certification{ARROW}</span>
        </div>
      </a>
      <a class="do-card" href="/coaching-skill-training-course-and-workshop" data-reveal>
        <div class="do-card__media"><img src="/assets/img/pathway-2.jpg" alt="" loading="lazy"></div>
        <div class="do-card__body">
          <h3>Organisational Coaching Capability</h3>
          <p>We help organisations build coaching capability in their leaders and managers, so they can develop people through the realities of everyday work — not only through formal development programmes.</p>
          <p>Our workplace solutions help leaders create stronger conversations around performance, learning, ownership and growth.</p>
          <span class="link">Build Coaching Capability{ARROW}</span>
        </div>
      </a>
      <a class="do-card" href="/executive-leadership-coaching-service-for-managers-and-leaders" data-reveal>
        <div class="do-card__media"><img src="/assets/img/pathway-3.jpg" alt="" loading="lazy"></div>
        <div class="do-card__body">
          <h3>Coaching Services</h3>
          <p>We work directly with individuals and leaders navigating important decisions, transitions and complexity.</p>
          <p>Our coaching creates the space to think clearly, understand what matters and move forward with choices they can stand behind.</p>
          <span class="link">Engage Coaching Services{ARROW}</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="container">
    <div class="section-head center" style="margin-inline:auto">
      <h2 data-reveal>A Vision to Inspire Positive Change through  Mastery of Coaching</h2>
    </div>
    <a class="video-cta" href="https://www.youtube.com/watch?v=NAVllbMOilw" target="_blank" rel="noopener" data-video data-reveal="scale">
      <img src="{IMG}featured_image1/2/our-potential-img.jpg" alt="" data-parallax="40">
      <div style="position:relative;z-index:1;display:grid;justify-items:center"><div class="play"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></div><span>watch video</span></div>
    </a>
  </div>
</section>

<section class="cta-full">
  <div class="container cta-full__inner cta-full__inner--stack">
    <div>
      <h2 data-reveal>Where do you want to make a difference?</h2>
      <p data-reveal>Whether you want to develop professionally as a coach, strengthen coaching capability in your organisation, or work through an important challenge with a coach, there is a place to begin.</p>
    </div>
    <div class="cta-full__actions cta-full__actions--three" data-reveal>
      {btn('Explore Coaching Certification', '/icf-coaching-training-program', 'btn--white')}
      {btn('Build Coaching Capability', '/coaching-skill-training-course-and-workshop', 'btn--ghost btn--ghost-light')}
      {btn('Engage Coaching Services', '/executive-leadership-coaching-service-for-managers-and-leaders', 'btn--ghost btn--ghost-light')}
    </div>
  </div>
</section>'''
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
    """The shared registration band was removed at the client's request (Sep 2026); kept as a stub so callers stay unchanged."""
    return ''
    return f'''
<section class="cta-full">
  <div class="container cta-full__inner">
    <div>
      <p class="eyebrow" data-reveal style="color:#F3A77F">Registration</p>
      <h2 data-reveal>Your journey towards mastering coaching begins with us.</h2>
      <p data-reveal>You can call our Global Office at +65-8299-8170 to explore which entry point and advanced structure best fit your experience, goals, and context.</p>
    </div>
    <div class="cta-full__actions" data-reveal>{btn('Registration', '/registration', 'btn--white')}{btn('Schedule a Call', 'https://calendly.com/coachmastersacademyglobaloffice/30min-phone-call-appointment', 'btn--ghost btn--ghost-light')}</div>
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

def faculty_section(page, compact=False, top=False):
    groups = parse_faculty(page)
    first = split_person(groups[0]['people'][0]) if groups and groups[0]['people'] else {'name': '', 'cred': '', 'role': '', 'loc': '', 'img': ''}
    tabs = ''.join(f'<button type="button"{" class=is-active" if i == 0 else ""}>{esc(g["title"])}</button>' for i, g in enumerate(groups))
    tracks = ''.join('<div class="faculty__track"' + (' hidden' if i else '') + '>' + ''.join(person_card(p) for p in g['people']) + '</div>' for i, g in enumerate(groups))
    n0 = len(groups[0]['people']) if groups else 0
    title = '<h1 data-split>Meet the minds behind <em class="hl">meaningful change.</em></h1>' if top else '<h2 data-reveal>Meet the minds behind meaningful change.</h2>'
    head_html = '' if compact else ('<div><p class="eyebrow" data-reveal>Our Global Faculty</p>' + title +
        '<p class="lead" data-reveal>World-class coaches, trainers and thought leaders united by a shared purpose: to elevate coaching, empower people and shape a better future together.</p></div>')
    return f'''
<section class="section faculty">
  <div class="container">
    <div class="faculty__head{' faculty__head--bare' if compact else ''}">
      {head_html}
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
{faculty_section(page, top=True)}
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
def gallery_listing(page): return listing_page(dict(page, banner=''), 'Gallery', kind='gallery')
def workshops_listing(page): return listing_page(page, 'Workshops')

def wide_page(page, heading=None):
    """Long-form pages that need the full width (tables, calendars, forms)."""
    content = re.sub(r'^\s*<h1>.*?</h1>', '', page['content'], count=1, flags=re.S)
    lead, content = take_lead(page, content)
    body = subnav(page) + page_hero(page, heading, lead=lead) + f'''
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
def acc_cards(cards, open_first=True):
    """Compact open/close cards. cards: list of dicts {num, title, sub, body, badges:[(file, alt)]}."""
    out = []
    for i, c in enumerate(cards):
        is_open = ' is-open' if (open_first and i == 0) else ''
        badges = ''.join(f'<img src="/assets/img/badges/{f}.png" alt="{esc(a)}" loading="lazy">' for f, a in c.get('badges', []) if f)
        sub = f'<p class="acc-card__sub">{c["sub"]}</p>' if c.get('sub') else ''
        bd = f'<div class="acc-card__badges">{badges}</div>' if badges else ''
        out.append(
            f'<article class="acc-card{is_open}" data-reveal>'
            f'<button class="acc-card__head" type="button" aria-expanded="{"true" if is_open else "false"}">'
            f'<span class="acc-card__num">{c["num"]}</span><span class="acc-card__title">{c["title"]}</span><span class="acc-card__chev" aria-hidden="true"></span></button>'
            f'<div class="acc-card__body"><div class="acc-card__inner">{sub}<div class="prose">{c["body"]}</div>{bd}</div></div>'
            f'</article>')
    return f'<div class="acc-cards" data-accordion>{"".join(out)}</div>'

def split_section(left_html, right_html, surface=False):
    cls = ' section--surface' if surface else ''
    return (f'<section class="section{cls}"><div class="container split-sticky">'
            f'<div class="split-sticky__left"><div class="prose prose--wide" data-auto-reveal>{left_html}</div></div>'
            f'<div class="split-sticky__right">{right_html}</div></div></section>')

def certification(page):
    import os
    c = page['content']
    # 1. stats block
    m = re.search(r'<h2>(Proven Success[^<]*)</h2>\s*<p>(\d+)</p>\s*<p>([^<]+)</p>\s*<p>(\d+)</p>\s*<p>([^<]+)</p>', c)
    stats = ''
    if m:
        stats = (f'<section class="section proof"><div class="container">'
                 f'<h2 class="proof__title" data-reveal>{m.group(1)}</h2>'
                 f'<div class="proof__row">'
                 f'<div class="proof__item" data-reveal><div class="proof__num" data-count="{m.group(2)}">0</div><i class="proof__tick" data-draw="x"></i><div class="proof__label">{m.group(3)}</div></div>'
                 f'<i class="proof__divider" data-draw="y"></i>'
                 f'<div class="proof__item" data-reveal><div class="proof__num" data-count="{m.group(4)}">0</div><i class="proof__tick" data-draw="x"></i><div class="proof__label">{m.group(5)}</div></div>'
                 f'</div></div></section>')
        c = c.replace(m.group(0), '')
    # 2. the accreditation strip (a flattened jpeg on the live site) -> the transparent badges
    BADGES = [('icf-level-1', 'ICF Level 1 accredited coaching education'), ('icf-level-2', 'ICF Level 2 accredited coaching education'),
              ('icf-level-3', 'ICF Level 3 accredited coaching education'), ('icf-aatc', 'ICF Advanced Accreditation in Team Coaching'),
              ('icf-cce', 'ICF Continuing Coach Education'), ('coaching-impact-award', 'ICF Coaching Impact Award')]
    grid = '<div class="badge-strip" data-strip>' + ''.join(f'<img src="/assets/img/badges/{f}.png" alt="{a}" loading="lazy">' for f, a in BADGES) + '</div>'
    c = re.sub(r'<img[^>]*src="data:image/jpeg[^"]*"[^>]*>', grid, c, count=1)

    # 3. slice the page: intro | credential paths + 4 Advantages | pathway + 4 tracks | tail (call + form)
    i_paths = c.find('<h3> Your Pathway to ICF Certification')
    if i_paths < 0: i_paths = c.find('<h2>ICF Credential Paths')
    i_details = c.find('<details>')
    i_tracks_head = c.find('<h2>Explore Your Coaching Pathway')
    i_track_items = c.find('<img', i_tracks_head)
    # icon, title, subtitle, one or more paragraphs, then the live site's flattened picture (dropped)
    track_re = re.compile(r'<img[^>]*entry-level-icon1\.png"[^>]*>\s*<h3>(.*?)</h3>\s*<p>(.*?)</p>\s*((?:<p>.*?</p>\s*)+?)(?:<img[^>]*src="([^"]+)"[^>]*>)?(?=\s*(?:<img[^>]*entry-level-icon1|<p>You can call|<h2>|<form|$))', re.S)
    tracks = list(track_re.finditer(c, i_track_items))
    i_tail = tracks[-1].end() if tracks else len(c)

    intro = c[:i_paths]
    lead, intro = take_lead(page, intro)
    paths_left = c[i_paths:i_details]
    details = re.findall(r'<details>\s*<summary>(.*?)</summary>(.*?)</details>', c[i_details:i_tracks_head], re.S)
    tracks_left = c[i_tracks_head:i_track_items]
    tail = c[i_tail:]

    adv_cards = [{'num': f'{i+1:02d}', 'title': t.strip(), 'body': b.strip()} for i, (t, b) in enumerate(details)]
    # each track: its ICF level badge, the ICF credential and the CMA seal, as on the live site's own pictures
    TRACK_BADGES = [
        [('icf-level-1', 'ICF Level 1'), ('icf-acc', 'ICF Associate Certified Coach'), ('cma-certified-professional-coach', 'CMA Certified Professional Coach')],
        [('icf-level-2', 'ICF Level 2'), ('icf-pcc', 'ICF Professional Certified Coach'), ('cma-advanced-practitioner-cpc', 'CMA Advanced Practitioner Certified Professional Coach')],
        [('icf-level-3', 'ICF Level 3'), ('icf-mcc', 'ICF Master Certified Coach'), ('cma-certified-master-coach', 'CMA Certified Master Coach')],
        [('icf-aatc', 'ICF Advanced Accreditation in Team Coaching'), ('icf-team-coaching', 'ICF Team Coaching Advanced Certification'), ('cma-certified-team-coach', 'CMA Certified Team Coach')],
    ]
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    def have(f): return os.path.exists(os.path.join(root, 'assets', 'img', 'badges', f + '.png'))
    track_cards = []
    for i, mt in enumerate(tracks):
        t, sub, desc, _pic = mt.groups()
        track_cards.append({'num': f'{i+1:02d}', 'title': re.sub(r'</?strong>', '', t).strip(), 'sub': re.sub(r'<[^>]+>', '', sub).strip(),
                            'body': desc, 'badges': [(f, a) for f, a in TRACK_BADGES[i % 4] if have(f)]})

    # the interest form at the end becomes a step-by-step form (same fields, same wording)
    k = tail.rfind('<form')
    if k >= 0:
        end_tag = tail.index('>', k)
        tail = tail[:k] + '<form' + tail[k+5:end_tag] + ' class="js-steps" data-steps="2,2,5,3">' + tail[end_tag+1:]

    call = ''
    mc = re.match(r'\s*<p>(You can call our Global Office.*?)</p>\s*<a href="([^"]+)"[^>]*>(Schedule a Call)</a>', tail, re.S)
    if mc:
        call = (f'<section class="section section--tight"><div class="container center">'
                f'<p class="lead" data-reveal style="margin:0 auto 22px">{mc.group(1)}</p>'
                f'{btn(mc.group(3), mc.group(2))}</div></section>')
        tail = tail[mc.end():]
    body = (subnav(page) + page_hero(page, lead=lead) + awards_band()
            + f'<section class="section section--tight"><div class="container"><div class="prose prose--wide" data-auto-reveal>{intro}</div></div></section>'
            + stats
            + split_section(paths_left, acc_cards(adv_cards), surface=True)
            + split_section(tracks_left, acc_cards(track_cards))
            + call
            + f'<section class="section section--tight"><div class="container"><div class="prose prose--wide" data-auto-reveal>{tail}</div></div></section>'
            + cta_band())
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

def attach_logo_intros(blocks):
    """The heading (+ up to two short paragraphs) right before a logo run moves inside the logo band,
    so heading, text and logos read as one centred section."""
    out = []
    for b in blocks:
        if b['t'] == 'logos' and out and out[-1]['t'] in ('prose', 'head'):
            prev = out[-1]
            if prev['t'] == 'head':
                out.pop(); b = dict(b, intro=f'<p class="eyebrow">{esc(prev["eyebrow"])}</p><h2>{prev["h2"]}</h2>')
            else:
                soup = BeautifulSoup(prev['html'], 'lxml'); root = soup.body or soup
                nodes = [n for n in root.children if getattr(n, 'name', None) or str(n).strip()]
                hi = max((k for k, n in enumerate(nodes) if getattr(n, 'name', None) in ('h2', 'h3')), default=-1)
                tail = nodes[hi:] if hi >= 0 else []
                if tail and len(tail) <= 4 and all(getattr(n, 'name', None) in ('h2', 'h3', 'p') for n in tail) \
                   and sum(len(_txt(n).split()) for n in tail[1:]) <= 80:
                    # a short line right above the heading (an eyebrow) comes along too
                    if hi >= 1 and getattr(nodes[hi - 1], 'name', None) in ('h3', 'p') and len(_txt(nodes[hi - 1]).split()) <= 8:
                        hi -= 1; tail = nodes[hi:]
                    intro = ''.join(str(n) for n in tail)
                    rest = ''.join(str(n) for n in nodes[:hi])
                    if rest.strip(): out[-1] = dict(prev, html=rest)
                    else: out.pop()
                    b = dict(b, intro=intro)
        out.append(b)
    return out

def render_blocks(blocks):
    blocks = attach_logo_intros(merge_stat_rows(blocks))
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
                cards = ''.join(f'<div class="ring-stat" data-reveal><div class="ring-stat__ring"><svg viewBox="0 0 120 120" aria-hidden="true"><circle class="ring-stat__disc" cx="60" cy="60" r="48"/><circle class="ring-stat__track" cx="60" cy="60" r="57"/><circle class="ring-stat__bar" cx="60" cy="60" r="57" pathLength="100"/></svg><div class="stat__num" data-count="{re.sub(r"[^0-9.]", "", v) or 0}">0</div></div><div class="stat__label">{esc(l)}</div></div>' for v, l in g['items'])
                title = f'<h3 data-reveal>{esc(g["title"])}</h3>' if g['title'] else ''
                groups += f'<div class="stats-group">{title}<div class="stats" style="grid-template-columns:repeat({min(4, len(g["items"]))},1fr)">{cards}</div></div>'
            out.append(f'<div class="stats-row" style="grid-template-columns:repeat({min(3, len(b["groups"]))},1fr)">{groups}</div>')
        elif t == 'stats':
            cards = ''.join(f'<div class="stat" data-reveal><div class="stat__num" data-count="{re.sub(r"[^0-9.]", "", v) or 0}">0</div><div class="stat__label">{esc(l)}</div></div>' for v, l in b['items'])
            title = f'<h3 data-reveal>{esc(b["title"])}</h3>' if b['title'] else ''
            out.append(f'<div class="stats-group">{title}<div class="stats" style="grid-template-columns:repeat({min(4, len(b["items"]))},1fr)">{cards}</div></div>')
        elif t == 'logos':
            intro = f'<div class="logo-section__intro" data-reveal>{b["intro"]}</div>' if b.get('intro') else ''
            SWAP = {'level-1.png': 'icf-level-1', 'level-2.png': 'icf-level-2', 'level-3.png': 'icf-level-3', 'cce.png': 'icf-cce'}
            def swap(src):
                name = src.rsplit('/', 1)[-1]
                return f'/assets/img/badges/{SWAP[name]}.png' if name in SWAP else src
            items = [(swap(src), alt) for src, alt in b['items']]
            if len(items) >= 8:
                # two endless lanes drifting opposite ways; the JS doubles each track for a seamless loop
                half = (len(items) + 1) // 2
                lane = lambda its: ''.join(f'<div class="logo-tile logo-tile--client"><img src="{esc(s)}" alt="{esc(a)}" loading="lazy"></div>' for s, a in its)
                out.append(f'<div class="logo-section">{intro}<div class="logo-lanes" data-reveal="none">'
                           f'<div class="marquee"><div class="marquee__track" style="animation-duration:48s">{lane(items[:half])}</div></div>'
                           f'<div class="marquee marquee--reverse"><div class="marquee__track" style="animation-duration:56s">{lane(items[half:])}</div></div>'
                           f'</div></div>')
            else:
                tiles = ''.join(f'<div class="logo-cell"><img src="{esc(s)}" alt="{esc(a)}" loading="lazy"></div>' for s, a in items)
                out.append(f'<div class="logo-section">{intro}<div class="logo-row" data-strip>{tiles}</div></div>')
        elif t == 'cards':
            cards = ''
            for c in b['items']:
                icon = f'<div class="icon-card__img"><img src="{esc(c["img"])}" alt="" loading="lazy"></div>' if c['img'] else ''
                cards += f'<article class="card icon-card" data-reveal>{icon}<h3>{esc(c["title"])}</h3><p>{c["body"]}</p></article>'
            out.append(f'<div class="grid grid-3">{cards}</div>')
        elif t == 'chips':
            out.append('')   # the expertise chips were removed from the design (client request, Sep 2026)
        elif t == 'media':
            out.append(f'<div class="media media--wide" data-reveal="scale" style="max-width:820px"><img src="{esc(b["src"])}" alt="{esc(b["alt"])}" loading="lazy" data-parallax="24"></div>')
    return '\n'.join(f'<div class="lp-block lp-block--{b["t"]}">{h}</div>' for b, h in zip(blocks, out))

def smart_page(page, extra=''):
    """Generic pages: plain text keeps the article + aside; anything with image
    runs, stat numbers or card patterns gets the landing layout. `extra` is a
    hand-built section slotted in before the registration band."""
    from build import strip_duplicate_heading
    content = strip_duplicate_heading(page['content'], page.get('h1'))
    content = re.sub(r'^\s*<h1>.*?</h1>', '', content, count=1, flags=re.S)
    blocks = parse_blocks(content)
    if not extra and all(b['t'] in ('prose', 'media', 'head') for b in blocks) and sum(1 for b in blocks if b['t'] == 'media') <= 1:
        return generic_page(page)
    lead, content = take_lead(page, content)
    blocks = parse_blocks(content)
    body = subnav(page) + page_hero(page, lead=lead) + f'''
<section class="section section--tight landing">
  <div class="container">{render_blocks(blocks)}</div>
</section>
{extra}
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
<section class="section section--tight flow-side">
  <svg class="flow-side__svg" viewBox="0 0 300 1000" preserveAspectRatio="none" aria-hidden="true">
    
    <path fill="#eb6422" d="M0 0 H110 C30 170, 240 330, 160 520 C90 690, 250 830, 140 1000 H0 Z"/>
    <path class="flow-side__line" d="M150 0 C70 170, 280 330, 200 520 C130 690, 290 830, 180 1000"/>
  </svg>
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


# ====================================================================== regional offices (Coaching Education)
def offices_section():
    """Region tabs, office cards and a map that follows the selected office.
    Data: src/content/offices.json, taken verbatim from the live page's tab block."""
    import json, os, urllib.parse
    data = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content', 'offices.json')))
    def query(office):
        addr = next((r['value'] for r in office['rows'] if r['label'] == 'Office'), '')
        return urllib.parse.quote(addr or office['country'] + ' Coach Masters Academy')
    tabs = ''.join(f'<button type="button" role="tab"{" class=is-active" if i == 0 else ""} data-region="{r["id"]}">{esc(r["label"])}</button>' for i, r in enumerate(data))
    panels = ''
    for i, r in enumerate(data):
        cards = ''
        for j, o in enumerate(r['offices']):
            rows = ''
            for row in o['rows']:
                ext = ' target="_blank" rel="noopener"' if (row['href'] or '').startswith('http') else ''
                val = f'<a href="{esc(row["href"])}"{ext}>{esc(row["value"])}</a>' if row['href'] else esc(row['value'])
                rows += f'<div class="office__row"><span>{esc(row["label"])}</span><span>{val}</span></div>'
            cards += (f'<button type="button" class="office{" is-active" if j == 0 else ""}" data-q="{query(o)}">'
                      f'<span class="office__name">{PIN}{esc(o["country"])}</span>{rows}</button>')
        panels += f'<div class="offices__panel"{"" if i == 0 else " hidden"} data-region="{r["id"]}">{cards}</div>'
    first = query(data[0]['offices'][0])
    return f'''
<section class="section offices" data-offices>
  <div class="container">
    <div class="tabs offices__tabs" role="tablist" data-reveal="none">{tabs}</div>
    <div class="offices__grid">
      <div class="offices__list">{panels}</div>
      <div class="offices__map" data-reveal="scale">
        <iframe title="Office location map" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen
          src="https://maps.google.com/maps?q={first}&z=13&output=embed"></iframe>
      </div>
    </div>
  </div>
</section>'''

def coaching_education(page):
    return smart_page(page, extra=offices_section())

RENDERERS['/pages/coaching-education'] = coaching_education


# ====================================================================== blog (WordPress) — listings, posts, widgets
def blog_widgets(content):
    """Pull WordPress's sidebar widgets (pagination list, search form, Categories list)
    out of the flat content. Returns (content_without_widgets, pagination_html, tools_html)."""
    soup = BeautifulSoup(content, 'lxml'); root = soup.body or soup
    pag = ''; search = ''; cats = ''
    # pagination: a <ul> whose links point at /blog/page/N
    for ul in root.find_all('ul'):
        links = ul.find_all('a', href=True)
        if links and all('/blog/page/' in a['href'] or a.get_text(strip=True) in ('…', '...') for a in links):
            items = []
            for li in ul.find_all('li'):
                a = li.find('a'); t = li.get_text(strip=True)
                if not t and not a: continue
                if not t: continue                                   # WP's empty "next" arrow
                if a and a.get('href'): items.append(f'<a href="{esc(a["href"])}">{esc(t)}</a>')
                elif t in ('…', '...'): items.append('<span>…</span>')
                else: items.append(f'<span class="is-active">{esc(t)}</span>')
            pag = '<nav class="pagination" aria-label="Pages">' + ''.join(items) + '</nav>'
            ul.decompose(); break
    for cf in root.find_all('form'):                                   # WordPress comment form is chrome, not copy
        if 'wp-comments-post' in (cf.get('action') or ''):
            prev = cf.find_previous_sibling(['h2', 'h3'])
            if prev is not None and 'Leave a Reply' in prev.get_text(): prev.decompose()
            cf.decompose()
    f = next((f for f in root.find_all('form') if f.find('input', attrs={'type': 'search'})), None)
    if f is not None:
        search = ('<form class="blog-search" action="/blog" method="get" role="search">'
                  '<input name="s" type="search" placeholder="Search…" aria-label="Search the blog">'
                  '<button type="submit" aria-label="Search"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg></button></form>')
        f.decompose()
    h = next((h for h in root.find_all(['h2', 'h3']) if h.get_text(strip=True) == 'Categories'), None)
    if h is not None:
        ul = h.find_next_sibling('ul')
        if ul is not None:
            chips = ''.join(f'<a class="chip-link" href="{esc(a["href"])}">{esc(a.get_text(strip=True))}</a>' for a in ul.find_all('a', href=True))
            cats = f'<div class="blog-cats"><span class="blog-cats__label">Categories</span>{chips}</div>'
            ul.decompose()
        h.decompose()
    rest = ''.join(str(n) for n in root.children)
    tools = f'<div class="blog-tools">{search}{cats}</div>' if (search or cats) else ''
    return rest, pag, tools

def blog_listing(page):
    content, pag, tools = blog_widgets(page['content'])
    groups = card_groups(content)
    cards = ''
    for g in groups:
        if not g['title']: continue
        href = g['href'] or '#'
        cards += f'''<article class="card card--image" data-reveal>
  <a class="card__media" href="{esc(href)}"><img src="{esc(g['img'])}" alt="{esc(g['alt'])}" loading="lazy"></a>
  <div class="card__body">{f'<span class="pill" style="margin-bottom:12px">{esc(g["date"])}</span>' if g['date'] else ''}<h3><a href="{esc(href)}">{esc(g['title'])}</a></h3>{f'<p>{esc(g["excerpt"])}</p>' if g['excerpt'] else ''}{link('Read More', href)}</div>
</article>'''
    heading = page.get('h1') or 'Resource'
    body = subnav(page) + page_hero(page, heading) + f'''
<section class="section section--tight">
  <div class="container">
    {tools}
    <div class="grid grid-3" style="margin-top:32px">{cards}</div>
    {pag}
  </div>
</section>'''
    return layout(page, body)

def blog_post(page):
    content, pag, tools = blog_widgets(page['content'])
    content = re.sub(r'^\s*<h1>.*?</h1>', '', content, count=1, flags=re.S)
    m = re.search(r'^\s*<img[^>]*src="([^"]+)"[^>]*>', content)
    hero_img = ''
    if m: hero_img = m.group(1); content = content[m.end():]
    d = re.search(r'^\s*<h5>(.*?)</h5>', content, re.S); date = ''
    if d: date = d.group(1).strip(); content = content[d.end():]
    content = re.sub(r'^\s*<h3>\s*' + re.escape(html.escape(page['h1'], quote=False)) + r'\s*</h3>', '', content, count=1)
    body = f'''
<section class="page-hero">
  <div class="container"><div class="page-hero__narrow">
    {crumbs(page)}
    {f'<span class="pill" style="margin-bottom:18px">{esc(date)}</span>' if date else ''}
    <h1 data-split>{esc(page['h1'])}</h1>
    {f'<div class="page-hero__banner" data-reveal="scale"><img src="{esc(hero_img)}" alt="" data-parallax="30"></div>' if hero_img else ''}
  </div></div>
</section>
<section class="section section--tight landing">
  <div class="container"><div class="prose prose--wide" data-auto-reveal>{content}</div></div>
</section>
{f'<section class="section section--tight section--surface"><div class="container">{tools}</div></section>' if tools else ''}'''
    return layout(page, body)

def blog_page(page):
    """Any /blog URL: a listing if it holds several posts, otherwise a single post."""
    return blog_listing(page) if len(re.findall(r'>Read More<', page['content'])) >= 2 else blog_post(page)

RENDERERS['/blog/'] = blog_page
RENDERERS['/blog/coaching'] = blog_listing
PREFIX_RENDERERS[:] = [(k, (blog_page if k.startswith('/blog') else f)) for k, f in PREFIX_RENDERERS]
PREFIX_RENDERERS.insert(0, ('/blog/', blog_page))


# ====================================================================== webinar detail
def webinar_detail(page):
    c = page['content']
    m = re.search(r'<h2>(.*?)</h2>', c, re.S)
    title = date = reg_href = reg_text = ''
    if m:
        inner = m.group(1)
        a = re.search(r'<a href="([^"]+)"[^>]*>(.*?)</a>', inner, re.S)
        if a: reg_href, reg_text = a.group(1), re.sub(r'<[^>]+>', '', a.group(2)).strip(); inner = inner.replace(a.group(0), '')
        text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', inner)).strip()
        d = re.search(r'(\d{1,2}\s+[A-Za-z]{3}\s*,.*)$', text)
        if d or a:                                   # a programme title: "Name  11 Jan , 12:00 AM Singapore  Register Now"
            if d: date = d.group(1).strip(); title = text[:d.start()].strip()
            else: title = text
            c = c.replace(m.group(0), '', 1)
        else: reg_href = reg_text = ''               # an ordinary heading: leave it in the body
    title = title or page_heading(page)
    body = subnav(page) + f'''
<section class="page-hero{' page-hero--banner' if page.get('banner') else ''}">
  <div class="container"><div class="page-hero__narrow">
    <h1 data-split>{esc(title)}</h1>
    {f'<p class="lead" data-reveal style="margin-top:18px"><span class="pill">{esc(date)}</span></p>' if date else ''}
    {f'<p data-reveal style="margin-top:24px">{btn(reg_text, reg_href)}</p>' if reg_href else ''}
    {f'<div class="page-hero__banner" data-reveal="scale"><img src="{esc(page["banner"])}" alt="" data-parallax="30"></div>' if page.get('banner') else ''}
  </div></div>
</section>
<section class="section section--tight landing">
  <div class="container">{render_blocks(parse_blocks(c))}</div>
</section>'''
    return layout(page, body)

PREFIX_RENDERERS.insert(0, ('/webinar/', webinar_detail))


# ====================================================================== layout pass: pairs, buttons, sectioned text
ACTION_RE = re.compile(r'read more|register|download|click here|schedule|apply|enquir|view (all|details|more)|learn more|book|contact', re.I)

def _split_prose_for_feature(html_, max_words=150):
    """Take a heading (h2/h3) and the paragraphs/lists that follow it, up to ~max_words, off the front of a prose block."""
    soup = BeautifulSoup(html_, 'lxml'); root = soup.body or soup
    nodes = [n for n in root.children if getattr(n, 'name', None) or str(n).strip()]
    if not nodes: return '', html_
    take, words, i = [], 0, 0
    if getattr(nodes[0], 'name', None) in ('h2', 'h3', 'h4'): take.append(str(nodes[0])); i = 1
    while i < len(nodes):
        n = nodes[i]; nm = getattr(n, 'name', None)
        if nm in ('h2', 'h3', 'h4', 'img', 'form', 'table', 'details'): break
        w = len(_txt(n).split())
        if words and words + w > max_words: break
        take.append(str(n)); words += w; i += 1
    if not take: return '', html_
    return ''.join(take), ''.join(str(n) for n in nodes[i:])

def pair_media(blocks):
    """A lone image beside plain text becomes one side-by-side row (alternating sides)."""
    out = []; i = 0; flip = False
    while i < len(blocks):
        b = blocks[i]
        if b['t'] == 'media':
            nxt = blocks[i + 1] if i + 1 < len(blocks) else None
            prv = out[-1] if out else None
            if nxt and nxt['t'] == 'prose':
                text, rest = _split_prose_for_feature(nxt['html'])
                if text:
                    out.append({'t': 'feature', 'img': b['src'], 'alt': b['alt'], 'html': text, 'flip': flip}); flip = not flip
                    if rest.strip(): blocks[i + 1] = dict(nxt, html=rest)
                    else: i += 1
                    i += 1; continue
            if prv and prv['t'] == 'prose':
                soup = BeautifulSoup(prv['html'], 'lxml'); root = soup.body or soup
                nodes = [n for n in root.children if getattr(n, 'name', None) or str(n).strip()]
                # last heading + what follows it becomes the pair's text
                hi = max((k for k, n in enumerate(nodes) if getattr(n, 'name', None) in ('h2', 'h3', 'h4')), default=-1)
                if hi >= 0 and len(nodes) - hi <= 6:
                    text = ''.join(str(n) for n in nodes[hi:]); rest = ''.join(str(n) for n in nodes[:hi])
                    if rest.strip(): out[-1] = dict(prv, html=rest)
                    else: out.pop()
                    out.append({'t': 'feature', 'img': b['src'], 'alt': b['alt'], 'html': text, 'flip': flip}); flip = not flip
                    i += 1; continue
        out.append(b); i += 1
    return out

def lift_actions(blocks):
    """Standalone action links inside prose become a button row."""
    out = []
    for b in blocks:
        if b['t'] != 'prose': out.append(b); continue
        soup = BeautifulSoup(b['html'], 'lxml'); root = soup.body or soup
        nodes = [n for n in root.children if getattr(n, 'name', None) or str(n).strip()]
        buf = []; acts = []
        def flush_prose():
            if buf: out.append({'t': 'prose', 'html': ''.join(buf)}); buf.clear()
        def flush_acts():
            if acts: out.append({'t': 'actions', 'items': list(acts)}); acts.clear()
        for n in nodes:
            nm = getattr(n, 'name', None)
            a = None
            if nm == 'a' and n.get('href'): a = n
            elif nm == 'p' and len([c for c in n.children if getattr(c, 'name', None) or str(c).strip()]) == 1 and n.find('a', href=True) and not n.find('img'):
                a = n.find('a', href=True)
            if a is not None and ACTION_RE.search(a.get_text()) and len(a.get_text().split()) <= 6:
                flush_prose(); acts.append((a.get_text(' ', strip=True), a['href'])); continue
            flush_acts(); buf.append(str(n))
        flush_prose(); flush_acts()
    return out

def sectionize(blocks):
    """Long text-only pages: each h2 opens a two-column section (heading + lead on the left, the rest on the right)."""
    if any(b['t'] not in ('prose', 'head', 'actions') for b in blocks): return blocks
    html_ = ''.join(b['html'] for b in blocks if b['t'] == 'prose')
    if html_.count('<h2>') < 2 or '<details' in html_ or '<form' in html_ or len(re.sub(r'<[^>]+>', ' ', html_).split()) < 500: return blocks
    out = []
    for b in blocks:
        if b['t'] != 'prose': out.append(b); continue
        parts = re.split(r'(?=<h2>)', b['html'])
        for part in parts:
            if not part.strip(): continue
            if not part.startswith('<h2>'): out.append({'t': 'prose', 'html': part}); continue
            m = re.match(r'(<h2>.*?</h2>)\s*(<p>.*?</p>)?(.*)', part, re.S)
            h2, first, rest = m.group(1), (m.group(2) or ''), (m.group(3) or '')
            if not (first + rest).strip(): out.append({'t': 'prose', 'html': part}); continue
            words = lambda h: len(re.sub(r'<[^>]+>', ' ', h).split())
            # the opening paragraph only joins the heading on the left when plenty remains for the right column
            if words(rest) >= 80 and words(first) <= 90: left, right = h2 + first, rest
            else: left, right = h2, first + rest
            out.append({'t': 'section2', 'left': left, 'right': right})
    return out

SERVICE_PHOTOS = {   # the three service cards become full-photo cards (client photos, Sep 2026)
    'Coaching Education': ('/assets/img/service-education.jpg', '/icf-coaching-training-program'),
    'Coaching Workshop': ('/assets/img/service-workshop.jpg', '/coaching-skill-training-course-and-workshop'),
    'Coaching Service': ('/assets/img/service-service.jpg', '/executive-leadership-coaching-service-for-managers-and-leaders'),
}

def showcase(blocks):
    """A heading, its intro and its button followed by the three service cards fold into one
    showcase block: heading and button on one row, intro beneath, photo cards under that."""
    out = []; i = 0
    while i < len(blocks):
        b = blocks[i]
        if b['t'] == 'cards' and b['items'] and all(c['title'].strip() in SERVICE_PHOTOS for c in b['items']):
            head = prose = None; acts = []
            k = len(out) - 1
            while k >= 0 and out[k]['t'] in ('prose', 'actions', 'head') and head is None:
                if out[k]['t'] == 'actions': acts = out[k]['items'] + acts
                elif out[k]['t'] == 'prose': prose = out[k]['html'] + (prose or '')
                else: head = out[k]
                k -= 1
            if head is not None:
                del out[k + 1:]
                out.append({'t': 'showcase', 'head': head, 'prose': prose, 'actions': acts, 'items': b['items']}); i += 1; continue
        out.append(b); i += 1
    return out

def program_accordions(blocks):
    """A card row that follows a stat-group row becomes centred open/close cards."""
    out = []
    for b in blocks:
        prev = [x for x in out if x['t'] != 'chips']
        if b['t'] == 'cards' and prev and prev[-1]['t'] == 'statrow':
            out.append({'t': 'acc', 'items': b['items']}); continue
        out.append(b)
    return out

_orig_render_blocks = render_blocks
def render_blocks(blocks):
    # whole-list passes first (they look at neighbouring blocks), then the layout passes
    blocks = program_accordions(showcase(sectionize(lift_actions(pair_media(attach_logo_intros(merge_stat_rows(blocks)))))))
    centre_idx = set()   # the heading and intro that introduce a stat-group row are centred over it
    for i, b in enumerate(blocks):
        if b['t'] == 'statrow':
            j = i - 1
            while j >= 0 and blocks[j]['t'] in ('prose', 'chips'): j -= 1
            if j >= 0 and blocks[j]['t'] == 'head': centre_idx.update(range(j, i))
    out = []
    for b in blocks:
        if b['t'] == 'acc':
            cards = ''
            for k, c in enumerate(b['items']):
                op = k == 0
                icon = f'<span class="acc-card__icon"><img src="{esc(c["img"])}" alt="" loading="lazy"></span>' if c['img'] else '<span class="acc-card__icon"></span>'
                cards += (f'<article class="acc-card{" is-open" if op else ""}" data-reveal><button class="acc-card__head" type="button" aria-expanded="{"true" if op else "false"}">'
                          f'{icon}<span class="acc-card__title">{esc(c["title"])}</span><span class="acc-card__chev" aria-hidden="true"></span></button>'
                          f'<div class="acc-card__body"><div class="acc-card__inner"><div class="prose"><p>{c["body"]}</p></div></div></div></article>')
            out.append(f'<div class="lp-block lp-block--acc"><div class="acc-cards acc-cards--center" data-accordion>{cards}</div></div>')
        elif b['t'] == 'showcase':
            btns = ''.join(btn(t, h, '' if k == 0 else 'btn--ghost') for k, (t, h) in enumerate(b['actions']))
            acts = f'<div class="actions" data-reveal>{btns}</div>' if btns else ''
            intro = f'<div class="prose showcase__intro" data-auto-reveal>{b["prose"]}</div>' if b['prose'] else ''
            cards = ''
            for c in b['items']:
                src, href = SERVICE_PHOTOS[c['title'].strip()]
                cards += (f'<a class="photo-card" href="{href}" data-reveal><img src="{src}" alt="" loading="lazy"><span class="photo-card__scrim"></span>'
                          f'<h3>{esc(c["title"])}</h3><p>{c["body"]}</p></a>')
            out.append(f'<div class="lp-block lp-block--showcase"><div class="showcase__row"><div class="section-head">'
                       f'<p class="eyebrow" data-reveal>{esc(b["head"]["eyebrow"])}</p><h2 data-reveal>{b["head"]["h2"]}</h2></div>{acts}</div>'
                       f'{intro}<div class="photo-cards">{cards}</div></div>')
        elif b['t'] == 'feature':
            out.append(f'<div class="lp-block lp-block--feature"><div class="feature-row{" feature-row--flip" if b["flip"] else ""}">'
                       f'<div class="feature-row__media media" data-reveal="scale"><img src="{esc(b["img"])}" alt="{esc(b["alt"])}" loading="lazy" data-parallax="18"></div>'
                       f'<div class="prose" data-auto-reveal>{b["html"]}</div></div></div>')
        elif b['t'] == 'actions':
            btns = ''.join(btn(t, h, '' if k == 0 else 'btn--ghost') for k, (t, h) in enumerate(b['items']))
            out.append(f'<div class="lp-block lp-block--actions"><div class="actions" data-reveal>{btns}</div></div>')
        elif b['t'] == 'section2':
            out.append(f'<div class="lp-block lp-block--section2"><div class="split-sticky"><div class="split-sticky__left"><div class="prose prose--wide" data-auto-reveal>{b["left"]}</div></div>'
                       f'<div class="split-sticky__right"><div class="prose prose--wide" data-auto-reveal>{b["right"]}</div></div></div></div>')
        else:
            out.append(_orig_render_blocks([b]))
    for i in centre_idx:
        out[i] = out[i].replace('class="lp-block lp-block--', 'class="lp-block lp-block--center lp-block--', 1)
    return '\n'.join(out)

# text-only pages go through the same layout pass instead of the plain article template
_orig_generic = generic_page
def generic_page(page):
    from build import strip_duplicate_heading, subnav as _sub, page_hero as _hero, layout as _layout, take_lead as _lead
    content = strip_duplicate_heading(page['content'], page.get('h1'))
    content = re.sub(r'^\s*<h1>.*?</h1>', '', content, count=1, flags=re.S)
    lead, content = _lead(page, content)
    blocks = sectionize(lift_actions(pair_media(parse_blocks(content))))
    if all(b['t'] == 'prose' for b in blocks): return _orig_generic(page)
    body = _sub(page) + _hero(page, lead=lead) + f'''
<section class="section section--tight landing">
  <div class="container">{render_blocks(blocks)}</div>
</section>
{cta_band()}'''
    return _layout(page, body)


# ====================================================================== Mentor Coaching + Our Unique Approach (open layouts, Sep 2026)
def _mc_curve(side):
    return ('<svg class="deco-curve deco-curve--' + side + '" viewBox="0 0 220 900" preserveAspectRatio="none" aria-hidden="true">'
            '<path class="deco-curve__fill" d="M220 0 H150 C60 160 200 330 110 480 C30 620 170 760 90 900 H220 Z"/>'
            '<path class="deco-curve__line" d="M118 0 C28 160 168 330 78 480 C-2 620 138 760 58 900"/></svg>')

def _inner(n):
    return n.decode_contents().strip() if hasattr(n, 'decode_contents') else str(n).strip()

def _plain(h):
    return re.sub(r'<[^>]+>', '', h).strip()

def _mc_testimonials(details):
    """Irregular photo / name / words runs inside the praise section -> list of dicts."""
    out = []; pending = None; cur = None
    for n in details.children:
        nm = getattr(n, 'name', None)
        if nm in (None, 'summary'): continue
        im = n if nm == 'img' else n.find('img')
        if im is not None: pending = im.get('src')
        if not _txt(n): continue
        if cur is not None and not cur['text']:
            for t in n.find_all(['img', 'br']): t.decompose()
            cur['text'] = _inner(n)
        else:
            cur = {'name': _txt(n), 'img': pending, 'text': ''}; pending = None; out.append(cur)
    return [t for t in out if t['text']]

def _mc_quote(t):
    m = re.match(r'(.+?)\s+(from\s.+)$', t['name'])
    who = ('<b>' + esc(m.group(1)) + '</b><span>' + esc(m.group(2)) + '</span>') if m else '<b>' + esc(t['name']) + '</b>'
    av = ('<img src="' + t['img'] + '" alt="">') if t['img'] else '<span class="quote-card__initial" aria-hidden="true">' + esc(t['name'][:1]) + '</span>'
    return '<figure class="quote-card quote-card--mentor"><span class="q">“</span><p>' + t['text'] + '</p><figcaption class="who">' + av + '<div>' + who + '</div></figcaption></figure>'

_PKG_RE = re.compile(r'^(Package\s+\d+)\s*\[\s*(.*?)\s*\]\s*@\s*(\S+)$')
_FEAT_RE = re.compile(r'^(\d+)\s+(.*?)\s*(\[[^\]]*\])?$')

def _mc_packages(details):
    intro = []; pkgs = []
    for n in details.children:
        nm = getattr(n, 'name', None)
        if nm in (None, 'summary'): continue
        txt = _txt(n)
        if not txt: continue
        if nm == 'h5' and _PKG_RE.match(txt):
            a, b, c = _PKG_RE.match(txt).groups(); pkgs.append({'name': a, 'tier': b, 'price': c, 'desc': [], 'feats': []})
        elif nm == 'h5' and pkgs and _FEAT_RE.match(txt):
            pkgs[-1]['feats'].append(_FEAT_RE.match(txt).groups())
        elif pkgs: pkgs[-1]['desc'].append(_inner(n))
        else: intro.append(_inner(n))
    return intro, pkgs

def _mc_price(pk, k):
    """Pricing card. DOM keeps name, tier and price together (they are one line of copy); CSS orders the headline above the price row."""
    def feat(num, label, note):
        note_html = (' <span class="price__note">' + esc(note) + '</span>') if note else ''
        return '<li><b class="price__n">' + esc(num) + '</b> <span>' + esc(label) + note_html + '</span></li>'
    descs = list(pk['desc'])
    head, sub = '', ''
    if descs:
        parts = re.split(r'(?<=\.)\s+', descs[0], maxsplit=1)
        head = parts[0]; sub = ' '.join(parts[1:] + descs[1:])
    sub = sub.replace('50 coaches', '<strong>50 coaches</strong>', 1)
    dark = bool(k)
    return ('<div class="price ' + ('price--dark' if dark else 'price--light') + '" data-reveal>'
            '<div class="price__top"><span class="price__name">' + esc(pk['name']) + '</span> <span class="price__br" aria-hidden="true">[</span> '
            '<span class="price__tier">' + esc(pk['tier']) + '</span> <span class="price__br" aria-hidden="true">]</span></div>'
            '<div class="price__bar"><div class="price__amount"><span class="price__br" aria-hidden="true">@</span> ' + esc(pk['price']) + '</div>'
            '<a class="btn ' + ('btn--white' if dark else '') + '" href="/registration">Registration' + ARROW + '</a>'
            '<div class="price__coach"><img src="/assets/img/ben-mentor.jpg" alt=""><span><b>Dr Ben Koh</b><small>Master Certified Coach</small></span></div></div>'
            + (('<p class="price__headline">' + head + '</p>') if head else '')
            + (('<p class="price__sub">' + sub + '</p>') if sub else '')
            + '<ul class="price__list">' + ''.join(feat(*f) for f in pk['feats']) + '</ul></div>')

def _mc_how(details):
    kids = [n for n in details.children if getattr(n, 'name', None) not in (None, 'summary')]
    ul_i = next(i for i, n in enumerate(kids) if n.name == 'ul')
    before = [_inner(n) for n in kids[:ul_i] if _txt(n)]
    steps, reviews, closing = [], [], []
    for li in kids[ul_i].find_all('li'):
        t = _txt(li)
        if not t: continue
        (reviews if (':' in t[:40] and len(t) > 60) else steps).append(_inner(li))
    for n in kids[ul_i + 1:]:
        t = _txt(n)
        if not t: continue
        (reviews if (':' in t[:40] and len(t) > 60) else closing).append(_inner(n))
    return before, steps, reviews, closing

def mentor_coaching(page):
    nodes = top_nodes(page['content'])
    tags = [getattr(n, 'name', None) for n in nodes]
    dets = [n for n in nodes if getattr(n, 'name', None) == 'details']
    if len(dets) != 4 or 'img' not in tags or tags[0] != 'h4':
        print('!! mentor-coaching layout pattern changed:', tags); return smart_page(page)
    i_img = tags.index('img'); i_det = tags.index('details'); i_after = max(i for i, t in enumerate(tags) if t == 'details') + 1
    title = _txt(nodes[0])
    title_html = (esc(title[:-10]) + '<em class="hl">Dr Ben Koh</em>') if title.endswith(' Dr Ben Koh') else esc(title)
    intro = [_inner(n) for n in nodes[1:i_img] if getattr(n, 'name', None) == 'p' and _txt(n)]
    ben = [_inner(n) for n in nodes[i_img + 1:i_det] if getattr(n, 'name', None) == 'p' and _txt(n)]
    d_how, d_samples, d_pkg, d_praise = dets
    summ = lambda d: _txt(d.summary) if d.summary else ''

    # how it works
    before, steps, reviews, closing = _mc_how(d_how)
    label = before[-1] if before and len(_plain(before[-1])) < 70 else ''
    how_ps = before[1:-1] if label else before[1:]
    def review(h):
        a, b = h.split(':', 1)
        return '<div class="mc-review" data-reveal><h3>' + a.strip() + ':</h3><p>' + b.strip() + '</p></div>'
    # samples
    sample_ps = [_inner(n) for n in d_samples.children if getattr(n, 'name', None) == 'p' and _txt(n)]
    shots = [im.get('src', '') for im in d_samples.find_all('img')]
    thumbs = ''.join('<a class="report-thumb" href="' + esc(src.replace(' ', '%20')) + '" data-lightbox="reports" data-reveal>'
                     '<img src="' + esc(src.replace(' ', '%20')) + '" alt="Sample feedback report ' + str(k + 1) + '" loading="lazy">'
                     '<span class="report-thumb__zoom" aria-hidden="true"></span></a>' for k, src in enumerate(shots))
    # packages + praise
    pkg_intro, pkgs = _mc_packages(d_pkg)
    praise = _mc_testimonials(d_praise); half = (len(praise) + 1) // 2
    # ICF credential + video
    tail = nodes[i_after:]
    t_h = next((k for k, n in enumerate(tail) if getattr(n, 'name', None) in ('h2', 'h3', 'h4')), None)
    ifr = next((n.find('iframe') for n in tail if hasattr(n, 'find') and n.find('iframe')), None)
    ym = re.search(r'embed/([\w-]{6,})', ifr.get('src', '')) if ifr else None
    yid = ym.group(1) if ym else ''
    tail_ps = lambda seq: [_inner(n) for n in seq if getattr(n, 'name', None) == 'p' and _txt(n)]
    cred_ps = tail_ps(tail[:t_h] if t_h is not None else tail) + tail_ps(tail[t_h + 1:] if t_h is not None else [])
    if cred_ps: cred_ps[0] = cred_ps[0].replace('SETS YOU APART', '<strong>SETS YOU APART</strong>', 1)
    cred_h = _txt(tail[t_h]) if t_h is not None else ''

    body = subnav(page) + page_hero(page) + (
        '<section class="section mc-intro"><div class="container mc-intro__grid">'
          '<div><h2 data-reveal>' + title_html + '</h2>'
          + ''.join(('<p class="lead" data-reveal>' if k == 0 else '<p data-reveal>') + x + '</p>' for k, x in enumerate(intro)) +
          '</div>'
          '<div class="media-stack" data-reveal="scale"><div class="media media--tall media--blob"><img src="/assets/img/ben-mentor.jpg" alt="Dr Ben Koh, Master Certified Coach" data-parallax="20"></div>'
          '<div class="badge-float" style="left:-6%;right:auto;top:auto;bottom:12%"><img src="/assets/img/badges/icf-mcc.png" alt="" width="54" height="54"><div><b>MCC</b><span>Master Certified Coach</span></div></div></div>'
        '</div></section>'

        '<section class="section section--green ben-band has-curve">' + _mc_curve('right') +
        '<div class="container ben-band__grid">'
          '<p class="ben-band__big" data-reveal>' + (ben[0].replace('more than 2000 coaches', '<strong>more than 2000 coaches</strong>', 1) if ben else '') + '</p>'
          '<div class="ben-band__side">' + ''.join(('<p class="ben-band__close" data-reveal>' if k == len(ben) - 2 else '<p data-reveal>') + x + '</p>' for k, x in enumerate(ben[1:])) + '</div>'
        '</div></section>'

        '<section class="section section--white mc-how"><div class="container mc-how__grid">'
          '<div class="mc-how__left"><h2 data-reveal>' + esc(summ(d_how)) + '</h2>' + (('<p class="lead" data-reveal>' + before[0] + '</p>') if before else '') + '</div>'
          '<div class="mc-how__right">' + ''.join('<p data-reveal>' + x + '</p>' for x in how_ps)
          + (('<p class="mc-label" data-reveal>' + label + '</p>') if label else '')
          + '<ol class="mc-steps">' + ''.join('<li data-reveal>' + x + '</li>' for x in steps) + '</ol>'
          + '<div class="mc-reviews">' + ''.join(review(r) for r in reviews) + '</div>'
          + ''.join('<p data-reveal>' + x + '</p>' for x in closing) +
        '</div></div></section>'

        '<section class="section section--surface mc-samples"><div class="container mc-samples__grid">'
          '<div class="mc-samples__text"><h2 data-reveal>' + esc(summ(d_samples)) + '</h2>' + ''.join('<p data-reveal>' + x + '</p>' for x in sample_ps) + '</div>'
          '<div class="reports">' + thumbs + '</div>'
        '</div></section>'

        '<section class="section packages has-curve">' + _mc_curve('left') + '<div class="container">'
          '<div class="section-head center" style="margin-inline:auto"><h2 data-reveal>' + esc(summ(d_pkg)) + '</h2>' + ''.join('<p data-reveal>' + x + '</p>' for x in pkg_intro) + '</div>'
          '<div class="price-row">' + ''.join(_mc_price(pk, k) for k, pk in enumerate(pkgs)) + '</div>'
        '</div></section>'

        '<section class="section section--surface praise"><div class="container"><div class="section-head center" style="margin-inline:auto"><h2 data-reveal>' + esc(summ(d_praise)) + '</h2></div></div>'
          '<div class="marquee" data-reveal="none"><div class="marquee__track" style="animation-duration:95s">' + ''.join(_mc_quote(t) for t in praise[:half]) + '</div></div>'
          '<div class="marquee marquee--reverse" data-reveal="none"><div class="marquee__track" style="animation-duration:110s">' + ''.join(_mc_quote(t) for t in praise[half:]) + '</div></div>'
        '</section>'

        '<section class="section section--white mc-cred"><div class="container mc-cred__grid">'
          '<div>' + ''.join(('<p class="mc-cred__lead" data-reveal>' if k == 0 else '<p data-reveal>') + x + '</p>' for k, x in enumerate(cred_ps)) + '</div>'
          '<div>' + (('<div class="video-card mc-cred__video" data-reveal="scale"><img src="https://i.ytimg.com/vi/' + yid + '/hqdefault.jpg" alt="" loading="lazy">'
                      '<a class="video-card__play" href="https://www.youtube.com/watch?v=' + yid + '" data-video aria-label="Play video"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></a></div>') if yid else '')
          + (('<h3 class="mc-cred__caption" data-reveal>' + esc(cred_h) + '</h3>') if cred_h else '') + '</div>'
        '</div></section>')
    return layout(page, body)

def unique_approach(page):
    nodes = top_nodes(page['content'])
    tags = [getattr(n, 'name', None) for n in nodes]
    expect = ['h2', 'p', 'p', 'p', 'p', 'h5', 'h3', 'p', 'h3', 'p', 'ul', 'img', 'h5', 'ul']
    if tags != expect:
        print('!! our-unique-approach layout pattern changed:', tags); return smart_page(page)
    h2, p1, p2, p3, q1, q2, h3a, pa, h3b, pb, ul1, logo, q3, ul2 = nodes
    lis = lambda ul: ''.join('<li data-reveal>' + _inner(li) + '</li>' for li in ul.find_all('li') if _txt(li))
    body = subnav(page) + page_hero(page) + (
        '<section class="section ua-intro has-curve">' + _mc_curve('right') + '<div class="container ua-intro__grid">'
          '<div><h2 data-reveal>' + _inner(h2) + '</h2><p class="ua-intro__lead" data-reveal>' + _inner(p1) + '</p></div>'
          '<div><p data-reveal>' + _inner(p2) + '</p><p class="ua-intro__strong" data-reveal>' + _inner(p3) + '</p></div>'
        '</div></section>'

        '<section class="section section--green ua-quotes">'
          '<svg class="ua-quotes__curve" viewBox="0 0 1440 600" preserveAspectRatio="none" aria-hidden="true">'
            '<path d="M-20 600 L-20 560 C320 430 540 660 840 500 S1280 230 1460 310 L1460 600 Z" fill="#eb6422" opacity=".16"/>'
            '<path d="M-20 520 C300 380 520 620 820 460 S1260 180 1460 260" fill="none" stroke="#eb6422" stroke-width="2" opacity=".65" vector-effect="non-scaling-stroke"/></svg>'
          '<div class="container ua-quotes__grid">'
            '<blockquote class="ua-quote ua-quote--big" data-reveal><div>' + _inner(q1) + '</div></blockquote>'
            '<blockquote class="ua-quote ua-quote--small" data-reveal><div>' + _inner(q2) + '</div></blockquote>'
        '</div></section>'

        '<section class="section section--white ua-steps"><div class="container ua-steps__grid">'
          '<svg class="ua-steps__link" viewBox="0 0 400 300" preserveAspectRatio="none" aria-hidden="true"><path d="M0 30 C170 30 190 270 400 262" fill="none" stroke="#eb6422" stroke-width="2" stroke-dasharray="6 9" vector-effect="non-scaling-stroke"/></svg>'
          '<div class="ua-step"><h3 data-reveal>' + _inner(h3a) + '</h3><p data-reveal>' + _inner(pa) + '</p></div>'
          '<div class="ua-step ua-step--low"><h3 data-reveal>' + _inner(h3b) + '</h3><p class="ua-step__lead" data-reveal>' + _inner(pb) + '</p><ul class="list-check">' + lis(ul1) + '</ul></div>'
        '</div></section>'

        '<section class="section section--surface ua-close has-curve">' + _mc_curve('left') + '<div class="container ua-close__grid">'
          '<div><div class="ua-close__logo" data-reveal="scale"><img src="' + esc(logo.get('src', '')) + '" alt="ICF Coaching Education" loading="lazy"></div>'
          '<blockquote class="ua-quote ua-quote--ink" data-reveal><div>' + _inner(q3) + '</div></blockquote></div>'
          '<ul class="ua-close__list">' + lis(ul2) + '</ul>'
        '</div></section>')
    return layout(page, body)

RENDERERS['/pages/mentor-coaching'] = mentor_coaching
RENDERERS['/pages/our-unique-approach'] = unique_approach
