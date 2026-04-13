/**
 * Theme Switcher — Light/Dark Mode
 * Default: LIGHT (opposite to TSI-UK)
 * Auto-detects browser preference, user can toggle
 */

(function() {
  const THEME_STORAGE_KEY = 'lnl-theme-preference';
  const LIGHT = 'light';
  const DARK = 'dark';

  // Get user's theme preference or system preference
  function getInitialTheme() {
    const stored = localStorage.getItem(THEME_STORAGE_KEY);
    if (stored) return stored;

    // Check system preference
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return DARK;
    }

    return LIGHT;
  }

  // Apply theme to DOM and CSS custom properties
  function applyTheme(theme) {
    const root = document.documentElement;
    root.setAttribute('data-theme', theme);

    if (theme === DARK) {
      root.style.setProperty('--color-bg', '#1a1a1a');
      root.style.setProperty('--color-text', '#fafafa');
      root.style.setProperty('--color-text-secondary', '#aaaaaa');
      root.style.setProperty('--color-border', '#333333');
      root.style.setProperty('--color-card-bg', '#262626');
      root.style.setProperty('--color-input-bg', '#1a1a1a');
    } else {
      root.style.setProperty('--color-bg', 'var(--color-light)');
      root.style.setProperty('--color-text', 'var(--color-dark)');
      root.style.setProperty('--color-text-secondary', '#666666');
      root.style.setProperty('--color-border', '#e0e0e0');
      root.style.setProperty('--color-card-bg', '#ffffff');
      root.style.setProperty('--color-input-bg', '#ffffff');
    }

    localStorage.setItem(THEME_STORAGE_KEY, theme);
  }

  // Toggle theme and update toggle button
  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const newTheme = current === DARK ? LIGHT : DARK;
    applyTheme(newTheme);
    updateToggleButton(newTheme);
  }

  function updateToggleButton(theme) {
    const btn = document.getElementById('theme-toggle-btn');
    if (!btn) return;

    const icon = btn.querySelector('svg');
    if (theme === DARK) {
      btn.setAttribute('aria-label', 'Switch to light mode');
      if (icon) icon.innerHTML = '☀️'; // Sun icon for light mode
    } else {
      btn.setAttribute('aria-label', 'Switch to dark mode');
      if (icon) icon.innerHTML = '🌙'; // Moon icon for dark mode
    }
  }

  // Initialize on page load
  window.addEventListener('DOMContentLoaded', function() {
    const initialTheme = getInitialTheme();
    applyTheme(initialTheme);
    updateToggleButton(initialTheme);

    // Attach toggle listener
    const themeToggle = document.getElementById('theme-toggle-btn');
    if (themeToggle) {
      themeToggle.addEventListener('click', toggleTheme);
    }
  });

  // Expose functions globally
  window.toggleTheme = toggleTheme;
})();
