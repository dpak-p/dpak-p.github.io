import re

with open('index.html', 'r') as f:
    content = f.read()

# I want to group the #gallery and #travel sections.
# I'll find where #gallery starts and wrap the rest in a container with a subtle background.
gallery_start = '<section id="gallery"'
contact_start = '<section id="contact"'

parts = content.split(gallery_start)

if len(parts) == 2:
    # Everything before gallery
    before = parts[0]
    rest = gallery_start + parts[1]

    # Everything from gallery up to contact
    contact_parts = rest.split(contact_start)
    if len(contact_parts) == 2:
        personal_sections = contact_parts[0]
        contact_and_footer = contact_start + contact_parts[1]

        # Add the wrapper with a subtle background and remove the border-t on the sections themselves
        # so the transition is smooth.

        # A nice subtle gradient background for the personal section
        # using travelGreen (emerald) and neonPink (pink) very faintly.
        wrapper_start = """
<!-- ════════════════════════════════════════
     PERSONAL SECTION WRAPPER
═════════════════════════════════════════ -->
<div class="relative bg-gradient-to-b from-transparent via-pink-50/30 to-emerald-50/30 dark:via-pink-900/5 dark:to-emerald-900/5 border-t border-black/5 dark:border-white/5">
"""
        wrapper_end = "</div>\n"

        # Remove border-t from gallery and travel sections so the wrapper border handles it
        personal_sections = personal_sections.replace('border-t border-black/5 dark:border-white/5', '')

        # I'll also add a subtle section divider heading to separate it conceptually
        divider = """
    <!-- Subtle Section Divider -->
    <div class="w-full text-center py-12 opacity-50 select-none">
        <div class="inline-flex items-center gap-4">
            <div class="h-px w-16 bg-gradient-to-r from-transparent to-slate-400"></div>
            <span class="font-mono text-[10px] tracking-[0.3em] uppercase text-slate-500">The Canvas Mind</span>
            <div class="h-px w-16 bg-gradient-to-l from-transparent to-slate-400"></div>
        </div>
    </div>
"""

        new_content = before + wrapper_start + divider + personal_sections + wrapper_end + contact_and_footer

        with open('index.html', 'w') as f:
            f.write(new_content)
        print("Personal section wrapper added.")
    else:
        print("Could not find contact section.")
else:
    print("Could not find gallery section.")
