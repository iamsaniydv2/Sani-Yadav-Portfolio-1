// Dark Mode Toggle functionality
document.addEventListener('DOMContentLoaded', function() {
  const darkModeToggle = document.getElementById('darkModeToggle');
  if (darkModeToggle) {
    const icon = darkModeToggle.querySelector('i');
    const currentTheme = localStorage.getItem('theme') || 'light';
    
    // Apply saved theme
    if (currentTheme === 'dark') {
      document.body.classList.add('dark-mode');
      if (icon) icon.classList.replace('bi-moon-fill', 'bi-sun-fill');
    }
    
    // Toggle function
    darkModeToggle.onclick = function() {
      if (document.body.classList.contains('dark-mode')) {
        document.body.classList.remove('dark-mode');
        if (icon) icon.classList.replace('bi-sun-fill', 'bi-moon-fill');
        localStorage.setItem('theme', 'light');
      } else {
        document.body.classList.add('dark-mode');
        if (icon) icon.classList.replace('bi-moon-fill', 'bi-sun-fill');
        localStorage.setItem('theme', 'dark');
      }
    };
  }
});
