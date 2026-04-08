import os
import glob

def fix_css(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Preload Critical Assets link might need to be inserted before</head> if not exists, but for now let's just replace style.css
    old_css = '<link rel="stylesheet" href="/assets/styles/style.css">'
    new_css = '<link rel="preload" href="/assets/styles/style.css" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n<noscript><link rel="stylesheet" href="/assets/styles/style.css"></noscript>'

    if old_css in content:
        content = content.replace(old_css, new_css)
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Fixed {file_path}")

for file in glob.glob('pages/*.html'):
    fix_css(file)
