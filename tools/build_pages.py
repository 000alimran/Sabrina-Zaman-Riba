#!/usr/bin/env python3
# Generates the subpages for sabrina-zaman-riba (static, no runtime build step).
import re, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700&family=Libre+Caslon+Condensed:ital,wght@0,400;0,500;1,400;1,500&family=Tiro+Bangla&display=swap" rel="stylesheet">'

def shell(title, desc, current, content, og_img="about.jpg"):
    nav_items = [("about.html","About"),("work.html","Work"),("albums.html","Albums"),("media-kit.html","Media kit"),("press.html","Press"),("contact.html","Contact")]
    nav = "\n      ".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h==current else ""}>{t}</a>' for h,t in nav_items)
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#FBF8F2">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://sabrina-zaman-riba.pages.dev/assets/img/{og_img}">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='24' fill='%23B3202E'/><text x='50' y='72' font-size='60' font-family='serif' font-style='italic' text-anchor='middle' fill='%23FBF8F2'>R</text></svg>">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  {FONTS}
  <link rel="stylesheet" href="assets/vendor/glightbox.min.css">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>

<a class="skip-link" href="#main">Skip to content</a>

<header class="nav-wrap" id="top">
  <div class="site-header">
    <a class="wordmark" href="index.html">S.Z.Riba</a>
    <nav class="site-nav" id="siteNav" aria-label="Main">
      {nav}
    </nav>
    <a class="btn btn-solid nav-book" href="contact.html">Book Riba<span class="btn-arr" aria-hidden="true">→</span></a>
    <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="siteNav">
      <span class="nav-toggle-line"></span>
      <span class="nav-toggle-line"></span>
      <span class="sr-only">Menu</span>
    </button>
  </div>
</header>

<main id="main">
{content}
</main>

<footer class="site-footer">
  <p class="footer-bn" lang="bn">সাবরিনা জামান রিবা</p>
  <p class="footer-line">Model, stylist &amp; creative director — Dhaka, Bangladesh</p>
  <nav class="footer-nav" aria-label="Footer">
    <a href="about.html">About</a><a href="work.html">Work</a><a href="albums.html">Albums</a><a href="media-kit.html">Media kit</a><a href="press.html">Press</a><a href="contact.html">Contact</a>
  </nav>
  <p class="footer-fine">© <span id="year">2026</span> Sabrina Zaman Riba · Site by The YOLO Studio</p>
</footer>

<a class="mobile-book" href="contact.html">Book Riba</a>

<script src="assets/vendor/gsap.min.js" defer></script>
<script src="assets/vendor/ScrollTrigger.min.js" defer></script>
<script src="assets/vendor/Flip.min.js" defer></script>
<script src="assets/vendor/lenis.min.js" defer></script>
<script src="assets/vendor/split-type.min.js" defer></script>
<script src="assets/vendor/glightbox.min.js" defer></script>
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''


BRANDS = {
 "Brands": ["Aarong","Taaga","Robi","Airtel","Teletalk","Sunsilk","Pond's","Lux","Veet","Surf Excel","Dabur Amla","VIVO","Yamaha","Vision","Shwapno","RISE","QRIUS","Sailor","Merlot","Kay Kraft","Anjan's","Texmart","Red Origin","Mbrella","Cats Eye","Twelve","Karpas","ALMIRA","Sadakalo","Khan Brothers","Tribeni","CANVAS","Grandeur","El Zein","Banthai","Amber Lifestyle","Orion Footwear","Rang Bangladesh"],
 "Designers & couture": ["Masterpiece by Masheerah Hasan","Viola by Fariha","Mayasir by Maheen Khan","HERSORY by Aarong","Glamarts","Tangail Saree Kuthir","Sandalina"],
 "On screen & in print": ["Prothom Alo — Naksha","The Daily Star","Channel i","ATN Bangla","NTV","Rtv","Maasranga Television","SA TV","ETV","ICETODAY"],
 "Runways & shows": ["Aarong Fashion Show","Rtv Lux Bridal Festival","Sunsilk ATH Show","Muslin Festival","WE — for fashion runway","Pond's Lustrous Runway","British Council show","SAARC fashion show"],
}
def brand_wall(link=True):
    groups = []
    for g, names in BRANDS.items():
        items = "".join(f'<li>{n}</li>' for n in names)
        groups.append(f'<div class="bw-group"><h3 class="bw-label">{g}</h3><ul class="bw-list">{items}</ul></div>')
    return f'''
<section class="section brand-wall" id="brands">
  <p class="eyebrow"><span class="badge-dot" aria-hidden="true"></span>Worked with</p>
  <div class="section-head">
    <h2 class="section-title">60-plus names, one <em>face</em></h2>
    <p class="section-intro">Brands, designers, channels and runways — straight from her own archive.</p>
  </div>
  {"".join(groups)}
</section>'''

