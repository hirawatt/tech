# Project Structure

## Root Directory
- `index.html` - Main landing page
- `manifest.json` - PWA configuration
- `robots.txt` - Search engine directives
- `sitemap.xml` - SEO sitemap
- `llms.txt` - LLM-specific documentation

## Core Directories

### `/assets/`
Main assets directory with organized subdirectories:

- **`/js/`** - JavaScript files
  - `main.js` - Core application logic and interactions
- **`/styles/`** - CSS stylesheets
  - `style.css` - Custom styles and animations
- **`/data/`** - JSON data files
  - `portfolio-data.json` - Project portfolio data
  - `team.json` - Team member information
  - `testimonials-data.json` - Client testimonials
- **`/icons/`** - Custom SVG icons for services
- **`/client-logos/`** - Client brand logos and images
- **`/img/`** - General images (currently empty)
- Font files and brand assets at root level

### `/pages/`
Static HTML pages:
- `about.html` - Company information
- `contact.html` - Contact form and details
- `pricing.html` - Service pricing
- Legal pages: `privacy.html`, `terms.html`, `cookies.html`, `refund.html`

### `/products/`
Product-specific pages and styles:
- `piwhatsapp.html` - πWhatsApp product page
- `tryar.html` - TryAR product page
- `main.css`, `main-pi.css` - Product-specific styles

### `/test/`
Development and testing files:
- `demo.html`, `coming.html` - Test pages
- Associated CSS files

## File Naming Conventions
- Use lowercase with hyphens for HTML files
- Use camelCase for JavaScript variables and functions
- Use kebab-case for CSS classes
- JSON data files use descriptive names with hyphens

## Data Organization
- Portfolio projects categorized by type: `3d-ar`, `d2c`, `automation`
- Client logos organized by company name
- Structured JSON for dynamic content loading

## Asset Loading Strategy
- Critical CSS and JS loaded in `<head>`
- External dependencies via CDN
- Images optimized with WebP format where possible
- Lazy loading implemented for non-critical assets