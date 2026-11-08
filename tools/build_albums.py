#!/usr/bin/env python3
"""Generate albums.html + album-<key>.html from data/albums.json.

Images live in assets/img/albums/<key>/NN.jpg (full) and NN-t.jpg (thumb).
To add an album later: drop images in a new folder, add an entry to
data/albums.json, run `python3 tools/build_albums.py`.
"""
import json, os, sys
from PIL import Image

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from build_pages import shell, page_hero  # noqa: E402

data = json.load(open('data/albums.json'))
albums = data['albums']
CATS = data['categories']


def photos(key):
    d = f'assets/img/albums/{key}'
    files = sorted(f for f in os.listdir(d) if f.endswith('.jpg') and not f.endswith('-t.jpg'))
    out = []
    for f in files:
        w, h = Image.open(os.path.join(d, f)).size
        out.append((f'{d}/{f}', f'{d}/{f[:-4]}-t.jpg', w, h))
    return out


# ───────────── index ─────────────
cards = []
for a in albums:
    ph = photos(a['key'])
    cover = ph[a.get('cover', 1) - 1]
    cards.append(f'''    <li class="album-card" data-cat="{a['category'].lower()}">
      <a href="album-{a['key']}.html" class="album-link">
        <figure class="album-cover">
          <img src="{cover[1]}" alt="{a['title']} — album cover" loading="lazy" width="{cover[2]}" height="{cover[3]}">
          <figcaption class="card-badge">{a['category']}</figcaption>
          <span class="album-count">{len(ph)} frames</span>
        </figure>
        <div class="album-meta">
          <h3>{a['title']}</h3>
          <p>{a['blurb']}</p>
        </div>
      </a>
    </li>''')

filters = '<button class="filter is-active" data-filter="all">All</button>\n    ' + '\n    '.join(
    f'<button class="filter" data-filter="{c.lower()}">{c}</button>' for c in CATS)

total_fb = sum(a['fb_count'] for a in albums)
index = page_hero('Albums', 'From the <em>archive</em>',
    f'Fifteen albums picked from her 170 on Facebook — runway, campaigns, couture and press. '
    f'{len(albums)*9} frames here, {total_fb:,}+ in the originals.') + f'''

<section class="section">
  <div class="filters" role="group" aria-label="Filter albums by category">
    {filters}
  </div>
  <ul class="album-grid" id="workGrid">
{chr(10).join(cards)}
  </ul>
  <p class="work-empty" id="workEmpty" hidden>No albums in this category yet.</p>
</section>

<section class="section">
  <div class="cta-band">
    <p>The full archive lives on <em>Facebook.</em></p>
    <a class="btn btn-solid" href="https://www.facebook.com/sabrinazamanribaauthentic/photos_albums" target="_blank" rel="noopener">Browse all 170 albums<span class="btn-arr" aria-hidden="true">→</span></a>
  </div>
</section>'''

open('albums.html', 'w').write(shell('Albums — Sabrina Zaman Riba',
    'Fifteen albums from Sabrina Zaman Riba’s archive — runway, campaigns, couture and press.',
    'albums.html', index, og_img=f"albums/{albums[0]['key']}/01.jpg"))
print('wrote albums.html')

# ───────────── album pages ─────────────
for i, a in enumerate(albums):
    ph = photos(a['key'])
    prev_a = albums[i - 1]
    next_a = albums[(i + 1) % len(albums)]
    tiles = '\n'.join(f'''    <a class="masonry-item glightbox" href="{full}" data-gallery="{a['key']}" data-description="{a['title']} · {n}/{len(ph)}">
      <img src="{thumb}" alt="{a['title']} — frame {n}" loading="lazy" width="{w}" height="{h}">
    </a>''' for n, (full, thumb, w, h) in enumerate(ph, 1))
    title_html = a['title_html'] if 'title_html' in a else a['title']
    content = page_hero(f'Album · {a["category"]}', title_html, a['intro']) + f'''

<section class="section album-section">
  <dl class="album-facts">
    <div><dt>Category</dt><dd>{a['category']}</dd></div>
    <div><dt>Here</dt><dd>{len(ph)} frames</dd></div>
    <div><dt>In the original</dt><dd>{a['fb_count']:,} photos</dd></div>
  </dl>

  <div class="masonry" id="masonry">
{tiles}
  </div>

  <div class="album-actions">
    <a class="btn btn-line" href="https://www.facebook.com/media/set/?set={a['fb_id']}&amp;type=3" target="_blank" rel="noopener">See the full album on Facebook</a>
    <a class="btn btn-solid" href="contact.html">Book a shoot like this<span class="btn-arr" aria-hidden="true">→</span></a>
  </div>
</section>

<nav class="album-pager section" aria-label="More albums">
  <a class="pager-link pager-prev" href="album-{prev_a['key']}.html">
    <span class="pager-dir">← Previous album</span>
    <span class="pager-title">{prev_a['title']}</span>
  </a>
  <a class="pager-link pager-all" href="albums.html">All albums</a>
  <a class="pager-link pager-next" href="album-{next_a['key']}.html">
    <span class="pager-dir">Next album →</span>
    <span class="pager-title">{next_a['title']}</span>
  </a>
</nav>'''
    fn = f"album-{a['key']}.html"
    open(fn, 'w').write(shell(f"{a['title']} — Sabrina Zaman Riba", a['blurb'], 'albums.html', content,
                              og_img=f"albums/{a['key']}/{a.get('cover',1):02d}.jpg"))
    print('wrote', fn)