def page_hero(kicker, title_html, intro):
    return f'''
<section class="page-hero">
  <p class="eyebrow"><span class="badge-dot" aria-hidden="true"></span>{kicker}</p>
  <h1 class="page-title" data-split>{title_html}</h1>
  <p class="page-intro">{intro}</p>
</section>'''

# ───────────────────────── ABOUT ─────────────────────────
about = page_hero("About", 'Hi, I&rsquo;m <em>Riba</em>',
  "Model first — then stylist, choreographer and director. A decade on Bangladesh's biggest ramps, and lately behind the camera too.") + '''

<section class="section">
  <div class="about-grid">
    <figure class="about-portrait" data-parallax><img src="assets/img/about.jpg" alt="Portrait of Sabrina Zaman Riba" loading="eager"></figure>
    <div class="about-copy">
      <p class="lede">A decade on the ramp teaches you what a frame needs before the photographer says it.</p>
      <p>I started as a runway model in 2010. These days the work rarely stops at the end of the catwalk: I style the shoots I appear in, choreograph shows, and direct. Recent firsts include co-directing the music video “E Shohore Tumihin”, shot across Kolkata, and a fashion film with a European Fashion Film Award–winning director — now headed for festivals in Europe and America.</p>
      <dl class="fact-list">
        <div><dt>Based in</dt><dd>Dhaka, Bangladesh</dd></div>
        <div><dt>Niche</dt><dd>Runway · Editorial · Bridal · Campaign</dd></div>
        <div><dt>Languages</dt><dd>বাংলা · English · हिन्दी</dd></div>
        <div><dt>Open to</dt><dd>Worldwide travel</dd></div>
        <div><dt>Representation</dt><dd>AMTC roster</dd></div>
      </dl>
      <p class="signature" lang="bn">— সাবরিনা জামান রিবা</p>
    </div>
  </div>
</section>

<section class="section section-tan">
  <div class="section-inner">
  <p class="eyebrow"><span class="badge-dot" aria-hidden="true"></span>Comp card</p>
  <div class="section-head">
    <h2 class="section-title">The <em>stats</em></h2>
    <p class="section-intro">Agency-standard figures — full card on request.</p>
  </div>
  <dl class="comp-grid">
    <div><dt>Height</dt><dd>5′8″</dd></div>
    <div><dt>Chest</dt><dd>34″</dd></div>
    <div><dt>Waist</dt><dd>26″</dd></div>
    <div><dt>Hips</dt><dd>36″</dd></div>
    <div><dt>Shoe</dt><dd>EU 40</dd></div>
    <div><dt>Hair</dt><dd>Black</dd></div>
  </dl>
  </div>
</section>

<section class="section">
  <p class="eyebrow"><span class="badge-dot" aria-hidden="true"></span>Beyond the runway</p>
  <div class="section-head">
    <h2 class="section-title">Three more hats, one <em>eye</em></h2>
    <p class="section-intro">What a booking can include beyond the walk.</p>
  </div>
  <ul class="svc-grid svc-grid-3">
    <li>
      <h3>Styling</h3>
      <p>Wardrobe and look direction for editorials and campaigns — including shoots credited as both model and stylist, like Merlot in The Daily Star.</p>
      <span class="svc-note">Scoped per brief</span>
    </li>
    <li>
      <h3>Choreography</h3>
      <p>Show choreography and ramp direction, built on ten-plus years of knowing exactly how a collection should move.</p>
      <span class="svc-note">Bookable on its own</span>
    </li>
    <li>
      <h3>Direction</h3>
      <p>Co-directed “E Shohore Tumihin” for Studio Maestros, shot in Kolkata; currently finishing a festival-bound fashion film.</p>
      <span class="svc-note">Motion &amp; film</span>
    </li>
  </ul>
</section>

<section class="section section-ink">
  <div class="section-inner">
  <p class="eyebrow"><span class="badge-dot" aria-hidden="true"></span>Milestones</p>
  <div class="section-head">
    <h2 class="section-title">The road so <em>far</em></h2>
    <p class="section-intro">Dated from her own archive of 170 albums.</p>
  </div>
  <ol class="timeline">
    <li><span class="tl-when">2010</span><div><h3>First ramp</h3><p>The runway years begin in Dhaka.</p></div></li>
    <li><span class="tl-when">2014</span><div><h3>WE — for fashion runway</h3><p>Walking the 2014 edition — and back again in 2015.</p></div></li>
    <li><span class="tl-when">2015</span><div><h3>Rtv Lux Bridal Festival</h3><p>Bridal runway on national television.</p></div></li>
    <li><span class="tl-when">2016</span><div><h3>Muslin Festival &amp; Sunsilk ATH Show</h3><p>Heritage textiles on one stage, a beauty-brand show on another.</p></div></li>
    <li><span class="tl-when">2017</span><div><h3>Aarong Fashion Show</h3><p>On the ramp for the country's best-known lifestyle brand.</p></div></li>
    <li><span class="tl-when">2021</span><div><h3>National interview</h3><p>“I think I will do experimental work with myself” — Shampratik Deshkal.</p></div></li>
    <li><span class="tl-when">2023</span><div><h3>সমর্থন বাংলাদেশ কনসার্ট</h3><p>On stage at the 2023 concert.</p></div></li>
    <li><span class="tl-when">2024–25</span><div><h3>RISE, two seasons</h3><p>Winter ’24 in the studio, Fall ’25 on the streets of Dhaka.</p></div></li>
    <li><span class="tl-when">Next</span><div><h3>Fashion film</h3><p>With a European Fashion Film Award–winning director — bound for festivals in Europe and America.</p></div></li>
  </ol>
  </div>
</section>

<section class="section">
  <div class="cta-band">
    <p>Want the longer story — or the comp card PDF? <em>Ask.</em></p>
    <a class="btn btn-solid" href="contact.html">Get in touch<span class="btn-arr" aria-hidden="true">→</span></a>
  </div>
</section>'''

