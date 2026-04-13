/**
 * Hero Carousel — "Top Picks"
 * 4-card rotating carousel, auto-advances every 6 seconds
 * Manually navigable via dots and arrows
 */

(function() {
  let currentSlide = 0;
  let autoPlayTimer = null;
  const AUTO_PLAY_INTERVAL = 6000; // 6 seconds

  function getCarousel() {
    return document.querySelector('.hero-carousel');
  }

  function getTracks() {
    return document.querySelectorAll('.carousel-track');
  }

  function getDots() {
    return document.querySelectorAll('.carousel-dot');
  }

  function showSlide(index) {
    const carousel = getCarousel();
    if (!carousel) return;

    const slides = carousel.querySelectorAll('.carousel-slide');
    if (slides.length === 0) return;

    // Wrap around
    currentSlide = (index + slides.length) % slides.length;

    // Update slides visibility
    slides.forEach((slide, i) => {
      slide.classList.toggle('active', i === currentSlide);
    });

    // Update dots
    getDots().forEach((dot, i) => {
      dot.classList.toggle('active', i === currentSlide);
    });

    // Update aria-live for accessibility
    const activeSlide = slides[currentSlide];
    if (activeSlide) {
      const title = activeSlide.querySelector('h3')?.textContent || '';
      const liveRegion = carousel.querySelector('[aria-live]');
      if (liveRegion) {
        liveRegion.textContent = `Showing slide ${currentSlide + 1} of ${slides.length}: ${title}`;
      }
    }
  }

  function nextSlide() {
    showSlide(currentSlide + 1);
    resetAutoPlay();
  }

  function prevSlide() {
    showSlide(currentSlide - 1);
    resetAutoPlay();
  }

  function autoPlay() {
    nextSlide();
  }

  function startAutoPlay() {
    if (autoPlayTimer) clearInterval(autoPlayTimer);
    autoPlayTimer = setInterval(autoPlay, AUTO_PLAY_INTERVAL);
  }

  function resetAutoPlay() {
    if (autoPlayTimer) clearInterval(autoPlayTimer);
    startAutoPlay();
  }

  function pauseAutoPlay() {
    if (autoPlayTimer) clearInterval(autoPlayTimer);
  }

  function init() {
    const carousel = getCarousel();
    if (!carousel) return;

    // Next/prev buttons
    const nextBtn = carousel.querySelector('.carousel-next');
    const prevBtn = carousel.querySelector('.carousel-prev');
    if (nextBtn) nextBtn.addEventListener('click', nextSlide);
    if (prevBtn) prevBtn.addEventListener('click', prevSlide);

    // Dot navigation
    getDots().forEach((dot, index) => {
      dot.addEventListener('click', () => {
        showSlide(index);
        resetAutoPlay();
      });
    });

    // Pause on hover
    carousel.addEventListener('mouseenter', pauseAutoPlay);
    carousel.addEventListener('mouseleave', startAutoPlay);

    // Pause on focus (for keyboard navigation)
    carousel.addEventListener('focusin', pauseAutoPlay);
    carousel.addEventListener('focusout', startAutoPlay);

    // Keyboard navigation
    carousel.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') nextSlide();
      if (e.key === 'ArrowLeft') prevSlide();
    });

    // Initialize
    showSlide(0);
    startAutoPlay();
  }

  // Initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose for testing
  window.carouselControl = {
    next: nextSlide,
    prev: prevSlide,
    show: showSlide,
    pause: pauseAutoPlay,
    play: startAutoPlay
  };
})();
