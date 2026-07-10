import re

with open('index.html', 'r') as f:
    content = f.read()

# Fix CSS for cursor
content = content.replace(
    'body { transition: background-color 0.4s ease, color 0.4s ease; overflow-x: hidden; cursor: none; }',
    'body { transition: background-color 0.4s ease, color 0.4s ease; overflow-x: hidden; }\n        @media (hover: hover) and (pointer: fine) { body, a, button, .custom-hover { cursor: none !important; } }'
)

content = content.replace(
    '/* ── CURSOR ── */\n        #cursor-glow {',
    '/* ── CURSOR ── */\n        @media (hover: none), (pointer: coarse) {\n            #cursor-glow, #cursor-dot { display: none !important; }\n        }\n        #cursor-glow {'
)

content = content.replace(
    'position: absolute; cursor: none;',
    'position: absolute;'
)

# Add aria-label to modeToggle
content = content.replace(
    '<button id="modeToggle" class="custom-hover',
    '<button id="modeToggle" aria-label="Toggle Dark Mode" class="custom-hover'
)

# Add aria-hidden="true" to ALL svgs
content = re.sub(r'<svg([^>]*)>', lambda m: f'<svg aria-hidden="true"{m.group(1)}>' if 'aria-hidden' not in m.group(1) else m.group(0), content)

with open('index.html', 'w') as f:
    f.write(content)

print("Modifications applied successfully.")
