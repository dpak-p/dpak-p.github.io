import re

with open('index.html', 'r') as f:
    content = f.read()

# Change JS animation logic to use transform instead of left/top for orbiting nodes
# Original JS:
#             node.style.left = tx + 'px';
#             node.style.top  = ty + 'px';
#             node.style.transform = 'translate(-50%,-50%)';
new_js = """
            node.style.transform = `translate3d(${tx}px, ${ty}px, 0) translate(-50%,-50%)`;
"""
content = re.sub(
    r"node\.style\.left = tx \+ 'px';\s*node\.style\.top\s*=\s*ty \+ 'px';\s*node\.style\.transform = 'translate\(-50%,-50%\)';",
    new_js.strip(),
    content
)

# And in CSS we need to make sure nodes start with top:0, left:0 so the translate works right relative to the top left of the screen
# Wait, they are positioned absolute.
# Oh right, top:0; left:0 in orbit-planet CSS
content = content.replace(
    'position: absolute;',
    'position: absolute; top: 0; left: 0;'
)

# We also need to fix cursor animation to use transform
content = re.sub(
    r"cursorDot\.style\.left = e\.clientX \+ 'px';\s*cursorDot\.style\.top\s*=\s*e\.clientY \+ 'px';\s*cursorGlow\.style\.left = e\.clientX \+ 'px';\s*cursorGlow\.style\.top\s*=\s*e\.clientY \+ 'px';",
    "cursorDot.style.transform = `translate3d(${e.clientX}px, ${e.clientY}px, 0) translate(-50%, -50%)`; cursorGlow.style.transform = `translate3d(${e.clientX}px, ${e.clientY}px, 0) translate(-50%, -50%)`;",
    content
)

# And in CSS for cursor
#             transform: translate(-50%, -50%);
content = content.replace(
    'transform: translate(-50%, -50%);',
    'transform: translate3d(-50%, -50%, 0);' # just to initialize, it gets overwritten by js anyway
)

with open('index.html', 'w') as f:
    f.write(content)

print("Performance improvements applied.")
