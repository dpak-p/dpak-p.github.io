import re

with open('index.html', 'r') as f:
    content = f.read()

# Make the orbital planets smaller on mobile using Tailwind responsive classes
content = content.replace(
    'class="orbit-planet custom-hover z-20 w-[104px] h-[104px]',
    'class="orbit-planet custom-hover z-20 w-[64px] h-[64px] md:w-[104px] md:h-[104px]'
)
content = content.replace(
    'class="orbit-planet custom-hover z-20 w-[116px] h-[116px]',
    'class="orbit-planet custom-hover z-20 w-[72px] h-[72px] md:w-[116px] md:h-[116px]'
)
content = content.replace(
    'class="orbit-planet custom-hover z-20 w-[100px] h-[100px]',
    'class="orbit-planet custom-hover z-20 w-[60px] h-[60px] md:w-[100px] md:h-[100px]'
)

# Also scale down the text inside them for mobile
content = re.sub(
    r'<span class="text-2xl">([^<]+)</span>\s*<span class="font-bubbly font-bold text-xs',
    r'<span class="text-xl md:text-2xl">\1</span>\n            <span class="font-bubbly font-bold text-[8px] md:text-xs',
    content
)

# The accretion disk is huge on mobile, let's scale it slightly
content = content.replace(
    '<svg aria-hidden="true" class="absolute w-[440px] h-[440px]',
    '<svg aria-hidden="true" class="absolute w-[300px] h-[300px] md:w-[440px] md:h-[440px]'
)

with open('index.html', 'w') as f:
    f.write(content)

print("Orbital scaling applied.")
