// Project Configuration
window.projectConfig = {
    name: 'HirawatTech',
    settings: {
        colors: { primary: '#2563EB', secondary: '#1E40AF' },
        fonts: { primary: 'Alata', secondary: 'Alata' }
    }
};

document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu elements
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const hamburgerIcon = document.getElementById('hamburger-icon');
    const closeIcon = document.getElementById('close-icon');

    // Toggle mobile menu function
    function toggleMobileMenu(show) {
        mobileMenu.classList.toggle('hidden', !show);
        hamburgerIcon.classList.toggle('hidden', show);
        closeIcon.classList.toggle('hidden', !show);
        mobileMenuButton.setAttribute('aria-expanded', show);
    }

    // Mobile menu event listeners
    mobileMenuButton.addEventListener('click', function() {
        toggleMobileMenu(mobileMenuButton.getAttribute('aria-expanded') !== 'true');
    });
    
    const mobileLinks = mobileMenu.querySelectorAll('a');
    for (let i = 0; i < mobileLinks.length; i++) {
        mobileLinks[i].addEventListener('click', function() { 
            toggleMobileMenu(false);
        });
    }

    // Global click and escape handlers
    document.addEventListener('click', function(e) {
        if (!mobileMenuButton.contains(e.target) && !mobileMenu.contains(e.target)) {
            toggleMobileMenu(false);
        }
    });
    
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') toggleMobileMenu(false);
    });

    // Hero section initialization
    var heroSection = document.querySelector('#hero');
    if (heroSection) {
        // CTA buttons scroll
        var buttons = heroSection.querySelectorAll('button');
        for (var j = 0; j < buttons.length; j++) {
            buttons[j].addEventListener('click', function() {
                var target = this.textContent.includes('View Our Work') ? '#portfolio' : '#contact';
                var element = document.querySelector(target);
                if (element) element.scrollIntoView({ behavior: 'smooth' });
            });
        }

        // Parallax effect
        var backgroundImage = heroSection.querySelector('img');
        if (backgroundImage) {
            window.addEventListener('scroll', function() {
                var scrolled = window.pageYOffset;
                if (scrolled < heroSection.offsetHeight) {
                    backgroundImage.style.transform = 'translateY(' + (scrolled * 0.5) + 'px)';
                }
            });
        }

        // Intersection Observer for animations
        var observer = new IntersectionObserver(function(entries) {
            for (var k = 0; k < entries.length; k++) {
                if (entries[k].isIntersecting) {
                    entries[k].target.classList.add('animate-fade-in');
                }
            }
        }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

        var heroElements = heroSection.querySelectorAll('h1, p, .grid > div');
        for (var l = 0; l < heroElements.length; l++) {
            observer.observe(heroElements[l]);
        }
    }
});