// Project Configuration
window.projectConfig = {
    name: 'HirawatTech',
    type: '',
    settings: {
        colors: {
            primary: '#2563EB',
            secondary: '#1E40AF',
            accent: ''
        },
        fonts: {
            primary: 'Inter',
            secondary: 'Inter'
        }
    }
};

// Mobile menu functionality
document.addEventListener('DOMContentLoaded', function () {
    initializeMobileMenu();
    initializeHeroSection();
});

function initializeMobileMenu() {
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const hamburgerIcon = document.getElementById('hamburger-icon');
    const closeIcon = document.getElementById('close-icon');

    mobileMenuButton.addEventListener('click', function () {
        const isExpanded = mobileMenuButton.getAttribute('aria-expanded') === 'true';
        toggleMobileMenu(!isExpanded);
    });

    // Close mobile menu when clicking on a link
    const mobileLinks = mobileMenu.querySelectorAll('a');
    mobileLinks.forEach(link => {
        link.addEventListener('click', () => toggleMobileMenu(false));
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function (event) {
        if (!mobileMenuButton.contains(event.target) && !mobileMenu.contains(event.target)) {
            toggleMobileMenu(false);
        }
    });

    // Close mobile menu on escape key
    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
            toggleMobileMenu(false);
        }
    });

    function toggleMobileMenu(show) {
        mobileMenu.classList.toggle('hidden', !show);
        hamburgerIcon.classList.toggle('hidden', show);
        closeIcon.classList.toggle('hidden', !show);
        mobileMenuButton.setAttribute('aria-expanded', show);
    }
}

function initializeHeroSection() {
    // Smooth scroll for CTA buttons
    const ctaButtons = document.querySelectorAll('#hero button');
    ctaButtons.forEach(button => {
        button.addEventListener('click', function () {
            const target = this.textContent.includes('View Our Work') ? '#portfolio' : '#contact';
            document.querySelector(target)?.scrollIntoView({ behavior: 'smooth' });
        });
    });

    // Parallax effect for background
    window.addEventListener('scroll', function () {
        const scrolled = window.pageYOffset;
        const heroSection = document.querySelector('#hero');
        const backgroundImage = heroSection.querySelector('img');

        if (backgroundImage && scrolled < heroSection.offsetHeight) {
            backgroundImage.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
    });

    // Intersection Observer for animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
            }
        });
    }, observerOptions);

    // Observe hero elements
    const heroElements = document.querySelectorAll('#hero h1, #hero p, #hero .grid > div');
    heroElements.forEach(el => observer.observe(el));
}