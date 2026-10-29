document.addEventListener('DOMContentLoaded', () => {
  const cards = document.querySelectorAll('.info-card');
  const tabs = document.querySelectorAll('.tab');
  const panels = document.querySelectorAll('.panel-content');

  const activatePanel = (key) => {
    panels.forEach((panel) => {
      panel.classList.toggle('active', panel.id === key);
    });

    tabs.forEach((tab) => {
      tab.classList.toggle('active', tab.dataset.panel === key);
    });

    cards.forEach((card) => {
      card.classList.toggle('active', card.dataset.target === key);
    });
  };

  cards.forEach((card) => {
    card.addEventListener('click', () => activatePanel(card.dataset.target));
  });

  tabs.forEach((tab) => {
    tab.addEventListener('click', () => activatePanel(tab.dataset.panel));
  });
});
