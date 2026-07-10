import re

with open('index.html', 'r') as f:
    content = f.read()

# I will add a toggle specifically in the hero section, absolutely positioned top right.
hero_toggle_html = """
    <!-- Hero Theme Toggle (visible before scrolling) -->
    <button id="heroModeToggle" aria-label="Toggle Dark Mode" class="absolute top-6 right-6 z-50 custom-hover w-14 h-7 rounded-full bg-slate-200 dark:bg-slate-800 p-1 flex items-center transition-all duration-300 shadow-inner border border-black/5 dark:border-white/5 opacity-80 hover:opacity-100 md:hidden">
        <div id="heroToggleKnob" class="w-5 h-5 rounded-full bg-researchCyan dark:bg-neonPurple shadow-md transform transition-transform duration-300 flex items-center justify-center">
            <svg id="heroSunIcon" class="w-3 h-3 text-white hidden" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd"/></svg>
            <svg id="heroMoonIcon" class="w-3 h-3 text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
        </div>
    </button>

    <button id="heroModeToggleDesktop" aria-label="Toggle Dark Mode" class="hidden md:flex absolute top-6 right-16 z-50 custom-hover w-16 h-8 rounded-full bg-slate-200 dark:bg-slate-800 p-1 items-center transition-all duration-300 shadow-inner border border-black/5 dark:border-white/5 opacity-60 hover:opacity-100">
        <div id="heroToggleKnobDesktop" class="w-6 h-6 rounded-full bg-researchCyan dark:bg-neonPurple shadow-md transform transition-transform duration-300 flex items-center justify-center">
            <svg id="heroSunIconDesktop" class="w-3.5 h-3.5 text-white hidden" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" clip-rule="evenodd"/></svg>
            <svg id="heroMoonIconDesktop" class="w-3.5 h-3.5 text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/></svg>
        </div>
    </button>
"""

content = content.replace(
    '<header id="hero" class="relative w-full h-screen flex items-center justify-center overflow-hidden z-10">',
    '<header id="hero" class="relative w-full h-screen flex items-center justify-center overflow-hidden z-10">\n' + hero_toggle_html
)

# Also update the JS to sync both buttons
js_sync_logic = """
    function updateToggle() {
        const isDark = html.classList.contains('dark');

        // Main nav toggle
        toggleKnob.classList.toggle('translate-x-8', isDark);
        moonIcon.classList.toggle('hidden', !isDark);
        sunIcon.classList.toggle('hidden', isDark);

        // Hero toggle mobile
        const heroToggleKnob = document.getElementById('heroToggleKnob');
        if (heroToggleKnob) {
            heroToggleKnob.classList.toggle('translate-x-7', isDark);
            document.getElementById('heroMoonIcon').classList.toggle('hidden', !isDark);
            document.getElementById('heroSunIcon').classList.toggle('hidden', isDark);
        }

        // Hero toggle desktop
        const heroToggleKnobDesktop = document.getElementById('heroToggleKnobDesktop');
        if (heroToggleKnobDesktop) {
            heroToggleKnobDesktop.classList.toggle('translate-x-8', isDark);
            document.getElementById('heroMoonIconDesktop').classList.toggle('hidden', !isDark);
            document.getElementById('heroSunIconDesktop').classList.toggle('hidden', isDark);
        }
    }
    updateToggle();

    function toggleTheme() {
        const isDark = html.classList.contains('dark');
        html.classList.remove(isDark ? 'dark' : 'light');
        html.classList.add(isDark ? 'light' : 'dark');
        localStorage.setItem('theme', isDark ? 'light' : 'dark');
        updateToggle();
    }

    modeToggle.addEventListener('click', toggleTheme);
    document.getElementById('heroModeToggle')?.addEventListener('click', toggleTheme);
    document.getElementById('heroModeToggleDesktop')?.addEventListener('click', toggleTheme);
"""

# replace the old JS
old_js = """    function updateToggle() {
        const isDark = html.classList.contains('dark');
        toggleKnob.classList.toggle('translate-x-8', isDark);
        moonIcon.classList.toggle('hidden', !isDark);
        sunIcon.classList.toggle('hidden', isDark);
    }
    updateToggle();

    modeToggle.addEventListener('click', () => {
        const isDark = html.classList.contains('dark');
        html.classList.remove(isDark ? 'dark' : 'light');
        html.classList.add(isDark ? 'light' : 'dark');
        localStorage.setItem('theme', isDark ? 'light' : 'dark');
        updateToggle();
    });"""

content = content.replace(old_js, js_sync_logic.strip())

with open('index.html', 'w') as f:
    f.write(content)

print("Hero toggle added.")