# ───────────────────────── WORK ─────────────────────────
def work_item(cat, img, alt, badge, title, sub):
    return f'''    <li class="work-item" data-cat="{cat}">
      <a class="work-link glightbox" href="assets/img/{img}" data-gallery="work" data-description="{title} — {sub}">
        <figure class="work-frame"><img src="assets/img/{img}" alt="{alt}" loading="lazy"><figcaption class="card-badge">{badge}</figcaption></figure>
      </a>
      <div class="work-meta"><h3>{title}</h3><p>{sub}</p></div>
    </li>'''

work_items = "\n".join([
  work_item("runway","hero-runway.jpg","Riba walking for ZURHEM in a sequined black-tie look","Runway","ZURHEM — black tie","Runway showcase"),
  work_item("runway","work/zurhem-runway.jpg","Riba walking for ZURHEM in all white","Runway","ZURHEM — resort","Runway showcase"),
  work_item("commercial","work/qrius.jpg","QRIUS festive campaign — family table scene","Campaign","QRIUS","Festive campaign"),
  work_item("commercial","work/rise-fall.jpg","RISE Fall Collection 25 at a flower market","Campaign","RISE","Fall Collection ’25"),
  work_item("commercial","hero-campaign.jpg","RISE Fall Collection 25 on a Dhaka street","Campaign","RISE","Street story, Fall ’25"),
  work_item("commercial","work/jewellery.jpg","Gold jewellery campaign","Campaign","Jewellery campaign","Commercial"),
  work_item("editorial","work/rm-masterpiece.jpg","RM Masterpiece editorial","Editorial","RM — Masterpiece","Editorial"),
  work_item("editorial","work/saree-story.jpg","Saree editorial against a Bengali calligraphy wall","Editorial","Saree story","Editorial"),
  work_item("editorial","hero-editorial.jpg","Riba in red with a black cat by candlelight","Editorial","Nine lives","Editorial"),
  work_item("bridal","work/bridal-01.jpg","Heritage bridal look with kundan jewellery","Bridal","Heritage bridal","Bridal campaign"),
  work_item("bridal","story-bridal.jpg","Bridal portrait in gold and green","Bridal","Gold &amp; emerald","Bridal campaign"),
  work_item("bridal","work/bridal-02.jpg","Velvet and gold bridal editorial","Bridal","Velvet &amp; gold","Bridal editorial"),
])

