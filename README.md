# Sabrina Zaman Riba — Portfolio

Static portfolio site for model, stylist & creative director **Sabrina Zaman Riba** (Dhaka, Bangladesh).

Built by [The YOLO Studio](https://theyolostudio.com).

## Stack

- Plain HTML / CSS / JS — **no build step**
- Fonts: Bodoni Moda · Archivo · Tiro Bangla (Google Fonts)
- Deploys anywhere that serves static files (Cloudflare Pages, Hostinger, Netlify…)

## Structure

```
index.html
assets/
  css/style.css
  js/main.js
  img/            ← drop real photos here
    hero.jpg      (4:5 full-length portrait)
    work/
      runway-01.jpg, runway-02.jpg
      editorial-01.jpg, editorial-02.jpg
      bridal-01.jpg, bridal-02.jpg
      commercial-01.jpg, motion-01.jpg
```

## Replacing the photo placeholders

Every image slot is a `<figure class="ph" data-ph="…">`. To use a real photo, replace the figure with:

```html
<figure class="work-frame">
  <img src="assets/img/work/runway-01.jpg" alt="Riba on the runway, Dhaka" loading="lazy">
</figure>
```

(Keep `work-frame` / `hero-portrait` classes for sizing. Add `object-fit:cover; width:100%; height:100%` images inherit it via the frame.)

## Before launch (TODO)

- [ ] Real photos in `assets/img/` (get photographer permissions for editorial shots)
- [ ] Real booking email — currently `booking@sabrinazamanriba.com` placeholder (in `index.html` **and** `assets/js/main.js`)
- [ ] Real WhatsApp number — `https://wa.me/8801XXXXXXXXX` placeholder
- [ ] Confirm comp-card measurements with Riba
- [ ] Showreel video section (optional, phase 2)
- [ ] Custom domain + OG image

## Deploy — Cloudflare Pages

Dashboard → **Workers & Pages → Create → Pages → Connect to Git** → pick this repo →
Framework preset: **None** · Build command: *(empty)* · Output directory: `/`

Every push to `main` auto-deploys. Temporary URL: `<project>.pages.dev`.
