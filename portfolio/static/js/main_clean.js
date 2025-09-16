/**
* Template Name: iPortfolio
* Template URL: https://bootstrapmade.com/iportfolio-bootstrap-portfolio-websites-template/
* Updated: Jun 29 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  // Header toggle functionality
  const headerToggleBtn = document.querySelector('.header-toggle');
  
  if (headerToggleBtn) {
    function headerToggle() {
      const header = document.querySelector('#header');
      if (header) {
        header.classList.toggle('header-show');
        headerToggleBtn.classList.toggle('bi-list');
        headerToggleBtn.classList.toggle('bi-x');
      }
    }
    
    headerToggleBtn.addEventListener('click', headerToggle);

    // Close mobile menu when clicking on nav links
    document.querySelectorAll('#navmenu a').forEach(navLink => {
      navLink.addEventListener('click', () => {
        if (document.querySelector('.header-show')) {
          headerToggle();
        }
      });
    });
  }

  // Mobile nav dropdowns
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(dropdown => {
    dropdown.addEventListener('click', function(e) {
      e.preventDefault();
      const parent = this.parentNode;
      if (parent) {
        parent.classList.toggle('active');
        if (parent.nextElementSibling) {
          parent.nextElementSibling.classList.toggle('dropdown-active');
        }
      }
      e.stopImmediatePropagation();
    });
  });

  // Remove preloader when page loads
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  // Scroll to top button
  const scrollTop = document.querySelector('.scroll-top');
  if (scrollTop) {
    function toggleScrollTop() {
      if (window.scrollY > 100) {
        scrollTop.classList.add('active');
      } else {
        scrollTop.classList.remove('active');
      }
    }
    
    scrollTop.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });

    window.addEventListener('scroll', toggleScrollTop);
    toggleScrollTop(); // Check on load
  }

  // Initialize AOS (Animate On Scroll)
  if (typeof AOS !== 'undefined') {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }

  // Initialize Typed.js if available
  if (typeof Typed !== 'undefined') {
    const typedElement = document.querySelector('.typed');
    if (typedElement) {
      const typedStrings = typedElement.getAttribute('data-typed-items');
      if (typedStrings) {
        try {
          new Typed('.typed', {
            strings: typedStrings.split(','),
            loop: true,
            typeSpeed: 100,
            backSpeed: 50,
            backDelay: 2000
          });
        } catch (e) {
          console.error('Error initializing Typed.js:', e);
        }
      }
    }
  }

  // Initialize Pure Counter
  if (typeof PureCounter !== 'undefined') {
    new PureCounter();
  }

  // Initialize Waypoint for skills animation
  if (typeof Waypoint !== 'undefined') {
    const skillsSections = document.querySelectorAll('.skills-animation');
    if (skillsSections.length > 0) {
      skillsSections.forEach(section => {
        new Waypoint({
          element: section,
          offset: '80%',
          handler: function() {
            const progressBars = section.querySelectorAll('.progress .progress-bar');
            progressBars.forEach(bar => {
              if (bar.getAttribute('aria-valuenow')) {
                bar.style.width = bar.getAttribute('aria-valuenow') + '%';
              }
            });
          }
        });
      });
    }
  }

  // Initialize GLightbox
  if (typeof GLightbox !== 'undefined') {
    GLightbox({
      selector: '.glightbox'
    });
  }

  // Initialize Isotope for portfolio filtering
  if (typeof Isotope !== 'undefined' && typeof imagesLoaded !== 'undefined') {
    document.querySelectorAll('.isotope-layout').forEach(container => {
      const layout = container.getAttribute('data-layout') || 'masonry';
      const filter = container.getAttribute('data-default-filter') || '*';
      const sort = container.getAttribute('data-sort') || 'original-order';
      const isotopeContainer = container.querySelector('.isotope-container');

      if (isotopeContainer) {
        imagesLoaded(isotopeContainer, function() {
          const iso = new Isotope(isotopeContainer, {
            itemSelector: '.isotope-item',
            layoutMode: layout,
            filter: filter,
            sortBy: sort
          });

          // Filter items on button click
          const filterButtons = container.querySelectorAll('.isotope-filters li');
          if (filterButtons.length > 0) {
            filterButtons.forEach(button => {
              button.addEventListener('click', function() {
                const activeButton = container.querySelector('.isotope-filters .filter-active');
                if (activeButton) {
                  activeButton.classList.remove('filter-active');
                }
                this.classList.add('filter-active');
                
                const filterValue = this.getAttribute('data-filter') || '*';
                iso.arrange({ filter: filterValue });
                
                // Refresh AOS after filtering
                if (typeof AOS !== 'undefined') {
                  AOS.refresh();
                }
              });
            });
          }
        });
      }
    });
  }

  // Initialize Swiper sliders
  if (typeof Swiper !== 'undefined') {
    function initSwipers() {
      document.querySelectorAll('.init-swiper').forEach(swiperEl => {
        const configEl = swiperEl.querySelector('.swiper-config');
        if (configEl) {
          try {
            const config = JSON.parse(configEl.textContent.trim());
            if (swiperEl.classList.contains('swiper-tab')) {
              if (typeof initSwiperWithCustomPagination === 'function') {
                initSwiperWithCustomPagination(swiperEl, config);
              } else {
                new Swiper(swiperEl, config);
              }
            } else {
              new Swiper(swiperEl, config);
            }
          } catch (e) {
            console.error('Error initializing Swiper:', e);
          }
        }
      });
    }

    // Initialize after DOM is fully loaded
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initSwipers);
    } else {
      initSwipers();
    }
  }

  // Handle hash-based navigation
  function handleHashNavigation() {
    if (window.location.hash) {
      const target = document.querySelector(window.location.hash);
      if (target) {
        setTimeout(() => {
          const scrollMargin = parseInt(getComputedStyle(target).scrollMarginTop) || 0;
          window.scrollTo({
            top: target.offsetTop - scrollMargin,
            behavior: 'smooth'
          });
        }, 100);
      }
    }
  }

  // Handle initial page load with hash
  window.addEventListener('load', handleHashNavigation);
  
  // Handle browser back/forward navigation
  window.addEventListener('popstate', handleHashNavigation);

  // Navigation menu scrollspy
  function setupScrollspy() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section[id]');
    
    if (navLinks.length === 0 || sections.length === 0) return;
    
    function updateActiveNav() {
      let currentSection = '';
      
      sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        const sectionHeight = section.offsetHeight;
        
        if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
          currentSection = section.getAttribute('id');
        }
      });
      
      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${currentSection}`) {
          link.classList.add('active');
        }
      });
    }
    
    window.addEventListener('scroll', updateActiveNav);
    updateActiveNav(); // Run once on load
  }
  
  // Initialize scrollspy after page load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupScrollspy);
  } else {
    setupScrollspy();
  }

})();