work = page_hero("Selected work", 'Work that <em>walks</em>',
  "Runway, editorial, bridal and campaign — tap any frame to view it full-screen.") + f'''

<section class="section">
  <div class="filters" role="group" aria-label="Filter work by category">
    <button class="filter is-active" data-filter="all">All</button>
    <button class="filter" data-filter="runway">Runway</button>
    <button class="filter" data-filter="editorial">Editorial</button>
    <button class="filter" data-filter="bridal">Bridal</button>
    <button class="filter" data-filter="commercial">Campaign</button>
  </div>

  <ul class="work-grid work-grid-3" id="workGrid">
{work_items}
  </ul>
  <p class="work-empty" id="workEmpty" hidden>Nothing in this category yet — photos are on the way.</p>
</section>

<section class="section">
  <div class="cta-band">
    <p>Like a frame? The next one can be <em>yours.</em></p>
    <a class="btn btn-solid" href="contact.html">Start a brief<span class="btn-arr" aria-hidden="true">→</span></a>
  </div>
</section>'''

# ───────────────────────── MEDIA KIT ─────────────────────────
mediakit = page_hero("Media kit", 'The <em>numbers</em>',
  "A style-focused audience across three platforms — figures as of Nov 2026, full engagement breakdown on request.") + '''

<section class="section section-ink">
  <div class="section-inner">
  <dl class="num-grid">
    <div><dd data-count="130" data-suffix="K+">130K+</dd><dt>combined following</dt></div>
    <div><dd data-count="88.6" data-suffix="K">88.6K</dd><dt>Instagram followers</dt></div>
    <div><dd data-count="42" data-suffix="K">42K</dd><dt>Facebook followers</dt></div>
    <div><dd data-count="230" data-suffix="">230</dd><dt>YouTube videos</dt></div>
  </dl>
  <ul class="platform-rows">
    <li>
      <a class="plat-link" href="https://www.instagram.com/sabrinazamanribaauthentic/" target="_blank" rel="noopener">
        <span class="plat-name">Instagram</span>
        <span class="plat-handle">@sabrinazamanribaauthentic</span>
        <span class="plat-note">88.6K followers · 1,232 posts</span>
      </a>
    </li>
    <li>
      <a class="plat-link" href="https://www.facebook.com/sabrinaribaofficial" target="_blank" rel="noopener">
        <span class="plat-name">Facebook</span>
        <span class="plat-handle">/sabrinaribaofficial</span>
        <span class="plat-note">42K followers · Official page</span>
      </a>
    </li>
    <li>
      <a class="plat-link" href="https://www.youtube.com/@sabrinazamanriba" target="_blank" rel="noopener">
        <span class="plat-name">YouTube</span>
        <span class="plat-handle">@SabrinaZamanRiba</span>
        <span class="plat-note">230 videos · Interviews &amp; campaigns</span>
      </a>
    </li>
  </ul>
  <p class="num-foot">Audience demographics and engagement rates come with the rate card — <a href="contact.html">request it</a>.</p>
  </div>
</section>

<section class="section">
  <p class="eyebrow"><span class="badge-dot" aria-hidden="true"></span>Services</p>
  <div class="section-head">
    <h2 class="section-title">Ways to work <em>together</em></h2>
    <p class="section-intro">Clear scopes, styling direction in-house on every booking.</p>
  </div>
  <ul class="svc-grid">
    <li>
      <h3>Campaign &amp; TVC</h3>
      <p>Brand campaigns, commercials and lookbooks — print or motion.</p>
      <span class="svc-note">Day or project rate</span>
      <a class="svc-link" href="contact.html">Enquire<span class="btn-arr" aria-hidden="true">→</span></a>
    </li>
    <li>
      <h3>Runway &amp; events</h3>
      <p>Fashion weeks, designer showcases, show opening — choreography available.</p>
      <span class="svc-note">Per show · Season bookings</span>
      <a class="svc-link" href="contact.html">Enquire<span class="btn-arr" aria-hidden="true">→</span></a>
    </li>
    <li>
      <h3>Editorial &amp; styling</h3>
      <p>Magazine and brand editorials; styling credit on request, as with Merlot.</p>
      <span class="svc-note">Half-day minimum</span>
      <a class="svc-link" href="contact.html">Enquire<span class="btn-arr" aria-hidden="true">→</span></a>
    </li>
    <li>
      <h3>Bridal</h3>
      <p>Bridal and semi-bridal campaigns through the wedding season.</p>
      <span class="svc-note">Books early — enquire ahead</span>
      <a class="svc-link" href="contact.html">Enquire<span class="btn-arr" aria-hidden="true">→</span></a>
    </li>
  </ul>
</section>

''' + brand_wall() + '''

<section class="section section-tan">
  <div class="section-inner">
  <p class="eyebrow"><span class="badge-dot" aria-hidden="true"></span>Brand stories</p>
  <div class="section-head">
    <h2 class="section-title">When brands hand over the <em>camera</em></h2>
    <p class="section-intro">Real briefs, and what came back.</p>
  </div>
  <div class="story">
    <figure class="story-img" data-parallax><img src="assets/img/story-rise.jpg" alt="RISE Winter Collection 24 — blue graffiti set" loading="lazy"><figcaption class="card-badge">Campaign</figcaption></figure>
    <div class="story-copy">
      <h3>RISE — season after season</h3>
      <p>Street-cast Dhaka energy for the Fall ’25 collection, a studio graffiti set for Winter ’24 — the same face carrying a brand across seasons.</p>
      <p class="story-stat">Fall ’25 &amp; Winter ’24 collections</p>
    </div>
  </div>
  <div class="story story-flip">
    <figure class="story-img story-img-tall" data-parallax><img src="assets/img/story-bridal.jpg" alt="Heritage bridal portrait in gold and green" loading="lazy"><figcaption class="card-badge">Bridal</figcaption></figure>
    <div class="story-copy">
      <h3>Bridal — the season that books first</h3>
      <p>Heritage bridal and jewellery campaigns through the wedding season — couture detail, camera-first lighting, and a calendar that fills up months ahead.</p>
      <p class="story-stat">Bridal &amp; jewellery campaigns</p>
    </div>
  </div>
  </div>
</section>

<section class="section">
  <div class="cta-band">
    <p>Rates, usage and deliverables — all in one <em>card.</em></p>
    <a class="btn btn-solid" href="contact.html">Request the rate card<span class="btn-arr" aria-hidden="true">→</span></a>
  </div>
</section>'''

