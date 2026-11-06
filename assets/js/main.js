// Sabrina Zaman Riba — site behaviour

// Current year
document.getElementById('year').textContent = new Date().getFullYear();

// Mobile nav
const navToggle = document.getElementById('navToggle');
const siteNav = document.getElementById('siteNav');
navToggle.addEventListener('click', () => {
  const open = siteNav.classList.toggle('is-open');
  navToggle.setAttribute('aria-expanded', String(open));
});
siteNav.addEventListener('click', (e) => {
  if (e.target.tagName === 'A') {
    siteNav.classList.remove('is-open');
    navToggle.setAttribute('aria-expanded', 'false');
  }
});

// Work filters
const filters = document.querySelectorAll('.filter');
const items = document.querySelectorAll('.work-item');
const empty = document.getElementById('workEmpty');

filters.forEach((btn) => {
  btn.addEventListener('click', () => {
    filters.forEach((b) => b.classList.remove('is-active'));
    btn.classList.add('is-active');
    const cat = btn.dataset.filter;
    let shown = 0;
    items.forEach((item) => {
      const show = cat === 'all' || item.dataset.cat === cat;
      item.hidden = !show;
      if (show) shown++;
    });
    empty.hidden = shown > 0;
  });
});

// Booking form → opens mail app with a composed enquiry
const form = document.getElementById('bookingForm');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const data = new FormData(form);
  const subject = encodeURIComponent(
    `Booking enquiry — ${data.get('type')} (${data.get('brand') || data.get('name')})`
  );
  const body = encodeURIComponent(
    `Name: ${data.get('name')}\nBrand: ${data.get('brand') || '—'}\nWork type: ${data.get('type')}\n\n${data.get('message')}`
  );
  // TODO: replace with Riba's real booking address
  window.location.href = `mailto:booking@sabrinazamanriba.com?subject=${subject}&body=${body}`;
});
