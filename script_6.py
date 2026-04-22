# Continue with Contact section and JavaScript
contact_section = '''
    <!-- Contact Section -->
    <section id="contact" class="py-20 bg-void-light/30">
        <div class="container mx-auto px-6">
            <div class="max-w-4xl mx-auto text-center">
                <h2 class="text-4xl font-bold mb-8 font-cyber neon-text">
                    <span class="text-neon">$</span> initialize_connection()
                </h2>
                
                <p class="text-xl text-gray-300 mb-12">
                    Ready to build something extraordinary together? Let's connect and transform ideas into digital reality.
                </p>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
                    <div class="contact-method hologram border border-neon/30 rounded-lg p-6 bg-void-light/20">
                        <div class="text-3xl mb-4">📧</div>
                        <h3 class="text-xl font-bold text-neon mb-2">Email</h3>
                        <p class="text-gray-400">bhavan9304@gmail.com</p>
                    </div>
                    
                    <div class="contact-method hologram border border-electric/30 rounded-lg p-6 bg-void-light/20">
                        <div class="text-3xl mb-4">🔗</div>
                        <h3 class="text-xl font-bold text-electric mb-2">LinkedIn</h3>
                        <p class="text-gray-400">linkedin.com/in/bhavan-shankar-m-397632254</p>
                    </div>
                    
                    <div class="contact-method hologram border border-cyber/30 rounded-lg p-6 bg-void-light/20">
                        <div class="text-3xl mb-4">📱</div>
                        <h3 class="text-xl font-bold text-cyber mb-2">Phone</h3>
                        <p class="text-gray-400">+91 8778934798</p>
                    </div>
                </div>
                
                <div class="contact-form p-8 rounded-2xl border border-neon/20 bg-void-light/20 hologram">
                    <form class="space-y-6">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <input type="text" placeholder="Your Name" 
                                   class="w-full p-4 bg-void-light/50 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:border-neon focus:outline-none">
                            <input type="email" placeholder="Your Email" 
                                   class="w-full p-4 bg-void-light/50 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:border-neon focus:outline-none">
                        </div>
                        <input type="text" placeholder="Subject" 
                               class="w-full p-4 bg-void-light/50 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:border-neon focus:outline-none">
                        <textarea rows="6" placeholder="Your Message" 
                                  class="w-full p-4 bg-void-light/50 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:border-neon focus:outline-none resize-none"></textarea>
                        <button type="submit" 
                                class="w-full py-4 bg-gradient-to-r from-neon to-electric text-black font-bold rounded-lg hover:scale-105 transition-transform">
                            Send Message
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>
    
    <!-- Footer -->
    <footer class="py-12 border-t border-neon/20">
        <div class="container mx-auto px-6 text-center">
            <div class="text-2xl font-cyber font-bold neon-text text-neon mb-4">
                BHAVAN.SYS
            </div>
            <p class="text-gray-400 mb-6">
                Crafting digital experiences where engineering meets creativity
            </p>
            <div class="flex justify-center space-x-6 text-sm text-gray-400">
                <span>© 2024 Bhavan Shankar M</span>
                <span>•</span>
                <span>All rights reserved</span>
            </div>
        </div>
    </footer>'''

# Add the JavaScript and closing tags
javascript_section = '''
    <script>
        // Matrix Background Effect
        const canvas = document.getElementById('matrix');
        const ctx = canvas.getContext('2d');

        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const matrix = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%^&*()*&^%+-/~{[|`]}";
        const matrixArray = matrix.split("");

        const fontSize = 10;
        const columns = canvas.width / fontSize;

        const drops = [];
        for(let x = 0; x < columns; x++) {
            drops[x] = 1;
        }

        function draw() {
            ctx.fillStyle = 'rgba(10, 10, 15, 0.04)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = '#00ff88';
            ctx.font = fontSize + 'px monospace';

            for(let i = 0; i < drops.length; i++) {
                const text = matrixArray[Math.floor(Math.random() * matrixArray.length)];
                ctx.fillText(text, i * fontSize, drops[i] * fontSize);

                if(drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    drops[i] = 0;
                }
                drops[i]++;
            }
        }

        setInterval(draw, 35);

        // Resize canvas on window resize
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });

        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Mobile menu toggle
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        if (mobileMenuBtn) {
            mobileMenuBtn.addEventListener('click', function() {
                // Add mobile menu functionality here
                console.log('Mobile menu clicked');
            });
        }

        // Add scroll animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe all sections for scroll animations
        document.querySelectorAll('section').forEach(section => {
            section.style.opacity = '0';
            section.style.transform = 'translateY(20px)';
            section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(section);
        });

        // Initialize first section
        document.querySelector('section').style.opacity = '1';
        document.querySelector('section').style.transform = 'translateY(0)';
    </script>
</body>
</html>'''

# Combine all sections
complete_html = updated_html + body_content_updated + about_section + skills_section + projects_section + experience_section + contact_section + javascript_section

print("Complete HTML file created!")
print("Total length:", len(complete_html))

# Save the complete HTML file
with open('updated_portfolio.html', 'w', encoding='utf-8') as file:
    file.write(complete_html)

print("File saved as 'updated_portfolio.html'")
print("✅ Portfolio updated successfully with Bhavan's information while maintaining the cyber theme!")