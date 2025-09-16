// Initialize AOS (Animate On Scroll)
function initAOS() {
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            once: true
        });
    }
}

// Load non-critical scripts
document.addEventListener('DOMContentLoaded', function() {
    // Initialize AOS
    initAOS();
    
    // Load validation script only if there's a form on the page
    if (document.querySelector('form')) {
        var validateScript = document.createElement('script');
        validateScript.src = "/static/vendor/php-email-form/validate.js";
        validateScript.defer = true;
        document.body.appendChild(validateScript);
    }
    
    // Load lightbox only if there are images with data-gallery attribute
    if (document.querySelector('[data-gallery]')) {
        var lightboxScript = document.createElement('script');
        lightboxScript.src = "/static/vendor/glightbox/js/glightbox.min.js";
        lightboxScript.defer = true;
        lightboxScript.onload = function() {
            // Initialize GLightbox after it's loaded
            if (typeof GLightbox !== 'undefined') {
                GLightbox({
                    selector: '[data-gallery]'
                });
            }
        };
        document.body.appendChild(lightboxScript);
    }
});
