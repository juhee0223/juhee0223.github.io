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
