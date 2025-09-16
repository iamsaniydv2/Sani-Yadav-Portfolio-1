// Initialize Typed.js for the typing animation
document.addEventListener('DOMContentLoaded', function() {
  if (typeof Typed !== 'undefined' && document.querySelector('.typed')) {
    try {
      new Typed('.typed', {
        strings: ['Full Stack Python Developer', 'Freelancer', 'Web Designer'],
        typeSpeed: 100,
        backSpeed: 50,
        backDelay: 3000,
        loop: true
      });
    } catch (e) {
      console.error('Error initializing Typed.js:', e);
    }
  }
});
