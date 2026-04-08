import re
import glob

def fix_images(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add width and height to hirawat logo if missing
    content = re.sub(
        r'(<img[^>]*src="[^"]*hirawat-tech-500-logo.webp"[^>]*)(?<!width="\d+”)(?<!height="\d+”)(>)',
        r'\1 width="150" height="40"\2',
        content
    )

    # Add width and height to unsplash images if missing
    content = re.sub(
        r'(<img[^>]*src="https://images.unsplash.com[^"]*"[^>]*)(?<!width="\d+”)(?<!height="\d+”)(>)',
        r'\1 width="1080" height="720"\2',
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed images in {file_path}")

for file in glob.glob('pages/*.html'):
    fix_images(file)
for file in glob.glob('products/*.html'):
    fix_images(file)
fix_images('index.html')
