/**
 * Hero Carousel — "Top Picks"
 * Sliding track: shows 3 cards on desktop, 2 on tablet, 1 on mobile.
 * Auto-advances by one card every 5 seconds, wraps around.
 */

(function() {
  let currentIndex = 0;
  let autoPlayTimer = null;
  const AUTO_PLAY_INTERVAL = 5000; // 5 seconds

  function getCarousel() {
    return document.querySelector('.hero-carousel');
  }

  function getTrack() {
    return document.querySelector('.carousel-track');
  }

  function getSlides() {
    return document.querySelectorAll('.carousel-slide');
  }

  function getDots() {
    return document.querySelectorAll('.carousel-dot');
  }

  /**
   * Number of cards visible at once based on viewport.
   * Mirrors the CSS breakpoints in style.css `.carousel-slide` rules.
   */
  function getVisibleCount() {
    const w = window.innerWidth;
    if (w <= 768) return 1;
    if (w <= 1024) return 2;
    return 3;
  }

  /**
   * Number of valid starting positions for the track.
   * With 5 slides and 3 visible, you can start at indices 0, 1, 2 (3 stops).
   * We allow wrap-around past that — once index > total - visible, jump back to 0.
   */
  function getMaxIndex() {
    return getSlides().length - 1; // we wrap at total slides for even cycling
  }

  function showIndex(index) {
    const track = getTrack();
    const slides = getSlides();
    if (!track || slides.length === 0) return;

    const total = slides.length;
    const visible = getVisibleCount();
    const lastValidStart = Math.max(0, total - visible);

    // Wrap: if we'd run past the last valid start, snap back to 0
    if (index > lastValidStart) {
      currentIndex = 0;
    } else if (index < 0) {
      currentIndex = lastValidStart;
    } else {
      currentIndex = index;
    }

    // Calculate translation: one card width + gap
    const firstSlide = slides[0];
    const slideWidth = firstSlide.getBoundingClientRect().width;
    const gap = parseFloat(getComputedStyle(track).gap) || 0;
    const offset = (slideWidth + gap) * currentIndex;

    track.style.transform = `translateX(-${offset}px)`;

    // Update dots
    getDots().forEach((dot, i) => {
      dot.classList.toggle('active', i === currentIndex);
    });

    // Update aria-live
    const carousel = getCarousel();
    if (carousel) {
      const liveRegion = carousel.querySelector('[aria-live]');
      if (liveRegion) {
        const visibleEnd = Math.min(currentIndex + visible, total);
        liveRegion.textContent =
          `Showing slides ${currentIndex + 1} to ${visibleEnd} of ${total}`;
      }
    }
  }

  function nextSlide() {
    showIndex(currentIndex + 1);
    resetAutoPlay();
  }

  function prevSlide() {
    showIndex(currentIndex - 1);
    resetAutoPlay();
  }

  function autoPlay() {
    showIndex(currentIndex + 1);
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

    // Next/prev
    const nextBtn = carousel.querySelector('.carousel-next');
    const prevBtn = carousel.querySelector('.carousel-prev');
    if (nextBtn) nextBtn.addEventListener('click', nextSlide);
    if (prevBtn) prevBtn.addEventListener('click', prevSlide);

    // Dots
    getDots().forEach((dot, index) => {
      dot.addEventListener('click', () => {
        showIndex(index);
        resetAutoPlay();
      });
    });

    // Pause on hover/focus
    carousel.addEventListener('mouseenter', pauseAutoPlay);
    carousel.addEventListener('mouseleave', startAutoPlay);
    carousel.addEventListener('focusin', pauseAutoPlay);
    carousel.addEventListener('focusout', startAutoPlay);

    // Keyboard
    carousel.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') nextSlide();
      if (e.key === 'ArrowLeft') prevSlide();
    });

    // Recalculate offsets on resize (slide width changes)
    let resizeTimer;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => showIndex(currentIndex), 150);
    });

    // Initial render
    showIndex(0);
    startAutoPlay();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose for debugging
  window.carouselControl = {
    next: nextSlide,
    prev: prevSlide,
    show: showIndex,
    pause: pauseAutoPlay,
    play: startAutoPlay
  };
})();