# ───────────────────────── PRESS ─────────────────────────
press = page_hero("Press", 'In the <em>press</em>',
  "Features and interviews from Bangladesh's national media.") + '''

<section class="section">
  <ul class="press-list">
    <li>
      <a href="https://en.shampratikdeshkal.com/print/211023706" target="_blank" rel="noopener">
        <span class="press-source">Shampratik Deshkal · 2021</span>
        <span class="press-headline">“I think I will do experimental work with myself”</span>
      </a>
    </li>
    <li>
      <a href="https://www.tbsnews.net/splash/studio-maestros-releases-new-song-e-shohore-tumihin-563078" target="_blank" rel="noopener">
        <span class="press-source">The Business Standard</span>
        <span class="press-headline">Riba stars in — and co-directs — “E Shohore Tumihin”</span>
      </a>
    </li>
    <li>
      <a href="https://www.thedailystar.net/life-living/fashion-beauty/news/merlot-giving-comfort-clothing-chic-twist-3122266" target="_blank" rel="noopener">
        <span class="press-source">The Daily Star</span>
        <span class="press-headline">Merlot: giving comfort clothing a chic twist</span>
      </a>
    </li>
    <li>
      <a href="https://bdnews24.com/media-en/image/0dbafff21e35" target="_blank" rel="noopener">
        <span class="press-source">bdnews24</span>
        <span class="press-headline">At the bdnews24 19th anniversary celebration</span>
      </a>
    </li>
  </ul>

  <blockquote class="pull-quote">
    <p>“I think I will do <em>experimental</em> work with myself.”</p>
    <cite>— Riba, in conversation with Shampratik Deshkal</cite>
  </blockquote>
</section>

<section class="section">
  <div class="cta-band">
    <p>Writing a story? Press enquiries get a fast <em>reply.</em></p>
    <a class="btn btn-solid" href="contact.html">Contact for press<span class="btn-arr" aria-hidden="true">→</span></a>
  </div>
</section>'''

