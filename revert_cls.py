import glob

def revert(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert the hero image loading="lazy" change as it didn't help (made CLS worse actually, the whole body shifted!)
    # Actually wait, why did the whole body shift? Because maybe Google Fonts display=swap causes it?
    # Or because `assets/styles/style.css` is preloaded?
    # If the main stylesheet is preloaded, the page renders without styles first (FOUC), and then styles snap in! That's a huge layout shift!
    # AHHHH! That's it!
    # In index.html, we had:
    # <link rel="preload" href="/assets/styles/style.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
    # This is standard for NON-CRITICAL CSS. But style.css is the MAIN tailwind stylesheet!
    # If we preload it, the entire page renders unstyled initially.
    # To fix this, we should NOT preload the main stylesheet unless we inline critical CSS.
    # Since we don't have critical CSS inlined, we MUST block rendering with style.css to prevent FOUC and massive CLS!

    # Let's revert the preload of style.css on ALL pages.

    content = content.replace(
        '<link rel="preload" href="/assets/styles/style.css" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n<noscript><link rel="stylesheet" href="/assets/styles/style.css"></noscript>',
        '<link rel="stylesheet" href="/assets/styles/style.css">'
    )
    # Also products css
    content = content.replace(
        '<link rel="preload" href="main.css" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n<noscript><link rel="stylesheet" href="main.css"></noscript>',
        '<link rel="stylesheet" href="main.css">'
    )
    content = content.replace(
        '<link rel="preload" href="main-pi.css" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n<noscript><link rel="stylesheet" href="main-pi.css"></noscript>',
        '<link rel="stylesheet" href="main-pi.css">'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for file in glob.glob('pages/*.html'):
    revert(file)
for file in glob.glob('products/*.html'):
    revert(file)
revert('index.html')
