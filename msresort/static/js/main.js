(function () {
  'use strict';

  /* Mobile navigation */
  const hamburger = document.getElementById('hamburger');
  const navMenu = document.getElementById('navMenu');

  if (hamburger && navMenu) {
    hamburger.addEventListener('click', function () {
      hamburger.classList.toggle('active');
      navMenu.classList.toggle('active');
    });

    navMenu.querySelectorAll('.navbar__link').forEach(function (link) {
      link.addEventListener('click', function () {
        hamburger.classList.remove('active');
        navMenu.classList.remove('active');
      });
    });
  }

  /* Navbar background on scroll */
  const navbar = document.getElementById('navbar');
  if (navbar) {
    window.addEventListener('scroll', function () {
      navbar.style.background = window.scrollY > 60 ? 'rgba(10,10,10,0.85)' : '';
    }, { passive: true });
  }

  /* Ensure background videos play (some mobile browsers block autoplay without this) */
  document.querySelectorAll('video[autoplay]').forEach(function (video) {
    video.play().catch(function () {});
  });

  /* Restaurant / bar menu toggle */
  window.showMenu = function (type, btn) {
    const slider = document.querySelector('.slider');
    const restaurantMenu = document.getElementById('restaurantMenu');
    const barMenu = document.getElementById('barMenu');

    if (!restaurantMenu || !barMenu) return;

    if (slider) {
      slider.style.transform = type === 'bar' ? 'translateX(100%)' : 'translateX(0)';
    }

    restaurantMenu.style.display = type === 'restaurant' ? 'grid' : 'none';
    barMenu.style.display = type === 'bar' ? 'grid' : 'none';

    document.querySelectorAll('.toggle-btn').forEach(function (b) {
      b.classList.remove('active');
    });
    if (btn) btn.classList.add('active');
  };

  /* Reviews auto-scroll */
  const reviewsSlider = document.querySelector('.reviews-slider');
  if (reviewsSlider && reviewsSlider.children.length > 1) {
    setInterval(function () {
      const card = reviewsSlider.querySelector('.review-card');
      const step = card ? card.offsetWidth + 30 : 320;
      const maxScroll = reviewsSlider.scrollWidth - reviewsSlider.clientWidth;
      if (reviewsSlider.scrollLeft >= maxScroll - 10) {
        reviewsSlider.scrollTo({ left: 0, behavior: 'smooth' });
      } else {
        reviewsSlider.scrollBy({ left: step, behavior: 'smooth' });
      }
    }, 4000);
  }
})();
