import re

def fix_css(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert preload css on products to block render (avoid FOUC/NO_LCP)
    content = content.replace(
        '''<link as="style" href="main.css" onload="this.onload=null;this.rel='stylesheet'" rel="preload"/>
<noscript><link href="main.css" rel="stylesheet"/></noscript>''',
        '''<link rel="stylesheet" href="main.css" />'''
    )
    content = content.replace(
        '''<link as="style" href="main-pi.css" onload="this.onload=null;this.rel='stylesheet'" rel="preload"/>
<noscript><link href="main-pi.css" rel="stylesheet"/></noscript>''',
        '''<link rel="stylesheet" href="main-pi.css" />'''
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

fix_css('products/tryar.html')
fix_css('products/piwhatsapp.html')
