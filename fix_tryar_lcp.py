def fix_lcp(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The issue is "Caught exception: NO_LCP". Lighthouse cannot find an LCP element, likely because the image is not loading or the iframe is taking over but failing.
    # The logo src is `/assets/images/logos/tryar-logo.png`. Does this file exist?

    # We will add width and height to the logo to make sure it's valid.
    content = content.replace('<img alt="TryAR logo" class="logo" src="/assets/images/logos/tryar-logo.png"/>', '<img alt="TryAR logo" class="logo" src="/assets/images/logos/tryar-logo.png" width="200" height="80"/>')
    # Let's add a text element with some size so LCP can trigger. H1 is already there.

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_lcp('products/tryar.html')
