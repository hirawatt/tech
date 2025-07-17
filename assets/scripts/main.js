// Project Configuration
window.projectConfig = {
    name: 'HirawatTech',
    settings: {
        colors: { primary: '#2563EB', secondary: '#1E40AF' },
        fonts: { primary: 'Alata', secondary: 'Alata' }
    }
};

document.addEventListener('DOMContentLoaded', function () {
    // Animated text rotation
    const animateTextElements = document.querySelectorAll('.animatedText span');
    if (animateTextElements.length > 0) {
        let currentIndex = 0;

        // Show the first text initially
        animateTextElements[0].classList.add('visible');

        // Rotate through texts every 3 seconds
        setInterval(() => {
            // Hide current text
            animateTextElements[currentIndex].classList.remove('visible');

            // Move to next text (loop back to start if at end)
            currentIndex = (currentIndex + 1) % animateTextElements.length;

            // Show next text
            animateTextElements[currentIndex].classList.add('visible');
        }, 3000);
    }

    // Mobile menu elements
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const hamburgerIcon = document.getElementById('hamburger-icon');
    const closeIcon = document.getElementById('close-icon');

    // Toggle mobile menu function
    function toggleMobileMenu(show) {
        if (mobileMenu) {
            mobileMenu.classList.toggle('hidden', !show);
            if (hamburgerIcon) hamburgerIcon.classList.toggle('hidden', show);
            if (closeIcon) closeIcon.classList.toggle('hidden', !show);
            if (mobileMenuButton) mobileMenuButton.setAttribute('aria-expanded', show);
        }
    }

    // Mobile menu event listeners
    if (mobileMenuButton) {
        mobileMenuButton.addEventListener('click', function () {
            toggleMobileMenu(mobileMenuButton.getAttribute('aria-expanded') !== 'true');
        });
    }

    if (mobileMenu) {
        const mobileLinks = mobileMenu.querySelectorAll('a');
        for (let i = 0; i < mobileLinks.length; i++) {
            mobileLinks[i].addEventListener('click', function () {
                toggleMobileMenu(false);
            });
        }
    }

    // Global click and escape handlers
    document.addEventListener('click', function (e) {
        if (!mobileMenuButton.contains(e.target) && !mobileMenu.contains(e.target)) {
            toggleMobileMenu(false);
        }
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') toggleMobileMenu(false);
    });

    // Loading Animation Management
    function initLoadingAnimation() {
        // Hide loading overlay when page is fully loaded
        window.addEventListener('load', function () {
            const loadingOverlay = document.getElementById('loading-overlay');
            if (loadingOverlay) {
                // Add a small delay to ensure all assets are rendered
                setTimeout(function () {
                    loadingOverlay.classList.add('loading-hidden');
                }, 500);
            }
        });

        // Fallback to hide loading screen if it takes too long
        setTimeout(function () {
            const loadingOverlay = document.getElementById('loading-overlay');
            if (loadingOverlay && !loadingOverlay.classList.contains('loading-hidden')) {
                loadingOverlay.classList.add('loading-hidden');
            }
        }, 5000);
    }

    // Mobile Menu Alpine.js Integration
    function initMobileMenu() {
        // Mobile menu implementation using Alpine.js
        if (typeof Alpine !== 'undefined') {
            Alpine.data('mobileMenu', () => ({
                isOpen: false,
                init() {
                    this.$watch('isOpen', value => {
                        document.body.style.overflow = value ? 'hidden' : '';
                    });

                    // Close on escape key
                    window.addEventListener('keydown', e => {
                        if (e.key === 'Escape' && this.isOpen) {
                            this.isOpen = false;
                        }
                    });
                },
                toggle() {
                    this.isOpen = !this.isOpen;
                },
                close() {
                    this.isOpen = false;
                }
            }));
        }
    }

    // Hero Section Animations and Interactions
    function initHeroSection() {
        var heroSection = document.querySelector('#hero');
        if (heroSection) {
            // CTA buttons scroll
            var buttons = heroSection.querySelectorAll('button');
            for (var j = 0; j < buttons.length; j++) {
                buttons[j].addEventListener('click', function () {
                    var target = this.textContent.includes('View Our Work') ? '#portfolio' : '#contact';
                    var element = document.querySelector(target);
                    if (element) element.scrollIntoView({ behavior: 'smooth' });
                });
            }

            // Parallax effect
            var backgroundImage = heroSection.querySelector('img');
            if (backgroundImage) {
                window.addEventListener('scroll', function () {
                    var scrolled = window.pageYOffset;
                    if (scrolled < heroSection.offsetHeight) {
                        backgroundImage.style.transform = 'translateY(' + (scrolled * 0.5) + 'px)';
                    }
                });
            }

            // Intersection Observer for animations
            var observer = new IntersectionObserver(function (entries) {
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
    }

    // About Section Animations
    function initAboutSection() {
        // Intersection Observer for animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-fade-in-up');
                }
            });
        }, observerOptions);

        // Observe about section elements
        const aboutElements = document.querySelectorAll('#about h2, #about h3, #about .grid > div, #about .space-y-4 > div');
        aboutElements.forEach(el => observer.observe(el));

        // Counter animation for stats
        const counters = document.querySelectorAll('#about .text-3xl');
        counters.forEach(counter => {
            const target = parseInt(counter.textContent);
            if (!isNaN(target)) {
                let current = 0;
                const increment = target / 50;
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        counter.textContent = target + '+';
                        clearInterval(timer);
                    } else {
                        counter.textContent = Math.floor(current) + '+';
                    }
                }, 30);
            }
        });
    }

    // Services Section Management
    function initServicesSection() {
        const modal = document.getElementById('service-modal');
        const modalTitle = document.getElementById('modal-title');
        const modalContent = document.getElementById('modal-content');
        const closeModalBtn = document.getElementById('close-modal');
        const closeModalBtnBottom = document.getElementById('close-modal-btn');
        const servicesGrid = document.getElementById('services-grid');

        if (!servicesGrid) return;

        // Load services from JSON file
        fetch('/assets/data/services-data.json')
            .then(response => response.json())
            .then(data => {
                // Render services
                servicesGrid.innerHTML = data.services.map(service => `
                    <article class="bg-gray-50 rounded-lg overflow-hidden hover:shadow-lg transition-shadow duration-300">
                        <div class="p-6">
                            <h3 class="text-xl font-semibold text-gray-900 mb-3">${service.title}</h3>
                            <ul class="space-y-2 text-l text-gray-600 mb-6">
                                ${service.items.map(item => `<li>• ${item}</li>`).join('')}
                            </ul>
                            <button
                                class="w-full ${service.buttonClass} text-white py-2 px-4 rounded-lg font-medium transition-colors duration-300"
                                data-service-id="${service.id}">
                                ${service.buttonText}
                            </button>
                        </div>
                    </article>
                `).join('');

                // Add event listeners to the newly created buttons
                document.querySelectorAll('#services-grid button').forEach(button => {
                    button.addEventListener('click', function () {
                        const serviceId = this.getAttribute('data-service-id');
                        const service = data.services.find(s => s.id === serviceId);
                        if (service) {
                            openModal(service.modalContent.title, service.modalContent.content);
                        }
                    });
                });
            })
            .catch(error => {
                console.error('Error loading services data:', error);
                servicesGrid.innerHTML = '<p class="text-center text-red-500">Failed to load services. Please try again later.</p>';
            });

        function openModal(title, content) {
            if (modal && modalTitle && modalContent) {
                modalTitle.textContent = title;
                modalContent.innerHTML = content;
                modal.classList.remove('hidden');
                modal.setAttribute('aria-hidden', 'false');
                document.body.style.overflow = 'hidden';

                // Focus trap
                if (closeModalBtn) closeModalBtn.focus();
            }
        }

        function closeModal() {
            if (modal) {
                modal.classList.add('hidden');
                modal.setAttribute('aria-hidden', 'true');
                document.body.style.overflow = '';
            }
        }

        // Modal event listeners
        if (closeModalBtn) {
            closeModalBtn.addEventListener('click', closeModal);
        }
        if (closeModalBtnBottom) {
            closeModalBtnBottom.addEventListener('click', closeModal);
        }

        // Close modal on outside click
        if (modal) {
            modal.addEventListener('click', function (e) {
                if (e.target === modal) {
                    closeModal();
                }
            });
        }

        // Close modal on escape key
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && modal && !modal.classList.contains('hidden')) {
                closeModal();
            }
        });
    }

    // Portfolio Section Management
    function initPortfolioSection() {
        // Client logos loading
        fetch('/assets/data/client-logos.json')
            .then(response => response.json())
            .then(data => {
                const row = document.getElementById('client-logos-row');
                if (row && data.logos) {
                    row.innerHTML = data.logos.map(filename => {
                        // Alt text from filename
                        const alt = filename.replace(/[-_]/g, ' ').replace(/\.[a-zA-Z0-9]+$/, '').replace(/\b\w/g, l => l.toUpperCase());
                        return `<img src="/assets/images/client-logos/${filename}" alt="${alt}" class="h-16 w-auto object-contain mx-6" loading="lazy">`;
                    }).join('');
                    // Duplicate for seamless scroll
                    row.innerHTML += row.innerHTML;
                }
            })
            .catch(error => console.error('Error loading client logos:', error));

        // Portfolio data loading and filtering
        fetch('/assets/data/portfolio-data.json')
            .then(response => response.json())
            .then(data => {
                // Render portfolio items
                const grid = document.querySelector('#portfolio-grid');
                if (grid) {
                    grid.innerHTML = data.projects.map(project => `
                        <article class="portfolio-item bg-white rounded-lg overflow-hidden shadow-lg hover:shadow-xl transition-shadow duration-300 cursor-pointer"
                                 data-category="${project.category}"
                                 data-project="${project.id}"
                                 tabindex="0"
                                 role="button"
                                 aria-labelledby="project-title-${project.id}">
                            <div class="h-64 overflow-hidden">
                                <img src="${project.image}" alt="${project.alt}" class="w-full h-full object-cover hover:scale-105 transition-transform duration-300" loading="lazy" />
                            </div>
                            <div class="p-6">
                                <div class="flex items-center justify-between mb-2">
                                    <span class="text-xs font-medium ${project.badgeClass} ${project.badgeBg} px-2 py-1 rounded">${project.badge}</span>
                                    <span class="text-xs text-gray-500">${project.year}</span>
                                </div>
                                <h3 id="project-title-${project.id}" class="text-lg font-semibold text-gray-900 mb-2">${project.title}</h3>
                                <p class="text-gray-600 text-sm">${project.description}</p>
                            </div>
                        </article>
                    `).join('');
                }

                // Store project details for modal
                window.projectDetails = data.details;

                // Portfolio filtering
                const filterButtons = document.querySelectorAll('.filter-btn');
                const portfolioItems = document.querySelectorAll('.portfolio-item');

                filterButtons.forEach(button => {
                    button.addEventListener('click', function () {
                        const filter = this.getAttribute('data-filter');

                        // Update active button
                        filterButtons.forEach(btn => btn.classList.remove('active', 'bg-blue-600', 'text-white'));
                        this.classList.add('active', 'bg-blue-600', 'text-white');

                        // Filter items
                        portfolioItems.forEach(item => {
                            if (filter === 'all' || item.getAttribute('data-category') === filter) {
                                item.style.display = 'block';
                                item.classList.add('animate-fade-in-opacity');
                            } else {
                                item.style.display = 'none';
                            }
                        });
                    });
                });

                // Portfolio item click handlers
                portfolioItems.forEach(item => {
                    item.addEventListener('click', function () {
                        const projectId = this.getAttribute('data-project');
                        const projectDetail = window.projectDetails[projectId];
                        if (projectDetail) {
                            openProjectModal(projectDetail);
                        }
                    });

                    // Keyboard accessibility
                    item.addEventListener('keydown', function (e) {
                        if (e.key === 'Enter' || e.key === ' ') {
                            e.preventDefault();
                            this.click();
                        }
                    });
                });
            })
            .catch(error => {
                console.error('Error loading portfolio data:', error);
                const grid = document.querySelector('#portfolio-grid');
                if (grid) {
                    grid.innerHTML = '<p class="text-center text-red-500 col-span-full">Failed to load portfolio. Please try again later.</p>';
                }
            });

        // Project modal management
        const projectModal = document.getElementById('project-modal');
        const projectModalTitle = document.getElementById('project-modal-title');
        const projectModalContent = document.getElementById('project-modal-content');
        const closeProjectModalBtn = document.getElementById('close-project-modal');
        const closeProjectModalBtnBottom = document.getElementById('close-project-modal-btn');

        function openProjectModal(projectDetail) {
            if (projectModal && projectModalTitle && projectModalContent) {
                projectModalTitle.textContent = projectDetail.title;
                projectModalContent.innerHTML = projectDetail.content;
                projectModal.classList.remove('hidden');
                projectModal.setAttribute('aria-hidden', 'false');
                document.body.style.overflow = 'hidden';

                // Focus trap
                if (closeProjectModalBtn) closeProjectModalBtn.focus();
            }
        }

        function closeProjectModal() {
            if (projectModal) {
                projectModal.classList.add('hidden');
                projectModal.setAttribute('aria-hidden', 'true');
                document.body.style.overflow = '';
            }
        }

        // Project modal event listeners
        if (closeProjectModalBtn) {
            closeProjectModalBtn.addEventListener('click', closeProjectModal);
        }
        if (closeProjectModalBtnBottom) {
            closeProjectModalBtnBottom.addEventListener('click', closeProjectModal);
        }

        // Close modal on outside click
        if (projectModal) {
            projectModal.addEventListener('click', function (e) {
                if (e.target === projectModal) {
                    closeProjectModal();
                }
            });
        }

        // Close modal on escape key
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && projectModal && !projectModal.classList.contains('hidden')) {
                closeProjectModal();
            }
        });
    }

    // Initialize all components
    initLoadingAnimation();
    initMobileMenu();
    initHeroSection();
    initAboutSection();
    initServicesSection();
    initPortfolioSection();
});