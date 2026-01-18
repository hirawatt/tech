# HirawatTech Codebase Guidelines for AI Agents

## Project Architecture

**HirawatTech** is a static marketing website for an Indian technology agency. The site is a **progressive web app (PWA)** with no build process—HTML/CSS/JS served directly from the root and `/assets/` directories.

### Key Architectural Decisions
- **Static-first approach**: All content is pre-rendered HTML with dynamic data loaded from JSON files via JavaScript
- **Data-driven design**: Portfolio, services, testimonials, and team data live in `/assets/data/*.json` files—edit these instead of hardcoding HTML
- **Minimal dependencies**: Vanilla JS + Alpine.js for reactivity, Tailwind CSS for styling, external CDNs for libraries (ApexCharts, Three.js)
- **SEO-focused**: Semantic HTML5, schema.org markup, structured meta tags, canonical URLs
## Data Model
## Critical Workflows
### Adding a New Portfolio Project
1. Edit `assets/data/portfolio-data.json` and add to `projects` array
2. Include: `id`, `category` (one of: `3d-ar`, `d2c`, `automation`), `title`, `description`, `year`, `image`, `badge`
3. The HTML section loads this JSON dynamically—no need to edit HTML

### Updating Services Section
1. Modify `assets/data/services-data.json`
2. Each service needs `name`, `description`, `icon` (Font Awesome or Material Symbols class)
3. JS loads and renders these; validate CSS classes exist before committing

### Deploying Changes
- **Local testing**: `python -m http.server 8000` or `npx serve .`
- **No build step required**—all files served as-is
- **Check**: JSON validity, HTML semantics, CSS class availability (Tailwind compiled via CDN)

## Frontend Stack
- **Main logic**: `assets/scripts/main.js` (~462 lines)
- **Event pattern**: Use `document.addEventListener()` with global click/keydown handlers
- **DOMContentLoaded**: All DOM queries wrapped in `DOMContentLoaded` event listener
- **Alpine.js**: Available via CDN; use `x-show`, `x-on:click`, `@click` for interactivity
- **Mobile menu**: Managed via `.hidden` class toggling with `aria-expanded` for accessibility
- **Loading animation**: Overlay hidden after `window.load` event or 5-second timeout fallback

## Development Tips
❌ Hardcoding portfolio/service/team data in HTML instead of JSON
❌ Breaking CSS classes from Tailwind (verify at `cdn.tailwindcss.com`)
❌ Not updating schema.org markup when contact info changes
❌ Ignoring mobile breakpoints in Tailwind classes

✅ Keep data in JSON, logic in JS, presentation in HTML
✅ Test locally with `python -m http.server 8000` before pushing
✅ Validate JSON syntax before committing
✅ Maintain semantic HTML structure for SEO
