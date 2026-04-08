import glob

def revert_style(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert style preload for the font-awesome and material icons.
    content = content.replace(
        '''<link as="style" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" onload="this.onload=null;this.rel='stylesheet'" rel="preload"/><noscript><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet"/></noscript>''',
        '''<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet" />'''
    )

    # We should restore style.css to blocking, which we already did in the last revert script.

    # Wait, the huge layout shift on body is likely because of FOUC.
    # What's left that could cause FOUC?
    # AlpineJS is deferred: <script defer="" src="https://cdnjs.cloudflare.com/ajax/libs/alpinejs/3.13.3/cdn.min.js"></script>
    # The header has x-data="mobileMenu" and x-show inside it. When Alpine loads, it processes these directives. Until it loads, elements with `x-show="false"` might be visible or take up space?
    # Yes! `x-show="!isOpen"` and `x-show="isOpen"` are on the SVG icons.
    # Also `x-show="isOpen"` is on the Mobile Navigation Menu `<div class="md:hidden" x-show="isOpen">`.
    # BUT, we have `class="md:hidden"`. In Tailwind, `hidden` on md breakpoints doesn't hide it on mobile. Wait! `md:hidden` means hide on md and larger. So on mobile, it's NOT hidden by Tailwind!
    # Without Alpine loaded, the mobile menu `<div class="md:hidden" x-show="isOpen">` is VISIBLE on mobile!
    # And then Alpine loads and hides it! That causes a massive layout shift on the body.

    # Let's fix this by adding `style="display: none;"` to the mobile menu div.
    content = content.replace('<div @click.away="close" class="md:hidden" x-show="isOpen"', '<div @click.away="close" class="md:hidden" style="display: none;" x-show="isOpen"')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for file in glob.glob('pages/*.html'):
    revert_style(file)
for file in glob.glob('products/*.html'):
    revert_style(file)
revert_style('index.html')
