# Now let's create the body content with Bhavan's information
# but keeping the same theme and structure

body_content_updated = '''
<body class="bg-void text-white">
    <!-- Matrix Background -->
    <canvas class="matrix-bg" id="matrix"></canvas>
    
    <!-- Floating Orbs -->
    <div class="floating-orb w-32 h-32 bg-neon/20 top-20 left-10 animate-pulse"></div>
    <div class="floating-orb w-24 h-24 bg-cyber/20 top-40 right-20 animate-bounce"></div>
    <div class="floating-orb w-16 h-16 bg-electric/20 bottom-40 left-1/4 animate-ping"></div>
    
    <!-- Navigation -->
    <nav class="fixed top-0 w-full z-50 bg-void/80 backdrop-blur-md border-b border-neon/20">
        <div class="container mx-auto px-6 py-4">
            <div class="flex items-center justify-between">
                <div class="text-2xl font-cyber font-bold neon-text text-neon">
                    BHAVAN.SYS
                </div>
                <div class="hidden md:flex space-x-8">
                    <a href="#about" class="hover:text-neon transition-colors">[about]</a>
                    <a href="#skills" class="hover:text-neon transition-colors">[skills]</a>
                    <a href="#projects" class="hover:text-neon transition-colors">[projects]</a>
                    <a href="#experience" class="hover:text-neon transition-colors">[experience]</a>
                    <a href="#contact" class="hover:text-neon transition-colors">[contact]</a>
                </div>
                <div class="md:hidden">
                    <button id="mobile-menu-btn" class="text-neon">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="min-h-screen flex items-center justify-center relative overflow-hidden">
        <div class="container mx-auto px-6 text-center">
            <div class="mb-8">
                <div class="inline-block p-1 rounded-full bg-gradient-to-r from-neon via-electric to-cyber">
                    <img src="3d_effect_photo.png" alt="Bhavan Shankar M" class="w-48 h-48 rounded-full object-cover hologram">
                </div>
            </div>
            
            <div class="space-y-4 mb-8">
                <div class="font-cyber text-sm text-gray-400">
                    <div class="mb-1">$ sudo su bhavan</div>
                    <div class="mb-1">$ whoami</div>
                </div>
                <h1 class="text-6xl md:text-8xl font-black font-cyber neon-text text-transparent bg-clip-text bg-gradient-to-r from-neon via-electric to-cyber leading-tight">
                    BHAVAN
                    <br>
                    SHANKAR M
                </h1>
            </div>
            
            <div class="text-xl md:text-2xl text-gray-300 mb-8 font-display">
                Crafting immersive digital experiences where <span class="text-neon">engineering</span> meets cutting-edge <span class="text-electric">technology</span>.
                <br>
                Specializing in AI-powered applications, interactive web experiences, and machine learning solutions.
            </div>
            
            <div class="flex flex-wrap justify-center gap-4 mb-12">
                <div class="px-4 py-2 border border-neon/30 rounded-full text-neon font-cyber text-sm">
                    Electronics & Communication Engineer
                </div>
                <div class="px-4 py-2 border border-electric/30 rounded-full text-electric font-cyber text-sm">
                    Frontend Developer
                </div>
                <div class="px-4 py-2 border border-cyber/30 rounded-full text-cyber font-cyber text-sm">
                    ML Engineer
                </div>
            </div>
            
            <div class="flex justify-center space-x-6">
                <a href="#projects" class="px-8 py-3 bg-gradient-to-r from-neon to-electric text-black font-bold rounded-full hover:scale-105 transition-transform">
                    View Projects
                </a>
                <a href="#contact" class="px-8 py-3 border border-neon text-neon hover:bg-neon hover:text-black transition-colors rounded-full">
                    Get In Touch
                </a>
            </div>
        </div>
    </section>'''

print("Created hero section successfully")
print("Length so far:", len(updated_html + body_content_updated))