# ───────────────────────── CONTACT ─────────────────────────
contact = page_hero("Booking", 'Let&rsquo;s make something <em>iconic</em>',
  "Campaigns, runway, editorials, bridal — and styling or direction work. Serious briefs get a reply within 48 hours.") + '''

<section class="section">
  <div class="booking-grid">
    <div class="booking-copy">
      <ul class="booking-channels">
        <!-- TODO: replace with Riba's real booking email & WhatsApp number -->
        <li><a href="mailto:booking@sabrinazamanriba.com">booking@sabrinazamanriba.com</a></li>
        <li><a href="https://wa.me/8801XXXXXXXXX" target="_blank" rel="noopener">WhatsApp</a></li>
        <li><a href="https://www.instagram.com/sabrinazamanribaauthentic/" target="_blank" rel="noopener">Instagram</a></li>
        <li><a href="https://www.facebook.com/sabrinaribaofficial" target="_blank" rel="noopener">Facebook</a></li>
        <li><a href="https://www.youtube.com/@sabrinazamanriba" target="_blank" rel="noopener">YouTube</a></li>
      </ul>
    </div>
    <form class="booking-form" id="bookingForm">
      <label>Your name
        <input type="text" name="name" id="f-name" autocomplete="name" required>
      </label>
      <label>Brand or organisation
        <input type="text" name="brand" id="f-brand" autocomplete="organization">
      </label>
      <label>What kind of work
        <select name="type" id="f-type">
          <option>Campaign / TVC</option>
          <option>Runway / event</option>
          <option>Editorial / styling</option>
          <option>Bridal</option>
          <option>Direction / choreography</option>
        </select>
      </label>
      <label>About the project
        <textarea name="message" id="f-message" rows="4" required></textarea>
      </label>
      <button class="btn btn-solid" type="submit">Send enquiry<span class="btn-arr" aria-hidden="true">→</span></button>
      <p class="form-note">Opens your email app with the enquiry pre-filled.</p>
    </form>
  </div>
</section>

<section class="section section-tan">
  <div class="section-inner">
  <p class="eyebrow"><span class="badge-dot" aria-hidden="true"></span>Process</p>
  <div class="section-head">
    <h2 class="section-title">How a booking <em>works</em></h2>
    <p class="section-intro">Three steps from first email to launch day.</p>
  </div>
  <ol class="steps">
    <li>
      <span class="step-no">01 · Day 1–2</span>
      <h3>Brief &amp; fit</h3>
      <p>Share the brand, dates and mood. You'll get availability and a fit read within 48 hours.</p>
    </li>
    <li>
      <span class="step-no">02 · Shoot week</span>
      <h3>Fitting &amp; shoot day</h3>
      <p>Fittings ahead of time; on set, styling and choreography input included where the brief wants it.</p>
    </li>
    <li>
      <span class="step-no">03 · Launch</span>
      <h3>Delivery &amp; press</h3>
      <p>Approvals on selects, tags and credits coordinated — press-ready the day the campaign breaks.</p>
    </li>
  </ol>
  </div>
</section>

<section class="section">
  <p class="eyebrow"><span class="badge-dot" aria-hidden="true"></span>FAQ</p>
  <div class="section-head">
    <h2 class="section-title">Questions, <em>answered</em></h2>
    <p class="section-intro">What brands ask before the first booking.</p>
  </div>
  <div class="faq-list">
    <details>
      <summary>How far ahead should we book?</summary>
      <p>Campaigns and editorials: two weeks is comfortable. Bridal season and fashion weeks book out earlier — enquire a month ahead.</p>
    </details>
    <details>
      <summary>Do you travel for shoots?</summary>
      <p>Yes — recent work includes an international shoot in Kolkata, and the current fashion film is headed to Europe. Travel and stay on the client.</p>
    </details>
    <details>
      <summary>Is styling included?</summary>
      <p>Styling direction is available on any booking; a full styling credit (as with Merlot) is scoped separately in the brief.</p>
    </details>
    <details>
      <summary>Do you choreograph shows you're not walking in?</summary>
      <p>Yes. Show choreography and ramp direction can be booked on their own.</p>
    </details>
    <details>
      <summary>How do payments work?</summary>
      <p>Advance on confirmation, balance on delivery. Rate card and terms come with the first reply.</p>
    </details>
  </div>
</section>'''

