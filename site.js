(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#site-nav');
  function closeMenu() {
    toggle?.setAttribute('aria-expanded', 'false');
    nav?.classList.remove('is-open');
  }
  toggle?.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') !== 'true';
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
  });
  nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle?.getAttribute('aria-expanded') === 'true') {
      closeMenu(); toggle.focus();
    }
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.nav-wrap')) closeMenu();
  });
  const contents = [...document.querySelectorAll('.case-toc a[href^="#"]')]
    .map(link => ({ link, section: document.getElementById(link.hash.slice(1)) }))
    .filter(item => item.section);
  if (contents.length) {
    let scheduled = false;
    function updateContents() {
      const offset = document.querySelector('.site-header').offsetHeight + 40;
      let current = contents[0];
      contents.forEach(item => {
        if (item.section.getBoundingClientRect().top <= offset) current = item;
      });
      if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2) {
        current = contents[contents.length - 1];
      }
      contents.forEach(item => {
        if (item === current) item.link.setAttribute('aria-current', 'location');
        else item.link.removeAttribute('aria-current');
      });
      scheduled = false;
    }
    function scheduleContents() {
      if (!scheduled) {
        scheduled = true;
        requestAnimationFrame(updateContents);
      }
    }
    window.addEventListener('scroll', scheduleContents, { passive: true });
    window.addEventListener('resize', scheduleContents);
    updateContents();
  }
  const buttons = document.querySelectorAll('[data-filter]');
  const cards = document.querySelectorAll('.project-card');
  buttons.forEach(button => button.addEventListener('click', () => {
    const filter = button.dataset.filter;
    buttons.forEach(item => {
      item.classList.toggle('active', item === button);
      item.setAttribute('aria-pressed', String(item === button));
    });
    let visible = 0;
    cards.forEach(card => {
      const show = filter === 'all' || card.dataset.category === filter;
      card.hidden = !show;
      if (show) visible++;
    });
    const count = document.querySelector('.project-count');
    if (count) count.textContent = `${visible}개의 프로젝트`;
  }));
})();
