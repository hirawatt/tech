import os

def fix_fonts(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    old_string = """<link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Alata&family=Material+Symbols+Outlined&display=swap">"""

    new_string = """<link href="https://fonts.googleapis.com/css2?family=Alata&family=Material+Symbols+Outlined&display=swap" rel="stylesheet" media="print" onload="this.media='all'">
    <noscript>
      <link href="https://fonts.googleapis.com/css2?family=Alata&family=Material+Symbols+Outlined&display=swap" rel="stylesheet">
    </noscript>"""

    if old_string in content:
        content = content.replace(old_string, new_string)
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Fixed {file_path}")

fix_fonts("index.html")