# ───────────────────────── 404 ─────────────────────────
notfound = '''
<section class="page-hero" style="min-height:55vh">
  <p class="eyebrow"><span class="badge-dot" aria-hidden="true"></span>404</p>
  <h1 class="page-title" data-split>Off the <em>runway</em></h1>
  <p class="page-intro">This page doesn't exist — but the work does.</p>
  <div class="hero-actions" style="margin-top:28px">
    <a class="btn btn-solid" href="index.html">Back home<span class="btn-arr" aria-hidden="true">→</span></a>
    <a class="btn btn-line" href="work.html">View the work</a>
  </div>
</section>'''

pages = {
 'about.html':   ('About — Sabrina Zaman Riba', "Who Riba is — a decade on Bangladesh's runways, now also styling, choreographing and directing.", 'about.html', about),
 'work.html':    ('Work — Sabrina Zaman Riba', 'Selected runway, editorial, bridal and campaign work by Sabrina Zaman Riba.', 'work.html', work),
 'media-kit.html':('Media kit — Sabrina Zaman Riba', 'Audience numbers, platforms and ways to work with Sabrina Zaman Riba.', 'media-kit.html', mediakit),
 'press.html':   ('Press — Sabrina Zaman Riba', 'Features and interviews — The Daily Star, The Business Standard, Shampratik Deshkal, bdnews24.', 'press.html', press),
 'contact.html': ('Booking — Sabrina Zaman Riba', 'Book Sabrina Zaman Riba for campaigns, runway, editorials, bridal, styling and direction.', 'contact.html', contact),
 '404.html':     ('Page not found — Sabrina Zaman Riba', 'This page does not exist.', '', notfound),
}
def write_all():
  for fn,(t,d,cur,content) in pages.items():
    open(fn,'w').write(shell(t,d,cur,content))
    print('wrote', fn)

if __name__ == '__main__':
  write_all()

