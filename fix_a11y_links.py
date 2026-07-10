import re

with open('index.html', 'r') as f:
    content = f.read()

# Make sure all social links without text inside them have aria-labels
social_links = [
    (r'<a href="https://linkedin.com[^>]*>(.*?)</a>', 'LinkedIn', re.DOTALL),
    (r'<a href="https://github.com/dpak-p"[^>]*class="custom-hover flex[^>]*>(.*?)</a>', 'GitHub', re.DOTALL),
    (r'<a href="#" target="_blank" class="custom-hover flex flex-col items-center gap-2 text-slate-400 hover:text-artAmber transition-colors" title="Link updating soon...">(.*?)</a>', 'Scholar', re.DOTALL)
]

for pattern, label, flags in social_links:
    def repl(m):
        full_tag_match = re.search(r'<a\s+[^>]*>', m.group(0))
        if full_tag_match:
            full_tag = full_tag_match.group(0)
            if 'aria-label' not in full_tag:
                new_tag = full_tag.replace('<a ', f'<a aria-label="{label}" ')
                return m.group(0).replace(full_tag, new_tag)
        return m.group(0)

    content = re.sub(pattern, repl, content, flags=flags)

# Fix the theme toggle button just in case we missed it
content = content.replace('<button id="modeToggle"', '<button id="modeToggle" aria-label="Toggle Dark Mode"')

# Specifically fix the timeline button
content = content.replace('<button id="timeline-btn"', '<button id="timeline-btn" aria-label="Toggle Timeline"')

# Specifically fix the pubs button
content = content.replace('<button id="pubs-expander"', '<button id="pubs-expander" aria-label="Toggle Publications"')


with open('index.html', 'w') as f:
    f.write(content)

print("A11y links updated.")
