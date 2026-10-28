const tabs = [...document.querySelectorAll('.viz-tab')];
const dashboardFrame = document.querySelector('#dashboard-frame');
const storyFrame = document.querySelector('#story-frame');
const nav = document.querySelector('#site-nav');
const menuToggle = document.querySelector('.menu-toggle');

function showView(name) {
  const storySelected = name === 'story';
  dashboardFrame.classList.toggle('is-hidden', storySelected);
  storyFrame.classList.toggle('is-hidden', !storySelected);
  storyFrame.setAttribute('aria-hidden', String(!storySelected));
  tabs.forEach((tab) => {
    const active = tab.dataset.view === name;
    tab.classList.toggle('is-active', active);
    tab.setAttribute('aria-pressed', String(active));
  });
  const storyIframe = storyFrame.querySelector('iframe');
  if (storySelected && !storyIframe.src) storyIframe.src = storyIframe.dataset.src;
}

tabs.forEach((tab) => tab.addEventListener('click', () => showView(tab.dataset.view)));
document.querySelector('[data-open-story]').addEventListener('click', () => showView('story'));
menuToggle.addEventListener('click', () => {
  const open = menuToggle.getAttribute('aria-expanded') !== 'true';
  menuToggle.setAttribute('aria-expanded', String(open));
  nav.classList.toggle('is-open', open);
});
nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
  nav.classList.remove('is-open');
  menuToggle.setAttribute('aria-expanded', 'false');
}));
