import re
import glob

def fix_cls(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The footer image is still lacking an explicit size according to Lighthouse because it has width="100" and height="30" but CSS has `h-8 w-auto`!
    # The `h-8` is 32px. We should use `height="32"` and `width="107"` (approx 32 * 500/150).
    # And we should REMOVE `w-auto` from the class of that specific image to ensure the width is driven by the attribute! Or just remove both `h-8 w-auto`.
    # Let's just remove the class "h-8 w-auto" and set height="32" width="107".

    # Let's find: class="h-8 w-auto" decoding="async" height="30" loading="lazy" src="/assets/images/logos/hirawat-tech-500-logo.webp" width="100"
    content = content.replace(
        'class="h-8 w-auto" decoding="async" height="30" loading="lazy" src="/assets/images/logos/hirawat-tech-500-logo.webp" width="100"',
        'decoding="async" height="32" loading="lazy" src="/assets/images/logos/hirawat-tech-500-logo.webp" width="107"'
    )
    # Also for the header logo if it has it
    content = content.replace(
        'class="h-8 w-auto mr-2" height="30" src="/assets/images/logos/hirawat-tech-500-logo.webp" width="100"',
        'class="mr-2" height="32" src="/assets/images/logos/hirawat-tech-500-logo.webp" width="107"'
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed CLS completely in {file_path}")

for file in glob.glob('pages/*.html'):
    fix_cls(file)
for file in glob.glob('products/*.html'):
    fix_cls(file)
fix_cls('index.html')
